# 20. Deposits and withdrawals

transactions = [
    ["Deposit", 5000],
    ["Withdrawal", 1000],
    ["Deposit", 3000],
    ["Withdrawal", 500]
]

total_deposit = 0
total_withdrawal = 0
largest = 0
balance = 0

for transaction in transactions:
    type = transaction[0]
    amount = transaction[1]

    if amount > largest:
        largest = amount

    if type == "Deposit":
        total_deposit += amount
        balance += amount
    elif type == "Withdrawal":
        total_withdrawal += amount
        balance -= amount

print("Total Deposits =", total_deposit)
print("Total Withdrawals =", total_withdrawal)
print("Final Balance =", balance)
print("Largest Transaction =", largest)
