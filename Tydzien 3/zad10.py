def zakupy(**lista):
    ilosc=0
    for x in lista: 
        ilosc+=lista[x]
    
    print("\nIlosc produktow w sumie: ", ilosc)

zakupy(mleko=2, ser=1, maslo=2, pizza=5, lody=9, bulki=5)