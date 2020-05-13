import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx=pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.bar()

wykres.set_ylabel("Liczba Urodzen w mln")
wykres.set_xlabel("Plec")
wykres.legend()

plt.title('Liczba urodzeń na rok, z podziałem na płeć')
plt.show()