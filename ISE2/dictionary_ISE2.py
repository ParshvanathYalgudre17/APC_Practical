students = {
    "Rahul": 85,
    "Priya": 95,
    "Amit": 78,
    "Sneha": 92,
    "Rohan": 88
}

# Display student marks
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Find the topper
topper = max(students, key=students.get)
print("\nTopper:", topper)
print("Topper Marks:", students[topper])

# Calculate average marks
average = sum(students.values()) / len(students)
print("Average Marks:", average)
