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
    Jugador('Juan','Base',0),
    Jugador('Anselmo','Alero-Pivot',14),
    Jugador('Pedro','Pivot',8)
]

"""
    MAP
    ---
    Toma una función y una lista y aplica esa función a cada elemento de esa lista, produciendo una nueva lista.
    Aquí aplicamos una función a cada elemento de una lista y en filter, aplicamos una condición.
"""

# crear un función para saber que comisión por puntos se lleva cada jugador
def calcular(jugador):
    if jugador.puntos > 10:
        jugador.puntos = str(jugador.puntos) + ' y gana una comisión por partido ' + str(jugador.puntos * 30) + '€'
    elif jugador.puntos == 0:
        jugador.puntos = str(jugador.puntos) + ' no sirves, vete al banquillo'

    jugador.nombre = jugador.nombre.upper()

    return jugador

# Map, aplicar a cada elemento de la lista, la función calcular
jugadoresYcomision = map(calcular,jugadores_del_equipo)

for comision in jugadoresYcomision:
    print(comision)