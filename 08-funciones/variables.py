"""
Variables locales: Se definend dentro de la funcion y no se puede usar 
fuera de ella, a no ser que hagamos un return

Variables globales: Se declaran fuera de una funcion y estan
disponibles dentro y fuera de ellas

"""

# Variable global
frase = "UN DIA SIN REIR, ES UN DIA PERDIDO"

print(frase)

def holaMundo():
    frase = "Hola mundo"
    print(frase)

    year = 2021       # Variable local: solo se puede usar dentro de la funcion
    print(year)

    return "Dato devuelto: " + str(year+1)

    website = "Sanperbal20112011@gmail.com"
    print("DENTRO: ", website)

print(holaMundo())
