s = input("Enter a sentance: ")

count = 0

for c in s:
    if c == " ":
        count += 1

print("Word count =", count+1)

