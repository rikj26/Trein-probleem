from classes import station, traject
from algorithms import random
import visualisatie

if __name__ == "__main__":
    stations_holland = station.laad_stations("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    stations_nationaal = station.laad_stations("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")

    random_algoritme = random.random_traject(stations_nationaal, traject.Traject())
    for station in random_algoritme.route:
        print(station.name)

    print("The totale tijd is:", random_algoritme.total_time)

    visualisatie.visualisatie(random_algoritme.route, "data/kaarten/netherlands_.geojson")
