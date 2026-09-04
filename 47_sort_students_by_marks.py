students = [
    ("Amit", 75),
    ("Rahul", 60),
    ("Sneha", 90),
    ("Priya", 80)
]

students.sort(key=lambda student: student[1])

print("Students sorted by marks:")
for student in students:
    print(student)
