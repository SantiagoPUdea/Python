class Mascota:
    def __init__(self, nombre, num_historia, tipo, peso, fecha_ingreso, medicamento):
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

    def getInfoPac(self, clave):
        recorre = self.get(clave)
        info = "\n----- Informacion del estudiante-------"
        info += "\n Nombre: " + recorre.verNombre()
        info += "\n Apellido: " + recorre.verApellido()
        info += "\n Documento: " + recorre.verCodigo()
        info += "\n Correo: " + recorre.verEmail()
   
class DatabaseMascota:
    def __init__(self, nombre):
        self.__data_mascota = {}
        self.nombre = nombre

    def insert(self, key, value):
        self.__data_mascota[key] = value
    def verCantidadMascotas(self):
        return len(self.__data_mascota)

    def update(self, key, value):
        if key in self.__data_mascota:
            self.__data_mascota[key] = value
        else:
            print("No existe en la BD")

    def imprimeMascotas(self):
        mas = Mascota()
        mas.getInfoPac(mas.verNum_historia())

    def delete(self, key):
        if key in self.__data_mascota:
            del self.__data_mascota[key]
        else:
            print("No existe en la BD")

    def get(self, key):
        if key in self.__data_mascota:
            return self.__data_mascota.get(key)
        else:
            print("No existe en la BD")

    def get_all(self):
        return list(self.__data_mascota.values())

def main(saludo = input("Hola, por favor ingrese su nombre: ")):
    while True:
        dbMascotas = DatabaseMascota("")
        print("\n------------ Ingreso al programa de Profesores -----------")
            
        opcion = input("\nDesea agregar o obtener un dato? (agregar/obtener/editar/eliminar/salir): \n")

        if opcion == "agregar":
            if dbMascotas.verCantidadMascotas() <= 10:
                mas = Mascota("",0,"", 0, "", "")
                nombre = input("Ingresa el nombre de la mascota: ")
                num_historia = int(input("Ingresa el N° historia clinica: "))
                tipo = input("Que tipo de mscota es: ")
                peso = int(input("Ingresa el peso: "))
                fecha_ingreso = input("Ingresa Fecha de ingreso: ")
                medicamento = input("Ingresa medicamento: ")
                mas.asignarNombre(nombre)
                mas.asignarNum_historia(num_historia)
                mas.asignarTipo(tipo)
                mas.asignarPeso(peso) 
                mas.asignarFecha_ingreso(fecha_ingreso)     
                mas.asignarMedicamento(medicamento)            
                dbMascotas.insert(mas.verNum_historia(), mas)
                
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