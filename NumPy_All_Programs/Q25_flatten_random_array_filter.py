import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
average = np.mean(flat)

print("Original 3D array:\n", arr)
print("\nFlattened array:", flat)
print("\nElements greater than 50:", flat[flat > 50])
print("Even elements:", flat[flat % 2 == 0])
print("Elements less than average (", average, "):", flat[flat < average])
