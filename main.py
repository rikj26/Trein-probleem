from classes import station, verbinding
from algorithms import random
import visualisatie

if __name__ == "__main__":
    station_test = station.laad_stations("data/StationsHolland.csv")
    verbinding_test = verbinding.laad_verbindingen("data/ConnectiesHolland.csv")

    random_algoritme = random.random_traject(station_test, verbinding_test)
    for station in random_algoritme:
        print(station.name)

    visualisatie.visualisatie(random_algoritme, "data/kaarten/netherlands_.geojson")
