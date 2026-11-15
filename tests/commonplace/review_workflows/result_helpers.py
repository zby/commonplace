"""Typed review fixtures shared by fake harness and storage consumers."""
import hashlib
from pathlib import Path

from commonplace.lib.review_workflows import result_contract

SOURCE = Path(__file__).resolve().parents[3] / "kb"


def copy_contract(library: Path) -> None:
    for name in ("review-result.md", "review-result.schema.yaml"):
        path = library / "types" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((SOURCE / "types" / name).read_bytes())


def evidence(root: Path, target: str = "Fixture target", raw: str = "Fixture raw output") -> dict:
    digest = hashlib.sha256(target.encode()).hexdigest()
    base = root / "kb/reports/state/fixtures" / digest
    base.mkdir(parents=True, exist_ok=True)
    (base / "target.md").write_bytes(target.encode())
    (base / "review.md").write_bytes(raw.encode())
    return {"target_sha256": digest, "target_capture": (base / "target.md").relative_to(root).as_posix(),
            "observation": (base / "observation.json").relative_to(root).as_posix(), "contract_sha256": result_contract.fingerprint(result_contract.capture_contract()),
            "raw_output": (base / "review.md").relative_to(root).as_posix(),
            "raw_output_sha256": hashlib.sha256(raw.encode()).hexdigest()}


def findings(outcome):
    return [] if outcome == "pass" else [{"scope": "document", "quotes": [], "reason": "A fixture finding",
                                         "level": outcome}]


FAKE_RESULT = r'''
def review_text(outcome):
    import json
    findings = [] if outcome in ("pass", "report") else [
        {"scope": "document", "quotes": [], "reason": "A fixture finding", "level": outcome}]
    data = {"type": "types/review-result.md", "findings": findings, "outcome": outcome}
    body = "# Review\n\n## Summary\n\nReviewed.\n"
    if outcome == "report":
        data["attack-outcome"] = "no surviving attack"
        body = ("# Critique\n\n**Central commitment:** Test.\n**Critique mode:** claim\n\n"
                "## Strongest case against it\nAn attack.\n\n"
                "## How the note engages it\nAnswers it.\n\n## Constructive findings\nNone.\n")
    return "---\n" + json.dumps(data) + "\n---\n\n" + body
'''
