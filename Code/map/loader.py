import Path

local_path = Path(__file__).parent.parent
local_path.append("/Areas")


class AreaLoader:
    def __init__(self):
        self.location = {
            "Belconnen": local_path / "BELC.osm.pbf",
            "Booth": local_path / "BOOT.osm.pbf",
            "Canberra Cental": local_path / "CANB.osm.pbf",
            "Coree": local_path / "CORE.osm.pbf",
            "Cotter River": local_path / "COTT.osm.pbf",
            "Gungahlin": local_path / "GUNG.osm.pbf",
            "Hall": local_path / "HALL.osm.pbf",
            "Jerrabomberra": local_path / "JERR.osm.pbf",
            "Kowen": local_path / "KOWE.osm.pbf",
            "Majura": local_path / "MAJU.osm.pbf",
            "Molonglo Valley": local_path / "MOLO.osm.pbf",
            "Mount Clear": local_path / "MOUN.osm.pbf",
            "Paddys River": local_path / "PADD.osm.pbf",
            "Rendezvous Creek": local_path / "REND.osm.pbf",
            "Stromlo": local_path / "STRO.osm.pbf",
            "Tennent": local_path / "TENN.osm.pbf",
            "Tuggeranong": local_path / "TUGG.osm.pbf",
            "Weston Creek": local_path / "WEST.osm.pbf",
            "Woden Valley": local_path / "WODE.osm.pbf",
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

        self.load_area = 1  # Number of adjacent areas to load: 1 Just the immediete adjacent, 2 their adjacentcies.

    def load_area():
        pass

    def load_region():
        pass
