import re

text = input("Enter a paragraph containing dates (DD-MM-YYYY): ")
dates = re.findall(r"\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b", text)
print("Dates found:", dates)
