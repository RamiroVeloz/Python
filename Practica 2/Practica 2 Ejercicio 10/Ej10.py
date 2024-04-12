import dataManagement.__dataManagement__ as dm

def show_players (data):
    for elem in data:
        print (f'Nombre: {elem[0]} - Goles realizados: {elem[1]} - Goles evitados: {elem[2]} - Asistencias: {elem[3]}')


"""Inciso 2 : Conocer el nombre y la cantidad de goles del goleador o goleadora."""

def search_player (data, op):
    if not(op.isalpha()):
        return('Error en la busqueda.')
    flag = False
    for elem in data:
        if (op == elem[0]):
            flag = True
            return (f'Nombre del jugador: {elem[0]} - Goles realizados: {elem [1]} - Goles evitados: {elem[2]} - Asistencias: {elem[3]}')
    if not flag:
        return (f"No se encontro al jugador {op}.")
    
def most_influence (player_influence):
    max = 0
    mvp = ""
    for elem in player_influence:
        if (elem[1] > max):
            max =  elem [1]
            mvp = elem[0]
    return (f'El o La jugadora mas valiosa es {mvp} con una influencia de: {max}')

def show_medias(players_medias):
    for elem in players_medias:
        print (f'Jugador/a: {elem[0]} - Promedio: {elem[1]}')

names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia, Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]

#Separo los nombres en una lista limpiando los caracteres y las comas
names = names.replace(',','').replace("'",'').replace("á",'a').replace("é",'e').replace("í",'i').replace("ó",'o').replace("ú",'u').upper().split()

"""Iniciso 1 : 1. Generar una estructura todas las estadísticas asociadas a cada jugador o jugadora."""

data = dm.structure_data(names,goals,goals_avoided,assists)
show_players(data)

"""Inciso 2 : Conocer el nombre y la cantidad de goles del goleador o goleadora."""

op = input ('Ingrese el nombre de un jugador o jugadora a buscar: ').upper()
player = search_player(data,op)
print (player)

"""Inciso 3 : Conocer el nombre del jugador o jugadora más influyente, esto se consigue sumando goles a favor, goles evitados y cantidad de asistencias."""
mvp = dm.mvp(goals,goals_avoided, assists)
#Hago zip entre los nombres y la tupla recibida en mvp, donde le asigno a cada jugador su influencia en los partidos
player_influence = zip (names,mvp)
print (most_influence(player_influence))


"""Inciso 4 : Conocer el promedio de goles por partido del equipo en general. Dato: Se jugaron 25 partidos en la temporada."""
match_media = dm.match_medias(goals)
print (f'El promedio de goles por partido es {match_media}')


"""Inciso 5 : Conocer el promedio de goles por partido del goleador o goleadora. Dato: Sejugaron 25 partidos en la temporada."""
players_medias = dm.player_media(names,goals)
show_medias(players_medias)

