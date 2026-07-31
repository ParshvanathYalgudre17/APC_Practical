s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

if s==rev:
    print("String is palindrom")
else:
    print("String is no Palindrom")
    

