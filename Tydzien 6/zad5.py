import numpy as np


def wektor(n):
    return np.diag([n for n in range(n,0,-1)])

print(wektor(10))