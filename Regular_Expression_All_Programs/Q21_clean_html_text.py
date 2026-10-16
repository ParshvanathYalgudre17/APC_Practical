import re
import string

text = input("Enter text containing HTML tags: ")
text = re.sub(r"<[^>]*>", " ", text)
text = re.sub(r"\s+", " ", text).strip()
text = re.sub(r"[^\w\s.,!?;:'-]", "", text)
print("Cleaned text:", text)
