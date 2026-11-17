import math
import copy
import opsvg
import yaml
import os
import svg_help
import svg_styles


def main(**kwargs):
    make_svg(**kwargs)

def make_svg(**kwargs):
    typ = svg_help.get_typ(**kwargs)
    oomp_mode = "project"
    #oomp_mode = "oobb"
    filt = ""
    build_variables = svg_help.get_build_variables(typ, filter=filt)
    if True:
        kwargs["filter"] = build_variables["filter"]
        kwargs["save_type"] = build_variables["save_type"]
        kwargs["navigation"] = build_variables["navigation"]
        kwargs["overwrite"] = build_variables["overwrite"]
        kwargs["oomp_mode"] = oomp_mode
    parts = get_parts(kwargs, oomp_mode)

    kwargs["parts"] = parts

    svg_help.make_parts(**kwargs)

    if kwargs["navigation"]:
        oobb_style = False
        sort = svg_help.get_navigation_sort(oobb_style=oobb_style)
        svg_help.generate_navigation(sort=sort)


def get_parts(kwargs, oomp_mode):
    parts = []

    #load parts from parts/folder/working.yaml
    parts_directory = os.path.join(os.path.dirname(__file__), "parts")
    if not os.path.isdir(parts_directory):
        return parts

    for folder in os.listdir(parts_directory):
        folder_path = os.path.join(parts_directory, folder)
        if not os.path.isdir(folder_path):
            continue

        working_yaml_path = os.path.join(folder_path, "working.yaml")
        if not os.path.isfile(working_yaml_path):
            continue

        with open(working_yaml_path, "r", encoding="utf-8") as infile:
            loaded_part = yaml.safe_load(infile)

        if not isinstance(loaded_part, dict):
            continue

        svg_details_raw = loaded_part.get("svg_details")
        # Accept either a single dict or a list of dicts.
        if isinstance(svg_details_raw, list):
            # Use the first entry to derive kwargs / oobb_name; the full list
            # is kept intact in part["svg_details"] for make_svg_generic.
            svg_details = svg_details_raw[0] if svg_details_raw else {}
        elif isinstance(svg_details_raw, dict):
            svg_details = svg_details_raw
        else:
            continue  # no recognisable svg_details — skip

        part = loaded_part

        part_kwargs = copy.deepcopy(kwargs)
        part_kwargs.update(copy.deepcopy(loaded_part.get("kwargs", {})))
        _SD_META = {"svg_name", "filename_extra", "width", "height", "depth", "styles",
                    "extra", "radius_name"}
        svg_details_safe = {k: v for k, v in svg_details.items()
                            if k not in _SD_META or (k in ("width", "height", "depth") and isinstance(v, (int, float)))}
        part_kwargs.update(copy.deepcopy(svg_details_safe))

        # stylesheet name override from yaml: svg_details.stylesheet: "jazzy"
        if "stylesheet" in svg_details:
            part_kwargs["stylesheet"] = svg_details["stylesheet"]

        # per-part style overrides from yaml: svg_details.styles: {plate: {color: "#FF0000"}}
        yaml_styles = svg_details.get("styles", {})
        if isinstance(yaml_styles, dict) and yaml_styles:
            existing = part_kwargs.get("part_styles", {})
            part_kwargs["part_styles"] = svg_styles.merge(
                svg_styles.get_stylesheet(part_kwargs.get("stylesheet", "default")),
                {**existing, **yaml_styles}
            ) if not existing else {**existing, **yaml_styles}

        part["kwargs"] = part_kwargs
        part["oobb_name"] = part.get("oobb_name", svg_details.get("svg_name", "default"))

        if oomp_mode == "oobb":
            part["kwargs"]["oomp_size"] = part["oobb_name"]

        parts.append(part)

    return parts


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("depth", 3)
    rot = kwargs.get("rot", [0,0,0])
    pos = kwargs.get("pos", [0,0,0])
    extra = kwargs.get("extra", "")



    #add plate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["shape"] = f"oobb_plate"
        p3["depth"] = depth
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        opsvg.se(thing,**p3)

    #add holes
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["shape"] = f"oobb_holes"
        p3["depth"] = depth
        p3["radius_name"] = "m6"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        opsvg.se(thing,**p3)

    #add text
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["shape"] = f"text"
        p3["text"] = "Base Plate"
        p3["size"] = 10.0
        p3["font"] = "sans-serif"
        p3["halign"] = "left"
        p3["valign"] = "center"
        p3["color"] = "#000000"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        opsvg.se(thing,**p3)

    if prepare_print:
        svg_help.prepare_base_for_print(thing, pos, **kwargs)


