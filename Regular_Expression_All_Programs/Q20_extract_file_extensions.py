import re

text = input("Enter text containing filenames: ")
extensions = re.findall(r"\b[\w.-]+\.(\w+)\b", text)
print("File extensions:", extensions)
