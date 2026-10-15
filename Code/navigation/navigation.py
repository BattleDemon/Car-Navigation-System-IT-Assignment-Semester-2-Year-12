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