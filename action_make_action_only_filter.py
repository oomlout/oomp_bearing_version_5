"""Refresh selected bearing labels, drawings and documentation without CAD renders."""

def main(**kwargs):
    kwargs.setdefault("filter", "_608_size_")
    kwargs["run_three_d_model"] = False
    kwargs["run_solidcraft"] = False
    kwargs["run_oomp_populate"] = True

    kwargs["run_oomp"] = True

    kwargs["run_action"] = True
    #kwargs["run_action"] = False

    kwargs["run_scad"] = False

    kwargs["generate_stl"] = False

    import working
    working.run(**kwargs)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="_608_size_")
    main(**vars(parser.parse_args()))
