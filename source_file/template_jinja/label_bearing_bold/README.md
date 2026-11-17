# Bold bearing labels

Run `action_make_label_overwrite.bat` to regenerate only the two labels for
every bearing, with overwrite. It can be launched from any working directory.

For printing, run `action_make_label_pdf_overwrite.bat`. It regenerates both
SVG sizes from current details and exports matching PDFs with text converted
to vector outlines, preventing font substitution when opening or printing.
Inkscape must be on PATH. To regenerate just selected bearings, use
`action_make_label_pdf_overwrite.bat --bearing 606 --bearing 608`.
On Windows the batch checks for `ARIALNB.TTF` before exporting. Install Arial
Narrow Bold on the exporting computer; outlining a substituted font cannot
repair its spacing. The reported 606/608 PDFs used Verdana Bold instead.
The webserver's **Convert to PDF** action also outlines these bold bearing labels;
restart a running webserver after updating its code.

| Output | Inches | Millimetres |
| --- | --- | --- |
| `label_bearing_bold_3x2.svg` | 3 × 2 | 76.2 × 50.8 |
| `label_bearing_bold_1_5x1.svg` | 1.5 × 1 | 38.1 × 25.4 |

Print at **100% / actual size**. The bearing designation is white on black,
followed by the family/series and bold ID, OD and width values in millimetres.
Decimal dimensions are retained. The existing three-word BIP39 identifier is
bold along the bottom. All artwork is black and white, with condensed editable
text using Arial Narrow (Liberation Sans Narrow fallback).

`working_oomp.py` calls `working_bearing_labels.add_actions`, registering a
native `text_jinja_template` action for each size. The template computes its
content and font fitting at render time. `dict_data_yaml_files` loads current
`parts_source/<bearing>/working.yaml` and optional
`parts/<bearing>/working_manual.yaml` each time the action runs; source fields
override generated metadata and manual fields override the source. Empty
`file_test` values ensure overwrite. There is no frozen dimensions snapshot.

Supported fields: `size` (designation), `family` or `series`, `id_mm` or
`inner_diameter` or numeric `id`, `od_mm` or `od`, and `width_mm` or `width`
(with `depth` fallback). Taxonomy values are fallbacks. Generated OOMP `id`
strings are never treated as the inner diameter. Source folders containing
underscores in place of decimal dots are mapped to the existing OOMP folders.
Keep source dimensions and taxonomy consistent when changing bearing identity.

The batch refreshes all label action definitions, preserves other actions and
artwork, and removes stale `label_bearing_bold*.png` renders only. It does not
run AI images, CAD, CorelDRAW, or other label actions. SVG output is intentional;
PDF and PNG conversion flags are off. Errors return a nonzero exit status.

Requirements: Python, PyYAML and Jinja2; Arial Narrow should be installed when
viewing SVGs or generating PDFs, including the Bold face (`ARIALNB.TTF`).
The outlined PDFs need no fonts installed to view or print. The templates contain font advance widths measured from
Arial Narrow Bold so fitting remains dynamic without custom Jinja filters.
Pillow and pytest are used by `python -m pytest tests/test_bearing_labels.py -q`.

The bundled English BIP39 list comes from
`oomlout_oomp_version_5/source/bip_39_wordlist.txt`. Existing stored three-word
names take precedence. New parts use the same first three 11-bit indices from
the taxonomy-based OOMP ID's MD5. The numeric source `id` is not used for hashing.
