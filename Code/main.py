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