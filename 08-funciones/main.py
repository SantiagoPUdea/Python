"""
FUNCIONES
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a 
la funcion tantas veces como sea necesario

"""

# Ejemplo 1
print("###### EJEMPLO 1 ######")

def muestraNombre():
    print("Santiago Perez")
    print("Lucho Perez")
    print("Pedro ROjas")
    print("Gustavo Perez")
    print("Andres Perez")
    print("Perico Perez")
    print("Rafael Perez")
    print("Alonso Perez")

# Invocar funcion
muestraNombre()
"""
# Ejemplo 2: parametros
print("###### EJEMPLO 2 ######")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad, bienvenido !!")
    else:
        print("No puedes ingresar, lo siento :(")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarTuNombre(nombre, edad)
"""

# Ejemplo 3: tablas demultiplicar con funciones
print("###### EJEMPLO 3 ######")

def tabla(numero):
    print(f"\nTabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

print("\n")

tabla(3)
tabla(7)

# Ejemplo 3.1 : todas las tablas del 1 al 10
for numero_tabla in range(1,11):
    tabla(numero_tabla)

# Ejemplo 4: 
print("\n###### EJEMPLO 4 ######")

# Parametros opcionales
def getEmpleado(nombre, dni = "1007429794"):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"DNI: {dni}")

getEmpleado("Santiago Perez")

# Ejemplo 5: 
print("\n###### EJEMPLO 5 ######")

def calculadora(numero1, numero2, basicas = None):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"
    return cadena

print(calculadora(5,5))

# Ejemplo 6: Funciones dentro de otras funciones
print("\n###### EJEMPLO 6 ######")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"los apellidos son: {apellidos}"
    return texto
def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + " " + getApellidos(apellidos)
    return texto


print(getNombre("Santiago"), getApellidos("Perez"))
print(devuelveTodo("Santiago", "Perez Baldovino"))

# Ejemplo 7: Funcion lambda
print("\n###### EJEMPLO 7 ######")
"""
Las funciones lambda se crean en una sola linea de codigo
y son especificamente para tareas sencillas que se pueden
volver repetitivas, como: operaciones, lineas de codigo, etc.
"""
dime_el_year = lambda year: f"El año es {year*50}"

print(dime_el_year(2023))