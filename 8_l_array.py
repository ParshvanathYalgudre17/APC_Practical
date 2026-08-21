from array import array

a = array('l', [1000, 2000, 3000, 4000, 5000])

print("Type Code: 'l'")
print("Original Array:", a)
print()

a.append(6000)
print("After append(6000):", a)
print()

print("buffer_info():", a.buffer_info())
print()

a.byteswap()
print("After byteswap():", a)
print()
a.byteswap()

print("count(2000):", a.count(2000))
print()

a.extend([7000, 8000])
print("After extend([7000, 8000]):", a)
print()

b = array('l')
b.frombytes(a.tobytes())
print("After frombytes():", b)
print()

with open("l_numbers.dat", "wb") as file:
    a.tofile(file)

c = array('l')
with open("l_numbers.dat", "rb") as file:
    c.fromfile(file, len(a))

print("After fromfile():", c)
print()

d = array('l')
d.fromlist([10000, 11000, 12000])
print("After fromlist():", d)
print()

print("index(3000):", a.index(3000))
print()

a.insert(2, 2500)
print("After insert(2, 2500):", a)
print()

removed = a.pop()
print("Popped element:", removed)
print("After pop():", a)
print()

a.remove(2500)
print("After remove(2500):", a)
print()

a.reverse()
print("After reverse():", a)
print()

print("tobytes():", a.tobytes())
print()

with open("l_array.dat", "wb") as file:
    a.tofile(file)

print("Array successfully written to file.")
print()

print("tolist():", a.tolist())
print()
