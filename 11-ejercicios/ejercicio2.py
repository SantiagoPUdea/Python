"""
Ejercicio2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
"""

coleccion = []
x = 0

while x < 120:
    coleccion.append(f"elemento-{x}")
    print(f"Mostrando el: " + coleccion[x])
    x += 1
print(coleccion[56])

"""
coleccion = []

for contador in range(0,120):
    coleccion.append(f"elemento-{contador}")
    print(f"Mostrando el: " + coleccion[contador])
    contador += 1
else:
    print("\nPrograma terminado")
"""