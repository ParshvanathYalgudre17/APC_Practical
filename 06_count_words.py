# 6. Count total number of words

filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

words = data.split()

print("Total number of words =", len(words))
