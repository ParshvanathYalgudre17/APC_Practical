def list_details(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
        total = total + n

    average = total / len(numbers)
    return minimum, maximum, total, average

numbers = list(map(int, input("Enter numbers: ").split()))
minimum, maximum, total, average = list_details(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)
