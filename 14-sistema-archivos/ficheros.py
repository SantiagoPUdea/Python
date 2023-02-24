from io import open_code
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir
archivo.write("****** Soy un texto metido desde python********\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")                                           # LA VARIABLE R ES PARA LEER CONTENIDO

# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

"""
Leer contenido mediante for
for elemento in contenido:
    print(elemento)
"""

# Leer contenido y guardar en lista
lista = archivo_lectura.readline()
archivo_lectura.close

for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)
    if not frase.isnumeric():
        # print("- "+frase.upper())
        pass


 # Copiar
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = "../09-listas/fichero_copiado.txt"

shutil.copyfile(ruta_original, ruta_alternativa)