# 14. Replace a word in a text file

filename = input("Enter file name: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open(filename, "r") as file:
    data = file.read()

data = data.replace(old_word, new_word)

with open(filename, "w") as file:
    file.write(data)

print("Word replaced successfully.")
