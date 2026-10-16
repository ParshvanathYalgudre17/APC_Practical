import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print("Array A:\n", a)
print("Array B:\n", b)
print("Horizontal concatenation:\n", np.hstack((a, b)))
print("Vertical concatenation:\n", np.vstack((a, b)))
