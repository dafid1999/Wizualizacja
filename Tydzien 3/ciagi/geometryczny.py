def nwyraz(a1=1,q=1,n=1):
    if(n==1):
        return a1
    else:
        an=a1*(q**(n-1))
        return an

def suma(a1=1,q=1,n=1):
    if(q==1):
        suma=a1*n
        return suma
    else:
        suma=a1*((1-(q**n))/(1-q))
        return suma