"""Build routing tests: no CAD process, writes or remote robot actions."""
import copy
import importlib
import sys
from types import SimpleNamespace
from unittest.mock import patch
import pytest

BACKENDS = ["working_oomp_populate", "working_bearing_records", "working_bearing_scad", "working_bearing_drawing", "working_bearing_native", "working_three_d_model", "action_documentation"]


def run_entry(**kwargs):
    calls = []
    modules = {}
    for name in BACKENDS:
        modules[name] = SimpleNamespace(main=lambda name=name, **options: calls.append((name, options)))
    with patch.dict(sys.modules, modules):
        importlib.import_module(kwargs["module"]).main(**kwargs.get("options", {}))
    return calls


def test_make_all_orders_population_assets_and_documentation():
    calls = run_entry(module="action_make_all", options={"filter": "_608_size_", "model_jobs": 3})
    assert [name for name, _ in calls] == [name for name in BACKENDS if name != "working_bearing_native"]
    assert all(options["filter"] == "_608_size_" for _, options in calls)
    assert calls[-2][1]["model_jobs"] == 3


def test_explicit_model_opt_out_preserves_drawings_and_documentation():
    calls = run_entry(module="action_make_all", options={"run_three_d_model": False})
    names = [name for name, _ in calls]
    assert "working_three_d_model" not in names
    assert "working_bearing_drawing" in names
    assert names[-1] == "action_documentation"


def test_native_is_explicit_and_uses_bearing_author():
    calls = run_entry(module="action_make_solidcraft", options={"filter": "_f608_size_"})
    assert [name for name, _ in calls] == ["working_oomp_populate", "working_bearing_records", "working_bearing_native", "action_documentation"]
    assert calls[2][1]["filter"] == "_f608_size_"


def test_native_context_is_not_mutated():
    import working
    original = {"run_solidcraft": True, "run_documentation": False, "solidcraft_context": {"part_filter": "_608_size_"}}
    expected = copy.deepcopy(original)
    with patch.dict(sys.modules, {"working_bearing_native": SimpleNamespace(main=lambda **options: None)}):
        working.run(**original)
    assert original == expected


def test_invalid_native_mode_fails_before_writes():
    with pytest.raises(ValueError, match="run_solidcraft"):
        run_entry(module="action_make_all", options={"run_solidcraft": "false"})


def test_native_can_be_disabled_in_native_action():
    calls = run_entry(module="action_make_solidcraft", options={"run_solidcraft": False})
    assert "working_bearing_native" not in [name for name, _ in calls]


def test_drawing_stage_runs_once_with_both_flags():
    calls = run_entry(module="working", options={"run_action": True, "run_svg": True})
    assert [name for name, _ in calls].count("working_bearing_drawing") == 1


@pytest.mark.parametrize("module", ["action_make_all_no_stl", "action_make_scad", "action_make_scad_no_stl", "action_make_action_only", "action_make_action_only_filter"])
def test_focused_actions_do_not_require_legacy_oobb_or_launch_renders(module):
    with patch.dict(sys.modules, {"working_scad": None}):
        calls = run_entry(module=module, options={"filter": "_608_size_", "run_three_d_model": True})
    names = [name for name, _ in calls]
    assert "working_three_d_model" not in names
    assert "working_bearing_native" not in names
    assert names[-1] == "action_documentation"
