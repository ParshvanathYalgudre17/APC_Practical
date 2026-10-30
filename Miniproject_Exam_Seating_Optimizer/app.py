from collections import Counter
from datetime import date
from pathlib import Path
import re
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from data import Store, FIELDS, YEARS
from seating import generate_plan

try:
    from excel_io import read_data, export_data, export_plan
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.ticker import MaxNLocator
except ImportError as error:
    print(f"Missing dependency: {error}\nRun: python -m pip install -r requirements.txt")
    sys.exit(1)

BG = "#F1F4FB"
NAV = "#273D7A"
BLUE = "#4169E1"
TEXT = "#17233D"
MUTED = "#68758E"
WHITE = "#FFFFFF"
LINE = "#DCE3F0"
YEAR_COLORS = {1: "#E4ECFF", 2: "#DDF3EB", 3: "#FFF0D5", 4: "#EEE5FF"}
YEAR_INK = {1: "#315BB8", 2: "#177455", 3: "#956311", 4: "#7049A7"}
LABELS = {"roll_no": "Roll number", "name": "Name", "year": "Year (1 to 4)",
          "division": "Division", "room_no": "Room number", "rows": "Rows",
          "benches_per_row": "Benches per row", "available": "Available (1=yes, 0=no)",
          "code": "Subject code", "staff_id": "Staff ID"}
PAGE_NAMES = {"students": "Students", "rooms": "Classrooms", "subjects": "Subjects",
              "supervisors": "Supervisors"}


def label(parent, text, size=10, bold=False, color=TEXT, bg=None, **kwargs):
    return tk.Label(parent, text=text, font=("Segoe UI", size, "bold" if bold else "normal"),
                    fg=color, bg=bg or parent.cget("bg"), **kwargs)


def card(parent):
    return tk.Frame(parent, bg=WHITE, highlightbackground=LINE, highlightthickness=1)


def scrollable(parent, bg=BG, width=300):
    """Keep dashboard and edit forms usable on smaller laptop screens."""
    outer = tk.Frame(parent, bg=bg)
    canvas = tk.Canvas(outer, bg=bg, width=width, highlightthickness=0)
    scrollbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    inner = tk.Frame(canvas, bg=bg)
    window = canvas.create_window((0, 0), window=inner, anchor="nw")
    inner.bind("<Configure>", lambda _: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda event: canvas.itemconfigure(window, width=event.width))
    return outer, inner


def button(parent, text, command, primary=False, **kwargs):
    return ttk.Button(parent, text=text, command=command,
                      style="Primary.TButton" if primary else "TButton", **kwargs)


def table(parent, columns, widths=None):
    holder = tk.Frame(parent, bg=WHITE)
    holder.pack(fill="both", expand=True)
    tree = ttk.Treeview(holder, columns=list(columns), show="headings", selectmode="browse")
    for i, (key, title) in enumerate(columns.items()):
        tree.heading(key, text=title)
        tree.column(key, width=widths[i] if widths else 130, minwidth=70, anchor="w")
    y = ttk.Scrollbar(holder, orient="vertical", command=tree.yview)
    x = ttk.Scrollbar(holder, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=y.set, xscrollcommand=x.set)
    holder.rowconfigure(0, weight=1)
    holder.columnconfigure(0, weight=1)
    tree.grid(row=0, column=0, sticky="nsew")
    y.grid(row=0, column=1, sticky="ns")
    x.grid(row=1, column=0, sticky="ew")
    tree.tag_configure("even", background="#F5F7FC")
    return tree


