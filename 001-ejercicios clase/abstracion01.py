class Persona:
    def __init__(self):
        self.__nombre = "Santiago"
        self.__cedula = 1007429794
        self.__genero = "Masculino"
        
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    
    def setCedula(self, cedula):
        self.__cedula = cedula
    def getCedula(self):
        return self.__cedula
    
    def setGenero(self, genero):
        self.__genero = genero
    def getGenero(self):
        return self.__genero

class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = "Hab-1987, Bloque 11"
        self.__list_paciente = []
        
    def setServicio(self, servicio):
        self.__servicio = servicio
    def getServicio(self):
        return self.__servicio
    
    def setPaciente(self, nombre, cedula, genero, servicio):
        self.__list_paciente.append(nombre, cedula, genero, servicio) 
    
    def getPaciente(self):
        return self.__list_paciente

    def getInfo(self):
        info = "\n----- Informacion del paciente-------"
        info += "\n Color: " + self.getNombre()
        info += "\n cedula: " + str(self.getCedula())
        info += "\n Genero: " + self.getGenero()
        info += "\n Servicio: " + self.getServicio()

        return info
    

class Enfermera():
    pass

class Medico:
    pass

g = Paciente()
print(g.getInfo())

nombre = g.setNombre("Lucho Torres")
cedula = g.setCedula(10072621)
genero = g.setGenero("Masculino")
servicio = g.setServicio("Hab 245- Bloque 43")

g.setPaciente(nombre, cedula, genero, servicio)
print(g.getPaciente())