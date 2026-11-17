"""Generate illustrated part pages and natural-order series navigation offline."""
from collections import defaultdict
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from bearing_io import ROOT, records, write_text

START = '<!-- bearing-catalogue:start -->'
END = '<!-- bearing-catalogue:end -->'


def managed(**kwargs):
    path = Path(kwargs["path"])
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    block = START + "\n" + kwargs["body"].rstrip() + "\n" + END
    if START in old or END in old:
        if old.count(START) != 1 or old.count(END) != 1 or old.index(START) > old.index(END):
            raise ValueError(f"Malformed documentation markers: {path}")
        content = old[:old.index(START)] + block + old[old.index(END) + len(END):]
    else:
        # Preserve specialist legacy notes at their original link location.
        content = block
        if old.strip():
            content += '\n\n<details>\n<summary>Previous catalogue notes</summary>\n\n' + old.rstrip() + '\n\n</details>'
    content = re.sub(r'\[([^\]]+)\]\([^\s)]+\.stl\)', r'\1 (STL export retired)', content, flags=re.I)
    write_text(path=path, text=content.rstrip() + "\n")


def natural(**kwargs):
    return [(0, int(s)) if s.isdigit() else (1, s.lower()) for s in re.split(r'(\d+)', str(kwargs["value"]))]


def safe(**kwargs):
    value = str(kwargs["value"])
    return value.replace('|', '&#124;').replace('<', '&lt;').replace('>', '&gt;').replace('[', '&#91;').replace(']', '&#93;').replace('\n', ' ')


def part_page(**kwargs):
    folder = kwargs["folder"]
    part = kwargs["part"]
    s = part["readme_details"]
    d = part["dimensions_mm"]
    lines = ['# ' + s["title"], '', '## Summary', '', s["description"], '']
    if (folder / 'three_d_model/render_product_low.png').exists():
        lines += ['| Product view | Isometric view |', '| --- | --- |', '| ![Open bearing product render](three_d_model/render_product_low.png) | ![Open bearing isometric render](three_d_model/render_low.png) |', '', 'Generated catalogue illustrations; the open internal geometry is illustrative.', '']
    lines += ['## Details', '', f'**OOMP ID:** `{part["oomp_id"]}`', '', '| Dimension | Nominal value |', '| --- | --- |']
    labels = {'bore': 'Bore / ID', 'outside': 'Outside diameter / OD', 'width': 'Width / B', 'flange_diameter': 'Flange outside diameter', 'flange_thickness': 'Flange thickness', 'contact_angle_deg': 'Catalogue contact angle'}
    for key, value in d.items():
        unit = 'degrees' if key == 'contact_angle_deg' else 'mm'
        lines.append(f'| {labels[key]} | {value:g} {unit} |')
    lines += ['', f'**Dimension evidence:** {part["dimension_authority"].replace("_", " ")} (review retained from {part["source_checked"]}).', '', part['model_note'], '']
    if 'contact_angle_deg' in d:
        authority = part['three_d_model_details']['parameters']['contact_angle_authority']
        lines += [f'Contact-angle authority: **{authority.replace("_", " ")}**. The mesh does not reconstruct the manufacturer contact surfaces.', '']
    if (folder / 'working_dimension.svg').exists():
        lines += ['![Dimensioned front and side views](working_dimension.svg)', '', '[Printable A4 dimension sheet](working_dimension_a4.pdf) · [1:1 outline](working_svg.svg)', '']
    lines += ['### Source evidence', '']
    for source in part['sources']:
        url = source if source.startswith('https://') else '../../' + source
        lines.append(f'- [{safe(value=source)}]({quote(url, safe="/:?=&._-")})')
    lines += ['', '[Retained research and corrected dimensions](../../source_file/solidcraft/) · [Editable declaration](../../working_oomp_declarations_bearing.py)', '', '## Parts', '', '[Canonical part folder](.) · [Metadata](working.yaml) · [Browse this series](../../navigation/' + quote(part['series']) + '/README.md)', '', '### Files', '']
    assets = {
        '3dpr.scad': 'Editable OpenSCAD geometry',
        'three_d_model/model_full.glb': 'Full model / GLB / metres, Y-up',
        'three_d_model/model_display.glb': 'Lightweight model / GLB / metres, Y-up',
        'three_d_model/studio.blend': 'Editable Blender studio',
        'three_d_model/render_product_high.png': 'Product render / 2048 px',
        'three_d_model/render_high.png': 'Isometric render / 2048 px',
        'three_d_model/parameters.json': 'Populated model and render recipe',
        'three_d_model/manifest.json': 'Mesh measurements and artifact hashes',
        'solidcraft/latest_success.json': 'Retained native CAD success manifest',
        'label_bearing_3x2.pdf': '76.2 x 50.8 mm label',
        'label_bearing_1_5x1.pdf': '38.1 x 25.4 mm label',
    }
    for filename, label in assets.items():
        if (folder / filename).exists():
            lines.append(f'- [{label}]({filename})')
    pointer = folder / 'solidcraft/latest_success.json'
    if pointer.exists():
        pointer_data = json.loads(pointer.read_text(encoding='utf-8'))
        native_manifest = (pointer.parent / pointer_data['manifest']).resolve()
        if native_manifest.is_relative_to(folder.resolve()) and native_manifest.is_file():
            native = json.loads(native_manifest.read_text(encoding='utf-8'))
            for filename in native.get('artifacts', {}):
                file = (native_manifest.parent / filename).resolve()
                if file.suffix == '.solidcraft' and file.is_relative_to(folder.resolve()) and file.is_file():
                    relative = file.relative_to(folder.resolve()).as_posix()
                    lines.append(f'- [Retained editable native bearing / SolidCraft]({quote(relative)})')
    if (folder / 'three_d_model/full').exists():
        lines += ['', '### Orthographic views', '', '| Quality | Isometric | Front | Back | Left | Right | Top | Bottom |', '| --- | --- | --- | --- | --- | --- | --- | --- |']
        for variant in ['full', 'display']:
            lines.append('| ' + variant.capitalize() + ' | ' + ' | '.join(f'[{view.title()}](three_d_model/{variant}/{view}.svg)' for view in ['isometric', 'front', 'back', 'left', 'right', 'top', 'bottom']) + ' |')
    lines += ['', '## Assembly', '', 'No installation procedure is established for this generic size record. Select the required closure, clearance, tolerance and load rating from the actual purchased bearing specification.', '', '<details>', '<summary>Complete OOMP metadata</summary>', '', '```yaml', yaml.dump(part, Dumper=getattr(yaml, "CSafeDumper", yaml.SafeDumper), sort_keys=False, allow_unicode=True).rstrip(), '```', '', '</details>']
    managed(path=folder / 'README.md', body='\n'.join(lines))


