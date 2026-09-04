# 10. Count alphabets, digits, spaces and special characters

filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch != "\n":
        special += 1

print("Alphabets =", alphabets)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)
