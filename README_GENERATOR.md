# Bearing generator and maintenance

The complete current build runs offline from this checkout. Install Python 3.12+
and Blender 4.5+ (tested with Blender 5.2), then:

```powershell
python -m pip install -r requirements.txt
python action_make_all.py --model-jobs 1
```

Set `OOMP_BLENDER_EXE` when Blender is not on PATH or in its normal installation
directory. Full builds render every part, so allow substantial time. Completed,
unchanged model builds are reused only after recipe/code and artifact-hash checks.
Public build commands default to one worker to limit GPU and host-memory use.
Increase concurrency only when the workstation has sufficient memory and disk
space for Windows paging as well as the generated assets.

## Explicit population stages

Edit `working_oomp_declarations_bearing.py`. There is one verbose, independently
editable dictionary per bearing. Dimensions, source authority and illustrative
internal parameters are named separately. The import utility in `scripts/` was
used once for migration; do not rerun it over subsequent hand edits.

`working_oomp_populate_bearing.py` resolves these stages with `**kwargs` functions:

1. Identity, taxonomy and retained catalogue metadata.
2. Nominal bore, outside diameter, width, flange dimensions and source evidence.
3. Race section vertices, ball radius, row centres and every ball position.
4. Full/display resolution, material, cameras, lighting and render outputs.
5. Drawing dimensions, page styles and label content.
6. Part descriptions and README fields.

The populated `parts_source/*/working.yaml` is the complete recipe. The
materialization stage updates `parts/*/working.yaml` while retaining existing
short names and specialist metadata. Mesh, SCAD, drawing and render stages read
those saved fields; they never infer dimensions from filenames or fetch evidence.
Changing populated geometry means changing the declarations/populate code and
rerunning population, rather than patching a render-only default.

## Focused commands

```powershell
# Full pipeline for the 608 only (substring or wildcard ID filter).
python action_make_all.py --filter _608_size_ --model-jobs 1

# Population, drawings, labels and documentation without expensive renders.
python action_make_all.py --no-models

# Render/model stage alone, from existing populated records.
python action_make_three_d_model.py --filter _f608_size_ --model-jobs 1

# Bulk models: four CPU preparation workers share one Blender/GPU slot.
python scripts/build_bearing_batch.py --model-jobs 4 --render-jobs 1

# Lower-memory build/resume with the same render quality.
python scripts/build_bearing_batch.py --model-jobs 1 --render-jobs 1

# Documentation alone; refreshes all navigation even on a filtered build.
python action_documentation.py

# Contract, geometry and asset verification.
python -m pytest -q
python working_validate_bearings.py
```

The optional local catalogue browser uses the same populated records and prefers
the new studio renders. Run `python -m webserver.app`, then open the address
printed by the server. See [browser configuration](webserver/README.md) for host,
port and part-source settings.

`--force` rebuilds selected models even when their cache matches. Failed model
builds leave the last complete manifest in place and return a failure status;
`three_d_model_build.json` records per-part errors. Each successful build exports
full and display GLB, fourteen mesh-derived vector views, four Cycles renders,
an editable Blender studio and a hashed manifest. OpenSCAD uses mm; GLB uses metres
with Y-up. SCAD uses the same populated component definitions.

## Drawings, pages and compatibility

Dimension sheets show nominal front/side envelopes; they are not section drawings
of bearing internals. `working_svg.svg` is a 1:1 outline; the dimension sheet is
scaled to A4 and labels its scale. Label PDFs are 76.2 x 50.8 and 38.1 x 25.4 mm.
No unverified generic ISO/DIN compliance claim is added to the new drawings.

`working_bearing_documentation.py` owns part pages and series indexes.
`documentation.json` owns the root introduction and selected examples. Generated
part sections have explicit markers; earlier notes remain in a collapsed section.
The original materialized IDs (including decimal points) and short names remain
stable. Forty-five old source-folder aliases are archived outside active roots.

The older `working_svg.py`, `working_scad.py` and OOBB helper files are retained
for compatibility/evidence. Current entry points dispatch to the bearing modules,
so ordinary builds do not invoke the scaffold plate recipe or legacy robot jobs.

## Native SolidCraft history

Historical native assets are retained under each part's `solidcraft/` and
`solidcraft_library/`. They are not counted as newly verified models. The complete
new GLB/Blender pipeline does not depend on SolidCraft or external OOMP modules.

An explicit `python action_make_solidcraft.py` delegates to the established native
bearing author. Set `OOMP_BEARING_NATIVE_HELPER` to its checkout, containing
`.venv/Scripts/python.exe` and `action_build_bearing_catalogue.py`; its CAD bridge
must be configured. This author uses its separately reviewed native specification.
Native generation is deliberately opt-in and preserves historical generations.

[Migration details and hard-link policy](migration/README.md) ·
[Original native workflow](migration/legacy/SOLIDCRAFT_BEARINGS.md) ·
[OOMP documentation standard](https://github.com/oomlout/oomlout_oomp_version_5/blob/main/presentation/README.md)

## STL storage policy

STL exports are not retained or tracked, including historical exports. Normal
builds write GLB models and editable OpenSCAD; legacy STL flags do not enable
STL generation. The optional native author removes its disposable STL outputs
after a successful run. The original OneDrive source remains untouched.

On 17 November 2026 the repository history was replaced by a fresh snapshot
without STL files. See [the retirement inventory](migration/stl_retirement.json).
