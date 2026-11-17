"""A4 dimension sheets and labels from svg_details saved during population."""
from html import escape
from pathlib import Path
import math
import xml.etree.ElementTree as ET
from bearing_io import records, write_text


def line(**kwargs):
    a, b = kwargs["a"], kwargs["b"]
    dash = ' stroke-dasharray="' + ' '.join(str(value) for value in kwargs["dash_pattern_mm"]) + '"' if kwargs.get("dashed") else ""
    return f'<line x1="{a[0]:.4f}" y1="{a[1]:.4f}" x2="{b[0]:.4f}" y2="{b[1]:.4f}"{dash}/>'


def text(**kwargs):
    return f'<text x="{kwargs["x"]:.4f}" y="{kwargs["y"]:.4f}" text-anchor="{kwargs.get("anchor", "middle")}" font-size="{kwargs["size"]}" fill="{kwargs["colour"]}" stroke="none">{escape(str(kwargs["value"]))}</text>'


def dimension(**kwargs):
    a, b = kwargs["a"], kwargs["b"]
    settings = kwargs["settings"]
    style = settings["dimension_style"]
    colour = settings["accent"]
    size = settings["arrow_size_mm"]
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    pieces = [f'<g stroke="{colour}" stroke-width="{style["line_width_mm"]}">', line(a=a, b=b)]
    arrow_half_width = size * style["arrow_half_width_ratio"]
    for origin, sign in [(a, 1), (b, -1)]:
        x, y = origin
        points = [(x, y), (x + sign * size * ux - arrow_half_width * uy, y + sign * size * uy + arrow_half_width * ux), (x + sign * size * ux + arrow_half_width * uy, y + sign * size * uy - arrow_half_width * ux)]
        pieces.append('<polygon fill="' + colour + '" points="' + ' '.join(f'{x:.4f},{y:.4f}' for x, y in points) + '"/>')
    tx = kwargs.get("text_x", (a[0] + b[0]) / 2)
    ty = kwargs.get("text_y", (a[1] + b[1]) / 2 - style["text_gap_mm"])
    pieces.append(text(x=tx, y=ty, value=kwargs["label"], size=settings["dimension_font_mm"], colour=colour, anchor=kwargs.get("anchor", "middle")))
    pieces.append('</g>')
    return ''.join(pieces)