def main(**kwargs):
    root = Path(kwargs.get('root', ROOT))
    selected = list(records(**kwargs))
    for path, part in selected:
        part_page(folder=path.parent, part=part)
    # Navigation always includes the complete catalogue, even after a filtered build.
    groups = defaultdict(list)
    for path, part in records(root=root):
        groups[part['series']].append(part)
    lines = ['# Bearing catalogue', '', '[Catalogue overview](../README.md)', '', '| Series | Parts |', '| --- | --- |']
    for series in sorted(groups, key=lambda value: natural(value=value)):
        parts = sorted(groups[series], key=lambda part: natural(value=part['size']))
        lines.append(f'| [{series}]({quote(series)}/README.md) | {len(parts)} |')
        page = [f'# {series} series bearings', '', '[All series](../README.md) · [Catalogue overview](../../README.md)', '', '| Bearing | Bore (mm) | Outside (mm) | Width (mm) | Drawing | Model |', '| --- | --- | --- | --- | --- | --- |']
        for part in parts:
            d = part['dimensions_mm']
            relative = '../../parts/' + quote(part['oomp_id'])
            page.append(f'| [{part["size"]}]({relative}/README.md) | {d["bore"]:g} | {d["outside"]:g} | {d["width"]:g} | [PDF]({relative}/working_dimension_a4.pdf) | [GLB]({relative}/three_d_model/model_display.glb) |')
        write_text(path=root / 'navigation' / series / 'README.md', text='\n'.join(page) + '\n')
    write_text(path=root / 'navigation/README.md', text='\n'.join(lines) + '\n')
    config = json.loads((root / 'documentation.json').read_text(encoding='utf-8'))
    examples = [part for series in groups.values() for part in series if part['size'] in config['example_sizes']]
    summary = config['summary'].format(part_count=sum(len(parts) for parts in groups.values()))
    overview = ['# ' + config['title'], '', '## Summary', '', summary, '']
    overview += ['| ' + ' | '.join(f'[{p["size"]}](parts/{quote(p["oomp_id"])}/README.md)' for p in examples) + ' |', '| ' + ' | '.join('---' for _ in examples) + ' |', '| ' + ' | '.join(f'![{p["size"]} open bearing render](parts/{quote(p["oomp_id"])}/three_d_model/render_product_low.png)' for p in examples) + ' |', '', 'Generated open-bearing illustrations. Nominal envelopes follow the retained catalogue evidence; internal raceways and balls are illustrative.', '', '## Details', '', '[OOMP directory](' + config['base_directory'] + ') · [Generator and maintenance guide](README_GENERATOR.md) · [Build validation](build_validation.json) · [Visual checks](validation/README.md)', '', 'Each part provides a dimensioned SVG and A4 PDF, 1:1 outline, two printable label sizes, editable OpenSCAD, full and lightweight GLB models, seven SVG views per quality, four studio renders and an editable Blender scene.', '', 'GLB files use metres and Y-up; OpenSCAD uses millimetres. STL exports are not retained. Render previews are 512 px; high-resolution images are 2048 px. Historical native SolidCraft files and their validation evidence are retained where previously generated.', '', 'Dimensions reviewed in October 2026 are preserved, including corrected flanges and double-row widths. Records distinguish manufacturer-checked dimensions from local catalogue values. No new manufacturer verification or stock check is implied by this migration.', '', '## Parts', '', '**[Browse by bearing series](navigation/README.md)** · [All part folders](parts/) · [Source records](parts_source/)', '', '| Family | Parts |', '| --- | --- |']
    families = defaultdict(int)
    for series in groups.values():
        for part in series:
            families[part['family']] += 1
    overview += [f'| {family.replace("_", " ").capitalize()} | {count} |' for family, count in sorted(families.items())]
    overview += ['', '## Assembly', '', 'Choose a size, inspect its drawing and consult the purchased bearing specification for closure, clearance, tolerances and load ratings. These catalogue models do not establish a fit allowance or installation procedure.', '', '[Source evidence](source_file/solidcraft/) · [Migration record](migration/README.md) · [Explicit bearing declarations](working_oomp_declarations_bearing.py)', '']
    write_text(path=root / 'README.md', text='\n'.join(overview))
    print(f'Updated {len(selected)} bearing pages and {len(groups)} series indexes', flush=True)
    return {"parts": len(selected), "series": len(groups)}


if __name__ == '__main__':
    main()