def get_fill_in_the_blanks(thing, **kwargs):
    svg_help.get_fill_in_the_blanks(thing, **kwargs)


def get_a4_sheet(thing, **kwargs):
    svg_help.get_a4_sheet(thing, **kwargs)


def get_label_76x50(thing, **kwargs):
    svg_help.get_label_76x50(thing, **kwargs)


def _default_label_boxes():
    """Default 3 × 4 grid matching the Project Bolt tin insert photo.

    Top row is 0.5 units tall (narrow label strip);
    the three lower rows are each 1.0 units tall.
    Total: 3 wide × 3.5 high = 12 boxes.
    """
    boxes = []
    n = 1
    layout = [
        (0.0, 0.5),   # top narrow row
        (0.5, 1.0),
        (1.5, 1.0),
        (2.5, 1.0),
    ]
    for (row_y, row_h) in layout:
        for col in range(3):
            boxes.append({
                "x": float(col),
                "y": row_y,
                "w": 1.0,
                "h": row_h,
                "name": f"box_{n}",
            })
            n += 1
    return boxes


def get_internal_label_sheet(thing, **kwargs):
    """Proportional grid label sheet for tin inserts.

    No dark background — boxes sit directly on the card, separated by the
    card's own fill showing through the gap.  Corner radii are computed per
    corner so junctions and card edges look geometrically correct:

      r_inner  = gap_mm / 2   — inner corners: arc exactly fills the gap void
      r_outer  = card_r - card_margin_mm  — outer corners: parallel to card edge

    Parameters
    ----------
    unit_mm        : float  — physical size of one grid unit in mm   (default 42.0)
    grid_w         : float  — grid width in units                    (default 3.0)
    grid_h         : float  — grid height in units                   (default 3.5)
    card_margin_mm : float  — card fill visible around the grid      (default 2.0)
                              unit_mm=42, grid_w=3, margin=2 → card_w=130 mm
    card_r         : float  — card corner radius in mm               (default 8.0)
    gap_frac       : float  — gap between boxes as fraction of unit_mm (default 0.07)
    boxes          : list   — list of box dicts.  Each dict may contain:
                               x, y        — top-left position in units (required)
                               w, h        — size in units              (required)
                               name        — identifier string          (default "box_N")
                               text        — display text               (defaults to name)
                               style       — box fill style             (default "plate.cell")
                               text_style      — text style             (default "label")
                               text_size       — font size override mm  (default from style)
                               halign          — text alignment         (default "center";
                                                 auto "left" when lined)
                               valign          — vertical alignment     (default "center";
                                                 auto "top" when lined)
                               lined           — fill box with ruled    (default False)
                                                 lines for handwriting
                               line_spacing_mm — spacing between lines  (default 6.0 mm)
                               (any extra keys are preserved and ignored)
    stylesheet     : str    — stylesheet name                        (default "project_bolt")
    """
    prepare_print  = kwargs.get("prepare_print", False)
    pos            = kwargs.get("pos", [0, 0, 0])
    unit_mm        = float(kwargs.get("unit_mm",         42.0))
    grid_w         = float(kwargs.get("grid_w",           3.0))
    grid_h         = float(kwargs.get("grid_h",           3.5))
    card_margin_mm = float(kwargs.get("card_margin_mm",   2.0))
    card_r         = float(kwargs.get("card_r",           8.0))
    gap_frac       = float(kwargs.get("gap_frac",         0.07))
    boxes          = kwargs.get("boxes", _default_label_boxes())

    # ── Derived dimensions ────────────────────────────────────────────────────
    sheet_w  = grid_w * unit_mm                       # 126.0 mm
    sheet_h  = grid_h * unit_mm                       # 147.0 mm
    card_w   = sheet_w + 2 * card_margin_mm           # 130.0 mm
    card_h   = sheet_h + 2 * card_margin_mm           # 151.0 mm
    gap_mm   = gap_frac * unit_mm                     #   2.94 mm

    # Corner radius rules:
    #   inner: arc radius = gap/2 → arc exactly reaches the gap centreline,
    #          filling the void where four box corners meet
    #   outer: parallel to the card's own rounded corner
    r_inner  = gap_mm / 2
    r_outer  = max(card_r - card_margin_mm, 0.0)

    _EPS = 1e-3   # tolerance for edge-touching checks

    def _radii(bx, by, bw, bh):
        """Return (r_tl, r_tr, r_br, r_bl) for a box at grid position (bx,by)."""
        at_left   = bx              < _EPS
        at_top    = by              < _EPS
        at_right  = (bx + bw - grid_w) > -_EPS
        at_bottom = (by + bh - grid_h) > -_EPS
        tl = r_outer if (at_left  and at_top)    else r_inner
        tr = r_outer if (at_right and at_top)    else r_inner
        br = r_outer if (at_right and at_bottom) else r_inner
        bl = r_outer if (at_left  and at_bottom) else r_inner
        return tl, tr, br, bl

    # ── Stylesheet ────────────────────────────────────────────────────────────
    if "styles" not in thing or not thing.get("styles"):
        sheet_name = kwargs.get("stylesheet", "project_bolt")
        thing["styles"] = svg_styles.get_stylesheet(sheet_name)

    # ── Card fill (drawn first — border comes last) ───────────────────────────
    pos1 = copy.deepcopy(pos)
    opsvg.se(thing, shape="rounded_rectangle", style="plate",
             size=[card_w, card_h, 0], r=card_r, pos=pos1,
             stroke="none", stroke_width=0)

    # ── Boxes ─────────────────────────────────────────────────────────────────
    # Box centre in Y-up coords (origin = card centre = sheet centre):
    #   cx = -sheet_w/2 + unit_mm*(bx + bw/2)
    #   cy =  sheet_h/2 - unit_mm*(by + bh/2)
    # gap_mm cancels in the centre calculation; only affects w_mm / h_mm.
    for i, box in enumerate(boxes):
        bx         = float(box.get("x", 0))
        by         = float(box.get("y", 0))
        bw         = float(box.get("w", 1))
        bh         = float(box.get("h", 1))
        name       = box.get("name",       f"box_{i + 1}")
        text       = box.get("text",       name)
        box_style  = box.get("style",      "plate.cell")
        txt_style  = box.get("text_style", "label")
        txt_size   = box.get("text_size",  None)
        lined      = bool(box.get("lined", False))
        line_spc   = float(box.get("line_spacing_mm", 6.0))

        # lined boxes default to top-left anchored text; explicit values win
        halign = box.get("halign", "left"   if lined else "center")
        valign = box.get("valign", "top"    if lined else "center")

        w_mm = bw * unit_mm - gap_mm
        h_mm = bh * unit_mm - gap_mm
        cx   = -sheet_w / 2 + unit_mm * (bx + bw / 2)
        cy   =  sheet_h / 2 - unit_mm * (by + bh / 2)

        tl, tr, br, bl = _radii(bx, by, bw, bh)

        pos1    = copy.deepcopy(pos)
        pos1[0] += cx
        pos1[1] += cy

        # 1. Box fill
        opsvg.se(thing, shape="rrect_corners", style=box_style,
                 size=[w_mm, h_mm, 0],
                 r_tl=tl, r_tr=tr, r_br=br, r_bl=bl,
                 pos=pos1)

        # 2. Ruled lines (drawn before text so text sits on top)
        if lined:
            pad_x      = gap_mm * 1.5          # horizontal inset
            pad_y      = gap_mm                # top / bottom inset
            rule_w     = w_mm - 2 * pad_x
            rule_thick = 0.35
            y_from_top = pad_y + line_spc * 0.65   # first line
            while y_from_top + rule_thick / 2 < h_mm - pad_y:
                # Y-up offset from box centre: positive = up
                line_dy = h_mm / 2 - y_from_top
                lpos    = copy.deepcopy(pos)
                lpos[0] += cx
                lpos[1] += cy + line_dy
                opsvg.se(thing, shape="rect", style="rule",
                         size=[rule_w, rule_thick, 0], pos=lpos)
                y_from_top += line_spc

        # 3. Text — anchor point offset so halign/valign align to box edge
        padding = gap_mm
        off_x = {"left":  -(w_mm / 2 - padding),
                 "right":  (w_mm / 2 - padding),
                 "center": 0.0}.get(halign, 0.0)
        off_y = {"top":    (h_mm / 2 - padding),    # Y-up: positive = up
                 "bottom": -(h_mm / 2 - padding),
                 "center": 0.0}.get(valign, 0.0)

        txt_pos    = copy.deepcopy(pos)
        txt_pos[0] += cx + off_x
        txt_pos[1] += cy + off_y

        txt_kwargs = dict(halign=halign, valign=valign)
        if txt_size is not None:
            txt_kwargs["size"] = txt_size
        opsvg.se(thing, shape="text", style=txt_style,
                 text=text, pos=txt_pos, **txt_kwargs)

    # ── Card border (drawn last — on top of everything) ───────────────────────
    pos1 = copy.deepcopy(pos)
    opsvg.se(thing, shape="rounded_rectangle", style="plate.outline",
             size=[card_w, card_h, 0], r=card_r, pos=pos1)

    if prepare_print:
        svg_help.prepare_base_for_print(thing, pos, **kwargs)


