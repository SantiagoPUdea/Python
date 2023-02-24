# Programacion orientada a objetos (POO O OOP)

# Definir una clase
# (coche) con caracteristicas similares)

class Coche:
    color = "Rojo"
     # Atributos o propuiedades (variables)
     # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 426
    caballaje = 752
    plazas = 2

     # Metodos, son acciones que hace el objeto(coche)(funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
     
    def getVelocidad(self):
        return self.velocidad

# fin definicion clase

# Crear Objetos / Instanciar la clase
coche = Coche()
print("COCHE 1:")

coche.setColor("amarillo")
coche.setModelo("AMG45")

print(coche.marca, coche.getColor(), coche.getModelo())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Nueva velocidad: ", coche.velocidad)

print("---------------------------")
# Crear mas objetos
coche2 = Coche()

coche2.setMarca("Lamborguini")
coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print("COCHE 2:")
print(coche2.getMarca(),coche2.getColor(), coche2.getModelo())
