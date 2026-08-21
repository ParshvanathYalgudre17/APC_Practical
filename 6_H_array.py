from array import array

a = array('H', [100, 200, 300, 400, 500])

print("Type Code: 'H'")
print("Original Array:", a)
print()

# append()
a.append(600)
print("After append(600):", a)
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
print("count(200):", a.count(200))
print()

# extend()
a.extend([700, 800])
print("After extend([700, 800]):", a)
print()

# frombytes()
b = array('H')
b.frombytes(a.tobytes())
print("After frombytes():", b)
print()

# fromfile()
with open("H_numbers.dat", "wb") as file:
    a.tofile(file)

c = array('H')
with open("H_numbers.dat", "rb") as file:
    c.fromfile(file, len(a))

print("After fromfile():", c)
print()

# fromlist()
d = array('H')
d.fromlist([1000, 1100, 1200])
print("After fromlist():", d)
print()

# index()
print("index(300):", a.index(300))
print()

# insert()
a.insert(2, 250)
print("After insert(2, 250):", a)
print()

# pop()
removed = a.pop()
print("Popped element:", removed)
print("After pop():", a)
print()

# remove()
a.remove(250)
print("After remove(250):", a)
print()

# reverse()
a.reverse()
print("After reverse():", a)
print()

# tobytes()
print("tobytes():", a.tobytes())
print()

# tofile()
with open("H_array.dat", "wb") as file:
    a.tofile(file)

print("Array successfully written to file.")
print()

# tolist()
print("tolist():", a.tolist())
print()
