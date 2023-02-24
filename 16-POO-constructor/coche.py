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

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

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
    
    def getInfo(self):
        info = "\n----- Informacion del coche-------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info

Carro = Coche
print()