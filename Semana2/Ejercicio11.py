#Ejercicio11
num_1 = int(input("Introduce el primer número: "))
num_2 = int(input("Introduce el segundo número: "))

if num_1 % 2 == 0 and num_2 % 2 == 0:
    print("La suma de los dos números es:", num_1 + num_2)
else:
    print("No se puede realizar la operación. \nAl menos uno de los números no es par.")