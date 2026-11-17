"""Generate bearing meshes, views and renders using saved population recipes."""
from working_three_d_model import main


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="")
    parser.add_argument("--model-jobs", type=int, default=1)
    parser.add_argument("--force", action="store_true")
    main(**vars(parser.parse_args()))
