#Ejercicio16
print("Calculadora de IMC (índice de masa corporal)")
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = peso / (altura **2)
print(f"Su IMC es: {imc:.2f}")