"""Sphinx configuration for the shared ACO documentation. Shared settings live in docs/_aco."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from _aco.base import configure  # noqa: E402

configure(globals(), slug="aco-docs", title="ACO Components", exclude=["_configs"])