def get_nut(thing, **kwargs):
    import svg_styles

    prepare_print = kwargs.get("prepare_print", False)
    pos = kwargs.get("pos", [0, 0, 0])

    if not kwargs.get("stylesheet"):
        thing["styles"] = svg_styles.get_stylesheet("project_bolt")

    s_mm  = float(thing.get("spec_iso_s_max_mm",  kwargs.get("svg_s_max_mm",  10.0)))
    dw_mm = float(thing.get("spec_iso_dw_min_mm", kwargs.get("svg_dw_min_mm",  8.9)))
    nom   = thing.get("spec_iso_nominal_diameter", kwargs.get("svg_nominal_diameter", "M?"))
    try:
        d_hole = float(str(nom).lstrip("Mm"))
    except (ValueError, AttributeError):
        d_hole = s_mm * 0.6

    R = (s_mm / 2) / math.cos(math.radians(30))
    hex_pts = [
        [R * math.cos(math.radians(30 + i * 60)),
         R * math.sin(math.radians(30 + i * 60))]
        for i in range(6)
    ]

    opsvg.se(thing, shape="polygon", style="outline",
             points=hex_pts, pos=copy.deepcopy(pos))
    opsvg.se(thing, shape="circle", style="hole.cut",
             r=d_hole / 2, pos=copy.deepcopy(pos))


