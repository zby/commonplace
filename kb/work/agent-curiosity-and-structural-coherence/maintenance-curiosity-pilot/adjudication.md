# Adjudication notes — do not supply to runners

## Standing

These are pre-run hypotheses, not answer keys. Historical edits and current repository state constrain plausible outcomes but do not make one wording or disposition uniquely correct. Before scoring, an independent maintainer should confirm each target's material facts and reclassify or exclude any supposed control with consequential drift.

## Cohort hypotheses

| ID | Semantic-age estimate | Pre-run hypothesis | Current evidence worth checking | Plausible disposition |
|---|---|---|---|---|
| P01 | Claim introduced 2026-03-12; later changes appear mechanical | The overlap-detection claim remains useful. “Index” may now include curated heads or scoped title listings, but that need not defeat the mechanism. | Current navigation and title-as-claim notes still rely on claim-shaped pointers. Check whether the numerical index-size rhetoric or examples mislead. | `keep`, or a narrow terminology revision if consequences change. |
| P02 | Core text dates to the initial corpus; later changes appear vocabulary/path migrations | The final statement that none of the text-testing pyramid has been built is false. Deterministic validation, semantic review gates, collection/type conformance pairs, and corpus-level signals now exist. | `commonplace-validate`, validation contract, review system, and text-testing framework. | Revise current-state paragraph while preserving the general testing argument; possible merge if the newer framework fully subsumes it. |
| P03 | Introduced as a standalone claim on 2026-05-20 | The partial-evaluation argument and its explicit analogy limits remain current. | Current frontloading and instruction-generation material should either corroborate or expose a changed boundary. | `keep` unless a specific contradiction is found. |
| P04 | Main argument broadened 2026-03-12; later edits largely mechanical | The suppression asymmetry remains useful, but the Commonplace implementation section describes retired `areas:`, Topics, `docs/indexes.md`, and hand-maintained membership. | ADR 004 replaced areas with tags; ADR 025 moved complete listings to build time; ADR 026 introduced curated tag heads with enforced marks. | Revise or split durable theory from historical implementation. Do not discard the general claim merely because the old defense changed. |
| P05 | Main claim split out by 2026-03-12; later changes are mostly migrations and linking | The indirection-cost boundary remains current and already distinguishes static from runtime values. | Current frontloading and instruction-generation paths should show whether the practical example remains representative. | `keep`, or narrow current-example repair. |
| P06 | Core argument is early; history contains many migrations and some later caveat work, so exact semantic date is uncertain | The durable distinction between claim-shaped titles and structured arguments remains current. The note also retains historical counts, enum-era migration language, current-tense `has-claim` statements, and implementation directions already resolved by path-valued types and current contracts. | Current notes collection contract, structured-claim type, ADR 012, ADR 018, and collections/types reference. | Revise substantially, or split historical design rationale from the surviving theoretical distinction. Retirement is plausible only if current contracts and ADRs fully carry the useful reasoning. |
| P07 | Argument redistributed and revised through 2026-04-06; later changes mainly citations, paths, and links | The distinction between locally contextual link-following and low-context search remains current, with later work extending rather than replacing it. | Navigation, link vocabulary, generated-index ADR, and pointer-design note. | `keep`, possibly narrow wording updates. |
| P08 | Last evident current-state maintenance around 2026-04-09; core proposal is older | The title's recommendation has been implemented. The body still describes `/validate` as an all-LLM skill and presents a validator as future work, while the listed hard/soft split now exists across `commonplace-validate` and semantic review. Some enumerated fields and paths are historical. | Commands, validation contract, ADR 047, collections/types reference. | Revise into an observed/promoted claim or retire/merge into current validation theory while preserving the hard/soft oracle distinction. |

## Adjudication cautions

- P02 and P08 share current evidence but ask different maintenance questions: whether text testing exists versus whether deterministic validation should be scripted. Do not count recognition of one as automatic success on the other.
- P04 is the key claim/state-splitting case. A wholesale deletion because `areas:` is obsolete loses the supported suppression mechanism.
- P06 is intentionally harder and may support several operations. Score whether the runner identifies the live distinction and the obsolete design state, not whether it guesses one preferred file operation.
- Controls are not required to receive literal `keep`. A narrow correction can be valid; the failure is unsupported churn or a claim-level rewrite without consequential evidence.
- A runner that notices drift only after receiving the supplied neighborhood demonstrates contextual reachability, not open question origination.

