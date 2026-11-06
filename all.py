import serial
import pynmea2
import _thread

# location of gps port
GPS_PORT = "/dev/ttyAMA0"


# GPS manager class
class GPSManager:
    def __init__(self):
        self.port = GPS_PORT
        self.lat = None
        self.lng = None

        # km/h
        self.speed = None

        # Set a refrence to the gps's serial data
        self.ser = serial.Serial(self.port, baudrate=9600, timeout=0.5)

        # Create thread for gps location update
        self.update_thread = _thread.start_new_thread(self._update)
        self.running = True

    def _update(self):  # _ for internal function, loop to update gps location
        while self.running:
            rawdata = self.ser.readline()

            # Check if the raw data is the correct type
            # $GNRMC gives longitude, latitude, speed (in Knots), UTC time, and date
            if rawdata[0:5] == "$GNRMC":
                # Parse rawdate into usable data
                data = pynmea2.parse(rawdata)

                # Set local refrence to needed data
                lat = data.latitude
                lng = data.longitude

                # Get raw speed (in knots), then change to km/h
                speed_knots = data.spd_over_grnd
                speed = speed_knots * 1.852

                # Set class data
                self._set_location_speed(lat, lng, speed)

    def get_location_speed(self):  # Called by other files when needed to get location
        return [self.lat, self.lng, self.speed]

    # Set location in class
    def _set_location_speed(self, lat, lng, speed):
        self.lat = lat
        self.lng = lng
        self.speed = speed

    def stop(self):
        self.running = False
        self.ser.close()

import json

# Load your multi-subsection GeoJSON
with open("Data/ACTGOV_DISTRICTS_-2248938068983619392.geojson", "r") as f:
    geojson_data = json.load(f)

extracts = []

# Loop through each feature to create an extract definition
for index, feature in enumerate(geojson_data["features"]):
    # Use a property name (like 'name' or 'id') for the filename, fallback to index
    properties = feature.get("properties", {})
    name = (
        properties.get("DISTRICT_NAME", f"subsection_{index}").replace(" ", "_").lower()
    )

    polygons = feature["geometry"]["coordinates"]

    extracts.append(
        {
            "output": f"{name}.osm.pbf",
            "description": f"Extract for {name}",
            "polygon": feature["geometry"]["coordinates"],
        }
    )

# Save to Osmium configuration format
osmium_config = {"extracts": extracts}

with open("extract_config.json", "w") as f:
    json.dump(osmium_config, f, indent=4)

print("Osmium extract configuration created successfully!")

from pathlib import Path
import _thread
import json
import time
from shapely.geometry import Point, shape

local_path = Path(__file__).parent.parent
local_path= local_path / "Areas"


