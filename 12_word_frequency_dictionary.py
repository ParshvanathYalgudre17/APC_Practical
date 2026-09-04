# 12. Count occurrence of each word using dictionary

filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

words = data.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Occurrences:")
print(word_count)
