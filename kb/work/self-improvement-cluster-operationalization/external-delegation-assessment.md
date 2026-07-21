# External-theory delegation — assessing the "thin semantic extension" proposal

The maintainer's direction (2026-07-21): use more external theories instead of developing everything locally — concentrate on what is special in the Commonplace machinery and cite established papers for the rest, buying robustness and shedding maintenance. An external ChatGPT review of the cluster endorsed this and proposed a delegation map (PDSA, MAPE-K, Argyris, Parasuraman, Bainbridge, assurance cases/GSN), five cleanup items, and a revision of this workshop's goal. This document checks that proposal against the actual state of the cluster and disposes of each item. Verdict up front: the *stance* is already the cluster's recorded design stance; the genuinely new content is the methodology-layer host decision (PDSA/MAPE-K) and the assurance-case suggestion; several cleanup items are stale or misdescribe what the notes contain.

## 1. What is already in place

The proposal's headline — "thin semantic extension over established methodologies, not a competing theory" — is not a new direction. It is the recorded design stance:

- **Conservative extension is the evaluation criterion.** [External-theory evaluation](./external-theory-evaluation.md) §0 fixes it: inherit wherever established theory suffices, extend only where the LLM-shaped capability outruns it, flag every extension. Findings 6 and 9 confirm the cluster already practices it.
- **The proposed "adapter" artifact already exists as a pattern.** The proposal asks for: snapshotted source, mapping into local vocabulary, explicit departures, local consequence. That is exactly the repo's `kb/sources/` snapshot+ingest discipline plus the Provenance sections in the definition notes (see [reflective system](../../notes/definitions/reflective-system.md)). No new artifact form is needed — only more instances of the existing one.
- **The Parasuraman inheritance has been executed.** The proposal treats it as pending ("once the provenance mapping is added"). It is added: [the source is ingested](../../sources/model-types-levels-human-interaction-automation.md) and the [profile note](../../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md)'s actor-allocation section records the form inheritance with the three flagged departures the maintainer specified in this README's Sequencing section.

So the decision on the table is not "adopt the stance" but "extend the stance from the theory layer (where it governs) to the methodology layer (the digest and change-process guidance this workshop will produce)."

## 2. Fact-check against current state

| Proposal claim | Current state | Consequence |
|---|---|---|
| The workshop goal "invites Commonplace to rebuild mature change processes" | The two-layer framework already blocks upfront methodology construction: digest content is promoted from observed fallback traffic, not designed | The risk is real but already has a guard; the goal revision makes the guard explicit rather than adding a new one |
| Parasuraman mapping "to be added" | Added (source ingested, profile note carries the inheritance and departures) | Item is complete; only the residual suggestions below remain |
| "Reflection makes retained lessons second-order" rederives Argyris's single/double-loop idea | The [second-order note](../../notes/reflection-makes-retained-lessons-second-order.md) contains no loop-level learning theory; it is the operation taxonomy (reject/revise/rescope) plus the represented-scope precondition — exactly what the proposal says to *keep* | There is nothing to delegate to Argyris from that note; the merge question is editorial, not delegational |
| Proposal-selection note should delegate "engineering decomposition to MAPE-K" | The [loop note](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) contains no engineering decomposition; it already cites Weyns for MAPE-K's status (reference model for engineering, not definition) and offers its own decomposition in the same spirit | Little to trim; the MAPE-K delegation applies to future runtime-pathway *guidance*, not to this note |
| "Keep autonomy-relocation as a short hypothesis grounded in Bainbridge, not foundational doctrine" | Already its state: the [note](../../notes/increasing-computational-autonomy-relocates-human-effort.md) cites Bainbridge 1983 and its Scope section marks the cross-system claim as conjecture | No change to the note; only the source hygiene item below |
| MAPE-K's Knowledge component doesn't guarantee addressability; Execute doesn't establish operative retention | Correct, and consistent with how the cluster already treats loop models | Confirms the local kernel list |

The proposal's "what should remain local" list (frame-indexed membership, operative change, direct-vs-proposal-selection, semantic reflection across forms, retrieval-as-causal-wire, addressability with represented scope, closure separation, cross-representational cumulativity) matches the LLM-shaped delta the evaluation isolated. No disagreement there.

## 3. The genuinely new decisions

### 3a. Goal revision (maintainer's call; recommended)

Extending the conservative-extension stance to the methodology layer is cheap, consistent, and YAGNI-shaped: where PDSA already supplies trial/observation/adoption procedure, local guidance should say only what PDSA cannot — whether the change targets the system's own behavior-determining organization, and whether adoption became operative through a consumer, channel, and force. Draft wording, adapting the proposal's:

> Use the cluster as an ontology and a Commonplace-specific overlay on established improvement methodologies; do not construct a standalone improvement methodology. Local guidance states only what the established host cannot: the operativity test, the reflective/addressability profile, and the warrant boundary.

### 3b. PDSA and MAPE-K as hosts (adopt the stance now; bind the host at the digest phase)

The proposal argues the host decision must precede the phase-1 audit "because it determines which guidance Commonplace does — and does not — need to create." That conflates two phases. The audit reads *existing* artifacts through the theory's questions (consumer/channel/force, loop function, oracle domain, retention scope) — none of those questions depend on a host methodology. What depends on the host is the *digest*: which change-process guidance gets written at all. And there the workshop's own two-layer principle cuts against upfront adoption: digest content is promoted from observed fallback traffic, and the repo's profile-promotion discipline (text contracts) is worked-case-first. Committing to "PDSA hosts human-inclusive changes" before a single change has been run through a PDSA overlay is the same upfront-design move the framework forbids for digest content.

Recommended sequencing:

