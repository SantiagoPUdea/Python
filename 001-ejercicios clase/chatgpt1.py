import datetime
import random

class Paciente:
    def __init__(self, nombre, edad, genero, altura, peso, fecha):
        self.id = None
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura
        self.peso = peso
        self.__fecha = fecha
        #self.medicina = medicina
    
    def verFecha(Self):
        return Self.__fecha
    def asignarFecha(self, fecha):
        self.__fecha = fecha
    def imprimir_paciente(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")
        print(f"Fecha de ingreso: {self.verFecha()}")
        #print(f"Medicina: {self.medicina}")

    def actualizar_paciente(self, nombre=None, edad=None, genero=None, altura=None, peso=None, fecha= datetime.datetime.now()):
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if genero:
            self.genero = genero
        if altura:
            self.altura = altura
        if peso:
            self.peso = peso
        if fecha:
            self.__fecha = fecha
class Medicamento:
    def __init__(self, dosis):
        self.nombre = None
        self.dosis = dosis
    
    def imprimir_medicamentos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Dosis: {self.dosis}")
    def actualizar_medicamento(self, dosis=None):
        if dosis:
            self.dosis = dosis

class Sistema:
    def __init__(self):
        self.pacientes = {}
        self.medicamentos = {}
    def agregar_paciente(self, id_paciente, paciente):
        paciente = self.pacientes.get(id_paciente)
        if paciente:
            if not paciente.id:
                paciente.id = input("Ingresa el id del paciente: ")
                self.pacientes[paciente.id] = paciente
                print("\nIngresado con exito.")
        else:
            print("YA EXISTE PAPITO")
    def agregar_medicamento(self, medicamento):
        if not medicamento.nombre:
            medicamento.nombre = input("Ingrese el nombre del medicamento: ")
        self.medicamentos[medicamento.nombre] = medicamento

    def imprimir_pacientes(self):
        for id_paciente, paciente in self.pacientes.items():
            print(f"Paciente con ID: {id_paciente}")
            paciente.imprimir_paciente()
            print("-"*40)
    def imprimir_medicamentos(self):
        for nombre_med, medicamento in self.medicamentos.items():
            print(f"Medicamento con el nombre: {nombre_med}")
            medicamento.imprimir_medicamentos()
            print("-"*40)

    def actualizar_paciente(self, id_paciente, nombre=None, edad=None, genero=None, altura=None, peso=None, fecha= None):
        paciente = self.pacientes.get(id_paciente)
        if paciente:
            paciente.actualizar_paciente(nombre, edad, genero, altura, peso, fecha)
            self.pacientes[id_paciente] = paciente
            print(f"Paciente con ID: {id_paciente} actualizado con éxito")
        else:
            print(f"No se encontró el paciente con ID: {id_paciente}")
    
    def pedir_informacion(self, nombre=None, edad=None, genero=None, altura=None, peso=None, fecha = None):
        nombre = input("\nNuevo nombre del paciente: ")
        edad = int(input("Nueva edad del paciente: "))
        genero = input("Genero: ")
        altura = input("Altura: ")
        peso =  int(input("Peso del paciente: "))
        fecha = datetime.datetime.now()
        """
        fecha_ingreso = datetime.datetime.now() 
        numero = int(input("Cantidad de med a ingresar: "))
        if numero <= 15:
            nm = int(input("Ingrese cuantos medicamentos va suministar: "))
            for i in range(0,nm):    
                nombre_medic = input("Ingresa nombre del medicamento: ")
                dosis = input("Ingresa la dosis ")
                med.asignarNombre(nombre_medic)
                med.asignarDosis(dosis)
                dbMedicamentos.insert(med.verNombre(), med)
                i += 1
        """
        return nombre, edad, genero, altura, peso, fecha
        
# Ejemplo de uso
sistema = Sistema()

# Creamos un paciente y lo agregamos al sistema
paciente1 = Paciente("Juan", 30, "Masculino", 1.70, 75, datetime.datetime.now())
paciente2 = Paciente("Lucho", 22, "Masculino", 1.65, 83, datetime.datetime.now())
paciente3 = Paciente("Ana Cristina", 19, "Femenino", 1.54, 50, datetime.datetime.now())
sistema.agregar_paciente(1234, paciente1)
sistema.agregar_paciente(123, paciente2)
sistema.agregar_paciente(11, paciente3)
nm = int(input("\nNumero de medicamentos a ingresar: "))
i = 1
while i < nm:
    print(f"\nDigite la informacion del #{i} medicamento.")
    random_num = random.randint(1, 50)
    medicamento1 = Medicamento(random_num)
    sistema.agregar_medicamento(medicamento1)
    i += 1
# Imprimimos la lista de pacientes en el sistema
sistema.imprimir_pacientes()
sistema.imprimir_medicamentos()

# Actualizamos un paciente existente
ingresa = input("Ingresa el id a buscar: ")
if ingresa:
    variables = sistema.pedir_informacion(nombre=None, edad=None, genero=None, altura=None, peso=None, fecha=None)
sistema.actualizar_paciente(ingresa, nombre= variables[0], edad= variables[1], genero= variables[2], altura= variables[3], peso= variables[4], fecha = variables[5])

# Imprimimos la lista de pacientes actualizada
paciente4 = Paciente("Juan", 30, "Masculino", 1.70, 75, datetime.datetime.now())
sistema.agregar_paciente(11, paciente4)
sistema.imprimir_pacientes()