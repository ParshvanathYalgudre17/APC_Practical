"""Two seats per bench. A shared bench never contains the same subject."""
from collections import defaultdict
from datetime import datetime
import heapq
import random
import re

from data import subject_key


def validate_session(date, start, end):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", date):
        raise ValueError("Exam date must use YYYY-MM-DD.")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError as error:
        raise ValueError("Enter a valid calendar date.") from error
    for time in (start, end):
        if not re.fullmatch(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]", time):
            raise ValueError("Use 24-hour time, for example 10:00 or 14:30.")
    if start >= end:
        raise ValueError("End time must be later than start time on the same day.")


def generate_plan(students, rooms, supervisors, subjects, choices,
                  date, start, end, seed=None):
    """choices maps each included year to one subject code for this session.

    Pair the two largest remaining subject groups. This achieves the minimum
    number of benches: max(ceil(student_count / 2), largest_subject_group).
    Leftover students sit alone instead of breaking the subject rule.
    """
    validate_session(date, start, end)
    choices = {int(year): code for year, code in choices.items()}
    if not choices:
        raise ValueError("Select at least one year and its exam subject.")
    catalog = {s["code"]: s for s in subjects}
    for year, code in choices.items():
        if code not in catalog or catalog[code]["year"] != year:
            raise ValueError(f"Choose a valid subject for year {year}.")
    rng = random.Random(seed)
    groups = defaultdict(list)
    rolls = set()
    for student in students:
        if student["year"] not in choices:
            continue
        if student["roll_no"] in rolls:
            raise ValueError("Duplicate student roll number.")
        rolls.add(student["roll_no"])
        subject = catalog[choices[student["year"]]]
        occupant = dict(student, subject_code=subject["code"], subject_name=subject["name"])
        groups[subject_key(subject["name"])].append(occupant)
    if not rolls:
        raise ValueError("There are no students in the selected years.")
    needed = max((len(rolls) + 1) // 2, max(map(len, groups.values())))
    active_rooms = sorted([dict(r) for r in rooms if r["available"]], key=lambda r: r["room_no"])
    capacity = sum(r["rows"] * r["benches_per_row"] for r in active_rooms)
    if capacity < needed:
        raise ValueError(f"Need {needed} benches to keep subjects apart; only {capacity} are available. "
                         "Add rooms or include another year's different-subject exam.")
    for group in groups.values():
        rng.shuffle(group)
    keys = list(groups)
    rng.shuffle(keys)
    heap = [(-len(groups[key]), index, key) for index, key in enumerate(keys)]
    heapq.heapify(heap)
    pairs = []
    while len(heap) >= 2:
        count1, order1, key1 = heapq.heappop(heap)
        count2, order2, key2 = heapq.heappop(heap)
        pair = [groups[key1].pop(), groups[key2].pop()]
        rng.shuffle(pair)
        pairs.append(pair)
        if count1 + 1:
            heapq.heappush(heap, (count1 + 1, order1, key1))
        if count2 + 1:
            heapq.heappush(heap, (count2 + 1, order2, key2))
    if heap:
        _, _, key = heap[0]
        pairs.extend([[student, None] for student in groups[key]])
    rng.shuffle(pairs)
    used_rooms, remaining = [], len(pairs)
    for room in active_rooms:
        if remaining <= 0:
            break
        used_rooms.append(room)
        remaining -= room["rows"] * room["benches_per_row"]
    staff = [dict(s) for s in supervisors if s["available"]]
    if len(staff) < len(used_rooms):
        raise ValueError(f"Need {len(used_rooms)} available supervisors, one per room; have {len(staff)}.")
    rng.shuffle(staff)
    assignments, offset = [], 0
    for room, supervisor in zip(used_rooms, staff):
        room["supervisor"] = supervisor
        count = room["rows"] * room["benches_per_row"]
        for index, pair in enumerate(pairs[offset:offset + count]):
            assignments.append(dict(room_no=room["room_no"], bench=index + 1,
                row=index // room["benches_per_row"] + 1,
                column=index % room["benches_per_row"] + 1,
                left=pair[0], right=pair[1]))
        offset += count
    return dict(date=date, start=start, end=end, choices=choices, rooms=used_rooms,
                assignments=assignments, student_count=len(rolls),
                benches_used=len(pairs), single_benches=sum(p[1] is None for p in pairs),
                generated_at=datetime.now().isoformat(timespec="seconds"))
