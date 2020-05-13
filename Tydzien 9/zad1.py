import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


xlsx=pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot(xticks=grupa.index.values)

wykres.set_ylabel("Liczba Urodzen")
wykres.set_xlabel("Rok")
wykres.legend()

plt.title('Liczba urodzen na rok')
plt.show()