class AreaLoader:
    def __init__(self, owner):
        # Reference to the owner
        self.owner = owner
        # Dictionary containing the files associated with the districts and their adjacentcies
        self.locations = {
            "Belconnen": [
                local_path / "BELC.osm.pbf",
                local_path / "BELC.geojson",
                [
                    "Coree",
                    "Hall",
                    "Gungahlin",
                    "Canberra Central",
                    "Molongolo Valley",
                    "Stromlo",
                ],
            ],
            "Booth": [
                local_path / "BOOT.osm.pbf",
                local_path / "BOOT.geojson",
                [
                    "Mount Clear",
                    "Rendezvous Creek",
                    "Tennent",
                ],
            ],
            "Canberra Cental": [
                local_path / "CANB.osm.pbf",
                local_path / "CANB.geojson",
                [
                    "Belconnen",
                    "Gungahlin",
                    "Majura",
                    "Jerrabomberra",
                    "Woden Valley",
                    "Weston Creek",
                    "Molongolo Valley",
                ],
            ],
            "Coree": [
                local_path / "CORE.osm.pbf",
                local_path / "CORE.geojson",
                [
                    "Belconnen",
                    "Stromlo",
                    "Paddys Creek",
                    "Cotter River",
                ],
            ],
            "Cotter River": [
                local_path / "COTT.osm.pbf",
                local_path / "COTT.geojson",
                [
                    "Coree",
                    "Paddys Creek",
                    "Tennent",
                    "Rendezvous Creek",
                ],
            ],
            "Gungahlin": [
                local_path / "GUNG.osm.pbf",
                local_path / "GUNG.geojson",
                [
                    "Hall",
                    "Belconnen",
                    "Canberra Central",
                    "Majura",
                ],
            ],
            "Hall": [
                local_path / "HALL.osm.pbf",
                local_path / "HALL.geojson",
                [
                    "Belconnen",
                    "Gungahlin",
                ],
            ],
            "Jerrabomberra": [
                local_path / "JERR.osm.pbf",
                local_path / "JERR.geojson",
                [
                    "Majura",
                    "Canberra Central",
                    "Woden Valley",
                    "Tuggeranong",
                ],
            ],
            "Kowen": [
                local_path / "KOWE.osm.pbf",
                local_path / "KOWE.geojson",
                ["Majura"],
            ],
            "Majura": [
                local_path / "MAJU.osm.pbf",
                local_path / "MAJU.geojson",
                [
                    "Kowen",
                    "Gungahlin",
                    "Canberra Central",
                    "Jerrabomberra",
                ],
            ],
            "Molonglo Valley": [
                local_path / "MOLO.osm.pbf",
                local_path / "MOLO.geojson",
                [
                    "Stromlo",
                    "Belconnen",
                    "Canberra Central",
                    "Weston Creek",
                ],
            ],
            "Mount Clear": [
                local_path / "MOUN.osm.pbf",
                local_path / "MOUN.geojson",
                [
                    "Rendezvous Creek",
                    "Booth",
                ],
            ],
            "Paddys River": [
                local_path / "PADD.osm.pbf",
                local_path / "PADD.geojson",
                [
                    "Cotter River",
                    "Coree",
                    "Stromlo",
                    "Tuggeranong",
                    "Tennent",
                ],
            ],
            "Rendezvous Creek": [
                local_path / "REND.osm.pbf",
                local_path / "REND.geojson",
                [
                    "Cotter River",
                    "Tennent",
                    "Booth",
                    "Mount Clear",
                ],
            ],
            "Stromlo": [
                local_path / "STRO.osm.pbf",
                local_path / "STRO.geojson",
                [
                    "Coree",
                    "Belconnen",
                    "Molongolo Valley",
                    "Weston Creek",
                    "Tuggeranong",
                    "Paddys Creek",
                ],
            ],
            "Tennent": [
                local_path / "TENN.osm.pbf",
                local_path / "TENN.geojson",
                [
                    "Cotter River",
                    "Paddys River",
                    "Tuggeranong",
                    "Booth",
                    "Rendezvous Creek",
                ],
            ],
            "Tuggeranong": [
                local_path / "TUGG.osm.pbf",
                local_path / "TUGG.geojson",
                [
                    "Stromlo",
                    "Weston Creek",
                    "Woden Valley",
                    "Jerrabomberra",
                    "Tennent",
                    "Paddys River",
                ],
            ],
            "Weston Creek": [
                local_path / "WEST.osm.pbf",
                local_path / "WEST.geojson",
                [
                    "Stromlo",
                    "Molongolo Valley",
                    "Canberra Central",
                    "Woden Valley",
                    "Tuggeranong",
                ],
            ],
            "Woden Valley": [
                local_path / "WODE.osm.pbf",
                local_path / "WODE.geojson",
                [
                    "Weston Creek",
                    "Canberra Central",
                    "Jerrabomberra",
                    "Tuggeranong",
                ],
            ],
        }

        # If the location has been found and what it is
        self.located = False
        self.location = None
        # Exact latitude and longitude
        self.coordinates = None

        self.load_area = 1  # Number of adjacent areas to load: 1 Just the immediete adjacent, 2 their adjacentcies.

        # Running and its thread
        self.running = True
        self.update_thread = _thread.start_new_thread(self._update)

    def find_location(self):
        lat_lng = self.owner.get_location()  # in form [Lat, Lng]
        self.cordinates = Point(lat_lng[1], lat_lng[0])

        if self.located:
            # Check adjacent

            for area1 in self.located[2]:
                area = list(self.locations.keys()).index(area1)

                with open(area[1], "r") as f:
                    geojson_date = json.load(f)

                for feature in geojson_date["features"]:
                    polygon = shape(feature["geometry"])
                    if polygon.contains(self.coordinates):
                        self.location = area1
                        self.located = True
                        break

        else:
            # Check all
            for area in self.locations:
                # Check if the areas.geojson has the current lat_lng in it
                with open(area[1], "r") as f:
                    geojson_date = json.load(f)

                for feature in geojson_date["features"]:
                    polygon = shape(feature["geometry"])
                    if polygon.contains(self.coordinates):
                        self.location = area
                        self.located = True
                        break

    def load_areas(self):
        pass

    def _update(self):
        while self.running:
            lat_lng = self.owner.get_location()
            self.coordinates = Point(lat_lng[1], lat_lng[0])

            with open(self.location[1], "r") as f:
                geojson_data = json.load(f)

            for feature in geojson_data["features"]:
                polygon = shape(feature["geometry"])
                if polygon.contains(self.coordinates):
                    break
                else:
                    self.find_location()

    time.sleep(15)  # Checks every 15 seconds


