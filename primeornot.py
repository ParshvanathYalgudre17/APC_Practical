num = int(input("Enter a number: "))

i = 2
count = 0

while i < num:
    if num % i == 0:
        count = 1
        break
    i = i + 1

if num <= 1:
    print(num, "is not a Prime Number.")
elif count == 0:
    print(num, "is a Prime Number.")
else:
    print(num, "is not a Prime Number.")
