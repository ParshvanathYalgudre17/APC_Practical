from array import array

a = array('d', [10.5, 20.5, 30.5, 40.5, 50.5])

print("Type Code: 'd'")
print("Original Array:", a)
print()

# append()
a.append(60.5)
print("After append(60.5):", a)
print()

# buffer_info()
print("buffer_info():", a.buffer_info())
print()

# byteswap()
a.byteswap()
print("After byteswap():", a)
print()
a.byteswap()

# count()
print("count(20.5):", a.count(20.5))
print()

# extend()
a.extend([70.5, 80.5])
print("After extend([70.5, 80.5]):", a)
print()

# frombytes()
b = array('d')
b.frombytes(a.tobytes())
print("After frombytes():", b)
print()

# fromfile()
with open("d_numbers.dat", "wb") as file:
    a.tofile(file)

c = array('d')
with open("d_numbers.dat", "rb") as file:
    c.fromfile(file, len(a))

print("After fromfile():", c)
print()

# fromlist()
d = array('d')
d.fromlist([100.5, 110.5, 120.5])
print("After fromlist():", d)
print()

# index()
print("index(30.5):", a.index(30.5))
print()

# insert()
a.insert(2, 25.5)
print("After insert(2, 25.5):", a)
print()

# pop()
removed = a.pop()
print("Popped element:", removed)
print("After pop():", a)
print()

# remove()
a.remove(25.5)
print("After remove(25.5):", a)
print()

# reverse()
a.reverse()
print("After reverse():", a)
print()

# tobytes()
print("tobytes():", a.tobytes())
print()

# tofile()
with open("d_array.dat", "wb") as file:
    a.tofile(file)

print("Array successfully written to file.")
print()

# tolist()
print("tolist():", a.tolist())
print()
