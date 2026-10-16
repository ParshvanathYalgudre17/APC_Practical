import re

text = input("Enter a string: ")
letters = re.findall(r"[A-Z]", text)
print("Uppercase letters:", letters)
