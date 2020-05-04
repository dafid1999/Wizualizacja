import numpy as np

def macierz(n):
   m=np.diag([2 for x in range(n)])
   print(m)
   for i in range(2,n+1):
    m+= np.diag([2*i for x in range(n-i+1)],-(i-1))
    m+= np.diag([2*i for x in range(n-i+1)],(i-1))
   return m

print(macierz(5))