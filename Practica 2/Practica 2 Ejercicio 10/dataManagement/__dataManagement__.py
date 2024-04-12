from functools import reduce

"""Iniciso 1 : 1. Generar una estructura todas las estadísticas asociadas a cada jugador o jugadora."""

def structure_data (names, goals, goals_avoided, assists):
    #El metodo zip me permite agrupar los elementos de las listas en el orden en el que estan ingresados
    #Es decir, el primero con el primero de todas las otras, el segundo con el segundo de todas las otras, y asi.
    return (list(zip(names, goals, goals_avoided,assists)))


"""Inciso 3 : Conocer el nombre del jugador o jugadora más influyente, esto se consigue sumando goles a favor, goles evitados y cantidad de asistencias."""

def mvp (goals, goals_avoided, assists):

    #Defino funciones en base al valor de los datos

    #1.5 para cada gol metido
    def mult_goals (data):
        return data * 1.5
    
    #1.25 para cada gol evitado
    def mult_avoided (data):
        return data * 1.25
    
    #1 para cada asistencia
    def mult_assists (data):
        return data * 1
    
    #Aplico un zip sobre las estructuras con los valores, donde a cada una le aplico un map con su respectiva funcion
    values = zip(map(mult_goals,goals), map(mult_avoided,goals_avoided),map(mult_assists,assists))
    influence = []
    for value in values:
        #Sumo los valores de cada una de las tuplas en values y la devuelvo en un auxiliar
        aux = reduce(lambda a,b: a + b, value)
        #Almaceno el auxiliar en la lista y luego la retorno en una tupla
        influence.append(aux)
    return tuple(influence)

"""Inciso 4 : Conocer el promedio de goles por partido del equipo en general. Dato: Se jugaron 25 partidos en la temporada."""

def match_medias(goals):
    total = reduce (lambda a,b : a + b,goals) / 25
    return total


"""Inciso 5 : Conocer el promedio de goles por partido del goleador o goleadora. Dato: Se jugaron 25 partidos en la temporada."""

def player_media (names,goals):
    
    def media (goals):
        return goals / 25
    
    return (zip (names,map (media,goals)))

