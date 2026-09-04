def consultation_charge():
    return 500

def laboratory_charge(tests):
    return tests * 300

def medicine_charge(amount):
    return amount

def room_charge(days):
    return days * 1000

def final_bill(tests, medicine, days, category):
    total = consultation_charge()
    total = total + laboratory_charge(tests)
    total = total + medicine_charge(medicine)
    total = total + room_charge(days)

    if category == "senior":
        total = total - total * 0.10
    elif category == "child":
        total = total - total * 0.05

    return total

tests = int(input("Enter number of laboratory tests: "))
medicine = float(input("Enter medicine charges: "))
days = int(input("Enter room days: "))
category = input("Enter category (senior/child/general): ").lower()

print("Final Hospital Bill =", final_bill(tests, medicine, days, category))
