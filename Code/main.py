# External import

import Path
import _thread
import pyosm
import pynmea2
import pandas
import numpy
import pandarm
import PyQt5i
import time

# Interal imports

from gps.gps import GPSManager
from map.osm_import import OSMImporter


class CarNavApp:
    def __init__(self):
        self.GPSManager = GPSManager()
        self.lat_lng_speed = [0, 0, 0]

        self.update_thread = _thread.start_new_thread(self._update)
        self.running = True

    def _update(self):
        while self.running:
            self.lat_lng_speed = self.GPSManager.get_location_speed()

            time.sleep(0.01)

    def get_location_speed(self):
        return self.lat_lng_speed

    def get_location(self):
        return [self.lat_lng_speed[0], self.lat_lng_speed[1]]

    def stop(self):
        self.running = False

        self.GPSManager.stop()
