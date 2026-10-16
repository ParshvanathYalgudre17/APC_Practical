import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 20000, 1500, 800, 12000],
    "Quantity": [3, 5, 10, 20, 4]
}

df = pd.DataFrame(data)
df["Total_Amount"] = df["Price"] * df["Quantity"]
print("Product Data:")
print(df)
print("\nProduct with Highest Total Sales:")
print(df.loc[df["Total_Amount"].idxmax()])
