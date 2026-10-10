"""Prepare isolated-input calibration packets and score human annotations.

No model launch, sandbox, production validation, or semantic grading is supplied.
Method bytes come only from one Git commit; answer keys stay outside packets.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

PROFILES_FILE = "kb/agentic-system-analyses/instructions/analyse-agentic-system/worker-profiles.yaml"
WORKSHOP = Path("kb/work/analysis-workflow-calibration")
METHOD_FILES = (
    "kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs-engine/verify-synthesis.md",
    "kb/agentic-system-analyses/types/agentic-system-verification.md",
    "kb/agentic-system-analyses/types/agentic-system-synthesis.md",
    "kb/agentic-system-analyses/instructions/agentic-analysis-records.md",
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path):
    return json.loads(path.read_text())


def save(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True,
    ).stdout


def prepare(repo: Path, revision: str, output: Path, profile: str,
            profiles_file: Path | None = None) -> dict:
    repo = repo.resolve()
    output = output.resolve()
    if output.is_relative_to(repo):
        raise ValueError("Run directory must be outside the repository; packets are not a sandbox")
    commit = git(repo, "rev-parse", "--verify", f"{revision}^{{commit}}").decode().strip()
    method = {path: git(repo, "show", f"{commit}:{path}") for path in METHOD_FILES}
    profiles_bytes = (profiles_file.read_bytes() if profiles_file is not None
                      else git(repo, "show", f"{commit}:{PROFILES_FILE}"))
    profiles = yaml.safe_load(profiles_bytes)["profiles"]
    if profile not in profiles:
        raise ValueError(f"Unknown worker profile: {profile}; available: {', '.join(profiles)}")
    selected = profiles[profile]
    if not all(selected.get(key) for key in ("harness", "launch-model", "effort")):
        raise ValueError(f"Incomplete worker profile: {profile}")
    fixtures_path = repo / WORKSHOP / "cases/packets.json"
    expected_path = repo / WORKSHOP / "expected/judgments.json"
    fixtures = load(fixtures_path)
    expected = load(expected_path)
    if set(fixtures) != set(expected) or len(fixtures) != 8:
        raise ValueError("Expected exactly eight matching case IDs")
    if any(not key.startswith("c") or not key[1:].isdigit() for key in fixtures):
        raise ValueError("Case IDs must be opaque c<number> names")
    for key, item in expected.items():
        if type(item["blocker"]) is not bool or not item["reason"]:
            raise ValueError(f"Invalid expected judgment: {key}")
    # Refuse reuse, including interrupted preparation. Pre-read inputs before writing.
    output.mkdir(parents=True, exist_ok=False)
    manifest = {
        "version": 1, "method-commit": commit, "profile": profile,
        "worker-profile": selected,
        "profile-source": str(profiles_file.resolve()) if profiles_file else f"{commit}:{PROFILES_FILE}",
        "task": "focused synthesis entailment assay, not full workflow validation",
        "files": {}, "cases": sorted(fixtures),
    }

    def retain(relative: str, data: bytes) -> None:
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        manifest["files"][relative] = digest(data)

    retain("private/worker-profiles.yaml", profiles_bytes)
    retain("private/expected.json", expected_path.read_bytes())
    retain("private/fixtures.json", fixtures_path.read_bytes())
    retain("private/protocol.md", (repo / WORKSHOP / "protocol.md").read_bytes())
    retain("private/runner.py", Path(__file__).read_bytes())
    for key, text in fixtures.items():
        retain(f"packets/{key}/input.md", text.encode())
        for index, data in enumerate(method.values(), 1):
            retain(f"packets/{key}/method-{index}.md", data)
        prompt = (
            "# Focused synthesis verification assay\n\n"
            "Judge whether the supplied synthesis excerpt is supported by the supplied "
            "evidence. Read input.md and method-1.md through method-4.md completely. "
            "method-1.md is the committed production synthesis-verifier mission; "
            "method-2.md and method-3.md give its judgment and synthesis contracts; "
            "method-4.md gives evidence interpretation rules.\n\n"
            "Assay deviations: these are synthetic excerpts, not complete set members. "
            "Judge only semantic support and materiality of the excerpt. Do not report "
            "missing frontmatter, sections, files, citation-link resolution, or a missing "
            "production self-check as defects. The source excerpt supplied here is the "
            "entire authorized evidence; make no source reads or new factual claims. "
            "No producer answers or previous refusals are supplied.\n\n"
            "Write response.md with ## Verification, ## Blockers and ## Limits. "
            "Blockers and Limits must each be exactly none or a Markdown list. "
            "Explain the defective passage, its evidence, the incorrect reader inference "
            "and why a limit cannot contain it. If support is insufficient to judge, "
            "write problem and explain instead. Do not correct the synthesis.\n\n"
            "Your only writable file is response.md. You may read only the five input "
            "files in this packet. Do not invoke skills or delegate. This textual scope "
            "requires the launching harness to enforce filesystem isolation separately.\n"
        )
        retain(f"packets/{key}/prompt.md", prompt.encode())
    save(output / "manifest.json", manifest)
    return manifest


def verify(run: Path) -> dict:
    manifest = load(run / "manifest.json")
    for relative, wanted in manifest["files"].items():
        path = run / relative
        if path.is_symlink() or not path.is_file() or digest(path.read_bytes()) != wanted:
            raise ValueError(f"Pinned input changed or missing: {relative}")
    for key in manifest["cases"]:
        packet = run / "packets" / key
        allowed = {"input.md", "prompt.md", "response.md", *(f"method-{i}.md" for i in range(1, 5))}
        if any(p.is_symlink() or p.name not in allowed or not p.is_file() for p in packet.iterdir()):
            raise ValueError(f"Unexpected packet entry: {key}")
    return manifest


def score(run: Path, annotations: Path) -> dict:
    manifest = verify(run)
    expected = load(run / "private/expected.json")
    observed = load(annotations)
    if set(observed) != set(expected):
        raise ValueError("Annotate every case, including execution failures")
    result = {"method-commit": manifest["method-commit"], "profile": manifest["profile"],
              "worker-profile": manifest["worker-profile"], "cases": {}, "counts": {
                  "detected": 0, "missed": 0, "false-blocker": 0,
                  "supported-control": 0, "execution-failure": 0, "unscorable": 0,
              }, "annotations-sha256": digest(annotations.read_bytes())}
    for key, item in observed.items():
        if not item.get("reason") or item.get("status") not in {"completed", "failed", "unscorable"}:
            raise ValueError(f"Missing status or annotation rationale: {key}")
        response = run / "packets" / key / "response.md"
        if item["status"] == "failed":
            outcome = "execution-failure"
        elif item["status"] == "unscorable":
            outcome = "unscorable"
        else:
            if not response.is_file() or not response.read_text().strip():
                raise ValueError(f"Completed case has no raw response: {key}")
            if type(item.get("blocker")) is not bool:
                raise ValueError(f"Completed case needs a boolean targeted blocker annotation: {key}")
            launch = item.get("launch", {})
            if any(launch.get(field) != value for field, value in manifest["worker-profile"].items()):
                raise ValueError(f"Launch does not match the pinned worker profile: {key}")
            if not launch.get("resolved-model") or not launch.get("isolation-evidence"):
                raise ValueError(f"Record resolved-model (or unknown) and isolation evidence: {key}")
            if expected[key]["blocker"]:
                outcome = "detected" if item["blocker"] else "missed"
            else:
                outcome = "false-blocker" if item["blocker"] else "supported-control"
        result["counts"][outcome] += 1
        result["cases"][key] = {
            "outcome": outcome, "annotation": item, "expected": expected[key],
            "response-sha256": digest(response.read_bytes()) if response.is_file() else None,
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="action", required=True)
    prep = subs.add_parser("prepare")
    prep.add_argument("--repo", type=Path, default=Path.cwd())
    prep.add_argument("--revision", required=True)
    prep.add_argument("--output", type=Path, required=True)
    prep.add_argument("--profile", required=True)
    prep.add_argument("--profiles-file", type=Path,
                      help="Explicit exploratory profile snapshot; default: committed profile file")
    check = subs.add_parser("verify")
    check.add_argument("run", type=Path)
    scoring = subs.add_parser("score")
    scoring.add_argument("run", type=Path)
    scoring.add_argument("--annotations", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.action == "prepare":
            result = prepare(args.repo, args.revision, args.output, args.profile, args.profiles_file)
        elif args.action == "verify":
            result = verify(args.run)
        else:
            result = score(args.run, args.annotations)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Calibration failed: {error}\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
