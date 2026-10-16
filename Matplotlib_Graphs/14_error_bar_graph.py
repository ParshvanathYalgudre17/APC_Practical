import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
error = [2, 3, 2, 4, 3]

plt.errorbar(x, y, yerr=error, fmt="o-", capsize=5)
plt.title("Error Bar Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
