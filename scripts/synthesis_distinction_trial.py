"""Prepare isolated packets for the frozen synthesis wording experiment.

No model calls, workflow mutations, acceptance claims, or semantic scoring.
See kb/reports/retained/synthesis-distinction-pilot-20261005/protocol/README.md
for execution rules.
"""

import argparse
import hashlib
import json
from pathlib import Path

PROTOCOL = Path(__file__).resolve().parents[1] / "kb/reports/retained/synthesis-distinction-pilot-20261005/protocol"
TARGET = "None checks prior outputs for correctness before inclusion."
CASES = {
    "original": TARGET,
    "qualified": (
        "The retrieval-synthesis curator prompt requests assessment of solution "
        "effectiveness and prioritizes accuracy; the inspected implementation does "
        "not independently validate that assessment before using its output."
    ),
    "bounded-absence": (
        "The direct-retrieval route has no curator call or correctness filter "
        "before supplying the selected prior pairs to the generator."
    ),
    "implicit-overclaim": (
        "Across these routes, prior outputs enter context without any assessment "
        "of their correctness."
    ),
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_bundle():
    path = PROTOCOL / "frozen-input.json"
    raw = path.read_bytes()
    bundle = json.loads(raw)
    for key, item in bundle["files"].items():
        if digest(item["text"].encode()) != item["sha256"]:
            raise ValueError(f"Frozen content hash mismatch: {key}")
    return bundle, digest(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("verify", help="Verify every frozen file's SHA-256")
    packet = sub.add_parser("packet", help="Create one fresh worker directory")
    packet.add_argument("--arm", choices=["control", "treatment"], required=True)
    packet.add_argument("--job", choices=["synthesize", "verify-synthesis"], required=True)
    packet.add_argument("--out", type=Path, required=True)
    packet.add_argument("--synthesis", type=Path)
    packet.add_argument("--verification", type=Path)
    packet.add_argument("--case", choices=list(CASES))
    packet.add_argument("--delivery", choices=["files", "inline"], default="files")
    args = parser.parse_args()
    bundle, bundle_hash = load_bundle()
    if args.command == "verify":
        print(f"Verified {len(bundle['files'])} frozen files; bundle SHA-256 {bundle_hash}")
        return
    if args.case and (args.job != "verify-synthesis" or args.synthesis):
        parser.error("--case is a review-only alternative to --synthesis")
    if args.verification and (args.job != "synthesize" or not args.synthesis):
        parser.error("--verification requires synthesize and --synthesis (correction)")
    if args.job == "synthesize" and args.synthesis and not args.verification:
        parser.error("correction requires both --synthesis and --verification")
    if args.job == "verify-synthesis" and not (args.synthesis or args.case):
        parser.error("review requires --synthesis or --case")

    # Validate all dependent inputs before creating the output directory.
    supplied = {}
    if args.synthesis:
        supplied["synthesis.md"] = args.synthesis.read_bytes()
    if args.verification:
        supplied["verification.md"] = args.verification.read_bytes()
    if args.case:
        baseline = bundle["files"]["historical/synthesis-1.md"]["text"]
        if baseline.count(TARGET) != 1:
            raise ValueError("Expected exactly one target sentence in frozen synthesis-1")
        supplied["synthesis.md"] = baseline.replace(TARGET, CASES[args.case]).encode()

    instruction = bundle["files"][f"method/{args.job}.md"]["text"]
    amendment = b""
    if args.arm == "treatment":
        amendment = (PROTOCOL / f"treatment-{args.job}.txt").read_bytes()
        marker = "Run the acceptance check before submitting."
        if instruction.count(marker) != 1:
            raise ValueError("Instruction insertion point changed")
        instruction = instruction.replace(marker, amendment.decode().strip() + "\n\n" + marker)

    out = args.out.resolve()
    manifest_path = out.with_name(out.name + ".manifest.json")
    if manifest_path.exists():
        raise FileExistsError(manifest_path)
    out.mkdir(parents=True, exist_ok=False)
    for key, item in bundle["files"].items():
        if key.startswith("historical/") or key in {
            "method/synthesize.md", "method/verify-synthesis.md"
        }:
            continue
        dest = out / "inputs" / key
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(item["text"].encode())
    (out / "inputs/instruction.md").write_bytes(instruction.encode())
    for name, content in supplied.items():
        (out / "inputs" / name).write_bytes(content)
    (out / "scratch").mkdir()
    round_name = "after-blockers" if args.verification else "first"
    task_inputs = ["boundary.md", "runtime.md", "memory.md", "epistemic.md", "reconciliation.md"]
    if args.delivery == "inline":
        reading = [
            "Read the complete inlined instruction, method contracts and records below.",
            "They are the exact contents of the named files under inputs/.",
            "Use the files only for targeted checks; avoid rereading whole documents.",
        ]
    else:
        reading = [
            "Read inputs/instruction.md, then all files in inputs/method/, then these records:",
            *[f"- inputs/records/{name}" for name in task_inputs],
            "Read each required file completely in bounded ranges; recover truncated reads.",
        ]
    lines = [
        "Complete one isolated analysis job using only this packet.",
        *reading,
        "Inspect only source paths needed to test a claim. Do not dump the source tree",
        "or re-read whole records when a targeted range or search will suffice.",
        "Keep a concise scratch index of record IDs and source anchors for later checks.",
        "", "Experiment transport overrides (identical in both conditions):",
        "This is an offline replay, not a live workflow job. These overrides replace",
        "the frozen method's filesystem, command, source-access and submission rules.",
        "All paths below are relative to your working directory. Do not resolve",
        "historical absolute paths, follow background links, or read parent directories.",
        "The supplied method contracts contain the operative vocabulary definitions.",
        "Relevant source text from the registered revision is in inputs/source/.",
        "You may inspect it read-only. Other source artifacts are unavailable here;",
        "bound conclusions accordingly. Do not execute source code or use the network.",
        "Do not run Commonplace commands: there is no live run-state or acceptance service.",
        "Check your format and references yourself; do not claim a checker passed.",
        "Write only output.md or problem.md, plus scratch/ files. Do not delegate.",
        "Do not read other tasks, previous audits, scoring guides, or experiment metadata.",
        "", f"job = {args.job}", "system = Dynamic Cheatsheet",
        f"run-id = {bundle['run_id']}", f"round = {round_name}",
        "boundary = inputs/records/boundary.md", "runtime = inputs/records/runtime.md",
        "memory = inputs/records/memory.md", "epistemic = inputs/records/epistemic.md",
        "reconciliation = inputs/records/reconciliation.md",
        "output = output.md", "problem = problem.md", "scratch = scratch/",
        "Member citations retain sibling names such as runtime.md; these denote",
        "the corresponding supplied records, not missing files beside output.md.",
    ]
    if "synthesis.md" in supplied:
        key = "previous-synthesis" if args.job == "synthesize" else "synthesis"
        lines.append(f"{key} = inputs/synthesis.md")
    if args.verification:
        lines.append("verification = inputs/verification.md")
    if args.delivery == "inline":
        lines += [
            "", "Required documents follow in full. Their text is the content of the",
            "corresponding inputs/ files, with SHA-256 in each boundary line.",
            "Reading the text below fulfills the read-first and task-input reading",
            "rules. Do not re-read these files wholesale through tools; use their",
            "paths only for targeted checks. Inspect source files selectively.",
        ]
        names = [
            "inputs/instruction.md",
            *[f"inputs/method/{name}" for name in (
                "collection.md", "worker-rules.md", "sources.md", "records.md",
                "overview.md",
            )],
            *[f"inputs/records/{name}" for name in task_inputs],
            *[f"inputs/{name}" for name in supplied],
        ]
        for name in names:
            data = (out / name).read_bytes()
            lines += ["", f"=== BEGIN {name} sha256={digest(data)} ===",
                      data.decode(), f"=== END {name} ==="]
    lines += ["", "Finish with one line naming output.md or problem.md."]
    (out / "prompt.txt").write_text("\n".join(lines) + "\n")
    manifest = {
        "arm": args.arm, "job": args.job, "case": args.case,
        "delivery": args.delivery,
        "round": round_name, "bundle_sha256": bundle_hash,
        "treatment_sha256": digest(amendment) if amendment else None,
        "files": {str(p.relative_to(out)): digest(p.read_bytes())
                  for p in sorted(out.rglob("*")) if p.is_file()},
    }
    # Coordinator retains this outside the worker's directory.
    with manifest_path.open("x") as stream:
        json.dump(manifest, stream, indent=2)
        stream.write("\n")
    print(out / "prompt.txt")


if __name__ == "__main__":
    main()
