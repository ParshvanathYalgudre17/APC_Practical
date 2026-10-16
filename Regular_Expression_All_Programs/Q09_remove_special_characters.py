import re

text = input("Enter a string: ")
result = re.sub(r"[^A-Za-z0-9 ]", "", text)
print("After removing special characters:", result)
