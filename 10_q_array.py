from array import array

a = array('q', [10000, 20000, 30000, 40000, 50000])

print("Type Code: 'q'")
print("Original Array:", a)
print()

a.append(60000)
print("After append(60000):", a)
print()

print("buffer_info():", a.buffer_info())
print()

a.byteswap()
print("After byteswap():", a)
print()
a.byteswap()

print("count(20000):", a.count(20000))
print()

a.extend([70000, 80000])
print("After extend([70000, 80000]):", a)
print()

b = array('q')
b.frombytes(a.tobytes())
print("After frombytes():", b)
print()

with open("q_numbers.dat", "wb") as file:
    a.tofile(file)

c = array('q')
with open("q_numbers.dat", "rb") as file:
    c.fromfile(file, len(a))

print("After fromfile():", c)
print()

d = array('q')
d.fromlist([100000, 110000, 120000])
print("After fromlist():", d)
print()

print("index(30000):", a.index(30000))
print()

a.insert(2, 25000)
print("After insert(2, 25000):", a)
print()

removed = a.pop()
print("Popped element:", removed)
print("After pop():", a)
print()

a.remove(25000)
print("After remove(25000):", a)
print()

a.reverse()
print("After reverse():", a)
print()

print("tobytes():", a.tobytes())
print()

with open("q_array.dat", "wb") as file:
    a.tofile(file)

print("Array successfully written to file.")
print()

print("tolist():", a.tolist())
print()
