import re

text = input("Enter a sentence: ")
result = re.sub(r" {2,}", " ", text).strip()
print("After replacing multiple spaces:", result)
