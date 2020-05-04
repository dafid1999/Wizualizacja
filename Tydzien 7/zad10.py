import numpy as np 

m=np.random.rand(9,9)
print(m)

a=m.reshape((3,27))
print(a)

b=m.reshape((27,3))
print(b)

c=m.ravel()
print(c)

d=m.T 
print(d)

e=m.reshape((10,3))
print(e)


# Macierz mozna zmieniać tak, by zmieściła wszystkie liczby których jest 81