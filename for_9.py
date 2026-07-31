n = int(input("Enter n: "))

letters = "ABCDE"

for i in range(1, n + 1):
    for j in range(i):
        print(letters[j], end=" ")
    print()
