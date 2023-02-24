"""
Ejercicio 1. Hcer un programa que tenga una lista de 8 numeros enteros
y haga lo siguiente:
(hecho) - Recorrer la lista y mostrarla
(hecho) - Hacer funcion que recorra listas de numeros y devuelva un string
(hecho) - Ordenarla y mostrarla
(hecho) - Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

numeros = [23, 65, 98, 45, 74, 90, 43, 32]


# Hacer funcion que recorra listas de numeros y devuelva un string
def mostrarList (lista):  
    resultado = ""
    
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado

# Recorrer la ista y mostrarla
print("########### Recorrer y mostrar ############")


"""
for numero in numeros:
    print(numero)
"""

print(mostrarList(numeros))
# print(mostrarList(numeros))
# print(mostrarList(["Rodri", "Pepe", "Gustavo"]))

# Ordenarla y mostrarla
print("########### Ordenarla y mostarla ############")
numeros.sort()
print(mostrarList(numeros))

# Mostar la longitud
print("########### Longitud ############")
long_lista = len(numeros)
print(f"\nLa longitud de la lista es de: {str(long_lista)}")

# Busqueda en la lista
print("\n########### Busqueda en la lista ############")

busqueda = int(input("\nIntroduce el numero: "))

def compruebaEstancia (numero, lista):
    if numero in lista: 
        comprobar = isinstance(numero, int)
    else:
        print(f"!! El numero: {numero} no se encuentra en la lista") 
        return False    
    return comprobar  
resultado = (compruebaEstancia(busqueda, numeros))

# Un ciclo infinito hasta que el ususario ingrese un entero positivo
while not resultado or busqueda <= 0:
    busqueda = int(input("\nIntroduce el numero: "))
else:
    print(f"\nHas introducido el {busqueda} !!")

print(f"\n##### Buscar en la lista el numero {busqueda} ######")

search = numeros.index(busqueda)
print(f"\nEl numero buscado se encuntra en el indice: {search}")

 