Liczby=[x for x in range(100) if x % 4 == 0]

plik =open("liczby.txt", "w+")

plik.write(str(Liczby))

plik.close()