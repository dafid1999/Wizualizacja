def fibonacci(n):
    a, b = 0, 1
    while a<n:
        yield a
        a, b = b, a + b

ciag=fibonacci(100)
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))
print(next(ciag))