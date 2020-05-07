import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('zamowienia.csv', header=0,delimiter=";")
print(df,"\n")

#a
print("Unikalni sprzedawcy:\n",df.Sprzedawca.unique(),"\n")

#b
naj=df.sort_values("Utarg", ascending=False)
print("Top 5 najdrozszych zamowien:\n",naj.head(5),"\n")

#c
ilosc=df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})
print("Ilość zamowien kazdego sprzedawcy:\n",ilosc,"\n")

#d
ilosc=df.groupby(['Kraj']).agg({"idZamowienia":['count']})
print("Ilość zamowien kazdego kraju:\n",ilosc,"\n")

ilosc=df.groupby(['Kraj']).agg({"Utarg":['sum']})
print("Suma zamowien kazdego kraju:\n",ilosc,"\n")
#Nie wiem o co dokładnie w zadaniu chodzi, wiec dałem 2 propozycje

#e
df['year']=pd.DatetimeIndex(df['Data zamowienia']).year
suma=df.groupby(['Kraj','year']).agg({"idZamowienia":['count']})
print(suma.index.values[5],suma.values[5],"\n")

#f
srednia=df.groupby(['year']).agg({"Utarg":['mean']})
print(srednia.index.values[1],srednia.values[1][0],"\n")

#g
rok4=df[df['year']==2004].copy()
rok4=rok4.drop(['year'],axis=1)
rok4.to_csv('zamowienia_2004.csv',header=True,index=False)

rok5=df[df['year']==2005].copy()
rok5=rok5.drop(['year'],axis=1)
rok5.to_csv('zamowienia_2005.csv',header=True,index=False)
