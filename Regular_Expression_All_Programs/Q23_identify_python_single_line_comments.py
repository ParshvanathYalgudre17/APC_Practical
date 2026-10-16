import re

source = input("Enter one line of Python source code: ")
comments = re.findall(r"#.*", source)
print("Possible single-line comments:", comments)

print("Note: This simple regex can also match # inside a string literal.")
print("For accurate Python comment detection, use the tokenize module.")
