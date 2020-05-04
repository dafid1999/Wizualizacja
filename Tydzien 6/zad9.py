import numpy as np

def macierz_fib(n):
    FIB=[]
    tempFIB=[]
    a=1
    b=1
    for x in range(n):
        for y in range(n):
            temp=b
            b+=a
            a=temp
            tempFIB.append(a)
        FIB.append(tempFIB)
        tempFIB=[]
    return np.array(FIB)
    
przyklad=macierz_fib(5)
print(przyklad)
