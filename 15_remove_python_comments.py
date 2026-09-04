# 15. Remove single-line comments from Python source file

source_file = input("Enter Python source file name: ")
new_file = input("Enter output file name: ")

with open(source_file, "r") as file:
    lines = file.readlines()

with open(new_file, "w") as file:
    for line in lines:
        if not line.strip().startswith("#"):
            file.write(line)

print("Comments removed successfully.")
