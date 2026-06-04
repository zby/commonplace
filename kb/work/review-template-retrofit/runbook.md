# Review template retrofit — per-review runbook
Migrate one agent-memory-system review to the **write-side / read-side** template. This runbook is the **delegatable** procedure: it assumes the tooling is already strict for the new layout (see `plan.md`, Phase 0), so an un-retrofitted review raises warnings and build flags, and conforms to `Overall: PASS (clean)` with 0 flags once retrofitted. One sub-agent per review.

**Precondition check:** if `commonplace-validate` is `Overall: PASS (clean)` on every in-scope review and the build reports 0 flags, the retrofit is done — stop. If validate tolerates the old layout with no warnings at all, the tooling is not strict yet; do `plan.md` Phase 0 first.

**Severity note:** schema violations validate as **warnings**, not failures (the validator hard-fails only on frontmatter `description`/`tags`/`type`), so an un-retrofitted review reports `Overall: PASS (N warnings)`. Do **not** gate on bare `Overall: PASS` — use the Worklist signals below.

Authority: `../../agent-memory-systems/types/agent-memory-system-review.md` (Write-side placement + Read-back placement sections, and the skeleton). Worked example: `../../agent-memory-systems/reviews/Zikkaron.md` (the canonical new-layout review; keep one example in sync). Mirror the delegation discipline of the earlier `../agent-memory-matrix-retrofit/` runbook: faithful-not-complete, `not-determinable` over guessing.
## What the new layout is
1. `## Trace-derived learning placement` **→** `## Write-side placement`, with the trace treatment demoted to a `### Trace-derived learning` **sub-section**. The write side is _everything that changes the store_; trace-learning is the automatic-from-traces case.
  
2. **Write-side lead tokens:**
  

- `**Write agency:**` `manual` · `automatic` — required in **every** review, under a kept `## Write-side placement` heading (parallel to `**Read-back:**`, which is always present even when its section body is omitted).
  
- `**Curation operations:**` `consolidate` · `dedup` · `evolve` · `synthesize` · `invalidate` · `decay` · `promote` — the _automatic_ operations only; omit when agency is manual-only.
  

3. **Read-back timing is gone.** No `**Read-back timing:**` line, no "Timing relative to action" item. One injection point, pre-invocation; after-the-turn work is write-side **maintenance**. Old "post-action read-back" prose that described capture/consolidation moves to the write side, not the read path.
  
4. **Read-back definition is not restated** in the review (it lives in the activation note). Don't re-add it.
  
## Scope
- **In:** `kb/agent-memory-systems/reviews/*.md` and `kb/agent-memory-systems/lightweight/*.md` (live instances of the type).
  
- **Out:** `*.replaced.*` (frozen — never edit), `dir-index.md`, `README.md`, any non-review file.
  
- **Lightweight caveat:** doc-grounded reviews often lack code evidence for curation operations — author `**Write agency:**` from the paper; use a sole `` `not-determinable` `` on `**Curation operations:**` only if the write path is genuinely automatic but unspecified. The matrix consumes `reviews/` only, but the rename + timing removal + agency verdict apply everywhere to pass the strict schema.
  
## Worklist
A review needs work if **any** of these deterministic signals fire (don't rely on `Overall: PASS` — see the severity note):

1. **Missing/incomplete tokens** — `python3 scripts/build_systems_matrix.py` lists per-review flags on repo-reviewed rows (e.g. `Write agency: missing lead token`, and `Curation operations` once agency is `automatic`).
  
2. **Old structure still present:**
  

```bash
rg -l "## Trace-derived learning placement|\*\*Read-back timing:\*\*" \
  kb/agent-memory-systems/reviews kb/agent-memory-systems/lightweight \
  | grep -v '\.replaced\.'
```

3. **New heading missing:**
  

```bash
for f in kb/agent-memory-systems/reviews/*.md kb/agent-memory-systems/lightweight/*.md; do
  case "$f" in *.replaced.*|*/dir-index.md|*/README.md) continue;; esac
  grep -qF "## Write-side placement" "$f" || echo "$f"
done
```

Lightweight reviews aren't in the matrix build, so signal 1 won't catch them — use signals 2–3 and a per-file `commonplace-validate` for those.
## Orchestration
1. For each worklist file, spawn **one sub-agent** scoped to that single file — sequential or bounded-parallel, but **never two agents on one file**. Pass it the file path, this runbook, the spec, and the Zikkaron example.
  
2. After each sub-agent returns, run `commonplace-validate <file>` → `Overall: PASS (clean)` (no Write-side / Read-back / Trace warnings), and re-run the build to confirm that file's flags are gone.
  
3. Repeat until the worklist is empty.
  
## Per-sub-agent procedure (one review file)
1. Read the whole review file.
  
2. **Rename** `## Trace-derived learning placement` → `## Write-side placement`; demote its trace content to a `### Trace-derived learning` sub-section. Preserve the trace lead tokens (`**Trace source:**`, `**Learning scope:**`, `**Learning timing:**`, `**Distilled form:**`) and prose verbatim.
  
3. **Add** `**Write agency:**` under the `## Write-side placement` heading: `manual` if the store changes only through the authoring channel; `automatic` if the system itself writes/curates (rule-driven, scheduled, or trace-learned); both when both apply. End with a short `— justification` from the review's own prose.
  
4. **Add** `**Curation operations:**` only when agency includes `automatic`: the automatic operations the review's evidence supports. Manual maintenance is _not_ an operation (agency only). Index/embedding rebuilds are access-structure upkeep, not operations. If the path is automatic but the operations are unreadable from the evidence, use a sole `` `not-determinable` ``.
  
5. **Remove the read-back timing** lead line and the old "Timing relative to action" item. If that prose carried real capture/consolidation meaning, relocate it to the write side (a curation operation or maintenance prose). Keep the read-back item numbering consistent with the spec (current item 3 is "Injection point — pre-invocation"; add injection-point prose only if the trigger/occasion is distinctive — session start, pre-compact, etc.).
  
6. Do **not** restate the read-back definition; do **not** read or modify the reviewed system's source; do **not** change the review's claims; do **not** bump `last-checked`. Preserve all citations, blockquotes, and CriticMarkup attributes.
  
7. **Self-check:** a `## Write-side placement` heading with a `**Write agency:**` token is present; no `## Trace-derived learning placement` heading remains; no `**Read-back timing:**` line remains; tokens use only allowed values; multi-valued tokens list every value that applies; `commonplace-validate` is `PASS (clean)`.
  
## Done condition
- All three worklist signals return nothing; every in-scope review is `Overall: PASS (clean)`.
  
- `python3 scripts/build_systems_matrix.py` → 0 flags on repo-reviewed rows.
  
- No `## Trace-derived learning placement` or `**Read-back timing:**` in live (non-`.replaced`) reviews:
  
  ```bash
  rg -l "## Trace-derived learning placement|\*\*Read-back timing:\*\*" \
    kb/agent-memory-systems/reviews kb/agent-memory-systems/lightweight \
    | grep -v '\.replaced\.'
  ```
  

Hand back to `plan.md` Phase 2 for the corpus-wide rebuild, table render, and close.
## Guardrails
- **Faithful, not complete.** A `not-determinable` token is honest; a guessed value pollutes the matrix.
  
- **Normalize, don't re-investigate.** The evidence is almost always already in the review prose — map it to the controlled vocabulary; don't re-read the system.
  
- `.replaced.*` **is frozen.** Never edit superseded snapshots.
  
- **One file per agent.** No agent edits a review another agent is touching.
