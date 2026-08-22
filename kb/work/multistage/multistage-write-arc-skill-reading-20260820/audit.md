# Audit: ARC skill as a route-asymmetric epistemic architecture

## Scope and result

Fresh audit of `brief.md`, every evidence path it lists, `reconstruction.md`, `claim-disposition.md`, `claim-skeleton.md`, and `draft.md`. The ARC checkout was clean at commit `dba53c3799eab600a512dd73ed037d7ab6958c66` (`docs: rewrite readme from site content`, 2026-08-19), and the relevant parser, live-action, replay/search, inspection, event, and CLI routes were checked directly.

Initial result: **not ready for candidate reconciliation without changes**. The audit opened eight material and four minor findings. None required new evidence or a user decision.

Severity meanings in this audit:

- **blocker** — cannot be resolved from the authorized inputs without new evidence or a user decision;
- **material** — changes a factual, evidential, route, force, or comparison claim that the analysis relies on;
- **minor** — a bounded accuracy, vocabulary, or compression problem that does not change the central contribution.

## Findings

### ARC-AUD-001 — ARC evidence links will be absent from the published workshop

Status: RESOLVED

Severity: material

Location: `draft.md:9` and every `../../../related-systems/arc-skill/...` link in `draft.md:15-24`, `32`, `40`, `42`, `48`, `62-66`, `77-80`, `105`, `107`, `111`, and `115`; the same link plan originates at `claim-skeleton.md:13-24`.

Recommendation: ground

Evidence/reason: `.gitignore:39` excludes the entire `/related-systems/` directory. The workshop contract says `kb/work/` is published, so these relative links resolve only in the operator's current checkout and will be dead in the repository and rendered workshop. The prose also never names the inspected commit, leaving code-grounded claims vulnerable to checkout drift. The actual clean source boundary is commit `dba53c3799eab600a512dd73ed037d7ab6958c66` of `https://github.com/pbshgthm/arc-skill.git`.

Required action: replace the ignored-checkout links with immutable source references, preferably GitHub blob links pinned to the inspected commit or an authorized durable source snapshot, and state the commit scope near the evidence-order paragraph. Keep campaign figures attributed to the README at that same revision.

### ARC-AUD-002 — Oracle strength is conflated with the property being checked

Status: RESOLVED

Severity: material

Location: `draft.md:15`, “the implemented check sits lower on the oracle-strength spectrum.”

Recommendation: clarify

Evidence/reason: `predictions.py:59-109` implements a deterministic parser and admission rule. It is a hard check for the narrow target “nonempty prediction accepted by this parser.” It is not an adequate check for the README's broader target “a falsifiable claim,” and it does not assess causal discrimination or explanation quality. `kb/notes/oracle-strength-spectrum.md:10-18` defines strength by how cheaply and reliably correctness can be checked relative to the objective. Ordering the parser below the README language without fixing a common target collapses the draft's own target/oracle distinction: the implementation changes the checked property as well as the check.

Required action: distinguish a deterministic oracle over narrow syntactic/observable admission from inadequate discrimination of the broader falsifiability or explanation-quality target. Do not give one unqualified strength ordering across different targets.

### ARC-AUD-003 — Free text induces `change` only when no structured claim exists

Status: RESOLVED

Severity: minor

Location: `draft.md:32`, “Unrecognized prose becomes an ungraded note and induces a generic `change` claim.”

Recommendation: clarify

Evidence/reason: `predictions.py:101-109` stores every unrecognized clause as a `note`, but appends the implied generic `change` claim only when the whole prediction contains no gradable structured claim. In a mixed prediction such as prose plus `cell ...`, the prose stays ungraded and the structured claim is graded; no extra `change` claim is added. `reconstruction.md:73` retained this qualifier, but it was lost downstream.

Required action: restore the condition “when the prediction contains no structured gradable claim.” Preserve the separate point that prose clauses are ungraded even in mixed predictions.

### ARC-AUD-004 — Replay does not use `render`/`observe` for every transition

Status: RESOLVED

Severity: material

