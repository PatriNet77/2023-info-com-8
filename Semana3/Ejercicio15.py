texto = input("Introduce un texto: ")
conteo = {}

for letra in texto:
    if letra in conteo:
        conteo[letra] += 1
    else:
        conteo[letra] = 1

for letra, cantidad in conteo.items():
    print(f"{letra}: {cantidad}")