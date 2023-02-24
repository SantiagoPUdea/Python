"""
Ejercicio 2. Escribir un scrip que nos muestre por panntalla 
todos los numeros pares del 1 al 120
"""

contador = 1
numero1 = int(input("Ingrese 1 numero: "))
numero2 = int(input("Ingrese 2 numero: "))

if numero1 < numero2:
    for contador in range(numero1,numero2):
        if contador%2 == 0:
            print(f"ES PAR |{contador}|")
        else: 
            print(f"ES IMPAR|{contador}|")
else:
    print("!! El 1 numero debe ser menor al 2 numero ingresado !!")