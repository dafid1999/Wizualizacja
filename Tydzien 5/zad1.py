class Material:
    rodzaj=""
    dlugosc=0
    szerokosc=0
    
    def __init__(self, ro,dl,sz):
        self.rodzaj=ro
        self.dlugosc=dl
        self.szerokosc=sz
    
    def wyswietl_nazwe(self):
        print(self.__class__.__name__)



class Ubrania(Material):
    rozmiar=""
    kolor=""
    dla_kogo=""

    def wyswietl_dane(self):
        print("Rozmiar: {} \nKolor: {} \nDla kogo: {}".format(self.rozmiar, self.kolor, self.dla_kogo))


class Sweter(Ubrania):
    rodzaj_swetra=""

    def wyswietl_dane(self):
        print("Rodzaj swetra: {}".format(self.rodzaj_swetra))

material=Material("welna",78,43)
material.wyswietl_nazwe()

ubranie=Ubrania("Syntentyki",70,35)
ubranie.rozmiar="L"
ubranie.kolor="Czarny"
ubranie.dla_kogo="Karol"
ubranie.wyswietl_nazwe()
ubranie.wyswietl_dane()

sweter=Sweter("Bawelna",90,50)
sweter.rodzaj_swetra="Rozpinany"
sweter.wyswietl_nazwe()
sweter.wyswietl_dane()