def get_bolt(thing, **kwargs):
    import svg_styles
    if not kwargs.get("stylesheet"):
        thing["styles"] = svg_styles.get_stylesheet("project_bolt")
    s_mm  = float(thing.get("spec_iso_s_max_mm",  kwargs.get("svg_s_max_mm",  10.0)))
    nom   = thing.get("spec_iso_nominal_diameter", kwargs.get("svg_nominal_diameter", "M?"))
    try:
        d_hole = float(str(nom).lstrip("Mm"))
    except (ValueError, AttributeError):
        d_hole = s_mm * 0.6
    R = (s_mm / 2) / math.cos(math.radians(30))
    hex_pts = [
        [R * math.cos(math.radians(30 + i * 60)),
         R * math.sin(math.radians(30 + i * 60))]
        for i in range(6)
    ]
    pos = kwargs.get("pos", [0, 0, 0])
    opsvg.se(thing, shape="polygon", style="outline",
             points=hex_pts, pos=copy.deepcopy(pos))
    opsvg.se(thing, shape="circle", style="hole.cut",
             r=d_hole / 2, pos=copy.deepcopy(pos))


def get_set_screw(thing, **kwargs):
    get_bolt(thing, **kwargs)


def get_oomp_mech_drawing_hardware(thing, **kwargs):
    import svg_template

    hardware_type    = kwargs.get("hardware_type", "nut")
    id_mm            = float(kwargs.get("id_mm",            6.0))
    af_mm            = float(kwargs.get("af_mm",           10.0))
    height_mm        = float(kwargs.get("height_mm",        5.0))
    head_height_mm   = float(kwargs.get("head_height_mm",  height_mm))
    length_mm        = float(kwargs.get("length_mm",       height_mm))
    thread_length_mm = float(kwargs.get("thread_length_mm", length_mm))

    if hardware_type == "nut":
        summary_cols = [
            (f"M{id_mm:.0f}",           "THREAD"),
            (f"{af_mm:.0f} mm",         "ACROSS FLATS"),
            (f"{height_mm:.1f} mm",     "NUT HEIGHT"),
        ]
    elif hardware_type in ("bolt", "set_screw"):
        summary_cols = [
            (f"M{id_mm:.0f}",               "THREAD"),
            (f"{af_mm:.0f} mm",             "ACROSS FLATS"),
            (f"{head_height_mm:.1f} mm",    "HEAD HEIGHT"),
            (f"{length_mm:.0f} mm",         "SHANK LENGTH"),
            (f"{thread_length_mm:.0f} mm",  "THREAD LENGTH"),
        ]
    elif hardware_type == "bearing":
        od_mm    = float(kwargs.get("od_mm",    26.0))
        width_mm = float(kwargs.get("width_mm",  8.0))
        # Set af_mm so r_c_d = (od_mm/2)*view_scale = outer display radius
        kwargs["af_mm"]          = (od_mm / 2.0) * math.sqrt(3)
        kwargs["id_mm"]          = id_mm
        kwargs["length_mm"]      = width_mm
        kwargs["head_height_mm"] = 0.0
        kwargs["height_mm"]      = width_mm
        summary_cols = [
            (f"{id_mm:.0f} mm",    "INNER DIA"),
            (f"{od_mm:.0f} mm",    "OUTER DIA"),
            (f"{width_mm:.1f} mm", "WIDTH"),
        ]

        # Build the full mech drawing into thing, then save it as
        # working_mechanical_drawing.svg, and replace thing's components
        # with the 1:1 top view so make_svg_generic writes working_svg.svg.
        svg_template.mech_drawing_page(thing, draw_fn=draw_item,
                                       summary_cols=summary_cols, **kwargs)
        folder = thing.get("directory", "")
        if folder:
            import svg_a4
            mech_path = os.path.join(folder, "working_mechanical_drawing.svg")
            overwrite  = kwargs.get("overwrite", True)
            opsvg.opsvg_make_object(mech_path, thing["svg_components"],
                                    overwrite=overwrite)
            svg_a4.make_pdf(mech_path, folder)

        # Replace components with 1:1 front + side view
        thing["svg_components"] = []
        _bearing_top_view_1to1(thing, od_mm=od_mm, id_mm=id_mm, width_mm=width_mm)
        return
    else:
        summary_cols = []

    svg_template.mech_drawing_page(thing, draw_fn=draw_item,
                                   summary_cols=summary_cols, **kwargs)


