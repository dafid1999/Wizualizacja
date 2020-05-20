import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
sin = np.sin(x)
cos = np.cos(x)
plt.plot(x, sin, label='sin(x)')
plt.plot(x, cos, label='cos(x)')

plt.xlabel('x')
plt.ylabel('y')

plt.title("Wykres sin(x) i cos(x)")

plt.legend()
plt.show()