def total_bill(prices, quantities):
    total = 0
    for p, q in zip(prices, quantities):
        total = total + p * q

    if total >= 5000:
        total = total - total * 0.10

    return total

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))

print("Total Bill =", total_bill(prices, quantities))
