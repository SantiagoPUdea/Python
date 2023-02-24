from ejemploprofe import Paciente, Medico, Enfermera, Persona

def main():
    listaPaciente = {}

    def verificarIngreso(ced):

        if ced in listaPaciente.keys():
            print(f"El paciente #{ced} ya existe en la base de datos.")
            return True
        else:
            return False
    def verificarEntero(a):
        while True:
            try:
                int(a)
                return(int(a))
            except:
                a=input("Oiga, eso que usted ingreso no es un numero, pilas pues, ingrese un numero ahora si: ")

    saludo = input("Ingresa tu nombre: ")
    print(f"""      ---------  Hola que tal, {saludo} -----------
    !!! Has ingreado al Sistema central de datos San Buenaventura !!!

    1. Ingresar un paciente.
    2. Ver la informacion de un paciente.
    3. Eliminar a un paciente.
    4. Salir.
    """
    )

    menu = verificarEntero(input("\nSelecciona una opcion: "))

    while menu<1 or menu>4:
        menu = verificarEntero(input("!! Opcion invalida, vuelve a intentarlo: "))

    if menu == 1:
        cedula = verificarIngreso(input("ingresa la cedula del paciente: "))
        if cedula == True:
            cedula = verificarIngreso(input("ingresa la cedula del paciente: "))
        else:
            print("""\nSeleccione una opcion: 
            1. Ingresar un paciente.
            2. Ingresar enfermera.
            3. Ingresar medico.
            4. Salir.
            """)
            menu = verificarEntero(input("\nSelecciona una opcion: "))
            
            while menu<1 or menu>4:
                menu = verificarEntero(input("\n!! Opcion invalida, vuelve a intentarlo: "))
            
            # Se crea un objeto Paciente
            if menu == 1:
                paciente = Paciente()
                nombre = input(paciente.asignarNombre("Nombre completo: "))
                cedula = input(paciente.asignarCedula("Cedula: "))
                genero = input(paciente.asignarGenero("Genero: "))
                servicio = input(paciente.asignarServicio("Area de servicio: "))

                listaPaciente[paciente.verCedula] = paciente.getInfo()
                print(listaPaciente[paciente.verCedula])
              
    elif menu == 2:
        pass
    elif menu == 2:
        pass
    elif menu == 4:
        pass