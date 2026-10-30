"""Small SQLite data layer, sample records and regular-expression validation."""
from pathlib import Path
import json
import random
import re
import sqlite3

YEARS = {1: "First Year", 2: "Second Year", 3: "Third Year", 4: "Fourth Year"}
FIELDS = {
    "students": ("roll_no", "name", "year", "division"),
    "rooms": ("room_no", "rows", "benches_per_row", "available"),
    "subjects": ("code", "name", "year"),
    "supervisors": ("staff_id", "name", "available"),
}


def subject_key(name):
    """Compare names without case, spaces or punctuation, even across years."""
    return re.sub(r"[\W_]+", "", name.casefold())


def integer(value, label, low, high):
    text = str(value).strip()
    if not re.fullmatch(r"[0-9]+", text) or not low <= int(text) <= high:
        raise ValueError(f"{label} must be a whole number from {low} to {high}.")
    return int(text)


def validate(table, values):
    if table not in FIELDS:
        raise ValueError("Unknown data table.")
    d = {k: str(values.get(k, "")).strip() for k in FIELDS[table]}
    if table in ("students", "subjects"):
        d["year"] = integer(d["year"], "Year", 1, 4)
    if table in ("students", "supervisors"):
        if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]{1,59}", d["name"]):
            raise ValueError("Name: use 2-60 English letters, spaces, dots, hyphens or apostrophes.")
    if table == "students":
        d["roll_no"] = d["roll_no"].upper()
        d["division"] = d["division"].upper()
        if d["division"] not in ("A", "B", "C"):
            raise ValueError("Division must be A, B or C.")
        match = re.fullmatch(r"CSE([1-4])([ABC])([0-9]{3})", d["roll_no"])
        if not match or int(match[3]) == 0:
            raise ValueError("Roll number example: CSE1A001 (001-999).")
        if int(match[1]) != d["year"] or match[2] != d["division"]:
            raise ValueError("Roll number must match the selected year and division.")
    elif table == "rooms":
        d["room_no"] = integer(d["room_no"], "Room number", 301, 9999)
        d["rows"] = integer(d["rows"], "Rows", 1, 20)
        d["benches_per_row"] = integer(d["benches_per_row"], "Benches per row", 1, 10)
    elif table == "subjects":
        d["code"] = d["code"].upper()
        if not re.fullmatch(r"[A-Z][A-Z0-9-]{1,14}", d["code"]):
            raise ValueError("Subject code: 2-15 letters, digits or hyphens; start with a letter.")
        if not 2 <= len(d["name"]) <= 80 or not subject_key(d["name"]):
            raise ValueError("Subject name must contain 2-80 characters, including letters or digits.")
        if d["name"][0] in "=+-@":
            raise ValueError("Start the subject name with a letter or digit.")
    elif table == "supervisors":
        d["staff_id"] = d["staff_id"].upper()
        if not re.fullmatch(r"S[0-9]{3}", d["staff_id"]):
            raise ValueError("Staff ID example: S001.")
    if "available" in d:
        d["available"] = integer(d["available"], "Available (1=yes, 0=no)", 0, 1)
    return d


def sample_data():
    """Repeatable fictional names; 20 students in each of 12 divisions."""
    rng = random.Random(301)
    first = ["Aarav", "Aditi", "Atharva", "Ananya", "Pratik", "Sneha", "Soham",
             "Sakshi", "Omkar", "Prachi", "Rohan", "Neha", "Yash", "Isha", "Vedant",
             "Riya", "Siddharth", "Pooja", "Aditya", "Tanvi", "Shreyas", "Sanika",
             "Nikhil", "Shruti", "Kunal", "Mitali", "Sahil", "Vaishnavi", "Rohit", "Anushka"]
    last = ["Patil", "Jadhav", "Shinde", "Pawar", "Deshmukh", "Kulkarni", "More",
            "Joshi", "Chavan", "Kadam", "Salunkhe", "Bhosale", "Mane", "Sawant"]
    names = [f"{f} {s}" for f in first for s in last]
    rng.shuffle(names)
    data = {t: [] for t in FIELDS}
    for year in YEARS:
        for division in "ABC":
            for number in range(1, 21):
                data["students"].append(dict(roll_no=f"CSE{year}{division}{number:03}",
                    name=names.pop(), year=year, division=division))
    data["rooms"] = [dict(room_no=i, rows=5, benches_per_row=4, available=1)
                     for i in range(301, 307)]
    courses = {
        1: [("CS101", "Programming in C"), ("MA101", "Engineering Mathematics I"),
            ("PH101", "Engineering Physics")],
        2: [("CS201", "Data Structures"), ("CS202", "Database Management Systems"),
            ("CS203", "Object Oriented Programming")],
        3: [("CS301", "Operating Systems"), ("CS302", "Computer Networks"),
            ("CS303", "Software Engineering")],
        4: [("CS401", "Cloud Computing"), ("CS402", "Artificial Intelligence"),
            ("CS403", "Information Security")],
    }
    for year, subjects in courses.items():
        for code, name in subjects:
            data["subjects"].append(dict(code=code, name=name, year=year))
    for i in range(1, 9):
        data["supervisors"].append(dict(staff_id=f"S{i:03}", name=names.pop(), available=1))
    return data


