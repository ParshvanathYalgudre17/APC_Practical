iimport math

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
    print("Square root", root, "is Not Prime")mport math

x = float(input("Enter x: "))
n = int(input("Enter n: "))

sum = 0

for i in range(0, n + 1, 2):
    fact = math.factorial(i)
    
    if (i // 2) % 2 == 0:
        sum = sum + (x ** i) / fact
    else:
        sum = sum - (x ** i) / fact

print("Cosine =", sum)

