pi = 3.1416
print("Perimetro del circulo")
radio=int(input("Ingresa el radio: "))
if radio <= 0:
    print("Error en el radio")
else:
    perimetro=2*pi*radio
    print("El perimetro es:",perimetro)