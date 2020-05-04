import numpy as np
#zad8
b = np.arange(9).reshape(3,3)
print(b,"\n")
for a in b.reshape(3,1,3):
   print(a,"\n")
#zad9
b = np.arange(10,19).reshape(3,3)
print(b,"\n")
for a in b.flat:
   print(a)