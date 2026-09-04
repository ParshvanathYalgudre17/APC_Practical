# 22. Combine contents of two files into a third file

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
file3 = input("Enter third file name: ")

with open(file1, "r") as f1:
    data1 = f1.read()

with open(file2, "r") as f2:
    data2 = f2.read()

with open(file3, "w") as f3:
    f3.write(data1)
    f3.write("\n")
    f3.write(data2)

print("Contents combined successfully.")
