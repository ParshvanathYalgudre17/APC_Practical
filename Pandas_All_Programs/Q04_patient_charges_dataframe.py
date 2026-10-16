import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Sneha", "Raj", "Priya", "Neha"],
    "Age": [65, 45, 72, 30, 61],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Diabetes"],
    "Medical_Charges": [60000, 15000, 90000, 25000, 55000]
}

df = pd.DataFrame(data)
print("Patients Above 60 Years:")
print(df[df["Age"] > 60])
print("\nAverage Medical Charge:", df["Medical_Charges"].mean())
print("\nMaximum Medical Charge:", df["Medical_Charges"].max())
print("\nPatients with Charges Above 50000:")
print(df[df["Medical_Charges"] > 50000])
