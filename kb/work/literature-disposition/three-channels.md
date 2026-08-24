# Three channels: migration, claims, machinery

Everything the 2026-08-24 sweeps turned up, sorted by **what kind of change it
is** rather than by which note it came from. The three channels have different
owners, different risk, and different blockers, and mixing them is what makes a
corpus cleanup stall.

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
error this workshop exists to catch, one level up.

---

## Channel 1 — Migration

The defect here is almost never that a claim is wrong. It is that **nothing
routes a reader from the claim to what would settle it.** Four of the first six
notes cite nothing external for claims placed in an outside tradition; the
remaining two name traditions with zero works.

### 1a. Route existing claims to sources

| Artifact | What is missing | Status |
|---|---|---|
| `agents-navigate-by-deciding-what-to-read-next` | C1–C3 are information scent, cited to nobody. Ingest now exists | [v] |
| `linking-theory` | Same tradition, no citation; the Pirolli ingest's own recommended action names this artifact | [v] |
| `index-curation-adds-orientation...` | LIS pathfinders / annotated bibliographies / PKM MOC. **Attribution already exists one hop away** in `an-enforced-tag-readme`, which links back here — may be a move, not an invention | [v] |
| `an-enforced-tag-readme...` | "Luhmann" and "Nick Milo's LYT" named with no dated work, no URL, no ingest | [v] |
| `knowledge-storage-does-not-imply-contextual-activation` | Five LLM-side ingests cited; **nothing** for the cognitive-psychology tradition establishing C1/C2 | [r] |
| `stale-indexes-reduce-discovery...` | Zero external references and no `Relevant Notes` tail at all | [r] |
| `addressability-grain...` | Zero external references | [r] |
| `pointer-design-tradeoffs...`, `link-following-and-search...`, `design-for-the-first-time-human...`, `charting-...-beyond-rag` | Zero external citations for claims placed in outside traditions | [r] |

### 1b. The standing-TODO batch

Three artifacts carry explicit "survey is from training data, not systematic"
TODOs inside these traditions: `links-README.md`,
`title-as-claim-enables-traversal-as-reasoning.md`,
`information-value-is-observer-relative.md`. **One batch, not three.** [v] for
the first, [r] for the others.

### 1c. Repair a false provenance signal

`a-knowledge-base-should-support-fluid-resolution-switching` declares
`traits: [has-external-sources]` on the strength of "a social media post on 'The
Art of Good Thinking: Moving Between Levels'" — no author, no URL. [v] Either
identify the source or drop the trait; a provenance signal pointing at nothing is
worse than none.

### 1d. Blocked on a corpus decision

Most of 1a cannot be executed until the sibling workshop decides which sources to
capture — and that decision was **reopened** by the scoping finding. The needed
corpus is not the navigation corpus originally proposed; see
[claim-inventory](./claim-inventory.md). Only the two rows with a live ingest are
executable today.

---

## Channel 2 — Claims to change

Ordered by whether a shipped artifact depends on the claim.

### Operative — an ADR or type spec rests on it

**2a. `index-curation-adds-orientation-that-generation-cannot-produce` is
unscoped.** [v] An LLM can generate groupings and role annotations; what
*deterministic build-time* generation cannot do is produce them **verifiably**.
The note's only evidence concerns bottom-up auto-aggregation. ADR 025:69 and ADR
026:69 both `rests-on` it. **Scoping it does not destabilize either** — both
concern build-time generation, so the scoped claim is all they need. The note
overclaims past its own dependents. Title change implied.

**2b. `stale-indexes...` C1 may be analytic, not empirical.** [r] It stipulates
the stopping behaviour into the comparison, so the conclusion holds by
construction and the claim cannot fail — yet ADR 026 treats it as a finding, "the
problem in [this note] in its sharpest form." The empirical claim the ADR needs —
that agents in fact stop at an apparently complete head — is assumed, not argued.
Re-check the wording before acting; if it holds, this needs either evidence or a
restatement that can fail.

### Prose-only — no shipped artifact depends on it

