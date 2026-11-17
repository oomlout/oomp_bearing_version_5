"""Populate the bearing catalogue; all downstream recipes are resolved here."""
import fnmatch
from pathlib import Path
from bearing_io import ROOT, write_yaml
from working_oomp_declarations_bearing import declarations
from working_oomp_populate_bearing import populate_bearing


def get_options(**kwargs):
    options = []
    identifiers = set()
    for declaration in declarations(**kwargs):
        identifier = declaration["oomp_id"]
        if identifier in identifiers:
            raise ValueError(f"Duplicate bearing: {identifier}")
        identifiers.add(identifier)
        pattern = kwargs.get("filter", "")
        if pattern and pattern not in identifier and not fnmatch.fnmatchcase(identifier, pattern):
            continue
        options.append(populate_bearing(declaration=declaration))
    if kwargs.get("filter") and not options:
        raise ValueError(f"No bearings match {kwargs['filter']!r}")
    return options


def main(**kwargs):
    root = Path(kwargs.get("root", ROOT))
    options = get_options(**kwargs)
    for option in options:
        write_yaml(path=root / "parts_source" / option["oomp_id"] / "working.yaml", data=option)
    print(f"Populated {len(options)} bearing recipes", flush=True)
    return options


if __name__ == "__main__":
    main()
