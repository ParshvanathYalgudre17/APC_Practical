import re

password = input("Enter a password: ")
pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}"

if re.fullmatch(pattern, password):
    print("Password meets the requirements")
else:
    print("Password does not meet the requirements")
