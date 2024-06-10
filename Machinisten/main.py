from classes import station, verbinding

if __name__ == "__main__":
    station_test = station.laad_stations("data/StationsHolland.csv")
    verbinding_test = verbinding.laad_verbindingen("data/ConnectiesHolland.csv")

    for i in verbinding_test:
        print(i.station1, i.station2)