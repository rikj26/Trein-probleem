import csv

class Station():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

def laad_stations(source_file):
    stations = []
    with open(source_file, 'r') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            station = Station(name=row['station'], y=float(row['y']), x=float(row['x']))
            stations.append(station)
    return stations
