class Traject():
    def __init__(self):
        self.route = []
        self.total_time = 0
    
    def add_station(self, station):
        self.route.append(station)
    
    def update_time(self, time):
        self.total_time += time

    def get_last_station(self):
        if self.route:
            return self.route[-1]
        else:
            return None