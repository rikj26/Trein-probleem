from classes import station, verbinding

if __name__ == "__main__":
    station_test = station.laad_stations("data/StationsHolland.csv")
    verbinding_test = verbinding.laad_verbindingen("data/ConnectiesHolland.csv")

    visualisatie.visualisatie(station_test, "data/kaarten/netherlands_.geojson")
