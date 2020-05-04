import numpy as np

def wykreslanka():
    slownik=['wroksnad','rakielce','odrzpołg','coasoród','łmkizedy','agópnaźn','wewkatwi','agdańska']
    a=np.array([[x for x in slownik[i]] for i in range(8)])
    return a

print(wykreslanka())


