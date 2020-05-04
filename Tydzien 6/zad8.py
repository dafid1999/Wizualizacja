import numpy as np

def funkcja(n,kierunek):
    czy=True
    if(kierunek=="poziomo"):
        if(n.shape[0]%2==0):
            c=int(n.shape[0]/2)
            m1=n[:c,:]
            m2=n[c:,:]
        else:
            czy=False
    elif(kierunek=="pionowo"):
        if(n.shape[1]%2==0):
            c=int(n.shape[1]/2)
            m1=n[:,:c]
            m2=n[:,c:]
        else:
            czy=False
    else:
        print("Błąd")
        print("Błąd")
        m1=0
        m2=0
    
    if(czy==True):
        return m1,m2
    else:
        print("Rozmiar tablicy nie pozwala na jej podzial")
        return 0,0

macierz=np.arange(30)
macierz=macierz.reshape(5,6)
print(macierz)

p1,p2=funkcja(macierz,"pionowo")
print(p1)
print(p2)
p1,p2=funkcja(macierz,"poziomo")
print(p1)
print(p2)
p1,p2=funkcja(macierz,"blabla")
print(p1)
print(p2)