**2c. The pointer-context monotone.** [v] "The more context a pointer carries,
the cheaper the navigation decision" merges estimate quality with interaction
cost. Two sites: `agents-navigate-...` and its verbatim copy at
`linking-theory.md:17`. Fully swept — [one inheritor, zero operative
reach](./c4-propagation-sweep.md), and `linking-theory` already states the
corrected form in its own thesis, description, and prediction 4. **The repair is
delete-and-promote, not rewrite.**

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

**Six of the nine need no source at all.** 2a, 2b, 2d, 2e, 2f, 2i are internal —
scope errors, category errors, and self-contradictions findable by reading the
note against itself and its dependents. So **Channel 2 is only partly blocked on
Channel 1**, and the operative items 2a and 2b are among the unblocked.

That is the running result of this workshop restated: pointed at redundancy, the
method returned **three operative defects and zero clean rediscoveries a
retirement would tidily remove.**

---

## Channel 3 — Machinery

### In flight

**3a. The claim-pull procedure.** Read the source, extract the claim, add it to
the ingest if missing, then use it. Two arguments and four open decisions in
[the candidate](../source-grounding/candidate-procedure-claim-pull.md).
Being implemented separately.

### Needs a proposal

**3b. Verbatim-quote retention under ignored snapshots.** [v]
`commonplace-verify-quotes` returns **0 match, 0 mismatch, 12 unresolved** over
1257 tracked files, and all twelve candidates cite internal notes rather than
sources. ADR 046 requires "the source snapshot is a checked-in file present at
validation time"; `kb/sources/` declares snapshots non-authority, ignores them,
and forbids linking to them. Four options, none selected. **This is the direct
blocker on Channel 1 being checkable rather than merely present.**

**3c. The ingest needs a claim ledger.** [v] Three of four needed extractions
land, but only scope conditions are actually *asked for*; the transfer argument
arrives voluntarily and the overlap arrives against a contract that says to "drop
weak, speculative, or duplicate edges" and defines value as "what is new." A
premise a note leans on is often the least novel thing the source contains.

**3d. No write-time check asks whether the literature already settles a claim.**
[v] Every novelty and economy test in the corpus is intra-KB — the log-entry
novelty battery, `cp-skill-write`'s duplicate guard, and all four attribution
gates, which audit attribution to *already-cited* targets and never require that
a source exist.

**3e. Nothing checks that a provenance trait points at something identifiable.**
[v] `has-external-sources` can be asserted against an unnamed social-media post
(1c). This looks like a deterministic check — a declared external-source trait
implies at least one resolvable external reference.

### Bugs

**3f. `commonplace-verify-quotes` scans ignored files.** [v] It walks into
`.snapshots/` and tries to resolve a mangled URL as a file path
(`kb/sources/.snapshots/http:/memory.md`).

**3g. `cp-skill-snapshot-web` cleanup blocks on equation-heavy PDFs.** [v] The
mandatory model-mediated Markdown conversion re-emits the whole document and hit
a content filter. A fix is in flight in another session.

### Rules, not code

**3h. Decide the corpus from the claims, not the cluster's name.** [v] The cohort
was scoped to foraging/LIS from note titles; its claims actually place across
cognitive psychology of memory and transfer, human-factors automation bias,
materialized-view maintenance, single-source publishing, and storage read
amplification. The failure mode is not missing a source — it is reading
*rejection from the scoped tradition* as *no external tradition*, which nearly
happened to `addressability-grain`.

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

1. **Channel 2's unblocked six** need nothing and include both operative items.
   Cheapest real repair available.
2. **Channel 3b** gates whether Channel 1 produces checkable citations or merely
   present ones. Worth settling before bulk migration.
3. **Channel 1** waits on the corpus decision, which waits on 3h.
4. **Channel 2's remaining three** wait on the sources that adjudicate them.

The tempting order — migrate first, because it looks mechanical — is the worst
one: it would write uncheckable citations at scale against a corpus chosen from
the wrong shelf.
