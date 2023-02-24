"""
Ejercicio 4. 
Crear un script que tenga 4 variables: un alista, un string, un entero
y un booleano y imprima un mensaje segun el tipo de dato de cada variable. 
Usar funciones
"""
def tipoDato (dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = f"\nLa variable ingresada es del tipo: {type(dato)}"
        print("")
    else:
        print("\nEl tipo de dato no es correcto !!!")
    return result
    

mi_lista = ["Uruguay", "Peru", "Bolivia", "Panama"]
mi_string = "La verdad os hara libres"
mi_entero = 3124817542
mi_booleano = True


print(tipoDato(mi_lista, list))
print(tipoDato(mi_string, str))
print(tipoDato(mi_entero, int))
print(tipoDato(mi_booleano, list))