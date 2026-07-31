sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    if len(word) > 0:
        result += word[0].upper() + word[1:] + " "

print("Title Case:", result.strip())
