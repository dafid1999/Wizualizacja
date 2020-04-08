def nwyraz(a1=1,r=1,n=1):
    if(n==1):
        return a1
    else:
        an=a1+((n-1)*r)
        return an

def suma(a1=1,r=1,n=1):
    suma=((((2*a1)+((n-1)*r))*n)/2)
    return suma
