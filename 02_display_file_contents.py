# 2. Display complete contents of a text file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

print("File Contents:")
print(data)
