def parzyste(data):
    for index in range(1,len(data),2):
        yield data[index]

parzysta=parzyste("Ala ma kotaa")
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))
print(next(parzysta))