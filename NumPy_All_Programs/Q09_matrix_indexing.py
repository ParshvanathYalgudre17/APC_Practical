import numpy as np

arr = np.arange(1, 17).reshape(4, 4)
print("Matrix:\n", arr)
print("First row:", arr[0, :])
print("Last column:", arr[:, -1])
print("Diagonal elements:", np.diag(arr))
print("Second and third rows:\n", arr[1:3, :])
