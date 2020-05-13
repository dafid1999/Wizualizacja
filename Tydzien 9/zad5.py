import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('zamowienia.csv', header=0,delimiter=";")
grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres = grupa.plot.bar()

wykres.set_ylabel("Liczba Zamowien")
wykres.set_xlabel("Sprzedawca")
wykres.legend()

plt.title('Ilosc zamowien zlozonych przez poszczegolnych Sprzedawcow')
plt.show()