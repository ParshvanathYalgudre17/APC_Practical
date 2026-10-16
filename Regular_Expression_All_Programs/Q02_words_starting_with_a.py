import re

sentence = input("Enter a sentence: ")
words = re.findall(r"\b[aA]\w*\b", sentence)
print("Words beginning with A or a:", words)
