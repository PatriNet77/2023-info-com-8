texto = input("Introduce un texto: ")
palabras = texto.split()
palabras_al_reves = [palabra[::-1] for palabra in palabras]
texto_al_reves = " ".join(palabras_al_reves)

print(texto_al_reves)