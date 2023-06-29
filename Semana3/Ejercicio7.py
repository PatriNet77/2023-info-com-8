#Ejercicio7
print("¿Es o no es un palíndromo?\n")
palabra = input("Ingrese una palabra: ").lower()
reversa = palabra[::-1]

if palabra == reversa:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
