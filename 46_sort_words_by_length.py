words = input("Enter words separated by space: ").split()

result = sorted(words, key=lambda word: len(word))

print("Sorted words =", result)
