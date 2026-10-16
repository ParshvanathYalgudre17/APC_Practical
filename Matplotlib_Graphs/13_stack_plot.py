import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 20]
y2 = [5, 10, 10, 15, 10]

plt.stackplot(x, y1, y2, labels=["Student A", "Student B"])
plt.title("Stack Plot")
plt.xlabel("X-axis")
plt.ylabel("Values")
plt.legend()
plt.show()
