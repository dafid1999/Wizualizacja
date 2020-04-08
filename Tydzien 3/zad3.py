spozywka = {
    "mleko" : "litry", 
    "ser" : "kg", 
    "wedlina" : "kg", 
    "jajka" : "sztuki", 
    "lody na patyku" : "sztuki"
}

print(spozywka)

spozywkav2 = {
    key for key in spozywka if spozywka[key]=="sztuki"
}

print(spozywkav2)