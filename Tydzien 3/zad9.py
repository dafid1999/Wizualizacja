def ciag(* liczby):
    if(len(liczby) == 0):
        return 0.0
    else:
        iloczyn = 1
    for i in liczby:
        iloczyn *= i
    return iloczyn
print(ciag())
print(ciag(1,2,3,4,5,6,7,8))