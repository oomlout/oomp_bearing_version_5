"""Mesh and SCAD backends consume fully populated components without size guesses."""
import json
import numpy as np
import trimesh
from pathlib import Path
from bearing_io import write_text


def build_model(**kwargs):
    recipe = kwargs["recipe"]
    quality = recipe["variants"][kwargs["variant"]]
    meshes = []
    components = []
    for component in recipe["parameters"]["components"]:
        if component["shape"] == "revolved_profile":
            mesh = trimesh.creation.revolve(linestring=component["profile_mm"], sections=quality["angular_segments"])
        elif component["shape"] == "sphere":
            mesh = trimesh.creation.icosphere(subdivisions=quality["sphere_subdivisions"], radius=component["radius_mm"])
            mesh.apply_translation(component["centre_mm"])
        else:
            raise ValueError(f"Unknown component shape: {component['shape']}")
        if mesh.volume < 0:
            mesh.invert()
        if not mesh.is_watertight or not mesh.is_winding_consistent or mesh.volume <= 0:
            raise ValueError(f"Invalid bearing component: {component['name']}")
        meshes.append(mesh)
        components.append({"name": component["name"], "faces": len(mesh.faces)})
    mesh = trimesh.util.concatenate(meshes)
    mesh.metadata["components"] = components
    return mesh


def export_mesh(**kwargs):
    mesh = kwargs["mesh"]
    path = Path(kwargs["path"])
    if path.suffix.lower() != ".glb":
        raise ValueError("Bearing mesh exports use GLB; STL files are not retained")
    material = kwargs["material"]
    web = mesh.copy()
    web.apply_transform(np.array([[.001, 0, 0, 0], [0, 0, .001, 0], [0, -.001, 0, 0], [0, 0, 0, 1]]))
    web.visual = trimesh.visual.TextureVisuals(material=trimesh.visual.material.PBRMaterial(
        name=material["name"], baseColorFactor=[round(v * 255) for v in material["base_colour_srgb"]] + [255],
        metallicFactor=material["metallic"], roughnessFactor=material["roughness"],
    ))
    scene = trimesh.Scene(web)
    scene.metadata.update(units="metres", source_units="mm", up_axis="Y")
    path.write_bytes(trimesh.exchange.gltf.export_glb(scene))


def write_scad(**kwargs):
    part = kwargs["part"]
    details = part["oobb_details"]
    lines = ["// Open bearing presentation, dimensions in millimetres.", "// " + part["model_note"], f"$fn = {details['angular_segments']};", ""]
    for component in details["components"]:
        lines.append("// " + component["name"])
        if component["shape"] == "revolved_profile":
            lines.append("rotate_extrude() polygon(points=" + json.dumps(component["profile_mm"]) + ");")
        else:
            lines.append("translate(" + json.dumps(component["centre_mm"]) + ") sphere(r=" + str(component["radius_mm"]) + ");")
    write_text(path=Path(kwargs["folder"]) / "3dpr.scad", text="\n".join(lines) + "\n")
