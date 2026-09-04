# 7. Count total number of characters including spaces

filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

print("Total number of characters =", len(data))
