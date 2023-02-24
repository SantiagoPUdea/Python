"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.

"""

pelicula = "Batman"

# Definir lista
peliculas= ["Batman", "Spiderman", "El señor de los anillos", "Avatar", "Chucky"]
cantantes = list(('2pac', 'Drake', 'Jenifer Lopez')) # Otro metodo para crear las listas
years = list(range(2020, 2050))
variada= ["Victor", 30202, 4.4, True, None]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# Indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])

# Reemplazar un indice
peliculas[1] = "Thor"
print(f"Cambio: {peliculas[1]}")
print(f"\nLa nueva lista es: {peliculas}")

# Añadir elemento a lista
cantantes.append("Kase o")
cantantes.append("Blessed  ")
print(cantantes)

# Recorrer lista

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n***********LISTADO PELICULAS************")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

# Lista multidimensionales
print("\n********* Listado de contactos *************")


