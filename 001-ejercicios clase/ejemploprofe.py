class Persona():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

    def asignarNombre(self,nombre):
        self.__nombre = nombre
    def asignarCedula(self,cedula):
        self.__cedula = cedula
    def asignarGenero(self,genero):
        self.__genero = genero

    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    
    def borrarNombre(self):
        del self.__nombre
    def borrarCedula(self):
        del self.__cedula
    def borrarGenero(self):
        del self.__genero

class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = ""

    def asignarServicio(self, servicio):
        self.__servicio = servicio
    def verServicio(self):
        return self.__servicio
       
class Empleado_Hospital(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__turno = ''

    def asignarTurno(self, turno):
        self.__turno = turno

    def verturno(self):
        return self.__turno
    
    def getInfoEmp(self):
        info = "\n----- Informacion del empleado -------"
        info += "\n Nombre: " + self.verNombre()
        info += "\n Cedula: " + self.verCedula()
        info += "\n Genero: " + self.verGenero()
        info += "\n Turno: " + str(self.verturno())

        return info

class Enfermera(Empleado_Hospital):
    def __init__(self):
        # Empleado_Hospital.__init__(self) # Invocando el constructor de la clase padre de la cual esta heredando 
        super().__init__() # Este metodo hace exactamente lo mismo que le anterior, invocar el constructor de la clase padre 
        self.__rango = ''

    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self):
        return self.__rango
    def getInfoEnf(self):
        info = "\n----- Informacion de la enfermera -------"
        info += "\n Nombre: " + self.verNombre()
        info += "\n Cedula: " + self.verCedula()
        info += "\n Genero: " + self.verGenero()
        info += "\n Rango: " + self.verRango()

        return info

class Medico(Empleado_Hospital):
    def __init__(self):
        Empleado_Hospital.__init__(self)
        
        self.__especialidad = ''
    
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = ''
    def verEspecialidad(self, especialidad):
        return self.__especialidad
    def getInfoMed(self):
        info = "\n----- Informacion del medico -------"
        info += "\n Nombre: " + self.verNombre()
        info += "\n Cedula: " + self.verCedula()
        info += "\n Genero: " + self.verGenero()
        info += "\n Servicio: " + self.verEspecialidad()

        return info

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
class Sistema:
    def __init__(self):
        self.__dict_pacientes = {}
        self.__dict_enfermeras = {}
        self.__dict_empleados = {}
        self.__dict_medicos = {}
 
    
    def ingresarPaciente(self, pac):
        self.__dict_pacientes[pac.verCedula] = pac
        
    def ingresarEnfermera(self, enf):
        self.__dict_enfermeras[enf.verCedula] = enf
     
    def ingresarEmpleado(self, emp):
        self.__dict_empleados[emp.verCedula] = emp
        
    def ingresarMedico(self, med):
        self.__dict_medicos[med.verCedula] = med

    def verDatosPacientes(self, c):
        for c in self.__dict_pacientes:
            return self.__dict_pacientes.get(c), self.getInfoPac(self.verDatosPacientes)
        else:
            print("No encontrado")
    
    def getInfoPac(self, pac):
        
        info = "\n----- Informacion del páciente-------"
        info += "\n Nombre: " + self.verNombre(pac)
        info += "\n Cedula: " + self.verCedula(pac)
        info += "\n Genero: " + self.verGenero(pac)
        info += "\n Servicio: " + str(self.verServicio(pac))

        return info

def main():
    sis = Sistema()
    while True:
        print(f"""      ---------  Hola que tal -----------
        !!! Has ingreado al Sistema central de datos San Buenaventura !!!

        1. Nuevo registro.
        2. Ver la informacion de un paciente.
        3. Eliminar a un paciente.
        4. Salir.
        """)
        menu = int(input("\nSelecciona una opcion: "))

        if menu == 1:  # Opciones para nuevo ingreso
            print("""\n
            Seleccione una opcion: 
            1. Ingresar un paciente.
            2. Ingresar enfermera.
            3. Ingresar empleado.
            4. Ingresar medico.
            5. Regresar al menu principal
            5. Salir.
            """)
            opcion = int(input("\nSelecciona una opcion: "))
        
            # Se crea un objeto Paciente
            if opcion == 1:  # Ingrear Paciente
                print("Digite los datos del paciente. \n")
                nombre = input("Nombre completo: ")
                cedula = input("Cedula: ")
                genero = input("Genero: ")
                servicio = input("Area de servicio: ")
                pac = Paciente()
                pac.asignarNombre(nombre)
                pac.asignarCedula(cedula)
                pac.asignarGenero(genero)
                pac.asignarServicio(servicio)

                sis.ingresarPaciente(pac.g)

            elif opcion == 2:  # Ingrear Enfermera
                print("Digite los datos de la enfermera. \n")
                nombre = input("Nombre completo: ")
                cedula = input(cedula)
                genero = input("Genero: ")
                rango = input("Rango: ")
                enf = Enfermera()
                enf.asignarNombre(nombre)
                enf.asignarCedula(cedula)
                enf.asignarGenero(genero)
                enf.asignarRango(rango)

                sis.ingresarEnfermera(enf)

            elif opcion == 3:  # Ingresar Empleado
                
                nombre = input("Nombre completo: ")
                cedula = input(cedula)
                genero = input("Genero: ")
                turno = input("Turno: ")
                emp = Empleado_Hospital()
                emp.asignarNombre(nombre)
                emp.asignarCedula(cedula)
                emp.asignarGenero(genero)
                emp.asignarTurno(turno)

                sis.ingresarEmpleado(emp)

            elif opcion == 4:  # Ingrear Medico
                med = Medico()
                nombre = input("Nombre completo: ")
                cedula = input("Cedula: ")
                genero = input("Genero: ")
                especialidad = input("Especialidad: ")
                med = Medico()
                med.asignarNombre(nombre)
                med.asignarCedula(cedula)
                med.asignarGenero(genero)
                med.asignarEspecialidad(especialidad)

                sis.ingresarMedico(med)
                
            elif opcion == 5:  # Salir
                print(" ------ Gracias por utilizar nuestros servicios, vuelve pronto ;) -------")
        
        
        elif menu == 2:  # Opciones para ver la informacion de un paciente
            c = int(input("Ingrese la cedula a buscar: "))
            i = sis.verDatosPacientes(c)
            print(i)
            
            
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        
if __name__ == "__main__":
    main()