# When load an area after the first time (Check all and find where we are using cord), then check adjacent first before doing the others

from pyrosm import OSM
from pathlib import Path


class OSMImporter:
    def __init__(self, file_path: Path):
        self.osm_file = file_path
        self.osm = OSM(self.osm_file)

        self.nodes, self.edges = self.osm.get_network(
            nodes=True, network_type="driving"
        )

        self.graph = self.osm.to_graph(self.nodes, self.edges, simplify=True)

from pyrosm import OSM


class RoadGraph:
    def __init__(self, osm_file):
        self.osm_file = osm_file

        self.osm = None
        self.nodes = None
        self.edges = None
        self.graph = None

    def load(self):
        self.osm = OSM(self.osm_file)

        self.nodes, self.edges = self.osm.get_network(
            network_type="driving", nodes=True
        )

        print(self.edges.columns)

        self.graph = self.osm.to_graph(self.nodes, self.edges, graph_type="networkx")

        return self.graph

from navigation.routing import Router


class NavigationController:
    def __init__(self, owner, road_graph):
        # CarNavApp gives us access to the current GPS location.
        self.owner = owner

        self.road_graph = road_graph
        # Router handles the actual pathfinding through the road network.
        self.router = Router(road_graph)

        # Current navigation information.
        self.destination = None
        self.route = None
        self.route_coordinates = []

    def set_destination(self, lat, lng):
        # Store the destination and immediately calculate a route to it.
        self.destination = [lat, lng]

        return self.calculate_route()

    def calculate_route(self):
        # A destination needs to be selected before routing can begin.
        if self.destination is None:
            return None

        start = self.owner.get_location()

        # GPS may not have produced a position yet.
        if start[0] is None or start[1] is None:
            return None

        self.route = self.router.calculate_route(
            start[0], start[1], self.destination[0], self.destination[1]
        )

        if self.route is None:
            self.route_coordinates = []
            return None

        self.route_coordinates = self.router.get_route_coordinates(self.route)
        self.route_length_speed = {}  # Key = node_id, element = [length, maxspeed]

        return self.route_coordinates

    def get_route(self):
        return self.route_coordinates

    def get_destination(self):
        return self.destination

    def clear_route(self):
        self.destination = None
        self.route = None
        self.route_coordinates = []

    def calculate_estimated_time(self):
        if self.route is None:
            return None

        length_speed = self.router.get_route_legth_speed(self.route)

        total_minutes = 0

        for length, speed in length_speed:
            if speed is None:
                speed = 50 # Assume default speed

            distance_km = length / 1000
            time_hours = distance_km / float(speed)

            total_minutes += time_hours * 60

        return total_minutes

    def calculate_estimated_distance(self):
        pass

