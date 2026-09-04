students = [
    ("Amit", 70),
    ("Sneha", 85),
    ("Rahul", 60),
    ("Priya", 90)
]

def average_marks(students):
    total = sum(map(lambda x: x[1], students))
    return total / len(students)

print("Average Marks =", average_marks(students))

above_75 = list(filter(lambda x: x[1] > 75, students))
print("Students above 75 =", above_75)

sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted Students =", sorted_students)
