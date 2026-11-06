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
        self.running = True
        self.update_thread = _thread.start_new_thread(self._update)
        

    def _update(self):
        while self.running:
            try:
                rawdata = self.ser.readline().decode(
                    "ascii", errors="ignore"
                ).strip()

                # Only process valid RMC messages
                if not rawdata.startswith(("$GNRMC", "$GPRMC")):
                    continue

                data = pynmea2.parse(rawdata)

                # Ignore messages without a valid GPS fix
                if data.status != "A":
                    continue

                lat = data.latitude
                lng = data.longitude

                # Convert speed from knots to km/h
                speed_knots = float(data.spd_over_grnd or 0)
                speed = speed_knots * 1.852

                self._set_location_speed(lat, lng, speed)

            except (pynmea2.ParseError, ValueError):
                continue

            except (serial.SerialException, OSError):
                if self.running:
                    print("GPS connection lost")
                break

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

import time


class SimulatedGPS:

    def __init__(self, lat=-35.325833, lng=149.057750):
        self.lat = lat
        self.lng = lng
        self.speed = 0

        self.route = []
        self.index = 0
        self.last_update = time.monotonic()

    def set_route(self, coordinates):
        self.route = coordinates
        self.index = 0
        self.last_update = time.monotonic()

        if coordinates:
            self.lat, self.lng = coordinates[0]
            self.speed = 50

    def get_location_speed(self):
        if self.route and time.monotonic() - self.last_update >= 1:
            self.last_update = time.monotonic()

            if self.index < len(self.route) - 1:
                self.index += 1
                self.lat, self.lng = self.route[self.index]
            else:
                self.speed = 0

        return [self.lat, self.lng, self.speed]

    def stop(self):
        self.route = []
        self.speed = 0

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

            if self.graph.is_multigraph():
                edge = list(edges.values())[0]
            else:
                edge = edges

            length_speed.append([
                edge.get("length"),
                edge.get("maxspeed")
            ])

        return length_speed

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
            if length is None:
                continue

            try:
                speed = float(speed)

                if speed <= 0:
                    speed = 50

            except (ValueError, TypeError):
                speed = 50

            distance_km = length / 1000
            time_hours = distance_km / speed

            total_minutes += time_hours * 60

    def calculate_estimated_distance(self):
        pass

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
import os

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = (
    "--disable-gpu --disable-gpu-compositing"
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

#from offline_folium import offline
import folium
from folium import plugins

from PyQt5.QtCore import Qt, QTimer

import sys
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
        self.speed_widget = QLabel("0 km/h")
        self.name_widget = QLabel("CarNav")
        self.time_widget = QLabel("00:00")
        self.location_widget = QLabel("GPS: No Location")

        self.speed_widget.setAlignment(Qt.AlignCenter)
        self.name_widget.setAlignment(Qt.AlignCenter)
        self.time_widget.setAlignment(Qt.AlignCenter)
        self.location_widget.setAlignment(Qt.AlignCenter)

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
        self.map = self.create_map(-35.325833, 149.057750,17)
        self.map.save('map.html')
        self.map_widget.setHtml(self.map.get_root().render())

        # Transparent overlay positioned over the map
        self.middle_glayout_widget = QWidget()
        self.middle_glayout_widget.setStyleSheet(
            "background: transparent; border: none;"
        )
        self.middle_glayout_widget.setAttribute(
            Qt.WA_TransparentForMouseEvents,
            True
        )
        self.middle_glayout_widget.hide()

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
        self.stop_route_widget = QPushButton("Stop")
        self.animation_widget = QProgressBar()
        self.eta_widget = QLabel("ETA: -- min")
        self.dest_select_widget = QLineEdit()

        self.animation_widget.setRange(0, 100)
        self.animation_widget.setValue(0)

        self.eta_widget.setAlignment(Qt.AlignCenter)

        self.dest_select_widget.setPlaceholderText("Lat, Lng")

        self.stop_route_widget.clicked.connect(self.on_stop_route_pressed)

        self.stop_route_widget.setFixedSize(65, 65)
        self.animation_widget.setFixedHeight(65)
        self.eta_widget.setFixedSize(100, 65)
        self.dest_select_widget.setFixedHeight(65)

        self.bottom_hlayout.addWidget(self.stop_route_widget, 1)
        self.bottom_hlayout.addWidget(self.animation_widget, 1)
        self.bottom_hlayout.addWidget(self.eta_widget, 1)
        self.bottom_hlayout.addWidget(self.dest_select_widget, 1)

        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)

        self.gps_timer = QTimer(self)
        self.gps_timer.timeout.connect(self.update_from_app)
        self.gps_timer.start(200)

        self.map_timer = QTimer(self)
        self.map_timer.timeout.connect(self.refresh_map)
        self.map_timer.start(1000)

        self.update_time()

        self.dest_select_widget.returnPressed.connect(
            self.find_destination
        )

        if debug:
            self.apply_debug_styling()
        else:
            self.apply_styling()

        self.destination = None

        self.show()

    def update_from_app(self):
        lat, lng, speed = (
            self.car_nav_controller.get_location_speed()
        )

        if speed is not None:
            self.update_speed(speed)

        self.update_location(lat, lng)

        gps = self.car_nav_controller.GPSManager

        if hasattr(gps, "route") and gps.route:
            progress = (
                gps.index / max(1, len(gps.route) - 1)
            ) * 100

            self.update_progress(progress)

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

    def refresh_map(self):
        lat, lng = self.car_nav_controller.get_location()

        if lat is None or lng is None:
            return

        gps = self.car_nav_controller.GPSManager
        route = self.car_nav_controller.NavigationController.get_route()

        # Only display the remaining route
        if hasattr(gps, "index") and route:
            route = route[gps.index:]

        # Move the existing vehicle marker
        javascript = f"""
            {self.vehicle_marker.get_name()}.setLatLng([{lat}, {lng}]);
        """

        # Update the existing route line
        if self.route_line is not None:
            javascript += f"""
                {self.route_line.get_name()}.setLatLngs({route});
            """

        self.map_widget.page().runJavaScript(javascript)

    def apply_styling(self):
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #E0E0E0;
                font-family: Arial;
            }

            QLabel {
                border: none;
                background: transparent;
            }

            QPushButton {
                background-color: #303030;
                border: 1px solid #444444;
                border-radius: 8px;
                padding: 8px;
                color: #E0E0E0;
            }

            QPushButton:pressed {
                background-color: #505050;
            }

            QLineEdit {
                background-color: #303030;
                border: 1px solid #444444;
                border-radius: 8px;
                padding: 8px;
                color: #E0E0E0;
            }

            QProgressBar {
                background-color: #303030;
                border: 1px solid #444444;
                border-radius: 8px;
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #888888;
                border-radius: 7px;
            }
        """)

        self.speed_widget.setStyleSheet(
            "font-size: 22px; font-weight: bold;"
        )

        self.name_widget.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        self.time_widget.setStyleSheet(
            "font-size: 16px;"
        )

        self.location_widget.setStyleSheet(
            "font-size: 13px;"
        )

        self.eta_widget.setStyleSheet(
            "font-size: 15px; font-weight: bold;"
        )

    def on_list_turns_presses(self):
        print("list turns")

    def on_stop_route_pressed(self):
        self.car_nav_controller.NavigationController.clear_route()

        gps = self.car_nav_controller.GPSManager

        if isinstance(gps, SimulatedGPS):
            gps.stop()

        self.destination = None
        self.update_eta()
        self.update_progress(0)

        lat, lng = self.car_nav_controller.get_location()

        if lat is not None and lng is not None:
            self.update_map(lat, lng)

        print("Route stopped")

    def create_map(self, latitude, longitude, zoom_start, route=None):
        map = folium.Map(
            location=[latitude, longitude],
            zoom_start=zoom_start,
            tiles="OpenStreetMap"
        )

        self.vehicle_marker = folium.Marker(
            [latitude, longitude],
            tooltip="Current Location",
            icon=folium.Icon(color="red")
        )

        self.vehicle_marker.add_to(map)

        self.route_line = None

        if route:
            self.route_line = folium.PolyLine(
                route,
                color="blue",
                weight=5
            )
            self.route_line.add_to(map)

        return map

    def update_speed(self, speed=0):
        self.speed_widget.setText(f"{speed:.0f} km/h")


    def update_time(self):
        from datetime import datetime

        current_time = datetime.now().strftime("%H:%M")
        self.time_widget.setText(current_time)


    def update_location(self, latitude=None, longitude=None):
        if latitude is None or longitude is None:
            self.location_widget.setText("GPS: No Location")
        else:
            self.location_widget.setText(
                f"{latitude:.5f}, {longitude:.5f}"
            )


    def update_eta(self, minutes=None):
        if minutes is None:
            self.eta_widget.setText("ETA: -- min")
        else:
            self.eta_widget.setText(
                f"ETA: {minutes:.0f} min"
            )


    def update_progress(self, progress=0):
        self.animation_widget.setValue(
            max(0, min(100, int(progress)))
        )

    def update_map(self, latitude, longitude, zoom_start=17, route=None):
        self.map = self.create_map(
            latitude,
            longitude,
            zoom_start=zoom_start,
            route=route
        )

        self.map_widget.setHtml(
            self.map.get_root().render()
        )

    def find_destination(self):
        try:
            # Read the coordinates entered by the user
            text = self.dest_select_widget.text()

            latitude, longitude = map(
                float, text.split(",")
            )

            # Check that coordinates are valid
            if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
                raise ValueError("Coordinates out of range")

        except ValueError:
            print("Invalid destination coordinates")
            return

        # Ask the main application to calculate a route
        route = self.car_nav_controller.set_destination(
            latitude, longitude
        )

        if route is None:
            print("Unable to calculate route")
            return

        # Get current GPS location
        current_lat, current_lng = (
            self.car_nav_controller.get_location()
        )

        # Display the calculated route
        self.update_map(
            current_lat,
            current_lng,
            route=route
        )

        # Display estimated travel time
        minutes = (
            self.car_nav_controller
            .NavigationController
            .calculate_estimated_time()
        )

        self.update_eta(minutes)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName("CarNav")

    w = MainWindow("temp")
    w.update_location(-35.325833, 149.057750)

    sys.exit(app.exec_())

# External import

from pathlib import Path
import _thread
import pyrosm
import pynmea2
import pandas
import numpy
import time

# Interal imports

from gps.gps import GPSManager
from gps.simulate_gps import SimulatedGPS
from map.osm_import import OSMImporter
from map.loader import AreaLoader
from map.road_graph import RoadGraph
from navigation.navigation import NavigationController
from ui.ui import MainWindow

import sys
from PyQt5.QtWidgets import QApplication


class CarNavApp:
    def __init__(self, simulate=True):
        self.lat_lng_speed = [None, None, None]
        self.running = True

        if simulate:
            self.GPSManager = SimulatedGPS()
        else:
            self.GPSManager = GPSManager()

        self.lat_lng_speed = self.GPSManager.get_location_speed()

        self.RoadGraph = RoadGraph("Code/map/WEST.osm.pbf")
        self.RoadGraph.load()

        self.NavigationController = NavigationController(
            self,
            self.RoadGraph
        )

        self.ui = MainWindow(self)

        self.update_thread = _thread.start_new_thread(
            self._update,
            ()
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

    def set_destination(self, latitude, longitude):
        # Calculate the route using the navigation controller
        route = self.NavigationController.set_destination(
            latitude, longitude
        )

        if route is None:
            print("Route calculation failed")
            return None

        print(f"Route calculated: {len(route)} coordinates")

        # Start simulated movement along the calculated route
        if isinstance(self.GPSManager, SimulatedGPS):
            self.GPSManager.set_route(route)

        return route

if __name__ == "__main__":
    app = QApplication(sys.argv)

    car_nav = CarNavApp(simulate=True)

    sys.exit(app.exec_())