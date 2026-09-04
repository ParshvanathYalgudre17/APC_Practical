numbers = list(map(int, input("Enter numbers: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers =", even_numbers)
