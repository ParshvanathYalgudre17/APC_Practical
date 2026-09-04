# 16. Create uppercase copy of a text file

source_file = input("Enter source file name: ")
new_file = input("Enter output file name: ")

with open(source_file, "r") as file:
    data = file.read()

with open(new_file, "w") as file:
    file.write(data.upper())

print("Uppercase file created successfully.")
