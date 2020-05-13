import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx=pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

dane=df[(df['Rok']>=2012)&(df['Rok']<=2017)]

grupa = dane.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))

plt.title('Suma ilosci urodzonych dzieci w ostatnich 5 latach, z podziałem na płeć')
plt.show()