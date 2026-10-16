import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())

df["Total"] = df[["Python", "DBMS", "Maths"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Maths"]].mean(axis=1)

print("\nTotal and Average Marks:")
print(df)
print("\nStudents with Average Above 75:")
print(df[df["Average"] > 75])
print("\nStudent with Highest Average:")
print(df.loc[df["Average"].idxmax()])
print("\nSubject-wise Average Marks:")
print(df[["Python", "DBMS", "Maths"]].mean())
