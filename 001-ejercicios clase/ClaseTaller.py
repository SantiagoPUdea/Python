def main():

  #Definir una base de datos
  db={123:"Pepito",1:"Juanita",2:"Ramon"}

  #Voy a definir las funciones secundarias
  def verificarIngreso(ced):
    if ced in db.keys():
      print("\nOe, si esta en la base de datos")
      return True
    else:
      print("Oe, no esta")
      return False
  
  def verificarEntero(a):
    while True:
      try:
        int(a)
        return(int(a))
      except:
        a=input("Oiga, eso que usted ingreso no es un numero, pilas pues, ingrese un numero ahora si: ")

  #Voy a definir un menu
  print("Hola, seleccione una opcion:\n  1. Ingresar\n  2. Salir")
  menu=verificarEntero(input("Seleccione una opcion: "))

  while menu<1 or menu>2:
    menu=verificarEntero(input("Oiga, esa no es una opcion valida, ingrese otra y no joda: "))

  #Desarrollamos el menu
  if menu==1:
    cedula=verificarEntero(input("Ingrese una cedula: "))
    ingreso=verificarIngreso(cedula)
    print('El resultado de la consulta fue: ',ingreso)
  elif menu==2:
    print("Listo, salgase pues")
  else:
    raise Exception("Algo paso y detengo el algoritmo")

main()