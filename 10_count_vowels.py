def count_vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiouAEIOU":
            count = count + 1
    return count

text = input("Enter a string: ")
print("Number of vowels =", count_vowels(text))
