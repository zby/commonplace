# Fifth-episode record: the Naur note's drift under repair

**Posed by:** the operator (Zbigniew Lukasiak), 2026-08-26, after watching one note drift through a write → full pass → trim → rewrite cycle in a single day. Opened as the workshop `editorial-drift-under-repair`; folded into the Popperian-maintenance workshop the same day as its fifth episode's record. Direction: retain the episode with its evidence and work out what, if anything, is durable.

**Goal.** Understand how a note whose motivation was clear ended up, after a sequence of individually justified edits, asserting something different and weaker — and whether the mechanism is a property of the improvement pipeline that deserves a library note, an instruction change, or nothing.

**What closes it.** Closes with the parent workshop. The durable candidates are listed in [fifth-episode-critique-without-repair.md](../fifth-episode-critique-without-repair.md); `kb/log.md` already carries a FIX entry dated 2026-08-26.

**Evaluation boundary.** Pipeline behaviour and the resulting texts only. Whether the final Naur reading is *correct* is the note's own business (`kb/notes/naur-binds-theory-to-humans-via-premise-that-machines-follow-rules.md`); here it matters only that the final version returned to the original motivation and survived grounding.

## The drift, step by step

| Step | Time (2026-08-26) | Artifact | Title-level claim | What moved it |
|---|---|---|---|---|
| v0 | 13:48 | `versions/v0-first-draft-cp-skill-write-13-48.md` | *Irreducibility to rules bounds text alone, not text plus an interpreter* — plus "Naur's thesis has an argued half and an assumed half", "in 1985 the candidate set was empty" | `cp-skill-write`, given the motivation below; wrote against the ingest's **five** retained quotes and judged them "sufficient" |
| v1 | 14:36 (committed 14:41, `def1280a`) | `versions/v1-full-pass-reframe-def1280a.md` | *Naur's retained passages do not establish a human-only theory bearer* | full pass `20260826T115728Z-a18058`, disposition `keep (reframe)`: premise-decomposition GLOBAL defeat (halting-decider counterexample to the universal "irreducibility"), `semantic/grounding-alignment` FAIL (source-wide "assumed" claim from a quote subset), critique |
| v2 | 15:22 (`4d707961`) | `versions/v2-defensive-trim-4d707961.md` | same | operator asked whether v1 had accumulated defensive talk; 969 → 677 words, same claims, each limit stated once |
| v3 | ~16:30 (committed `eac2b0b8`) | `versions/v3-essay-level-rewrite.md` | *Naur binds program theory to humans through the premise that machines only follow rules* | operator: "argue about the full article, not retained passages"; full snapshot read; four `cp-skill-ground` runs (5 → 18 quotes); file relocated |

### Second cycle, same day

| Step | Time | Artifact | Title-level claim | What moved it |
|---|---|---|---|---|
| v4 | ~17:40 | `versions/v4-second-pass-reframe.md` | *Naur's rule-inexpressibility argument does not by itself bind program theory to humans* | second full pass `20260826T140020Z-7c9e` on v3, disposition `keep (reframe)`: critique and premise gate defeated v3's "a trained interpreter falls outside Naur's partition" (an LLM *is* formal symbol manipulation on a computer; an induced decision tree is learned yet an explicit rule set), plus real grounding faults (universals over the essay, unsourced 1985 motive, "only personal advice repaired") |
| v5 | ~18:10 | `versions/v5-bridge-as-equation.md` | *Naur binds program theory to humans by equating machine execution with formulated criteria* | operator review of the v4 packet: the defeat of v3 was correct, the repair retreated to a bare logical point ("needs an additional premise") plus a three-level taxonomy the closing gates found partly unused; the operator's correction — at the time, execution by machine meant formal interpretation of formulated rules, so the bridge was accurate for its day and trained recognizers *separated* execution from formulated criteria rather than falling outside a partition |

**The twist in cycle 2.** The pass caught a genuine error in v3 *and* drifted: it replaced a wrong strong claim with a true weak one, and recorded the contribution as *strengthened* against its own reframed update. Both things are true at once, which is why "the gates found real defects" cannot be the test of whether a repair was right. The v5 claim is stronger than v3, v4, and v0, and it came from reading the objections against the motivation rather than against the incumbent text.

Pass-2 evidence: `evidence/pass2-full-pass-report.md`, `evidence/pass2-initial/` (critique, friction, premises), `evidence/pass2-closing/` (same). One further `cp-skill-ground` run retained the section 6 program-life passage (19 quotes).

