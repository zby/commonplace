# Three channels: migration, claims, machinery

Everything the 2026-08-24 sweeps turned up, sorted by **what kind of change it
is** rather than by which note it came from. The three channels have different
owners, different risk, and different blockers, and mixing them is what makes a
corpus cleanup stall.

**Refreshed 2026-08-25.** Rows describing the original sweep remain historical.
The operative grounding machinery below now follows ADR 073's direct
Quotes/snapshot protocol, and the rollout's literature handoffs have been added
as intake rather than counted as artifact dispositions.

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
| `stale-indexes-reduce-discovery...` | Zero external references and no `Relevant Notes` tail at all | Open [r] |
| `addressability-grain...` | Zero external references | Open [r] |
| `pointer-design-tradeoffs...`, `link-following-and-search...`, `design-for-the-first-time-human...`, `charting-...-beyond-rag` | Zero external citations for claims placed in outside traditions | Open [r] |

### 1b. The standing-TODO batch

Three artifacts carry explicit "survey is from training data, not systematic"
TODOs inside these traditions: `links-README.md`,
`title-as-claim-enables-traversal-as-reasoning.md`,
`information-value-is-observer-relative.md`. **One batch, not three.** [v] for
the first, [r] for the others. **Open.**

### 1c. Repair a false provenance signal

**Open [v].** `a-knowledge-base-should-support-fluid-resolution-switching` declares
`traits: [has-external-sources]` on the strength of "a social media post on 'The
Art of Good Thinking: Moving Between Levels'" — no author, no URL. Either
identify the source or drop the trait; a provenance signal pointing at nothing is
worse than none.

### 1d. Blocked on a corpus decision

The open rows in 1a cannot be executed until the sibling workshop decides which
sources to capture. The needed corpus is not the navigation corpus originally
proposed; see [claim-inventory](./claim-inventory.md). The two rows supported by
the live Pirolli ingest are complete and establish that the V1 grounding path
works.

### 1e. Rollout literature-handoff intake

**Open [v].** The completed claim-grounding rollout handed off sixteen claim
uses across ten notes. Seven uses now have a matching tracked ingest, while nine
still lack a direct source route or stable evidence artifact. Only
`knowledge-storage-does-not-imply-contextual-activation` belongs to this
workshop's starting cohort. The other nine notes need an explicit
cohort-membership decision before they become disposition work. Source
acquisition, route migration, target re-evaluation, and final artifact
disposition remain separate steps; none of the sixteen handoffs is itself a
keep, merge, thin, or retire decision. The detailed triage is in the [workshop
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

**2b. `stale-indexes...` C1 may be analytic, not empirical.** [r] It stipulates
the stopping behaviour into the comparison, so the conclusion holds by
construction and the claim cannot fail — yet ADR 026 treats it as a finding, "the
problem in [this note] in its sharpest form." The empirical claim the ADR needs —
that agents in fact stop at an apparently complete head — is assumed, not argued.
Re-check the wording before acting; if it holds, this needs either evidence or a
restatement that can fail.

### Prose-only — no shipped artifact depends on it

**2c. The pointer-context monotone. Done 2026-08-24 [v].** "The more context a
pointer carries, the cheaper the navigation decision" merged estimate quality
with interaction cost. The [propagation sweep](./c4-propagation-sweep.md) found
one inheritor and zero operative reach. The claim-pull rollout removed the
monotone from `agents-navigate-...` and `linking-theory`, promoted uncertainty
reduction per unit of context, added the Pirolli source route, and passed both
then-operative source review pairs. The first note's artifact-level disposition
remains open.

**2d. `pointer-design-tradeoffs...` conflates availability with accuracy.** [r]
Table 1 scores fixed pointers "Highest — always present, deterministic"; Table 2
gives them "Stale if source changes." A stale description is confidently wrong,
which is worse than an absent one — as this KB's own `stale-indexes` note argues.

**2e. `link-following-and-search...` misfiles skill descriptions.** [r] They are
placed under "link-following: local navigation with rich context," but load at
session start with no surrounding argument. By the note's own criterion they
belong on the search side, and the section's summary sentence is false for one of
its three members.

**2f. `fluid-resolution-switching` title overclaims.** [r] The title says KB
quality "should be measured by" fluidity; the body defers all measurement to open
questions.

**2g. `an-enforced-tag-readme` C2 is an unsurveyed universal negative.** [r] "No
Zettelkasten or LYT practitioner writes 'this map lists every note on the topic'
as an enforced promise." The note's pivotal move rests on it. Needs evidence or
weakening.

**2h. `charting-...-beyond-rag` has two soft spots.** [r] Its navigation-mode list
is not cut on one principle (a target type sits beside a task type), and its
"seems independent from navigation mode" was hardened by promotion into a
standalone note without being tested. Self-labelled brainstorming, which
discounts any disposition applied to it.

**2i. `human-llm-differences...` Navigation row is superseded in place.** [r]
`design-for-the-first-time-human` was written partly to correct it; the original
row was never retracted.

### What is notable about this channel

**Five of the seven open findings need no source at all.** 2b, 2d, 2e, 2f, and
2i are internal — scope errors, category errors, and self-contradictions
findable by reading the note against itself and its dependents. So **Channel 2
is only partly blocked on Channel 1**, and the remaining operative item 2b is
among the unblocked.

That is the running result of this workshop restated: pointed at redundancy, the
method returned **three defects and zero clean rediscoveries a retirement would
tidily remove.** Two defects are repaired; the remaining operative item is 2b.

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

**Freshness note, 2026-08-25 [v].** At its certification freeze, the rollout had
a fresh standard grounding result for all 68 target notes: 34 PASS, 10 WARN, and
24 FAIL. That is a dated coverage result, not standing assurance. Later edits,
including the activation-note revision, require current freshness checks and
may require new reviews. Neither a fresh result nor its outcome settles an
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
unnamed social-media post in 1c still passes the trait contract. This remains a
candidate deterministic check.

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

1. **Continue with Channel 2's unblocked five.** Re-check 2b before changing it
   because ADR 026 rests on it, then repair 2d, 2e, 2f, and 2i. These need no
   source-corpus decision.
2. **Triage the received literature handoffs.** Separate the seven uses that now
   have matching tracked ingests from the nine that still lack a direct route,
   and decide whether the nine out-of-cohort notes belong here.
3. **Select the wider corpus from the claim inventory.** Source-grounding owns
   the selection; the V1 Quotes/snapshot path is ready to carry each result.
4. **Run the remaining migrations and source-dependent claim judgments** in
   small source-coherent batches.
5. **Record dated artifact dispositions and execute one end to end.** A claim
   correction does not substitute for the first keep, merge, thin, or retire
   decision with all required rewiring.
6. **Close the two general questions.** Promote a disposition rule or record
   that judgment remains per-note, and decide the unresolved prior-art check.

Bulk migration still should not precede source selection. The machinery is no
longer the blocker; choosing evidence from the wrong tradition is.
