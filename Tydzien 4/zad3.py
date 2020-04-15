with open("dane.txt", "w+") as plik:
    plik.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n")
    plik.write("Etiam vulputate sapien eget sapien cursus pharetra.\n")
    plik.write("Ut id diam quis sem vulputate ullamcorper vel vel tortor\n")
    plik.write("Praesent mattis velit eget placerat imperdiet\n")
    plik.write("Morbi in turpis vel neque eleifend imperdiet.\n")
    plik.seek(0,0)
    for linia in plik:
        print(linia, end="")