**Motivation as stated before v0** (session discussion): Naur's thesis splits into an argued half — text cannot carry the application judgment a program's theory needs — and a second half, that only a person can hold it, which the operator did not accept. The intended note was about that second half. v3 is the first version that actually says what the motivation said, and it says it more strongly than v0 did: the human binding is *argued* in the essay, from an identifiable premise (machine = formal symbol manipulation = rule-following; §2, §5, §6, §8), and that premise is what a trained interpreter contests.

**Where v0 went wrong.** Two overreaches, both caught correctly by the pass: it generalized to every "irreducibility" argument (false — impossibility results over the whole effective procedure reach text and interpreter together), and it asserted the human premise was *assumed* across the essay while reading five quotes.

**Where v1 went wrong.** The pass repaired the grounding failure by making the evidence set the qualifier — "retained passages do not establish…". True, defensible, and no longer a claim about Naur or about the world: a claim about what this KB had retained. The subject did not narrow (compare the subject-narrowing escape in `kb/notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md`); the *evidence scope* became the claim's boundary.

**Why the pass did that.** Step 7 of the full pass has "narrow the claim" as an operation and no "extend the evidence" operation: `cp-skill-ground` sits outside the pass, and `grounding-alignment` judges against the retained quotes as fixed evidence. When a note's motivation exceeds its retained grounding, the cheapest in-pass repair is to bound the claim by the grounding — even when the full source sits in `kb/sources/.snapshots/`, as it did here. The closing cycle then recorded the contribution as *preserved*, because it compared v1 against v1's own reframed update, not against the motivation.

## Analysis

The analysis of this episode as a case of the pass working as critique and failing as repair is [fifth-episode-critique-without-repair.md](../fifth-episode-critique-without-repair.md). This directory holds the record; that file holds the argument and the candidate design consequences.

## Raw theoretical part (unreviewed)

Candidate claim: **a repair loop that can narrow a claim but cannot extend its evidence drifts the claim toward the retained evidence.**

- Third escape from counterexamples beside widening vocabulary (`generality-bought-to-avoid-counterexamples-is-paid-for-in.md`) and narrowing the subject (`narrowing-bought-to-survive-review-is-paid-for-in-content.md`). Same generator — repair that optimizes defensibility — different shape: the result is true and non-analytic, but about the evidence set instead of the world.
- Candidate guard, the **evidence-scope test**: if a repair adds a qualifier that names the evidence set ("retained passages", "the quoted sections", "in the sampled runs") rather than a property of the subject, check whether the evidence can be extended before accepting the narrowed claim. A claim bounded by its evidence is a report on retention, not a claim about its subject.
- Scope of the failure: honest evidence-bounding is legitimate when the source is unavailable or the wider claim is false. The failure mark is the **available-but-unread source**.
- Possible instruction consequence: step 7 could route a `grounding-alignment` FAIL to a grounding request (`cp-skill-ground` with the source-side claim the note needs) before choosing between reframe and keep, at least when a pinned snapshot exists. Untested; would change the pass's "steps 1–7 only write reports" invariant only if grounding counts as a report-side operation (it edits the ingest, not the note).
- Open: is the v0 overreach itself the same mechanism in the writing direction? `cp-skill-write` judged five quotes "sufficient" for claims it had shaped to fit those quotes, then generalized past them. Writing against a quote pool rather than a source may produce the overreach that the pass later narrows back to the pool — two halves of one loop that never reads the source.

## Evidence

- `evidence/full-pass-report.md` — the reconciled packet (warranted contribution, disposition, body edits, routed attention, gate table, closing cycle). Copied from the gitignored `kb/reports/full-pass/…/20260826T115728Z-a18058/`.
- `evidence/initial/` — critique, friction, premises, compression bundle, and the `semantic/grounding-alignment` FAIL that drove the reframe.
- `evidence/closing/` — closing critique (attack "partially lands": exegetical force of "someone"/"programmer", unsupported narrow reading of "rules"), friction, premises.
- `versions/` — the six texts, v0 through v5.
- Git: `def1280a` (v1), `4d707961` (v2), `eac2b0b8` (v3); v4 was never committed; v5 in the commit that adds cycle 2.
- Session: <https://claude.ai/code/session_017dDJmV15wVzPkVffW1eLEh> — the motivation discussion (Naur, Ryle's regress, the "only humans" objection), the v2 trim, the full-essay read, and the four grounding runs. The pass itself ran in a separate operator session.
- `kb/log.md` FIX entry dated 2026-08-26 keyed on the pass id.
