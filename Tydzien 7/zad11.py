import numpy as np 

a=np.arange(12)
print(a,"\n")

b=a.reshape(3,4)
print(b,"\n")

c=a.reshape(4,3)
print(c,"\n")

d=a.reshape(2,6)
print(d,"\n")

print(b.ravel())
print(c.ravel())
print(d.ravel())

#Tak, są identyczne