import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients Above 60 Years:")
print(df[df["Age"] > 60])
print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())
print("\nPatient with Highest Medical Expense:")
print(df.loc[df["Medical_Expense"].idxmax()])
print("\nNumber of Patients for Each Disease:")
print(df["Disease"].value_counts())
print("\nPatients with Medical Expense Above 50000:")
print(df[df["Medical_Expense"] > 50000])