def draw_item(thing, **kwargs):
    hardware_type = kwargs.get("hardware_type", "nut")
    if hardware_type == "bolt":
        draw_bolt(thing, **kwargs)
    elif hardware_type == "set_screw":
        draw_set_screw(thing, **kwargs)
    elif hardware_type == "bearing":
        draw_bearing(thing, **kwargs)
    else:
        draw_nut(thing, **kwargs)


def draw_nut(thing, **kwargs):
    """Front and side views + dimension annotations for a hex nut."""
    front_cx     = kwargs["front_cx"]
    side_cx      = kwargs["side_cx"]
    view_cy      = kwargs["view_cy"]
    r_c_d        = kwargs["r_c_d"]
    af_d         = kwargs["af_d"]
    bore_r_d     = kwargs["bore_r_d"]
    height_d     = kwargs["height_d"]
    upper_vert_y = kwargs["upper_vert_y"]
    af_mm        = float(kwargs.get("af_mm",     10.0))
    id_mm        = float(kwargs.get("id_mm",      6.0))
    height_mm    = float(kwargs.get("height_mm",  5.0))

    _plate_c  = kwargs["_plate_c"]
    _plate_sk = kwargs["_plate_sk"]
    _plate_sw = kwargs["_plate_sw"]
    _cut_c    = kwargs["_cut_c"]
    _cut_sk   = kwargs["_cut_sk"]
    _cut_sw   = kwargs["_cut_sw"]
    _light_sk = kwargs["_light_sk"]
    _light_sw = kwargs["_light_sw"]
    _abs_pos  = kwargs["abs_pos_fn"]
    _dim      = kwargs["dim_fn"]
    _hex_pts  = kwargs["hex_pts_fn"]

    e_d = 2 * r_c_d

    fpos = _abs_pos(front_cx, view_cy)
    opsvg.se(thing, shape="polygon", points=_hex_pts(r_c_d),
             color=_plate_c, stroke=_plate_sk, stroke_width=_plate_sw, pos=fpos)
    opsvg.se(thing, shape="circle", r=bore_r_d,
             color=_cut_c, stroke=_cut_sk, stroke_width=_cut_sw, pos=fpos)

    spos = _abs_pos(side_cx, view_cy)
    opsvg.se(thing, shape="rect", size=[e_d, height_d, 0],
             color=_plate_c, stroke=_plate_sk, stroke_width=_plate_sw, pos=spos)
    opsvg.se(thing, shape="rect", size=[bore_r_d * 2, height_d, 0],
             color=_cut_c, stroke=_cut_sk, stroke_width=_cut_sw, pos=spos)
    for x_off in (-af_d / 2, af_d / 2):
        opsvg.se(thing, shape="line",
                 p1=[x_off, -height_d / 2], p2=[x_off, height_d / 2],
                 color=_light_sk, stroke_width=_light_sw, pos=spos)

    _dim(front_cx, view_cy,
         p1=[-af_d / 2, upper_vert_y], p2=[af_d / 2, upper_vert_y],
         offset=upper_vert_y + 8, text=f"ACROSS FLATS  {af_mm:.0f} mm",
         direction="horizontal")
    _dim(front_cx, view_cy,
         p1=[-bore_r_d, 0], p2=[bore_r_d, 0],
         offset=-(r_c_d + 8), text=f"THREAD BORE  Ø{id_mm:.0f} mm",
         direction="horizontal")
    _dim(side_cx, view_cy,
         p1=[-af_d / 2, height_d / 2], p2=[af_d / 2, height_d / 2],
         offset=8, text=f"ACROSS FLATS  {af_mm:.0f} mm",
         direction="horizontal")
    _dim(side_cx, view_cy,
         p1=[af_d / 2, -height_d / 2], p2=[af_d / 2, height_d / 2],
         offset=8, text=f"NUT HEIGHT  {height_mm:.1f} mm",
         direction="vertical")


