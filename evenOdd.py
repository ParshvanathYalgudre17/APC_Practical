n = int(input("Enter the value of n: "))

i = 1

print("Even Numbers:")
while i <= n:
    if i % 2 == 0:
        print(i)
    i = i + 1

i = 1

print("Odd Numbers:")
while i <= n:
    if i % 2 != 0:
        print(i)
    i = i + 1
