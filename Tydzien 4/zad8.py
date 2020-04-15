class Robaczek:
    x=0
    y=0
    krok=1

    def __init__(self,x,y,k):
        self.x=x
        self.y=y
        self.krok=k

    def ile_w_gore(self,n):
        self.y+=n*self.krok

    def ile_w_dol(self,n):
        self.y-=n*self.krok

    def ile_w_prawo(self,n):
        self.x+=n*self.krok

    def ile_w_lewo(self,n):
        self.x-=n*self.krok
    
    def pokaz_gdzie_jestes(self):
        print("Współrzędne robaczka: X=",self.x,"Y=",self.y)

    def __del__(self):
        del self.x
        del self.y
        del self.krok
        print("There is nothing here")

glizda=Robaczek(0,0,1)
glizda.pokaz_gdzie_jestes()
glizda.ile_w_gore(9)
glizda.pokaz_gdzie_jestes()
glizda.ile_w_prawo(3)
glizda.pokaz_gdzie_jestes()
glizda.ile_w_dol(1)
glizda.pokaz_gdzie_jestes()
glizda.ile_w_lewo(7)
glizda.pokaz_gdzie_jestes()

glizda="It disappeared"
print(glizda)

