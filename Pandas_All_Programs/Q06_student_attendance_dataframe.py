import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 120, 100, 80],
    "Classes_Attended": [80, 65, 90, 70, 50]
}

df = pd.DataFrame(data)
df["Attendance_Percentage"] = df["Classes_Attended"] / df["Total_Classes"] * 100
print("Student Attendance:")
print(df)
print("\nStudents with Attendance Below 75%:")
print(df[df["Attendance_Percentage"] < 75])
