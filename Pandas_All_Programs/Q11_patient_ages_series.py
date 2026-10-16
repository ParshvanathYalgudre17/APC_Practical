import pandas as pd

patients = {101: 45, 102: 65, 103: 72, 104: 30, 105: 61}
s = pd.Series(patients)

print("Patient Ages:")
print(s)
print("\nAverage Age:", s.mean())
print("\nOldest Patient ID:", s.idxmax(), "Age:", s.max())
print("Youngest Patient ID:", s.idxmin(), "Age:", s.min())
print("\nPatients Above 60 Years:")
print(s[s > 60])
