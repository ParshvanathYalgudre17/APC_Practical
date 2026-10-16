import pandas as pd

products = {"Laptop": 50000, "Mobile": 20000, "Keyboard": 1500, "Mouse": 800, "Monitor": 12000}
s = pd.Series(products)

print("Product Prices:")
print(s)
s = s * 1.10
print("\nPrices After 10% Increase:")
print(s)
print("\nMost Expensive Product:")
print(s.idxmax(), "Price:", s.max())
print("\nProducts Costing Above 1000:")
print(s[s > 1000])
