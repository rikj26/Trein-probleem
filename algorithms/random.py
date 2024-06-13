import random

def random_traject(stations, traject): # stations: lijst met alle objecten van stations
    current_station = random.choice(stations)
    traject.add_station(current_station)
    previous_station = None

    while(len(traject.route) < 8):
        possible_stations = list(current_station.connecties.keys())

        # Het moet niet mogelijk zijn om direct hetzelfde traject terug te nemen, behalve als dit de enige optie is.
        if previous_station and len(possible_stations) > 1:
            possible_stations.remove(previous_station)

        next_station = random.choice(possible_stations)
        while traject.total_time + current_station.connecties[next_station] > 120:
            possible_stations.remove(next_station)
            
            # wanneer alle opties ervoor zorgen dat de tijd groter wordt 120, stuur dan het huidige traject
            if not possible_stations:
                return traject
            
            next_station = random.choice(possible_stations)

        previous_station = current_station.name
        current_station = get_new_station(next_station, stations)
        traject.add_station(current_station)
    
    return traject

def get_new_station(new_station, stations): # new_station : string met stationsnaam, stations : lijst met alle objecten van stations
    for station in stations:
        if station.name == new_station:
            return station