def drawing_svg(**kwargs):
    s = kwargs["settings"]
    layout = s["layout"]
    style = s["dimension_style"]
    d = s["dimensions_mm"]
    maximum = d.get("flange_diameter", d["outside"])
    scale = min(s["max_view_width_mm"] / maximum, s["max_side_width_mm"] / d["width"])
    radius, bore = d["outside"] * scale / 2, d["bore"] * scale / 2
    flange = maximum * scale / 2
    half_width = d["width"] * scale / 2
    cx, cy = s["front_centre_mm"]
    sx, sy = s["side_centre_mm"]
    pieces = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{s["sheet_width_mm"]}mm" height="{s["sheet_height_mm"]}mm" viewBox="0 0 {s["sheet_width_mm"]} {s["sheet_height_mm"]}">',
              '<title>' + escape(s["title"]) + '</title>',
              f'<rect width="{s["sheet_width_mm"]}" height="{s["sheet_height_mm"]}" fill="{s["paper"]}"/>',
              f'<g font-family="{s["font_family"]}" stroke="{s["ink"]}" stroke-width="{s["line_width_mm"]}" fill="none">']
    pieces.append(text(x=layout["left_margin_mm"], y=layout["title_y_mm"], value=s["title"], size=s["title_font_mm"], colour=s["ink"], anchor="start"))
    pieces.append(text(x=layout["left_margin_mm"], y=layout["family_y_mm"], value=s["family"], size=layout["family_font_mm"], colour=s["muted"], anchor="start"))
    pieces.append(text(x=layout["right_margin_mm"], y=layout["title_y_mm"], value=layout["brand"], size=layout["brand_font_mm"], colour=s["accent"], anchor="end"))
    pieces.append(line(a=[layout["left_margin_mm"], layout["header_rule_y_mm"]], b=[layout["right_margin_mm"], layout["header_rule_y_mm"]]))
    face_circles = [
        (radius, s["race_face_fill"]),
        (s["outer_race_face_inside_mm"] * scale / 2, s["paper"]),
        (s["inner_race_face_outside_mm"] * scale / 2, s["race_face_fill"]),
        (bore, s["paper"]),
    ]
    for value, fill in face_circles:
        pieces.append(f'<circle cx="{cx}" cy="{cy}" r="{value:.4f}" fill="{fill}"/>')
    if "flange_diameter" in d:
        pieces.append(f'<circle cx="{cx}" cy="{cy}" r="{flange:.4f}"/>')
    extension = style["centre_extension_mm"]
    pieces.append(line(a=[cx - flange - extension, cy], b=[cx + flange + extension, cy], dashed=True, dash_pattern_mm=style["dash_pattern_mm"]))
    pieces.append(line(a=[cx, cy - flange - extension], b=[cx, cy + flange + extension], dashed=True, dash_pattern_mm=style["dash_pattern_mm"]))
    pieces.append(f'<rect x="{sx - half_width:.4f}" y="{sy - radius:.4f}" width="{half_width * 2:.4f}" height="{radius * 2:.4f}"/>')
    if "flange_thickness" in d:
        t = d["flange_thickness"] * scale
        pieces.append(f'<rect x="{sx - half_width:.4f}" y="{sy - flange:.4f}" width="{t:.4f}" height="{flange * 2:.4f}"/>')
    for value in [-bore, bore]:
        pieces.append(line(a=[sx - half_width, sy + value], b=[sx + half_width, sy + value], dashed=True, dash_pattern_mm=style["dash_pattern_mm"]))
    # Outside diameter and bore of the front view.
    y = cy - flange - s["dimension_offset_mm"]
    for x in [cx - radius, cx + radius]:
        pieces.append(line(a=[x, cy], b=[x, y - style["extension_mm"]]))
    pieces.append(dimension(a=[cx - radius, y], b=[cx + radius, y], label=f'OD {d["outside"]:g}', settings=s))
    pieces.append(dimension(a=[cx - bore, cy], b=[cx + bore, cy], label=f'ID {d["bore"]:g}', settings=s))
    # Overall width measured on the side view.
    y = sy + flange + s["dimension_offset_mm"]
    for x in [sx - half_width, sx + half_width]:
        pieces.append(line(a=[x, sy + flange], b=[x, y + style["width_extension_mm"]]))
    pieces.append(dimension(a=[sx - half_width, y], b=[sx + half_width, y], label=f'B {d["width"]:g}', settings=s))
    if "flange_diameter" in d:
        for x in [cx - flange, cx + flange]:
            pieces.append(line(a=[x, cy], b=[x, y + style["extension_mm"]]))
        pieces.append(dimension(a=[cx - flange, y], b=[cx + flange, y], label=f'Flange OD {d["flange_diameter"]:g}', settings=s))
        # Flange shoulder shown with a leader; avoids crowded arrows on thin flanges.
        leader_x, leader_y = style["flange_leader_offset_mm"]
        text_x, text_y = style["flange_text_offset_mm"]
        pieces.append(line(a=[sx - half_width + t / 2, sy + flange], b=[sx - half_width + leader_x, y + leader_y]))
        pieces.append(text(x=sx - half_width + text_x, y=y + text_y, value=f'Flange B {d["flange_thickness"]:g}', size=style["flange_font_mm"], colour=s["accent"]))
    pieces.append(text(x=cx, y=layout["view_caption_y_mm"], value=layout["front_caption"], size=layout["view_caption_font_mm"], colour=s["muted"]))
    pieces.append(text(x=sx, y=layout["view_caption_y_mm"], value=layout["side_caption"], size=layout["view_caption_font_mm"], colour=s["muted"]))
    pieces.append(line(a=[layout["left_margin_mm"], layout["footer_rule_y_mm"]], b=[layout["right_margin_mm"], layout["footer_rule_y_mm"]]))
    pieces.append(text(x=layout["left_margin_mm"], y=layout["note_y_mm"], value=s["note"], size=layout["note_font_mm"], colour=s["ink"], anchor="start"))
    pieces.append(text(x=layout["left_margin_mm"], y=layout["internal_note_y_mm"], value=s["internal_note"], size=layout["note_font_mm"], colour=s["muted"], anchor="start"))
    pieces.append(text(x=layout["left_margin_mm"], y=layout["source_y_mm"], value=layout["source_prefix"] + s["authority"], size=layout["source_font_mm"], colour=s["muted"], anchor="start"))
    pieces.append(text(x=layout["right_margin_mm"], y=layout["source_y_mm"], value=f'{layout["scale_prefix"]} {scale:.3f}:1 / mm', size=layout["source_font_mm"], colour=s["muted"], anchor="end"))
    pieces.append('</g></svg>')
    return '\n'.join(pieces)


