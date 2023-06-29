texto = input("Introduce un texto: ")
vocales = "aeiouáéíóú"
vocales_mayusculas = ""

for letra in texto:
    if letra in vocales:
        vocales_mayusculas += letra.upper()
    else:
        vocales_mayusculas += letra
print(vocales_mayusculas)