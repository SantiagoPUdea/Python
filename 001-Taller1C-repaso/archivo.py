class Materias:
    def __init__(self, codigo, nombre, horario):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__horario = horario
    
    def verCodigo(self):
        return self.__codigo
    def verNombre(self):
        return self.__nombre
    def verHorario(self):
        return self.__horario

    def asignarCodigo(self, codigo):
        self.__codigo = codigo
    def asignarNombre(self, nombre):
        self.__nombre = nombre
    def asignarHorario(self, horario):
        self.__horario = horario
    def getInfoMateria(self):
        
        info = "\n----- Informacion del curso -------"
        info += "\n Nombre: " + self.verNombre()
        info += "\n Codigo: " + self.verCodigo()
        info += "\n Horario: " + self.verHorario()
        
        return info

class MateriasCarrera(Materias):
    def __init__(self, codigo, nombre, horario, version):
        super().__init__(codigo, nombre, horario, version)
        self.__version_pensum = version

    def verVersion(self):
        return self.__version_pensum    
    def asignarVersion(self, version):
        self.__version_pensum = version

    def getInfoMateriaCarrera(self): 
        info = "\n----- Informacion de la materia Electiva -------"
        info += "\n Codigo: " + self.verCodigo()
        info += "\n Nombre: " + self.verNombre()
        info += "\n Horario: " + self.verHorario()
        info += "\n Creditos aprobados: " + self.verVersion()
        return info

class MateriasTroncoComun(Materias):
    def __init__(self, codigo, nombre, horario):
        super().__init__(codigo, nombre, horario)
    def getInfoMateriaTronco(self): 
        info = "\n----- Informacion de la materia del tronco comun -------"
        info += "\n Codigo: " + self.verCodigo()
        info += "\n Nombre: " + self.verNombre()
        info += "\n Horario: " + self.verHorario()
        return info

class Electivas(Materias):
    def __init__(self, codigo, nombre, horario, creditos):
        super().__init__(codigo, nombre, horario, creditos)
        self.__creditos_a = creditos
    
    def verCreditos(self):
        return self.__creditos_a
    def asignarCreditos(self, creditos):
        self.__creditos_a = creditos
    
    def getInfoElec(self): 
        info = "\n----- Informacion de la materia Electiva -------"
        info += "\n Codigo: " + self.verCodigo()
        info += "\n Nombre: " + self.verNombre()
        info += "\n Horario: " + self.verHorario()
        info += "\n Creditos aprobados: " + self.verCreditos()
        return info

