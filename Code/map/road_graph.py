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
            network_type="driving",
            nodes=True
        )

        self.graph = self.osm.to_graph(
            self.nodes,
            self.edges,
            graph_type="networkx"
        )

        return self.graph