def draw_bolt(thing, **kwargs):
    """Front and side views + dimension annotations for a hex bolt."""
    front_cx         = kwargs["front_cx"]
    side_cx          = kwargs["side_cx"]
    view_cy          = kwargs["view_cy"]
    r_c_d            = kwargs["r_c_d"]
    af_d             = kwargs["af_d"]
    bore_r_d         = kwargs["bore_r_d"]
    upper_vert_y     = kwargs["upper_vert_y"]
    view_scale       = kwargs["view_scale"]
    ann_ts           = kwargs["ann_ts"]
    af_mm            = float(kwargs.get("af_mm",             10.0))
    id_mm            = float(kwargs.get("id_mm",              6.0))
    head_height_mm   = float(kwargs.get("head_height_mm",     4.0))
    length_mm        = float(kwargs.get("length_mm",         16.0))
    thread_length_mm = float(kwargs.get("thread_length_mm", length_mm))

    _plate_c  = kwargs["_plate_c"]
    _plate_sk = kwargs["_plate_sk"]
    _plate_sw = kwargs["_plate_sw"]
    _cut_c    = kwargs["_cut_c"]
    _cut_sk   = kwargs["_cut_sk"]
    _cut_sw   = kwargs["_cut_sw"]
    _dim_sk   = kwargs["_dim_sk"]
    _dim_sw   = kwargs["_dim_sw"]
    _light_sk = kwargs["_light_sk"]
    _light_sw = kwargs["_light_sw"]
    _abs_pos  = kwargs["abs_pos_fn"]
    _text_at  = kwargs["text_at_fn"]
    _dim      = kwargs["dim_fn"]
    _hex_pts  = kwargs["hex_pts_fn"]

    _st = thing.get("styles", {})
    _plate_light = _st.get("plate.light", {}).get("color", "#F0F0F0")

    e_d = 2 * r_c_d

    head_d    = head_height_mm * view_scale
    shank_d   = length_mm * view_scale
    total_d   = head_d + shank_d
    top_y     = view_cy + total_d / 2
    bear_y    = top_y - head_d
    bot_y     = top_y - total_d
    thread_d  = thread_length_mm * view_scale
    grip_d    = shank_d - thread_d
    grip_cy   = bear_y - grip_d / 2
    thread_cy = bot_y + thread_d / 2
    origin    = _abs_pos(side_cx, 0)

    fpos = _abs_pos(front_cx, view_cy)
    opsvg.se(thing, shape="polygon", points=_hex_pts(r_c_d),
             color=_plate_c, stroke=_plate_sk, stroke_width=_plate_sw, pos=fpos)
    opsvg.se(thing, shape="circle", r=bore_r_d,
             color=_cut_c, stroke=_cut_sk, stroke_width=_cut_sw, pos=fpos)

    opsvg.se(thing, shape="rect", size=[e_d, head_d, 0],
             color=_plate_c, stroke=_plate_sk, stroke_width=_plate_sw,
             pos=_abs_pos(side_cx, (top_y + bear_y) / 2))
    for x_off in (-af_d / 2, af_d / 2):
        opsvg.se(thing, shape="line",
                 p1=[x_off, bear_y], p2=[x_off, top_y],
                 color=_light_sk, stroke_width=_light_sw, pos=origin)
    if grip_d > 0:
        opsvg.se(thing, shape="rect", size=[bore_r_d * 2, grip_d, 0],
                 color=_plate_c, stroke=_plate_sk, stroke_width=_plate_sw,
                 pos=_abs_pos(side_cx, grip_cy))
    opsvg.se(thing, shape="rect", size=[bore_r_d * 2, thread_d, 0],
             color=_plate_light, stroke=_plate_sk, stroke_width=_plate_sw,
             pos=_abs_pos(side_cx, thread_cy))

    _dim(front_cx, view_cy,
         p1=[-af_d / 2, upper_vert_y], p2=[af_d / 2, upper_vert_y],
         offset=upper_vert_y + 8, text=f"ACROSS FLATS  {af_mm:.0f} mm",
         direction="horizontal")
    _dim(front_cx, view_cy,
         p1=[-bore_r_d, 0], p2=[bore_r_d, 0],
         offset=-(r_c_d + 8), text=f"THREAD BORE  Ø{id_mm:.0f} mm",
         direction="horizontal")
    _dim(side_cx, 0,
         p1=[-af_d / 2, top_y], p2=[af_d / 2, top_y],
         offset=8, text=f"ACROSS FLATS  {af_mm:.0f} mm",
         direction="horizontal")

    _gap = 1.5;  _ovr = 1.5;  _tick = 1.5
    _bx  = side_cx - r_c_d - 8
    _dpos = _abs_pos(0, 0)
    for _ey in (bear_y, top_y):
        opsvg.se(thing, shape="line",
                 p1=[side_cx - r_c_d - _gap, _ey], p2=[_bx - _ovr, _ey],
                 color=_dim_sk, stroke_width=_dim_sw, pos=_dpos)
        opsvg.se(thing, shape="line",
                 p1=[_bx - _tick, _ey], p2=[_bx + _tick, _ey],
                 color=_dim_sk, stroke_width=_dim_sw, pos=_dpos)
    opsvg.se(thing, shape="line",
             p1=[_bx, bear_y], p2=[_bx, top_y],
             color=_dim_sk, stroke_width=_dim_sw, pos=_dpos)
    _text_at(_bx - _tick - 2, (top_y + bear_y) / 2,
             f"HEAD HEIGHT  {head_height_mm:.1f} mm",
             size=ann_ts, halign="right")

    _dim(side_cx, 0,
         p1=[r_c_d, bot_y], p2=[r_c_d, bear_y],
         offset=8, text=f"SHANK LENGTH  {length_mm:.0f} mm",
         direction="vertical")
    _dim(side_cx, 0,
         p1=[-bore_r_d, bot_y], p2=[-bore_r_d, bot_y + thread_d],
         offset=-(r_c_d - bore_r_d + 8), text=f"THREAD LENGTH  {thread_length_mm:.0f} mm",
         direction="vertical")


