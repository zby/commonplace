---
description: "Proposal: separate logical artifact identity from the pinned content an operation actually read, giving multi-method runs and guarded transitions one capture-compare-guard boundary"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, evaluation]
---

# Artifact-version substrate for pinned operation inputs

An operation that reads an artifact several times over a long wall-clock window cannot assume it read the same text each time. A multi-method pass re-reads the note for each method; an asynchronous recommendation is executed against the note hours later; a freshness baseline claims evidence still applies to *this* artifact. Each of these needs the same two things kept apart: **which artifact** (a logical identity that determines collection, type context, relative-link base, and every key the artifact is stored under) and **which characters** (an immutable content version, hashed, that the operation actually consumed).

Commonplace conflates them almost everywhere. A path is both the name of the artifact and the instruction to go read it now. That works while an operation is a single synchronous read, and fails as soon as evidence, recommendations, or baselines outlive the read.

This proposal specifies the shared substrate: capture a content version, carry it under an unchanged logical identity, compare it against current state, and guard any state transition on the comparison. It deliberately holds no policy about what a changed input *means* — that belongs to whatever target owns the decision.

## Current state (as of 2026-07-13)

Most of this substrate is already shipped inside the review system, purpose-built for one target kind. What is missing is smaller than it first appears, and stating the existing surface precisely is what keeps the implementation from doubling it:

- **Capture store.** `review_file_snapshots` is keyed by path and content hash and retains the full `content_text` ([ADR 032](../adr/032-review-freshness-uses-db-snapshots-not-git.md)). It is role-neutral: any repo document can sit on either side of a pair. This *is* a content-addressed capture store; it is not named as one.
- **Capture.** `review_db.snapshot_file()` reads UTF-8 text from the live file under `repo_root`, hashes the re-encoded text, and persists it.
- **Hash and current-version resolution.** `review/freshness.py` exposes `content_sha256_for_text()` and `file_content_sha256()`.
- **Compare and diff.** `review_target_selector.py` already compares an accepted baseline hash against a freshly computed one and renders a `difflib` unified diff from the captured text to the current text.
- **Threading captured text onward.** `capture_review_inputs()` snapshots the pair's inputs and hands the captured `note_texts` and `criterion_texts` to prompt rendering, so the prompt and the stored snapshot already agree.

The gap is a **seam, not a subsystem**: content enters `snapshot_file()` only through its own `read_text()`, and there is no way for a caller to say "here are the characters — store them under this path." Criterion applicability, including type and trait routing, is likewise derived from a then-current file read before job preparation. An external caller therefore cannot make applicability, snapshot storage, and prompt rendering consume one supplied capture.

Outside review, the boundary is inconsistent. The compression worker already receives the note *text* alongside its path — the handoff this proposal generalizes. `cp-skill-connect` derives both identity and content from one path. The full-improvement pass runs five method families over what it calls "the note" without pinning a version, so a concurrent edit silently makes its reports describe different text.

## The design

### Two components, never collapsed

Every operation input carries:

```text
logical identity:  kb/notes/example.md          # what this artifact IS
content version:   <captured character sequence> # what this operation READ
content hash:      <sha256 of its UTF-8 encoding>
```

The logical identity determines collection membership, type resolution, the base directory for relative-link resolution, output naming, and the artifact side of any stored key. The content version supplies the exact characters the operation reads. **The content version is never substituted for the logical identity.** Treating a captured copy under `kb/reports/` as the artifact itself would select the wrong collection, break relative links, and store state against the wrong path — this is the single most important invariant here, and the easiest one to violate by passing one path where two components were meant.

Captured content is the exact Unicode character sequence returned by Commonplace's UTF-8 text read, hashed through its UTF-8 encoding. The substrate intentionally does not distinguish byte representations that produce the same consumed text; content freshness is about what the text operation saw. The capture is write-once by contract and identified by its recorded hash for the life of the operation. It lives in the shipped snapshot store, so a consumer names a capture by logical path and content hash rather than by a file it owns. Any human-readable copy an operation writes for inspection is derived and non-authoritative; it takes a non-Markdown extension so KB link scans, artifact scans, and validators do not mistake it for an authored artifact. Field names for captures should not reuse `source_snapshot`, which already denotes external-source lineage to the extraction utilities.

An operation may pin several inputs. A recommendation about a *pair* of artifacts — merge this note into that one — is only guardable if both sides are captured: a guard over one side alone lets the other drift out from under the decision unnoticed. The substrate therefore treats a pinned input set, not a single pinned input, as the unit an operation carries.

That set is declared by the consumer; the substrate does not recursively pin every file the operation consults or provide repository-wide snapshot isolation. A review pair pins its note and criterion. A full pass pins the assessed note and, for a merge recommendation, the proposed target. Prompt scaffolding, collection contracts, and other system-definition dependencies remain under their owning version or freshness policies rather than expanding every operation capture into a snapshot of the repository.

### Four operations, three of which exist

