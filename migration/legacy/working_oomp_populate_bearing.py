import csv
import os
from pathlib import Path

import yaml

BEARING_CSV = os.path.join("source_file", "dimension", "oomp_bearing_sizes.csv")
BEARING_INFO = Path(__file__).resolve().parent / "source_file" / "dimension" / "6700_series_info.yaml"


def add_bearing_info(options):
    """Keep researched catalogue information with the generated part records."""
    with BEARING_INFO.open(encoding="utf-8") as handle:
        research = yaml.safe_load(handle)
    for option in options:
        if option.get("series") != "6700":
            continue
        info = research["parts"].get(str(option.get("size")))
        if info:
            option.update(info)
            option["source_checked"] = research["checked"]
            option["weight_unit"] = "g"
            option["weight_note"] = "Approximate catalogue mass for the cited open bearing; varies by manufacturer and closure."
            option["availability_note"] = "Listed in the cited catalogue; current stock and lead time not confirmed."


def generate():
    options = []
    with open(BEARING_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            size   = str(row["size"]).strip()
            id_mm  = str(row["id"]).strip()
            od     = str(row["od"]).strip()
            width  = str(row["width"]).strip()
            weight = str(row["weight"]).strip().replace(",", "")
            series = str(row["series"]).strip()

            series_tax = f"{series}_series"
            id_tax     = id_mm.replace(".", "_") + "_mm_id"
            od_tax     = od.replace(".", "_")    + "_mm_od"
            depth_tax  = width.replace(".", "_") + "_mm_depth"

            option = {
                "taxonomy_1": "hardware",
                "taxonomy_2": "bearing",
                "taxonomy_3": series_tax,
                "taxonomy_4": f"{size}_size",
                "taxonomy_5": id_tax,
                "taxonomy_6": od_tax,
                "taxonomy_7": depth_tax,
                "id":     id_mm,
                "od":     od,
                "width":  width,
                "depth":  width,
                "series": series,
                "size":   size,
                "weight": weight,
            }
            options.append(option)
    add_bearing_info(options)
    return options
