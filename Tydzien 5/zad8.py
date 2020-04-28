class Samogloski:
    """Iterator zwracający wartości będące samogłoskami"""
    __samogloski={"a","ą","e","ę","i","o","u","ó","y"}

    def __init__(self, data):
        if isinstance(data,str):
            self.data=data
        else:
            self.data=str(data)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index >=len(self.data):
            raise StopIteration
        if self.data[self.index] in Samogloski.__samogloski:
            return self.data[self.index]

przyklad=Samogloski("Ala ma kota, yeti ma duzą stopę")

sprawdz=iter(przyklad)
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
print(next(sprawdz))
