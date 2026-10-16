import re

text = input("Enter a social media post: ")
hashtags = re.findall(r"(?<!\w)#\w+", text)
print("Hashtags:", hashtags)