Location: `draft.md:20`, `42`, `79`, and the replay row at `95`; upstream overcompression appears in `claim-skeleton.md:96`, `140`, `217`, and `235`.

Recommendation: clarify

Evidence/reason: `rules.py:212-309` uses heterogeneous transition checks. For ordinary nonterminal transitions, it compares exact `render` output when present or equality under `observe` after re-grounding. For a level advance, `rules.py:214-237` checks whether the predicted state satisfies the model's own `goal`; it does not compare that predicted terminal state through `render` or `observe`. For `GAME_OVER`, `rules.py:238-253` checks the optional `dead` predicate. Resets and boundary openings are re-grounded. A `HISTORY_FIT` result therefore means no mismatch or declared gap under the checks applicable to each route, not uniform board or observation-projection agreement over every recorded transition.

Required action: make the replay description enumerate the ordinary-transition, level-completion, game-over, and re-grounding checks. Scope exact `render`/`observe` comparison to the transitions where the implementation actually performs it, and carry that scope through the Commonplace and taxonomy comparisons.

### ARC-AUD-005 — `MISMATCH` is not the only condition that can prevent solve

Status: RESOLVED

Severity: material

Location: `draft.md:42`, “Only `MISMATCH` blocks solve.”

Recommendation: clarify

Evidence/reason: `rules.py:367-373` always refuses search when replay status is `MISMATCH`, but `rules.py:374-379` also refuses search when replay leaves no usable current model state. This commonly accompanies an `INCOMPLETE` replay whose current board cannot be grounded. The ledger at `draft.md:21` states the narrower rule more accurately: `INCOMPLETE` is not itself disqualifying if the current state is available.

Required action: say that `MISMATCH` categorically blocks search, while `INCOMPLETE` may proceed only when replay leaves a usable current model state. Remove the exclusive “only” formulation.

### ARC-AUD-006 — Commonplace freshness can survive an acknowledged input change

Status: RESOLVED

Severity: material

Location: `draft.md:48`, especially “In both cases, ‘fresh’ means applicable to unchanged inputs”; related summary at `draft.md:80`.

Recommendation: clarify

Evidence/reason: `kb/reference/README-REVIEW-SYSTEM.md:27`, `51`, and `102-112` says a Commonplace acknowledgement may advance a freshness baseline to the current note snapshot after a non-invalidating note change while preserving the older evidence review pair. Commonplace freshness means that retained evidence is recorded as applicable to the current note/criterion inputs. It does not always mean the files are unchanged since the evidence was produced. ARC plan freshness is stricter: changed event identity, observation hash, or rules hash refuses the plan and has no acknowledgement transition.

Required action: keep the comparison at the shared applicability function, but state the transition difference exactly. Use “unchanged provenance” only for ARC; describe Commonplace as current snapshot applicability that can be established either by review finalization or explicit acknowledgement of a non-invalidating note change.

### ARC-AUD-007 — Recorded grading is listed as operative without its route condition

Status: RESOLVED

Severity: material

Location: `draft.md:26`, “Operativity moves among admission, recorded grading, model-search eligibility, plan applicability, queue survival, and environment completion.” Check the compressed recurrences at `draft.md:67` and `121` during resolution.

Recommendation: clarify

Evidence/reason: the draft defines an operative oracle at `draft.md:5` as one whose result changes admission, survival, rollback, use, or continued execution, and says recording a grade is insufficient. In `live.py:115-174`, a standalone grade is recorded and reported but creates no persistent action block. In `live.py:194-265`, the same kind of post-action grade becomes operative over the active batch because a miss discards the suffix. Treating “recorded grading” itself as a locus of operativity erases the route and horizon that make it operative.

Required action: state that grading supplies evidence on every graded action, but acquires code-enforced continuation force only on queued routes. Keep standalone reporting, agent-mediated response, and deterministic queue survival distinct.

### ARC-AUD-008 — Prose-note participation is stated as realized behavior despite the evidence boundary

Status: RESOLVED

Severity: material

Location: `draft.md:52`, `62`, `67`, and `92`, including “Prose notes ... guide predictions and plans,” “action-guiding notes,” and “Direct action-guiding synthesis.”

