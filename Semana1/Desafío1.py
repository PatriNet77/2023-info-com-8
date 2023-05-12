#Desafío1
print("CALCULÁ TU COMISIÓN \nTu comisión es de un 6 % ""sobre el total de la venta. \n")
name = str(input("Ingrese su nombre: "))
venta = float(input("Ingrese el total de sus ventas en pesos: "))
comi = (6 * venta) / 100
print(name, f"tu comisión es de: {comi} pesos" )