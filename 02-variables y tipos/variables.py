"""

Una variable es un contenedor de informacion
que dentro guarda un dato, se pueden crear 
muchas variables y que cada una tenga un dato en especifico
"""

# Crear variables y asignar un valor
texto = "Master en python"
texto2 = "con Santiago Perez"
numero = 45
decimal = 6.7

print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------------")

# Sustituir el valor de algunas variables / reasignando valores
numero = 77
decimal = 34.65

print(numero)
print(decimal)

# Concatenacion
nombre = "Santiago"
apellidos = "Perez"
web = "santiago.perezb1@udea.edu.co"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))