def export_pdf(**kwargs):
    from svglib.svglib import svg2rlg
    from reportlab.pdfgen import canvas
    from reportlab.graphics import renderPDF
    drawing = svg2rlg(str(kwargs["svg"]))
    pdf = canvas.Canvas(str(kwargs["pdf"]), pagesize=(drawing.width, drawing.height), invariant=1)
    pdf.setTitle(kwargs["title"])
    renderPDF.draw(drawing, pdf, 0, 0)
    pdf.showPage()
    pdf.save()


def generate(**kwargs):
    folder = Path(kwargs["folder"])
    part = kwargs["part"]
    svg = folder / "working_dimension.svg"
    write_text(path=svg, text=drawing_svg(settings=part["svg_details"]))
    export_pdf(svg=svg, pdf=folder / "working_dimension_a4.pdf", title=part["readme_details"]["title"])
    d = part["dimensions_mm"]
    outline_style = part["svg_details"]["outline"]
    diameter = d.get("flange_diameter", d["outside"])
    outline = f'<svg xmlns="http://www.w3.org/2000/svg" width="{diameter}mm" height="{diameter}mm" viewBox="{-diameter/2} {-diameter/2} {diameter} {diameter}"><g fill="none" stroke="{outline_style["ink"]}" stroke-width="{outline_style["line_width_mm"]}"><circle r="{d["outside"]/2}"/><circle r="{d["bore"]/2}"/>'
    if "flange_diameter" in d:
        outline += f'<circle r="{diameter/2}"/>'
    write_text(path=folder / "working_svg.svg", text=outline + '</g></svg>\n')
    for index, (width, height) in enumerate(part["label_details"]["formats_mm"]):
        label = part["label_details"]
        view_box = ' '.join(str(value) for value in label["view_box_mm"])
        pieces = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}mm" height="{height}mm" viewBox="{view_box}">', f'<rect width="{label["view_box_mm"][2]}" height="{label["view_box_mm"][3]}" fill="{label["paper"]}"/>', f'<g font-family="{label["font_family"]}">']
        for field in ["brand", "size", "dimensions"]:
            x, y = label[field + "_position_mm"]
            colour = label["accent"] if field == "brand" else label["ink"]
            pieces.append(text(x=x, y=y, value=label[field], size=label[field + "_font_mm"], colour=colour, anchor="start"))
        pieces.append('</g></svg>')
        name = label["file_stems"][index]
        write_text(path=folder / (name + ".svg"), text='\n'.join(pieces))
        export_pdf(svg=folder / (name + ".svg"), pdf=folder / (name + ".pdf"), title=part["name"])


def main(**kwargs):
    count = 0
    for path, part in records(**kwargs):
        generate(folder=path.parent, part=part)
        count += 1
    print(f"Generated {count} dimension sheets and label pairs", flush=True)
    return count


if __name__ == "__main__":
    main()
