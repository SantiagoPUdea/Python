"""
Crear un alista con el cont4enido de esta tabla:
ACCION        AVENTURA        DEPPORTES
GTA             ASSASINS        FIFA 23
COD             CRASH           MOTO GP
BLACK       prince of persia    ASPHALT 8
PUGB            super mario     NBA2K23
WARZON          SPIDERMAN       ULTIMATE 
"""

print("########### Coleccion de juegos ##########")
coleccion = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", " BLACK", "PUGB", " WARZON"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSASIN", "CRASH", "prince of persia", "super mario", "SPIDERMAN"]
    },
    {
        "categoria": "ACCION",
        "juegos": ["FIFA 23", "MOTO GP", "ASPHALT 8", "NBA2K23", "ULTIMATE"]
    }
]
   
for categoria in coleccion:
    print(f"------------{categoria['categoria']}-----------")
    for juego in categoria['juegos']:
        print(juego)
