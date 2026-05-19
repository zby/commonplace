# Ingest generalization for installed KBs

## Question

How should `cp-skill-ingest` become a general installed-KB tool without smuggling this repository's methodology-KB assumptions into every source analysis?

Ingest is one specialized directed-reading case. It reads a source through the stable KB-assimilation lens and writes an `ingest-report`: classification, summary, connections, extractable value, limitations, and recommended next action. Other specialized cases can live in skills or type specs; `agent-memory-system-review` is a type-driven example where the review lens is embedded in the type contract rather than generated as a separate instruction note. Ingest's stable shape is useful, and its deictic language is mostly portable: in an installed KB, "our" naturally refers to that installed project's system, work, codebase, and goals. The remaining portability issue is narrower: some examples and recommended destinations still assume this repository's methodology-KB shape.

The first pass should not redesign source ingestion. It should separate the stable ingest lens from this repository's local goal frame.

## Current coupling

`cp-skill-ingest` is coupled to this KB in several ways:

- **Goal-frame implicitness.** Phrases like "our theory", "our stack", "our work", "our codebase", and "our thinking or practices" are acceptable installed-KB language because "our" follows the local project context. The missing piece is not replacement wording; it is an explicit reminder that "our" is governed by `AGENTS.md ## KB Goals`, not by this repository's methodology domain.
- **Destination assumptions.** Recommended actions are framed as note writes, note updates, brainstorms, or filing as reference. That should remain the default: installed KBs should still treat notes as the main transferable-claim document type. The portability issue is that notes are not the only possible promotion target; local collection contracts may route some source value into reference docs, instructions, ADRs, runbooks, policies, datasets, product requirements, incident notes, or other project-specific artifact types.
- **Direct write-scope assumptions.** The skill tells agents not to modify files under `kb/notes/`, but the write boundary should be sharper: ingest's direct write is only the `.ingest.md`. It may delegate snapshot capture and connection discovery, and those delegated steps write their own snapshot and connect-report artifacts. Ingest should not directly change notes, reference docs, instructions, indexes, or any other library artifact. Promotion belongs to a later explicit step.
- **Connect dependency.** Ingest relies on `cp-skill-connect` before classification and value extraction. That remains right, but it means ingest generalization depends on connect generalization: the connect report must already be filtered by project goals and collection contracts.
- **Source-type examples.** The source-type list is mostly portable, but the extraction prompts under each type are tuned toward agent-KB methodology and software architecture. The type taxonomy can stay; the questions under it need to be goal-relative.
- **Directory ingest drift.** `ingest-directory.md` still warns that `source_type: code-repository` is missing from the schema, but `kb/sources/types/ingest-report.schema.yaml` already includes it. The instruction is stale.

## Stable core

Keep these parts:

- Source snapshot stays separate from ingest analysis.
- Ingest report remains the source-facing artifact: classify, summarize, connect, extract value, state limitations, recommend one next action.
- `cp-skill-connect` remains load-bearing because extractable value should be new relative to the existing KB, not merely interesting in isolation.
- The report schema can stay unchanged for the first pass.
- The skill's own direct write should still be only the `.ingest.md`; snapshot files and connect reports are produced by delegated steps, and promotion is a later decision.

## Goal-frame split

Ingest needs the same control-plane split as connect:

| Layer | Binding time | In ingest |
|---|---|---|
| Project KB goals | installation/session start | define what source value means and which consumers matter |
| Source collection contract | repository state before the run | defines source/report conventions, labels, and allowed source-analysis posture |
| Connect report | current run | gives existing-KB context and novelty filter |
| Source interpretation | current run | classifies the source and identifies its actual claims, evidence, and limits |
| Recommended action | current run | proposes one explicit downstream action inside the installed KB's collection model |

Working formulation:

> Use `AGENTS.md ## KB Goals` to decide what kind of source value matters. Use `kb/sources/COLLECTION.md` and `kb/sources/types/ingest-report.md` to preserve the ingest report contract. Use the connect report to decide what is new relative to the current KB. Treat notes as the default promotion target for transferable claims, but follow local collection/type contracts when the better destination is a reference doc, instruction, ADR, runbook, dataset, or other project artifact.

## Proposed first implementation slice

1. Rewrite `cp-skill-ingest/SKILL.md` to load or rely on the project goal frame before value extraction.
2. Keep "our" language where it is natural, but add a short rule: interpret "our" through the installed KB's goals and collection contracts.
3. Replace repo-specific examples only where they name this KB's domain or imply that `kb/notes/` is the only promotion target.
4. Keep note creation/update as the default recommended action for transferable claims, but let the action name another local collection or artifact type when the source value belongs there.
5. Change the critical constraint from "do not modify `kb/notes/`" to "ingest's direct write is only the ingest report; delegated snapshot/connect steps may write their own artifacts."
6. Deduplicate the repeated `kb/sources/types/ingest-report.md` read instruction.
7. Keep the existing sections and schema until installed-KB trials show the section set is wrong.

## Analyze before changing deeply

**Source value vocabulary.** The current `Extractable Value` section works because this KB wants transferable methodology. Installed KBs may instead value compliance evidence, operational lessons, product requirements, incident signals, customer language, experimental data, or domain facts. The skill needs generic value classes without becoming vague.

Candidate generic classes:

- evidence for an existing claim or decision
- contradiction or limitation affecting a current claim
- reusable method, workflow, or procedure
- data point, benchmark, or empirical result
- vocabulary or framing that improves retrieval and discussion
- operational warning, risk, or failure mode
- candidate artifact to write, update, retire, or review

**Recommended action authority.** Ingest should recommend, not execute. The downstream action will usually target a note, but may target reference docs, instructions, ADRs, source-only coverage, reports, or a project-specific collection when the collection contracts make that the better home. The action should name both target and rationale, but not perform the promotion.

**Directory ingest.** `ingest-directory.md` is a parallel ingest lens for source trees. It should receive the same goal-frame cleanup, but it also needs code/data specific guidance: pinning, file manifest, and evidence across files are its distinctive contract.

## Non-goals

- Do not remove `cp-skill-connect` from ingestion.
- Do not collapse snapshots and ingest reports.
- Do not make ingest write promoted notes, instructions, or reference docs directly.
- Do not make ingest directly update indexes or other library artifacts; any index refresh should be a separate explicit maintenance step unless the ingest command's contract is deliberately changed.
- Do not redesign the ingest-report schema until a real installed-KB trial exposes a schema problem.
- Do not make commonplace methodology collections default destinations for installed user KBs.

## Prior work

- [Connect generalization for installed KBs](./connect-generalization.md) - dependency: ingest consumes connect reports, so connect's goal-frame cleanup is upstream of ingest quality.
- [Writing Directed Reading Instructions](./directed-reading.md) - grounds: ingest is a stable directed-reading pass through the KB-assimilation lens.
- [Workshop README](./README.md) - context: ingest, connect, and instruction notes are sibling frontloading artifacts.
- [Source collection contract](../../sources/COLLECTION.md) - current-state: snapshots and ingest reports are separate descriptive artifacts.
- [Ingest report type](../../sources/types/ingest-report.md) - current-state: stable report contract and schema.
- [Control-plane goals](../../reference/control-plane-goals.md) - current-state: installed KB goals live in `AGENTS.md`.
