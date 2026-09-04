employees = [
    ("Amit", "IT", 45000),
    ("Sneha", "HR", 55000),
    ("Rahul", "IT", 70000),
    ("Priya", "Finance", 50000)
]

high_salary = list(filter(lambda x: x[2] > 50000, employees))
print("Employees earning more than 50000:")
print(high_salary)

increased = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))
print("After 10% salary increase:")
print(increased)

sorted_employees = sorted(employees, key=lambda x: x[2])
print("Sorted by salary:")
print(sorted_employees)
