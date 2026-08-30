---
name: write-agent-memory-system-review
description: Run only when analyse-agentic-system invokes the legacy review-publication workflow for a detected external memory, knowledge, or context-engineering system; do not select or invoke directly.
type: kb/types/instruction.md
user-invocable: false
allowed-tools: Read, Write, Grep, Glob, Bash, Task
context: fork
model: opus
argument-hint: "prepared-source packet from analyse-agentic-system"
---

# Write Agent Memory System Review

Publish or replace one legacy-collection `type: kb/agent-memory-systems/types/agent-memory-system-review.md` artifact from the frozen evidence boundary established by `analyse-agentic-system`, then run its established editorial QA and validation workflow. The artifact is a source-faithful, ontology-normalized account of the external system; current Commonplace implications are a separately commissioned transfer scan.

This is a local Commonplace-repo publication subworkflow, not a public external-system analysis entry and not a promoted `cp-skill-*` framework skill. The invoking orchestrator owns the source boundary, mutation authority, artifact lifecycle, taxonomy and semantic QA, closing validation, and final report. A delegated worker owns only the new review draft and its first structural validation.

Delegation means a harness-provided sub-agent or worker tool only. Never start a nested agent by running `codex`, `codex exec`, `claude`, or another agent CLI from the shell. If the harness cannot supply the required worker and the prepared packet does not authorize local drafting, stop before archiving an incumbent review; do not work around the limit with a command-line agent process.

## Prerequisites

Every invocation carries the parent `AAS-*` run ID, selected subject and stable subject slug, frozen `SRC-*` register, and legacy-publication authority disposition. If publication is not authorized, return `not published — legacy review output not authorized` before requiring or reading publication-only fields.

For an authorized publication, also require:

- `source-tier`: `code-grounded` when the review's material findings can rest on inspected implementation, otherwise `doc-grounded`;
- the frozen `SRC-*` register and the inspectable source locations or bundle it identifies;
- reviewed revision or capture, evidence limitations, and citation format;
- an authorized `note_path`, plus authority to move an incumbent at that path to one collision-safe `.replaced.<date>[.<n>].md` sibling;
- any separately authorized auxiliary paths: `kb/agent-memory-systems/README.md` and the trace-learning survey are excluded unless named;
- the downstream comparison disposition: either authority for the generated `systems.csv` and `systems-table.md` pair plus any separately commissioned current landscape-synthesis output, or an explicit no-authority disposition that requires the workflow to report those consumers stale;
- authority to create the workflow-owned review jobs, results, and freshness state required by semantic QA.
- whether local drafting is authorized when a fresh worker is unavailable.

Code-grounded reviews live under `kb/agent-memory-systems/reviews/`; doc-grounded reviews live under `kb/agent-memory-systems/lightweight/`. The prepared boundary must be citable under the review type: immutable source-file anchors for `code-grounded`, or identified and dated or versioned document anchors for `doc-grounded`.

If the boundary is inspectable for the parent analysis but cannot support durable citations, return `blocked — prepared source boundary is not publishably citable`. Detection routes here; it does not grant publication authority.

## Steps

1. **Verify the packet and frozen boundary.** Check that every prerequisite is present, each supplied source location or bundled item is readable, and its identity still matches the `SRC-*` register and reviewed revision or fingerprint. Do not acquire, clone, fetch, merge, pull, capture, mutate, or widen sources. If the identity changed, return `blocked — prepared source boundary changed`.

   Confirm `note_path` is inside the directory required by `source-tier`. Use the subject name as the default filename unless an established house-style variant applies. Do not replace a same-name review unless its source metadata resolves to the same selected subject and source identity. Run `git status --short` in the Commonplace repo before writing so unrelated changes remain visible.

2. **Choose the drafting mode before replacing anything.** Use `delegated` when the harness can launch a fresh worker. Otherwise use `local` only when the packet explicitly authorizes it, and report `drafting was local, not delegated` as a workflow exception. If neither mode is available, return `blocked — delegated drafting unavailable`, leaving any incumbent review untouched. Do not draft in this step; step 3 performs any replacement, and step 4 drafts exactly once in the selected mode.

   A worker that launches and then fails, or a draft that later QA rejects, can still leave the incumbent archived with no replacement. The restore obligation remains undecided; the option space is in [Recoverable replacement of an incumbent review](../../reference/proposals/recoverable-replacement-of-an-incumbent-review.md).

