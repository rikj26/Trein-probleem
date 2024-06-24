import copy

def greedy_traject(network, max_trajects, max_time):
    original_connections = copy.deepcopy(network.connections)
    
    while(len(network.trajects) < max_trajects and len(network.connections) != 0):
        traject = network.create_traject()
        greedy_connection = network.connections[-1]
        network.connections.remove(greedy_connection)

        traject.add_station(greedy_connection.station2)
        traject.add_station(greedy_connection.station1)
        traject.update_time(greedy_connection.time)

        while(traject.total_time <= max_time):
            current_station = traject.get_last_station()
            greedy_connection = get_greedy_connection(current_station, network.connections)

            if greedy_connection == None:
                break
            
            if greedy_connection.time + traject.total_time > max_time:
                break

            if current_station.name == greedy_connection.station1.name:
                traject.add_station(greedy_connection.station2)
            elif current_station.name == greedy_connection.station2.name:
                traject.add_station(greedy_connection.station1)

            traject.update_time(greedy_connection.time)
            network.connections.remove(greedy_connection)
        
        network.add_traject(traject)

    network.connections = original_connections
    return network

def get_greedy_connection(station, connections):
    possible_connections = []
    for connection in connections:
        if station.name == connection.station1.name or station.name == connection.station2.name:
            possible_connections.append(connection)
    
    if not possible_connections:
        return None
    else:
        return sorted(possible_connections, key=lambda x:x.time)[-1]