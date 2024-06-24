import random
import copy

def random_traject(network, max_trajects, max_time):
    original_connections = copy.deepcopy(network.connections)
    
    while(len(network.trajects) < max_trajects and len(network.connections) != 0):
        traject = network.create_traject()
        random_connection = random.choice(network.connections)
        network.connections.remove(random_connection)

        traject.add_station(random_connection.station1)
        traject.add_station(random_connection.station2)
        traject.update_time(random_connection.time)

        while(traject.total_time <= max_time):
            current_station = traject.get_last_station()
            possible_connections = get_possible_connections(current_station, network.connections)
            
            if not possible_connections:
                break

            random_connection = random.choice(possible_connections)
            if random_connection.time + traject.total_time > max_time:
                break

            if current_station.name == random_connection.station1.name:
                traject.add_station(random_connection.station2)
            elif current_station.name == random_connection.station2.name:
                traject.add_station(random_connection.station1)

            traject.update_time(random_connection.time)
            network.connections.remove(random_connection)

        network.add_traject(traject)

    network.connections = original_connections
    return network

def get_possible_connections(station, connections):
    possible_connections = []
    for connection in connections:
        if station.name == connection.station1.name or station.name == connection.station2.name:
            possible_connections.append(connection)
    return possible_connections