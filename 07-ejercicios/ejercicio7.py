"""
Ejercicio 8. ¿Cuanto es el x por ciento de x numero?
                        20% de 150
"""
numero = int(input("\nIngrese un numero: "))
porcentaje = int(input("\nIngrese el porcentaje que desea obtener: "))

resultado = (numero*porcentaje)/100
print(f"\nValor del descuento aplicado: {resultado}, menos el valor del articulo: {numero}\nLe queda en: {numero-resultado}")