import numpy as np
import matplotlib.pyplot as mpl

s = 50

x = np.random.rand(s)
y = np.random.rand(s)
colors = np.random.rand(s)
area = (30 * np.random.rand(s)) ** 2

mpl.scatter(x, y, s=area, c=colors, alpha=0.5)
mpl.show()
