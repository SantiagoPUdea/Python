"""
Ejercicio 4. Pedir dos numeros al usuario y hacer todas las
operaciones basicas de una calculadora y mostrarlo por pantalla.
"""
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print("\n########### CALCULADORA ############")
print()

print(f"El resultado de la suma de {numero1} y {numero2} = {numero1+numero2}")
print(f"El resultado de la resta de {numero1} y {numero2} = {numero1-numero2}")
print(f"El resultado de la multiplicacion de {numero1} y {numero2} = {numero1*numero2}")
print(f"El resultado de la division de {numero1} y {numero2} = {numero1/numero2}")
print("\n!! Otra forma de imprimir la salida !!")
print(f"\n|{numero1} + {numero2} = {numero1+numero2}|")
print(f"|{numero1} - {numero2} = {numero1-numero2}|")
print(f"|{numero1} * {numero2} = {numero1*numero2}|")
print(f"|{numero1} / {numero2} = {numero1/numero2}|")