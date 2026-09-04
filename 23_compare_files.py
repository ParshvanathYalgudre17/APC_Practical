# 23. Compare two text files

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")

with open(file1, "r") as f1:
    lines1 = f1.readlines()

with open(file2, "r") as f2:
    lines2 = f2.readlines()

same = True
limit = min(len(lines1), len(lines2))

for i in range(limit):
    if lines1[i] != lines2[i]:
        print("Files are different.")
        print("First difference is at line", i + 1)
        print("File 1:", lines1[i].strip())
        print("File 2:", lines2[i].strip())
        same = False
        break

if same:
    if len(lines1) == len(lines2):
        print("Files are identical.")
    else:
        print("Files are different.")
        print("First difference is at line", limit + 1)
