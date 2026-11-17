"""Populate bearing recipes, then build drawings, models, renders and documentation."""

def main(**kwargs):
    kwargs.setdefault("model_jobs", 1)
    kwargs.setdefault("run_three_d_model", True)
    kwargs["run_oomp_populate"] = True

    kwargs["run_oomp"] = True

    kwargs["run_action"] = True
    #kwargs["run_action"] = False

    kwargs["run_scad"] = True
    # Native bearing CAD is a separate, explicit author; normal builds are portable.
    kwargs.setdefault("run_solidcraft", False)

    kwargs["run_svg"] = True

    kwargs["generate_stl"] = False

    # Retained native-author flags for explicit callers.
    kwargs["export_extras"] = kwargs.get("export_extras", True)  # STEP and PNG previews.
    kwargs["export_stl"] = False
    kwargs["verify_solidcraft"] = kwargs.get("verify_solidcraft", False)

    import working
    working.run(**kwargs)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Populate and build the bearing catalogue")
    parser.add_argument("--filter", default="")
    parser.add_argument("--model-jobs", type=int, default=1)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--no-models", dest="run_three_d_model", action="store_false")
    main(**vars(parser.parse_args()))
