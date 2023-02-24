import datetime

class Mascota:
    def __init__(self, nombre,num_historia, tipo, peso, fecha_ingreso, medicamento):
        self.__nombre = nombre
        self.__num_historia = num_historia
        self.__tipo = tipo
        self.__peso = peso
        self.__fecha_ingreso = fecha_ingreso
        self.__medicamento = medicamento
    
    def verNombre(self):
        return self.__nombre
    def verNum_historia(self):
        return self.__num_historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha_ingreso(self):
        return self.__fecha_ingreso
    def verMedicamento(self):
        return self.__medicamento

    def asignarNombre(self, nombre):
        self.__nombre = nombre    
    def asignarNum_historia(self,num_historia):
        self.__num_historia = num_historia
    def asignarTipo(self, tipo):
        self.__tipo = tipo
    def asignarPeso(self, peso):
        self.__peso = peso
    def asignarFecha_ingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso
    def asignarMedicamento(self, medicamento):
        self.__medicamento = medicamento
    
    def imprimir_mascota(self):
        print(f"\nN° historia: {self.verNum_historia()}")
        print(f"Nombre: {self.verNombre()}")
        print(f"Tipo: {self.verTipo()}")
        print(f"Peso: {self.verPeso()}")
        print(f"Fecha de ingreso: {self.verFecha_ingreso()}")
        print(f"Medicamentos: {self.verMedicamento()}")

class Medicamento:
    def __init__(self, nombre,dosis):
        self.__nombre = nombre
        self.__dosis = dosis
  
    def __str__(self):
        return f"\n- Nombre: {self.__nombre},\n- Dosis: {self.__dosis}"
    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis

    def asignarNombre(self, nombre):
        self.__nombre = nombre    
    def asignarDosis(self, dosis):
        self.__dosis = dosis
    def imprimir_medicamentos(self):
        print(f"Dosis: {self.verDosis()}")
        print(f"Nombre: {self.verNombre()}")
     

class DatabaseMascota:
    def __init__(self, nombre):
        self.__data_mascota = {}
        self.nombre = nombre

    def insert(self, key, value):
        self.__data_mascota[key] = value
    def agregar_mascota(self, mascota):
        if mascota.verNombre():
            self.__data_mascota[mascota.verNombre()] = mascota
        else:
            print("!!!!!!! No hay med. encontrado !!!!!!!")
    def verCantidadMascotas(self):
        return len(self.__data_mascota)

    def update(self, key, value):
        if key in self.__data_mascota:
            self.__data_mascota[key] = value
        else:
            print("No existe en la BD")

        
    def imprimir_mascotas(self, clave):
        x = self.getMascota(clave)
        y = x.verNum_historia()
        for y, x in self.__data_mascota.items():
            print(f"Paciente con N°: {y}")
            x.imprimir_mascota()
            print("-"*40)

    def delete(self, key):
        if key in self.__data_mascota:
            del self.__data_mascota[key]
        else:
            print("No existe en la BD")

    def getMascota(self, key):
        if key in self.__data_mascota:
            return self.__data_mascota.get(key)
        else:
            print("No existe en la BD")

    def get_all(self):
        return list(self.__data_mascota.values())

class DatabaseMedicamento:
    def __init__(self, nombre):
        self.__data_medicamentos = {}
        self.nombre = nombre

    def agregar_medicamento(self, medicamento):
        if medicamento.verNombre():
            self.__data_medicamentos[medicamento.verNombre()] = medicamento
        else:
            print("!!!!!!! No hay med. encontrado !!!!!!!")

    def verCantidadMedicamentos(self):
        return len(self.__data_medicamentos)
    def verLista(self):
        return self.__data_medicamentos

    def update(self, key, value):
        if key in self.__data_medicamentos:
            self.__data_medicamentos[key] = value
        else:
            print("No existe en la BD")
    def imprimir_medicamentos(self):
        variable = self.verNombre()
        for variable, medicamento in self.__data_medicamentos.items():
            print(f"medicamento: {variable}")
            medicamento.imprimir_medicamentos()
            print("-"*40)
        

    def delete(self, key):
        if key in self.__data_medicamentos:
            del self.__data_medicamentos[key]
        else:
            print("No existe en la BD")
    

