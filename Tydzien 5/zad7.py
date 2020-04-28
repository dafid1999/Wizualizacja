class Parzyste:
    """Iterator zwracający wartości z parzystych indeksów"""
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=2
        if self.index >=len(self.data):
            raise StopIteration
        return self.data[self.index]

kolekcja=Parzyste("kajak krzystof")
parzysta=iter(kolekcja)
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
