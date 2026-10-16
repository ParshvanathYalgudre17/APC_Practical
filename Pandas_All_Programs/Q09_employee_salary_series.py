import pandas as pd

salary = {"Amit": 45000, "Sneha": 60000, "Rahul": 75000, "Priya": 40000, "Neha": 55000}
s = pd.Series(salary)

print("Employee Salaries:")
print(s)
print("\nHighest Salary:", s.max())
print("Lowest Salary:", s.min())
print("Average Salary:", s.mean())
print("\nEmployees Earning Above 50000:")
print(s[s > 50000])
