cantantes = ["2pac", "adele", "totoy", "ryan castro"]
numeros = [1,3,5,6,8,9,4]

# Ordenar
numeros.sort()
print(numeros)


# Añadir elementos
#print(cantantes)
cantantes.append("chockquicktown")
cantantes.insert(3 ,"diomedez")
numeros.append(2)
numeros.append(7)
#print(cantantes)


# Eliminar elementos
#print(cantantes)
cantantes.pop(1)
cantantes.remove("diomedez")


# Dar la vuelta
#print(numeros)
numeros.reverse()
#print(numeros)


# Contar los elementos de la lista
print(cantantes)
print(len(cantantes))

# Cuantas veces esta un elemento en una lista
numeros.append(1)
print(numeros.count(1))

# Conocer el indice del elemento
print(cantantes.index("totoy"))