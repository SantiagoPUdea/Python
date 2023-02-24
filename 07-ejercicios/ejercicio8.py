"""
Ejercicio 8. El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han suspendido.

"""
contador = 1
aprobados = 0
suspendidos = 0
print("------")
numero_alumnos = int(input("\n¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = float(input(f"\nNota obtenida por el alumno '{contador}': "))
    if nota <= 5:
        aprobados +=1
    if nota >= 5:
        suspendidos += 1
    contador += 1
print(f"\nLa cantidad de reprobados es: {aprobados}")
print(f"\nLa cantidad de aprobados es: {suspendidos}")