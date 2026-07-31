n = int(input("Enter n: "))

letters = "ABCDE"

for i in range(n, 0, -1):
    for j in range(i):
        print(letters[j], end=" ")
    print()
