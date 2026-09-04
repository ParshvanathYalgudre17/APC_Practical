# 11. Find the longest word in a file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

words = data.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)
