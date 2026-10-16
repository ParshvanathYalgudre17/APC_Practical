import numpy as np

arr = np.array([12, 55, 34, 78, 49, 63, 20, 91, 45, 51])
print("Original array:", arr)
arr[arr > 50] = 0
print("After replacing values greater than 50 with 0:", arr)