Recommendation: clarify

Evidence/reason: `skills/arc-skill/SKILL.md:50-53` assigns notes a recovery and planning role, and `inspect.py:520-532` prints them in status output. The selected code does not establish that an agent read them, changed a prediction because of them, or followed their declared `Verified`/`Assumed` status in the campaign. The brief explicitly excludes inferring campaign compliance, and `kb/notes/definitions/behavioral-authority.md:23-25` says declared intent alone does not establish effective authority. Executable rules and generated plans have a direct implemented consumption path when invoked; prose notes have assigned and available action-guiding authority whose realized effect is not shown by the supplied run evidence.

Required action: qualify prose-note participation as designed, available, or conditional on agent consumption, and reserve realized campaign influence for evidence not supplied here. Keep that distinction visible in the five-case and pressure-test tables because the participation classification depends on it.

### ARC-AUD-009 — The rules contract does not require a causal model

Status: RESOLVED

Severity: minor

Location: `draft.md:95`, “A causal executable model participates.”

Recommendation: clarify

Evidence/reason: `rules.py:37-59` requires grounding, transition, action, goal, and observation functions. It does not require causal variables, interventions, counterfactual structure, rival discrimination, or any other criterion that would establish a causal explanation in Commonplace's stronger sense. No campaign `rules.py` was supplied for inspection. Calling the interface causal adds a commitment absent from both implementation and evidence.

Required action: use a bounded label such as executable action-conditioned transition model. Use “causal” only if a specific model artifact supplies and warrants that structure.

### ARC-AUD-010 — The scorecard row puts the evaluated bundle in the explanation-participation column

Status: RESOLVED

Severity: material

Location: `draft.md:97`, “The configured bundle participates only as a whole,” under `Explanation participation`.

Recommendation: clarify

Evidence/reason: the participation axis in `kb/work/epistemic-architectures/ai-research-os-reading.md:20-27` asks whether explanatory content is inside the production loop. The scorecard is an after-run outcome over the configured system, as the draft itself says at `draft.md:24`; it is not explanatory content and has no in-harness theory-status or future-action route in the inspected files. The configured bundle is the scorecard's evaluated target, not an explanation that participates.

Required action: mark explanation participation for the scorecard route as not applicable or absent at that route, then state separately that the outcome bears on the configured bundle and supplies no component or theory attribution.

### ARC-AUD-011 — `Warranted autonomy` is applied outside its defined pathway

Status: RESOLVED

Severity: minor

Location: `draft.md:22`, “strong path control within the domain of warranted autonomy.”

Recommendation: remove

Evidence/reason: `kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md:10-12` and `32-37` scopes the technical term to unattended evaluation in a proposal-selection improvement pathway. ARC's plan execution is task action, not an accepted behavior-changing proposal retained into an improvement loop. Oracle-domain reasoning is analogous, but the technical term does not automatically cover every autonomously checked action sequence.

Required action: remove the claim that this route is within warranted autonomy. If the oracle-domain analogy is retained, label it explicitly as an analogy and do not imply category membership.

### ARC-AUD-012 — The interpretive sections repeat ledger facts more than they advance them

Status: RESOLVED

Severity: minor

Location: the ledger at `draft.md:13-24` is repeated substantially in `draft.md:30-54`, then again in the Commonplace table at `75-80` and the pressure-test table at `90-97`. Repeated examples include plan freshness (`22`, `46-48`, `80`, `96`) and replay scope (`20`, `42`, `79`, `95`).

Recommendation: remove

Evidence/reason: `claim-skeleton.md:337` says the ledger is the factual spine and later prose should interpret rather than repeat every cell. Several later units restate target, timing, and force before adding only a short comparison conclusion. This makes the public workshop harder to scan and weakens the otherwise simple prose without adding evidential coverage.

Required action: retain the complete ledger once. In later sections, keep only the new inference or comparison and refer back to the named route instead of restating its mechanics, except where one exact fact is needed to make the contrast intelligible.

## Reconciliation

