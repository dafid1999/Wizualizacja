import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("zamowienia.csv",header=0,delimiter=";")

grupa=df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})

sprzedawcy=grupa.index.values
zamowienia=[grupa.values[y][0] for y in range(len(grupa.values))]

Explode=[0.1 for i in range(len(grupa.index.values))]

wedges, texts, autotexts = plt.pie(zamowienia,labels=sprzedawcy, explode=Explode, shadow=True,
                                   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))


plt.setp(autotexts, size=10)
plt.legend(title='Sprzedawcy')
plt.show()