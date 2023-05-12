#Ejercicio7
print("Adivinemos que es")
caracter = input("Ingrese un caracter cualquiera:")
if caracter.isupper():
    print("Es una letra mayúscula.")
elif caracter.islower():
    print("Es una letra minúscula.")
elif caracter.isdigit():
    print("Es un número.")
else:
    print("Es un caracter especial.")