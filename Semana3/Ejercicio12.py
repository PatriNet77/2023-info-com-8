numeros = input("Introduce una lista de números separados por comas: ")
numeros = [int(numero) for numero in numeros.split(",")]
promedio = sum(numeros) / len(numeros)

print(f"El promedio de los números es {promedio}")