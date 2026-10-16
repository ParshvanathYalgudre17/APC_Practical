import re

text = input("Enter a string: ")
digits = re.findall(r"\d", text)
print("Digits:", digits)
