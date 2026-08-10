# Semantic audit of `candidate-v1.md`

Scope: this report applies each gate under `kb/instructions/review-gates/semantic/` directly to the snapshot now preserved as `candidate-v1.md`. Candidate-relative links were resolved as though the candidate lived in `kb/notes/`. Grounding review followed only direct candidate links: the three-source bundle for the operations claim and one direct link for each other distinct claim or footer relation. No review-store state was registered.

`PASS` below means only that this gate found no reportable defect. It is not global certification.

## `semantic/completeness-boundary-cases`

- **Applicability:** Applicable. The candidate presents a three-operation framework (`candidate.md:10-14`), an enumeration of dispositions (`candidate.md:12-14`), and a four-way outcome framework (`candidate.md:20`).
- **Status:** **WARN**
- **Anchored rationale:**
  - The operation framework handles its stated core cases: a simple exposed claim can be challenged and answered; a true conclusion with an invalid route can be challenged at the route (`candidate.md:16`); a support gap can be investigated or retained as unresolved (`candidate.md:14`); and settled rendering is explicitly outside scope (`candidate.md:10`). Early ideation without a definite claim is also explicitly adjacent rather than silently claimed (`candidate.md:12`). Because the candidate calls the three operations neither canonical nor complete (`candidate.md:12`), those boundary exclusions do not fail this gate.
  - The disposition list also covers its clear boundaries: a false positive can be rebutted with support, a curable fault can lead to revision or narrowing, a defeated position can be switched or rejected, and unavailable evidence can lead to investigation or an unresolved marker (`candidate.md:12-14`).
  - The outcome framework does not cover one boundary that the candidate itself declares relevant. `candidate.md:12` names **idea generation** as an adjacent effect or outcome. But `candidate.md:20` defines artifact outcomes only through upheld findings producing corrections, better-supported boundaries, or rejection; human-understanding outcomes through human restatement or update; later-system outcomes through retrieval and changed use; and acceptance through admission authority. A newly generated hypothesis or explanation need not be a correction, a human update, later use, or acceptance, so it maps to none of the four. The wording “the other three” presents those categories as a closed local set. This is a clear coverage failure at the framework's own stated boundary, regardless of whether the eventual authorial decision is to make that set exhaustive or explicitly narrower.

## `semantic/conceptual-role-conflation`

- **Applicability:** Applicable. The candidate imports practitioner accounts, introduces its own synthesis, defines operations and outcomes, and applies them to a human-agent design.
- **Status:** **PASS**
- **Anchored rationale:** `candidate.md:12` explicitly separates the practitioner accounts from the candidate's current synthesis and denies that the synthesis is canonical or validated. `candidate.md:14` separates checker and acceptor roles from the human, agent, or policy actors that may fill them. `candidate.md:18-20` separates admission authority, checking performance, artifact change, human understanding, and later-system use. These passages do not permit two materially different assignments of term, source account, current contribution, and object of application. The unused human-agent scope is routed to the qualifier gate rather than treated as role conflation.

## `semantic/explanatory-reach`

- **Applicability:** Applicable because the candidate declares `title-as-claim` (`candidate.md:4`).
- **Status:** **PASS**
- **Anchored rationale:** The mechanism for the defensible central claim is explicit: define the object each role receives, record the exact input, checker report, and disposition, and thereby preserve evidence of the attempted work and handoffs for inspection (`candidate.md:10,14`). Varying the recording premise changes the conclusion: without a recoverable input, report, or disposition, an auditor cannot trace which commitment was checked or what happened to a finding. A missing, mismatched, or unrecoverable trace would falsify the auditability claim. The candidate does not protect an effectiveness claim with ad hoc qualifications; it repeatedly distinguishes inspectability of an attempt from fault detection, justified disposition, independence, or improved outcomes (`candidate.md:10,14,16,20`).

## `semantic/explication-quality`

- **Applicability:** Not applicable. The gate requires `type: kb/types/definition.md`; the candidate declares `type: kb/types/note.md` and no `definition` trait (`candidate.md:3-4`).
- **Status:** **INFO**
- **Anchored rationale:** No Carnap-style explication verdict is warranted for this artifact type. The locally introduced operation and outcome labels remain reviewable under the other semantic gates.

## `semantic/grounding-alignment`

- **Applicability:** Applicable because the candidate declares `has-external-sources` and uses linked sources and notes in load-bearing passages (`candidate.md:4,12,16,18,32-35`).
- **Status:** **INFO**
- **Anchored rationale:**
  - The three practitioner sources support the modest route actually claimed at `candidate.md:12`: `putting-ideas-into-words.md:20` describes committing ideas to exact words and rereading as a neutral stranger; `how-to-think-in-writing.md:54,72-76` describes definite claims, explicit explanatory premises, and criticism/counterexamples; and `learning-by-writing.md:73,101` describes finding weaknesses, further inquiry, revision, and switching. The candidate correctly calls its three bundles a noncanonical synthesis motivated by reported practice, not a controlled validation.
  - `reasoning-production-is-not-reasoning-evaluation.md:12` directly supports testing critics on true conclusions reached through invalid routes (`candidate.md:16`). `error-correction-works-above-chance-oracles-with-decorrelated-checks.md:22,48` supports the distinct discrimination and error-correlation conditions. The candidate correctly refuses to treat a fresh runner or different prompt as proof of independence.
  - `llm-generation-relaxes-goals-where-human-writing-stalls.md:28` presents the relaxation mechanism as a hypothesis, matching the candidate's explicit conjectural qualifier (`candidate.md:18`). `when-is-it-better-to-think-without-words.md:85` directly supports the narrower warning that human writing can stabilize false precision.
  - `why-almost-never-use-ai-to-write-anything-substantive.md:84` supports passive assent once prose is already present, but it does not establish **anchoring** as a measured effect or show that pre-commitment ordering reduces it. The candidate marks the claim with “may” and leaves the ordering test open at `candidate.md:25`, so this is a plausible but non-airtight inference rather than scope overreach.
  - The footer relations align with their targets: actor allocation is not fixed by a human analogy; readable artifacts enable inspection without guaranteeing correctness; discrimination and decorrelation are separate requirements; and persistence, activation, and verification are distinct (`candidate.md:32-35`).

