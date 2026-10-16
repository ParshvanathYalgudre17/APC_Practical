import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [15, 25, 20, 35, 45]

plt.plot(x, y1, label="Student A", marker="o")
plt.plot(x, y2, label="Student B", marker="s")
plt.title("Multiple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Values")
plt.legend()
plt.show()
