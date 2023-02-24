class Objeto:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion}"

    def ingresar(self):
        self.id = int(input("Ingrese el ID: "))
        self.nombre = input("Ingrese el nombre: ")
        self.descripcion = input("Ingrese la descripción: ")
        print("El objeto ha sido ingresado.")

    def editar(self):
        self.nombre = input("Ingrese el nuevo nombre: ")
        self.descripcion = input("Ingrese la nueva descripción: ")
        print("El objeto ha sido editado.")

    def imprimir(self):
        print(self)

class Menu:
    def __init__(self, objeto):
        self.objeto = objeto
        self.lista_objetos = []

    def mostrar_menu(self):
        opcion = None
        while opcion != "5":
            print("---- MENU ----")
            print("1. Ingresar objeto")
            print("2. Editar objeto")
            print("3. Imprimir objetos")
            print("4. Eliminar objeto")
            print("5. Salir")
            opcion = input("Ingrese la opción: ")
            if opcion == "1":
                nuevo_objeto = self.objeto(0, "", "")
                nuevo_objeto.ingresar()
                self.lista_objetos.append(nuevo_objeto)
            elif opcion == "2":
                id = int(input("Ingrese el ID del objeto a editar: "))
                objeto_encontrado = self.buscar_objeto(id)
                if objeto_encontrado is not None:
                    objeto_encontrado.editar()
                else:
                    print("El objeto no existe.")
            elif opcion == "3":
                self.imprimir_objetos()
            elif opcion == "4":
                id = int(input("Ingrese el ID del objeto a eliminar: "))
                objeto_encontrado = self.buscar_objeto(id)
                if objeto_encontrado is not None:
                    self.lista_objetos.remove(objeto_encontrado)
                    print("El objeto ha sido eliminado.")
                else:
                    print("El objeto no existe.")
            elif opcion == "5":
                print("Hasta luego.")
            else:
                print("Opción no válida.")

    def buscar_objeto(self, id):
        for objeto in self.lista_objetos:
            if objeto.id == id:
                return objeto
        return None

    def imprimir_objetos(self):
        for objeto in self.lista_objetos:
            objeto.imprimir()

menu_objetos = Menu(Objeto)
menu_objetos.mostrar_menu()