## `semantic/internal-consistency`

- **Applicability:** Applicable to the whole body.
- **Status:** **PASS**
- **Anchored rationale:** The opening claim that traces establish auditability but not effectiveness (`candidate.md:10`) is maintained by the concrete loop (`candidate.md:14`), the demand for separate performance evidence (`candidate.md:16`), the rejection of authorship and approval as proxies (`candidate.md:18`), and the outcome-specific conclusion (`candidate.md:20`). The global definition of “human-agent” as requiring at least one human role (`candidate.md:10`) is logically compatible with saying that either checker or acceptor may individually be filled by a human, agent, or policy (`candidate.md:14`); the scope may be unnecessary, but the passages do not contradict each other. No definition drift or summary/body reversal remains.

## `semantic/load-bearing-qualifiers`

- **Applicability:** Applicable because the candidate declares `title-as-claim`; the gate watches the title, description, opening, and main proof.
- **Status:** **WARN**
- **Anchored rationale:**
  - The opening restricts the construction to “substantive **KB** claims” (`candidate.md:10`), but no step in the auditability mechanism uses a KB-specific property. Deleting “KB” leaves the defined-input and preserved-trace argument unchanged, and the cited cases are prose arguments rather than KB-specific machinery. This is usage-fit narrowing of the central construction.
  - The description and opening also restrict the construction to a **human-agent** workflow, defined as retaining at least one human checking or acceptance role (`candidate.md:2,10`). Yet the central auditability route depends on recorded role artifacts, and `candidate.md:14` says the checker and acceptor may be human, agent, or policy while `candidate.md:18` says tested checking and adjudication matter rather than who produced or approved the prose. Human participation is needed for the separately named human-understanding outcome, but `candidate.md:20` explicitly separates that optional outcome from auditability. The at-least-one-human condition therefore narrows the central claim without entering its reasoning.
  - By contrast, “recorded,” “attempted,” and “whose commitment or support is still unsettled” are load-bearing: removing them would erase the trace mechanism, reintroduce an unsupported effectiveness claim, or include the settled-rendering boundary that `candidate.md:10` explicitly excludes.

## `semantic/underspecified-assertions`

- **Applicability:** Applicable. The loop's handoff requirement is load-bearing.
- **Status:** **WARN**
- **Anchored rationale:** The requirement to map “every **material reported finding**” to a disposition (`candidate.md:14`) leaves the materiality rule unresolved. One reasonable reading is prospective: a finding is material when, if true, it could change a load-bearing claim or route, so the acceptor must disposition serious reported objections before their truth is known. Another is adjudicative: a finding is material only after independent review establishes a real fault, so false positives need not enter the disposition-completeness test. The choice changes the population of required dispositions, the order of adjudication, and what evidence would show that a handoff is complete. `candidate.md:16` separately requires dispositions for independently upheld findings but does not say whether those are the only material findings, so nearby context does not settle the choice.

## `semantic/unearned-generality`

- **Applicability:** Applicable because the candidate declares `title-as-claim` and the gate watches the title-level central claim.
- **Status:** **WARN**
- **Anchored rationale:** The title says the checks make “attempted **epistemic work**” auditable (`candidate.md:8`), while the mechanism records only the claim, premises, route, critic report, and disposition in one prose-argument loop (`candidate.md:10-16`). Downgrading the object to the attempted operations or prose-argument checking leaves every mechanism, example, citation, and conclusion unchanged. The broader wording additionally covers epistemic work such as idea generation and early evidence search, but the candidate itself calls idea generation adjacent (`candidate.md:12`) and records no trace for it. The abstraction therefore extends the title's auditability promise beyond the work the argument makes inspectable; the body does not establish a second instance or a form-independent reason that all of that wider work is captured.

## Material blockers and routed findings

Material blockers:

- The outcome framework omits the adjacent idea-generation outcome it names (`semantic/completeness-boundary-cases`).
- “KB” and the at-least-one-human condition narrow the central auditability construction without entering its mechanism (`semantic/load-bearing-qualifiers`).
- “Material reported finding” leaves the required disposition population and adjudication order unresolved (`semantic/underspecified-assertions`).
- “Epistemic work” widens the title beyond the recorded prose-argument operations (`semantic/unearned-generality`).

Non-blocking routed findings:

- The source supports passive assent but not an established anchoring effect; the candidate's modal wording and open question keep this at INFO (`semantic/grounding-alignment`).
- `semantic/explication-quality` is inapplicable to this note type and is recorded as INFO only.
- The conceptual-role, explanatory-reach, and internal-consistency gates pass on their own criteria; those passes do not resolve the blockers above and do not certify the candidate globally.
