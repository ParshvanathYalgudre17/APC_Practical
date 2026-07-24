n = int(input("Enter how many numbers: "))

i = 1

num = int(input("Enter number: "))
largest = num
smallest = num

while i < n:
    num = int(input("Enter number: "))

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    i = i + 1

print("Largest number =", largest)
print("Smallest number =", smallest)