import math
import networkx as nx


class Router:
    def __init__(self, road_graph):
        # Store the road network loaded by RoadGraph.
        # Pyrosm converts the OSM data into a NetworkX graph.
        self.road_graph = road_graph
        self.graph = road_graph.graph

    def find_closest_node(self, lat, lng):
        # GPS coordinates won't always match the coordinates of an
        # exact road node, so find the nearest node in the road network.
        # Won't always work if there is too much error in gps distance or crowded area
        closest_node = None
        closest_distance = float("inf")

        for node_id, node in self.graph.nodes(data=True):
            node_lat = node["y"]
            node_lng = node["x"]

            distance = (lat - node_lat) ** 2 + (lng - node_lng) ** 2

            if distance < closest_distance:
                closest_distance = distance
                closest_node = node_id

        return closest_node

    def est_distance(self, node1, node2):
        # A* needs an estimate of how far a node is from the destination.
        first = self.graph.nodes[node1]
        second = self.graph.nodes[node2]

        return self.distance(first["y"], first["x"], second["y"], second["x"])

    def distance(self, lat1, lng1, lat2, lng2):
        # Calculate distance betwee GPS coordinates
        # using the Haversine formula. The result is returned in metres.
        earth_radius = 6371000

        # Since lat and lng are basically just the angles from equator
        # they can be turned into radians
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)

        lat_difference = math.radians(lat2 - lat1)
        lng_difference = math.radians(lng2 - lng1)

        a = (
            math.sin(lat_difference / 2) ** 2
            + math.cos(lat1_rad)
            * math.cos(lat2_rad)
            * math.sin(lng_difference / 2) ** 2
        )

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return earth_radius * c

    def calculate_route(self, start_lat, start_lng, end_lat, end_lng):
        # Convert the start and destination coordinates into actual
        # nodes in the road network.
        start_node = self.find_closest_node(start_lat, start_lng)
        end_node = self.find_closest_node(end_lat, end_lng)

        print("Start node:", start_node)
        print("End node:", end_node)

        try:
            # Use A* to find the shortest route through the road network.
            # The road edge "length" from Pyrosm is used as the travel cost.
            route = nx.astar_path(
                self.graph,
                start_node,
                end_node,
                heuristic=self.est_distance,
                weight="length",
            )

            return route

        except nx.NetworkXNoPath:
            # If the two locations are not connected in the loaded map data,
            # return None instead of crashing the program.
            print("No route found")
            return None

    def get_route_coordinates(self, route):
        # The route returned by NetworkX is a list of OSM node IDs.
        # Convert those IDs into latitude and longitude coordinates so
        # the map can draw the route.
        coordinates = []

        for node_id in route:
            node = self.graph.nodes[node_id]

            coordinates.append([node["y"], node["x"]])

        return coordinates

    def get_route_legth_speed(self, route):
        length_speed = []
        last_node = None

        for node_id in route:
            if last_node is None:
                last_node = node_id
                continue

            edges = self.graph.get_edge_data(last_node, node_id)

            if edges is None:
                last_node = node_id
                continue

            edge = list(edges.values())[0]

            length_speed.append([
                edge.get("length"),
                edge.get("maxspeed")
            ])
            last_node = node_id

        return length_speed

from PyQt5.QtWidgets import *

"""(
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QApplication,
    QGridLayout,
    QStackedLayout,
    QGraphicsOpacityEffect,
    QPushButton
)"""

from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

