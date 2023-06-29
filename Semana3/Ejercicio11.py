numero = int(input("Introduce un número entero positivo: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es {factorial}")