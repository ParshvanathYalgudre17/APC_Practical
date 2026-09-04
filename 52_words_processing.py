words = input("Enter words separated by space: ").split()

lengths = list(map(lambda word: len(word), words))
print("Length of words =", lengths)

long_words = list(filter(lambda word: len(word) > 5, words))
print("Words having more than 5 characters =", long_words)

sorted_words = sorted(words, key=lambda word: len(word))
print("Words sorted by length =", sorted_words)
