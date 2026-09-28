"""One-off: split a retained agentic-analysis result into the partition candidate's members.

Temporary fixture tooling for kb/work/agentic-analysis-output-documents;
delete when that workshop closes. Reads a run's retained result and local
specialist report, writes overview/runtime/memory/epistemic members to an
output directory, and prints set checks: member sizes, declaration
uniqueness, reference resolution, and duplicate quote passages.

Run: uv run python scripts/split_agentic_result_fixture.py <run-id> <out-dir>
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from commonplace.lib.quote_matching import normalize_text, parse_blockquotes

ID_RE = re.compile(r"\b(?:SRC|CMP|OBJ|RTE|CLM|ABS|BAP)-\d+\b")
MEM_RE = re.compile(r"\bMEM-(?:CMP|OBJ|RTE|CLM|ABS|BAP)-\d+\b")
DECL_RE = re.compile(r"^#{3,4} ((?:CMP|OBJ|RTE|CLM|ABS|BAP)-\d+) — ", re.MULTILINE)
QUOTE_BLOCK_RE = re.compile(r"(?:^> .*\n)+^> --- .*\n", re.MULTILINE)
OVERVIEW_SECTIONS = [
    "Run identity", "Boundary and evidence", "Source register", "Lens scoping",
    "Reconciliation", "Bounded synthesis", "Limitations", "Verification and blockers",
]
KINDS = ["Components", "Operative objects", "Routes", "Claims",
         "Evidenced absences", "Behavioral-authority paths"]


def split_frontmatter(text: str) -> tuple[str, str]:
    end = text.index("\n---\n", 4)
    return text[4:end], text[end + 5:]


def sections(body: str, level: str = "## ") -> dict[str, str]:
    out: dict[str, str] = {}
    current = "(preamble)"
    for line in body.splitlines(keepends=True):
        if line.startswith(level) and not line.startswith(level + "#"):
            current = line[len(level):].strip()
            out[current] = ""
        else:
            out[current] = out.get(current, "") + line
    return out


def records(shared: str) -> dict[str, tuple[str, str]]:
    """Map ID -> (kind heading, declaration block) from the Shared records body."""
    out: dict[str, tuple[str, str]] = {}
    kind = None
    block_id = None
    for line in shared.splitlines(keepends=True):
        if line.startswith("### ") and line[4:].strip() in KINDS:
            kind, block_id = line[4:].strip(), None
            continue
        m = DECL_RE.match(line)
        if m:
            block_id = m.group(1)
            out[block_id] = (kind or "?", line)
            continue
        if block_id:
            out[block_id] = (out[block_id][0], out[block_id][1] + line)
    return out


def words(text: str) -> int:
    return len(text.split())


def quotes(text: str) -> list[str]:
    return [normalize_text(c.quote, "code") for c in parse_blockquotes(text) if c.error is None]


def main(argv: list[str]) -> int:
    run_id, out_dir = argv[0], Path(argv[1])
    retained = Path(f"kb/reports/retained/agentic-system-analysis/{run_id}/result.md")
    report_path = Path(f"kb/reports/state/agentic-system-analysis/{run_id}/memory-report.md")
    result = retained.read_text(encoding="utf-8")
    report = report_path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(result)
    secs = sections(body)
    title = body.split("\n", 1)[0]

    # 1. proposal mapping from Reconciliation
    recon = secs.get("Reconciliation", "")
    mapping = dict(re.findall(r"\|\s*`?(MEM-[A-Z]+-\d+)`?\s*\|\s*((?:CMP|OBJ|RTE|CLM|ABS|BAP)-\d+)\s*\|", recon))
    mapping.update(re.findall(r"`(MEM-[A-Z]+-\d+)` became ((?:CMP|OBJ|RTE|CLM|ABS|BAP)-\d+)", recon))
    memory_ids = set(mapping.values())
    recs = records(secs["Shared records"])
    runtime_ids = [i for i in recs if i not in memory_ids]

    # 2. members
    identity_fm = "\n".join(l for l in fm.splitlines() if not l.startswith((" ", "memory-comparison")))
    identity_fm = re.sub(r"^type: .*$", "type: types/agentic-system-analysis-overview.md", identity_fm, flags=re.MULTILINE)
    overview = f"---\n{identity_fm}\n---\n{title}\n\n" + "".join(
        f"## {s}\n{secs[s]}" for s in OVERVIEW_SECTIONS if s in secs)
    runtime = ("---\ntype: types/agentic-system-runtime-report.md\n"
               f"run-id: {run_id}\n---\n# Runtime report — {run_id}\n\n"
               f"## Runtime account\n{secs['Runtime account']}## Shared records\n\n")
    for kind in KINDS:
        members = [recs[i][1] for i in runtime_ids if recs[i][0] == kind]
        runtime += f"### {kind}\n\n" + ("".join(members) if members else "none declared in this member.\n\n")
    memory = report
    for mem, canon in sorted(mapping.items(), key=lambda kv: -len(kv[0])):
        memory = re.sub(rf"\b{re.escape(mem)}\b", canon, memory)
    # A seeded canonical record re-declared by the specialist becomes an annotation.
    seeded_redeclared = [i for i in DECL_RE.findall(memory) if i not in memory_ids]
    for i in seeded_redeclared:
        memory = re.sub(rf"^(#{{3,4}}) {i} — ", rf"\1 On {i} — ", memory, flags=re.MULTILINE)
    # A passage the memory member holds is cited, not repeated, by the runtime member.
    memory_quotes = set(quotes(memory))
    removed_from_runtime = 0
    def _dedup(m: re.Match) -> str:
        nonlocal removed_from_runtime
        block = m.group(0)
        if quotes(block) and quotes(block)[0] in memory_quotes:
            removed_from_runtime += 1
            return "(passage retained in the memory member)\n"
        return block
    runtime = QUOTE_BLOCK_RE.sub(_dedup, runtime)
    # coordinator's versions of memory-registered records, appended as amendments
    # The coordinator's version of a memory-registered record is appended as an
    # amendment body under a non-declaring heading; passages the specialist
    # already retained are cited, not repeated.
    amendment_words = 0
    amendments = ""
    for i in recs:
        if i not in memory_ids:
            continue
        body = recs[i][1].split("\n", 1)[1] if "\n" in recs[i][1] else ""
        body = QUOTE_BLOCK_RE.sub(
            lambda m: "(passage retained above)\n" if quotes(m.group(0)) and quotes(m.group(0))[0] in memory_quotes else m.group(0),
            body)
        amendment_words += words(body)
        amendments += f"#### Coordinator amendment to {i}\n\n{body}"
    memory += "\n## Coordinator amendments\n\n" + (amendments or "none\n")
    lens = sections(secs["Lens outputs"], "### ")
    epistemic = ("---\ntype: types/agentic-system-epistemic-report.md\n"
                 f"run-id: {run_id}\n---\n# Epistemic report — {run_id}\n\n" + lens["Epistemic lens"])
    dropped_lens = lens["Memory/context lens"]
    out_dir.mkdir(parents=True, exist_ok=True)
    members_text = {"overview.md": overview, "runtime.md": runtime, "memory.md": memory, "epistemic.md": epistemic}
    for name, text in members_text.items():
        (out_dir / name).write_text(text, encoding="utf-8")
    (out_dir / "dropped-memory-lens.md").write_text(dropped_lens, encoding="utf-8")

    # 3. checks
    decls: dict[str, list[str]] = {}
    for name, text in members_text.items():
        for i in DECL_RE.findall(text):
            decls.setdefault(i, []).append(name)
    src_decl = set(re.findall(r"^\|\s*(SRC-\d+)\s*\|", secs["Source register"], re.MULTILINE))
    duplicates = {i: m for i, m in decls.items() if len(m) > 1}
    unresolved: dict[str, Counter] = {}
    for name, text in members_text.items():
        refs = set(ID_RE.findall(text))
        missing = [r for r in refs if r not in decls and r not in src_decl]
        if missing:
            unresolved[name] = Counter(missing)
    leftover_mem = Counter(MEM_RE.findall(memory))
    q_result, q_report = quotes(result), quotes(report)
    q_members = {name: quotes(text) for name, text in members_text.items()}
    all_member_quotes = Counter(q for qs in q_members.values() for q in qs)
    dup_passages = [q for q, n in all_member_quotes.items() if n > 1]
    stats = {
        "run": run_id,
        "records": {"total": len(recs), "runtime": len(runtime_ids), "memory": len(memory_ids)},
        "words": {"result": words(result), "local_report": words(report),
                  **{n: words(t) for n, t in members_text.items()},
                  "set_total": sum(words(t) for t in members_text.values()),
                  "dropped_memory_lens": words(dropped_lens)},
        "declarations": {"declared_once": sum(1 for m in decls.values() if len(m) == 1),
                         "declared_twice": duplicates,
                         "seeded_redeclared_by_specialist": seeded_redeclared},
        "passages_moved_out_of_runtime_member": removed_from_runtime,
        "coordinator_amendment_words_in_memory_member": amendment_words,
        "unresolved_references": {k: dict(v) for k, v in unresolved.items()},
        "unmapped_MEM_tokens_in_memory_member": dict(leftover_mem),
        "quotes": {"result": len(q_result), "local_report": len(q_report),
                   "result_report_overlap": len(set(q_result) & set(q_report)),
                   **{n: len(q) for n, q in q_members.items()},
                   "distinct_in_set": len(all_member_quotes),
                   "duplicate_passages_in_set": len(dup_passages),
                   "union_of_inputs": len(set(q_result) | set(q_report))},
    }
    (out_dir / "stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(json.dumps(stats, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
