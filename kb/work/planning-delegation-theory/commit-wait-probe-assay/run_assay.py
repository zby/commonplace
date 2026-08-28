"""Build and score the workshop-local commit/wait/probe assay."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
INSTRUCTION = ROOT / "kb/instructions/invert-solution-shaped-requests.md"
EXPECTED_INSTRUCTION_SHA256 = "08b7779e12b8cc45b0fd78dc0784f187a1e9f7a88b20c2c614b34daf0cd08733"
SEED = 202608281

CONTROL_COST_TEXT = """Prefer the least-committing route that preserves learning. Treat new skills, commands, validators, types, and indexes as high-maintenance surfaces; require stronger evidence for them than for a log entry, workshop, note, or instruction."""

TREATMENT_COST_TEXT = """Choose the smallest sufficient route whose commitment, delay, information, and
maintenance costs are justified. Treat new skills, commands, validators, types,
and indexes as high-maintenance surfaces; require stronger evidence for them
than for a log entry, workshop, note, or instruction. Do not prefer delay merely
because it commits less.

Run the following branch only when the proposed solution would destroy a
meaningful alternative or create dependencies that are costly to reverse.
Otherwise select the route directly from the evidence above.

Compare four moves:

- `commit now` -- current evidence discriminates and the expected cost of
  waiting, fragmentation, or lost coordination warrants commitment
- `passively wait` -- name an exogenous observation that can change the choice
- `run a bounded probe` -- name limited work whose possible output can change
  the choice without committing the whole solution
- `decline or do nothing` -- the problem or expected benefit does not warrant
  commitment, waiting, or a probe

For `passively wait` or `run a bounded probe`, name the alternative being
preserved, the observation or possible output that can change the decision,
whether the opportunity will remain available, and the current benefit,
coordination value, or opportunity lost by waiting. Give the move a review,
stop, or follow-on decision rule. If no later result can change the choice,
waiting or probing is not an information-producing reason to defer it."""

CONTROL_VERIFY_TEXT = """- The recommended route is the smallest sufficient outcome.
- Any implementation step follows from the problem, not from momentum behind the initial solution."""

TREATMENT_VERIFY_TEXT = """- The recommended route is the smallest sufficient outcome.
- A costly-to-reverse commitment was compared with waiting or a bounded probe
  only when a meaningful alternative can remain live.
- Any deferral names discriminating evidence and a return to decision.
- Any implementation step follows from the problem, not from momentum behind the initial solution."""

CONDITION_MAP = {
    "condition-2c": "control",
    "condition-9a": "treatment",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def operative_instruction() -> str:
    text = INSTRUCTION.read_text(encoding="utf-8")
    actual = sha256_text(text)
    if actual != EXPECTED_INSTRUCTION_SHA256:
        raise SystemExit(f"instruction drift: expected {EXPECTED_INSTRUCTION_SHA256}, got {actual}")
    if not text.startswith("---\n"):
        raise SystemExit("instruction frontmatter missing")
    text = text.split("\n---\n", 1)[1].lstrip()
    text = text.split("\n---\n\nRelevant Notes:", 1)[0].rstrip() + "\n"
    return text


def variant_text(kind: str) -> str:
    text = operative_instruction()
    if TREATMENT_COST_TEXT not in text or TREATMENT_VERIFY_TEXT not in text:
        raise SystemExit("treatment blocks not found in current instruction")
    if kind == "treatment":
        return text
    if kind == "control":
        return text.replace(TREATMENT_COST_TEXT, CONTROL_COST_TEXT).replace(
            TREATMENT_VERIFY_TEXT, CONTROL_VERIFY_TEXT
        )
    raise ValueError(kind)


def packet_text(packet_id: str, condition_id: str, case: dict[str, object], response_path: str) -> str:
    instruction = variant_text(CONDITION_MAP[condition_id])
    scenario = case["scenario"]
    return f"""# Planning assay packet {packet_id}

Use only this packet. Do not inspect other repository files, run searches, read
links from the instruction, or use conversation history. Do not delegate or
spawn another agent. Treat the case as complete and each stated fact as true.

Apply the operative instruction to the case, but write only the JSON response
specified below. Choose the recommendation the instruction warrants; do not
maximize deferral, option analysis, or detail.

## Operative instruction

{instruction}
## Case

**{case['title']}**

{scenario}

## Sole output

Write one JSON object to `{response_path}` with exactly these keys:

```json
{{
  "packet_id": "{packet_id}",
  "decision_class": "direct | commit | wait | probe | decline",
  "recommended_next_move": "at most 45 words",
  "option_analysis_used": true,
  "preserved_alternative": "string or null",
  "discriminating_input": "string or null",
  "opportunity_status": "string or null",
  "delay_or_probe_cost": "string or null",
  "return_rule": "string or null",
  "reason": "at most 70 words"
}}
```

