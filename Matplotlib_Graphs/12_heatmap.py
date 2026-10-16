import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

plt.imshow(data, cmap="viridis")
plt.colorbar()
plt.title("Heatmap")
plt.show()
