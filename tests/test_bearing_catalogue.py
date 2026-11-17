"""Bearing-specific regressions: sources, geometry, units and population contracts."""
import copy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import numpy as np
import pytest

from bearing_io import write_yaml
from bearing_model_geometry import build_model, export_mesh, write_scad
from working_oomp_populate import get_options
from working_oomp_populate_bearing import populate_bearing
from working_oomp_declarations_bearing import declarations


def test_catalogue_coverage_identity_and_corrected_sources():
    options = get_options()
    assert len(options) == 339
    assert len({p["oomp_id"].lower() for p in options}) == 339
    sizes = {p["size"]: p for p in options}
    assert sizes["6208"]["dimensions_mm"] == {"bore": 40.0, "outside": 80.0, "width": 18.0}
    assert sizes["F608"]["dimensions_mm"]["flange_diameter"] == 25
    assert sizes["5300"]["dimensions_mm"]["width"] == 19
    assert sizes["5300"]["three_d_model_details"]["parameters"]["contact_angle_authority"] == "selected_catalogue_convention"


@pytest.mark.parametrize("pattern", ["_608_size_", "_f608_size_", "_5204_size_", "_5300_size_", "_mr31_size_", "_6830_size_"])
def test_closed_meshes_and_nominal_dimensions(pattern):
    part = get_options(filter=pattern)[0]
    recipe = part["three_d_model_details"]
    dimensions = part["dimensions_mm"]
    diameter = dimensions.get("flange_diameter", dimensions["outside"])
    counts = {}
    for variant in recipe["variants"]:
        mesh = build_model(recipe=recipe, variant=variant)
        assert mesh.is_watertight and mesh.is_winding_consistent
        assert mesh.volume > 0
        assert mesh.body_count == recipe["parameters"]["ball_count"] + 2
        np.testing.assert_allclose(mesh.extents, [diameter, diameter, dimensions["width"]])
        assert np.linalg.norm(mesh.vertices[:, :2], axis=1).min() == pytest.approx(dimensions["bore"] / 2)
        counts[variant] = len(mesh.faces)
    assert counts["display"] < counts["full"] / 2


def test_populate_has_every_geometry_drawing_and_render_input():
    part = get_options(filter="_f608_size_")[0]
    recipe = part["three_d_model_details"]
    assert part["oobb_details"]["components"] == recipe["parameters"]["components"]
    assert part["svg_details"]["dimensions_mm"] == part["dimensions_mm"]
    assert len(recipe["renders"]) == 4
    assert len(recipe["views"]) == 7
    assert recipe["studio"]["lights"]
    assert recipe["material"]["roughness"] > 0
    original = copy.deepcopy(part)
    build_model(recipe=recipe, variant="display")
    assert original == part


def test_populate_dimension_change_reaches_all_asset_recipes():
    declaration = next(p for p in declarations() if p["size"] == "608")
    declaration["dimensions"]["width"] = 8
    part = populate_bearing(declaration=declaration)
    assert part["svg_details"]["dimensions_mm"]["width"] == 8
    assert part["three_d_model_details"]["parameters"]["width"] == 8
    mesh = build_model(recipe=part["three_d_model_details"], variant="display")
    assert mesh.extents[2] == 8
    assert "8 x 22 x 8 mm" in part["label_details"]["dimensions"]


def test_filtered_population_does_not_erase_unselected_records(tmp_path):
    import working_oomp_populate
    existing = tmp_path / "parts_source/retained/working.yaml"
    write_yaml(path=existing, data={"keep": True})
    working_oomp_populate.main(root=tmp_path, filter="_608_size_")
    assert existing.read_text() == "keep: true\n"
    assert len(list((tmp_path / "parts_source").glob("*/working.yaml"))) == 2


def test_unknown_filter_fails_instead_of_silently_succeeding():
    with pytest.raises(ValueError, match="No bearings match"):
        get_options(filter="not-a-bearing")


def test_marked_docs_preserve_manual_notes_and_reject_broken_markers(tmp_path):
    from working_bearing_documentation import managed
    path = tmp_path / "README.md"
    path.write_text("Original specialist notes\n", encoding="utf-8")
    managed(path=path, body="New catalogue section")
    first = path.read_bytes()
    managed(path=path, body="New catalogue section")
    assert path.read_bytes() == first
    assert "Original specialist notes" in path.read_text()
    path.write_text("<!-- bearing-catalogue:start --> broken", encoding="utf-8")
    with pytest.raises(ValueError, match="Malformed"):
        managed(path=path, body="replacement")


def test_model_cache_rejects_corrupted_or_missing_artifacts(tmp_path):
    import hashlib
    from working_three_d_model import cached
    artifact = tmp_path / "model.stl"
    artifact.write_bytes(b"original artifact")
    manifest = {"fingerprint": "recipe-v1", "artifacts": {"model.stl": {"sha256": hashlib.sha256(artifact.read_bytes()).hexdigest()}}}
    (tmp_path / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    assert cached(output=tmp_path, fingerprint="recipe-v1")
    assert not cached(output=tmp_path, fingerprint="recipe-v2")
    artifact.write_bytes(b"changed artifact")
    assert not cached(output=tmp_path, fingerprint="recipe-v1")
    artifact.unlink()
    assert not cached(output=tmp_path, fingerprint="recipe-v1")


def test_scad_action_never_exports_stl_even_with_legacy_flag(tmp_path):
    import working_bearing_scad
    part = get_options(filter="_608_size_")[0]
    folder = tmp_path / "parts" / part["oomp_id"]
    write_yaml(path=folder / "working.yaml", data=part)
    working_bearing_scad.main(root=tmp_path, generate_stl=False)
    assert (folder / "3dpr.scad").is_file()
    assert not (folder / "3dpr.stl").exists()
    working_bearing_scad.main(root=tmp_path, generate_stl=True)
    assert not (folder / "3dpr.stl").exists()


def test_populated_exports_are_glb_only_and_stl_export_is_rejected(tmp_path):
    part = get_options(filter="_608_size_")[0]
    recipe = part["three_d_model_details"]
    assert recipe["model_formats"] == ["glb"]
    mesh = build_model(recipe=recipe, variant="display")
    with pytest.raises(ValueError, match="GLB"):
        export_mesh(mesh=mesh, path=tmp_path / "bearing.stl", material=recipe["material"])


def test_stl_removal_preserves_hard_linked_original_and_other_formats(tmp_path):
    import os
    from working_bearing_storage import remove_stl
    original = tmp_path / "original.stl"
    original.write_bytes(b"original source mesh")
    catalogue = tmp_path / "catalogue"
    catalogue.mkdir()
    os.link(original, catalogue / "legacy.STL")
    (catalogue / "bearing.glb").write_bytes(b"retained model")
    removed = remove_stl(root=catalogue)
    assert len(removed) == 1
    assert not (catalogue / "legacy.STL").exists()
    assert original.read_bytes() == b"original source mesh"
    assert (catalogue / "bearing.glb").read_bytes() == b"retained model"
