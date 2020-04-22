
class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x=x
        self.y=x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

    def __lt__(self,other):
        if (self.x<other.x):
            return True
        return False

    def __le__(self,other):
        if (self.x<=other.x):
            return True
        return False

    def __gt__(self,other):
        if (self.x>other.x):
            return True
        return False

    def __ge__(self,other):
        if (self.x>=other.x):
            return True
        return False

figura=Kwadrat(5)
figura1=Kwadrat(2)
print(figura>figura1)

print(figura>=figura1)

print(figura<figura1)

print(figura<=figura1)

print(figura1<=figura)

print(figura>=figura)