Use JSON `null`, not the string `"null"`. `direct` means selecting the route
without invoking the costly-commitment comparison. `commit` means the
costly-commitment comparison applies and current action wins. `wait` means
passive waiting for an exogenous observation. `probe` means bounded active work
whose output can change the choice. `decline` includes do nothing or removing
an unwarranted future item.

Modify no other file. End your turn after the JSON file exists.
"""


def generate() -> None:
    cases = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))["cases"]
    generated = HERE / "generated"
    packets = generated / "packets"
    responses = generated / "responses"
    packets.mkdir(parents=True, exist_ok=True)
    responses.mkdir(parents=True, exist_ok=True)
    rows = []
    for condition_id, condition_kind in CONDITION_MAP.items():
        for case in cases:
            material = f"{SEED}:{condition_id}:{case['id']}".encode()
            packet_id = "trial-" + hashlib.sha256(material).hexdigest()[:12]
            packet_rel = f"kb/work/planning-delegation-theory/commit-wait-probe-assay/generated/packets/{packet_id}.md"
            response_rel = f"kb/work/planning-delegation-theory/commit-wait-probe-assay/generated/responses/{packet_id}.json"
            text = packet_text(packet_id, condition_id, case, response_rel)
            (ROOT / packet_rel).write_text(text, encoding="utf-8")
            rows.append(
                {
                    "packet_id": packet_id,
                    "condition_id": condition_id,
                    "condition_kind": condition_kind,
                    "case_id": case["id"],
                    "packet_path": packet_rel,
                    "packet_sha256": sha256_text(text),
                    "response_path": response_rel,
                }
            )
    random.Random(SEED).shuffle(rows)
    codebook = {
        "schema_version": 1,
        "seed": SEED,
        "condition_map": CONDITION_MAP,
        "instruction_sha256": EXPECTED_INSTRUCTION_SHA256,
        "variant_sha256": {
            kind: sha256_text(variant_text(kind)) for kind in ("control", "treatment")
        },
        "trials": rows,
    }
    write_json(generated / "codebook.json", codebook)
    write_json(
        generated / "dispatch.json",
        {
            "schema_version": 1,
            "trials": [
                {key: row[key] for key in ("packet_id", "packet_path", "packet_sha256", "response_path")}
                for row in rows
            ],
        },
    )
    print(f"generated {len(rows)} packets")


def load_responses() -> tuple[dict[str, object], list[dict[str, object]]]:
    codebook = json.loads((HERE / "generated/codebook.json").read_text(encoding="utf-8"))
    results = []
    missing = []
    for trial in codebook["trials"]:
        packet_path = ROOT / trial["packet_path"]
        if sha256_text(packet_path.read_text(encoding="utf-8")) != trial["packet_sha256"]:
            raise SystemExit(f"packet drift: {trial['packet_path']}")
        response_path = ROOT / trial["response_path"]
        if not response_path.exists():
            missing.append(trial["packet_id"])
            continue
        response = json.loads(response_path.read_text(encoding="utf-8"))
        if response.get("packet_id") != trial["packet_id"]:
            raise SystemExit(f"response packet mismatch: {trial['response_path']}")
        results.append({**trial, "response": response})
    if missing:
        raise SystemExit(f"missing {len(missing)} responses: {', '.join(missing)}")
    return codebook, results


def build_judge() -> None:
    _, results = load_responses()
    cases = {item["id"]: item for item in json.loads((HERE / "cases.json").read_text())["cases"]}
    rubric = json.loads((HERE / "rubric.json").read_text(encoding="utf-8"))["cases"]
    anonymized = []
    for item in results:
        judge_id = "item-" + hashlib.sha256(f"judge:{SEED}:{item['packet_id']}".encode()).hexdigest()[:12]
        anonymized.append(
            {
                "judge_id": judge_id,
                "case": cases[item["case_id"]],
                "expected": rubric[item["case_id"]],
                "response": item["response"],
            }
        )
    random.Random(SEED + 1).shuffle(anonymized)
    judge_output = "kb/work/planning-delegation-theory/commit-wait-probe-assay/generated/judge-output.json"
    prompt = f"""# Blind judge packet

Use only this file. Do not inspect other repository files, search, use
conversation history, or delegate. The condition identities and mapping are
withheld. Evaluate every item independently against its stated expected posture
and requirements; do not compare writing style across items.

For each item, score:

- `posture_correct`: response decision class equals the expected class.
- `option_activation_correct`: response option-analysis flag matches the
  expected flag and the reason does not contradict it.
- `requirements_met`: number of listed requirements visibly satisfied.
- `false_deferral`: response waits or probes without a discriminating input, a
  still-live alternative, and a return rule.
- `unnecessary_overhead`: response adds commitment comparison, waiting, or a
  probe to the cheap reversible case.
- `rationale`: at most 60 words, using only the case and response.

Write one JSON object to `{judge_output}`:

```json
{{
  "items": [
    {{
      "judge_id": "item id",
      "posture_correct": true,
      "option_activation_correct": true,
      "requirements_met": 0,
      "requirement_count": 0,
      "false_deferral": false,
      "unnecessary_overhead": false,
      "rationale": "..."
    }}
  ],
  "cross_item_notes": "at most 100 words; no guessed condition mapping"
}}
```

Return exactly one item for every supplied `judge_id`. Modify no other file.
End your turn after the JSON file exists.

## Items

```json
{json.dumps(anonymized, indent=2, ensure_ascii=False)}
```
"""
    path = HERE / "generated/judge-prompt.md"
    path.write_text(prompt, encoding="utf-8")
    packet_by_response = {json.dumps(item["response"], sort_keys=True): item["packet_id"] for item in results}
    write_json(
        HERE / "generated/judge-codebook.json",
        {
            "schema_version": 1,
            "items": [
                {
                    "judge_id": item["judge_id"],
                    "packet_id": packet_by_response[json.dumps(item["response"], sort_keys=True)],
                }
                for item in anonymized
            ],
        },
    )
    print(f"built judge packet with {len(anonymized)} items")


def score() -> None:
    codebook, results = load_responses()
    rubric = json.loads((HERE / "rubric.json").read_text(encoding="utf-8"))["cases"]
    judge = json.loads((HERE / "generated/judge-output.json").read_text(encoding="utf-8"))
    judge_codebook = json.loads((HERE / "generated/judge-codebook.json").read_text(encoding="utf-8"))
    packet_by_judge = {item["judge_id"]: item["packet_id"] for item in judge_codebook["items"]}
    judgments = {packet_by_judge[item["judge_id"]]: item for item in judge["items"]}
    rows = []
    for item in results:
        expected = rubric[item["case_id"]]
        response = item["response"]
        judgment = judgments.get(item["packet_id"])
        if judgment is None:
            raise SystemExit(f"missing judgment for {item['packet_id']}")
        rows.append(
            {
                "packet_id": item["packet_id"],
                "condition_id": item["condition_id"],
                "condition_kind": item["condition_kind"],
                "case_id": item["case_id"],
                "expected": expected["expected"],
                "observed": response["decision_class"],
                "deterministic_posture_correct": response["decision_class"] == expected["expected"],
                "response": response,
                "judgment": judgment,
            }
        )
    summary = {}
    for kind in ("control", "treatment"):
        arm = [row for row in rows if row["condition_kind"] == kind]
        summary[kind] = {
            "trials": len(arm),
            "postures_correct": sum(row["deterministic_posture_correct"] for row in arm),
            "judge_postures_correct": sum(row["judgment"]["posture_correct"] for row in arm),
            "option_activation_correct": sum(row["judgment"]["option_activation_correct"] for row in arm),
            "requirements_met": sum(row["judgment"]["requirements_met"] for row in arm),
            "requirements_total": sum(row["judgment"]["requirement_count"] for row in arm),
            "false_deferrals": sum(row["judgment"]["false_deferral"] for row in arm),
            "unnecessary_overhead": sum(row["judgment"]["unnecessary_overhead"] for row in arm),
        }
    difference = summary["treatment"]["postures_correct"] - summary["control"]["postures_correct"]
    control_by_case = {row["case_id"]: row for row in rows if row["condition_kind"] == "control"}
    treatment_by_case = {row["case_id"]: row for row in rows if row["condition_kind"] == "treatment"}
    new_safety_misses = [
        case_id
        for case_id, spec in rubric.items()
        if spec["safety_critical"]
        and control_by_case[case_id]["deterministic_posture_correct"]
        and not treatment_by_case[case_id]["deterministic_posture_correct"]
    ]
    false_deferral_delta = summary["treatment"]["false_deferrals"] - summary["control"]["false_deferrals"]
    if difference >= 2 and not new_safety_misses and false_deferral_delta <= 0:
        signal = "positive-directional"
    elif difference <= -2 or new_safety_misses or false_deferral_delta > 0:
        signal = "negative-directional"
    else:
        signal = "inconclusive"
    write_json(
        HERE / "generated/scored-results.json",
        {
            "schema_version": 1,
            "source_instruction_sha256": codebook["instruction_sha256"],
            "variant_sha256": codebook["variant_sha256"],
            "summary": summary,
            "primary_difference": difference,
            "new_safety_misses": new_safety_misses,
            "false_deferral_delta": false_deferral_delta,
            "signal": signal,
            "judge_cross_item_notes": judge.get("cross_item_notes"),
            "trials": rows,
        },
    )
    print(json.dumps({"summary": summary, "signal": signal}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("generate", "build-judge", "score"))
    args = parser.parse_args()
    {"generate": generate, "build-judge": build_judge, "score": score}[args.action]()


if __name__ == "__main__":
    main()