Reconciled result: **ready for candidate and fresh acceptance review**. The main agent resolved every finding in `draft.md`:

| Finding | Resolution |
|---|---|
| ARC-AUD-001 | Replaced ignored-checkout links with GitHub blob links pinned to commit `dba53c3799eab600a512dd73ed037d7ab6958c66` and stated the inspected revision and publication boundary. |
| ARC-AUD-002 | Recast admission as a deterministic oracle over a narrow parser target and rejected any unqualified strength ordering against broader falsifiability or explanation targets. |
| ARC-AUD-003 | Restored the condition that free text induces generic `change` only when no structured gradable claim exists. |
| ARC-AUD-004 | Enumerated ordinary-transition `render`/`observe`, level-completion `goal`, game-over `dead`, and re-grounding routes; bounded `HISTORY_FIT` to the checks applicable to each transition. |
| ARC-AUD-005 | Stated that `MISMATCH` categorically blocks search and that `INCOMPLETE` can proceed only when replay leaves a usable current model state. |
| ARC-AUD-006 | Distinguished ARC's unchanged-provenance refusal from Commonplace finalization and acknowledgement, which can advance current applicability across a non-invalidating note change. |
| ARC-AUD-007 | Separated evidence supplied by every grade from code-enforced continuation force, which arises only when a queued route consumes the grade. |
| ARC-AUD-008 | Qualified prose notes as designed, displayed, and available for action guidance; every comparison now says realized campaign influence is unshown. |
| ARC-AUD-009 | Replaced “causal executable model” with “executable action-conditioned transition model.” |
| ARC-AUD-010 | Marked explanation participation as not applicable to the after-run scorecard route and kept the configured bundle as its evaluated target. |
| ARC-AUD-011 | Removed the technical `warranted autonomy` classification from plan execution instead of extending that proposal-selection term by analogy. |
| ARC-AUD-012 | Compressed the interpretation: admission/grading/queue mechanics, notes/replay, and freshness now refer to the ledger and retain only the inferential contrasts needed later. |

## Clean dimensions / no finding

- **Claim-disposition and skeleton coverage:** clean. The draft realizes the selected central contribution and every retained disposition item. The negative and handoff dispositions remain bounded; no independent second claim cluster is smuggled into the target.
- **Draft commitment delta:** clean apart from the scoped inaccuracies identified above. No `NEW COMMITMENT FOR AUDIT` marker appears, and no unmarked draft-only material commitment was found outside the skeleton.
- **Five prior cases:** clean. ScienceFlow, the ontology draft, Eigenius, Commonplace, and AI Research OS are represented faithfully to the supplied historical workshop files. The draft preserves their unequal evidence grades and the ontology draft's no-running-loop and lab-tooling qualifications.
- **Campaign evidence and causal attribution:** clean. Quantities are clearly attributed to the ARC README; the missing run directories are disclosed; benchmark success and selected action-class miss rates are not presented as component ablations.
- **Epistemic versus operational authority:** clean at the governing-claim level. The draft consistently denies transfer from action fit, replay fit, freshness, or task success to general theory warrant; findings ARC-AUD-004, ARC-AUD-007, ARC-AUD-008, and ARC-AUD-010 concern local route precision, not a collapse of the headline distinction.
- **Artifact shape and workshop contract:** clean. One ARC-specific comparative proposition organizes the document, plain Markdown without frontmatter is correct, the intended durable fold remains a separately authorized handoff, and the target does not present itself as a stable library source.
- **Commonplace terminology not otherwise flagged:** clean. `explanatory-reach`, `discovery lifecycle`, `warrant`, operative oracle, and proposal-selection are used within the supplied definitions. `Freshness baseline` and `warranted autonomy` require only the bounded corrections above.
- **Local path resolution:** clean for all Commonplace and peer-workshop links when resolved from the intended target directory. The only source-path problem is the ignored ARC checkout covered by ARC-AUD-001.

## Blockers

None. Every OPEN finding can be resolved from the already authorized sources and the inspected ARC commit. No user choice, campaign artifact, ablation, or new external source is required for the commissioned code-grounded workshop reading.
