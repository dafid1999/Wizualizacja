class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


    
kolekcja=Wspak("kajak")
naodwrot=iter(kolekcja)
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot),"\n")

kolekcja=Wspak("Ala ma kota")
naodwrot=iter(kolekcja)
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))
print(next(naodwrot))