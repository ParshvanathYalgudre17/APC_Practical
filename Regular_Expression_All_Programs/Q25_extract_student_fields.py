import re

text = input("Enter text (example: Name: Amit, Roll: 23, Marks: 85): ")

name = re.search(r"Name\s*:\s*([A-Za-z ]+)", text, flags=re.IGNORECASE)
roll = re.search(r"Roll(?:\s*(?:No|Number))?\s*:\s*(\d+)", text, flags=re.IGNORECASE)
marks = re.search(r"Marks\s*:\s*(\d+(?:\.\d+)?)", text, flags=re.IGNORECASE)

print("Name:", name.group(1).strip() if name else "Not found")
print("Roll number:", roll.group(1) if roll else "Not found")
print("Marks:", marks.group(1) if marks else "Not found")
