import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
sin = np.sin(x)+2
cos = np.sin(-x)
plt.plot(x, sin, label='sin(x)')
plt.plot(x, cos, label='sin(x)')

plt.xlabel('x')
plt.ylabel('sin(x)')

plt.title("Wykres sin(x), sin(x)")

plt.legend(loc=6)
plt.show()