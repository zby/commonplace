#!/usr/bin/env python3
"""Towers of Hanoi — LLM bookkeeping stress test.

Two conditions, both run by Haiku:
  1. Flat prompt — plain English instruction
  2. OpenProse — prose.md VM spec + hanoi.prose program

Compares outputs against the known-correct 15-move sequence for 4 disks.
"""

import json
import sys
import re
from pathlib import Path

import anthropic

MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 4096

# The correct sequence for hanoi(4, A, C, B)
CORRECT_MOVES = [
    (1, "A", "B"),
    (2, "A", "C"),
    (1, "B", "C"),
    (3, "A", "B"),
    (1, "C", "A"),
    (2, "C", "B"),
    (1, "A", "B"),
    (4, "A", "C"),
    (1, "B", "C"),
    (2, "B", "A"),
    (1, "C", "A"),
    (3, "B", "C"),
    (1, "A", "B"),
    (2, "A", "C"),
    (1, "B", "C"),
]


FLAT_PROMPT = """\
Solve the Towers of Hanoi problem for 4 disks.

Pegs are named A, B, and C.
- All 4 disks start on peg A (disk 1 is smallest, disk 4 is largest).
- Goal: move all disks to peg C.
- Rules: move one disk at a time; never place a larger disk on a smaller one.
- Use peg B as auxiliary.

List every move in order, one per line, in this exact format:
MOVE disk <n>: <source> → <target>

Then state the total number of moves.
"""


def build_openprose_prompt():
    """Build the OpenProse condition prompt: VM spec + program."""
    here = Path(__file__).parent
    repo = here / "../../related-systems/prose/skills/open-prose"

    prose_md = (repo / "prose.md").read_text()
    hanoi_prose = (here / "hanoi.prose").read_text()

    return f"""\
You are the OpenProse VM. Read the following VM specification, then execute the program that follows.

=== VM SPECIFICATION (prose.md) ===

{prose_md}

=== PROGRAM (hanoi.prose) ===

{hanoi_prose}

=== INSTRUCTIONS ===

Execute this program. You ARE the VM — follow the execution model from prose.md.
Since this is a simple experiment, use in-context state (narration protocol) rather than filesystem state.
For each session statement, don't actually spawn a subagent — just execute it yourself inline and report the output.
Track the call stack and variable bindings as you go.

After execution, list all moves made in order, one per line, in this exact format:
MOVE disk <n>: <source> → <target>

Then state the total number of moves.
"""


def parse_moves(text):
    """Extract moves from LLM output."""
    pattern = r"MOVE disk (\d+):\s*([A-C])\s*(?:→|->|-->)\s*([A-C])"
    moves = []
    for m in re.finditer(pattern, text):
        moves.append((int(m.group(1)), m.group(2), m.group(3)))
    return moves


def score_moves(moves):
    """Compare extracted moves against correct sequence."""
    correct_count = len(CORRECT_MOVES)
    actual_count = len(moves)

    # Count positional matches
    matches = 0
    for i, (actual, expected) in enumerate(zip(moves, CORRECT_MOVES)):
        if actual == expected:
            matches += 1

    # Find first divergence
    first_error = None
    for i, (actual, expected) in enumerate(zip(moves, CORRECT_MOVES)):
        if actual != expected:
            first_error = i
            break
    if first_error is None and actual_count != correct_count:
        first_error = min(actual_count, correct_count)

    return {
        "expected_moves": correct_count,
        "actual_moves": actual_count,
        "count_correct": actual_count == correct_count,
        "positional_matches": matches,
        "positional_accuracy": matches / correct_count if correct_count else 0,
        "perfect": moves == CORRECT_MOVES,
        "first_error_at": first_error,
    }


def run_condition(client, name, prompt):
    """Run one experimental condition."""
    print(f"\n{'='*60}")
    print(f"CONDITION: {name}")
    print(f"{'='*60}")

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text
    print(f"\n--- Raw output ---\n{text}\n--- End output ---")

    moves = parse_moves(text)
    scores = score_moves(moves)

    print(f"\n--- Scoring ---")
    print(f"Moves found:          {scores['actual_moves']} (expected {scores['expected_moves']})")
    print(f"Count correct:        {scores['count_correct']}")
    print(f"Positional matches:   {scores['positional_matches']}/{scores['expected_moves']}")
    print(f"Positional accuracy:  {scores['positional_accuracy']:.1%}")
    print(f"Perfect:              {scores['perfect']}")
    if scores['first_error_at'] is not None:
        print(f"First error at move:  {scores['first_error_at'] + 1}")
        if scores['first_error_at'] < len(moves) and scores['first_error_at'] < len(CORRECT_MOVES):
            print(f"  Got:      {moves[scores['first_error_at']]}")
            print(f"  Expected: {CORRECT_MOVES[scores['first_error_at']]}")

    return {
        "condition": name,
        "model": MODEL,
        "raw_output": text,
        "parsed_moves": [(d, s, t) for d, s, t in moves],
        "scores": scores,
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        },
    }


def main():
    client = anthropic.Anthropic()

    results = []

    # Condition 1: Flat prompt
    results.append(run_condition(client, "flat-prompt", FLAT_PROMPT))

    # Condition 2: OpenProse
    results.append(run_condition(client, "openprose-vm", build_openprose_prompt()))

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for r in results:
        s = r["scores"]
        print(f"  {r['condition']:20s}  perfect={s['perfect']}  accuracy={s['positional_accuracy']:.0%}  moves={s['actual_moves']}/15  tokens_in={r['usage']['input_tokens']}  tokens_out={r['usage']['output_tokens']}")

    # Save full results
    out_path = Path(__file__).parent / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nFull results saved to {out_path}")


if __name__ == "__main__":
    main()
