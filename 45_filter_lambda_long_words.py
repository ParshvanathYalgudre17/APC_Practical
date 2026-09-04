words = input("Enter words separated by space: ").split()

result = list(filter(lambda word: len(word) > 5, words))

print("Words having more than 5 characters =", result)
