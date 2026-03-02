---
description: Reference framework for automated text testing — contracts per document type, test pyramid (deterministic/LLM rubric/corpus), production workflow
type: note
traits: [has-external-sources]
areas: [document-system]
status: current
---

# Text testing framework — source material

Full framework for automated testing of text artifacts, received 2026-02-21.
Saved as reference for when we start building concrete checks.

See [automated-tests-for-text](./automated-tests-for-text.md) for the distilled observation.

---

## 1) Think in terms of a text "spec" (contracts)

Software tests work because there's a spec, even if it's implicit. Free text can have specs too, for example:

* **Structural contract:** must include sections (Summary / Decision / Next steps), must be under 250 words, must include an owner + date.
* **Audience contract:** written for "new joiners," avoid internal slang, define acronyms.
* **Tone/voice contract:** friendly but direct, no hype, no moralizing, no sarcasm.
* **Safety/privacy contract:** no secrets, no personal data, no legal/medical claims without disclaimers.
* **Truthfulness contract:** claims must be either cited, explicitly labeled as assumptions, or consistent with a reference corpus.
* **Actionability contract:** at least 1 concrete next action, deadlines in ISO dates, no ambiguous "soon."

Once you have contracts, you can test them.

## 2) A "test pyramid" for text

### Level A — Deterministic checks (fast, cheap, reliable)

* Length / reading time / sentence length
* Formatting & required sections
* Forbidden phrases / banned claims
* Link validity / citation presence
* Terminology consistency
* Dates & numbers
* PII/secret scanning

### Level B — LLM rubric graders (medium cost, high coverage)

* Prompt + rubric + examples → structured JSON (pass/fail + reasons + spans)
* "Does the note contain a single clear thesis in the first 2 sentences?"
* "Does each claim have either a source, or is it explicitly tagged as assumption?"
* "Is there a concrete next step with owner + date?"
* "Is the tone aligned to our style guide?"
* "Is there any internal contradiction?"

### Level C — Cross-model / adversarial checks (slower, higher confidence)

* N-of-M voting
* Two-model agreement
* Adversarial prompting
* Metamorphic testing

## 3) Testing meaning indirectly

### Metamorphic tests

* Paraphrase invariance
* Summarization invariance
* Reformat invariance
* Reverse test (generate Q&A, check consistency)

### Claim extraction + verification

1. Extract atomic claims
2. Entailment check against source corpus
3. Contradiction check
4. Missing citation flag

## 4) Compatibility with a collection of texts

* No contradictions with existing docs
* Terminology + ontology alignment
* Style/voice consistency
* Duplicate / near-duplicate detection
* Coverage and linking behavior
* Update compatibility (supersedes, migration notes)

## 5) Production workflow

1. Pre-commit / local lint — structure, length, banned phrases, PII
2. CI unit tests — deterministic + basic rubric
3. CI integration tests — contradiction, taxonomy, duplication
4. Human review for edge cases
5. Regression suite with golden notes

## 6) Failure modes

* LLM judges not deterministic → voting, multi-judge
* Judges can be lenient → adversarial critique passes
* Corpus checks miss context → improve retrieval, require citations
* Over-testing early → start with 10-20 high-value checks

## 7) Minimal starting checklist

Single-note: required sections, max length, next step with owner, no relative dates, acronyms defined, no PII, clarity rubric, main point in first 2 sentences.

Corpus: top-5 similarity contradiction check, threshold linking, glossary alignment.

Topics:
- [document-system](./document-system.md)
