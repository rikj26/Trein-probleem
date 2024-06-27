import copy

def bfs_traject(network, max_trajects, max_time):
    original_connections = copy.deepcopy(network.connections)
    
    while len(network.trajects) < max_trajects and len(network.connections) != 0:
        traject = network.create_traject()
        
        start_connection = network.connections[0]
        queue = [(start_connection.time, [start_connection.station1, start_connection.station2])]
        visited = set()
        visited.add((start_connection.station1.name, start_connection.station2.name))
        visited.add((start_connection.station2.name, start_connection.station1.name))
        network.connections.remove(start_connection)
        
        while queue:
            current_time, path = queue.pop(0)
            current_station = path[-1]
            
            if current_time > max_time:
                continue
            
            for connection in network.connections[:]:
                if current_station.name == connection.station1.name and current_time + connection.time <= max_time:
                    new_path = path + [connection.station2]
                    if (connection.station1.name, connection.station2.name) not in visited:
                        queue.append((current_time + connection.time, new_path))
                        visited.add((connection.station1.name, connection.station2.name))
                        visited.add((connection.station2.name, connection.station1.name))
                        network.connections.remove(connection)
                elif current_station.name == connection.station2.name and current_time + connection.time <= max_time:
                    new_path = path + [connection.station1]
                    if (connection.station2.name, connection.station1.name) not in visited:
                        queue.append((current_time + connection.time, new_path))
                        visited.add((connection.station2.name, connection.station1.name))
                        visited.add((connection.station1.name, connection.station2.name))
                        network.connections.remove(connection)
        
        for station in path:
            traject.add_station(station)
        traject.update_time(current_time)
        
        network.add_traject(traject)
    
    network.connections = original_connections

    return network