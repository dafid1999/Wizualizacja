class CiagArytmetyczny:
    r=0
    a1=0
    n=0

    

    def wyswietl_dane(self,r,a1,n):
        print("Różnica: ", r,"\nPierwszy wyraz: ", a1,"\nIlosc wyrazow: ",n)


    def pobierz_elementy(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3
        return self.a1, self.a2, self.a3

    def pobierz_parametry(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n
        return self.a1,self.r,self.n

    def policz_sume(self):
        self.an=self.a1+(self.n-1)*self.r
        print("\nSuma=",((self.a1+self.an)/2)*self.n)

    def policz_elementy(self):
        print("\nAn=",self.an)
    


ciag=CiagArytmetyczny()
ciag.wyswietl_dane(2,1,3)
ciag.pobierz_elementy(1,2,3)
ciag.pobierz_parametry(10,2,3)
ciag.policz_sume()
ciag.policz_elementy()