n = int(input("Enter the number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1
