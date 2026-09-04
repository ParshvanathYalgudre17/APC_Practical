# 19. Student attendance

students = [
    ["Amit", 80, 100],
    ["Priya", 70, 100],
    ["Rahul", 90, 100],
    ["Sneha", 60, 100]
]

print("Attendance below 75%:")

for student in students:
    percentage = (student[1] / student[2]) * 100

    print(student[0], "=", percentage, "%")

    if percentage < 75:
        print("Below 75%")
