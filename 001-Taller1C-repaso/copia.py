from archivo import *

def main(saludo = input("Hola, por favor ingrese su nombre: ")):
    while True:

        dbMateriasT = DatabaseMateriasTronco("Base datos - materias de tronco comun")
        dbMateriasC = DatabaseMateriasCarrera("Base datos - materias de carrera")
        dbElectivas = DatabaseElectivas("Base datos - electivas")
        dbEstudiantes = DatabaseEstudiantes("")
        dbProfesores = DatabaseProfesores("")
        dbSolicitudes = DatabaseSolicitudes("")
        menu = Menu()
        menu.mostrar_menu_general()
        opcion = input("\nSelecciona una opcion: ")
        if opcion == "1":
            while True:
                menu.mostrar_menu_estudiantes()
                opcion = input("Seleccione una opcion: ")
                result = menu.ejecutar_opcion_estudiante(opcion)
               
                if result == "self":
                    estu = menu.agregar_estudiante()
                    dbEstudiantes.insert(estu.verCodigo(), estu)
                    
                elif opcion == "obtener":
                    clave = input("\nIngrese el documento del estudiante: ")
                    valor = dbEstudiantes.get(clave)
                    if valor:
                        print(dbEstudiantes.getInfoPac(clave))
                    else:
                        print("No se encontro al estudiante en el sistema.")
                
                elif opcion == "editar":
                    clave = input("Ingrese el documento del estudiante: ")
                    valor = dbEstudiantes.get(clave)
                    if valor:
                        result = menu.editar_estudiante(clave)
                    else:
                        print("No se encontro al estudiante en el sistema.")
                    dbEstudiantes.update(clave, result)
                    print(f"Actualizacion: \n{dbEstudiantes.getInfoPac(clave)}")

                elif opcion == "eliminar":
                    clave = input("Ingrese el documento del estudiante: ")
                    valor = dbEstudiantes.get(clave)
                    if valor:
                        print(f"El estudiante con la siguiente informacion: \n{dbEstudiantes.getInfoPac(clave)},\nfue eliminado con exito")
                        result = dbEstudiantes.delete(clave)
                    else:
                        print(f"El estudiante {clave} no se encontra en el sistema.")
                    
            
                elif opcion == "salir":
                    main ()
                else:
                    print("Opción inválida")
            else:
                print("")
        elif opcion == "2": # Profesores
            print("\n------------ Ingreso al programa de Profesores -----------")
            while True:
                opcion = input("\nDesea agregar o obtener un dato? (agregar/obtener/editar/eliminar/salir): \n")

                if opcion == "agregar":

                    pro = Profesores("","","","")
                    nombre = input("Ingresa el nombre: ")
                    apellido = input("Ingresa el apellido: ")
                    codigo = input("Ingresa documento del docente: ")
                    especialidad = input("Ingresa especialidad: ")
                    pro.asignarNombre(nombre)
                    pro.asignarApellido(apellido)
                    pro.asignarCodigo(codigo)
                    pro.asignarEspecialidad(especialidad)        
                    dbProfesores.insert(pro.verCodigo(), pro.getInfoPro())
            
                elif opcion == "obtener":
                    clave = input("Ingrese la clave del dato: ")
                    valor = dbProfesores.get(clave)
                    print(f"Esta es la informacion encontrada: \n{valor}")
                
                elif opcion == "editar":
                    clave = input("Ingrese el documento del docente: ")
                    valor = dbProfesores.get(clave)
                    if valor:
                        profe = Profesores("","","","")
                        nombre = input("Ingresa el nombre: ")
                        apellido = input("Ingresa el apellido: ")
                        especialidad = input("Ingresa especialidad: ")
                        profe.asignarNombre(nombre)
                        profe.asignarApellido(apellido)
                        profe.asignarEspecialidad(especialidad)  
                        profe.asignarCodigo(clave)      
                        dbProfesores.update(profe.verCodigo(), profe.getInfoPro())
                elif opcion == "eliminar":
                    clave = input("Ingrese el documento del profesor: ")
                    valor = dbProfesores.get(clave)
                    if valor:
                        print(f"Ha eliminado al docente {nombre} - {clave} de la base de datos con exito.")
                        dbProfesores.delete(clave)
            
                    else:
                        print("No existe el estudiantes en la BD")
            
                elif opcion == "salir":
                    main ()
                else:
                    print("Opción inválida")
        elif opcion == "3":  # Materia de tronco comun
            print("------------ Ingreso al programa de Materias de tronco comun -----------")
            while True:
                opcion = input("¿Desea agregar o obtener un dato? (agregar/obtener/editar/eliminar/salir)")

                if opcion == "agregar":

                    mat = MateriasTroncoComun()
                    nombre = input("Ingresa: ")
                    codigo = input("Ingresa codigo: ")
                    horario = input("Ingresa nombre: ")
                    mat.asignarNombre(nombre)
                    mat.asignarCodigo(codigo)
                    mat.asignarHorario(horario)        
                    dbMateriasT.insert(mat.verCodigo(), mat.getInfoMateria())
            
                elif opcion == "obtener":
                    clave = input("Ingrese la clave del dato: ")
                    valor = dbMateriasT.get(clave)
                    print(f"El valor del dato es: {valor}")
                
                elif opcion == "editar":
                    clave = input("Ingrese el codigo de la materia: ")
                elif opcion == "eliminar":
                    pass
                elif opcion == "salir":
                    break
                else:
                    print("Opción inválida")




        elif opcion == "6":
            print("Fin del programa")
         
        else:
            print("vacio")
        
if __name__ == "__main__":
    main()