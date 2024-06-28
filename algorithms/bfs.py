import copy

class BFS:
    def __init__(self, network, max_trajects, max_time):
        self.network = network
        self.max_trajects = max_trajects
        self.max_time = max_time
    
    def bfs(self):
        for _ in range(self.max_trajects):

            queue = self.initialize_queue()
            best_traject = self.network.create_traject()

            while queue:
                current_traject = queue.pop(0)
                current_station = current_traject.get_last_station()

                for connection in self.get_possible_connections(current_station):

                    if connection in current_traject.covered_connections:
                        continue

                    next_station = connection.station2 if current_station == connection.station1 else connection.station1
                
                    if current_traject.total_time + connection.time > self.max_time:
                        if current_traject != best_traject and len(current_traject.route) > len(best_traject.route):
                            best_traject = current_traject
                    else:
                        new_traject = copy.deepcopy(current_traject)
                        new_traject.add_station(next_station)
                        new_traject.update_time(connection.time)
                        new_traject.add_covered_connection(connection)
                        queue.append(new_traject)

            self.network.trajects.append(best_traject)
            for connection in best_traject.covered_connections:
                self.network.connections.remove(connection)
    
        return self.network
    
    def initialize_queue(self):
        queue = []

        for station in self.network.stations.values():
            traject = self.network.create_traject()
            traject.add_station(station)
            queue.append((traject))
        
        return queue
    
    def get_possible_connections(self, station):
        possible_connections = []
        for connection in self.network.connections:
            if station == connection.station1 or station == connection.station2:
                possible_connections.append(connection)
        return possible_connections
