print("Perimetro del trapecio")
baseM=int(input("Ingresa la base mayor: "))
basem=int(input("Ingresa la base menor: "))
lado=int(input("Ingresa el lado oblicuo: "))
if baseM <= 0 and basem <= 0 and lado <= 0:
    print("Error en las bases o en el lado oblicuo")
else:
    perimetro=baseM+basem+(2*lado)
    print("El perimetro es: ",perimetro)