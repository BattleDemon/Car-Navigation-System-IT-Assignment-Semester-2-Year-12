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
        # Local refrence to latitude, longitude, and speed
        self.lat_lng_speed = [None, None, None]
        self.running = True # if app is running

        # if the app is simulated or actually using the gps
        if simulate:
            self.GPSManager = SimulatedGPS()
        else:
            self.GPSManager = GPSManager()

        # get the latitude and longitude from gpsmanager
        self.lat_lng_speed = self.GPSManager.get_location_speed()

        # Load the osm data for weston (feel free to test with other areas, or larger, but some might take a while to load)
        self.RoadGraph = RoadGraph("Code/map/WEST.osm.pbf")
        self.RoadGraph.load()

        # Define a navigation controller
        self.NavigationController = NavigationController(
            self,
            self.RoadGraph
        )

        # Set the ui
        self.ui = MainWindow(self)

        # create the update thread
        self.update_thread = _thread.start_new_thread(
            self._update,
            ()
        )

    # Update thread
    def _update(self):
        while self.running:
            # Get updated location
            self.lat_lng_speed = self.GPSManager.get_location_speed()

            # Wait so not constantly getting location
            time.sleep(0.25)

    # Get refrence to lat lng speed
    def get_location_speed(self):
        return self.lat_lng_speed

    # Same as above but without speed
    def get_location(self):
        return [self.lat_lng_speed[0], self.lat_lng_speed[1]]

    # get time
    def get_time(self):
        return time.localtime()

    # Stop the app
    def stop(self):
        self.running = False

        self.GPSManager.stop()

    # Find the destination
    def set_destination(self, latitude, longitude):
        # Calculate the route using the navigation controller
        route = self.NavigationController.set_destination(
            latitude, longitude
        )

        # If there is a route defined
        if route is None:
            print("Route calculation failed")
            return None

        print(f"Route calculated: {len(route)} coordinates")

        # Start simulated movement along the calculated route
        if isinstance(self.GPSManager, SimulatedGPS): # Checks if it is simulated or not (isinstance of class)
            self.GPSManager.set_route(route)

        return route

# Run the game locally with simulated since gps not on your computer
if __name__ == "__main__":
    app = QApplication(sys.argv)

    car_nav = CarNavApp(simulate=True)

    sys.exit(app.exec_())
