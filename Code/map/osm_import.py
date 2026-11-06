from pyrosm import OSM
from pathlib import Path


class OSMImporter:
    def __init__(self, file_path: Path):
        # The file then turned into osm
        self.osm_file = file_path
        self.osm = OSM(self.osm_file)

        self.nodes, self.edges = self.osm.get_network(
            nodes=True, network_type="driving"
        )

        self.graph = self.osm.to_graph(self.nodes, self.edges, simplify=True)
