"""Live-agent review prompt artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class LiveAgentPrompt:
    review_run_id: int
    artifact_dir: Path
    prompt_path: Path
    bundle_output_path: Path


def write_live_agent_prompt(
    *,
    review_run_id: int,
    artifact_dir: Path,
    prompt: str,
) -> LiveAgentPrompt:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = artifact_dir / "prompt.md"
    bundle_output_path = artifact_dir / "bundle-output.md"
    prompt_path.write_text(prompt, encoding="utf-8")
    return LiveAgentPrompt(
        review_run_id=review_run_id,
        artifact_dir=artifact_dir,
        prompt_path=prompt_path,
        bundle_output_path=bundle_output_path,
    )
