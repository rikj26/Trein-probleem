import random

def random_traject(stations, connections): # stations: lijst met alle stations, connections: lijst met alle verbindingen
    current_station = random.choice(stations)
    traject = [current_station]
    while(len(traject) < 8):
        random_connection = random.choice(get_posssible_connections(current_station, connections))
        current_station = get_new_station(current_station, random_connection, stations)
        traject.append(current_station)
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