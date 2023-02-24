"""
Modulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, qu elos puedes consultar aqui:
https://docs.python.org/es/3/tutorial/modules.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet y tambien podemos crear nuestros modulos
"""
import mimodulo
#from mimodulo import holaMundo     # para importar directamente solo una funcion del modulo
# from mimodulo import *            # importa todo dentro del modulo directamente

print(mimodulo.holaMundo("Santiago Perez"))
print("-----------------------------------")
print(mimodulo.calculadora(23, 54, True))
# print(holaMundo("felipe Melo 2.0"))

# Modulo fechas 
import datetime

print(datetime.date.today())      # FECHA

fecha_completa = datetime.datetime.now()    # FECHA COMPLETA

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")   # PERSONALIZAR LA FECHA
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())


# Modulo matematicas
import math

print("\nRaiz cuadrada de 10: ", math.sqrt(10))     # METODO RAIZ CUADRADA

print("Numero pi: ", float(math.pi))                  # SACAR PI

print("Numero pi redondeado: ", math.floor(math.pi))   # METODO PARA REDONDEAR

# Modulo random
import random

print("Numnero aleatorio entre 15 y 67: ", random.randint(100, 4967))