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