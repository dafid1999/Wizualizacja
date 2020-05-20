import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")

grupa1=df.groupby(['Plec']).agg({"Liczba":["sum"]})
plt.subplot(1,3,1)
plt.bar(['K','M'],[grupa1.values[0][0],grupa1.values[1][0]],color=['red','blue'])
plt.ylabel('Ilość urodzeń (mln)')
plt.xlabel('Płeć')

plt.subplot(1,3,2)
ch=df[df["Plec"]=='M'].groupby(['Rok']).sum()
dz=df[df["Plec"]=='K'].groupby(['Rok']).sum()
chlopcy=[ch.values[y][0] for y in range(len(ch.values))]
dziewczeta=[dz.values[y][0] for y in range(len(dz.values))]
plt.plot(df.Rok.unique(),chlopcy,"b", label="M")
plt.plot(df.Rok.unique(),dziewczeta,"r", label="K")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend()

plt.subplot(1,3,3)
grupa2=df.groupby(['Rok']).agg({"Liczba":["sum"]})
plt.bar(df.Rok.unique(),[grupa2.values[y][0] for y in range(len(grupa2.values))],color="yellow")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.show()