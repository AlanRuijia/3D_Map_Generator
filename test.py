import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

def paraboloid(x, y):
  return x**2 + y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-3.0, 3.0, 0.5)
X, Y = np.meshgrid(x, y)
zs = np.array([paraboloid(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

x1 = y1 = np.arange(-3.0, 3.0, 0.5)
X_1, Y_1 = np.meshgrid(x, y)
zs = np.array([paraboloid(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z_1 = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z, alpha=0.5)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()