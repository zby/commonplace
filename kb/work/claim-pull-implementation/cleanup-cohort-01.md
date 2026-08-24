# Cleanup cohort 01: Pirolli navigation claims

Frozen 2026-08-24 before any cleanup mutation. The source had already been read
by the pre-rule source-grounding and literature-disposition workshops, so this
cannot recreate a source-blind inventory. It preserves their target-first claim
inventory and pins the exact incumbents before the new procedure is applied.

## Freeze

Repository HEAD: `391c83213966c418e81e81a72b5958eac9b8c5e8`

| Target | Frozen blob | Last target commit |
|---|---|---|
| `kb/notes/agents-navigate-by-deciding-what-to-read-next.md` | `90a4c08c1e35dded6b8a392b3ce78529d1899ad9` | `d230455743fc4d6630af610af67d1b6c0fd7632b` |
| `kb/notes/linking-theory.md` | `e5914b43954d14f2076dfe1abe581cc0f756515f` | `13b143cd36862dd5de328664292318bd37cc52c2` |

The paired source is
`kb/sources/pirolli-proximal-information-scent-distal-content.ingest.md`.
Its name-paired snapshot has SHA-256
`dcbc565308e0a9eab683087f729137d462f8b6f0d5a8808f989b10b3095e1da2`,
which equals the ingest's `snapshot_sha256`; both files name the same canonical
source URL.

## Frozen target claims

The unit below is one target use, even where `linking-theory.md` imports wording
from the other note.

| ID | Target | Claim as frozen | Source-side need |
|---|---|---|---|
| AN-1 | `agents-navigate-by-deciding-what-to-read-next.md` | A pointer follow/skip decision is "the fundamental unit of navigation." | What unit or action choices Pirolli's Web-navigation account actually models. |
| AN-2 | `agents-navigate-by-deciding-what-to-read-next.md` | The pointer decision is probabilistic: estimate likely relevance and the cost of finding out. | Whether Pirolli joins cue-based relevance prediction and interaction cost at the individual pointer decision. |
| AN-3 | `agents-navigate-by-deciding-what-to-read-next.md` | Surrounding pointer context hints at target content, makes the decision tractable, and avoids loading the target merely to judge relevance. | What proximal cues disclose about unavailable distal content and what mechanism or avoided cost the source establishes. |
| AN-4 | `agents-navigate-by-deciding-what-to-read-next.md` | "The more context a pointer carries, the cheaper the navigation decision." | Whether the source varies cue quantity and establishes a monotonic navigation-cost effect. |
| LT-1 | `linking-theory.md` | Every link encounter can be modeled as follow or skip. | What unit or action choices Pirolli's Web-navigation account actually models. |
| LT-2 | `linking-theory.md` | The decision is always probabilistic because the target is unknown until it is loaded. | Whether Pirolli establishes that universal pointer-level formulation. |
| LT-3 | `linking-theory.md` | Surrounding pointer context hints at target content and makes the decision tractable. | What proximal cues disclose about unavailable distal content, without importing a target-loading mechanism. |
| LT-4 | `linking-theory.md` | "The more context a pointer carries, the cheaper the navigation decision." | Whether the source varies cue quantity and establishes a monotonic navigation-cost effect. |

The local claims about Commonplace pointer types, metadata investment, and
title-as-claim are outside this source cohort. Pirolli may motivate their premise,
but it cannot establish the transfer to LLM agents or Commonplace's design.

## Completion record

Populate this section only after grounding, target comparison, mutation,
validation, and source-conformance review.

| ID | Disposition | Target change | Validation | Source review |
|---|---|---|---|---|
| AN-1 | pending | pending | pending | pending |
| AN-2 | pending | pending | pending | pending |
| AN-3 | pending | pending | pending | pending |
| AN-4 | pending | pending | pending | pending |
| LT-1 | pending | pending | pending | pending |
| LT-2 | pending | pending | pending | pending |
| LT-3 | pending | pending | pending | pending |
| LT-4 | pending | pending | pending | pending |

Record any unavailable observation, append accumulation, or failed gate here;
do not silently reconcile or replace an incumbent Claims entry.
