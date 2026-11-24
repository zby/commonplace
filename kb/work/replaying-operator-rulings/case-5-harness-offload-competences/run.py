"""Single-use replay for Case 5 (harness offloading vs. base LLM competences).

Run from the repository checkout after commissioning. An existing run directory
blocks reruns. Use --model to override the default worker/scorer model.
"""
import argparse
import concurrent.futures
import hashlib
import json
import random
import subprocess
import tempfile
from pathlib import Path

BASE_COMMIT = "785ffc64a"
RETRIEVAL_PATHS = [
    "kb/theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md",
    "kb/theory/semantic-work-can-be-relocated-but-not-eliminated.md",
]

COMMISSION = (
    "Write one kb/theory/ note (complete Markdown file with YAML frontmatter, "
    "30-65 lines) specifying what base competences a frozen LLM needs to run a "
    "selection-based learning system like Commonplace autonomously. Leave aside "
    "inference-time compression and speculative domain ceilings; focus strictly "
    "on the base competences the LLM needs to run the loop. Output only the "
    "Markdown note."
)

ALLOCATION_NUDGE = (
    "Before attributing a required capability to one component (here, the "
    "frozen LLM), check each item against the rest of the system's "
    "architecture: do not assign a system-level function to the model if "
    "another layer can perform it."
)

RUBRIC = """Grade each anonymous draft on two independent dimensions:

Dimension 1 — Harness offloading (H, P, or M):
- H: Explicitly separates loop functions that code / the harness / software can supply (such as enforcement, context loading, trace capture, replay, store bookkeeping, or rollbacks) from the narrower set of irreducible semantic competences required of the frozen LLM, and keeps the LLM list narrowed accordingly.
- P: Mentions that tools, code, or a harness assist the model, or moves one mechanical item off the model, without systematically factoring harness-offloadable work out of the base-LLM list.
- M: Attributes system-level loop functions (such as enforcement, trace collection, replay, or store bookkeeping/pruning) directly to the frozen base LLM without factoring out what code/harness can supply.

Dimension 2 — Working-hypothesis modality (W or U):
- W: Explicitly marks the competence list/split as a working hypothesis or conjecture (in title, description, opening, or Scope) rather than an established requirement.
- U: States the list as an unqualified or settled requirement.

Return all 12 IDs with both grades (e.g., `d01: H / W`) and a brief justification for each. Do not infer experimental conditions."""


def git_show(path: str) -> str:
    return subprocess.check_output(["git", "show", f"{BASE_COMMIT}:{path}"], text=True)


def call_model(out: Path, name: str, model: str, system: str, prompt: str) -> str:
    cmd = [
        "claude",
        "-p",
        "--model",
        model,
        "--tools",
        "",
        "--strict-mcp-config",
        "--disable-slash-commands",
        "--no-session-persistence",
        "--output-format",
        "json",
        "--system-prompt",
        system,
    ]
    with tempfile.TemporaryDirectory() as cwd:
        r = subprocess.run(cmd, input=prompt, cwd=cwd, text=True, capture_output=True, timeout=900)
    if r.returncode:
        (out / f"{name}.error").write_text(r.stderr + "\n" + r.stdout)
        raise RuntimeError(f"{name} exited {r.returncode}")
    j = json.loads(r.stdout)
    (out / f"{name}.meta.json").write_text(
        json.dumps(
            {
                k: j.get(k)
                for k in (
                    "is_error",
                    "modelUsage",
                    "duration_ms",
                    "num_turns",
                    "total_cost_usd",
                    "stop_reason",
                )
            },
            indent=2,
        )
        + "\n"
    )
    if j.get("is_error") or not j.get("result"):
        raise RuntimeError(f"{name} did not return a completion")
    (out / f"{name}.txt").write_text(j["result"].strip() + "\n")
    return j["result"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="opus")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    out = here / "run"
    out.mkdir()

    collection_doc = git_show("kb/theory/COLLECTION.md")
    article_doc = (here / "materials" / "lead-article-pre-extraction.md").read_text()
    retrieval_docs = "".join(f"\n\nDOCUMENT: {p}\n{git_show(p)}" for p in RETRIEVAL_PATHS)

    base_packet = (
        f"\n\nDOCUMENT: kb/theory/COLLECTION.md\n{collection_doc}"
        f"\n\nDOCUMENT: lead-article-pre-extraction.md\n{article_doc}"
    )

    (out / "packet.sha256").write_text(
        json.dumps(
            {
                "base_packet_sha256": hashlib.sha256(base_packet.encode()).hexdigest(),
                "retrieval_docs_sha256": hashlib.sha256(retrieval_docs.encode()).hexdigest(),
                "model": args.model,
            },
            indent=2,
        )
        + "\n"
    )

    arms = ["C", "R", "A", "RA"] * 3
    random.SystemRandom().shuffle(arms)
    key = {f"d{i:02d}": arm for i, arm in enumerate(arms, start=1)}
    (out / "key.json").write_text(json.dumps(key, indent=2) + "\n")

    writer_system = "You are a careful technical writer contributing an atomic theory note to a knowledge base."

    def run_writer(item: tuple[str, str]) -> str:
        name, arm = item
        parts = [COMMISSION]
        if "A" in arm:
            parts.append(ALLOCATION_NUDGE)
        parts.append(base_packet)
        if "R" in arm:
            parts.append(retrieval_docs)
        return call_model(out, name, args.model, writer_system, "\n\n".join(parts))

    with concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
        list(pool.map(run_writer, key.items()))

    scorer_system = "You independently score anonymous technical drafts against a fixed rubric."

    def run_scorer(idx: int) -> str:
        ids = list(key)
        random.SystemRandom().shuffle(ids)
        bundle = "\n\n".join(f"=== {nid} ===\n{(out / f'{nid}.txt').read_text()}" for nid in ids)
        return call_model(out, f"scorer{idx}", args.model, scorer_system, f"{RUBRIC}\n\n{bundle}")

    with concurrent.futures.ThreadPoolExecutor(2) as pool:
        list(pool.map(run_scorer, [1, 2]))


if __name__ == "__main__":
    main()
