from array import array

a = array('b', [10, 20, 30, 40, 50])

print("Type Code: 'b'")
print("Original Array:", a)
print()

# 1. append()
a.append(60)
print("After append(60):", a)
print()

# 2. buffer_info()
print("buffer_info():", a.buffer_info())
print()

# 3. byteswap()
a.byteswap()
print("After byteswap():", a)
print()
a.byteswap()

# 4. count()
print("count(20):", a.count(20))
print()

# 5. extend()
a.extend([70, 80])
print("After extend([70, 80]):", a)
print()

# 6. frombytes()
b = array('b')
b.frombytes(a.tobytes())
print("After frombytes():", b)
print()

# 7. fromfile()
with open("b_numbers.dat", "wb") as file:
    a.tofile(file)

c = array('b')
with open("b_numbers.dat", "rb") as file:
    c.fromfile(file, len(a))

print("After fromfile():", c)
print()

# 8. fromlist()
d = array('b')
d.fromlist([100, 110, 120])
print("After fromlist():", d)
print()

# 9. index()
print("index(30):", a.index(30))
print()

# 10. insert()
a.insert(2, 25)
print("After insert(2, 25):", a)
print()

# 11. pop()
removed = a.pop()
print("Popped element:", removed)
print("After pop():", a)
print()

# 12. remove()
a.remove(25)
print("After remove(25):", a)
print()

# 13. reverse()
a.reverse()
print("After reverse():", a)
print()

# 14. tobytes()
byte_data = a.tobytes()
print("tobytes():", byte_data)
print()

# 15. tofile()
with open("b_array.dat", "wb") as file:
    a.tofile(file)

print("Array successfully written to file.")
print()

# 16. tolist()
print("tolist():", a.tolist())
print()
