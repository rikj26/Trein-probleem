import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

def visualisatie(trajects, geo_file): # traject : lijst met stations
    kaart = gpd.read_file(geo_file)

    fig, ax = plt.subplots(figsize=(10, 10))
    kaart.plot(ax=ax, color='white', edgecolor='black')

    color_map = plt.cm.tab20

    annotated_stations = set()

    for idx, traject in enumerate(trajects):
        coordinates_list = [Point(station.x, station.y) for station in traject.route]
        
        geo_points = gpd.GeoDataFrame(geometry=coordinates_list)
        geo_lines = gpd.GeoDataFrame(geometry=[LineString(coordinates_list)])

        color = color_map(idx)

        geo_points.plot(ax=ax, marker='o', color=color, label=f'Traject {idx + 1}')
        geo_lines.plot(ax=ax, color=color)

        for i, station in enumerate(traject.route):
            if station.name not in annotated_stations:
                offset_x = 0.01 * ((i % 2) * 2 - 1)
                offset_y = 0.01 * ((i % 2) * 2 - 1)  
                plt.annotate(station.name, (station.x + offset_x, station.y + offset_y), ha='center', fontsize=8)
                annotated_stations.add(station.name)

    plt.legend()
    plt.show()
