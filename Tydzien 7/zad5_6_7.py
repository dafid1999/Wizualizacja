import numpy as np
m = np.array([[0.167,0.25,0.5],[0.75,1.,-1.]])
print(m,"\n")
#zad5
a = np.sin(m)
print(a,"\n")
#zad6
b = np.cos(m)
print(b,"\n")
#zad7
def dodawanie(a,b):
    return a+b

print(dodawanie(a,b))