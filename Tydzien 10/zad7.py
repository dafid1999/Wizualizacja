import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")

plt.subplot(1,3,2)
ch=df[df["Plec"]=='M'].groupby(['Rok']).sum()
dz=df[df["Plec"]=='K'].groupby(['Rok']).sum()
chlopcy=[ch.values[y][0] for y in range(len(ch.values))]
dziewczeta=[dz.values[y][0] for y in range(len(dz.values))]
plt.bar(df.Rok.unique(),chlopcy,color="blue", label="M")
plt.bar(df.Rok.unique(),dziewczeta,color="red", label="K", bottom=chlopcy)
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend(loc=1)
plt.show()