def main(saludo = input("Hola, por favor ingrese su nombre: ")):
    while True:
        dbMascotas = DatabaseMascota("Base de datos de las mnascotas")
        dbMedicamentos = DatabaseMedicamento("Base de datos de los medicamentos")
        print(f"\nHola {saludo} que hay de nuevo viejo")
        print("\n------------ Ingreso al programa -----------")
            
        opcion = input("\nDesea agregar o obtener un dato? (agregar/obtener/editar/eliminar/salir): \n")

        if opcion == "agregar":
            if dbMascotas.verCantidadMascotas() <= 10:
                mas = Mascota("", 0,"", 0, "", "")
                nombre = input("Ingresa el nombre de la mascota: ")
                num_historia = input("Digita el N° de historia: ")
                tipo = input("Que tipo de mscota es: ")
                peso = int(input("Ingresa el peso: "))
                fecha_ingreso = datetime.datetime.now() 
                nm = int(input("Ingrese cuantos medicamentos va suministar: "))
                i = 0
                while i < nm:
                    med = Medicamento("", 0)
                    i += 1
                    print(f"\nMedicamento #{i}")
                    nombre = input("Ingresa el nombre del med: ")
                    dosis = input("Ingresa la dosis: ")
                    med.asignarNombre(nombre)
                    med.asignarDosis(dosis)
                    dbMedicamentos.agregar_medicamento(med)
               
                mas.asignarNombre(nombre)
                mas.asignarNum_historia(num_historia)
                mas.asignarTipo(tipo)
                mas.asignarPeso(peso) 
                mas.asignarFecha_ingreso(fecha_ingreso)     
                mas.asignarMedicamento(med)            
                dbMascotas.agregar_mascota(mas)
                dbMascotas.imprimir_mascotas(mas.verNum_historia())
                print("")
                dbMascotas.imprimir_mascotas(mas.verNum_historia())
                #dbMedicamentos.imprimir_medicamentos()
            else:
                print("Sistema lleno, actualiza la base de datos.")
        elif opcion == "obtener":
            clave = input("Ingrese la clave del dato: ")
            valor = dbMascotas.get(clave)
            print(f"Esta es la informacion encontrada: \n{valor}")
        
        elif opcion == "editar":
            clave = input("Ingrese el N° de historia a buscar: ")
            valor = dbMascotas.get(clave)
            if valor:
                mas = Mascota("",0,"", 0, "", "")
                nombre = input("Ingresa el nombre de la mascota: ")
                tipo = input("Que tipo de mscota es: ")
                peso = int("Ingresa el peso: ")
                fecha_ingreso = input("Ingresa Fecha de ingreso: ")
                medicamento = input("Ingresa medicamento: ")
                mas.asignarNombre(nombre)
                mas.asignarNum_historia(clave)
                mas.asignarTipo(tipo)
                mas.asignarPeso(peso) 
                mas.asignarFecha_ingreso(fecha_ingreso)     
                mas.asignarMedicamento(medicamento)    
                dbMascotas.update(mas.verCodigo(), mas)
        elif opcion == "eliminar":
            clave = input("Ingrese el documento del profesor: ")
            valor = dbMascotas.get(clave)
            if valor:
                print(f"Ha eliminado al docente {nombre} - {clave} de la base de datos con exito.")
                dbMascotas.delete(clave)
    
            else:
                print("No existe el estudiantes en la BD")
    
        elif opcion == "salir":
            main ()
        else:
            print("Opción inválida")

    
    
if __name__ == "__main__":
    main()