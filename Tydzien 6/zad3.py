import numpy as np

def funkcja(n):
    return np.array([[n for n in range(x*n+1,x*n+n+1)] for x in range(0,n)])
   

a=funkcja(4)
print(a)