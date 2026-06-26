# Current lineage practices and theory

This review captures what Commonplace already does around lineage before deciding what to revise. It is intentionally descriptive: the goal is to see the system we have, not to settle the new policy prematurely.

## What Lineage Is Supposed To Answer

The definition in `kb/notes/definitions/lineage.md` is already precise: lineage records a retained artifact's review-relevant source dependencies and derivation status. It should answer whether an artifact is source material, canonical source, derived view, generated index, compiled artifact, assembled package, learned update, or archival evidence, and what must be invalidated, regenerated, or retired when a source changes.

`kb/notes/axes-of-artifact-analysis.md` makes lineage one of four artifact-analysis axes:

- storage substrate: where retained state persists;
- representational form: how the operative part is encoded and consumed;
- lineage: what sources or derivations this retained behavior depends on;
- behavioral authority: who consumes it, through which channel, and with what force.

The key implication is that lineage is not "where did this file come from?" in a historical sense. It is the dependency information needed for review, invalidation, regeneration, retirement, rollback, and source alignment.

## Current Mechanisms

| surface | current practice | lineage consequence | open tension |
|---|---|---|---|
| Source snapshots | `kb/sources/*.md` snapshots preserve captured source content and should not be edited or annotated after capture. | The snapshot is source material, not authored analysis. Authored links normally belong in the matching `.ingest.md`. | Snapshot fidelity varies by capture path; source updates require a new snapshot or explicit recapture decision. |
| Ingest reports | `.ingest.md` files live next to snapshots, carry `source_snapshot`, classify the source, summarize connect findings, and recommend one next action. | The ingest is a durable analysis artifact derived from the snapshot and current KB context. | It uses generated connect reports as working context but must not cite or link them, so the generated report's contribution is summarized and then disappears unless promoted. |
| Directory ingests | `ingest-directory.md` writes one `.ingest.md` for an input directory, usually under `tmp/` or `kb/work/`, and records a File Manifest plus a Pin line. | The source tree may be gitignored or ephemeral; the ingest report plus pin is the durable handle. | The manifest records files read, but the source tree itself may not remain available. Reproducibility depends on a good pin and upstream availability. |
| Agent-memory-system reviews | Code-grounded reviews use a prepared `source_dir`, inspect an external repository checkout, and record source tier, source identity, reviewed revision, commit-pinned citations, and optional quote anchors. | The review note is durable derived analysis. The source repository remains external source material rather than a KB snapshot. | Need a general rule for external git-backed sources: when revision-pinned pointers are enough, when snapshots are required, and how freshness is reviewed. |
| Connect reports | `cp-skill-connect` writes `kb/reports/connect/<collection>/<artifact>.connect.md`; reports are generated, gitignored, and candidate-only. | Connect reports are immediate downstream context, not durable graph state. Their maintenance observations need explicit promotion. | Generated reports can accumulate important signals without durable ownership until a workshop like connect-maintenance extracts them. |
| Report types | `kb/reports/types/connect-report.md` and schema are tracked even though report instances are ignored. | The report contract is durable methodology; report instances are working outputs. | `kb/reports/` mixes tracked methodology files with ignored generated instances, so "reports are ignored" is not the whole rule. |
| Reviews | Review markdown files remain generated report outputs, while canonical lineage/freshness/acceptance state lives in SQLite acceptance events. Freshness is moving from Git SHAs to DB-owned note/gate snapshot hashes. | Lineage is explicit for review pairs: note snapshot, gate snapshot, model partition, acceptance event. | Report files are readable review artifacts, but selectors bind on DB state; the DB/file split is a special exception to file-first design. |
| Critiques and friction reports | Experimental report-only instructions write reports without acceptance/freshness state. | They create analysis artifacts that may guide edits but do not create canonical review state. | Their lineage and retention policy is weaker than reviews even though the prose may be influential. |
| Generated indexes | Complete generated listings are build-time-only for the site; agents use committed curated heads plus scoped `rg`. | The generated listing is a derived view over frontmatter and should not become a committed source of truth. | Curated heads remain committed and can still drift; optional marks such as `complete`/`covered_by` are validator-checked. |
| Ad-hoc distillations | Prompts, source packets, and workshop notes can package selected sources plus caller judgment before a type, schema, command, or skill exists. | They are derived artifacts even when untyped and ephemeral; if retained or reused, lineage needs to say what they compressed and what judgment they frontloaded. | Need a boundary between discardable prompt, reusable workshop artifact, promoted instruction, promoted skill, and report type. |
| Distillation tracking | `Distilled into:` lives at the source side, not usually in the distilled artifact. | Source edits surface downstream distillates at edit time; reverse provenance is a deliberate search. | This works for source-note -> distillate. It is less clear for source snapshot -> ingest -> note, source -> source, or external work derived from internal vocabulary. |
| Checked derived copies | Recomputable derived truth must be checked by a validator or omitted. | Mechanical lineage can be machine-followable rather than human-visible. | Only applies where derivation is deterministic and cheap to re-check; most prose/source lineage remains judgmental. |
| Source link labels | `kb/sources/COLLECTION.md` authorizes `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, and `see-also`. | Sources have an authored outbound surface, mostly through ingest reports and source reviews. | Several triage cases need contrast or parallel-mechanism relations that are not evidence, derivation, rationale, or source-to-source `compares-with`. |

## Gitignore And Persistence

The current repository distinguishes durable report methodology from generated report instances:

- tracked under `kb/reports/`: README-like pages, `link-vocabulary.md`, `promotion-candidates.md`, and report type specs;
- ignored under `kb/reports/`: connect reports, critique reports, friction reports, fix reports, bundle-review artifacts, review DB, and autoreason outputs.

This is directionally coherent: report contracts and durable summaries are committed, high-volume generated outputs are not. The policy is not yet named as a lineage rule, though. "Some reports are ignored and some are tracked" should probably become "report producers, report contracts, durable indexes/summaries, and report instances have different lineage classes."

The ambiguity matters because ignored reports can still contain high-value maintenance observations. The connect-maintenance workshop exists because generated reports had useful signals that needed a promotion pass.

## The Two-Step Report Pattern

Many operations already split into source gathering and typed report generation:

| operation | gathering/source step | generated report or state | durable promotion path |
|---|---|---|---|
| Source ingest | snapshot URL or read existing snapshot; run connect for connection context | `.ingest.md` report, using `kb/sources/types/ingest-report.md` | later note/reference/instruction update recommended by ingest |
| Directory ingest | read selected files from an external tree; record manifest and pin | `.ingest.md` report for the tree | later artifact chosen by recommended next action |
| Agent-memory-system review | prepare or refresh an external git checkout; inspect selected source files and docs | typed review note, using `kb/agent-memory-systems/types/agent-memory-system-review.md`; source repo remains external | agent-memory-system index updates, cross-system comparisons, methodology notes, or follow-up proposals |
| Connect | read source artifact, collection rules, indexes, searches, link neighborhoods | `.connect.md` report, using `kb/reports/types/connect-report.md` | future writer authors links, index entries, or maintenance work |
| Review | render prompt for note/gate pair(s), run agent review, parse output | markdown review report outputs plus DB lineage/acceptance/freshness state | acceptance events, warn/fix queue, note edits |
| Critique | read target note and build adversarial argument | `.critique.md` report | optional note revision; no canonical review state |
| Ad-hoc distillation | gather sources, examples, current theory, and caller judgment for a task-local boundary | one-off prompt, source packet, workshop draft, or temporary synthesis | later note, instruction, skill, report type, or discarded working context |
| Generated navigation | scan frontmatter and tag membership | build-time generated listings for the site | no committed generated listing; curated heads stay authored |

This suggests a useful design separation:

- the skill or command owns execution: what to read, which tools to call, where to write;
- the type owns the generated report contract: required fields, sections, and quality checks;
- the collection owns durable link authority: which links may be authored and which labels mean something;
- the promotion step owns what becomes library state.

That separation is visible in `cp-skill-connect`: the skill explicitly says it owns execution while the `connect-report` type owns report content. It is also visible in ingest: `cp-skill-ingest` gathers or delegates snapshot/connect work, then the `ingest-report` type defines how the durable source analysis should be shaped.

The automation question is what gets retained after the promotion step. A generated connect report over a note may be discarded, but if it drives an edit to that note, the resulting note version is still derivative at the update-event level. The canonical artifact is now "note after merge-back," not "report plus old note." That means lineage must distinguish artifact role from update provenance: a file can be canonical for readers while its latest version depends on automatic reports, source context, and merge decisions.

The review subsystem shows why this may require relational edge-state, not only file conventions. Review content did not stop being markdown, but review lineage moved to SQLite because selectors need indexed current-state queries and append-only acceptance events over a changing note/gate relation. If automatic derivation expands beyond reviews, the same shape may be needed for notes, ingests, source reviews, compiled views, cues, and merge-back edits: files hold canonical content; an edge-state surface holds dependency edges, source versions, generation events, freshness state, and update queues. That surface might begin as edge files or manifests before it earns a real DB.

## Existing Theory Inventory

### Artifact-analysis lineage

Lineage is one artifact-analysis axis, independent of substrate and form. A repo file can be canonical source, derived view, generated index, compiled view, or archival evidence. A database row can be canonical state. A generated Markdown report can be a disposable view or a promoted summary depending on authority and persistence.

### Distillation strips provenance

`distilled-artifacts-need-source-tracking.md` argues that shaped artifacts often suppress provenance by design. The dependency record should live where it interrupts source edits, usually source-side `Distilled into:` pointers at current scale.

This theory directly applies to skills, instructions, and reference artifacts distilled from notes. It does not yet fully handle external-source chains where the "source" is captured material, the ingest is analysis, and the promoted note may be a synthesis across multiple sources.

### Frontloaded artifacts need validity windows

`frontloading-spares-execution-context.md` says any frontloaded artifact whose inputs may change needs lineage, timestamp, or regeneration instructions. This covers generated prompt views, precomputed indexes, copied contract values, and sub-agent packets.

### Ad-hoc prompts are pre-typed derivations

`ad-hoc-prompts-extend-the-system-without-schema-changes.md` treats ad-hoc prompts as low-friction system extensions. They let the caller package what matters before a type signature, schema, or skill exists. For lineage, the key point is that the prompt may be temporary, but the distillation it performs is real: it selects sources, packages judgment, fixes a task boundary, and may later be extracted into a skill or instruction.

### External git-backed reviews preserve handles, not snapshots

`kb/agent-memory-systems/types/agent-memory-system-review.md` gives a different source-preservation shape. A code-grounded review depends on a source repository, but Commonplace does not copy the repository into `kb/sources/`. The durable artifact preserves reviewed revision, source identity, commit-pinned citations, and optional quote-anchored evidence. This suggests source preservation can mean retaining a stable verification handle, not always retaining a local snapshot.

### Recomputable truth must be checked or absent

`a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` handles the deterministic special case. When derivation can be mechanically re-run, the copy must be validated or not committed. Generated complete indexes and checked tag-README marks fit here.

### Managed staleness for judgmental derivations

`link-graph-plus-timestamps-enables-make-like-staleness-detection.md` and `evolving-understanding-needs-re-distillation-not-composition.md` cover the judgmental case: source changes should trigger review or re-distillation, not automatic patching.

### Compiled views need source-of-truth rules

`agent-memory-requirements/keep-compiled-views-aligned.md` says generated cues, prompt files, indexes, and assistant-specific views need provenance, source version or hash, generation time, owner, and regeneration rules when they can shape behavior.

### Report staleness can be fuzzy

`kb/work/derivative-report-uniformity/README.md` already decided that derivative report staleness should record exact facts but decide loosely. The key principle is: strictness follows behavioral authority. Reports can be fuzzy when they are advisory; canonical review state needs stronger tracking.

### Churning many-to-many edge state needs relational structure

`kb/notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md` extracts the storage rule from the review case. ADR 010 moved review state to SQLite after review artifacts stopped behaving like authored files and started behaving like operational lineage: keyed by note, gate, and model; mutated by acceptance events; queried by selectors for freshness. The extracted theory names the structural condition: churning state on an ownerless many-to-many edge. It also softens the implementation claim: a directory of edge files can represent the relation for a while, but that is already a filesystem-backed relational store, and a real database wins when keyed lookup, churn, and consistency demands exceed that surface.

This should be the basis for further investigations. The artifact content can stay in git, but any future automatic dependency-maintenance mechanism that maintains freshness, acceptance, or update state over many-to-many artifact edges should be modeled as relational edge-state first, then assigned an implementation weight: links, edge files, generated index, or real DB.

The review-specific storage case is now separated into [src-architecture-alternatives/review-lineage-storage-case.md](../src-architecture-alternatives/review-lineage-storage-case.md), including whether the same operational behavior could be ported into markdown review files plus JSON/YAML manifests, append-only event ledgers, and generated current-state indexes.

### Model provenance belongs to derivation events

`model-provenance.md` separates the model-conditioned derivation event from the durable artifact being edited. Review freshness is keyed by `(note_path, gate_path, model_partition)` because the gate note path identifies the review contract and model identity changes the judgment being accepted, but that model partition currently lives in lineage state, not in the note or gate files. The same rule should apply broadly with a storage decision per type: one-shot retained derivatives may need producer model metadata in frontmatter or manifests; canonical notes should not carry "last edited by model" as frontmatter because their content is revised through many events.

### Automation expands only with update mechanisms

`the-boundary-of-automation-is-the-boundary-of-verification.md` and the Commonplace agent-memory gap plan both point to the same pressure: automatic generation is easy, but automatic promotion, activation, retirement, and merge-back require authority and verification. For lineage, this means git retention is not the core question by itself. The system also needs stale selectors, regeneration commands, merge-back provenance, and retirement rules for each derivative class.

## Open Design Tensions

### 1. Source relation labels are too provenance-shaped

Current source labels cover evidence, derivation, rationale, comparison, definitions, and weak adjacency. Triage surfaced source-to-note relations that are parallel, contrasting, or same-mechanism-with-different-surface. Forcing them into `evidence` or `derived-from` misstates lineage.

Question: should `kb/sources/COLLECTION.md` add `contrasts` and `parallels` for source-to-note relations, or should those relationships stay in ingest prose until they become notes?

### 2. Source-to-source comparison may be too weak

`compares-with` exists for sources, agent-memory, and agentic-systems. It handles the Claude dynamic-workflows pair in principle. The unresolved question is whether source-to-source links should be durable links in ingests, or whether a synthesis note should own the comparison once it matters.

### 3. Inverse lineage is underspecified

The Where-it-lives case reverses the usual direction. If an external paper was distilled from internal KB vocabulary, a note-to-paper `derived-from` edge is wrong. But the paper can still be evidence of externalization, publication, or category fit.

Question: do we need a label such as `externalized-as`, `published-as`, or `derived-into`, or is this a source-note in the source's ingest prose rather than a library edge?

### 4. Generated reports can carry signals that later become durable

Connect reports are intentionally gitignored and candidate-only. Yet their `Maintenance Observations` sections have become a source of durable work. The pipeline from ignored report -> triage workshop -> library edit is real but informal.

Question: should report types define promotion expectations for observations, or should promotion stay in explicit workshops only?

### 5. Report persistence policy is implicit

Generated report instances are ignored, while report contracts and some durable summaries are tracked. That distinction is probably right, but it is not expressed as a named lineage rule.

Question: should `kb/reports/` get a top-level README that classifies report contracts, report instances, ledgers, and promoted summaries?

### 6. The type-owned report contract is under-theorized

Several instructions say the skill owns execution and the type owns the report contract. This is a useful local pattern but not yet a methodological claim.

Question: should Commonplace explicitly define "typed report generation" as a lineage pattern: source gathering creates bounded evidence; a type-shaped report records analysis; promotion decides what becomes durable library state?

### 7. External git-backed sources need a non-snapshot rule

Agent-memory-system reviews show that source preservation cannot mean "always snapshot the source into `kb/sources/`." Some sources are already durable git repositories, may be too large to retain as KB snapshots, and are better represented by reviewed revisions plus pinned citations.

Question: what metadata makes an external git-backed source sufficiently reviewable, and when should Commonplace still create a snapshot or ingest?

### 8. Ad-hoc distillation needs a promotion boundary

Ad-hoc prompts and source packets deliberately avoid schema work, but the moment one is retained, reused, or used to hand work to another agent, it has already become derived material. The lineage need appears before the formal type appears.

Question: what minimal lineage should a retained ad-hoc distillation carry, and when does repetition force promotion into a typed report, instruction, or skill?

### 9. Git retention needs automation-centered rules

Saving every automatic derivation in git will create churn and hide the canonical signal. Saving none of them loses auditability, update triggers, and the ability to learn from automated work. The rule needs to distinguish source material, report contracts, cheap candidate reports, durable derived analyses, high-churn operational state, deterministic generated views, behavior-facing compiled views, and merge-back provenance.

Question: which derivative classes belong in git, which belong in `kb/reports/` but ignored, which belong in SQLite or another state store, and which should exist only long enough to drive a merge-back edit?

### 10. Canonical artifacts can have derivative update events

A note revised from a connect report or review is derivative from its previous version and the report/source context, but it remains a canonical note. Treating the whole file as "derived material" would eventually classify most mature notes as derivative and stop helping. Ignoring the derivation loses the update lineage automation needs.

Question: should Commonplace record merge-back derivation events in commit messages, a git-tracked ledger, a DB, source-side pointers, or some combination keyed by artifact authority?

### 11. Complex automatic dependency maintenance may require edge-state infrastructure

Review lineage moved to SQLite because plain files were a poor surface for current-state selectors over churning review edge state. That rationale is not review-specific. Once automatic derivation happens across artifact meshes, selectors will need to ask similar questions: what sources does this artifact version depend on, which generated reports informed it, what source changes invalidate it, what update events have been accepted, and which derivatives are now stale?

Question: which future dependency-maintenance mechanisms are trees/stars/static meshes that can stay in files or links, which need filesystem-backed edge relations, and which become churning many-to-many edge-state systems that need a DB?

### 12. Authored links are latent dependency edges

The extracted note opens a larger question: every authored link can go stale when either endpoint changes. Most links should not be automatically maintained; many are static reader aids. But some link labels or edge types may have high disruption probability when endpoints change.

Question: can Commonplace rank link and edge types by how likely endpoint changes are to invalidate them, then reserve automatic maintenance for the high-disruption classes while leaving ordinary links to on-demand review?

## Transferred Case Backlog

| case | current state | mechanism question |
|---|---|---|
| Claude dynamic-workflows docs vs practitioner article | Agentic-system analysis links both snapshots; docs ingest names paired source and future `compares-with`. | Durable source-to-source `compares-with` vs synthesis-only comparison. |
| How to build your own agent harness | Ingest exists; source collection still lacks contrast/parallel labels for source-to-note relation. | Add source-to-note labels or keep these relationships in prose until promoted. |
| The log is the agent | Ingest exists; overlaps `scaling-managed-agents...`. | Near-duplicate ingest cross-reference and sovereignty/lock-in synthesis trigger. |
| Text optimization | Ingest exists; `update-time compute` remains unnamed; external-cognition lineage has no note home. | Record external-cognition lineage and future Meta-Harness cross-references. |
| Where it lives | Ingest exists; direction corrected away from note-to-paper `derived-from`; sovereignty-risk remains open. | Represent external paper downstream of internal vocabulary without lying about provenance. |
