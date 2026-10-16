import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Amit", "Sneha", "Raj", "Priya", "Neha"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [2, 1, 3, 2, 1],
    "Price": [40000, 25000, 12000, 10000, 8000],
    "Discount": [2000, 1000, 1500, 500, 200]
}

df = pd.DataFrame(data)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]
print("All Orders:")
print(df)
print("\nOrders Above 5000:")
print(df[df["Final_Amount"] > 5000])
print("\nHighest-Value Order:")
print(df.loc[df["Final_Amount"].idxmax()])
print("\nAverage Order Value:", df["Final_Amount"].mean())
