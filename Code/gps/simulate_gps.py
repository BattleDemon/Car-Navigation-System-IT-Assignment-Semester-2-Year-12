import time


class SimulatedGPS:
    def __init__(self, lat=-35.325833, lng=149.057750):
        self.lat = lat
        self.lng = lng
        self.speed = 0

        # Store the route coordinates and the index of the current position along that route
        self.route = []
        self.index = 0
        # Use a monotonic clock to control movement independently of changes to the system time
        self.last_update = time.monotonic()

    def set_route(self, coordinates):
        # Replace the previous route and reset the simulated vehicle to the beginning
        self.route = coordinates
        self.index = 0
        self.last_update = time.monotonic()

        if coordinates:
            self.lat, self.lng = coordinates[0]
            # Use a fixed simulated speed of 50 km/h while travelling, since it doesn't read the osm to see the real one
            self.speed = 50

    # Advance to the next road node once per second while a route is active
    def get_location_speed(self):
        if self.route and time.monotonic() - self.last_update >= 1:
            self.last_update = time.monotonic()

            if self.index < len(self.route) - 1:
                self.index += 1
                self.lat, self.lng = self.route[self.index]
            else:
                self.speed = 0

        # Return lat lnd speed so it can simulate the gps
        return [self.lat, self.lng, self.speed]

    def stop(self):
        self.route = []
        self.speed = 0