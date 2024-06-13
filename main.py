import csv

from classes import station, traject
from algorithms import random
import visualisatie

if __name__ == "__main__":
    stations_holland = station.laad_stations("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    stations_nationaal = station.laad_stations("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")

    # Dit is een tijdelijke oplossing, en moet anders. Maar ik heb het idee dat ik een verkeerde representatie heb gekozen.
    max_connecties_holland = 0
    with open("data/ConnectiesHolland.csv", 'r') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            max_connecties_holland += 1

    gem_K_score = 0
    for _ in range(500):
        random_algoritme = random.random_traject(stations_holland, traject.Traject())
        aantal_verbindingen = len(random_algoritme.route) - 1
        gem_K_score += aantal_verbindingen / max_connecties_holland * 10000 - ((aantal_verbindingen * 100) + random_algoritme.total_time)

    print("De gemiddelde K-scores is:", gem_K_score / 500)

    visualisatie.visualisatie(random_algoritme.route, "data/kaarten/netherlands_.geojson")
