from array import array

a = array('u', 'ABCDE')

print("Type Code: 'u'")
print("Original Array:", a)
print()

# 1. append()
a.append('F')
print("After append('F'):", a)
print()

# 2. buffer_info()
print("buffer_info():", a.buffer_info())
print()

# 3. count()
print("count('B'):", a.count('B'))
print()

# 4. extend()
a.extend('GH')
print("After extend('GH'):", a)
print()

# 5. fromunicode()
b = array('u')
b.fromunicode('HELLO')
print("After fromunicode('HELLO'):", b)
print()

# 6. fromlist()
d = array('u')
d.fromlist(['X', 'Y', 'Z'])
print("After fromlist():", d)
print()

# 7. index()
print("index('C'):", a.index('C'))
print()

# 8. insert()
a.insert(2, 'X')
print("After insert(2, 'X'):", a)
print()

# 9. pop()
removed = a.pop()
print("Popped element:", removed)
print("After pop():", a)
print()

# 10. remove()
a.remove('X')
print("After remove('X'):", a)
print()

# 11. reverse()
a.reverse()
print("After reverse():", a)
print()

# 12. tolist()
print("tolist():", a.tolist())
print()

# 13. tounicode()
print("tounicode():", a.tounicode())
print()
