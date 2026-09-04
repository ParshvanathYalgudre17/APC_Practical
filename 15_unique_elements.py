def unique_elements(numbers):
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result

numbers = list(map(int, input("Enter numbers: ").split()))
print("Unique elements =", unique_elements(numbers))