def draw_set_screw(thing, **kwargs):
    draw_bolt(thing, **kwargs)


def draw_bearing(thing, **kwargs):
    """Front and side views + dimension annotations for a ball bearing."""
    front_cx   = kwargs["front_cx"]
    side_cx    = kwargs["side_cx"]
    view_cy    = kwargs["view_cy"]
    r_c_d      = kwargs["r_c_d"]      # = (od_mm/2) * view_scale
    height_d   = kwargs["height_d"]   # = width_mm * view_scale
    view_scale = kwargs["view_scale"]
    ann_ts     = kwargs["ann_ts"]

    od_mm    = float(kwargs.get("od_mm",    26.0))
    id_mm    = float(kwargs.get("id_mm",    10.0))
    width_mm = float(kwargs.get("width_mm",  8.0))

    _plate_c  = kwargs["_plate_c"]
    _plate_sk = kwargs["_plate_sk"]
    _plate_sw = kwargs["_plate_sw"]
    _cut_c    = kwargs["_cut_c"]
    _cut_sk   = kwargs["_cut_sk"]
    _cut_sw   = kwargs["_cut_sw"]
    _light_sk = kwargs["_light_sk"]
    _light_sw = kwargs["_light_sw"]
    _abs_pos  = kwargs["abs_pos_fn"]
    _dim      = kwargs["dim_fn"]

    od_r = r_c_d                        # outer radius in display units
    id_r = (id_mm / 2.0) * view_scale   # inner (bore) radius in display units

    # ── Front view: filled annulus ────────────────────────────────────────────
    fpos = _abs_pos(front_cx, view_cy)
    opsvg.se(thing, shape="circle", r=od_r,
             color=_plate_c, stroke=_plate_sk, stroke_width=_plate_sw, pos=fpos)
    opsvg.se(thing, shape="circle", r=id_r,
             color=_cut_c, stroke=_cut_sk, stroke_width=_cut_sw, pos=fpos)

    # Centre lines
    ext = od_r + 5
    opsvg.se(thing, shape="line",
             p1=[-ext, 0], p2=[ext, 0],
             color=_light_sk, stroke_width=_light_sw, pos=fpos)
    opsvg.se(thing, shape="line",
             p1=[0, -ext], p2=[0, ext],
             color=_light_sk, stroke_width=_light_sw, pos=fpos)

    # ── Side view: outer rect + bore rect ────────────────────────────────────
    spos = _abs_pos(side_cx, view_cy)
    opsvg.se(thing, shape="rect", size=[od_r * 2, height_d, 0],
             color=_plate_c, stroke=_plate_sk, stroke_width=_plate_sw, pos=spos)
    opsvg.se(thing, shape="rect", size=[id_r * 2, height_d, 0],
             color=_cut_c, stroke=_cut_sk, stroke_width=_cut_sw, pos=spos)

    # Light bore-edge indicator lines
    for x_off in (-id_r, id_r):
        opsvg.se(thing, shape="line",
                 p1=[x_off, -height_d / 2], p2=[x_off, height_d / 2],
                 color=_light_sk, stroke_width=_light_sw, pos=spos)

    # ── Dimension annotations ─────────────────────────────────────────────────
    _dim(front_cx, view_cy,
         p1=[-od_r, 0], p2=[od_r, 0],
         offset=od_r + 8,
         text=f"OUTER DIA  Ø{od_mm:.0f} mm",
         direction="horizontal")
    _dim(front_cx, view_cy,
         p1=[-id_r, 0], p2=[id_r, 0],
         offset=-(od_r + 8),
         text=f"INNER BORE  Ø{id_mm:.0f} mm",
         direction="horizontal")
    _dim(side_cx, view_cy,
         p1=[-od_r, height_d / 2], p2=[od_r, height_d / 2],
         offset=8,
         text=f"OUTER DIA  Ø{od_mm:.0f} mm",
         direction="horizontal")
    _dim(side_cx, view_cy,
         p1=[od_r, -height_d / 2], p2=[od_r, height_d / 2],
         offset=8,
         text=f"WIDTH  {width_mm:.1f} mm",
         direction="vertical")


