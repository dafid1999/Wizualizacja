import pandas as pd
import numpy as np
import xlrd
import openpyxl

#zad1
xlsx=pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
print(df)

#zad2
#a
print(df[df['Liczba']>1000],"\n")

#b
print(df[df['Imie']=="DAWID"],"\n")

#c
print("Suma wszystkich urodzonych:",sum(df['Liczba']),"\n")

#d
dane=df[(df['Rok']>=2000)&(df['Rok']<=2005)]
print("Suma urodzonych z przedzialu 2000-2005:",sum(dane['Liczba']),"\n")

#e
chlopcy=df[df['Plec']=='M']
dziewczynki=df[df['Plec']=='K']
print("Suma urodzonych chlopcow:",sum(chlopcy['Liczba']),"\n")
print("Suma urodzonych dziewczynek:",sum(dziewczynki['Liczba']),"\n")

#f
popular=df.sort_values("Liczba", ascending=False).groupby(['Rok',"Plec"]) 

for key, popular in popular:
    print(popular.head(1))

#g
print("Najbardziej popularne imie dziewczynki ogólnie:\n",df[df['Liczba']==max(dziewczynki['Liczba'])])
print("Najbardziej popularne imie chlopca ogólnie:\n",df[df['Liczba']==max(chlopcy['Liczba'])])