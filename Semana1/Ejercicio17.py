#Ejercicio17
words = str(input("Ingrese dos palabras separadas por un espacio: "))
w_cad = words.split(" ")
w_cad.reverse()
esp = " "
nw_cad = esp.join(w_cad)
print(f"Lista invertida: {nw_cad}")