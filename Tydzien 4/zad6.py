class Slowa:
    slowo1=""
    slowo2=""

    def __init__(self,x,y):
        self.slowo1=x
        self.slowo2=y


    def sprawdz_czy_palindrom(self):
        print(self.slowo1)
        if self.slowo1!=self.slowo1[::-1]:
            print("Nie jest palindromem.\n")
        else:
            print("Jest palindromem.\n")


        print(self.slowo2)
        if self.slowo2!=self.slowo2[::-1]:
            print("Nie jest palindromem.\n")
        else:
            print("Jest palindromem.\n")
    
    def sprawdz_czy_metagram(self):
        metagram=False
        if len(self.slowo1)==len(self.slowo2):
            lit=0
            for i in range(len(self.slowo1)):
                if self.slowo1[i]!=self.slowo2[i]:
                    lit+=1
            if lit==1:
                metagram=True
        if metagram:
            print("Slowa sa metagramami.")
        else:
            print("Slowa nie sa metagramami.")

    def sprawdz_czy_anagram(self):
        anagram=True
        if len(self.slowo1)==len(self.slowo2):
            napis = self.slowo2
            for znak in self.slowo1:
                if znak in napis:
                    i = napis.index(znak)
                    napis = napis[:i]+napis[i+1:]
                else:
                    anagram=False
        else:
            anagram=False
        if anagram:
            print("Slowa sa anagramami.")
        else:
            print("Slowa nie sa anagramami.")

    def wyswietl_wyrazy(self):
        print(self.slowo1,self.slowo2)

sprawdz=Slowa("ala","siema")
sprawdz.wyswietl_wyrazy()
sprawdz.sprawdz_czy_palindrom()
sprawdz.sprawdz_czy_metagram()
sprawdz.sprawdz_czy_anagram()
sprawdz=Slowa("mata","tata")
sprawdz.wyswietl_wyrazy()
sprawdz.sprawdz_czy_palindrom()
sprawdz.sprawdz_czy_metagram()
sprawdz.sprawdz_czy_anagram()
sprawdz=Slowa("mata","tama")
sprawdz.wyswietl_wyrazy()
sprawdz.sprawdz_czy_palindrom()
sprawdz.sprawdz_czy_metagram()
sprawdz.sprawdz_czy_anagram()