#from offline_folium import offline
import folium
from folium import plugins

import sys
import os
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

# from main import CarNavApp

debug = False

# Color Palette
mono_dark_mode = {
    "background": "#121212",
    "primary text": "#E0E0E0",
    "Secondary Text": "#B0B0B0",
    "border/dividers": "#444444",
    "accent": "#888888",
}
'''
Background: #121212 (charcoal black)
Primary Text: #E0E0E0 (light gray)
Secondary Text: #B0B0B0 (medium gray)
Borders/Dividers: #444444 (dark gray)
Accent: #888888 (soft gray)
'''

deep_dark_mode = {
    "background": "#1A1A1A",
    "primary text": "#F0F0F0",
    "Secondary Text": "#004D61",
    "border/dividers": "#822659",
    "accent": "#3E5641",
}
'''
    Background: #1A1A1A (rich black)
    Primary Text: #F0F0F0 (off-white)
    Accent 1: #004D61 (dark teal)
    Accent 2: #822659 (deep ruby)
    Button/CTA: #3E5641 (forest green)
'''

class MainWindow(QMainWindow):
    def __init__(self, carnavapp):
        super().__init__()

        self.setWindowTitle("CarNav")
        self.resize(720, 480)
        self.setFixedSize(
            720, 480
        )  # Needed due to my computers using Hyprland (auto tiling window manager), which overwrote the handling of size

        self.car_nav_controller = carnavapp

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.central_vlayout = QVBoxLayout(self.central_widget)
        self.central_vlayout.setContentsMargins(0, 0, 0, 0)
        self.central_vlayout.setSpacing(0)

        # Main layouts
        self.top_hlayout = QHBoxLayout()
        self.middle_slayout = QStackedLayout()
        self.bottom_hlayout = QHBoxLayout()

        self.middle_slayout.setStackingMode(QStackedLayout.StackAll)

        self.central_vlayout.addLayout(self.top_hlayout)
        self.central_vlayout.addLayout(self.middle_slayout, 1)
        self.central_vlayout.addLayout(self.bottom_hlayout)

        self.top_hlayout.setContentsMargins(5, 5, 5, 5)
        self.top_hlayout.setSpacing(5)

        self.bottom_hlayout.setContentsMargins(5, 5, 5, 5)
        self.bottom_hlayout.setSpacing(5)

        # Top layout widgets
        self.speed_widget = QWidget()
        self.name_widget = QWidget()
        self.time_widget = QWidget()
        self.location_widget = QWidget()

        self.name_widget.setFixedWidth(200)
        self.time_widget.setFixedWidth(200)

        self.speed_widget.setFixedSize(100, 65)
        self.location_widget.setFixedHeight(65)

        self.time_name_vlayout = QVBoxLayout()
        self.time_name_vlayout.setContentsMargins(0, 0, 0, 0)
        self.time_name_vlayout.setSpacing(5)

        self.time_name_vlayout.addWidget(self.name_widget)
        self.time_name_vlayout.addWidget(self.time_widget)

        self.top_hlayout.addWidget(self.speed_widget)
        self.top_hlayout.addLayout(self.time_name_vlayout, 1)
        self.top_hlayout.addWidget(self.location_widget, 1)

        # Middle layout widgets
        self.map_widget = QWebEngineView()
        self.map = self.create_map(-35.3265,149.053,17)
        self.map.save('map.html')
        self.map_widget.setHtml(self.map.get_root().render())

        # Transparent overlay positioned over the map
        self.middle_glayout_widget = QWidget()
        self.middle_glayout_widget.setStyleSheet(
            "background: transparent; border: none;"
        )

        self.middle_glayout = QGridLayout(self.middle_glayout_widget)
        self.middle_glayout.setContentsMargins(10, 10, 10, 10)

        self.list_turns = QPushButton()
        self.list_turns.setFixedSize(50, 50)
        self.list_turns.clicked.connect(self.on_list_turns_presses)

        self.middle_glayout.addWidget(self.list_turns, 1, 1, Qt.AlignBottom | Qt.AlignRight)

        self.middle_slayout.addWidget(self.map_widget)
        self.middle_slayout.addWidget(self.middle_glayout_widget)

        self.middle_slayout.setCurrentWidget(self.middle_glayout_widget)

        # Bottom layout widgets
        self.stop_route_widget = QPushButton()
        self.animation_widget = QWidget()
        self.eta_widget = QWidget()
        self.dest_select_widget = QLineEdit()

        self.stop_route_widget.clicked.connect(self.on_stop_route_pressed)

        self.stop_route_widget.setFixedSize(65, 65)
        self.animation_widget.setFixedHeight(65)
        self.eta_widget.setFixedSize(100, 65)
        self.dest_select_widget.setFixedHeight(65)

        self.bottom_hlayout.addWidget(self.stop_route_widget, 1)
        self.bottom_hlayout.addWidget(self.animation_widget, 1)
        self.bottom_hlayout.addWidget(self.eta_widget, 1)
        self.bottom_hlayout.addWidget(self.dest_select_widget, 1)

        if debug:
            self.apply_debug_styling()
        else:
            self.apply_styling()

        self.show()

    def __update(self):
        pass

    def apply_debug_styling(self):
        # Debug styling
        debug_widgets = {
            self.speed_widget: ("Speed", "#e57373"),
            self.name_widget: ("Name", "#ffb74d"),
            self.time_widget: ("Time", "#fff176"),
            self.location_widget: ("Location", "#81c784"),
            self.map_widget: ("Map", "#64b5f6"),
            self.stop_route_widget: ("Stop Route", "#ba68c8"),
            self.animation_widget: ("Travel Animation", "#4dd0e1"),
            self.eta_widget: ("ETA", "#f06292"),
            self.dest_select_widget: ("Destination Select", "#a1887f"),
            self.list_turns: ("List Turns", "#ffb74d"),
        }

        for widget, (name, colour) in debug_widgets.items():
            widget.setStyleSheet(
                f"background-color: {colour};"
                "border:3px solid #333333;"
                "border-radius: 5px;"
            )

            label = QLabel(name)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("background: transparent; border: none;")

            layout = QVBoxLayout(widget)
            layout.setContentsMargins(2, 2, 2, 2)
            layout.addWidget(label)

    def apply_styling(self):
        pass

    def on_list_turns_presses(self):
        print("list turns")

    def on_stop_route_pressed(self):
        print("Route Stopped")

    def create_map(self, latitude, longitude, zoom_start = 12):
        map = folium.Map(
            location=[latitude, longitude],
            zoom_start=zoom_start,
            tiles='OpenStreetMap')
        
        folium.Marker(
            [latitude, longitude],
            icon=folium.Icon(color='red', icon='ion.car-sport-outline')
        ).add_to(map)

        plugins.LocateControl().add_to(map)

        return map

    def update_speed(self):
        pass

    def update_time(self):
        pass

    def find_destination(self):
        pass

    def get_estimated_time(self):
        pass

    def update_map(self):
        self.map = self.create_map()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName("CarNav")

    w = MainWindow("temp")

    sys.exit(app.exec_())
