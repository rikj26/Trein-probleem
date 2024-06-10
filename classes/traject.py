class Traject:
    def __init__(self):
        self.verbindingen = []
        self.tijd = 0

    def verbinding_toevoegen(self, verbinding):
        self.verbindingen.append(verbinding)
        self.tijd += verbinding.time

    def totale_tijd(self):
        return self.tijd

    def stations(self):
        station_lijst = [self.verbindingen[0].station1]
        
        for verbinding in self.verbindingen:
            station_lijst.append(verbinding.station2)
        
        return station_lijst