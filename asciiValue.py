s = input("Enter a string: ")

for ch in s:
    for i in range(128):
        if chr(i) == ch:
            print(ch, "=", i)
            break
