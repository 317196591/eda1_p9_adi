print("Area del trapecio")
baseM=int(input("Ingresa la base mayor: "))
basem=int(input("Ingresa la base menor: "))
altura=int(input("Ingresa la altura: "))
if baseM <= 0 and basem <=0 and altura <=0:
    print("Error en las bases o en la altura")
else:
    area=((baseM+basem)*altura)/2
    print("El resultado es:",area)