from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Reduce grid resolution for speed
num_points = 50  # Reduce from 100 to 50

theta1 = np.linspace(0, 2*np.pi, num_points)
r1 = np.linspace(-2, 0, num_points)
t1, R1 = np.meshgrid(theta1, r1)

X1 = R1 * np.cos(t1)
Y1 = R1 * np.sin(t1)
Z1 = 5 + R1 * 2.5

theta2 = np.linspace(0, 2*np.pi, num_points)
r2 = np.linspace(0, 2, num_points)
t2, R2 = np.meshgrid(theta2, r2)

X2 = R2 * np.cos(t2)
Y2 = R2 * np.sin(t2)
Z2 = -5 + R2 * 2.5

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
ax.set_aspect('auto')  # Use 'auto' instead of 'equal' for better performance

# Use colormap instead of solid color
ax.plot_surface(X1, Y1, Z1, rstride=2, cstride=2, cmap="Blues", linewidth=0, edgecolor='none')
ax.plot_surface(X2, Y2, Z2, rstride=2, cstride=2, cmap="Blues", linewidth=0, edgecolor='none')

plt.show()
