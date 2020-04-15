class NaZakupy:
    nazwa_produktu=""
    ilosc=0
    jednostka_miary=""
    cena_jed=0
    def __init__(self, nazwa, ilosc, jednostka, cena):
        self.nazwa_produktu=nazwa
        self.ilosc=ilosc
        self.jednostka_miary=jednostka
        self.cena_jed=cena
    
    def wyswietl_produkt(self):
        print("Nazwa produktu: ", self.nazwa_produktu,"\nIlosc: ", self.ilosc,"\nJednostka miary: ",self.jednostka_miary,"\nCena za jednostke: ", self.cena_jed)
    
    def ile_produktu(self):
        print("Ilosc:",self.ilosc, self.jednostka_miary,sep=" ")

    def ile_kosztuje(self):
        print("Suma=",self.ilosc * self.cena_jed)


kapusta=NaZakupy("kapusta", 10,"kg", 3)

kapusta.wyswietl_produkt()
kapusta.ile_produktu()
kapusta.ile_kosztuje()