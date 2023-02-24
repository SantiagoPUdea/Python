class Paciente:
    def __init__(self, nombre, edad, peso, estatura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Estatura: {self.estatura} m")

def main():
    pacientes = []
    n = int(input("Ingrese la cantidad de pacientes que desea registrar: "))
    for i in range(n):
        print(f"\nIngrese los datos del paciente {i + 1}:")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        peso = float(input("Peso (kg): "))
        estatura = float(input("Estatura (m): "))
        paciente = Paciente(nombre, edad, peso, estatura)
        pacientes.append(paciente)

    print("\nDatos de los pacientes registrados:")
    for i, paciente in enumerate(pacientes):
        print(f"\nPaciente {i + 1}:")
        paciente.mostrar_datos()

if __name__ == "__main__":
    main()