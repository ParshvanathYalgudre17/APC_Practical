def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculate(a, b, operation):
    return operation(a, b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", calculate(a, b, addition))
print("Subtraction =", calculate(a, b, subtraction))
print("Multiplication =", calculate(a, b, multiplication))

if b != 0:
    print("Division =", calculate(a, b, division))
else:
    print("Division not possible")
