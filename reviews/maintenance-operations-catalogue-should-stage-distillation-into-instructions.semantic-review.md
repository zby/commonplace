=== SEMANTIC REVIEW: maintenance-operations-catalogue-should-stage-distillation-into-instructions.md ===

Claims identified: 13

WARN:
- [Completeness] The catalogue claims to be "that staging ground" for periodic KB maintenance operations, yet it lists only three operations. Several plausible maintenance operations are missing from the enumeration: (1) stale index detection (indexes whose entries no longer match their linked notes' titles or descriptions — the KB even has a note "stale-indexes-are-worse-than-no-indexes"); (2) link health checking (broken markdown links, which is mentioned in the deterministic-validation note but is clearly a periodic maintenance concern); (3) description quality audit (scanning for empty, generic, or summary-style descriptions); (4) log.md triage (the CLAUDE.md routing table sends improvement opportunities to kb/log.md, but no catalogue entry harvests them back). These are not exotic — they are implied by the KB's own methodology. The catalogue's framing as "the" staging ground for maintenance operations creates an implicit completeness claim that the current three entries do not satisfy.

- [Completeness] The orphan detection script searches only `kb/notes/` for references: `rg -q "$fname" --glob "*.md" kb/notes/`. Notes can also be linked from `kb/instructions/`, `kb/sources/`, `CLAUDE.md`, and `kb/tasks/`. A note referenced only from an instruction file would be flagged as an orphan by this script. The script's search scope is narrower than the actual link space.

INFO:
- [Completeness] The distillation pipeline's four steps (capture, re-run/tighten, mark ready, distill) do not mention a "retire" or "supersede" step. What happens when a catalogued operation becomes obsolete — replaced by a script, or merged into another operation? The deterministic-validation note (linked as "escalation path") describes operations graduating beyond instructions into scripts, but the pipeline has no step for removal or archival. This is a minor gap since the pipeline is still itself in staging, but worth noting.

- [Completeness] The neighborhood tension review's four categories (contradictions, tensions, redundancies, improvement opportunities) are reasonable but "improvement opportunities" is a catch-all that could mask distinct concerns. For example, "missing links" and "stale framing" are structurally different issues — one is a graph gap, the other is a content-quality issue. The category is functional but loose.

- [Grounding] The link to deterministic-validation-should-be-a-script is described as "escalation path: deterministic operations can move beyond instructions into scripts." The linked note is specifically about validation checks and the hard-oracle / soft-oracle split — it does not discuss a general escalation path for all maintenance operations. The semantic is reasonable as an analogy (if validation can graduate to script, so can other deterministic maintenance), but the linked note does not itself make the general claim. The note is inferring a general pattern from a specific example.

PASS:
- [Grounding] The link to periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing accurately reflects the source. That note does argue that routing docs should stay slim and periodic operations should be externally triggered. The relationship semantic "foundation" is appropriate — the hygiene note motivates the catalogue's existence.
- [Grounding] The link to instructions-are-skills-without-automatic-routing accurately reflects the source. That note defines instructions as execution-oriented distilled procedures in kb/instructions/, which is exactly the "target form" the catalogue claims mature entries should reach. The relationship semantic is sound.
- [Internal consistency] The introduction says operations should be distilled "once an operation is stable enough," and the pipeline's step 3 says "mark as ready when inputs, outputs, and decision points are stable." These are consistent — stability is the promotion criterion in both places.
- [Internal consistency] All three catalogue entries are marked "distillation status: staging," which is consistent with the note's self-description as a staging ground. No entry claims to be distilled while still residing in the catalogue.
- [Internal consistency] The note's description ("catalogue of periodic KB maintenance operations and distillation status, used as a staging ground before promotion into kb/instructions procedures") faithfully represents the body. No elided tensions.

Overall: 2 warnings, 3 info
===
