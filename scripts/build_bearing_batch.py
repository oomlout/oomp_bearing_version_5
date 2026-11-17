"""Overlap CPU mesh work while limiting Blender processes to the available GPU."""
import argparse
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import multiprocessing
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def initialize_renderer(**kwargs):
    import mechanical_model_render
    semaphore = kwargs["semaphore"]
    original = mechanical_model_render.render_studio

    def render_with_limit(**options):
        with semaphore:
            return original(**options)

    mechanical_model_render.render_studio = render_with_limit


def main(**kwargs):
    import working_three_d_model
    options = dict(kwargs)
    render_jobs = options.pop("render_jobs", 1)
    if type(render_jobs) is not int or not 1 <= render_jobs <= 2:
        raise ValueError("render_jobs must be 1 or 2")
    context = multiprocessing.get_context("spawn")
    semaphore = context.BoundedSemaphore(render_jobs)
    initializer = partial(initialize_renderer, semaphore=semaphore)
    pool = partial(ProcessPoolExecutor, mp_context=context, initializer=initializer)
    original_pool = working_three_d_model.ProcessPoolExecutor
    # Scheduling changes only concurrency. Recipes, render quality, artifact
    # validation and cache fingerprints use the unchanged canonical builder.
    working_three_d_model.ProcessPoolExecutor = pool
    try:
        return working_three_d_model.main(**options)
    finally:
        working_three_d_model.ProcessPoolExecutor = original_pool


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="")
    parser.add_argument("--model-jobs", type=int, default=4)
    parser.add_argument("--render-jobs", type=int, default=1)
    parser.add_argument("--force", action="store_true")
    main(**vars(parser.parse_args()))
