"""Mutable write-brief fixtures shared by the two review workflows."""

import json
from pathlib import Path

from tests.commonplace.validation_helpers import REPO_ROOT, copy_repo_files


def add_brief(root: Path, note: str) -> Path:
    copy_repo_files(root, "kb/types/write-brief.md", "kb/types/write-brief.schema.yaml")
    target = root / note
    brief = target.with_name(f"{target.stem}.brief.md")
    target.write_text(target.read_text().replace("type: types/note.md\n",
                                               f"type: types/note.md\nbrief: {brief.name}\n"))
    brief.write_text("---\ntype: types/write-brief.md\ndescription: Commission for Alpha, preserving its "
                     "example and excluding a new claim\n---\n\n# Brief: Alpha\n\n"
                     "## Must keep\n\nKeep the Alpha body passage.\n")
    return brief


def use_full_instruction(root: Path) -> None:
    rel = "kb/instructions/run-full-improvement-pass-on-note.md"
    (root / rel).write_text((REPO_ROOT / rel).read_text())


def captured_inputs(log: Path) -> list[dict]:
    return [json.loads(line) for line in Path(str(log) + ".inputs").read_text().splitlines()]