The substrate is small on purpose, and the implementation should stay proportionate to that. These are the operations a consumer needs; the parenthetical names the code that already provides each:

- **Capture** — given a logical identity, read current text once, hash its UTF-8 encoding, and persist the pair. Every later reader of this operation consumes the capture, not the file. (`snapshot_file()`, storing into `review_file_snapshots` — *plus the missing text-override seam*.)
- **Resolve current** — given a logical identity, return the current content hash, or *absent*. (`file_content_sha256()`; absence is the new case.)
- **Compare** — given a capture and the current state, return `matching`, `changed`, or `missing`, machine-readably, plus a diff from the captured text to the current text when both exist. (Hash comparison and `difflib` rendering already in `review_target_selector.py`; what is missing is exposing them as one result rather than inline selector logic.)
- **Guard** — compare every member of the consumer's pinned input set immediately before a state transition and refuse to begin if any member is not `matching`. A guard is a hard precondition that returns all comparisons, not a warning the caller may ignore. After the transition, the caller verifies the target-owned postconditions and routes an incomplete or ambiguous result to reconciliation. (New, but thin: a loop over Compare.)

**No new module, no new store.** These belong where their pieces already live — the review library — until a second consumer justifies extraction. Naming this a "substrate" up front invites building one; the freshness workshop is the extraction's proper trigger, and it has already committed to performing it.

`missing` is a distinct result, not a flavour of `changed`: absence is observationally ambiguous (deletion, relocation, and partial merge look alike), so the substrate reports it and refuses to interpret it.

The guard is deliberately optimistic. Commonplace assumes low write concurrency and does not add filesystem locks or compare-and-set machinery for the unlikely interval between the final comparison and the transition. A write detected before the transition stops it; post-transition verification catches incomplete or unexpected results. A write that races inside the small check-to-mutation window is residual risk, not something this substrate claims to prevent or reliably detect.

### Input-boundary seams

Pinning is not achieved by telling a worker that a capture exists. It requires explicit seams where content currently enters by a live read:

- **Review-job creation** accepts a text override keyed by the logical path. It stores the supplied text as the reviewed snapshot *under the original path*, renders that text into the job prompt, and uses its hash for the resulting freshness baseline. Criterion applicability is derived from the supplied frontmatter rather than a fresh read. This is the `snapshot_file()` / `job_prompt.py` change.
- **Direct-method callers** (compression, composition friction) receive the logical path plus the full captured text and perform no live read. Compression already works this way; the others adopt the same boundary.
- **Connection discovery** receives both components: collection rules and relative-link bases from the logical identity, claim and outbound links from the captured content. Its report continues to name the logical identity.
- **Synthesis and application steps** read the retained method outputs and the capture, never reopening the live artifact to reconstruct context.

The contract is harness-neutral within existing assumptions: a worker sharing the workspace can read the capture from disk, and a worker without shared-file reads can receive the same text inline. Review workers need neither, because their generated job prompt already embeds the note text — which is precisely why the change belongs at job preparation rather than in sub-agent lifecycle semantics.

### What the substrate does not decide

A changed input means nothing on its own. The substrate reports the comparison; the target decides. A full-pass disposition resolves to `superseded` ([report-owned resolution](./report-owned-resolution-for-asynchronous-full-pass-dispositions.md)); a review pair goes stale and is reselected; a generated index regenerates; a mark is recomputed. Encoding any of these responses into the substrate would make it a freshness policy engine, and the general policy question is exactly what the freshness workshop is still open on.

## Option space and free choices

- **Substrate scope now versus after a second consumer.** One worked consumer (the full-improvement pass) motivates capture, compare, and guard today. Building a general artifact-version boundary immediately risks designing for imagined consumers. The settled default is the smallest change that serves the worked case: add the override seam and the guard where the existing pieces live, and let the freshness workshop extract the boundary when it acquires the second consumer that would prove its shape.
- **Capture storage.** The settled default is the shipped `review_file_snapshots` table, which already stores path, content hash, and full content text for exactly this purpose. A sibling capture file in the operation's own output directory would make a full-pass packet diffable without DB access — the one real thing this choice gives up — but it would also duplicate a store that exists, and pull a hash validator, a report-type contract for the capture, and retention-unit rules into cleanup behind it. A packet may still write a derived, human-readable copy of its capture for inspection, provided that copy is explicitly *not* the authority and nothing validates against it: a second authoritative copy would be [a derived copy of recomputable truth](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) that must then be checked. The DB-coupling objection — that snapshot rows are pruned on a schedule owned by assay evidence — is currently hypothetical: no such pruning exists, and the review system treats old snapshot rows as harmless historical storage.
- **Provenance of a capture.** Captured text cannot prove which logical path it came from. The DB row carries the path alongside the text, which settles this for the default above; it becomes a live question again only if captures move to bare sibling files.
- **Override seam versus a read-through content resolver.** An explicit content override at each entry point is small and inspectable but must be threaded through every caller; a resolver injected into the read path pins content globally but hides the pinning from the code that depends on it. The proposed default is the explicit override — a silent pin is worse than an unpinned read, because it is invisible when it is wrong.
- **Guard placement.** A guard at each mutation site is precise but must be remembered; a guard inside the transition API cannot be forgotten but forces every writer to carry a capture. The proposed default is one grouped guard inside each transition that consumes a pinned input set, immediately before its first mutation, followed by target-owned postcondition verification.

