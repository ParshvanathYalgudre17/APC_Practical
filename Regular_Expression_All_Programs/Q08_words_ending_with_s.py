import re

sentence = input("Enter a sentence: ")
words = re.findall(r"\b\w+s\b", sentence, flags=re.IGNORECASE)
print("Words ending with s:", words)
