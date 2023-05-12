#Desafío2
print("Analizador de textos")
texto = input("Ingrese un texto, frase o artículo que quiera analizar: ").lower()


letras_bs = []
for letra in range(3):
    letras_bs.append(input(f"Ingrese una letra {letra+1}: ").lower())
    
for letras_b in letras_bs:
    cuenta = texto.count(letras_b)
    mensaje = f"La cantidad de veces que aparece la letra {letras_b} es: {cuenta}"
    print(mensaje)


palabras = texto.split()
cantidad = len(palabras)
print(f"La cantidad de palabras en el texto es de: {cantidad}")


if texto[-1] == ".":
    print(f"La primera letra del texto es: {texto[0]} y la última es: {texto[-2]}")
else:
   print(f"La primera letra del texto es: {texto[0]} y la última es: {texto[-1]}")


reves = texto[::-1]
print(f"Es más divertido al reves: {reves}")


encontrar = "python" in texto.lower()
dicc = {True: "SÍ", False: "NO"}
resultado = dicc[encontrar]
print(f"La palabra python {resultado} aparece en tu texto.")