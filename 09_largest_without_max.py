def largest(numbers):
    large = numbers[0]
    for i in numbers:
        if i > large:
            large = i
    return large

numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    numbers.append(int(input("Enter number: ")))

print("Largest =", largest(numbers))
