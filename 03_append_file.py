# 3. Append information to an existing file

filename = input("Enter file name: ")
info = input("Enter information to append: ")

with open(filename, "a") as file:
    file.write("\n" + info)

print("Information appended successfully.")
