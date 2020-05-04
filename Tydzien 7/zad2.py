import numpy as np

a = np.random.randn(3,3)
b = np.random.randn(4,4)

print(a)
print(b,"\n")

print(a.min(axis=1))
print(a.min(axis=0),"\n")

print(b.min(axis=1))
print(b.min(axis=0))