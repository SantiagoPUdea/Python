"""
Diccionario:
Un tipo que almacena un conjunto de datos.
En formato clave > valor

"""

persona = {
    "nombre": "Santiago",
    "apellido": "Perez",
    "web": "santpb@gmail.com" 
}

print(persona["apellido"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'udea@udea.edu.co',
        'tamaño': '18 cm'
    },
    {
        'nombre':'Jose',
        'email': 'Salvador',
        'tamaño': '23 cm'
    },
    {
        'nombre': 'Salvador',
        'email': 'reydali2000@hotmail.com',
        'tamaño': '11 cm'
    }
]

contactos[0]['nombre'] = "Toñito"
print(contactos[0]['nombre'])

print("\nListado de contactos: ")
print("---------------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}, {contacto['tamaño']}")
    print(f"Email del contacto: {contacto['email']}")
    print("---------------------------------------------")