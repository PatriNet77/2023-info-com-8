#Ejercicio12
import datetime
print("Ingrese su fecha de nacimiento dd/mm/aaaa: ")
f_nac = input()
dia, mes, anio = map(int, f_nac.split("/"))
f_hoy = datetime.date.today()
edad = f_hoy.year - anio
if mes > f_hoy.month or (mes == f_hoy.month and dia > f_hoy.day):
    edad = edad - 1
print(f"Tu edad actual es: {edad} años")