3. **Archive an existing review before writing.** If `note_path` exists, move it to `{note_path%.md}.replaced.{YYYY-MM-DD}.md`. If that target exists, append a numeric suffix starting at `2` and increment until the path is free.

   Then mark the archived file:
   - Change `type` to `kb/types/note.md`; the preserved predecessor is no longer a live review or matrix input.
   - Set `tags: []`, clearing any `trace-learning` tag.
   - Add after the title: `> Replaced {YYYY-MM-DD}. See [{name}](./{name}.md) for the current review.`
   - Remove `user-verified`; archiving is a substantive lifecycle edit and the replacement banner carries the supersession fact.

   Do not read the archived `.replaced.*.md` file while writing the replacement.

4. **Draft once in the selected mode.** Use `kb/agent-memory-systems/types/agent-memory-system-review.md` as the artifact contract. Do not load the full [designing-agent-memory-systems](../../notes/designing-agent-memory-systems.md) note; its comparison lens is already condensed into the contract.

   The common draft contract is:

   ```text
   Draft review content for {note_path}.

   Read, in this order:
   - kb/agent-memory-systems/COLLECTION.md
   - kb/agent-memory-systems/types/agent-memory-system-review.md — the authoritative artifact contract. Use its current retained-artifact vocabulary, including `knowledge-artifact` and `system-definition-artifact` as behavioral-authority families.
   - 1-2 current reviews from the same evidence tier's directory and kb/agent-memory-systems/README.md, for style only; ignore any legacy Commonplace-comparison, borrowable-idea, or watch sections they retain

   Inputs:
   - parent run: {parent_run_id}
   - source tier: {source_tier}
   - frozen source register and readable locations or bundle: {source_register_and_locations}
   - note path: {note_path}
   - selected subject and source identities: {subject_and_source_identities}
   - reviewed revision or capture: {reviewed_revision_or_capture}
   - citation format: {citation_format}
   - evidence limitations: {evidence_limitations_or_none}

   If any required input is missing, stop and report which. Verify every supplied source location or bundled item is readable. Never update last-checked without actually reading the frozen sources. Do not mutate or widen them.

   Ground the review in the primary sources in the frozen register. For a code-grounded review, inspect README, architecture/design docs, CLAUDE.md/AGENTS.md, package manifests, and the core source files implementing the central claims; where implementation clarifies or contradicts doctrine, report what the code does and note the divergence. For a doc-grounded review, keep behavior claim-level and carry evidence limitations into the relevant claims. Decide trace-learning status only at the confidence the tier supports, and keep the placement section and trace-learning tag in parity.

   Write each material mechanism in the external system's native operational terms before applying Commonplace ontology. For every mapping, make the defining fit visible and qualify partial or uncertain analogies. Fill the closed controlled fields even when the value resembles Commonplace. Treat open mechanisms such as frontloading as evidenced instances, not as population-complete absence fields. Put an ontology mismatch in Curiosity Pass instead of forcing the nearest term.

   Do not add Comparison with Our System, Borrowable Ideas, What to Watch, a Commonplace delta, or a transfer recommendation. Those are excluded from the durable review even when the style examples contain them.

   Do not add user-verified; drafting and semantic review cannot grant human attestation. Write note_path from the strongest supplied evidence outward. Do not cite the parent run as evidence; cite the frozen primary sources.

   Then run: commonplace-validate {note_path}
   Fix any structural or description-quality issues it reports and re-run until clean.

   During this draft, edit only note_path, run no other commonplace-* command, and do not spawn or delegate. If completion is impossible, stop and report the blocker; never run an agent CLI as a substitute.

   Return the commonplace-validate result and whether trace-learning applies.
   ```

   In `delegated` mode, launch one fresh worker with a minimal task-local context. Do not fork the orchestrator's full context when the harness offers a clean-context option. Give it a task made from the following load-bearing wrapper plus the common draft contract above, with all values filled in; do not also hand it this skill file. The wrapper is required because [skill discovery re-fires in every sub-agent context](../../notes/skill-discovery-re-fires-in-every-sub-agent-context.md).

   ```text
   You are a delegated drafting worker; the wrapper and draft contract below are your complete and only brief. Your environment may surface write-agent-memory-system-review or another skill because the task resembles its trigger. Do not invoke or follow it. Its archive, auxiliary-artifact, QA, and final-validation steps belong to the orchestrator. Follow only this brief and do not delegate.
   ```

   Verify the worker-owned draft and validation result, then close, terminate, or release the worker. Do not retain it for semantic QA or a follow-up task.

   In `local` mode, do not launch a worker. Follow the common draft contract directly after step 3; its single-file isolation ends when this step validates cleanly, then continue with step 5.

