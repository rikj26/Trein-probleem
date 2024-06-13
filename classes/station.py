import csv

class Station():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.connecties = {}

def laad_stations(station_file, connection_file):
    stations = []
    with open(station_file, 'r') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            station = Station(name=row['station'], y=float(row['y']), x=float(row['x']))
            stations.append(station)
    
    with open (connection_file, 'r') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            for station in stations:
                if row['station1'] == station.name:
                    station.connecties[row['station2']] = float(row['distance'])
                elif row['station2'] == station.name:
                    station.connecties[row['station1']] = float(row['distance'])
    return stations
