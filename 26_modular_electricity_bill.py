def energy_charge(units):
    if units <= 100:
        return units * 2
    elif units <= 200:
        return 100 * 2 + (units - 100) * 3
    else:
        return 100 * 2 + 100 * 3 + (units - 200) * 5

def calculate_bill(units):
    energy = energy_charge(units)
    fixed = 100
    tax = (energy + fixed) * 0.05
    discount = 0

    if units < 100:
        discount = (energy + fixed) * 0.05

    return energy + fixed + tax - discount

units = int(input("Enter units consumed: "))
print("Electricity Bill =", calculate_bill(units))
