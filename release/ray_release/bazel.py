import os
import logging

import runfiles

REPO_NAME = "com_github_ray_project_ray"
_LEGACY_REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../.."),
)

the_runfiles = runfiles.Create()

logger = logging.getLogger(__name__)


def _norm_path_join(*args):
    return os.path.normpath(os.path.join(*args))


def bazel_runfile(*args):
    """Return the path to a runfile in the release directory."""
    p = _norm_path_join(*args)
    runfile = the_runfiles.Rlocation(os.path.join(REPO_NAME, p))
    if not runfile or not os.path.exists(runfile):
        logging.warning(f"runfile {p} not found, falling back to repo root")
        return os.path.join(_LEGACY_REPO_ROOT, p)
    return runfile
