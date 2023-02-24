"""
 Pooo: Es un paradigma de programacion, en donde todo lo vamos a ver como objetos.
 La estructura es la siguiente:

Clase = Es el molde para crear los objetos
    Esta a su vez tiene atributos y metodos.

Atributos = Son las caracteristicas que va tener la clase, en este caso definimos
             los atributos de la clase Carro():
    - Marca         - N° Chasis
    - Color         - N° Puertas
    - Caballaje     - Euro

Metodos = Son las acciones que puede realizar la clase, en este caso definimos para
          la clase Carro():
    - Acelerar      - EncenderLuz
    - Frenar        - ApagarLuz
    - Estacionar    - SubirVentana

ABSTRACCION: Poder utilizar objeto sin necesidad de saber el funcionamiento interno de este,
puedo utilizar para que me haga una funcionalidad en concreto o para cierta tarea, utilizando
los metodos que tiene este definidos. Creo objetos para casos parecidos pero diferentes

HERENCIA: Las clases en la Poo pueden heredar unas de otros (metodos, atributos), por ejemplo 
una clase padre que tenga propiedades basicas de un vehiculo y una hijas que sean, Moto, carro,
tractocamion, Lancha, Helicoptero. Que van a heredar todas las clase Vehiculo(): y cada una tendra
sus atributos adicionales especificos.

MODULARIDAD: 

OCULTACION: Esto se refiere a que los datos de un objeto solo puedan ser modificados desde dentro, para
que estos atributos puedan ser modificados solo desde dentro de la clase que se encarguen de esto.

"""