import csv

class Verbinding():
    def __init__(self, station1, station2, time):
        self.station1 = station1
        self.station2 = station2
        self.time = time

def laad_verbindingen(source_file):
    verbindingen = []
    with open(source_file, 'r') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            verbinding = Verbinding(station1=row['station1'], station2=row['station2'], time=int(row['distance']))
            verbindingen.append(verbinding)
    return verbindingen