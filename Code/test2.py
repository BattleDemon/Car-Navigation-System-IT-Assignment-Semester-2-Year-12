from map.road_graph import RoadGraph
from navigation.routing import Router


road_graph = RoadGraph("Code/map/act.osm.pbf")
road_graph.load()

router = Router(road_graph)

route = router.calculate_route(
    -35.2809,
    149.1300,
    -35.2387,
    149.0844
)

if route:
    print("Route nodes:", len(route))

    coordinates = router.get_route_coordinates(route)

    print("First coordinate:", coordinates[0])
    print("Last coordinate:", coordinates[-1])