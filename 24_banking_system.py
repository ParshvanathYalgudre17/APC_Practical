balance = 1000
transactions = []

def deposit(amount):
    global balance
    balance = balance + amount
    transactions.append("Deposited: " + str(amount))

def withdrawal(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        transactions.append("Withdrawn: " + str(amount))

def balance_enquiry():
    print("Balance =", balance)

def transaction_history():
    print("Transaction History:")
    for transaction in transactions:
        print(transaction)

deposit(500)
withdrawal(300)
balance_enquiry()
transaction_history()
