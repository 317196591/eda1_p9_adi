pi = 3.1416
print("Area del circulo")
radio=int(input("Ingresa el radio: "))
if radio <= 0:
    print("Error en el radio")
else:
    area=pi*radio*radio
    print("El area es:",area)