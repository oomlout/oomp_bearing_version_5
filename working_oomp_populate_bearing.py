"""Verbose population stages: identity, dimensions, geometry, drawing, presentation."""
import copy
import math
from mechanical_model_render import presentation_defaults


def race_profile(**kwargs):
    """Resolve a closed radial/Z section now, not during mesh or SCAD generation."""
    p = kwargs["parameters"]
    outer = kwargs["outer"]
    rows = kwargs["rows"]
    width = p["width"]
    edge = min(p["edge"], width / 10)
    shoulder = p["outer_shoulder"] if outer else p["inner_shoulder"]
    zs = {0.0, edge, width - edge, width}
    for zc in rows:
        for index in range(41):
            z = zc - p["groove_radius"] + 2 * p["groove_radius"] * index / 40
            if edge < z < width - edge:
                zs.add(z)
    track = []
    for z in sorted(zs):
        radius = shoulder
        for zc in rows:
            if abs(z - zc) < p["groove_radius"]:
                arc = math.sqrt(p["groove_radius"] ** 2 - (z - zc) ** 2)
                radius = max(radius, p["pitch_radius"] + arc) if outer else min(radius, p["pitch_radius"] - arc)
        track.append([radius, z])
    if outer:
        outside = p["outside"] / 2
        boundary = [[outside - edge, 0], [outside, edge], [outside, width - edge], [outside - edge, width]]
        if "flange_diameter" in p:
            flange = p["flange_diameter"] / 2
            thickness = p["flange_thickness"]
            bevel = p["flange_edge"]
            boundary = [[flange - bevel, 0], [flange, bevel], [flange, thickness - bevel], [flange - bevel, thickness], [outside, thickness], [outside, width - edge], [outside - edge, width]]
        profile = boundary + list(reversed(track))
    else:
        bore = p["bore"] / 2
        boundary = [[bore + edge, width], [bore, width - edge], [bore, edge], [bore + edge, 0]]
        profile = track + boundary
    profile.append(copy.deepcopy(profile[0]))
    return profile