def _bearing_top_view_1to1(thing, od_mm, id_mm, width_mm=8.0):
    """1:1 scale front + side view. Fills drawn first, outlines on top (transparent fill)."""
    _st = thing.get("styles") or svg_styles.get_stylesheet("project_bolt")
    if not thing.get("styles"):
        thing["styles"] = _st

    _plate_c  = _st.get("plate",         {}).get("color",        "#FAFAFA")
    _plate_sk = _st.get("plate.outline", {}).get("stroke",       "#1A1A1A")
    _plate_sw = _st.get("plate.outline", {}).get("stroke_width", 0.8)
    _cut_c    = _st.get("hole.cut",      {}).get("color",        "#FFFFFF")
    _cut_sk   = _st.get("hole.cut",      {}).get("stroke",       "#444444")
    _cut_sw   = _st.get("hole.cut",      {}).get("stroke_width", 0.3)
    _light_sk = _st.get("outline.light", {}).get("stroke",       "#AAAAAA")
    _light_sw = _st.get("outline.light", {}).get("stroke_width", 0.3)

    od_r    = od_mm / 2.0
    id_r    = id_mm / 2.0
    ext     = od_r + 3.0
    gap     = 6.0
    side_cx = ext + gap + width_mm / 2.0

    fpos = [0, 0, 0]
    spos = [side_cx, 0, 0]

    # ── 1. Fills (no stroke so outlines don't get buried) ────────────────────
    opsvg.se(thing, shape="circle", r=od_r,
             color=_plate_c, stroke="none", stroke_width=0, pos=fpos)
    opsvg.se(thing, shape="circle", r=id_r,
             color=_cut_c, stroke="none", stroke_width=0, pos=fpos)
    opsvg.se(thing, shape="rect", size=[width_mm, od_mm, 0],
             color=_plate_c, stroke="none", stroke_width=0, pos=spos)
    opsvg.se(thing, shape="rect", size=[width_mm, id_mm, 0],
             color=_cut_c, stroke="none", stroke_width=0, pos=spos)

    # ── 2. Light indicator lines ───────────────────────────────────────────────
    opsvg.se(thing, shape="line",
             p1=[-ext, 0], p2=[ext, 0],
             color=_light_sk, stroke_width=_light_sw, pos=fpos)
    opsvg.se(thing, shape="line",
             p1=[0, -ext], p2=[0, ext],
             color=_light_sk, stroke_width=_light_sw, pos=fpos)
    for y_off in (-id_r, id_r):
        opsvg.se(thing, shape="line",
                 p1=[-width_mm / 2, y_off], p2=[width_mm / 2, y_off],
                 color=_light_sk, stroke_width=_light_sw, pos=spos)

    # ── 3. Outlines last — transparent fill so nothing below is obscured ──────
    opsvg.se(thing, shape="circle", r=od_r,
             color="none", stroke=_plate_sk, stroke_width=_plate_sw, pos=fpos)
    opsvg.se(thing, shape="circle", r=id_r,
             color="none", stroke=_cut_sk, stroke_width=_cut_sw, pos=fpos)
    opsvg.se(thing, shape="rect", size=[width_mm, od_mm, 0],
             color="none", stroke=_plate_sk, stroke_width=_plate_sw, pos=spos)
    opsvg.se(thing, shape="rect", size=[width_mm, id_mm, 0],
             color="none", stroke=_cut_sk, stroke_width=_cut_sw, pos=spos)


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)