class Store:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(self.path))
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS students (
                roll_no TEXT PRIMARY KEY, name TEXT NOT NULL,
                year INTEGER NOT NULL, division TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS rooms (
                room_no INTEGER PRIMARY KEY, rows INTEGER NOT NULL,
                benches_per_row INTEGER NOT NULL, available INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS subjects (
                code TEXT PRIMARY KEY, name TEXT NOT NULL, year INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS supervisors (
                staff_id TEXT PRIMARY KEY, name TEXT NOT NULL, available INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        """)
        if self.get_setting("initialized") is None:
            self.import_records(sample_data())
            self.set_setting("initialized", True)

    def all(self, table):
        if table not in FIELDS:
            raise ValueError("Unknown table.")
        order = "year, division, roll_no" if table == "students" else FIELDS[table][0]
        return [dict(r) for r in self.db.execute(f"SELECT * FROM {table} ORDER BY {order}")]

    def get_setting(self, key):
        row = self.db.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def set_setting(self, key, value):
        with self.db:
            self.db.execute("INSERT OR REPLACE INTO settings VALUES (?,?)", (key, json.dumps(value)))

    def _clear_plan(self):
        self.db.execute("DELETE FROM settings WHERE key='latest_plan'")

    def clear_plan(self):
        with self.db:
            self._clear_plan()

    def _write(self, table, record):
        columns = FIELDS[table]
        slots = ",".join("?" for _ in columns)
        self.db.execute(f"INSERT OR REPLACE INTO {table} ({','.join(columns)}) VALUES ({slots})",
                        [record[k] for k in columns])

    def _check_subjects(self, records):
        seen = set()
        for r in records:
            key = (r["year"], subject_key(r["name"]))
            if key in seen:
                raise ValueError(f"Duplicate subject name for year {r['year']}: {r['name']}")
            seen.add(key)

    def save(self, table, values, editing=False):
        record = validate(table, values)
        primary = FIELDS[table][0]
        exists = self.db.execute(f"SELECT 1 FROM {table} WHERE {primary}=?",
                                 (record[primary],)).fetchone()
        if exists and not editing:
            raise ValueError(f"{record[primary]} already exists. Select its row to edit it.")
        if editing and not exists:
            raise ValueError("This record no longer exists. Refresh and try again.")
        if table == "subjects":
            self._check_subjects([r for r in self.all(table) if r[primary] != record[primary]] + [record])
        with self.db:
            self._write(table, record)
            self._clear_plan()

    def delete(self, table, key):
        if table not in FIELDS:
            raise ValueError("Unknown table.")
        with self.db:
            self.db.execute(f"DELETE FROM {table} WHERE {FIELDS[table][0]}=?", (key,))
            self._clear_plan()

    def import_records(self, batches):
        """Validate all rows before an atomic merge; no partly imported workbook."""
        cleaned = {}
        for table, rows in batches.items():
            if table not in FIELDS:
                raise ValueError(f"Unknown sheet: {table}")
            cleaned[table], seen = [], set()
            for row_number, row in enumerate(rows, start=2):
                try:
                    record = validate(table, row)
                    key = record[FIELDS[table][0]]
                    if key in seen:
                        raise ValueError(f"Duplicate ID: {key}")
                    seen.add(key)
                    cleaned[table].append(record)
                except ValueError as error:
                    raise ValueError(f"{table}, row {row_number}: {error}") from error
        if "subjects" in cleaned:
            merged = {r["code"]: r for r in self.all("subjects")}
            merged.update({r["code"]: r for r in cleaned["subjects"]})
            self._check_subjects(merged.values())
        with self.db:
            for table, rows in cleaned.items():
                for row in rows:
                    self._write(table, row)
            self._clear_plan()
        return {table: len(rows) for table, rows in cleaned.items()}

    def close(self):
        self.db.close()
