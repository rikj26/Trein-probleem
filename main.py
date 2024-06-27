from classes import network
from algorithms import random, greedy, hillclimber, bfs
import visualisatie
import matplotlib.pyplot as plt

if __name__ == "__main__":
    netwerk_holland = network.Network("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    netwerk_nationaal = network.Network("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
    
    # Random algorithm
    random_algoritme = random.random_traject(netwerk_nationaal, 7, 120)
    visualisatie.visualisatie(random_algoritme.trajects, "data/kaarten/netherlands_.geojson")

    # Greedy algorithm
    greedy_algoritme = greedy.greedy_traject(netwerk_nationaal, 7, 120)
    visualisatie.visualisatie(greedy_algoritme.trajects, "data/kaarten/netherlands_.geojson")

    # Hillclimber algorithm
    hillclimber_trajects, hillclimber_score = hillclimber.hill_climber(netwerk_nationaal, max_time=120)
    visualisatie.visualisatie(hillclimber_trajects, "data/kaarten/netherlands_.geojson")

    bfs_algoritme = bfs.bfs_traject(netwerk_nationaal, 7, 120)
    visualisatie.visualisatie(bfs_algoritme.trajects, "data/kaarten/netherlands_.geojson")
    
    # Scores
    random_scores = []
    for _ in range(100):
        test_random = random.random_traject(netwerk_nationaal, 7, 120)
        random_scores.append(test_random.score())
        test_random.clear_trajects()

    visualisatie.histogram(random_scores, 'random algorithm')

    hillclimber_scores = []
    for _ in range(100):
        hillclimber_trajects, hillclimber_score = hillclimber.hill_climber(netwerk_nationaal, max_time=120)
        hillclimber_scores.append(hillclimber_score)
    
    visualisatie.histogram(hillclimber_scores, 'hillclimber algorithm')

bfs_scores = []
    for _ in range(100):
        test_bfs = bfs.bfs_traject(netwerk_nationaal, 7, 120)
        bfs_scores.append(test_bfs.score())
        test_bfs.clear_trajects()

    visualisatie.histogram(bfs_scores, 'BFS Algorithm')



