# Writing-as-thinking → process transfer

## Goal

Harvest the still-unincorporated ideas from the four writing/thinking essays ingested 2026-08-10 and turn each into a Commonplace **process** change (review gate, FIX routing, connect/multistage step, writing convention) — or an explicit rejection with a recorded reason. The prior written-artifacts-in-learning-loops workshop (closed 2026-08-10) promoted two conjectures and closed, but its own ingests flagged ~20 extractable items and most were left as "scaffolding already covered." This workshop works that backlog.

## Why a workshop, and the one hard rule

The prior workshop was killed because it **accreted wrong ideas** faster than it tested them. So the governing discipline here is **discriminating-test-before-build**: no idea gets promoted to a durable artifact until a cheap one-note (or one-pair) test shows it has signal over what Commonplace already ships. An idea that fails its discriminator is *rejected in this README*, not built. Distilling the counterexamples that kill an idea is fine to do inline; do not reopen the closed workshop to mine them.

## What closes this workshop

Every candidate below reaches a terminal state: **promoted** (named library artifact) or **rejected** (one-line reason recorded here). When no candidate remains open, extract the survivors and delete this directory per `kb/work/COLLECTION.md`.

## Evaluation boundary

- These are **human** first-person essays. Transfer to an agent/KB process is a hypothesis, not an inheritance — `human analogies can motivate functions without determining component boundaries`. State each transfer as the behaviour/dependency a process must preserve, then test it.
- Changed human understanding, a retained artifact, and changed agent behaviour are different outcomes; do not call written output "learning" without the retention/activation/effect links.
- A candidate that only restates an existing gate or note is redundant, not novel — check the shipped gate catalogue (`kb/instructions/review-gates/`, `composition-friction-gate.md`, `critique-note.md`) before claiming novelty.

## Candidate backlog

Status ∈ {open, testing, promoted, rejected}. Method and first target are deliberately left to the live session.

| # | Idea (essay source) | Residual increment over what ships / what to discriminate | Status |
|---|---|---|---|
| 1 | **Premise-decomposition review** (how-to-think #2) | `composition-friction-gate` already decomposes into inferential *joints (edges)* and attacks each. Increment: decompose into *premises (nodes)* and test each for external support / counterexample. Discriminator: on one note, does the premise-node check surface a real weakness the joint check misses? | open |
| 2 | **Counterexample-scope routing** (how-to-think #1) | Classify a defeated point as *local* (defeats a premise → revise, keep title-claim) vs *global* (propagates to the conclusion → retire). Targets: `discovery-lifecycle.md` test branch and `FIX-SYSTEM`. Composes with #1. | open |
| 3 | **Value-of-information reading** (learning-by-writing #3) | Route the next read by *expected claim-change*, not retrieval relevance, in `connect` / `write-multistage`. Operationalizes the open question in the claim-routed conjecture. | open |
| 5 | **Stance-reversal operator** (learning-by-writing #4) | Routine "write the strongest note that contradicts this one" as an anchoring check in connect/review. Cheap; de-risks the claim-routed conjecture's own anchoring failure mode. | open |
| 6 | **False-precision anti-gate / "accurately-vague" register** (wordless #2) | A check for stating-as-settled what the evidence leaves open — the counter-pressure to constraining. `AGENTS.md` forbids invented precision but no gate enforces it. | open |

(#4, a killed-conjecture ledger, is deprioritized per maintainer: distilling counterexamples is useful but the closed workshop is not to be reopened.)

## Open discriminating tests carried in from the two promoted conjectures

- [descriptive-link-labels may supply claim self-sufficiency](../../notes/descriptive-link-labels-may-supply-claim-self-sufficiency.md) — a **label-ablation test (2026-08-10)** was run: 6/6 cold-reader PASS, gate never fired even de-labeled; it reassigned the mechanism from the label convention to the body-premise convention and left the **thin pre-connect-draft** case open. That thin-draft test is the cheapest remaining experiment.
- [claim-routed reading may beat reading-first for synthesis notes](../../notes/claim-routed-reading-may-beat-reading-first-for-synthesis-notes.md) — its head-to-head test (build one synthesis note both ways, compare warranted update vs context cost) is **deferred** by maintainer to control scope.

## Sources

- [How to think in writing](../../sources/how-to-think-in-writing.ingest.md) — Karlsson/Lakatos: conjecture, premises, local/global counterexamples (#1, #2)
- [Learning by writing](../../sources/learning-by-writing.ingest.md) — Karnofsky: hypothesis as inquiry-control state (#3, #5)
- [Putting ideas into words](../../sources/putting-ideas-into-words.ingest.md) — Graham: exact-word commitment + neutral-stranger reread
- [When is it better to think without words](../../sources/when-is-it-better-to-think-without-words.ingest.md) — Karlsson: expansion/compression phasing, false precision (#6)

## Bookkeeping

- Move each candidate to `testing` when its discriminator runs; record the verdict and the promoted/rejected outcome in this table's row before closing it.
- Run cold-reader / adversarial tests in fresh sub-agents (no sympathy for the framing), mirroring the label-ablation setup.
- Validate any promoted artifact with `commonplace-validate` before it leaves the workshop.
