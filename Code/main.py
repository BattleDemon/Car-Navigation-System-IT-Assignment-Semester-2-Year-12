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
