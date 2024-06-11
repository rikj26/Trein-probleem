from classes import station, verbinding

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

def visualisatie(traject, geo_file): # traject : lijst met stations
    coordinates_list = []
    for station in traject:
        coordinates_list.append(Point(station.x, station.y))

    geo_points = gpd.GeoDataFrame(geometry=coordinates_list)
    geo_lines = gpd.GeoDataFrame(geometry=[LineString(coordinates_list)])

    kaart = gpd.read_file(geo_file)

    fig, ax = plt.subplots(figsize=(10, 10))
    kaart.plot(ax=ax, color='white', edgecolor='black')
    geo_points.plot(ax=ax, color='red', marker='o')
    geo_lines.plot(ax=ax)

    for station in traject:
        plt.annotate(station.name, (station.x, station.y), ha='center')

    plt.show()