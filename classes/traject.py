class Traject():
    def __init__(self):
        self.route = []
        self.total_time = 0
    
    def add_station(self, station):
        if len(self.route) > 1:
            self.total_time += self.route[-1].connecties[station.name]
        
        self.route.append(station)
