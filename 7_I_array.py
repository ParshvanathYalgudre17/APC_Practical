from array import array

a = array('I', [10, 20, 30, 40, 50])

print("Type Code: 'I'")
print("Original Array:", a)
print()

# append()
a.append(60)
print("After append(60):", a)
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
print("count(20):", a.count(20))
print()

# extend()
a.extend([70, 80])
print("After extend([70, 80]):", a)
print()

# frombytes()
b = array('I')
b.frombytes(a.tobytes())
print("After frombytes():", b)
print()

# fromfile()
with open("I_numbers.dat", "wb") as file:
    a.tofile(file)

c = array('I')
with open("I_numbers.dat", "rb") as file:
    c.fromfile(file, len(a))

print("After fromfile():", c)
print()

# fromlist()
d = array('I')
d.fromlist([100, 200, 300])
print("After fromlist():", d)
print()

# index()
print("index(30):", a.index(30))
print()

# insert()
a.insert(2, 25)
print("After insert(2, 25):", a)
print()

# pop()
removed = a.pop()
print("Popped element:", removed)
print("After pop():", a)
print()

# remove()
a.remove(25)
print("After remove(25):", a)
print()

# reverse()
a.reverse()
print("After reverse():", a)
print()

# tobytes()
print("tobytes():", a.tobytes())
print()

# tofile()
with open("I_array.dat", "wb") as file:
    a.tofile(file)

print("Array successfully written to file.")
print()

# tolist()
print("tolist():", a.tolist())
print()
