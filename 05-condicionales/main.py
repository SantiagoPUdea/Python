"""

Es una estructura de control que me permite
controlar el flujo del programa, evaluando una 
condicion

# Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos
and Y
or O
! negacion
not No
"""

# Condicional IF
# Ejemplo 1
print("########## EJEMPLO 1 ############")  

color = "rojo"
#color = input(" Adivina cual es mi color favorito: ")

if color == 'rojo':
    print("Felicidades")
    print("El color es ROJO")
else:
    print("Color incorrecto !!")

# Ejemplo 2
print("\n########## EJEMPLO 2 ############") 

year = 2020
#year = int(input(" ¿En que año estamos?: "))

if year >= 2021:
    print(" Estamos de 2021 en adelante")
else: 
    print("Es un año anterior a 2021")


# Ejemplo 3
print("\n########## EJEMPLO 3 ############") 

nombre = "Santiago Perez"
ciudad = "Barranquilla"
Continente = "America"
edad = 19
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if Continente != "America":
        print("El usuario no es Americano")
    else:
        print(f"Es Americano y de {ciudad}")

else:
    print(f"{nombre} No es mayor de edad")


# Ejemplo 4
# Estructura de control ELIF

print("\n########## EJEMPLO 4 ############") 

dia = 7

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")

# Ejemplo 5
# 2 Condiciones en un if
print("\n########## EJEMPLO 5 ############") 

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("¿Tienes edad para trabajar? Introduce tu edad: "))
edad_oficial = 18

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("No esta en edad para trabajar")

# Ejemplo 6
# Uso de operadores logicos
print("\n########## EJEMPLO 6 ############") 

pais = "Suiza"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana :(")


# Ejemplo 7
# Operadores logicos de negacion
print("\n########## EJEMPLO 7 ############") 

pais = "Colombia"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO un pais habla hispana !!")
else:
    print(f"{pais} SI es un pais de habla hispana :(")


# Ejemplo 8
# Operadores logicos diferente
print("\n########## EJEMPLO 8 ############") 

pais = "Mexico"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO un pais habla hispana !!")
else:
    print(f"{pais} SI es un pais de habla hispana :(")