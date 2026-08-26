# Three channels: migration, claims, machinery

Everything the 2026-08-24 sweeps turned up, sorted by **what kind of change it
is** rather than by which note it came from. The three channels have different
owners, different risk, and different blockers, and mixing them is what makes a
corpus cleanup stall.

**Refreshed 2026-08-26.** Rows describing the original sweep remain historical.
The operative grounding machinery below now follows ADR 073's direct
Quotes/snapshot protocol, and the rollout's literature handoffs have been added
as intake rather than counted as artifact dispositions. The source-independent
Channel 2 pass and the false-provenance repair are now recorded as executed.

- **Migration** — make the route from a claim to its source navigable and its
  wording checkable. Additive, low risk, batchable. Owner: this workshop.
- **Claims** — content discovered to be untrue, unscoped, or unsupported.
  Truth-apt; some sit under ADRs. Needs per-item judgment and approval.
- **Machinery** — system and procedure changes. Owner:
  [source-grounding](../source-grounding/README.md) and
  [`kb/reference/proposals/`](../../reference/proposals/README.md).

**Verification status is marked on every row.** `[v]` = confirmed directly
against the file. `[r]` = reported by a sweep and not independently re-checked;
re-check before acting. Acting on an `[r]` row as if it were `[v]` is the same
error this workshop exists to catch, one level up. `Done` and `Open` separately
record execution state; `[v]` does not mean the change has landed.

---

## Channel 1 — Migration

The defect here is almost never that a claim is wrong. It is that **nothing
routes a reader from the claim to what would settle it.** The first Pirolli
migration is complete. The remaining rows still lack an adjudicating source
route.

### 1a. Route existing claims to sources

| Artifact | Finding or remaining work | Status |
|---|---|---|
| `agents-navigate-by-deciding-what-to-read-next` | Pirolli source route linked; inherited claims narrowed; transfer boundary stated. The original grounding ran under the retired normalized-Claims protocol | Done 2026-08-24 [v] |
| `linking-theory` | Same Pirolli route added; unsupported pointer-context monotone removed. The original grounding ran under the retired normalized-Claims protocol | Done 2026-08-24 [v] |
| `index-completeness-does-not-determine-editorial-orientation` | Needs LIS pathfinders / annotated bibliographies / PKM MOC. **Attribution already exists one hop away** in `an-enforced-tag-readme`, which links back here — may be a move, not an invention | Open [v] |
| `an-enforced-tag-readme...` | "Luhmann" and "Nick Milo's LYT" named with no dated work, no URL, no ingest | Open [v] |
| `knowledge-storage-does-not-imply-contextual-activation` | Six tracked LLM-side ingests cited. Gao and Chen add bounded evidence about explicit documentation consultation versus behavioral uptake, but no primary cognitive source for C1/C2; the 2026-08-25 edit requires current grounding freshness to be checked | Open [v] |
| `indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more` | No external source route; the 2026-08-26 claim reframe does not supply one | Open [v] |
| `addressability-grain...` | Zero external references | Open [r] |
| `pointer-design-tradeoffs...`, `link-following-and-search...`, `design-for-the-first-time-human...`, `charting-...-beyond-rag` | Zero external citations for claims placed in outside traditions | Open [r] |

### 1b. The standing-TODO batch

Three artifacts carry explicit "survey is from training data, not systematic"
TODOs inside these traditions: `links-README.md`,
`title-as-claim-enables-traversal-as-reasoning.md`,
`information-value-is-observer-relative.md`. **One batch, not three.** [v] for
the first, [r] for the others. **Open.**

### 1c. Repair a false provenance signal

**Done 2026-08-26 [v].**
`a-knowledge-base-should-support-fluid-resolution-switching` no longer declares
`has-external-sources` for the unnamed social-media post. The origin note remains
visible in prose, but it no longer emits a false machine-readable provenance
signal.

### 1d. Blocked on a corpus decision

The open rows in 1a cannot be executed until the sibling workshop decides which
sources to capture. The needed corpus is not the navigation corpus originally
proposed; see [claim-inventory](./claim-inventory.md). The two rows supported by
the live Pirolli ingest are complete and establish that the V1 grounding path
works.

### 1e. Rollout literature-handoff intake

