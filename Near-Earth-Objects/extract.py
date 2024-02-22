import json
import csv
from models import CloseApproach, NearEarthObject


def load_approaches(cad_json_path):
    with open(cad_json_path, "r") as f:
        reader = json.load(f)
        new_reader = []
        for data in reader["data"]:
            new_dict = {}
            for i, field in enumerate(reader["fields"]):
                new_dict[field] = data[i]
            new_reader.append(new_dict)
        approaches = []
        for line in new_reader:
            try:
                approach = CloseApproach(
                    time=line["cd"],
                    designation=line["des"],
                    distance=float(line["dist"]),
                    velocity=float(line["v_rel"]),
                )
            except Exception as e:
                print(e)
            else:
                approaches.append(approach)
    return approaches


def load_neos(neo_csv_path):
    with open(neo_csv_path, "r") as f:
        reader = csv.DictReader(f)
        neos = []
        for line in reader:
            line["name"] = line["name"] or None
            line["diameter"] = float(
                line["diameter"]) if line["diameter"] else None
            line["pha"] = False if line["pha"] in ["", "N"] else True
            try:
                neo = NearEarthObject(
                    designation=line["pdes"],
                    name=line["name"],
                    diameter=line["diameter"],
                    hazardous=line["pha"],
                )
            except Exception as e:
                print(e)
            else:
                neos.append(neo)
    return neos
