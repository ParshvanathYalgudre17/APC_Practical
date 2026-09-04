# 18. Employee records using functions

employees = [
    [101, "Amit", "IT", 50000],
    [102, "Priya", "HR", 60000],
    [103, "Rahul", "Sales", 45000]
]

def display_employees():
    for employee in employees:
        print(employee)

def highest_paid():
    high = employees[0]

    for employee in employees:
        if employee[3] > high[3]:
            high = employee

    return high

def average_salary():
    total = 0

    for employee in employees:
        total += employee[3]

    return total / len(employees)

def above_salary(amount):
    for employee in employees:
        if employee[3] > amount:
            print(employee)

print("All Employees:")
display_employees()

high = highest_paid()
print("\nHighest Paid Employee:", high)

print("Average Salary =", average_salary())

salary = float(input("\nEnter salary limit: "))
print("Employees earning above", salary, ":")
above_salary(salary)
