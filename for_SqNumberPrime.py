import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))
prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

if prime:
    print("Square root", root, "is Prime")
else:
    print("Square root", root, "is Not Prime")
