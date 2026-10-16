import re

text = input("Enter text (use \\t for a tab and \\n for a newline if needed): ")
matches = re.findall(r"[ \t\n]", text)
print("Whitespace characters found:", len(matches))
print("Characters (space shown as SPACE, tab as TAB, newline as NEWLINE):")
print(["SPACE" if c == " " else "TAB" if c == "\t" else "NEWLINE" for c in matches])
