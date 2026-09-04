products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 5),
    ("Keyboard", 1500, 3),
    ("Mobile", 20000, 2)
]

total_values = list(map(lambda x: (x[0], x[1] * x[2]), products))
print("Total value of each product:")
print(total_values)

expensive = list(filter(lambda x: x[1] > 1000, products))
print("Products costing more than 1000:")
print(expensive)

sorted_products = sorted(products, key=lambda x: x[1] * x[2])
print("Products sorted by total value:")
print(sorted_products)
