from pyrosm import OSM


class RoadGraph:
    def __init__(self, osm_file):
        # Open the locally stored OpenStreetMap data using Pyrosm
        self.osm_file = osm_file

        self.osm = None
        self.nodes = None
        self.edges = None
        self.graph = None

    def load(self):
        self.osm = OSM(self.osm_file)

        # Extract the road network suitable for driving, including its road nodes and connections
        self.nodes, self.edges = self.osm.get_network(
            network_type="driving", nodes=True
        )

        print(self.edges.columns)

        # Convert the extracted road network into a NetworkX graph for use by the routing algorithm
        self.graph = self.osm.to_graph(self.nodes, self.edges, graph_type="networkx")

        return self.graph

