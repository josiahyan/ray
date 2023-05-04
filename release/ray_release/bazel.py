import os

import runfiles

REPO_NAME = "com_github_ray_project_ray"

the_runfiles = runfiles.Create()


def _norm_path_join(*args):
    return os.path.normpath(os.path.join(*args))


def bazel_runfile(*args):
    """Return the path to a runfile in the release directory."""
    path = os.path.join(REPO_NAME, _norm_path_join(*args))
    return the_runfiles.Rlocation(path)
