import re

sentence = input("Enter a sentence: ")
words = re.findall(r"\b\w+\b", sentence)
print("Number of words:", len(words))
