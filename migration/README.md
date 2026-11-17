# Bearing migration

The working catalogue was migrated from `C:\od\OneDrive\docs\oomp_bearing`
to `C:\gh\oomp_bearing_version_5` on 16 November 2026. The original directory
was retained. `manifest.json` records the 18,786 migrated files and their routes.
Python caches, pytest caches and incomplete temporary files were excluded.

The reviewed 339-part inventory, corrected CSV, manufacturer snapshots, native
CAD history, labels and earlier drawings are preserved. Original scripts and
reports are under `legacy/`; the newer repository scaffold remains the starting
point for the current build commands. `legacy_metadata/` preserves the exact
pre-migration source and materialized YAML files. Decimal-bearing IDs and existing
short names are retained for compatibility.

The old folder had 339 source records but 338 materialized YAML files. The missing
6700 record was reconstructed from its source declaration. Thirty source-folder
spellings were normalized to their existing materialized IDs for case-sensitive
checkouts; see `folder_casing.json`. Native artifact hashes for all 339 retained
models pass the [history integrity audit](../native_history_validation.json).

On 17 November 2026 all STL exports were removed from this checkout and its Git
history was replaced with a fresh snapshot. GLB models, studio scenes, drawings
and native SolidCraft files remain. See [the retirement inventory](stl_retirement.json).
The original OneDrive folder remains untouched; removing a hard link here does
not remove the original file there. Original migration inventories describe the
initial import, including STL files that have since been retired.

Historical SolidCraft binaries still use **hard links** on this workstation.
Treat native files inside `solidcraft/` histories and `solidcraft_library/` as
immutable; copy to a new filename before editing. New generated files in
`three_d_model/` are independent of the original OneDrive source.

Historical manifests retain their original STL entries as evidence; those files
are intentionally absent and excluded from the retained-native integrity audit.
Historical manifests and input hashes describe their original runs, not a new
validation of the native CAD. Their original machine paths remain evidence.
Current mesh/render manifests are regenerated separately and use relative files.
The current build never silently invokes or edits the historical native CAD.

The mesh studio, pose and hidden-line renderer were adapted from the local
`oomp_mechanical_version_5` project. Copies are included in this repository;
building does not import code from its sibling checkout. Their settings are
resolved and saved by the bearing populate stage.
