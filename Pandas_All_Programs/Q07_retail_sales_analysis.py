import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [50000, 20000, 1500, 12000, 800],
    "Quantity": [2, 4, 10, 3, 15]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print("Product Data:")
print(df)
print("\nProducts with Sales Above 10000:")
print(df[df["Total_Sales"] > 10000])
print("\nProduct with Maximum Sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("\nAverage Sales:", df["Total_Sales"].mean())
