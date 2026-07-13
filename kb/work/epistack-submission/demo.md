# The one-command adversarial demo

**Claim:** a conforming casebook's quotations pass its own checker — and you can falsify that in one command.

This is the entry's most legible guarantee. Every other property (semantic review freshness, model partitions, the compounding backlog) takes reading to appreciate. This one you *run*. The whole point of the brief's "stands up to adversarial pressure" is that a skeptic can attack the artifact directly; here the skeptic runs the checker, breaks a citation, and watches the checker catch it.

You do not need to trust that we verified our quotations. You verify them.

---

## What the checker does

`commonplace-verify-quotes` takes every quotation a casebook marks `verbatim`, follows the citation to the retained source snapshot it points at, and compares the quoted text against the snapshot **exactly**. A mismatch — a dropped word, a silent `[bracketed]` substitution, a case change, punctuation moved inside the quotation boundary — is a **failure**, not a warning.

This is claim-level provenance for the claims that carry the most adversarial weight: the ones in quotation marks, attributed to a named source, in a contested debate. It is deterministic. There is no model in the loop and nothing to argue with — the quoted string either is or is not in the snapshot.

---

## Run it (≈30 seconds)

From a checkout of the casebooks repo, with the `llm-commonplace` package installed:

```bash
# 1. Verify every verbatim quotation in a case against its snapshots.
commonplace-verify-quotes kb/covid/

#    Clean output means every quoted claim resolves exactly against
#    the source it cites. That is Level-1 (Referential) conformance.
```

```bash
# 2. See a successful check, not just the silence of no failures.
commonplace-verify-quotes kb/covid/ --show-matches
```

```bash
# 3. Now attack it. Edit any verbatim quotation in a note — drop a
#    word, change a number, swap a term — and re-run:
commonplace-verify-quotes kb/covid/notes/<some-note>.md

#    The checker reports the mismatch: the note's text, the snapshot's
#    text, and the file. The tampered citation fails. Undo the edit and
#    it passes again.
```

That is the demo. A citation you can break and watch break is worth more than a paragraph asserting citations are trustworthy.

---

## Why this is the right demo to lead with

**It is falsifiable by the judge, not narrated by us.** The brief's top question is "would this help someone reason about this case" and its adversarial-pressure clause asks whether the artifact survives attack. A judge who breaks a quotation and sees the checker catch it has *tested* the guarantee, not read a claim about it.

**We failed it first, in writing.** The first sweep across the demonstration casebooks found **18 mismatches out of 87 candidate quotations** — real failures of the strict assertion: editorial omission, bracketed substitution, case changes, punctuation crossing the quotation boundary. We report the pre-repair number because a checker whose own corpus passed on the first try is a checker no one stressed. The 18 are the fix queue; the repaired corpus is what ships, and *"a submission whose citations pass its own checker"* is the deliverable — with the failure baseline on the record so the pass means something.

**It generalizes with zero case-specific code.** The same command runs on `kb/lhc/` and `kb/eggs/` unchanged. The checker knows nothing about virology, particle physics, or nutrition — it knows citations and snapshots. That is the protocol's "standardize the connective tissue" rule paying off: the adversarial guarantee is domain-independent because it operates on provenance, not substance.

**It sits exactly on the honest architectural frontier.** Quote verification is a *referential* check — its ground truth lives in a second artifact (the snapshot), reached by dereferencing a citation. That is a distinct class from schema validation, and the entry names it as such (protocol §5.3), including that a *general* referential-check engine is identified future work. The demo shows one worked, shipped member of that class; it does not pretend the class is finished.

---

## Full deterministic check, for the thorough judge

Quote verification is one of several deterministic checks. To run structural conformance (schema validity, required sections, link health, orphans) alongside it:

```bash
commonplace-validate kb/covid/          # structural conformance (Level 0)
commonplace-verify-quotes kb/covid/     # referential conformance (Level 1)
```

A casebook that passes both is Level-1 conformant: every artifact is well-formed, every link resolves, and every quoted claim is exactly what its source says. Semantic review (Level 2) is the archival LLM layer and is not a one-command demo — it is the freshness-tracked, partition-scoped judgment the protocol document describes.

---

## Scope honesty

- **"One command" is the *checking* path, not the *install* path.** Reading and verifying a casebook needs the package installed and the snapshots present; standing up a new casebook from scratch is real setup, documented in `INSTALL.md`. The claim here is scoped to the adversarial check, which is the part a judge most wants to run.
- **The checker verifies fidelity, not truth.** A quotation passing means the casebook quoted its source accurately — not that the source is correct. That distinction is the whole protocol: deterministic checks guard the connective tissue; the substance stays in attributed prose for the reader to judge.
