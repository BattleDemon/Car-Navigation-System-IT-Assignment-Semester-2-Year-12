import Path
import _thread
import json
from shapely.geometry import Point, shape

local_path = Path(__file__).parent.parent
local_path.append("/Areas")


class AreaLoader:
    def __init__(self, owner):
        # Reference to the owner
        self.owner = owner
        # Dictionary containing the files associated with the districts and their adjacentcies
        self.locations = {
            "Belconnen": [
                local_path / "BELC.osm.pbf",
                local_path / "BELC.geojson",
                [
                    "Coree",
                    "Hall",
                    "Gungahlin",
                    "Canberra Central",
                    "Molongolo Valley",
                    "Stromlo",
                ],
            ],
            "Booth": [
                local_path / "BOOT.osm.pbf",
                local_path / "BOOT.geojson",
                [
                    "Mount Clear",
                    "Rendezvous Creek",
                    "Tennent",
                ],
            ],
            "Canberra Cental": [
                local_path / "CANB.osm.pbf",
                local_path / "CANB.geojson",
                [
                    "Belconnen",
                    "Gungahlin",
                    "Majura",
                    "Jerrabomberra",
                    "Woden Valley",
                    "Weston Creek",
                    "Molongolo Valley",
                ],
            ],
            "Coree": [
                local_path / "CORE.osm.pbf",
                local_path / "CORE.geojson",
                [
                    "Belconnen",
                    "Stromlo",
                    "Paddys Creek",
                    "Cotter River",
                ],
            ],
            "Cotter River": [
                local_path / "COTT.osm.pbf",
                local_path / "COTT.geojson",
                [
                    "Coree",
                    "Paddys Creek",
                    "Tennent",
                    "Rendezvous Creek",
                ],
            ],
            "Gungahlin": [
                local_path / "GUNG.osm.pbf",
                local_path / "GUNG.geojson",
                [
                    "Hall",
                    "Belconnen",
                    "Canberra Central",
                    "Majura",
                ],
            ],
            "Hall": [
                local_path / "HALL.osm.pbf",
                local_path / "HALL.geojson",
                [
                    "Belconnen",
                    "Gungahlin",
                ],
            ],
            "Jerrabomberra": [
                local_path / "JERR.osm.pbf",
                local_path / "JERR.geojson",
                [
                    "Majura",
                    "Canberra Central",
                    "Woden Valley",
                    "Tuggeranong",
                ],
            ],
            "Kowen": [
                local_path / "KOWE.osm.pbf",
                local_path / "KOWE.geojson",
                ["Majura"],
            ],
            "Majura": [
                local_path / "MAJU.osm.pbf",
                local_path / "MAJU.geojson",
                [
                    "Kowen",
                    "Gungahlin",
                    "Canberra Central",
                    "Jerrabomberra",
                ],
            ],
            "Molonglo Valley": [
                local_path / "MOLO.osm.pbf",
                local_path / "MOLO.geojson",
                [
                    "Stromlo",
                    "Belconnen",
                    "Canberra Central",
                    "Weston Creek",
                ],
            ],
            "Mount Clear": [
                local_path / "MOUN.osm.pbf",
                local_path / "MOUN.geojson",
                [
                    "Rendezvous Creek",
                    "Booth",
                ],
            ],
            "Paddys River": [
                local_path / "PADD.osm.pbf",
                local_path / "PADD.geojson",
                [
                    "Cotter River",
                    "Coree",
                    "Stromlo",
                    "Tuggeranong",
                    "Tennent",
                ],
            ],
            "Rendezvous Creek": [
                local_path / "REND.osm.pbf",
                local_path / "REND.geojson",
                [
                    "Cotter River",
                    "Tennent",
                    "Booth",
                    "Mount Clear",
                ],
            ],
            "Stromlo": [
                local_path / "STRO.osm.pbf",
                local_path / "STRO.geojson",
                [
                    "Coree",
                    "Belconnen",
                    "Molongolo Valley",
                    "Weston Creek",
                    "Tuggeranong",
                    "Paddys Creek",
                ],
            ],
            "Tennent": [
                local_path / "TENN.osm.pbf",
                local_path / "TENN.geojson",
                [
                    "Cotter River",
                    "Paddys River",
                    "Tuggeranong",
                    "Booth",
                    "Rendezvous Creek",
                ],
            ],
            "Tuggeranong": [
                local_path / "TUGG.osm.pbf",
                local_path / "TUGG.geojson",
                [
                    "Stromlo",
                    "Weston Creek",
                    "Woden Valley",
                    "Jerrabomberra",
                    "Tennent",
                    "Paddys River",
                ],
            ],
            "Weston Creek": [
                local_path / "WEST.osm.pbf",
                local_path / "WEST.geojson",
                [
                    "Stromlo",
                    "Molongolo Valley",
                    "Canberra Central",
                    "Woden Valley",
                    "Tuggeranong",
                ],
            ],
            "Woden Valley": [
                local_path / "WODE.osm.pbf",
                local_path / "WODE.geojson",
                [
                    "Weston Creek",
                    "Canberra Central",
                    "Jerrabomberra",
                    "Tuggeranong",
                ],
            ],
        }

        # If the location has been found and what it is
        self.located = False
        self.location = None
        # Exact latitude and longitude
        self.coordinates = None

        self.load_area = 1  # Number of adjacent areas to load: 1 Just the immediete adjacent, 2 their adjacentcies.

        # Running and its thread
        self.running = True
        self.update_thread = _thread.start_new_thread(self._update)

    def find_location(self):
        lat_lng = self.owner.get_location()  # in form [Lat, Lng]
        self.cordinates = Point(lat_lng[1], lat_lng[0])

        if self.located:
            # Check adjacent

            for area1 in self.located[2]:
                area = list(self.locations.keys()).index(area1)

                with open(area[1], "r") as f:
                    geojson_date = json.load(f)

                for feature in geojson_date["features"]:
                    polygon = shape(feature["geometry"])
                    if polygon.contains(self.coordinates):
                        self.location = area1
                        self.located = True
                        break

        else:
            # Check all
            for area in self.locations:
                # Check if the areas.geojson has the current lat_lng in it
                with open(area[1], "r") as f:
                    geojson_date = json.load(f)

                for feature in geojson_date["features"]:
                    polygon = shape(feature["geometry"])
                    if polygon.contains(self.coordinates):
                        self.location = area
                        self.located = True
                        break

    def load_areas(self):
        pass

    def _update(self):
        while self.running:
            pass


# When load an area after the first time (Check all and find where we are using cord), then check adjacent first before doing the others
