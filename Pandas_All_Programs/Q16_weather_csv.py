import pandas as pd

df = pd.read_csv("weather.csv")

print("Maximum Temperature:")
print(df["Temperature"].max())
print("\nMinimum Temperature:")
print(df["Temperature"].min())
print("\nAverage Temperature:")
print(df["Temperature"].mean())
print("\nRecords with Temperature Above 35:")
print(df[df["Temperature"] > 35])
print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())
