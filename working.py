"""Explicit ordered bearing pipeline. Geometry and presentation start at populate."""
import copy


def main(**kwargs):
    options = copy.deepcopy(kwargs)
    options.setdefault("model_jobs", 1)
    options.setdefault("run_oomp_populate", True)
    options.setdefault("run_oomp", True)
    options.setdefault("run_scad", True)
    options.setdefault("run_svg", True)
    options.setdefault("run_three_d_model", True)
    options.setdefault("run_documentation", True)
    options.setdefault("run_solidcraft", False)
    return run(**options)


def run(**kwargs):
    import working_cad
    options = copy.deepcopy(kwargs)
    options.setdefault("model_jobs", 1)
    working_cad.solidcraft_mode(options.get("run_solidcraft", False))
    if options.get("run_oomp_populate", False):
        import working_oomp_populate
        working_oomp_populate.main(**options)
    if options.get("run_oomp", False):
        import working_bearing_records
        working_bearing_records.main(**options)
    if options.get("run_scad", False):
        import working_bearing_scad
        working_bearing_scad.main(**options)
    if options.get("run_svg", False) or options.get("run_action", False):
        import working_bearing_drawing
        working_bearing_drawing.main(**options)
    if options.get("run_solidcraft", False):
        import working_bearing_native
        working_bearing_native.main(**options)
    if options.get("run_three_d_model", False):
        import working_three_d_model
        working_three_d_model.main(**options)
    if options.get("run_documentation", True):
        import action_documentation
        action_documentation.main(**options)


if __name__ == "__main__":
    main()
