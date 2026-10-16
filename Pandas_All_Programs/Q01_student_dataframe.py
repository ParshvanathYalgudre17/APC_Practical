import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Python": [85, 70, 90, 60, 80],
    "DBMS": [80, 75, 88, 65, 85],
    "Mathematics": [90, 80, 92, 70, 78]
}

df = pd.DataFrame(data)
df["Total"] = df[["Python", "DBMS", "Mathematics"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Mathematics"]].mean(axis=1)

print("Student Data:")
print(df)
print("\nStudents with Average Above 75:")
print(df[df["Average"] > 75])
