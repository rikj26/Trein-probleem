import random
import copy

def initial_solution(network, max_time):
    original_connections = copy.deepcopy(network.connections)
    trajects = []
    all_stations = set(network.stations)
    visited_stations = set()

    while len(trajects) < 7 and visited_stations != all_stations:
        traject = network.create_traject()
        unvisited_connections = [conn for conn in network.connections if conn.station1 not in visited_stations or conn.station2 not in visited_stations]

        random_connection = random.choice(unvisited_connections) if unvisited_connections else random.choice(network.connections)
        network.connections.remove(random_connection)

        traject.add_station(random_connection.station1)
        traject.add_station(random_connection.station2)
        traject.update_time(random_connection.time)

        visited_stations.update([random_connection.station1, random_connection.station2])

        while traject.total_time <= max_time:
            current_station = traject.get_last_station()
            possible_connections = get_possible_connections(current_station, network.connections)

            if not possible_connections:
                break

            unvisited_connections = [conn for conn in possible_connections if conn.station1 not in visited_stations or conn.station2 not in visited_stations]
            random_connection = random.choice(unvisited_connections) if unvisited_connections else random.choice(possible_connections)

            if random_connection.time + traject.total_time > max_time:
                break

            next_station = random_connection.station2 if current_station.name == random_connection.station1.name else random_connection.station1
            traject.add_station(next_station)
            visited_stations.add(next_station)

            traject.update_time(random_connection.time)
            network.connections.remove(random_connection)

        if traject.route:
            trajects.append(traject)

    network.connections = original_connections
    return trajects

def get_neighbors(current_solution, network, max_time):
    neighbors = []
    for i, traject in enumerate(current_solution):
        new_traject = extend_traject(copy.deepcopy(traject), network, max_time)
        new_solution = copy.deepcopy(current_solution)
        new_solution[i] = new_traject
        neighbors.append(new_solution)
    return neighbors

def extend_traject(traject, network, max_time):
    while traject.total_time < max_time:
        current_station = traject.get_last_station()
        possible_connections = get_possible_connections(current_station, network.connections)
        if not possible_connections:
            break

        random_connection = random.choice(possible_connections)
        if traject.total_time + random_connection.time <= max_time:
            next_station = random_connection.station2 if current_station.name == random_connection.station1.name else random_connection.station1
            traject.add_station(next_station)
            traject.update_time(random_connection.time)
        else:
            break
    return traject

def get_possible_connections(station, connections):
    return [conn for conn in connections if station.name in (conn.station1.name, conn.station2.name)]

def evaluate_solution(trajects, all_stations, max_time):
    unique_stations = {station for traject in trajects for station in traject.route}
    total_length = sum(traject.total_time for traject in trajects)
    traject_scores = sum(1 - abs(traject.total_time - max_time) / max_time for traject in trajects)
    coverage_score = len(unique_stations) / len(all_stations)
    return coverage_score + traject_scores

def hill_climber(network, max_time):
    all_stations = set(network.stations)
    current_solution = initial_solution(network, max_time)
    current_value = evaluate_solution(current_solution, all_stations, max_time)

    improvement = True
    while improvement:
        neighbors = get_neighbors(current_solution, network, max_time)
        best_neighbor = max(neighbors, key=lambda neighbor: evaluate_solution(neighbor, all_stations, max_time))
        best_value = evaluate_solution(best_neighbor, all_stations, max_time)

        if best_value > current_value:
            current_solution = best_neighbor
            current_value = best_value
        else:
            improvement = False

    score_value = score(current_solution, network.max_connections)
    return current_solution, score_value

def score(trajects, max_connections):
    used_connections = sum(len(traject.route) - 1 for traject in trajects)
    total_time = sum(traject.total_time for traject in trajects)
    num_trajects = len(trajects)
    
    score_value = (used_connections / max_connections) * 10000 - (num_trajects * 100 + total_time)
    return round(score_value)