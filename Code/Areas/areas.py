from pathlib import Path

local_path = Path(__file__).parent

AREAS = {
    "Belconnen": local_path / "BELC.osm.pbf",
    "Booth": local_path / "BOOT.osm.pbf",
    " Canberra Cental": local_path / "CANB.osm.pbf",
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