1. **Now (with the goal revision):** adopt the negative commitment — the audit dispositions and the digest must not create local guidance duplicating what PDSA/MAPE-K supply; where a disposition wants change-testing procedure, it cites the host instead.
2. **Now (mechanical, unblocked):** snapshot + ingest the candidate host sources (§5), so audit dispositions can cite them.
3. **Digest phase:** run one real repository change through a PDSA overlay as the worked case; bind the host and write the adapter only if the worked case holds. Same for MAPE-K if and when a computational runtime pathway actually exists to engineer — currently none does, so binding MAPE-K now would be pure anticipation.

### 3c. Assurance cases / GSN for warrant recording (new; ledger candidate)

The one delegation target the evaluation did not consider. The fit is real: [warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) says which acceptances an oracle warrants; an assurance case is the established form for *recording* that a specific acceptance decision rests on specific evidence under a specific claim scope. The local remainder is exactly what the proposal says: define the oracle domain and name which acceptance decision the evidence warrants. Disposition: add to the ledger as an open inheritance candidate; act on it only when the review system's baselines need a warrant-recording form (they may already be the lightweight instance — a freshness baseline is an evidence-pinned acceptance record).

## 4. Disposition of the five cleanup items

1. **Merge "second-order" into "addressability."** Not on delegation grounds — see the fact-check; the note carries no Argyris content to shed. As pure editing, the two notes split deliberately: addressability carries the compounding-vs-reading contrast against parametric retention; second-order carries the operation taxonomy and the represented-scope dependency. A merge yields one long note and breaks six inbound links for no delegation gain. **Recommend: no merge.** The evaluation's "optional convergence" provenance line for Argyris (finding 7's neighbor, §4) remains the right-sized engagement, and belongs in the second-order or closure note only if the human-inclusive cases get developed.
2. **"Let Parasuraman own per-function allocation; remove the local rederivation; fold the measurement note into the profile."** The inheritance is done, but the residual asks contradict the maintainer's recorded decision: inherit the *form*, not base the theory on it. The "profile, not ladder" argument cannot be removed — its ground is the local commensurability argument, and the functions differ (improvement functions, not task-performance stages; a flagged departure). The [measurement note](../../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) is cited from two notes as a standalone open problem; folding it is a link-churn editorial call with no delegation payoff. **Recommend: no further action; item closed by the executed inheritance.**
3. **Trim the proposal-selection note.** Nothing to trim — see the fact-check. The note's length is boundary-case analysis (Homeostat, Zinkevich, Gödel machine), which is the distinctive kernel the proposal itself says to keep. **Recommend: no change; delegate change-testing procedure to PDSA in the future digest, not here.**
4. **Fold the stub note into coverage/addressability.** Already a ledger item with exactly this option on the table; the proposal is a second vote for folding. **Recommend: fold**, unless the phase-1 audit turns up a live need for the self-ontology investigation — the audit is the cheap way to find out, so resolve this ledger item after phase 1 starts, not before.
5. **Keep autonomy-relocation as a Bainbridge-grounded hypothesis.** Already true. The only real gap is source hygiene: Bainbridge 1983 is a bare DOI link, not a `kb/sources/` snapshot — the one place the cluster cites an external theory without the adapter discipline. **Recommend: snapshot + ingest Bainbridge** (needs open egress, like the Parasuraman step did).

## 5. Work items (if the maintainer adopts §3a–b)

- Revise this README's Goal per §3a (maintainer sign-off; one paragraph).
- Snapshot + ingest, from a machine with open egress: Bainbridge 1983 ("Ironies of Automation"); Kephart & Chess 2003 ("The Vision of Autonomic Computing") for MAPE-K's origin (currently reached only through the Weyns tour); a PDSA/Model-for-Improvement source (Moen & Norman's PDSA history paper is the open-access candidate; Langley et al.'s *Improvement Guide* is the canonical but paywalled form); optionally Argyris 1977 (HBR double-loop) and the GSN Community Standard.
- Ledger addition: assurance-case/GSN inheritance for warrant recording (§3c), including the question whether freshness baselines already instantiate it.
- Digest phase: one repository change run as a PDSA worked case before any host binding (§3b step 3).

What this buys, honestly stated: delegation does not delete maintenance — it converts derivation maintenance into fidelity maintenance (the adapter must track its source and its departures). The repo already pays that cost well (Provenance discipline, finding 6), which is the strongest argument that more delegation is cheap here.

---

Links:

- [Workshop README](./README.md) — depends-on: the goal and sequencing this assessment proposes to revise
- [External-theory evaluation](./external-theory-evaluation.md) — extends: the conservative-extension stance and findings this assessment carries to the methodology layer
- [Self-improving systems tag README](../../notes/self-improving-systems-README.md) — tests: the cluster whose delegation surface is assessed
- [A self-improving system needs a profile, not a ladder](../../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md) — evidence: the executed Parasuraman form-inheritance the proposal treats as pending
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — tests: the note cleanup item 3 targets; already delegates loop-model status via Weyns
- [Reflection makes retained lessons second-order](../../notes/reflection-makes-retained-lessons-second-order.md) — tests: the note cleanup item 1 targets; carries no Argyris content to delegate
- [Increasing computational autonomy relocates human effort](../../notes/increasing-computational-autonomy-relocates-human-effort.md) — tests: already the short Bainbridge-grounded hypothesis item 5 asks for
- [Warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — extends: the local theory an assurance-case inheritance would give a recording form
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — grounds: the recurrence-driven promotion principle that argues against binding a host methodology before a worked case
- [Model for Types and Levels of Human Interaction with Automation](../../sources/model-types-levels-human-interaction-automation.md) — evidence: the ingested Parasuraman source
