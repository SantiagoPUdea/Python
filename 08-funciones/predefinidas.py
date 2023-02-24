

nombre = "Santiago Perez"
cedula = 1007429794
talla = 112.15
# funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(cedula, int)
if comprobar:
    print(f"Esa variable es un numero entero {cedula}")
else:
    print("No es un numero entero")

if not isinstance(talla, float):
    print("La variable no es un numero con decimales")
else:
    print("Es un decimal")

# Limpiar espacios
frase = "     mi  contenido     "
print(frase.strip())


# Eliminar variables
year = 2022
print(year)
del year

# Comprobar variable vacia, contar los caracteres de un string
texto = " ff  "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print(f"La variable tiene contenido: {len(texto)}")


# Encontrar caracteres



# Reemplazar variables en un string


# Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())    