"""
    Filtrar datos de Jugadores de Basket
"""

# clase para los jugadores(nombre, posicion, puntos)
class Jugador:
    # función constructor
    def __init__(self,nombre,posicion,puntos):
        self.nombre = nombre
        self.posicion = posicion
        self.puntos = puntos

    # función string, devolver un string de los datos en la función
    def __str__(self):
        return f'{self.nombre} tiene la posición de {self.posicion} en el equipo, y sus puntos por partido son {self.puntos}.'


    

# instanciar 5 jugadores
jugadores_del_equipo = [
    Jugador('Tomas','Pivot',22),
    Jugador('Pepe','Alero',9),
    Jugador('Juan','Base',4),
    Jugador('Anselmo','Alero-Pivot',14),
    Jugador('Pedro','Pivot',8)
]

# Filtrar los jugadores con une media de puntos superior a 10
filtro_sup_diez = filter(lambda masDiez: masDiez.puntos > 10,jugadores_del_equipo)

for jugador_puntos in filtro_sup_diez:
    print(jugador_puntos)