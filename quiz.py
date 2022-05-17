print("--------------------------------------------------------------------------------------------")
print("------Programa para determinar si es un triangulo equilatero, escaleno, isosceles-----------")
print("--------------------------------------------------------------------------------------------")


#Input
X = int(input("Ingrese la longitud del primer lado: "))
Y = int(input("Ingrese la longitud del segundo lado: "))
Z = int(input("Ingrese la longitud del tercer lado: "))

#Procesing

if X==Y and X==Z:
    print("Es un triangulo equilatero") #Output

else:
    print("No es un triangulo equilatero") #Output

if X==Y and X!=Z:
    print("Es un triangulo isosceles") #Output

else:
    print("No es un triangulo isosceles") #Output


if X!=Y!=Z:
    print("Es un triangulo escaleno") #Output

else:
    print("No es un triangulo escaleno") #Output


