import csv
from .station import Station
from .connection import Connection
from .traject import Traject

class Network():
    def __init__(self, station_file, connection_file):
        self.stations = self.load_stations(station_file)
        self.connections = self.load_connections(connection_file)
        self.trajects = []

    def load_stations(self, station_file):
        stations = {}
        with open(station_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                station = Station(name=row['station'], y=float(row['y']), x=float(row['x']))
                stations[station.name] = station
        return stations

    def load_connections(self, connection_file):
        connections = []
        with open(connection_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                station1 = self.stations[row['station1']]
                station2 = self.stations[row['station2']]
                connection = Connection(station1=station1, station2=station2, time=float(row['distance']))
                connections.append(connection)
        return connections
    
    def create_traject(self):
        return Traject()

    def add_traject(self, traject):
        self.trajects.append(traject)