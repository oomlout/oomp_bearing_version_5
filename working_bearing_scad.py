"""Write editable OpenSCAD from populated bearing components."""
from bearing_io import records
from bearing_model_geometry import write_scad


def main(**kwargs):
    count = 0
    for path, part in records(**kwargs):
        write_scad(part=part, folder=path.parent)
        count += 1
    print(f"Wrote {count} bearing SCAD recipes", flush=True)
    return count
