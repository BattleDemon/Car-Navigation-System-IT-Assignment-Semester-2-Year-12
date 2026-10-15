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
