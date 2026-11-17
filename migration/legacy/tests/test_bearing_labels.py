"""Printing, numeric precision, identity and fresh-data Jinja action checks."""
import importlib.util
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import ImageFont
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("bearing_labels", ROOT / "working_bearing_labels.py")
labels = importlib.util.module_from_spec(spec)
spec.loader.exec_module(labels)


def sample():
    return dict(taxonomy_1="hardware", taxonomy_2="bearing", taxonomy_3="6000_series",
                taxonomy_4="6000_size", taxonomy_5="10_mm_id", taxonomy_6="26_mm_od",
                taxonomy_7="8_mm_depth", id="10", od="26", width="8", series="6000", size="6000")


def text(svg, element):
    return svg.find(f".//*[@id='{element}']").text


def test_all_bearings_dimensions_words_and_text_fit():
    font = ImageFont.truetype(r"C:\Windows\Fonts\ARIALNB.TTF", 1000)
    sources = list((ROOT / "parts_source").glob("*/working.yaml"))
    assert sources
    for source in sources:
        part = labels.load(source)
        existing = labels.load(ROOT / "parts" / labels.identifier(part) / "working.yaml")
        assert labels.bip39_name(part) == existing["bip_39_3_word_space"]
        for size, (w, h, scale) in labels.FORMATS.items():
            svg = ET.fromstring(labels.render(part, size))
            assert (svg.get("width"), svg.get("height"), svg.get("viewBox")) == (f"{w}mm", f"{h}mm", f"0 0 {w} {h}")
            assert text(svg, "bearing-code") == part["size"]
            assert text(svg, "bearing-family") == part["series"]
            for field, key in [("id", "id"), ("od", "od"), ("width", "width")]:
                assert labels.Decimal(text(svg, f"bearing-{field}")) == labels.Decimal(part[key])
                node = svg.find(f".//*[@id='bearing-{field}']")
                assert font.getlength(node.text) / 1000 * float(node.get("font-size")) <= 10.41
            assert text(svg, "bip39") == existing["bip_39_3_word_space"]
            for node in svg.iter():
                assert not node.tag.endswith("image")
                if "fill" in node.attrib:
                    assert node.get("fill") in {"#000000", "#ffffff"}


def test_generated_id_is_not_confused_with_diameter():
    part = sample()
    part["id"] = labels.identifier(part)
    assert text(ET.fromstring(labels.render(part, "1_5x1")), "bearing-id") == "10"


def test_live_template_uses_changed_source_and_manual_values():
    part = sample()
    part["bip_39_3_word_space"] = labels.bip39_name(part)
    labels.add_actions(part)
    action = part["oomlout_ai_roboclick_1"]["actions"][0]
    assert "dict_data" not in action  # No frozen dimensions baked into the action.
    assert set(action["dict_data_yaml_files"]) == {"label_source", "label_manual"}
    template = labels.Environment(undefined=labels.StrictUndefined).from_string(Path(action["file_template"]).read_text(encoding="utf-8"))
    part["label_source"] = dict(sample(), id="12", od="28", width="8.25", series="NEW")
    svg = ET.fromstring(template.render(p=part))
    assert (text(svg, "bearing-id"), text(svg, "bearing-od"), text(svg, "bearing-width"), text(svg, "bearing-family")) == ("12", "28", "8.25", "NEW")
    part["label_manual"] = {"id_mm": 13, "width": 8.5, "family": "Manual"}
    svg = ET.fromstring(template.render(p=part))
    assert (text(svg, "bearing-id"), text(svg, "bearing-width"), text(svg, "bearing-family")) == ("13", "8.5", "Manual")


def test_overwrite_is_repeatable_and_preserves_other_files(tmp_path):
    templates = tmp_path / labels.TEMPLATE_DIR
    templates.mkdir(parents=True)
    for size in labels.FORMATS:
        (templates / f"{size}.svg.j2").write_bytes((ROOT / labels.TEMPLATE_DIR / f"{size}.svg.j2").read_bytes())
    part_name = labels.identifier(sample())
    source = tmp_path / "parts_source" / part_name / "working.yaml"
    source.parent.mkdir(parents=True)
    source.write_text(yaml.safe_dump(sample()), encoding="utf-8")
    directory = tmp_path / "parts" / part_name
    directory.mkdir(parents=True)
    original = "# Preserve this\nbip_39_3_word_space: icon shiver husband\noomlout_ai_roboclick_1:\n  actions:\n  - command: unrelated\n"
    (directory / "working.yaml").write_text(original, encoding="utf-8")
    for name in ["label_bearing_bold_3x2.png", "label_oomp.png", "initial_generated_icon.png"]:
        (directory / name).write_bytes(b"test")
    assert labels.regenerate(tmp_path) == (2, 1)
    first = (directory / "working.yaml").read_bytes()
    assert (directory / "working.yaml").read_text(encoding="utf-8").startswith(original)
    assert labels.regenerate(tmp_path) == (2, 0)
    assert first == (directory / "working.yaml").read_bytes()
    assert (directory / "label_oomp.png").exists()
    assert (directory / "initial_generated_icon.png").exists()
    data = labels.load(directory / "working.yaml")
    labels.add_actions(data, root=tmp_path, part_name=part_name)
    assert len([k for k in data if k.startswith("oomlout_ai_roboclick_")]) == 3
    source.write_text(yaml.safe_dump(dict(sample(), width="9.5")), encoding="utf-8")
    labels.regenerate(tmp_path)
    assert text(ET.fromstring((directory / "label_bearing_bold_3x2.svg").read_text(encoding="utf-8")), "bearing-width") == "9.5"


def test_invalid_dimensions_fail_before_render():
    with pytest.raises(ValueError, match="smaller"):
        labels.render(dict(sample(), od="9"), "3x2")


def test_decimal_source_folder_and_uppercase_family_are_not_double_counted(tmp_path):
    part = dict(sample(), series="MR", size="MR10", id="2.5", width="5.5",
                taxonomy_3="MR_series", taxonomy_4="MR10_size",
                taxonomy_5="2.5_mm_id", taxonomy_7="5.5_mm_depth")
    name = labels.identifier(part).lower()
    source = tmp_path / "parts_source" / name.replace(".", "_") / "working.yaml"
    source.parent.mkdir(parents=True)
    source.write_text(yaml.safe_dump(part), encoding="utf-8")
    directory = tmp_path / "parts" / name
    directory.mkdir(parents=True)
    (directory / "working.yaml").write_text(yaml.safe_dump(dict(part, id=labels.identifier(part))), encoding="utf-8")
    templates = tmp_path / labels.TEMPLATE_DIR
    templates.mkdir(parents=True)
    for size in labels.FORMATS:
        (templates / f"{size}.svg.j2").write_bytes((ROOT / labels.TEMPLATE_DIR / f"{size}.svg.j2").read_bytes())
    assert labels.regenerate(tmp_path) == (2, 0)
    data = labels.load(directory / "working.yaml")
    action = data["oomlout_ai_roboclick_1"]["actions"][0]
    assert Path(action["dict_data_yaml_files"]["label_source"]).resolve() == source.resolve()
    assert text(ET.fromstring((directory / "label_bearing_bold_3x2.svg").read_text(encoding="utf-8")), "bearing-id") == "2.5"
