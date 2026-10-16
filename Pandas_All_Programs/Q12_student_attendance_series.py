import pandas as pd

attendance = {"Amit": 85, "Sneha": 70, "Rahul": 95, "Priya": 60, "Neha": 92}
s = pd.Series(attendance)

print("Student Attendance:")
print(s)
print("\nAverage Attendance:", s.mean())
print("\nAttendance Below 75%:")
print(s[s < 75])
print("\nAttendance Above 90%:")
print(s[s > 90])
print("\nHighest Attendance:", s.max())
