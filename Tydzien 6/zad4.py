import numpy as np

def generuj(p,n):
    return np.logspace(1,n,num=n, base=p)

print(generuj(3,5))