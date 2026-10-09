"""Library-relative location of the collection-owned analysis plan, and its expansion.

The plan is library data beside the job instructions, not generated Python;
it is compact, and `start_run` expands it from the type's layout.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from commonplace.artifactrun.compact import expand_text

PLAN = "agentic-system-analyses/instructions/analyse-agentic-system/plan.yaml"


def expanded(library: Path) -> dict:
    """The full plan the engine runs for the analysis plan under `library`."""
    path = library / PLAN
    return yaml.safe_load(expand_text(path.read_text(encoding="utf-8"), library=library, plan_dir=path.parent))
