import Path

local_path = Path(__file__).parent.parent
local_path.append("/Areas")


class AreaLoader:
    def __init__(self, owner):
        self.owner = owner
        self.location = {
            "Belconnen": [
                local_path / "BELC.osm.pbf",
                local_path / "BELC.geojson",
            ],
            "Booth": [
                local_path / "BOOT.osm.pbf",
                local_path / "BOOT.geojson",
            ],
            "Canberra Cental": [
                local_path / "CANB.osm.pbf",
                local_path / "CANB.geojson",
            ],
            "Coree": [
                local_path / "CORE.osm.pbf",
                local_path / "CORE.geojson",
            ],
            "Cotter River": [
                local_path / "COTT.osm.pbf",
                local_path / "COTT.geojson",
            ],
            "Gungahlin": [
                local_path / "GUNG.osm.pbf",
                local_path / "GUNG.geojson",
            ],
            "Hall": [
                local_path / "HALL.osm.pbf",
                local_path / "HALL.geojson",
            ],
            "Jerrabomberra": [
                local_path / "JERR.osm.pbf",
                local_path / "JERR.geojson",
            ],
            "Kowen": [
                local_path / "KOWE.osm.pbf",
                local_path / "KOWE.geojson",
            ],
            "Majura": [
                local_path / "MAJU.osm.pbf",
                local_path / "MAJU.geojson",
            ],
            "Molonglo Valley": [
                local_path / "MOLO.osm.pbf",
                local_path / "MOLO.geojson",
            ],
            "Mount Clear": [
                local_path / "MOUN.osm.pbf",
                local_path / "MOUN.geojson",
            ],
            "Paddys River": [
                local_path / "PADD.osm.pbf",
                local_path / "PADD.geojson",
            ],
            "Rendezvous Creek": [
                local_path / "REND.osm.pbf",
                local_path / "REND.geojson",
            ],
            "Stromlo": [
                local_path / "STRO.osm.pbf",
                local_path / "STRO.geojson",
            ],
            "Tennent": [
                local_path / "TENN.osm.pbf",
                local_path / "TENN.geojson",
            ],
            "Tuggeranong": [
                local_path / "TUGG.osm.pbf",
                local_path / "TUGG.geojson",
            ],
            "Weston Creek": [
                local_path / "WEST.osm.pbf",
                local_path / "WEST.geojson",
            ],
            "Woden Valley": [
                local_path / "WODE.osm.pbf",
                local_path / "WODE.geojson",
            ],
        }

        self.adjacentcies = {
            "Belconnen": [
                "Hall",
                "Gungahlin",
                "Canberra Central",
                "Molongolo Valley",
                "Stromlo",
                "Coree",
            ],
            "Booth": [
                "Mount Clear",
                "Rendezvous Creek",
                "Tennent",
            ],
            "Canberra Central": [
                "Belconnen",
                "Gungahlin",
                "Majura",
                "Jerrabomberra",
                "Woden Valley",
                "Weston Creek",
                "Molongolo Valley",
            ],
            "Coree": [
                "Belconnen",
                "Stromlo",
                "Paddys Creek",
                "Cotter River",
            ],
            "Cotter River": [
                "Coree",
                "Paddys Creek",
                "Tennent",
                "Rendezvous Creek",
            ],
            "Gungahlin": [
                "Hall",
                "Belconnen",
                "Canberra Central",
                "Majura",
            ],
            "Hall": [
                "Belconnen",
                "Gungahlin",
            ],
            "Jerrabomberra": [
                "Majura",
                "Canberra Central",
                "Woden Valley",
                "Tuggeranong",
            ],
            "Kowen": ["Majura"],
            "Majura": [
                "Kowen",
                "Gungahlin",
                "Canberra Central",
                "Jerrabomberra",
            ],
            "Molongolo Valley": [
                "Stromlo",
                "Belconnen",
                "Canberra Central",
                "Weston Creek",
            ],
            "Mount Clear": [
                "Rendezvous Creek",
                "Booth",
            ],
            "Paddys River": [
                "Cotter River",
                "Coree",
                "Stromlo",
                "Tuggeranong",
                "Tennent",
            ],
            "Rendezvous Creek": [
                "Cotter River",
                "Tennent",
                "Booth",
                "Mount Clear",
            ],
            "Stromlo": [
                "Coree",
                "Belconnen",
                "Molongolo Valley",
                "Weston Creek",
                "Tuggeranong",
                "Paddys Creek",
            ],
            "Tennent": [
                "Cotter River",
                "Paddys River",
                "Tuggeranong",
                "Booth",
                "Rendezvous Creek",
            ],
            "Tuggeranong": [
                "Stromlo",
                "Weston Creek",
                "Woden Valley",
                "Jerrabomberra",
                "Tennent",
                "Paddys River",
            ],
            "Weston Creek": [
                "Stromlo",
                "Molongolo Valley",
                "Canberra Central",
                "Woden Valley",
                "Tuggeranong",
            ],
            "Woden Valley": [
                "Weston Creek",
                "Canberra Central",
                "Jerrabomberra",
                "Tuggeranong",
            ],
        }

        self.located = False

        self.load_area = 1  # Number of adjacent areas to load: 1 Just the immediete adjacent, 2 their adjacentcies.

    def load_area(self):
        location = self.owner.get_location()  # in form [Lat, Lng]

        if self.located:
            # Check adjacent
            pass

        else:
            # Check all
            pass


# When load an area after the first time (Check all and find where we are using cord), then check adjacent first before doing the others