class App:
    def __init__(self, root, data_dir=None):
        self.root = root
        self.root.title("Exam Seating Optimizer - CSE Admin")
        width = min(1280, max(1040, self.root.winfo_screenwidth() - 70))
        height = min(850, max(680, self.root.winfo_screenheight() - 100))
        self.root.geometry(f"{width}x{height}")
        self.root.minsize(1040, 680)
        self.root.configure(bg=BG)
        self.store = Store(Path(data_dir or Path(__file__).parent / "data") / "exam_seating.db")
        self.plan = self.store.get_setting("latest_plan")
        self.session = self.store.get_setting("session") or {
            "date": str(date.today()), "start": "10:00", "end": "13:00",
            "years": {str(y): {"included": True, "code": f"CS{y}01"} for y in YEARS}}
        self.chart = None
        self.page = "Home"
        self.configure_style()
        self.build_shell()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.show("Home")

    def configure_style(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(".", font=("Segoe UI", 10))
        style.configure("TButton", padding=(12, 9), background="#E9EEFA", foreground=TEXT,
                        borderwidth=0, focusthickness=0)
        style.map("TButton", background=[("active", "#DBE4FB")])
        style.configure("Primary.TButton", background=BLUE, foreground=WHITE)
        style.map("Primary.TButton", background=[("active", "#3056C5"), ("disabled", "#A8B9E8")])
        style.configure("TEntry", padding=7, fieldbackground=WHITE, bordercolor=LINE)
        style.configure("TCombobox", padding=6, fieldbackground=WHITE, bordercolor=LINE)
        style.map("TCombobox", fieldbackground=[("readonly", WHITE)],
                  selectbackground=[("readonly", WHITE)], selectforeground=[("readonly", TEXT)])
        style.configure("Treeview", rowheight=34, background=WHITE, fieldbackground=WHITE,
                        foreground=TEXT, borderwidth=0)
        style.configure("Treeview.Heading", background="#E9EEF8", foreground=NAV,
                        font=("Segoe UI", 10, "bold"), padding=(8, 10), relief="flat")
        style.map("Treeview", background=[("selected", "#D8E3FF")], foreground=[("selected", TEXT)])
        style.configure("TNotebook", background=WHITE, borderwidth=0)
        style.configure("TNotebook.Tab", padding=(14, 8))

    def build_shell(self):
        sidebar = tk.Frame(self.root, bg=NAV, width=214)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)
        label(sidebar, "EXAM SEATING", 17, True, WHITE).pack(anchor="w", padx=21, pady=(30, 2))
        label(sidebar, "CSE  /  ADMINISTRATOR", 9, color="#BFCFF6").pack(anchor="w", padx=22)
        tk.Frame(sidebar, bg="#465B94", height=1).pack(fill="x", padx=22, pady=26)
        self.nav_buttons = {}
        for name in ("Home", "Students", "Classrooms", "Subjects", "Supervisors", "Seating"):
            b = tk.Button(sidebar, text=name, anchor="w", font=("Segoe UI", 11),
                          bg=NAV, fg=WHITE, activebackground=BLUE, activeforeground=WHITE,
                          relief="flat", bd=0, padx=18, pady=14, cursor="hand2",
                          command=lambda n=name: self.show(n))
            b.pack(fill="x", padx=12, pady=3)
            self.nav_buttons[name] = b
        footer = tk.Frame(sidebar, bg=NAV)
        footer.pack(side="bottom", fill="x", padx=22, pady=24)
        label(footer, "2 seats per bench", 10, True, WHITE).pack(anchor="w")
        label(footer, "Different subjects together", 9, color="#BFCFF6").pack(anchor="w", pady=6)
        self.main = tk.Frame(self.root, bg=BG)
        self.main.pack(side="left", fill="both", expand=True)
        header = tk.Frame(self.main, bg="#E2E9FF", height=108)
        header.pack(fill="x", padx=24, pady=(24, 0))
        header.pack_propagate(False)
        label(header, "Exam Seating Optimizer", 25, True, "#14234A").pack(anchor="w", padx=24, pady=(19, 4))
        label(header, "Computer Science & Engineering   /   First to Fourth Year   /   Divisions A, B, C",
              10, color="#42567D").pack(anchor="w", padx=25)
        self.status = tk.StringVar(value="Ready. Sample names and subjects are editable.")
        tk.Label(self.main, textvariable=self.status, font=("Segoe UI", 9), bg=BG,
                 fg=MUTED, anchor="w").pack(side="bottom", fill="x", padx=25, pady=(3, 10))
        self.content = tk.Frame(self.main, bg=BG)
        self.content.pack(fill="both", expand=True, padx=24, pady=18)

    def show(self, page):
        self.page = page
        self.plan = self.store.get_setting("latest_plan")
        if self.chart:
            self.chart.get_tk_widget().destroy()
            self.chart.figure.clear()
            self.chart = None
        for widget in self.content.winfo_children():
            widget.destroy()
        for name, b in self.nav_buttons.items():
            b.configure(bg=BLUE if name == page else NAV)
        if page == "Home":
            self.home()
        elif page == "Seating":
            self.seating_page()
        else:
            selected_table = next(t for t, n in PAGE_NAMES.items() if n == page)
            self.data_page(selected_table)

    def heading(self, title, subtitle, parent=None):
        parent = parent or self.content
        label(parent, title, 18, True).pack(anchor="w")
        label(parent, subtitle, 10, color=MUTED).pack(anchor="w", pady=(4, 16))

    def home(self):
        scroll, home_body = scrollable(self.content)
        scroll.pack(fill="both", expand=True)
        self.heading("Admin dashboard", "Manage exam data, choose one paper per year, then generate the seating plan.", home_body)
        students, rooms, staff = [self.store.all(t) for t in ("students", "rooms", "supervisors")]
        active_rooms = [r for r in rooms if r["available"]]
        metrics = tk.Frame(home_body, bg=BG)
        metrics.pack(fill="x", pady=(0, 16))
        entries = [(len(students), "Students"), (len(active_rooms), "Available rooms"),
                   (sum(s["available"] for s in staff), "Available supervisors"),
                   (self.plan["student_count"] if self.plan else 0, "Students seated")]
        for i, (value, title) in enumerate(entries):
            metrics.columnconfigure(i, weight=1, uniform="metric")
            c = card(metrics)
            c.grid(row=0, column=i, sticky="ew", padx=(0 if i == 0 else 7, 0 if i == 3 else 7))
            label(c, str(value), 25, True, BLUE).pack(anchor="w", padx=18, pady=(14, 3))
            label(c, title, 10, color=MUTED).pack(anchor="w", padx=18, pady=(0, 16))
        center = tk.Frame(home_body, bg=BG)
        center.pack(fill="x", pady=(0, 16))
        setup = card(center)
        setup.pack(side="left", fill="both", expand=True, padx=(0, 14))
        label(setup, "Exam setup", 14, True).pack(anchor="w", padx=20, pady=(16, 12))
        info = [("Department", "CSE only"), ("Divisions", "A, B and C in each year"),
                ("Available capacity", f"{sum(r['rows'] * r['benches_per_row'] * 2 for r in active_rooms)} seats"),
                ("Seating rule", "Different subjects on a shared bench")]
        for name, value in info:
            line = tk.Frame(setup, bg=WHITE)
            line.pack(fill="x", padx=20, pady=5)
            label(line, name, color=MUTED, width=18, anchor="w").pack(side="left")
            label(line, value, bold=name == "Seating rule", anchor="w").pack(side="left")
        label(setup, "Sample subjects for now. Update them after uploading your syllabus.",
              9, color="#94651D", wraplength=460, justify="left").pack(anchor="w", padx=20, pady=15)
        actions = card(center)
        actions.pack(side="right", fill="both")
        label(actions, "Quick actions", 14, True).pack(anchor="w", padx=20, pady=(16, 12))
        for text, command, primary in [("Generate seating", lambda: self.show("Seating"), True),
                                        ("Import Excel data", self.import_excel, False),
                                        ("Export current data", self.export_excel, False)]:
            button(actions, text, command, primary, width=25).pack(fill="x", padx=20, pady=5)
        tk.Frame(actions, bg=WHITE, height=12).pack()
        chart_card = card(home_body)
        chart_card.configure(height=280)
        chart_card.pack(fill="x", pady=(0, 8))
        chart_card.pack_propagate(False)
        label(chart_card, "Students by year", 14, True).pack(anchor="w", padx=20, pady=(14, 2))
        counts = Counter(s["year"] for s in students)
        fig = Figure(figsize=(7.5, 2.5), dpi=100, facecolor=WHITE)
        ax = fig.add_subplot(111)
        values = [counts[y] for y in YEARS]
        bars = ax.bar(list(YEARS.values()), values, width=.48,
                      color=["#5376DF", "#41A58A", "#D8A44A", "#9875C8"])
        ax.set_ylim(0, max(values + [1]) * 1.25)
        ax.bar_label(bars, padding=6, color=TEXT, fontsize=10)
        ax.set_ylabel("Students", color=MUTED, fontsize=9)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.spines["bottom"].set_color(LINE)
        ax.tick_params(axis="both", length=0, labelcolor=MUTED, labelsize=9)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_axisbelow(True)
        ax.grid(axis="y", color="#EDF1F8")
        fig.tight_layout(pad=1.5)
        self.chart = FigureCanvasTkAgg(fig, master=chart_card)
        self.chart.draw()
        self.chart.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=(0, 8))

    def data_page(self, selected_table):
        notes = {"students": "CSE roll numbers: CSE1A001, CSE2B001, CSE3C001. Select a row to edit.",
                 "rooms": "Room numbers start at 301. Capacity = rows x benches per row x 2.",
                 "subjects": "Sample subjects. Add syllabus papers here; choose the exam paper on the Seating page.",
                 "supervisors": "Fictional sample staff. Each used room receives one different available supervisor."}
        self.heading(PAGE_NAMES[selected_table], notes[selected_table])
        toolbar = tk.Frame(self.content, bg=BG)
        toolbar.pack(fill="x", pady=(0, 12))
        search = tk.StringVar()
        regex = tk.BooleanVar(value=False)
        label(toolbar, "Search").pack(side="left", padx=(0, 7))
        ttk.Entry(toolbar, textvariable=search, width=22).pack(side="left")
        tk.Checkbutton(toolbar, text="Regex", variable=regex, bg=BG, fg=MUTED,
                       activebackground=BG).pack(side="left", padx=7)
        year_filter, div_filter = tk.StringVar(value="All years"), tk.StringVar(value="All divisions")
        if selected_table in ("students", "subjects"):
            ttk.Combobox(toolbar, textvariable=year_filter, values=("All years", "1", "2", "3", "4"),
                         state="readonly", width=10).pack(side="left", padx=4)
        if selected_table == "students":
            ttk.Combobox(toolbar, textvariable=div_filter, values=("All divisions", "A", "B", "C"),
                         state="readonly", width=12).pack(side="left", padx=4)
        button(toolbar, "Import Excel", self.import_excel).pack(side="right")
        body = tk.Frame(self.content, bg=BG)
        body.pack(fill="both", expand=True)
        form_outer, form = scrollable(body, bg=WHITE, width=275)
        form_outer.pack(side="right", fill="y", padx=(14, 0))
        label(form, "Record details", 13, True).pack(anchor="w", padx=16, pady=(16, 6))
        form_status = label(form, "New record", 9, color=MUTED)
        form_status.pack(anchor="w", padx=16, pady=(0, 5))
        variables, widgets = {}, {}
        fields = FIELDS[selected_table]
        editing = [False]
        for field in fields:
            label(form, LABELS[field], 9, color=MUTED).pack(anchor="w", padx=16, pady=(10, 4))
            var = tk.StringVar()
            variables[field] = var
            options = {"year": ("1", "2", "3", "4"), "division": ("A", "B", "C"), "available": ("1", "0")}
            if field in options:
                widget = ttk.Combobox(form, textvariable=var, values=options[field], state="readonly", width=24)
            else:
                widget = ttk.Entry(form, textvariable=var, width=26)
            widget.pack(fill="x", padx=16)
            widgets[field] = widget
        list_card = card(body)
        list_card.pack(side="left", fill="both", expand=True)
        count_label = label(list_card, "", 9, color=MUTED)
        count_label.pack(anchor="w", padx=12, pady=10)
        columns = {f: LABELS[f] for f in fields}
        if selected_table == "rooms":
            columns["capacity"] = "Capacity"
        tree = table(list_card, columns, [170 if f == "name" else 120 for f in columns])

        def refresh(*_):
            tree.delete(*tree.get_children())
            query = search.get().strip()
            try:
                pattern = re.compile(query if regex.get() else re.escape(query), re.IGNORECASE)
            except re.error:
                count_label.configure(text="Invalid regular expression", fg="#B13D3D")
                return
            records = self.store.all(selected_table)
            found = []
            for r in records:
                if year_filter.get() != "All years" and str(r.get("year")) != year_filter.get():
                    continue
                if div_filter.get() != "All divisions" and r.get("division") != div_filter.get():
                    continue
                if pattern.search(" ".join(map(str, r.values()))):
                    found.append(r)
            for i, record in enumerate(found):
                values = [record[f] for f in fields]
                if selected_table == "rooms":
                    values.append(record["rows"] * record["benches_per_row"] * 2)
                tree.insert("", "end", iid=str(record[fields[0]]), values=values,
                            tags=("even",) if i % 2 == 0 else ())
            count_label.configure(text=f"{len(found)} of {len(records)} records", fg=MUTED)

        def reset():
            editing[0] = False
            widgets[fields[0]].configure(state="normal")
            for f, var in variables.items():
                var.set({"year": "1", "division": "A", "available": "1", "rows": "5", "benches_per_row": "4"}.get(f, ""))
            if tree.selection():
                tree.selection_remove(*tree.selection())
            form_status.configure(text="New record")

        def select(_):
            selected = tree.selection()
            if not selected:
                return
            records = self.store.all(selected_table)
            record = next((r for r in records if str(r[fields[0]]) == selected[0]), None)
            if record:
                for f in fields:
                    variables[f].set(str(record[f]))
                editing[0] = True
                widgets[fields[0]].configure(state="disabled")
                form_status.configure(text="Editing selected record")

        def save():
            try:
                self.store.save(selected_table, {f: v.get() for f, v in variables.items()}, editing[0])
                self.plan = None
                refresh()
                reset()
                self.status.set("Record saved. Generate seating again to use the updated data.")
            except ValueError as error:
                messagebox.showerror("Check record", str(error), parent=self.root)

        def delete():
            if not editing[0]:
                messagebox.showinfo("Select a row", "Select the record to delete.", parent=self.root)
                return
            key = variables[fields[0]].get()
            if messagebox.askyesno("Delete record", f"Delete {key}? The current seating plan will be cleared.", parent=self.root):
                self.store.delete(selected_table, key)
                self.plan = None
                refresh()
                reset()
                self.status.set("Record deleted. Generate seating again.")

        button(form, "Save record", save, True).pack(fill="x", padx=16, pady=(20, 8))
        button(form, "New / clear form", reset).pack(fill="x", padx=16, pady=4)
        button(form, "Delete selected", delete).pack(fill="x", padx=16, pady=4)
        tree.bind("<<TreeviewSelect>>", select)
        for var in (search, regex, year_filter, div_filter):
            var.trace_add("write", refresh)
        reset()
        refresh()

    def seating_page(self):
        self.heading("Generate seating", "Choose one subject per included year. All its A/B/C students take that paper in this session.")
        setup = card(self.content)
        setup.pack(fill="x", pady=(0, 12))
        dates = tk.Frame(setup, bg=WHITE)
        dates.pack(fill="x", padx=16, pady=12)
        self.date_vars = {}
        for key, title, width in (("date", "Date (YYYY-MM-DD)", 13), ("start", "Start", 7), ("end", "End", 7)):
            label(dates, title, 9, color=MUTED).pack(side="left", padx=(0 if key == "date" else 14, 5))
            var = tk.StringVar(value=self.session[key])
            self.date_vars[key] = var
            ttk.Entry(dates, textvariable=var, width=width).pack(side="left")
        button(dates, "Generate seating", self.generate, True).pack(side="right")
        subject_row = tk.Frame(setup, bg=WHITE)
        subject_row.pack(fill="x", padx=12, pady=(0, 14))
        self.year_vars, self.subject_vars = {}, {}
        subjects = self.store.all("subjects")
        for col, (year, title) in enumerate(YEARS.items()):
            subject_row.columnconfigure(col, weight=1, uniform="years")
            frame = tk.Frame(subject_row, bg=WHITE)
            frame.grid(row=0, column=col, sticky="ew", padx=4)
            saved = self.session["years"].get(str(year), {})
            included = tk.BooleanVar(value=saved.get("included", True))
            self.year_vars[year] = included
            tk.Checkbutton(frame, text=title, variable=included, bg=WHITE, fg=TEXT,
                           activebackground=WHITE, font=("Segoe UI", 10, "bold")).pack(anchor="w")
            available = [s for s in subjects if s["year"] == year]
            options = [f"{s['code']} | {s['name']}" for s in available]
            selected = next((text for text in options if text.startswith(saved.get("code", "") + " | ")),
                            options[0] if options else "")
            value = tk.StringVar(value=selected)
            self.subject_vars[year] = value
            combo = ttk.Combobox(frame, textvariable=value, values=options, state="readonly", width=21)
            combo.pack(fill="x")
        self.result_holder = card(self.content)
        self.result_holder.pack(fill="both", expand=True)
        self.render_result()
        for var in list(self.date_vars.values()) + list(self.year_vars.values()) + list(self.subject_vars.values()):
            var.trace_add("write", self.session_changed)

    def capture_session(self):
        self.session = {k: v.get() for k, v in self.date_vars.items()}
        self.session["years"] = {str(y): {"included": self.year_vars[y].get(),
            "code": self.subject_vars[y].get().split(" | ", 1)[0]} for y in YEARS}

    def session_changed(self, *_):
        self.capture_session()
        self.store.set_setting("session", self.session)
        if self.plan:
            self.store.clear_plan()
            self.plan = None
            self.render_result()
        self.status.set("Exam settings changed. Click Generate seating.")

    def generate(self):
        self.capture_session()
        choices = {y: self.session["years"][str(y)]["code"] for y in YEARS if self.year_vars[y].get()}
        try:
            plan = generate_plan(self.store.all("students"), self.store.all("rooms"),
                self.store.all("supervisors"), self.store.all("subjects"), choices,
                self.session["date"].strip(), self.session["start"].strip(), self.session["end"].strip())
        except ValueError as error:
            messagebox.showerror("Cannot generate seating", str(error), parent=self.root)
            return
        self.plan = plan
        self.store.set_setting("latest_plan", plan)
        self.store.set_setting("session", self.session)
        self.render_result()
        self.status.set(f"{plan['student_count']} students seated in {len(plan['rooms'])} rooms. "
                        f"{plan['single_benches']} single-occupancy benches. No same-subject bench pairs.")

    def render_result(self):
        for child in self.result_holder.winfo_children():
            child.destroy()
        if not self.plan:
            label(self.result_holder, "Your seating plan will appear here", 17, True).pack(pady=(75, 10))
            label(self.result_holder, "Select the exam subjects above, then click Generate seating.",
                  color=MUTED).pack()
            label(self.result_holder, "Available rooms start at 301. Supervisors are assigned automatically.",
                  9, color=MUTED).pack(pady=10)
            return
        plan = self.plan
        top = tk.Frame(self.result_holder, bg=WHITE)
        top.pack(fill="x", padx=16, pady=12)
        label(top, f"{plan['student_count']} students   /   {len(plan['rooms'])} rooms   /   0 subject conflicts",
              11, True).pack(side="left")
        button(top, "Export seating Excel", self.export_seating, True).pack(side="right")
        bar = tk.Frame(self.result_holder, bg=WHITE)
        bar.pack(fill="x", padx=16, pady=(0, 8))
        label(bar, "Room", 10, True).pack(side="left", padx=(0, 8))
        room_var = tk.StringVar(value=str(plan["rooms"][0]["room_no"]))
        selector = ttk.Combobox(bar, textvariable=room_var, values=[str(r["room_no"]) for r in plan["rooms"]],
                                width=7, state="readonly")
        selector.pack(side="left")
        supervisor_label = label(bar, "", 9, color=MUTED)
        supervisor_label.pack(side="left", padx=16)
        tabs = ttk.Notebook(self.result_holder)
        tabs.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        layout = tk.Frame(tabs, bg=WHITE)
        student_list = tk.Frame(tabs, bg=WHITE)
        tabs.add(layout, text="Classroom layout")
        tabs.add(student_list, text="Student list")
        tree = table(student_list, {"bench": "Bench", "side": "Side", "roll": "Roll number",
            "name": "Name", "year": "Year", "div": "Division", "subject": "Subject"},
            [75, 75, 120, 160, 100, 75, 220])
        canvas_holder = tk.Frame(layout, bg=WHITE)
        canvas_holder.pack(fill="both", expand=True)
        canvas = tk.Canvas(canvas_holder, bg=WHITE, highlightthickness=0)
        sy = ttk.Scrollbar(canvas_holder, orient="vertical", command=canvas.yview)
        sx = ttk.Scrollbar(canvas_holder, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
        canvas_holder.rowconfigure(0, weight=1)
        canvas_holder.columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky="nsew")
        sy.grid(row=0, column=1, sticky="ns")
        sx.grid(row=1, column=0, sticky="ew")

        def draw(*_):
            room_no = int(room_var.get())
            room = next(r for r in plan["rooms"] if r["room_no"] == room_no)
            occupants = [a for a in plan["assignments"] if a["room_no"] == room_no]
            seated = sum(bool(a[s]) for a in occupants for s in ("left", "right"))
            supervisor_label.configure(text=f"Supervisor: {room['supervisor']['name']}   |   {seated} students   |   "
                                            f"{plan['date']}  {plan['start']}-{plan['end']}")
            tree.delete(*tree.get_children())
            row_index = 0
            for a in occupants:
                for side in ("left", "right"):
                    s = a[side]
                    if s:
                        tree.insert("", "end", values=(a["bench"], side.title(), s["roll_no"], s["name"],
                            YEARS[s["year"]], s["division"], s["subject_name"]), tags=("even",) if row_index % 2 == 0 else ())
                        row_index += 1
            canvas.delete("all")
            bench_width, bench_height, gap = 226, 100, 16
            full_width = room["benches_per_row"] * (bench_width + gap) + gap
            canvas.create_rectangle(16, 12, full_width - 16, 43, fill="#E9EEF8", outline="")
            canvas.create_text(full_width / 2, 27, text="FRONT / BLACKBOARD", fill=MUTED, font=("Segoe UI", 9, "bold"))
            by_bench = {a["bench"]: a for a in occupants}
            for index in range(room["rows"] * room["benches_per_row"]):
                row, col = divmod(index, room["benches_per_row"])
                x, y = gap + col * (bench_width + gap), 60 + row * (bench_height + 24)
                canvas.create_text(x + 2, y, text=f"BENCH {index + 1:02}", anchor="nw", fill=MUTED, font=("Segoe UI", 8))
                assignment = by_bench.get(index + 1, {})
                for side_index, side in enumerate(("left", "right")):
                    s = assignment.get(side)
                    left = x + side_index * (bench_width / 2 + 2)
                    fill = YEAR_COLORS[s["year"]] if s else "#F3F5F9"
                    ink = YEAR_INK[s["year"]] if s else MUTED
                    canvas.create_rectangle(left, y + 17, left + bench_width / 2 - 3, y + 100,
                                            fill=fill, outline="#DCE3F0")
                    if s:
                        canvas.create_text(left + 8, y + 27, text=s["roll_no"], anchor="nw", fill=ink,
                                           font=("Segoe UI", 9, "bold"))
                        short_name = s["name"] if len(s["name"]) <= 24 else s["name"][:21] + "..."
                        canvas.create_text(left + 8, y + 47, text=short_name, anchor="nw", width=98,
                                           fill=TEXT, font=("Segoe UI", 8))
                        canvas.create_text(left + 8, y + 82, text=s["subject_code"], anchor="nw", fill=ink,
                                           font=("Segoe UI", 8, "bold"))
                    else:
                        canvas.create_text(left + 53, y + 58, text="EMPTY", fill=MUTED, font=("Segoe UI", 8))
            canvas.configure(scrollregion=(0, 0, full_width, 70 + room["rows"] * (bench_height + 24)))
        selector.bind("<<ComboboxSelected>>", draw)
        legend = tk.Frame(layout, bg=WHITE)
        legend.pack(fill="x", padx=12, pady=8)
        for year, title in YEARS.items():
            label(legend, "  " + title + "  ", 9, color=YEAR_INK[year], bg=YEAR_COLORS[year]).pack(side="left", padx=4)
        label(legend, "Scroll to view all benches", 9, color=MUTED).pack(side="right")
        draw()

    def import_excel(self):
        path = filedialog.askopenfilename(title="Import exam data", filetypes=[("Excel workbook", "*.xlsx")], parent=self.root)
        if not path:
            return
        try:
            records = read_data(path)
            counts = self.store.import_records(records)
        except Exception as error:
            messagebox.showerror("Import failed", f"No records imported.\n\n{error}", parent=self.root)
            return
        self.plan = None
        self.show(self.page)
        result = ", ".join(f"{n} {t}" for t, n in counts.items())
        self.status.set(f"Imported: {result}. Generate seating again.")
        messagebox.showinfo("Import complete", f"Added/updated: {result}.\nOther existing records were kept.", parent=self.root)

    def export_excel(self):
        path = filedialog.asksaveasfilename(title="Export current data", defaultextension=".xlsx",
            initialfile="exam_data.xlsx", filetypes=[("Excel workbook", "*.xlsx")], parent=self.root)
        if path:
            try:
                export_data(self.store, path)
                self.status.set(f"Data exported: {Path(path).name}")
                messagebox.showinfo("Export complete", f"Saved to:\n{path}", parent=self.root)
            except Exception as error:
                messagebox.showerror("Export failed", str(error), parent=self.root)

    def export_seating(self):
        if not self.plan:
            return
        path = filedialog.asksaveasfilename(title="Export seating plan", defaultextension=".xlsx",
            initialfile=f"seating_{self.plan['date']}.xlsx", filetypes=[("Excel workbook", "*.xlsx")], parent=self.root)
        if path:
            try:
                export_plan(self.plan, path)
                self.status.set(f"Seating exported: {Path(path).name}")
                messagebox.showinfo("Export complete", f"Room sheets, supervisor details and student list saved to:\n{path}", parent=self.root)
            except Exception as error:
                messagebox.showerror("Export failed", str(error), parent=self.root)

    def close(self):
        self.store.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    try:
        app = App(root)
    except Exception as error:
        messagebox.showerror("Startup error", str(error), parent=root)
        root.destroy()
        raise
    root.mainloop()
