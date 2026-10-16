import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr)
print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:\n", np.sum(arr, axis=(1, 2)))
print("Sum along rows (for each layer):\n", np.sum(arr, axis=2))
print("Sum along columns (for each layer):\n", np.sum(arr, axis=1))