5. **Update auxiliary artifacts only when separately authorized.** Edit `kb/agent-memory-systems/README.md` only when its path is in the packet's mutation set and either the subject was named in the `## Coverage` review backlog or the review establishes a genuinely new cross-system pattern. Edit `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md` only when its path is authorized and the review's trace-learning placement adds meaningfully to the survey. Otherwise report the candidate edit without making it.

6. **Run ontology and taxonomy QA.** Re-read the draft against the type contract's ontology-normalization rule, artifact-analysis fields, and trace-learning split. For each controlled field, ask whether the external mechanism, value, and mapping rationale remain together. For each open Commonplace concept, verify that the review states the native mechanism and does not turn omission into absence. Move a partial or failed fit to Curiosity Pass. Confirm the draft contains no Commonplace comparison, borrowable ideas, watch items, or transfer recommendations. Do not force a rigid section when the system has no distinctive mechanism there; revise only when absence hides an important tradeoff or the wording is ambiguous.

7. **Run semantic QA.** Follow `kb/instructions/run-review-batches.md` on the new review in requested mode with the `semantic` bundle. Select pairs, create jobs from selector JSON, delegate each job through the harness, and finalize each sentinel-bracketed output with runner and any harness-supplied model provenance. Treat findings as a read-only QA loop: fix clearly valid issues and leave uncertain findings for the final report. If the current harness cannot complete semantic QA, report it as a blocked QA step rather than substituting a shell-launched agent.

8. **Validate.** Run `commonplace-validate "{note_path}"`. Fix any structural or description-quality issues and validate once more.

9. **Close the downstream comparison handoff.** A code-grounded new or replacement review changes the source set for the matrix, table, and any synthesis presented as current. Do not let review publication complete with that state implicit.

   - Start a generated refresh only when both paths are authorized. Rebuild `kb/agent-memory-systems/systems.csv`, require a successful build report with `flags: 0`, then regenerate `kb/agent-memory-systems/systems-table.md` from those exact CSV bytes. If either path is unauthorized or either build fails, report the pair as stale and never describe a partial refresh as current. Never hand-edit either generated artifact.
   - A current public synthesis is invalidated whenever its matrix, row-linked reviews, or ontology inputs differ from its recorded evidence identity. Invoke [Synthesize the agent-memory landscape](../synthesize-agent-memory-landscape/SKILL.md) only when the caller separately commissioned it, authorized its output and generated inputs, and supplied a reconstructable revision or retained snapshot. Otherwise report the existing synthesis as historical after this review change. Never patch its counts or examples piecemeal.
   - A doc-grounded review does not enter the code-grounded matrix or table. Report those as unchanged; report a public synthesis stale only when it actually includes the doc-grounded qualitative corpus that changed.

## Report

Report:

- parent run ID and reused source boundary;
- publication disposition and review path;
- whether an incumbent was archived;
- whether drafting was delegated;
- authorized auxiliary paths changed or candidate edits withheld;
- matrix/table refresh or stale disposition, including the matrix flag count;
- current landscape-synthesis refresh, historical, unchanged, or blocked disposition;
- ontology and taxonomy QA outcome;
- semantic bundle outcome;
- final `commonplace-validate` result.

## Constraints

**Always:**

- reuse the invoking run's source register and revision;
- write code-grounded reviews under `reviews/` and doc-grounded reviews under `lightweight/`;
- cite the frozen source identity at the review type's required strength;
- preserve the external system's native mechanism beneath each Commonplace ontology mapping;
- run semantic QA before final validation.

**Never:**

- acquire, refresh, mutate, or widen the prepared source boundary;
- mutate a path outside the packet's authorized review, auxiliary, or generated-comparison set, except workflow-owned semantic-QA state and a separately commissioned synthesis output owned by its invoked skill;
- overwrite a review whose source identity belongs to another subject;
- update `last-checked` without reading the frozen sources;
- write Commonplace differences, borrowable ideas, watch items, or transfer recommendations into the durable review;
- run an agent CLI from the shell to bypass delegation or worker limits;
- leave a published review unvalidated.
