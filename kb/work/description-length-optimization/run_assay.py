#!/usr/bin/env python3
"""Generate and score the first description-length retrieval assay.

The script is intentionally workshop-local.  It builds candidate sets from the
live Commonplace corpus, preserving incumbent distractor descriptions while
substituting a controlled target description from cases.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import subprocess
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CORPUS_ROOTS = ("kb/notes", "kb/reference", "kb/instructions", "kb/sources")
ALLOWANCES = (120, 160, 200, 250, 300)
SCALES = (5, 20, 80)
LARGE_CASES = {"pointer_design", "representational_form", "adr_025", "trajectory_memory"}
TOKEN_RE = re.compile(r"[a-z0-9]+")


def frontmatter_value(text: str, key: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    match = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", text[4:end], re.MULTILINE)
    if not match:
        return None
    value = match.group(1)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def title_value(text: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def tokens(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def corpus() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for root_name in CORPUS_ROOTS:
        for path in (ROOT / root_name).rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            description = frontmatter_value(text, "description")
            title = title_value(text)
            if not description or not title:
                continue
            relative = path.relative_to(ROOT).as_posix()
            result[relative] = {
                "path": relative,
                "title": title,
                "description": description,
                "sha256": hashlib.sha256(text.encode()).hexdigest(),
            }
    return result


def rank_distractors(task: str, target: str, items: dict[str, dict[str, str]]) -> list[str]:
    query = Counter(tokens(task))
    documents = {
        path: Counter(tokens(f"{item['path']} {item['title']} {item['description']}"))
        for path, item in items.items()
        if path != target
    }
    document_frequency: Counter[str] = Counter()
    for document in documents.values():
        document_frequency.update(document.keys())
    count = len(documents)

    def score(path: str) -> tuple[float, str]:
        document = documents[path]
        value = 0.0
        for term, query_frequency in query.items():
            if term not in document:
                continue
            inverse_frequency = math.log((count + 1) / (document_frequency[term] + 1)) + 1
            value += query_frequency * (1 + math.log(document[term])) * inverse_frequency
        return (-value, path)

    return sorted(documents, key=score)


def pointer(item: dict[str, str], description: str | None = None) -> str:
    return f"{item['path']} — {item['title']} — {description or item['description']}"


def prompt_text(trials: list[dict[str, object]]) -> str:
    lines = [
        "You are evaluating retrieval pointers for a knowledge base.",
        "Use only the tasks and pointer lists below. Do not open files, search, or use tools.",
        "For each trial, select every artifact you would open to answer the task. Opening has a cost: select a pointer only when its title/path/description makes it plausibly necessary. Abstention is allowed.",
        "Return one decision for every trial_id. In selected, copy the exact path strings before the first em dash. Confidence concerns whether your selections contain all necessary artifacts.",
        "",
    ]
    for trial in trials:
        lines.extend((f"TRIAL {trial['trial_id']}", f"Task: {trial['task']}", "Pointers:"))
        for value in trial["pointers"]:
            lines.append(f"- {value}")
        lines.append("")
    return "\n".join(lines)


def generate() -> None:
    cases = json.loads((HERE / "cases.json").read_text())["cases"]
    items = corpus()
    generated = HERE / "generated"
    prompts = generated / "prompts"
    results = generated / "results"
    prompts.mkdir(parents=True, exist_ok=True)
    results.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, object] = {
        "schema_version": 1,
        "corpus_roots": list(CORPUS_ROOTS),
        "corpus_size": len(items),
        "candidate_selection": "BM25-like lexical overlap with task; target inserted after distractor ranking",
        "description_design": "target-only substitution; distractors use incumbent descriptions",
        "token_measurement": "ceil(UTF-8 character count / 4), reported only as an estimate because the evaluator tokenizer is unavailable",
        "batches": [],
    }
    case_by_id = {case["id"]: case for case in cases}
    for case in cases:
        target = case["path"]
        if target not in items:
            raise SystemExit(f"Missing target: {target}")
        case["artifact_sha256"] = items[target]["sha256"]
        for allowance in ALLOWANCES:
            value = case["variants"][str(allowance)]
            if len(value) > allowance:
                raise SystemExit(f"{case['id']} {allowance}: {len(value)} characters")

    for scale in SCALES:
        repetitions = (1, 2) if scale < 80 else (1,)
        active_cases = cases if scale < 80 else [case for case in cases if case["id"] in LARGE_CASES]
        batch_size = 10 if scale < 80 else 2
        for allowance in ALLOWANCES:
            for repetition in repetitions:
                trials = []
                for case in active_cases:
                    target = case["path"]
                    paths = rank_distractors(case["task"], target, items)[: scale - 1] + [target]
                    seed_material = f"{case['id']}:{scale}:{allowance}:{repetition}".encode()
                    seed = int.from_bytes(hashlib.sha256(seed_material).digest()[:8], "big")
                    random.Random(seed).shuffle(paths)
                    variant = case["variants"][str(allowance)]
                    values = [pointer(items[path], variant if path == target else None) for path in paths]
                    trials.append(
                        {
                            "trial_id": f"{case['id']}-s{scale}-a{allowance}-r{repetition}",
                            "case_id": case["id"],
                            "task": case["task"],
                            "target": target,
                            "allowance": allowance,
                            "variant_characters": len(variant),
                            "variant_bytes": len(variant.encode()),
                            "pointer_characters": sum(len(value) for value in values),
                            "pointer_bytes": sum(len(value.encode()) for value in values),
                            "pointer_token_estimate": math.ceil(sum(len(value) for value in values) / 4),
                            "pointers": values,
                        }
                    )
                for offset in range(0, len(trials), batch_size):
                    batch_trials = trials[offset : offset + batch_size]
                    batch_id = f"s{scale}-a{allowance}-r{repetition}-b{offset // batch_size + 1}"
                    prompt_path = prompts / f"{batch_id}.txt"
                    result_path = results / f"{batch_id}.json"
                    prompt_path.write_text(prompt_text(batch_trials), encoding="utf-8")
                    manifest["batches"].append(
                        {
                            "batch_id": batch_id,
                            "prompt": prompt_path.relative_to(HERE).as_posix(),
                            "result": result_path.relative_to(HERE).as_posix(),
                            "trials": [{key: value for key, value in trial.items() if key != "pointers" and key != "task"} for trial in batch_trials],
                        }
                    )
    manifest["cases"] = [
        {
            "id": case["id"],
            "path": case["path"],
            "artifact_class": case["artifact_class"],
            "title_strength": case["title_strength"],
            "artifact_sha256": case["artifact_sha256"],
        }
        for case in cases
    ]
    (generated / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"generated {len(manifest['batches'])} batches, {sum(len(batch['trials']) for batch in manifest['batches'])} trials")


def score() -> None:
    manifest = json.loads((HERE / "generated/manifest.json").read_text())
    cases = {case["id"]: case for case in json.loads((HERE / "cases.json").read_text())["cases"]}
    rows = []
    missing = []
    for batch in manifest["batches"]:
        result_path = HERE / batch["result"]
        if not result_path.exists():
            missing.append(batch["batch_id"])
            continue
        result = json.loads(result_path.read_text())
        decisions = {item["trial_id"]: item for item in result["decisions"]}
        for trial in batch["trials"]:
            decision = decisions.get(trial["trial_id"])
            if decision is None:
                raise SystemExit(f"Missing decision {trial['trial_id']} in {result_path}")
            selected = decision["selected"]
            target_selected = trial["target"] in selected
            irrelevant = sum(path != trial["target"] for path in selected)
            rows.append(
                {
                    **trial,
                    "artifact_class": cases[trial["case_id"]]["artifact_class"],
                    "title_strength": cases[trial["case_id"]]["title_strength"],
                    "target_selected": target_selected,
                    "false_skip": not target_selected,
                    "irrelevant_opens": irrelevant,
                    "selected_count": len(selected),
                    "precision": (1 / len(selected)) if target_selected and selected else 0,
                    "confidence": decision["confidence"],
                }
            )
    if missing:
        raise SystemExit(f"Missing {len(missing)} result files: {', '.join(missing[:5])}")

    groups: dict[tuple[int, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[(row["allowance"], int(row["trial_id"].split("-s")[1].split("-")[0]))].append(row)
    summary = []
    for (allowance, scale), values in sorted(groups.items(), key=lambda pair: (pair[0][1], pair[0][0])):
        count = len(values)
        summary.append(
            {
                "scale": scale,
                "allowance": allowance,
                "trials": count,
                "recall": sum(row["target_selected"] for row in values) / count,
                "false_skip_rate": sum(row["false_skip"] for row in values) / count,
                "mean_irrelevant_opens": sum(row["irrelevant_opens"] for row in values) / count,
                "mean_precision": sum(row["precision"] for row in values) / count,
                "mean_pointer_characters": sum(row["pointer_characters"] for row in values) / count,
                "mean_pointer_bytes": sum(row["pointer_bytes"] for row in values) / count,
                "mean_pointer_token_estimate": sum(row["pointer_token_estimate"] for row in values) / count,
            }
        )
    output = {"trials": rows, "summary": summary}
    (HERE / "generated/scored-results.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


def evaluate(jobs: int) -> None:
    manifest = json.loads((HERE / "generated/manifest.json").read_text())
    log_dir = HERE / "generated/logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    def run_batch(batch: dict[str, object]) -> tuple[str, int, str]:
        prompt_path = HERE / str(batch["prompt"])
        result_path = HERE / str(batch["result"])
        if result_path.exists():
            try:
                json.loads(result_path.read_text())
                return str(batch["batch_id"]), 0, "already complete"
            except json.JSONDecodeError:
                pass
        command = [
            "codex",
            "exec",
            "--ephemeral",
            "-C",
            str(ROOT),
            "--sandbox",
            "read-only",
            "--output-schema",
            str(HERE / "selection-schema.json"),
            "-o",
            str(result_path),
            "-",
        ]
        completed = subprocess.run(
            command,
            input=prompt_path.read_text(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=300,
        )
        log_path = log_dir / f"{batch['batch_id']}.log"
        log_path.write_text(completed.stdout)
        return str(batch["batch_id"]), completed.returncode, completed.stdout[-500:]

    failures = []
    with ThreadPoolExecutor(max_workers=jobs) as executor:
        futures = [executor.submit(run_batch, batch) for batch in manifest["batches"]]
        for index, future in enumerate(as_completed(futures), 1):
            batch_id, returncode, tail = future.result()
            print(f"[{index}/{len(futures)}] {batch_id}: {returncode}", flush=True)
            if returncode:
                failures.append((batch_id, tail))
    if failures:
        for batch_id, tail in failures:
            print(f"FAILED {batch_id}\n{tail}")
        raise SystemExit(f"{len(failures)} evaluator batches failed")


def fidelity(jobs: int) -> None:
    cases = json.loads((HERE / "cases.json").read_text())["cases"]
    result_dir = HERE / "generated/fidelity"
    log_dir = HERE / "generated/fidelity-logs"
    result_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    def run_case(case: dict[str, object]) -> tuple[str, int, str]:
        result_path = result_dir / f"{case['id']}.json"
        prompt = (
            f"Review the five description variants for case {case['id']} in "
            "kb/work/description-length-optimization/cases.json against the full target artifact "
            f"{case['path']}. Judge only semantic fidelity: whether each variant is truthful, "
            "preserves the artifact scope relevant to its retrieval task, and introduces no unsupported claim. "
            "A shorter variant may omit detail and still pass. Return exactly five reviews. Do not edit files."
        )
        command = [
            "codex",
            "exec",
            "--ephemeral",
            "-C",
            str(ROOT),
            "--sandbox",
            "read-only",
            "--output-schema",
            str(HERE / "fidelity-schema.json"),
            "-o",
            str(result_path),
            prompt,
        ]
        completed = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=300,
        )
        (log_dir / f"{case['id']}.log").write_text(completed.stdout)
        return str(case["id"]), completed.returncode, completed.stdout[-500:]

    failures = []
    with ThreadPoolExecutor(max_workers=jobs) as executor:
        futures = [executor.submit(run_case, case) for case in cases]
        for index, future in enumerate(as_completed(futures), 1):
            case_id, returncode, tail = future.result()
            print(f"[{index}/{len(futures)}] {case_id}: {returncode}", flush=True)
            if returncode:
                failures.append((case_id, tail))
    if failures:
        for case_id, tail in failures:
            print(f"FAILED {case_id}\n{tail}")
        raise SystemExit(f"{len(failures)} fidelity reviews failed")
    reviews = []
    for case in cases:
        reviews.extend(json.loads((result_dir / f"{case['id']}.json").read_text())["reviews"])
    (HERE / "generated/fidelity-review.json").write_text(json.dumps({"reviews": reviews}, indent=2) + "\n")
    print(f"aggregated {len(reviews)} fidelity judgments")


def downstream_generate() -> None:
    retrieval_manifest = json.loads((HERE / "generated/manifest.json").read_text())
    definitions = json.loads((HERE / "downstream-cases.json").read_text())["cases"]
    selected_by_trial: dict[str, list[str]] = {}
    for batch in retrieval_manifest["batches"]:
        result = json.loads((HERE / str(batch["result"])).read_text())
        selected_by_trial.update({decision["trial_id"]: decision["selected"] for decision in result["decisions"]})
    output_dir = HERE / "generated/downstream"
    prompt_dir = output_dir / "prompts"
    result_dir = output_dir / "results"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    result_dir.mkdir(parents=True, exist_ok=True)
    batches = []
    for allowance in ALLOWANCES:
        for repetition in (1, 2):
            trials = []
            lines = [
                "Answer each question using only the loaded artifact excerpts. Do not open files, search, or use tools.",
                "If the excerpts do not support an answer, say that the evidence is insufficient. Return one answer for every trial_id.",
                "",
            ]
            for case_id, definition in definitions.items():
                source_trial_id = f"{case_id}-s20-a{allowance}-r{repetition}"
                trial_id = f"downstream-{source_trial_id}"
                selected = selected_by_trial[source_trial_id]
                loaded = []
                lines.extend((f"TRIAL {trial_id}", f"Question: {definition['question']}", "Loaded excerpts:"))
                for selected_path in selected:
                    body = (ROOT / selected_path).read_text(errors="replace")[:15000]
                    loaded.append({"path": selected_path, "characters": len(body)})
                    lines.extend((f"===== {selected_path} =====", body))
                if not selected:
                    lines.append("(none)")
                lines.append("")
                trials.append(
                    {
                        "trial_id": trial_id,
                        "source_trial_id": source_trial_id,
                        "case_id": case_id,
                        "allowance": allowance,
                        "repetition": repetition,
                        "selected": selected,
                        "loaded": loaded,
                    }
                )
            batch_id = f"downstream-a{allowance}-r{repetition}"
            prompt_path = prompt_dir / f"{batch_id}.txt"
            result_path = result_dir / f"{batch_id}.json"
            prompt_path.write_text("\n".join(lines))
            batches.append(
                {
                    "batch_id": batch_id,
                    "prompt": prompt_path.relative_to(HERE).as_posix(),
                    "result": result_path.relative_to(HERE).as_posix(),
                    "trials": trials,
                }
            )
    (output_dir / "manifest.json").write_text(json.dumps({"body_excerpt_limit": 15000, "batches": batches}, indent=2) + "\n")
    print(f"generated {len(batches)} downstream batches and {sum(len(batch['trials']) for batch in batches)} trials")


def downstream_evaluate(jobs: int) -> None:
    manifest = json.loads((HERE / "generated/downstream/manifest.json").read_text())
    log_dir = HERE / "generated/downstream/logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    def run_batch(batch: dict[str, object]) -> tuple[str, int, str]:
        result_path = HERE / str(batch["result"])
        command = [
            "codex", "exec", "--ephemeral", "-C", str(ROOT), "--sandbox", "read-only",
            "--output-schema", str(HERE / "downstream-schema.json"), "-o", str(result_path), "-",
        ]
        completed = subprocess.run(
            command,
            input=(HERE / str(batch["prompt"])).read_text(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=300,
        )
        (log_dir / f"{batch['batch_id']}.log").write_text(completed.stdout)
        return str(batch["batch_id"]), completed.returncode, completed.stdout[-500:]

    failures = []
    with ThreadPoolExecutor(max_workers=jobs) as executor:
        futures = [executor.submit(run_batch, batch) for batch in manifest["batches"]]
        for index, future in enumerate(as_completed(futures), 1):
            batch_id, returncode, tail = future.result()
            print(f"[{index}/{len(futures)}] {batch_id}: {returncode}", flush=True)
            if returncode:
                failures.append((batch_id, tail))
    if failures:
        for batch_id, tail in failures:
            print(f"FAILED {batch_id}\n{tail}")
        raise SystemExit(f"{len(failures)} downstream batches failed")


def downstream_score() -> None:
    manifest = json.loads((HERE / "generated/downstream/manifest.json").read_text())
    definitions = json.loads((HERE / "downstream-cases.json").read_text())["cases"]
    rows = []
    for batch in manifest["batches"]:
        answers = {
            answer["trial_id"]: answer["answer"]
            for answer in json.loads((HERE / str(batch["result"])).read_text())["answers"]
        }
        for trial in batch["trials"]:
            answer = answers[trial["trial_id"]]
            folded = " ".join(TOKEN_RE.findall(answer.lower()))
            groups = definitions[trial["case_id"]]["required_term_groups"]
            passed = all(
                any(" ".join(TOKEN_RE.findall(term.lower())) in folded for term in group)
                for group in groups
            )
            rows.append({**trial, "answer": answer, "success": passed})
    summary = []
    for allowance in ALLOWANCES:
        values = [row for row in rows if row["allowance"] == allowance]
        summary.append(
            {
                "allowance": allowance,
                "trials": len(values),
                "success_rate": sum(row["success"] for row in values) / len(values),
                "body_characters_loaded": sum(sum(item["characters"] for item in row["loaded"]) for row in values),
            }
        )
    (HERE / "generated/downstream/scored-results.json").write_text(json.dumps({"trials": rows, "summary": summary}, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=("generate", "evaluate", "fidelity", "score", "downstream-generate", "downstream-evaluate", "downstream-score"),
    )
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()
    if args.command == "generate":
        generate()
    elif args.command == "evaluate":
        evaluate(args.jobs)
    elif args.command == "fidelity":
        fidelity(args.jobs)
    elif args.command == "downstream-generate":
        downstream_generate()
    elif args.command == "downstream-evaluate":
        downstream_evaluate(args.jobs)
    elif args.command == "downstream-score":
        downstream_score()
    else:
        score()


if __name__ == "__main__":
    main()
