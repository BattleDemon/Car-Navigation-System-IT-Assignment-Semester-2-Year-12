from map.road_graph import RoadGraph
from navigation.navigation import NavigationController


class TestOwner:
    def __init__(self):
        # Middle of Coolo
        self.location = [-35.3413, 149.0527]

    def get_location(self):
        return self.location


owner = TestOwner()

road_graph = RoadGraph("Code/map/WEST.osm.pbf")
road_graph.load()

navigation = NavigationController(
    owner,
    road_graph
)

# Destination is school just outside parking lot
route = navigation.set_destination(
    -35.325833,
    149.057750
)

if route is None:
    print("Route calculation failed")

else:
    print("Destination:", navigation.get_destination())
    print("Route points:", len(route))

    print("First route coordinate:")
    print(route[0])

    print("Last route coordinate:")
    print(route[-1])

    print("\nFirst 10 route coordinates:")

    for coordinate in route[:10]:
        print(coordinate)

    print("\nLast 10 route coordinates:")

    for coordinate in route[-10:]:
        print(coordinate)

    mid = len(route) // 2

    start = max(0, mid - 5)
    end = min(len(route), mid + 5)

    print("\nMiddle 10 route coordinates:")
    mid_10 =  route[start:end]
    
    for coordinate in mid_10:
        print(coordinate)