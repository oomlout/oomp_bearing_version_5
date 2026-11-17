# Native bearing generation

Updated 27 October 2026. The generator is deterministic and explicit: ordinary
make-all, label and SCAD actions are not invoked. Without `--build` it only plans.
The earlier full run finished with 276 succeeded, one reused, 61 unsupported and
one needs_review. The extension work is limited to representative pilots; its
full batch has not been launched.

## Launch the extension

Use `LUNA_BEARING_EXTENSIONS_PROMPT.txt` for the supervised run. From the helper:

```powershell
& .\.venv\Scripts\python.exe .\action_build_bearing_catalogue.py --root C:\od\OneDrive\docs\oomp_bearing --build --series F600 --series 5200 --series 5300 --manufacturer-only
```

The dimension reviews were resolved on 27 October 2026 at the user's request.
All 61 extension entries and the separate 6208 correction now pass preflight.
Full inventory: **339 ready, zero reviews**. This is eligibility, not a claim that
all native models have been built.

The choice is standard metric open catalogue dimensions from the cited
manufacturers. No measured sales-popularity ranking is asserted. For 5300, 5301,
5315 and 5316, the model uses the documented NSK 25-degree 5xxx family convention
alongside RBI envelope dimensions; that angle is labelled a selected catalogue
convention, not an RBI-specific specification.

`solidcraft_dimension_migration.json` maps the 35 old IDs to corrected IDs and
locates the archive of original folders, drawings and CSV. Source and materialized
records, hashes and 70 bold SVG labels have been updated. Old dimensioned artwork
is archived; it has not been relabelled as corrected. No full batch was launched.

The launch prompt now runs the 61 extensions followed by a separate 6208 run.

`--size` and `--series` can be repeated. `--filter` matches IDs; `--limit` bounds
selection. The extension selection excludes the original single-row catalogue.
Re-running reuses results only if inputs, generator, backend and artifact hashes
match. An exit code of 1 indicates a failure or unexpected new review; inspect the counts.

## Models and sources

Authors support open single-row deep-groove, flanged deep-groove and double-row
angular-contact presentation models. A flange is part of the continuous outer
race. Double-row models share inner and outer races, with two rows of balls,
four retainers and mirrored groove offsets for the sourced contact angle.
Unspecified closure is open; shields and seals require a separate author.

Dimensions use millimetres. Bore, outside diameter, width, flange dimensions and
contact angles must agree with sourced facts. Ball sizes/counts, pitch circle,
row spacing, groove conformity, chamfers and retainer details are illustrative
unless individually sourced. These are not manufacturer reconstructions or
manufacturing/tolerance/load-rating models.

Facts: `source_file/solidcraft/bearing_facts.json`.
Snapshots: `source_file/solidcraft/references/`.
Sources: JTEKT open flanged product pages, NSK Bearing and Linear Replacement
Guide pages 48 and 50, and RBI's 5300-series table. The helper's explicit
`components/bearing_catalogue/source_extensions.py` refreshes these records;
planning and generation never fetch or infer dimensions online.

## Saved output and validation

```text
parts/<part_id>/solidcraft/
  latest_success.json
  generations/<fingerprint>_<run>/
    bearing_<size>_open.solidcraft
    manifest.json
    ...native health and RPC evidence...
solidcraft_library/masters/<geometry_hash>/<run>/
  parametric.solidcraft
  edited.solidcraft
  manifest.json
```

Native-only delivery; no STL/STEP/preview is required or exported by the batch.
Read latest_success.json to locate the current hashed manifest. Older successes
and failed attempts remain preserved. A new pointer is published only after
validation. Consuming projects use the existing full-folder part-library importer.

Each master is saved, width-edited by 1%, saved again and reopened. Named items
are saved and independently reopened. Native inspection checks healthy features,
constrained sketches, closed positive-volume bodies, bounds, bore/OD surfaces,
ball placement, spacing and retainers. Extension checks include flange diameter
and shoulder thickness, and both rows' angular-contact raceway surfaces.
Only the tested width edit is qualified; arbitrary manual edits are not certified.

## Monitor

- `solidcraft_plan.json`: complete catalogue eligibility.
- `solidcraft_progress.json`: latest selected run, current item and counts.
- `solidcraft_library/runs/<run>/progress.json`: retained run evidence and errors.
- `solidcraft_library/build.lock`: writer PID; never remove a live writer's lock.

The extension pilots are F608, 5204 and 5305. See
`solidcraft_extension_pilot_validation.json` for final test results and manifests.
The helper automated suite passed 146 tests after the migration changes.
The post-migration pilots are 5300, 6208 and F683; their results are recorded in
`solidcraft_dimension_resolution_validation.json`.

Implementation: `C:\od\OneDrive\docs\software_cad_mcp_helper\components\bearing_catalogue`.
