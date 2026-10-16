import re

text = input("Enter a paragraph containing PIN codes: ")
pin_codes = re.findall(r"\b[1-9]\d{5}\b", text)
print("PIN codes:", pin_codes)
