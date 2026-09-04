employees = [
    ("Amit", 40000),
    ("Rahul", 60000),
    ("Sneha", 50000),
    ("Priya", 45000)
]

employees.sort(key=lambda employee: employee[1])

print("Employees sorted by salary:")
for employee in employees:
    print(employee)
