# Review accuracy fixes

- **Recorded:** 2026-09-30, at the operator's request after fact checks of the two reviews published under ADR 096 and ADR 097.
- **Status:** planned; the operator approved the approach. Implement after run `AAS-2026-09-30-instinctual-memory-03` finishes, because a method commit while a run is open makes its publication refuse.
- **Evidence:** fact checks against the pinned sources of `kb/agentic-systems/reviews/pageindex.md` (run `AAS-2026-09-29-pageindex-02`, source `d2693d80`) and `kb/agentic-systems/reviews/instinctual-memory.md` (run `AAS-2026-09-30-instinctual-memory-02`, source `6acb13dc`). Neither review contains a claim the source contradicts. The errors are of the kinds below.

## Error kinds found

| Kind | PageIndex | instinctual-memory |
|---|---|---|
| A fact true of one route or mode written as system-wide | three cases (flash-only parser split and PDF refusal; SDK-local-only "only other writer") | minor (LLM-extractor-only auto consolidation and evidence check) |
| Caller workflow written as code behaviour | "deleted and resubmitted"; citation resolution the chat path never calls; "caller-supplied" id the code generates | none |
| A whole route missing, so a negative verdict reads system-wide | minor (index-time injection hardening omitted) | `mem tidy` absent from all four members; it is LLM criticism of stored facts, user-reviewed, whose suppressions later consolidation reads (`src/tidy.rs`, `src/consolidate.rs:148-153`). The "no content-directed criticism / no self-improvement" verdict never considered it. The failed run `AAS-2026-09-29-instinctual-memory-03` did cover tidy, so route coverage varies between runs. |
| Set-internal references in the public review | "This Reconciliation" in a limitation row | a second `Evidence basis:` line; bare `SRC-1`; "the runtime pass"; unnamed "conditions 1–4"; profile field names (`trace_source`) in the Limitations |
| Cited records that do not bear on the text | CLM-1 and CLM-5 on the cloud row | minor |
| Overlapping limitation rows | rows 8/9 and 6/7 | rows 2/3 and 1/4 |

## Planned changes

1. **Entry-point inventory in the runtime member.** The runtime type requires a table of every entry point at the boundary (CLI subcommands, hooks, MCP and HTTP tools, exported library functions, scheduled jobs), each mapped to the route records that cover it or to a stated exclusion with its reason. The runtime job builds it; the reconcile and verify jobs check that every negative or system-wide verdict considered each relevant entry point.
2. **A template for the Bounded synthesis.** Fixed level-three sections in the overview type and `reconcile.md`:
   - `### What it is`: the system and its boundary in one paragraph, with no evidence-basis line (code adds it to the review).
   - `### How it operates`: by route or mode; each claim names the route, mode or entry point it covers.
   - `### What it retains and reads back`
   - `### What is checked`: checks by route, and what no route checks.
   - `### Learning and self-improvement`: one entry each for the theory-builder conditions 1–4 (named), reflective, autonomous and self-improving, each with verdict, evidence status, and the entry points it considered.
   - `### What would change this assessment`

   A section with nothing to say takes one line, "Not applicable at this boundary", with the reason. The reconcile validator refuses a synthesis without these sections or one that opens with an `Evidence basis:` line. The review projection keeps the sections, one heading level up.
3. **Verify checks the public text.** `verify.md` adds: claims about a system with several routes or modes name the one they cover; code behaviour is distinguished from what a caller or user does; the synthesis and Limitations contain no set-internal vocabulary (overview section names, profile field names, bare `SRC-` IDs, "this Reconciliation"); each record a limitation row cites bears on that row; limitation rows do not duplicate each other. Findings are blockers.
4. **Reconcile writes Limitations for the public reader.** `reconcile.md`: Limitations make no reference to the overview's own sections and use no profile field names; merge rows that state the same limit.
5. **Judging norms** add: describe what the code does, not what a caller or user would do with it, and name the route or mode a claim covers.
6. **Boundary fetch wording** (from run `-03`'s first boundary attempt, which stalled on a sandboxed `git fetch`): a local commit matching the selected revision needs no fetch.

## After implementation

Rerun PageIndex and instinctual-memory. Compare against the fact checks above: the error kinds should not recur, and `mem tidy` should appear in the instinctual-memory inventory and in its criticism verdict. A generated review is not hand-edited, so the two published reviews are replaced by the reruns, not corrected in place.
