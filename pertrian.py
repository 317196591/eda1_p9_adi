print("Perimetro del triangulo")
lado1=int(input("Ingresa el lado 1: "))
lado2=int(input("Ingresa el lado 2: "))
lado3=int(input("Ingresa el lado 3: "))
if lado1 <= 0 and lado2 <= 0 and lado3 <= 0:
    print("Error en los lados")
else:
    perimetro=lado1+lado2+lado3
    print("El perimetro es",perimetro)