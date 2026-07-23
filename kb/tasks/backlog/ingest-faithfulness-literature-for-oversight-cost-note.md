# Ingest faithfulness literature and restore citations in the oversight-cost note

## Status
complete

## Prerequisites
- [ ] none

## Goal
The two external papers that anchor the faithful-vs-plausible distinction are captured as `kb/sources/` ingests, and `kb/notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md` cites them as in-KB source links where the argument uses them.

## Context
- Papers to ingest (links verified 2026-07-22):
  - Jacovi and Goldberg (2020), "Towards Faithfully Interpretable NLP Systems: How Should We Define and Evaluate Faithfulness?", ACL 2020 — <https://arxiv.org/abs/2004.03685>, <https://aclanthology.org/2020.acl-main.386/>. Supplies the faithful-vs-plausible distinction: a faithful explanation reflects the process behind a decision; a plausible one merely convinces a reader.
  - Turpin, Michael, Perez, and Bowman (2023), "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting", NeurIPS 2023 — <https://arxiv.org/abs/2305.04388>. Evidence that a fluent chain-of-thought rationale can systematically omit the factors actually driving the answer.
- Relevant files:
  - `kb/notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md` — the note that dropped these citations pending ingestion; "The condition is faithfulness, not legibility" is where they attach.
  - `kb/sources/llm-agents-are-not-always-faithful-self-evolvers.md` — already-captured neighbor; its related-work section cites Turpin et al., useful for cross-linking the ingests.
- How to verify / reproduce:
  - Both ingests exist under `kb/sources/` and pass `commonplace-validate`.
  - The note's faithfulness section cites the ingests; footer carries evidence/derived-from entries for them.

## Decision Record
- Decision: cite from ingested sources rather than from parametric memory; the note shipped with bare concepts and this task carries the deferred literature work.
- Follow-ups: consider whether the Jacovi-Goldberg graded-faithfulness point (they argue against a binary notion) should soften the note's binary faithful/unfaithful phrasing.

## Tasks
- [x] Ingest Jacovi and Goldberg (2020) via `cp-skill-ingest`
- [x] Ingest Turpin et al. (2023) via `cp-skill-ingest`
- [x] Restore the two citations in the oversight-cost note's faithfulness section, linking the ingests
- [x] Run `cp-skill-connect` on the note afterward

## Current State
Complete. Both papers are captured as cleaned, metadata-stamped snapshots and validated ingest reports. The oversight-cost note cites the Jacovi-Goldberg ingest for the faithful/plausible distinction and the Turpin et al. ingest for controlled behavioral evidence. A post-connect report for the note records the source edges, reverse-edge candidates, and the graded-faithfulness caveat.

## Notes
- arXiv was unreachable from the remote session that created this task (proxy 403 on arxiv.org and export.arxiv.org); if that recurs, use the ACL Anthology page for Jacovi-Goldberg or run the ingest from an environment with arXiv access.
