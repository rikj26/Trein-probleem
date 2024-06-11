import random

def random_traject(stations, connections): # stations: lijst met alle stations, connections: lijst met alle verbindingen
    current_station = random.choice(stations)
    traject = [current_station]
    previous_connection = None

    while(len(traject) < 8):
        possible_connections = get_posssible_connections(current_station, connections)

        if previous_connection and len(possible_connections) > 1: # Het moet niet mogelijk zijn om dezelfde connectie meteen terug te nemen
            possible_connections.remove(previous_connection)

        random_connection = random.choice(possible_connections)
        current_station = get_new_station(current_station, random_connection, stations)

        traject.append(current_station)
        previous_connection = random_connection
    
    return traject

def get_posssible_connections(station, connections): # connections: lijst met alle connections
    possible_connections = []
    for connection in connections:
        if connection.station1 == station.name or connection.station2 == station.name:
            possible_connections.append(connection)
    return possible_connections

def get_new_station(station, connection, stations): # stations: lijst met alle stations
    if station.name == connection.station1:
        for elem in stations:
            if elem.name == connection.station2:
                return elem
            
    if station.name == connection.station2:
        for elem in stations:
            if elem.name == connection.station1:
                return elem
