import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Matrix multiplication:\n", np.matmul(a, b))
