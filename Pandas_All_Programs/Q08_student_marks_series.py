import pandas as pd

marks = {"Amit": 85, "Sneha": 72, "Rahul": 90, "Priya": 65, "Neha": 80}
s = pd.Series(marks)

print("Student Marks:")
print(s)
print("\nMarks of Sneha:")
print(s["Sneha"])
print("\nMaximum Marks:", s.max())
print("Minimum Marks:", s.min())
print("Average Marks:", s.mean())
print("\nStudents Scoring Above 75:")
print(s[s > 75])
