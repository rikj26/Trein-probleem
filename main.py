from classes import network
from algorithms import random, greedy
import visualisatie

if __name__ == "__main__":
    netwerk_holland = network.Network("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    netwerk_nationaal = network.Network("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
    
    random_algoritme = random.random_traject(netwerk_nationaal, 20, 180)

    greedy_algoritme = greedy.greedy_traject(netwerk_nationaal, 20, 180)

    visualisatie.visualisatie(greedy_algoritme.trajects, "data/kaarten/netherlands_.geojson")

    scores = []
    for _ in range(10000):
        test_random = random.random_traject(netwerk_holland, 7, 120)
        scores.append(test_random.score())
        test_random.clear_trajects()

    visualisatie.histogram(scores, 'random algorithm')
