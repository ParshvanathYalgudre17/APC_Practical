# 13. Search word and display occurrences and line numbers

filename = input("Enter file name: ")
search_word = input("Enter word to search: ")

count = 0
line_numbers = []

with open(filename, "r") as file:
    for line_no, line in enumerate(file, start=1):
        words = line.split()

        for word in words:
            if word.lower() == search_word.lower():
                count += 1
                if line_no not in line_numbers:
                    line_numbers.append(line_no)

print("Number of occurrences =", count)
print("Line numbers =", line_numbers)
