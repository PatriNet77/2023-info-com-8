#Ejercicio2
num_user = int(input("Ingrese un número: "))
suma = 0
for i in range(1, num_user + 1):
    suma += i
print(f"La suma de todos los números naturales entre 1 y {num_user} es {suma}")
