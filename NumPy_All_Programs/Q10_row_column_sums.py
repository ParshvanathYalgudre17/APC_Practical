import numpy as np

arr = np.arange(1, 17).reshape(4, 4)
print("Matrix:\n", arr)
print("Sum of each row:", np.sum(arr, axis=1))
print("Sum of each column:", np.sum(arr, axis=0))
