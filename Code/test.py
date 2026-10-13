from map.road_graph import RoadGraph


road_graph = RoadGraph("Code/map/WEST.osm.pbf")
graph = road_graph.load()

print("Nodes:", len(graph.nodes))
print("Edges:", len(graph.edges))

first_node = list(graph.nodes)[0]

print("First node ID:", first_node)
print("First node data:", graph.nodes[first_node])