import folium
from folium import plugins

def create_map(latitude, longitude, zoom_start=18):
    """
    Create an interactive map with a custom marker at specified coordinates.
    
    Parameters:
    latitude (float): Latitude of the location
    longitude (float): Longitude of the location
    zoom_start (int): Initial zoom level of the map (default: 12)
    
    Returns:
    folium.Map: Interactive map object
    """
    # Create a map centered at the specified location
    m = folium.Map(location=[latitude, longitude], 
                   zoom_start=zoom_start,
                   tiles='OpenStreetMap')
    
    # Add a marker with a popup
    folium.Marker(
            [latitude, longitude],
            icon=folium.Icon(color='red', icon='ion.car-sport-outline')
        ).add_to(m)
    
    # Add fullscreen button
    plugins.Fullscreen().add_to(m)
    
    # Add location finder
    plugins.LocateControl().add_to(m)
    
    return m

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MapWindow(QMainWindow):
    def __init__(self, latitude, longitude, zoom_start=12):
        super().__init__()
        
        # Create the map
        self.map = create_map(latitude, longitude, zoom_start)
        
        # Save the map to an HTML file
        self.map.save('map.html')
        
        # Create a QWebEngineView widget
        self.browser = QWebEngineView()
        
        # Load the HTML content into the QWebEngineView
        self.browser.setHtml(self.map.get_root().render())
        
        # Set the central widget of the MainWindow to the QWebEngineView
        self.setCentralWidget(self.browser)
        
        # Set the window title
        self.setWindowTitle('Folium Map with PyQt5')
        
        # Set the window size
        self.resize(800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Example coordinates 
    latitude = -35.3265
    longitude = 149.053


    #35°19'35.0"S 149°03'32.3"E
    
    # Create the main window
    window = MapWindow(latitude, longitude)
    window.show()
    
    # Run the application
    sys.exit(app.exec_())

# External import

from pathlib import Path
import _thread
import pyrosm
import pynmea2
import pandas
import numpy
import pandarm
import time

# Interal imports

from gps.gps import GPSManager
from map.osm_import import OSMImporter
from map.loader import AreaLoader
from map.road_graph import RoadGraph
from navigation.navigation import NavigationController
from ui.ui import MainWindow


class CarNavApp:
    def __init__(self):
        self.GPSManager = GPSManager()
        self.OSMImporter = OSMImporter()
        self.AreaLoader = AreaLoader(self)
        self.ui = MainWindow(self)
        self.lat_lng_speed = [0, 0, 0]

        self.update_thread = _thread.start_new_thread(self._update)
        self.running = True

        self.RoadGraph = RoadGraph("Code/map/WEST.osm.pbf")
        self.RoadGraph.load()

        self.NavigationController = NavigationController(
            self,
            self.RoadGraph
        )

    def _update(self):
        while self.running:
            self.lat_lng_speed = self.GPSManager.get_location_speed()

            time.sleep(0.01)

    def get_location_speed(self):
        return self.lat_lng_speed

    def get_location(self):
        return [self.lat_lng_speed[0], self.lat_lng_speed[1]]

    def get_time(self):
        return time.localtime()

    def stop(self):
        self.running = False

        self.GPSManager.stop()

import Path

local_path = Path(__file__).parent

AREAS = {
    "Belconnen": local_path / "BELC.osm.pbf",
    "Booth": local_path / "BOOT.osm.pbf",
    " Canberra Cental": local_path / "CANB.osm.pbf",
    "Coree": local_path / "CORE.osm.pbf",
    "Cotter River": local_path / "COTT.osm.pbf",
    "Gungahlin": local_path / "GUNG.osm.pbf",
    "Hall": local_path / "HALL.osm.pbf",
    "Jerrabomberra": local_path / "JERR.osm.pbf",
    "Kowen": local_path / "KOWE.osm.pbf",
    "Majura": local_path / "MAJU.osm.pbf",
    "Molonglo Valley": local_path / "MOLO.osm.pbf",
    "Mount Clear": local_path / "MOUN.osm.pbf",
    "Paddys River": local_path / "PADD.osm.pbf",
    "Rendezvous Creek": local_path / "REND.osm.pbf",
    "Stromlo": local_path / "STRO.osm.pbf",
    "Tennent": local_path / "TENN.osm.pbf",
    "Tuggeranong": local_path / "TUGG.osm.pbf",
    "Weston Creek": local_path / "WEST.osm.pbf",
    "Woden Valley": local_path / "WODE.osm.pbf",
}
