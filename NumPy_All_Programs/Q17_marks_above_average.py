import numpy as np

marks = np.array([78, 85, 92, 67, 88, 74, 95, 81, 69, 90,
                  72, 86, 91, 64, 83, 77, 89, 70, 96, 80])
average = np.mean(marks)

print("Marks:", marks)
print("Class average:", average)
print("Marks above average:", marks[marks > average])
