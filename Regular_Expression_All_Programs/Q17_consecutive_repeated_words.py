import re

sentence = input("Enter a sentence: ")
matches = re.findall(r"\b(\w+)\s+\1\b", sentence, flags=re.IGNORECASE)
print("Consecutive repeated words:", matches)
