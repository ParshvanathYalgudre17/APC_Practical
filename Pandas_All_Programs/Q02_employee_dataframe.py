import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Sneha", "Raj", "Priya", "Neha"],
    "Department": ["CSE", "IT", "HR", "CSE", "IT"],
    "Salary": [45000, 60000, 55000, 75000, 40000],
    "Experience": [2, 5, 8, 6, 3]
}

df = pd.DataFrame(data)
print("Employees with Salary Above 50000:")
print(df[df["Salary"] > 50000])
print("\nAverage Salary:", df["Salary"].mean())
print("\nHighest Salary:", df["Salary"].max())
print("\nEmployee with Highest Experience:")
print(df.loc[df["Experience"].idxmax()])
