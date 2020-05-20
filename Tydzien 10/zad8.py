import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rzucaj(n):
    return [(np.random.randint(6)+1)+(np.random.randint(6)+1) for x in range(n)]

lista=rzucaj(50)
plt.hist(lista, bins=11, facecolor="blue", alpha=1)
plt.xlabel('Wartości')
plt.ylabel('Ilość rzutów')
plt.title('Histogram')
plt.grid(True)
plt.show()