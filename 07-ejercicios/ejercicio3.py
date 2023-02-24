





print(" Ejemplo con el uso del while ")
print() 
contador = 1

while contador <= 60:
    print(f"{contador} x {contador} = {contador*contador}")
    contador += 1
else:
    print("#### Programa terminado ####")

contador = 1

print("Ejemplo mio")
while contador <= 60:
    resultado = int(contador*contador)
    print(f"El resultado de {contador} al cuadrado es {resultado}")
    contador += 1

print()

print(" Ejemplo con el uso del for ")
print("-------------------------------------------\n")
contador = 1

for contador in range(1,61):
    print(f"{contador} x {contador} = {contador*contador}")
    contador += 1
else:
    print("###### Operacion finalizada #####")