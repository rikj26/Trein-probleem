from classes import network
from algorithms import random
import visualisatie

if __name__ == "__main__":
    netwerk_holland = network.Network("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    netwerk_nationaal = network.Network("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
    
    random_algoritme = random.random_traject(netwerk_holland)

    visualisatie.visualisatie(random_algoritme.trajects, "data/kaarten/netherlands_.geojson")

    print(random_algoritme.score())
