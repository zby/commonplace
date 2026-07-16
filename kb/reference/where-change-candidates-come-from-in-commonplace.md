---
description: "Surveys how problem-noticing and candidate-drafting happen in Commonplace beyond a maintainer's own judgment — skills, ephemeral reports, mechanical checks, freshness tracking, agent initiative"
type: kb/types/note.md
tags: [foundations, computational-model, self-improving-systems]
---

# Where change candidates come from in Commonplace

[A proposal-selection improvement loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) needs search — noticing a problem, generating a candidate — before evaluation or retention can act on anything. [Commonplace as a partially autonomous, reflective self-improving system](./commonplace-as-a-reflective-system.md) traces one instance of that — a maintainer noticing the `index` type doing two jobs, an agent formulating the fix as ADR 026 — and reads Search as split: non-reflective and human where the noticing happened, reflective and autonomous where the agent formulated the candidate. That single trace understates how much of this Commonplace channels through its own mechanisms rather than a maintainer's unaided judgment; this note surveys the wider set.

## Candidate formulation is channeled through self-representation

Channeling search through self-representation is not unique to editing a self-representing artifact. Every note `cp-skill-write` drafts — a theory note, an instruction, a skill alike — has its candidate shaped by self-representation before a word is written: the skill's own steps require reading the target collection's `COLLECTION.md` for its conventions and linking rules, then the named type spec for the artifact's shape (`kb/instructions/cp-skill-write/SKILL.md`, Steps 2–3). Search's candidate-generation function, not only evaluation or retention, routes through self-representation as a matter of course.

`cp-skill-connect` takes part too, even though its own output is ephemeral — a gitignored report that is never itself committed. Some procedures fold its candidates back into a note automatically: `cp-skill-ingest` runs connect as a fixed step and distills its findings straight into the durable ingest report (`kb/instructions/cp-skill-ingest/SKILL.md`, Steps 2–4). Others leave the folding to a later, separate act: `cp-skill-write` only suggests connect as the next step, and turning its candidates into authored links is a choice made afterward, by a human or an agent. An ephemeral artifact can still do search's work — the report itself is discarded, but what a later step does with it need not be.

## Noticing is not purely human either

The ADR 026 trace's own third change — the `covered_by` check catching what the `rg` recipe had missed, described in [Commonplace as a reflective system](./commonplace-as-a-reflective-system.md) — is a case in point: a symbolic check noticing a gap no human had, not a maintainer's insight.

Commonplace also keeps designed channels for noticing besides a maintainer's own attention. [`kb/log.md`](../log.md) is an append-only observation log, rarely used in practice. `cp-skill-connect`'s Maintenance Observations section is a best-effort signal that surfaces on every connect run. And `commonplace-freshness-status` is a more systematic one: it compares each registered target's accepted input snapshots against current text and flags drift automatically, so a note or criterion changing since a baseline was accepted becomes a visible staleness signal without anyone reading for it (`kb/reference/freshness-architecture.md`). It is new and unproven at scale, and v1 registers only `review-pair` targets — the general theory-to-implementation lineage this note's companion trace already names as mostly absent is exactly what a wider freshness substrate would still need to cover. None of the four — mechanical check, log, connect report, or freshness status — closes the loop unattended: promoting an entry from any of them into an actual candidate still needs an explicit maintenance or triage step nobody has automated.

## Agent initiative is part of the mechanism

None of this runs on rails. The instructions above name conventions to read and steps to take, not which specific files answer a given question — deciding that is the agent's own initiative under a direction the human left general. This note is itself an instance of it: asked only whether the reflective-system note's "search is human" framing undersold the story, choosing which files would confirm or complicate that claim — `cp-skill-write`'s steps, `cp-skill-connect`'s report semantics, `kb/log.md` — was the agent's initiative, not a lookup the human specified in advance.

`cp-skill-write`, `cp-skill-connect`, `kb/log.md`, mechanical checks, freshness status, and agent initiative are illustrations, not a catalogue. Noticing and candidate-drafting in Commonplace run through a rich ecosystem of self-representing mechanisms and agent judgment together, and more of it goes unnamed here than named.

---

Relevant Notes:

- [Commonplace as a partially autonomous, reflective self-improving system](./commonplace-as-a-reflective-system.md) — evidence: the ADR 026 trace this note generalizes beyond
- [The tag-readme change as an observed causal-connection trace](./tag-readme-trace-observed-causal-connection.md) — evidence: the full walkthrough of the agent-assisted drafting this note's opening trace summarizes
- [The tag-readme trace read as a self-improving loop](./tag-readme-trace-as-self-improving-loop.md) — evidence: reads the same agent-assisted drafting as the reflective, autonomous half of Search
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: defines the search function this note catalogs mechanisms for
- [Freshness architecture](./freshness-architecture.md) — evidence: the newer, systematic staleness-noticing mechanism, still limited to review-pair targets
