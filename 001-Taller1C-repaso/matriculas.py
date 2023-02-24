"""
1. DESCRIPCIÓN GENERAL DEL PROBLEMA:
El director de carrera necesita ayuda para la temporada de matrícula y ajustes para hacer más eficiente 
el proceso de ajustes forzosos y apertura de cupos en materias obligatorias de la carrera.

2. DESCRIPCIÓN ESPECÍFICA DEL PROBLEMA:
El jefe de carrera necesita ayuda para optimizar el proceso de los ajustes forzosos, normalmente la 
información que el maneja es la siguiente:

El jefe necesita que la información de las materias sea guardada con código, nombre completo, horario 
y versión de pensum (Para las materias de carrera), además de créditos aprobados necesarios (Para las electivas).

a. Materias de carrera:
Son las materias propias del programa, se identifican porque los grupos están compuestos únicamente 
por estudiantes de bioingeniería.

b. Materias de tronco común:
Son las materias compartidas con el resto de la facultad. Se identifican porque son las materias en las 
que se encuentran estudiantes de ingeniería sin importar la carrera.

c. Electivas:
Son las materias no obligatorias de la carrera y que ayudan a la formación integral del estudiante en 
distintos ámbitos profesionales y personales.

El jefe de carrera solicita que toda la información esté cotejada consigo misma y que constantemente 
se verifique que lo ingresado sí tenga sentido (validar la información), pues entre tantos datos puede 
enrredarse. Entre las acciones solicitadas con relevancia, pide que se cargue una lista de estudiantes 
a matricular ingresando el código de la materia en el buscador.

Por seguridad, se debe pedir una contraseña cuando se ingresa al programa, esta debe ser “123”. 
Además de la información de las materias, el jefe también necesita almacenar la siguiente información:

a. Estudiantes que solicitan cupos
Es la lista de los estudiantes que necesitan cupos. Se
necesita la información completa del estudiante además de
en qué materia/materias se necestian los cupos.
b. Horarios disponibles de los profesores
Es la lista de profes de la carrera y en qué horarios se
encuentran disponibles para poder abrir cupos nuevos.

b. Solicitudes al SSOFI
Es la lista de solicitudes que se suben al SSOFI para hacer otro tipo de ajustes, como exoneración 
de pre-requisito o solicitud de una materia en modalidad dirigida.

3. ACCIONES:
El programa a desarrollar debe ser capaz de gestionar en forma de aplicación CRUD todos los requerimientos 
de la empresa, además de que debe validar absolutamente todos los campos ingresados y adelantarse a posibles 
errores que el usuario pueda cometer. Se debe disponer de un menú para realizar las distintas acciones 
descritas.
"""

class Estudiante:
    def __init__(self, nombre, apellido, edad, codigo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.codigo = codigo
        self.materia = None
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.codigo})"

    def matricular_en_materia(self, materia):
        self.materia = materia

class Materia:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.estudiantes = []

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)

class Menu:
    def __init__(self):
        self.opciones = {
            "1": self.agregar_estudiante,
            "2": self.editar_estudiante,
            "3": self.imprimir_estudiantes,
            "4": self.eliminar_estudiante,
            "5": self.salir
        }
        self.materias = {"M001":"Matematicas", "M002" : "Info2"}
    
    def mostrar_menu(self):
        print("Bienvenido al programa de estudiantes y materias")
        print("1. Ingresar estudiante")
        print("2. Editar estudiante")
        print("3. Imprimir estudiantes")
        print("4. Eliminar estudiante")
        print("5. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion in self.opciones:
            self.opciones[opcion]()
        else:
            print("Opción inválida")

    def agregar_estudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        codigo = input("Ingrese el código del estudiante: ")

        estudiante = Estudiante(nombre, apellido, edad, codigo)
        print("Materias disponibles:")
        for materia in self.materias.values():
            print(materia)
        codigo_materia = input("Ingrese el código de la materia a matricular al estudiante: ")
        materia = self.materias.get(codigo_materia, None)
        if materia:
            materia.agregar_estudiante(estudiante)
            estudiante.matricular_en_materia(materia)
            print(f"El estudiante {estudiante} ha sido matriculado en la materia {materia}")
        else:
            print(f"No se encontró la materia con el código {codigo_materia}")

    def editar_estudiante(self):
        codigo_estudiante = input("Ingrese el código del estudiante a editar: ")
        materia_actual = None
        for materia in self.materias.values():
            for estudiante in materia.estudiantes:
                if estudiante.codigo == codigo_estudiante:
                    materia_actual = materia
                    break
            if materia_actual:
                break
        if materia_actual:
            nombre = input("Ingrese el nuevo nombre del estudiante: ")
            apellido = input("Ingrese el nuevo apellido del estudiante: ")
            edad = int(input("Ingrese la nueva edad del estudiante: "))
            estudiante = Estudiante(nombre, apellido, edad, codigo_estudiante)
            materia_actual.eliminar_estudiante(estudiante)
            self.materias[materia_actual.codigo].agregar_estudiante
    def imprimir_estudiantes(self):
        pass

    def eliminar_estudiante(self):
        pass

    def salir(self):
        pass

materia1 = Materia("M001", "Matemáticas")
materia2 = Materia("M002", "Historia")


menu = Menu()
print(menu.mostrar_menu())
print(menu.ejecutar_opcion('1'))