class Profesores:
    def __init__(self, nombre, apellido, codigo, especialidad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__codigo = codigo
        self.__especialidad = especialidad
    
    def verNombre(self):
        return self.__nombre
    def verApellido(self):
        return self.__apellido
    def verCodigo(self):
        return self.__codigo
    def verEspecialidad(self):
        return self.__especialidad

    def asignarNombre(self, nombre):
        self.__nombre = nombre    
    def asignarApellido(self, apellido):
        self.__apellido = apellido
    def asignarCodigo(self, codigo):
        self.__codigo = codigo
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = especialidad

    def getInfoPro(self):
        info = "\n----- Informacion del profesor -------"
        info += "\n Nombre: " + self.verNombre()
        info += "\n Apellido: " + self.verApellido()
        info += "\n Codigo: " + self.verCodigo()
        info += "\n Especialidad: " + str(self.verEspecialidad())
        return info

class Estudiante(Profesores):
    def __init__(self, nombre, apellido, codigo, email):
        super().__init__(nombre, apellido, codigo, email)
        self.__email = email
    
    def verNombre(self):
        return self.__nombre
    def verApellido(self):
        return self.__apellido
    def verCodigo(self):
        return self.__codigo
    
    def verEmail(self):
        return self.__email
    
    def asignarNombre(self, nombre):
        self.__nombre = nombre    
    def asignarApellido(self, apellido):
        self.__apellido = apellido
    def asignarCodigo(self, codigo):
        self.__codigo = codigo
    
    def asignarEmail(self, email):
        self.__email = email
    
    def getInfoEst(self): 
        info = "\n----- Informacion del estudiante -------"
        info += "\n Nombre: " + self.verNombre()
        info += "\n Apellido: " + self.verApellido()
        info += "\n Codigo: " + self.verCodigo()
        return info
    
class Solicitudes:
    def __init__(self, tipo, mensaje, radicado):
        self.__tipo = tipo
        self.__mensaje = mensaje
        self.__radicado = radicado
    
    def verTipo(self):
        return self.__tipo
    def verMensaje(self):
        return self.__mensaje
    def verRadicado(self):
        return self.__radicado
    
    def asignarTipo(self, tipo):
        self.__tipo = tipo
    def asignarMensaje(self, mensaje):
        self.__mensaje = mensaje
    def asignarRadicado(self, radicado):
        self.__radicado = radicado
    
    def getInfoSoli(self): 
        info = "\n----- Informacion del estudiante -------"
        info += "\n Nombre: " + self.verTipo()
        info += "\n Apellido: " + self.verMensaje()
        info += "\n Codigo: " + self.verRadicado()
        return info

class BuscadorObjeto:
    def buscar_objeto(self, codigo, base):
        if codigo in base:
            return base[codigo]
        else:
            raise KeyError("Key not found in database.")

class DatabaseMateriasTronco:
    def __init__(self, nombre):
        self.__data_tronco = {}
        self.nombre = nombre

    def insert(self, key, value):
        self.__data_tronco[key] = value

    def update(self, key, value):
        if key in self.__ata:
            self.__data_tronco[key] = value
        else:
            raise KeyError("Key not found in database.")

    def delete(self, key):
        if key in self.__data:
            del self.__data_tronco[key]
        else:
            raise KeyError("Key not found in database.")

    def get(self, key):
        if key in self.__data_tronco:
            return self.__data_tronco[key]
        else:
            raise KeyError("Key not found in database.")

    def get_all(self):
        return list(self.__data_tronco.values())

class DatabaseMateriasCarrera:
    def __init__(self, nombre):
        self.__data_carrera = {}
        self.nombre = nombre

    def insert(self, key, value):
        self.__data_carrera[key] = value

    def update(self, key, value):
        if key in self.__ata:
            self.__data_carrera[key] = value
        else:
            raise KeyError("Key not found in database.")

    def delete(self, key):
        if key in self.__data:
            del self.__data_carrera[key]
        else:
            raise KeyError("Key not found in database.")

    def get(self, key):
        if key in self.__data_carrera:
            return self.__data_carrera[key]
        else:
            raise KeyError("Key not found in database.")

    def get_all(self):
        return list(self.__data_carrera.values())

class DatabaseElectivas:
    def __init__(self, nombre):
        self.__data_electivas = {}
        self.nombre = nombre

    def insert(self, key, value):
        self.__data_electivas[key] = value

    def update(self, key, value):
        if key in self.__ata:
            self.__data_electivas[key] = value
        else:
            raise KeyError("Key not found in database.")

    def delete(self, key):
        if key in self.__data:
            del self.__data_electivas[key]
        else:
            raise KeyError("Key not found in database.")

    def get(self, key):
        if key in self.__data_electivas:
            return self.__data_electivas[key]
        else:
            raise KeyError("Key not found in database.")

    def get_all(self):
        return list(self.__data_electivas.values())

class DatabaseSolicitudes:
    def __init__(self, nombre):
        self.__data_solicitudes = {}
        self.nombre = nombre

    def insert(self, key, value):
        self.__data_solicitudes[key] = value

    def update(self, key, value):
        if key in self.__ata:
            self.__data_solicitudes[key] = value
        else:
            raise KeyError("Key not found in database.")

    def delete(self, key):
        if key in self.__data:
            del self.__data_solicitudes[key]
        else:
            raise KeyError("Key not found in database.")

    def get(self, key):
        if key in self.__data_solicitudes:
            return self.__data_solicitudes[key]
        else:
            raise KeyError("Key not found in database.")

    def get_all(self):
        return list(self.__data_solicitudes.values())

class DatabaseEstudiantes:
    def __init__(self,nombre):
        self.__data_estudiantes = {}
        self.nombre = nombre

    def insert(self, key, value):
        self.__data_estudiantes[key] = value

    def update(self, key, value):
        if key in self.__data_estudiantes:
            self.__data_estudiantes[key] = value
        else:
            raise KeyError("Key not found in database.")

    def delete(self, key):
        if key in self.__data_estudiantes:
            del self.__data_estudiantes[key]
        else:
            raise KeyError("Key not found in database.")

    def get(self, key):
        if key in self.__data_estudiantes:
            return self.__data_estudiantes.get(key)
        else:
            print("vacio")
    
    def getInfoPac(self, clave):
        recorre = self.get(clave)
        info = "\n----- Informacion del estudiante-------"
        info += "\n Nombre: " + recorre.verNombre()
        info += "\n Apellido: " + recorre.verApellido()
        info += "\n Documento: " + recorre.verCodigo()
        info += "\n Correo: " + recorre.verEmail()

        return info

    def get_all(self):
        return list(self.__data_estudiantes.values())

class DatabaseProfesores:
    def __init__(self, nombre):
        self.__data_profesores = {}
        self.nombre = nombre

    def insert(self, key, value):
        self.__data_profesores[key] = value

    def update(self, key, value):
        if key in self.__data_profesores:
            self.__data_profesores[key] = value
        else:
            print("No existe en la BD")

    def delete(self, key):
        if key in self.__data_profesores:
            del self.__data_profesores[key]
        else:
            print("No existe en la BD")

    def get(self, key):
        if key in self.__data_profesores:
            return self.__data_profesores.get(key)
        else:
            print("No existe en la BD")

    def get_all(self):
        return list(self.__data_profesores.values())

class Menu:
    def __init__(self):
        self.opciones_estudiantes = {
            "1": self.agregar_estudiante,
            "2": self.editar_estudiante,
            "3": self.imprimir_estudiantes,
            "4": self.eliminar_estudiante,
            "5": self.salir
        }
        """
        self.opciones_materias = {
            "1": self.agregar_materia,
            "2": self.editar_materia,
            "3": self.imprimir_materia,
            "4": self.eliminar_materia,
            "5": self.salir
        }
        self.opciones_profesores = {
            "1": self.agregar_profesores,
            "2": self.editar_profesores,
            "3": self.imprimir_profesores,
            "4": self.eliminar_profesores,
            "5": self.salir
        }
        self.opciones_solicitudes = {
            "1": self.agregar_solicitud,
            "2": self.editar_solicitudes,
            "3": self.imprimir_solicitudes,
            "4": self.eliminar_solicitud,
            "5": self.salir
        }
        
        """
    def mostrar_menu_estudiantes(self):
        print("Bienvenido al programa de registro estudiantil")
        print("1. Ingresar estudiante")
        print("2. Editar estudiante")
        print("3. Imprimir estudiantes")
        print("4. Eliminar estudiante")
        print("5. Salir")
    
    def mostrar_menu_profesores(self):
        print("Bienvenido al programa de registro docentes")
        print("1. Ingresar docente")
        print("2. Editar docente")
        print("3. Imprimir docentes")
        print("4. Eliminar docente")
        print("5. Salir")
    
    def mostrar_menu_materias(self):
        print("Bienvenido al programa de registro magistral")
        print("1. Ingresar materia")
        print("2. Editar docmateriaente")
        print("3. Imprimir materias")
        print("4. Eliminar materia")
        print("5. Salir")
    
    def mostrar_menu_solicitudes(self):
        print("Bienvenido al programa de solicitudes - Ssofi")
        print("1. Ingresar solicitud")
        print("2. Editar solicitud")
        print("3. Imprimir solicitud")
        print("4. Eliminar solicitud")
        print("5. Salir")

    def mostrar_menu_general(self):
        print("\nBienvenido al programa de registro de la UdeA.")
        print("1. Estudiantes")
        print("2. Profesores")
        print("3. Materias")
        print("4. Solicitudes Ssofi")
        print("5. Matricular un curso")
        print("6. Matricular un curso")

    def ejecutar_opcion_estudiante(self, opcion):
        if opcion in self.opciones_estudiantes:
            self.opciones_estudiantes[opcion]()
        else:
            print("Opción inválida")
    """
    def ejecutar_opcion_materias(self, opcion):
        if opcion in self.opciones_materias:
            self.opciones_materias[opcion]()
        else:
            print("Opción inválida")
    
    def ejecutar_opcion_profesores(self, opcion):
        if opcion in self.opciones_profesores:
            self.opciones_profesores[opcion]()
        else:
            print("Opción inválida")
    
    def ejecutar_opcion_solicitudes(self, opcion):
        if opcion in self.opciones_solicitudes:
            self.opciones_solicitudes[opcion]()
        else:
            print("Opción inválida")
    """
    def agregar_estudiante(self):
        nombre = input("\nIngrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido: ")
        codigo =  input("Ingrese el codigo del estudiante: ")
        email = input("Ingrese el email: ")
        est = Estudiante("","","","")
        est.asignarNombre(nombre)
        est.asignarApellido(apellido)
        est.asignarCodigo(codigo)
        est.asignarEmail(email) 
        dbEstudiantes = DatabaseEstudiantes("")
        dbEstudiantes.insert(est.verCodigo(), est)
        return dbEstudiantes

    def editar_estudiante(self):
        codigo = input("Ingrese el documento del estudiante: ")
        estu = Estudiante("","","","")
        nombre = input("Ingresa el nombre: ")
        apellido = input("Ingresa el apellido: ")
        email = input("Ingresa elemail: ")
        estu.asignarNombre(nombre)
        estu.asignarApellido(apellido)
        estu.asignarEmail(email)  
        estu.asignarCodigo(codigo)      
        return estu
    def eliminar_estudiante(self, codigo):
        clave = input("\nIngrese el documento del estudiante: ")
        valor1 = DatabaseEstudiantes("")
        valor1.get(clave)
        if valor1:
            print("Eliminado con exito")
            valor1.delete(codigo)
        else:
            print("No existe el estudiantes en la BD")
        
    
    def imprimir_estudiantes(self):
        clave = input("\nIngrese el documento del estudiante: ")
        valor = DatabaseEstudiantes("")
        valor.get(clave)
        if valor:
            print(valor.getInfoPac(clave))
        else:
            print("No se encontro al estudiante en el sistema.")
    def salir(self):
        pass