def populate_bearing(**kwargs):
    declaration = copy.deepcopy(kwargs["declaration"])
    dimensions = copy.deepcopy(declaration["dimensions"])
    bore = dimensions["bore"]
    outside = dimensions["outside"]
    width = dimensions["width"]
    if not 0 < bore < outside or width <= 0:
        raise ValueError(f"Invalid bearing envelope: {declaration['size']}")

    # Stage 1: identity and preserved catalogue evidence.
    part = copy.deepcopy(declaration["catalogue_metadata"])
    part["catalogue_schema"] = "oomp_bearing_v5"
    part["oomp_id"] = declaration["oomp_id"]
    part["id"] = declaration["oomp_id"]
    part["size"] = declaration["size"]
    part["series"] = declaration["series"]
    part["family"] = declaration["family"]
    part["taxonomy_1"] = "hardware"
    part["taxonomy_2"] = "bearing"
    part["taxonomy_3"] = declaration["series"] + "_series"
    part["taxonomy_4"] = declaration["size"] + "_size"
    part["taxonomy_5"] = f"{bore:g}_mm_id"
    part["taxonomy_6"] = f"{outside:g}_mm_od"
    part["taxonomy_7"] = f"{width:g}_mm_depth"
    part["name"] = f"{part['size']} bearing"
    part["name_proper"] = part["name"]
    part["directory"] = "parts/" + part["oomp_id"]
    part["link_github"] = "https://github.com/oomlout/oomp_bearing_version_5/tree/main/" + part["directory"]

    # Stage 2: explicit physical dimensions and their authority.
    part["dimensions_mm"] = dimensions
    part["bore"] = bore
    part["od"] = outside
    part["width"] = width
    part["depth"] = width
    part["dimension_authority"] = declaration["dimension_authority"]
    part["source_checked"] = declaration["source_checked"]
    part["sources"] = declaration["sources"]
    part["model_note"] = declaration["model_note"]
    part["closure"] = "open"

    # Stage 3: freeze every mesh dimension and component into the population record.
    spec = declaration["internal_geometry"]
    parameters = copy.deepcopy(spec["parameters"])
    parameters.update(dimensions)
    parameters["identity"] = part["oomp_id"]
    parameters["specification"] = f"{part['size']} / {bore:g} x {outside:g} x {width:g} mm"
    parameters["characteristic_dimension_mm"] = max(outside, dimensions.get("flange_diameter", outside), width)
    parameters["characteristic_dimension_basis"] = "maximum nominal envelope dimension"
    parameters["ball_count"] = spec["ball_count"]
    parameters["balls_per_row"] = spec["balls_per_row"]
    parameters["row_count"] = spec["row_count"]
    parameters["ball_specification"] = spec["ball_specification"]
    parameters["contact_angle_authority"] = spec["contact_angle_authority"]
    parameters["row_centres_z"] = [width / 2] if spec["row_count"] == 1 else [width / 4, 3 * width / 4]
    components = []
    for outer in [True, False]:
        component = {}
        component["name"] = "outer_race" if outer else "inner_race"
        component["shape"] = "revolved_profile"
        component["profile_mm"] = race_profile(parameters=parameters, rows=parameters["row_centres_z"], outer=outer)
        components.append(component)
    for row_index, z in enumerate(parameters["row_centres_z"]):
        for ball_index in range(parameters["balls_per_row"]):
            angle = 2 * math.pi * ball_index / parameters["balls_per_row"]
            component = {}
            component["name"] = f"ball_row_{row_index + 1}_{ball_index + 1}"
            component["shape"] = "sphere"
            component["radius_mm"] = parameters["ball_radius"]
            component["centre_mm"] = [parameters["pitch_radius"] * math.cos(angle), parameters["pitch_radius"] * math.sin(angle), z]
            components.append(component)
    parameters["components"] = components

    # Stage 4: geometry quality, file formats and every studio/render setting.
    recipe = {}
    recipe["schema_version"] = 1
    recipe["generator"] = "bearing_open"
    recipe["output_folder"] = "three_d_model"
    recipe["parameters"] = parameters
    recipe["modelling_note"] = part["model_note"]
    recipe["dimension_authority"] = part["dimension_authority"]
    recipe["model_formats"] = ["glb"]
    recipe["variants"] = {}
    recipe["variants"]["full"] = {}
    recipe["variants"]["full"]["angular_segments"] = 128
    recipe["variants"]["full"]["sphere_subdivisions"] = 3
    recipe["variants"]["display"] = {}
    recipe["variants"]["display"]["angular_segments"] = 32
    recipe["variants"]["display"]["sphere_subdivisions"] = 2
    recipe["views"] = ["isometric", "front", "back", "left", "right", "top", "bottom"]
    presentation = presentation_defaults(family="bearing", finish="satin")
    presentation["material"]["name"] = "Illustrative polished bearing steel"
    presentation["material"]["roughness"] = 0.22
    presentation["material"]["note"] = "Illustrative bearing steel; material grade and finish are not specified."
    presentation["studio"]["low_samples"] = 24
    presentation["studio"]["high_samples"] = 48
    for key, value in presentation.items():
        recipe[key] = copy.deepcopy(value)
    part["three_d_model_details"] = recipe
    part["oobb_type"] = "bearing_open"
    part["oobb_details"] = {}
    part["oobb_details"]["oobb_type"] = "bearing_open"
    part["oobb_details"]["run_scad"] = True
    part["oobb_details"]["run_solidcraft"] = False
    part["oobb_details"]["angular_segments"] = 128
    part["oobb_details"]["components"] = copy.deepcopy(components)

    # Stage 5: all drawing inputs, label content and visual settings.
    drawing = {}
    drawing["svg_name"] = "bearing_dimension"
    drawing["title"] = part["size"] + " / OPEN BEARING"
    drawing["family"] = part["family"].replace("_", " ").upper()
    drawing["dimensions_mm"] = copy.deepcopy(dimensions)
    drawing["sheet_width_mm"] = 297
    drawing["sheet_height_mm"] = 210
    drawing["ink"] = "#183336"
    drawing["accent"] = "#147d83"
    drawing["muted"] = "#61767a"
    drawing["paper"] = "#ffffff"
    drawing["race_face_fill"] = "#edf3f3"
    drawing["inner_race_face_outside_mm"] = 2 * parameters["inner_shoulder"]
    drawing["outer_race_face_inside_mm"] = 2 * parameters["outer_shoulder"]
    drawing["line_width_mm"] = 0.45
    drawing["font_family"] = "Helvetica"
    drawing["dimension_font_mm"] = 4
    drawing["title_font_mm"] = 9
    drawing["front_centre_mm"] = [79, 103]
    drawing["side_centre_mm"] = [211, 103]
    drawing["max_view_width_mm"] = 78
    drawing["max_side_width_mm"] = 55
    drawing["dimension_offset_mm"] = 12
    drawing["arrow_size_mm"] = 2
    drawing["note"] = "Nominal dimensions in mm. Illustration only; no tolerances or fit allowances."
    drawing["authority"] = part["dimension_authority"].replace("_", " ")
    drawing["internal_note"] = "Open presentation; internal races and balls are illustrative. Retainers omitted."
    drawing["layout"] = {}
    drawing["layout"]["left_margin_mm"] = 14
    drawing["layout"]["right_margin_mm"] = 283
    drawing["layout"]["title_y_mm"] = 22
    drawing["layout"]["family_y_mm"] = 33
    drawing["layout"]["family_font_mm"] = 3.5
    drawing["layout"]["brand"] = "OOMP / BEARINGS"
    drawing["layout"]["brand_font_mm"] = 3.5
    drawing["layout"]["header_rule_y_mm"] = 40
    drawing["layout"]["view_caption_y_mm"] = 173
    drawing["layout"]["view_caption_font_mm"] = 3
    drawing["layout"]["front_caption"] = "FRONT VIEW"
    drawing["layout"]["side_caption"] = "SIDE VIEW"
    drawing["layout"]["footer_rule_y_mm"] = 180
    drawing["layout"]["note_y_mm"] = 187
    drawing["layout"]["internal_note_y_mm"] = 194
    drawing["layout"]["note_font_mm"] = 3.2
    drawing["layout"]["source_y_mm"] = 202
    drawing["layout"]["source_font_mm"] = 3
    drawing["layout"]["source_prefix"] = "SOURCE: "
    drawing["layout"]["scale_prefix"] = "A4 / scale"
    drawing["dimension_style"] = {}
    drawing["dimension_style"]["line_width_mm"] = 0.25
    drawing["dimension_style"]["arrow_half_width_ratio"] = 0.3
    drawing["dimension_style"]["text_gap_mm"] = 2
    drawing["dimension_style"]["extension_mm"] = 2
    drawing["dimension_style"]["width_extension_mm"] = 3
    drawing["dimension_style"]["centre_extension_mm"] = 5
    drawing["dimension_style"]["dash_pattern_mm"] = [2, 1]
    drawing["dimension_style"]["flange_leader_offset_mm"] = [-13, 11]
    drawing["dimension_style"]["flange_text_offset_mm"] = [-13, 16]
    drawing["dimension_style"]["flange_font_mm"] = 3.5
    drawing["outline"] = {}
    drawing["outline"]["ink"] = "black"
    drawing["outline"]["line_width_mm"] = 0.1
    part["svg_details"] = drawing
    part["label_details"] = {}
    part["label_details"]["size"] = part["size"]
    part["label_details"]["dimensions"] = f"{bore:g} x {outside:g} x {width:g} mm"
    part["label_details"]["formats_mm"] = [[76.2, 50.8], [38.1, 25.4]]
    part["label_details"]["ink"] = drawing["ink"]
    part["label_details"]["accent"] = drawing["accent"]
    part["label_details"]["paper"] = drawing["paper"]
    part["label_details"]["font_family"] = drawing["font_family"]
    part["label_details"]["view_box_mm"] = [0, 0, 76.2, 50.8]
    part["label_details"]["file_stems"] = ["label_bearing_3x2", "label_bearing_1_5x1"]
    part["label_details"]["brand"] = "OOMP / BEARING"
    part["label_details"]["brand_position_mm"] = [5, 10]
    part["label_details"]["brand_font_mm"] = 3
    part["label_details"]["size_position_mm"] = [5, 29]
    part["label_details"]["size_font_mm"] = 14
    part["label_details"]["dimensions_position_mm"] = [5, 42]
    part["label_details"]["dimensions_font_mm"] = 4

    # Stage 6: human-facing text is populated alongside the assets it describes.
    part["readme_details"] = {}
    part["readme_details"]["title"] = f"{part['size']} bearing - {bore:g} x {outside:g} x {width:g} mm"
    part["readme_details"]["description"] = f"{part['family'].replace('_', ' ').capitalize()} bearing: {bore:g} mm bore, {outside:g} mm outside diameter and {width:g} mm width."
    return part