## Forces and risks

- **The invariant is one substitution away from breaking.** Passing the capture path where the logical path was expected produces a plausible-looking run that resolves the wrong collection and stores state against a path under `kb/reports/`. Types or wrapper structures that make the two components unmixable are worth their cost here.
- **Consistency is not authority.** Pinned content makes every method in a pass internally consistent, and that is all. It does not license applying an edit plan to text nobody assessed — the guard before application is a hard stop, not an acknowledgement path.
- **The capture depends on the review DB.** Reusing `review_file_snapshots` means an asynchronous decision is only inspectable and diffable where that database is. This is the accepted cost of not building a second store, and it is bounded: the review DB is already local, already required by the workflow that produces the recommendation, and already the thing every freshness comparison consults. Git is not an alternative — Commonplace cannot infer capture or freshness from a repository that may be uncommitted, rebased, shallow, ignored, or managed through another workflow. If packets ever need to travel without the DB, the sibling-file option becomes live again, and its validator and retention rules become the price of that portability.
- **Code proportionality.** The temptation here is to build a general versioning subsystem for a workflow that needs one override parameter, one absence case, one result object, and one guard loop. Every capability this design names already has a home in `review/`; adding a parallel one would create exactly the [derived copy that must be checked](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) this KB warns about, in code rather than in notes.
- **The optimistic guard is not a transaction.** Comparing captures, mutating state, and editing artifacts are not atomic on a filesystem. Commonplace accepts the small residual race window rather than adding locks for a low-concurrency workflow. Postcondition verification and explicit reconciliation still cover incomplete or ambiguous transitions; the absence of an artifact is never evidence that an operation succeeded.
- **Retention couples an operation to its capture.** A capture is only useful while the operation that owns it can still be acted on. Cleanup must treat the operation's output and its captures as one retention unit, or a diff becomes impossible exactly when someone needs it.
- **Freshness is downstream, not included.** This substrate supplies versions and comparisons. Accepted baselines over arbitrary targets, reverse selection from a changed dependency to affected targets, and target-owned refresh policy remain open in the freshness workshop; adopting this proposal does not settle them.

## Adoption criteria

Adopt only with a worked case — the full-improvement pass is the intended one — covering:

1. Every method in a multi-method run consumes one captured text while retaining the original logical path as identity: collection rules, type context, relative-link resolution, and output naming all derive from the logical path.
2. Review-job applicability, prompts, reviewed snapshots, and freshness baselines derive from supplied content rather than an intervening live read, and the resulting baseline is stored under the logical path.
3. Connection discovery resolves the capture's relative links from the logical source's directory and applies the logical source's collection contract.
4. Comparison distinguishes `matching`, `changed`, and `missing`, and produces a diff from captured to current text when both exist.
5. One guard compares the complete pinned input set immediately before mutation, refuses to begin if any input is changed or missing, and returns every comparison rather than proceeding or silently rejecting.
6. A transition verifies its target-owned postconditions and routes an incomplete or ambiguous result to explicit reconciliation.
7. An editorial change to a live artifact during a run does not corrupt what the run assesses; when the change is present at the final guard, it prevents the run's output from being applied. The implementation does not claim atomic exclusion of a write racing inside the guard-to-mutation window.

A negative criterion carries as much weight as the rest: the implementation must add **no second capture store, no capture-file type spec, no capture validator, and no new retention semantics**. If it does, the design has outgrown the problem — the store, the hash, the comparison, and the diff already exist, and the worked case needs a seam and a guard, not a subsystem.

When a second consumer arrives, extracting a named boundary out of `review/` is the freshness workshop's prerequisite cleanup — a step it has already committed to, and not a reason to build the boundary speculatively now.

---

Relevant Notes:

- [Report-owned resolution for asynchronous full-pass dispositions](./report-owned-resolution-for-asynchronous-full-pass-dispositions.md) — part-of: the first consumer, which supplies the worked case and one target-owned response to a changed input
- [Review system](../README-REVIEW-SYSTEM.md) — part-of: owns the purpose-built two-input version of this substrate, whose capture path this proposal opens
- [ADR 032: review freshness uses DB snapshots, not Git](../adr/032-review-freshness-uses-db-snapshots-not-git.md) — see-also: the shipped role-neutral snapshot store this substrate generalizes rather than replaces
- [Full improvement pass closure](../full-improvement-pass-closure.md) — see-also: the multi-method run whose unpinned inputs motivate capture
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why a capture must be validated against its hash rather than trusted