**Intake triaged 2026-08-26 [v]; route work open.** The completed
claim-grounding rollout handed off sixteen claim uses across ten notes. Seven
uses now have a matching tracked ingest, while nine still lack a direct source
route or stable evidence artifact. Artifact-level triage admitted
`a-proposal-selection-loop-requires-search-evaluation-and-retention` and
`goedel-machines-are-a-proof-governed-case-of-self-modification` as two new
candidates alongside the already-cohort activation note. The other seven notes
stay in source-grounding, provenance, or evidence-stabilization queues: their
handoffs concern supporting uses, not credible subsumption of the artifact's
central contribution. Source acquisition, route migration, target
re-evaluation, and final artifact disposition remain separate steps; none of
the sixteen handoffs is itself a keep, merge, thin, or retire decision. The
detailed test, decisions, and 7-by-9 route matrix are in the [workshop
README](./README.md#received-claim-grounding-rollout-handoffs).

---

## Channel 2 — Claims to change

Ordered by whether a shipped artifact depends on the claim.

### Operative — an ADR or type spec rests on it

**2a. `index-completeness-does-not-determine-editorial-orientation`. Done
2026-08-24 [v].** The former title claimed that generation could not produce
orientation. The revised note instead distinguishes mechanically verifiable
membership from purpose-relative editorial judgment, explicitly allows people,
models, and graph algorithms to draft orientation, and explains how encoded
judgments can be regenerated. ADR 025, ADR 026, and the dependent MOC note now
use the scoped claim; neither ADR was destabilized.

**2b. `indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more`.
Done 2026-08-26 [v].** The re-check found a narrower defect than the sweep
reported. A conditional control-flow mechanism may be analytic, but suppression
alone does not lower recall: the suppressed operation must produce greater
realized task-relevant coverage at the same endpoint. The note was retitled and
reframed around that condition, distinguishes the mechanism from prevalence,
and now states what a predictive use must evidence. ADR 026 remains sound
without an empirical generalization because Commonplace explicitly authorizes
an exhaustive consumer to skip the by-tag `rg` when `complete: true` is present;
an omitted member is exactly what that suppressed sweep would recover.

### Prose-only — no shipped artifact depends on it

**2c. The pointer-context monotone. Done 2026-08-24 [v].** "The more context a
pointer carries, the cheaper the navigation decision" merged estimate quality
with interaction cost. The [propagation sweep](./c4-propagation-sweep.md) found
one inheritor and zero operative reach. The claim-pull rollout removed the
monotone from `agents-navigate-...` and `linking-theory`, promoted uncertainty
reduction per unit of context, added the Pirolli source route, and passed both
then-operative source review pairs. The first note's artifact-level disposition
remains open.

**2d. `pointer-design-tradeoffs...` conflates availability with accuracy. Done
2026-08-26 [v].** The note now treats specificity, cost, availability, and
accuracy as four axes. Fixed pointers are highly available but may be stale;
query-time and crafted pointers carry separate availability and accuracy failure
modes. Dependent summaries were reconciled.

**2e. `link-following-and-search...` misfiles skill descriptions. Done
2026-08-26 [v].** Skill descriptions now sit with long-range selection surfaces:
the task supplies context, but no source document's surrounding argument helps
the agent decide whether to load the full skill. The local-navigation summary
now covers only inline links and index entries.

**2f. `fluid-resolution-switching` retrieval surface overclaims. Done
2026-08-26 [v].** Direct inspection found the wording in the description, not the
title. The description and criterion section now present resolution fluidity as
a qualitative design lens whose measurement remains open. The false
`has-external-sources` trait was removed with Channel 1c.

**2g. `an-enforced-tag-readme` C2 is an unsurveyed universal negative.** [r] "No
Zettelkasten or LYT practitioner writes 'this map lists every note on the topic'
as an enforced promise." The note's pivotal move rests on it. Needs evidence or
weakening.

**2h. `charting-...-beyond-rag` has two soft spots.** [r] Its navigation-mode list
is not cut on one principle (a target type sits beside a task type), and its
"seems independent from navigation mode" was hardened by promotion into a
standalone note without being tested. Self-labelled brainstorming, which
discounts any disposition applied to it.

**2i. `human-llm-differences...` Navigation row is superseded in place. Done
2026-08-26 [v].** The row now states the human and agent defaults in access-mode
terms and links the sharper claim: either consumer can move between linear and
sublinear access when the interface changes.

### What is notable about this channel

**The five source-independent findings are closed.** 2b, 2d, 2e, 2f, and 2i
were scope errors, category errors, or self-contradictions found by reading the
notes against themselves and their dependents. None required a source-corpus
decision.

That is the running result of this workshop restated: pointed at redundancy, the
method returned **three defects and zero clean rediscoveries a retirement would
tidily remove.** All three defects in that running tally are repaired. The first
artifact disposition remains open.

---

## Channel 3 — Machinery

### Landed

**3a. Direct source grounding and standard review. Done 2026-08-25 [v].**
[ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
requires the promoted writing skills to identify the exact target claim or
paragraph for every explicit new or materially changed source dependency. The
writer then applies the standard `semantic/grounding-alignment` gate directly
against one of the two routes below. Insufficient direct support is a stop, not
a new source-specific review-pair type.

**3b. Two explicit source routes under ignored snapshots. V1 decided 2026-08-25
[v].** A normal ingest link declares that its tracked `## Quotes` section is
sufficient for the cited use. A link marked `(snapshot required)` declares that
sound checking needs the exact name-paired local snapshot; the writer verifies
its canonical source and exact-byte SHA-256 before using it. A missing or
mismatched required snapshot fails closed. This removes the machinery blocker on
Channel 1 without pretending that ignored primary bodies are present in a fresh
clone.

**3c. No normalized claim or quote identity in V1. Decided 2026-08-25 [v].**
The old `## Claims` ledger, virtual source lens, link-derived artifact-to-ingest
pairs, and source-specific freshness behavior are retired. The rollout recorded
205 uses under that historical protocol and 59 under the direct Quotes/snapshot
protocol. It found no semantic reconciliation or reuse pressure that earned
stable identifiers for normalized claims or retained quotes. Quotes remain
append-only exact passages; target-specific transfer reasoning remains in the
target.

**Freshness note, refreshed 2026-08-26 [v].** At its certification freeze, the
rollout had a fresh standard grounding result for all 68 target notes: 34 PASS,
10 WARN, and 24 FAIL. That is a dated coverage result, not standing assurance. Later edits,
including the activation-note revision, require current freshness checks and
may require new reviews. The 2026-08-26 `concept-attribution` and
`misleading-link-text` prompt edits also changed criterion snapshots and stale
their previous partitions. Neither a fresh result nor its outcome settles an
artifact disposition.

### Still open

**3d. Prior-art discovery at write time. Partial [v].** ADR 073 guards a source
dependency once the candidate names it. It deliberately cannot detect an
uncited claim that external literature already establishes. The log-entry
novelty battery and duplicate search remain intra-KB. The workshop still must
decide whether model recall should emit non-authoritative reading assignments,
whether a deterministic provenance report covers enough of the gap, or whether
no broader write-time arm is warranted.

**3e. Identifiable provenance. Open [v].** Nothing checks that
`has-external-sources` resolves to an identifiable external reference. The
false trait instance in 1c is repaired, but another instance could still pass
the current contract. This remains a candidate deterministic check.

### Bugs

**3f. `commonplace-verify-quotes` scans ignored files. Open [v].** It walks into
`.snapshots/` and tries to resolve a mangled URL as a file path
(`kb/sources/.snapshots/http:/memory.md`). This does not block the ADR 073
grounding path, but the command's corpus walk remains wrong.

**3g. Equation-heavy PDF capture. Done 2026-08-24 [v].**
`cp-skill-snapshot-web` no longer makes model-mediated cleanup a condition of
capture. It copies the extracted body locally, permits bounded cleanup only when
explicitly requested, and retains raw extraction as fallback.

### Rules, not code

**3h. Decide the corpus from the claims, not the cluster's name. Adopted as a
working rule [v].** The cohort was scoped to foraging/LIS from note titles; its
claims actually place across cognitive psychology of memory and transfer,
human-factors automation bias, materialized-view maintenance, single-source
publishing, and storage read amplification. The failure mode is not missing a
source — it is reading *rejection from the scoped tradition* as *no external
tradition*, which nearly happened to `addressability-grain`. The wider corpus
itself remains undecided in the sibling workshop.

**3i. A link label is missing.** [v] Connect found no label for "this source
states the established version of a local claim written from recall" and used
`is-evidence-for` as the nearest fit. Surfacing belongs here; the conclusion
belongs to [linking-foundations](../linking-foundations/README.md).

**3j. The reusable pattern for a delta note.** [r] The seven-move structure
extracted from `an-enforced-tag-readme` in [claim-inventory](./claim-inventory.md),
plus the eighth move that note does not perform — route the tradition claim to a
dated source, and evidence any negative claim about the tradition. Copying the
form without the eighth move propagates the problem in more convincing packaging.

---

## Sequencing

1. **Ground the Gödel-machine note's ancillary handoff, then make the first
   dated artifact judgment.** Its primary Schmidhuber route is already present
   and the Incremental Self-Improvement report now has a matching ingest, making
   this the smallest candidate that can exercise disposition rather than only
   claim repair.
2. **Complete the proposal-selection candidate's source set.** Ground the three
   matching ingests and obtain a direct primary Ashby route for its two remaining
   uses before judging whether the three-function model is established
   vocabulary, a local subtype, or a mixture.
3. **Select the wider corpus from the original claim inventory.**
   Source-grounding owns the selection; the V1 Quotes/snapshot path is ready to
   carry each result.
4. **Run the remaining migrations and source-dependent claim judgments** in
   small source-coherent batches, without treating the seven excluded handoff
   notes as artifact-disposition blockers.
5. **Record the remaining dated artifact dispositions and close the two general
   questions.** Promote a disposition rule or record that judgment remains
   per-note, and decide the unresolved prior-art check.

Bulk migration still should not precede source selection. The machinery is no
longer the blocker; choosing evidence from the wrong tradition is.
