# 17. Student records

import csv

filename = "students.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["RollNo", "Name", "Marks"])
    writer.writerow([101, "Amit", 85])
    writer.writerow([102, "Priya", 92])
    writer.writerow([103, "Rahul", 78])

students = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Marks"] = int(row["Marks"])
        students.append(row)

print("All Records:")
for student in students:
    print(student["RollNo"], student["Name"], student["Marks"])

highest = students[0]
total = 0

print("\nStudents scoring more than 80:")
for student in students:
    total += student["Marks"]

    if student["Marks"] > highest["Marks"]:
        highest = student

    if student["Marks"] > 80:
        print(student["Name"])

average = total / len(students)

print("\nHighest Scorer =", highest["Name"])
print("Highest Marks =", highest["Marks"])
print("Average Marks =", average)
