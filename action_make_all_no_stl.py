"""Refresh bearing metadata, SCAD, drawings and pages without mesh generation."""

def main(**kwargs):
    kwargs["run_three_d_model"] = False
    kwargs["run_solidcraft"] = False
    kwargs["run_oomp_populate"] = True

    kwargs["run_oomp"] = True

    kwargs["run_action"] = True
    #kwargs["run_action"] = False

    kwargs["run_scad"] = True

    kwargs["generate_stl"] = False

    import working
    working.run(**kwargs)

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)
