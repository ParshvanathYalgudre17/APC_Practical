import numpy as np

arr = np.arange(1, 21)
print("Array:", arr)
print("Even numbers:", arr[arr % 2 == 0])
print("Odd numbers:", arr[arr % 2 != 0])
