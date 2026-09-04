list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda x, y: x + y, list1, list2))

print("Sum =", result)
