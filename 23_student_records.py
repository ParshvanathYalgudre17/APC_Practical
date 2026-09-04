def grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"

def process_student(name, roll, marks):
    total = sum(marks)
    percentage = total / 5
    return {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade(percentage)
    }

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = []

    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    students.append(process_student(name, roll, marks))

total_percentage = 0
highest = students[0]
lowest = students[0]

for student in students:
    print("\nName:", student["name"])
    print("Roll No:", student["roll"])
    print("Total:", student["total"])
    print("Percentage:", student["percentage"])
    print("Grade:", student["grade"])

    total_percentage += student["percentage"]

    if student["percentage"] > highest["percentage"]:
        highest = student

    if student["percentage"] < lowest["percentage"]:
        lowest = student

print("\nClass Average =", total_percentage / n)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])
