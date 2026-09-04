def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]

numbers = list(map(int, input("Enter numbers: ").split()))
print("Second Largest =", second_largest(numbers))
