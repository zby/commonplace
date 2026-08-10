# Audit: recorded composition checks

## 1. Claim delta

Status: resolved

**Anchor:** `draft.md:2,7,9`; `claim-skeleton.md:7-12,107-110`; `original.md:2,8,12-14,18,22`.

**Finding:** The title, description, and governing paragraph replace the incumbent's positive reconstruction claim and mandatory-human-judge condition with the skeleton's narrower result: a workflow can expose attempted work without establishing preserved effects or an advantage over solo writing. This is a material reversal, but it is the reversal expressly required by the claim revision (`claim-revision-log.md:22-37,110-112`), not an accidental loss. The title remains a truth-apt, composable claim, and the description distinguishes this note from the stronger incumbent.

**Recommended action:** keep

**Resolution:** Kept in `candidate.md`; the candidate retains the source-directed reversal and does not restore the incumbent's stronger reconstruction or superiority claims.

Status: resolved

**Anchor:** `draft.md:9-25`; `claim-skeleton.md:28-92,129-133`.

**Finding:** All six planned body commitments appear in order: the evidential ceiling, the three-operation synthesis, an auditable candidate loop, stage-performance tests, authorship/approval failure modes, and distinct artifact/human/system outcomes. The optional questions also preserve all three planned tests. No planned body commitment is omitted. The only material deviations are the metadata, lineage, and success-coded wording addressed separately below.

**Recommended action:** keep

**Resolution:** Kept in `candidate.md`; all planned body commitments and the three open questions remain present in the same argumentative order.

Status: resolved

**Anchor:** `draft.md:4,9-19`; `kb/types/note.md:36-43`; `kb/notes/COLLECTION.md:44-46`.

**Finding:** The draft adds `synthesis` and `has-external-sources`, neither present in the incumbent or specified by the skeleton. Both are warranted. The note composes several practitioner claims and local theories into one three-operation argument, and its source snapshots represent material originating outside the project. The body also restates the synthesis and its boundaries inline, as the `synthesis` expectation requires.

**Recommended action:** keep

**Resolution:** Kept both traits in `candidate.md`; the body remains an inline synthesis of external practitioner sources and local theory.

Status: resolved

**Anchor:** `original.md:5`; `draft.md:1-5`; `kb/types/note.md:18-20`; `brief.md:77-80`.

**Finding:** The draft silently removes `tags: [foundations]`. Neither the reconstruction, skeleton, revision log, nor type contract decides whether the substantially narrowed replacement still belongs in that navigation category. The retained commission preserves the incumbent's collection placement and subject, but does not authorize either preserving or deleting its tag. This is an intent-dependent navigation decision rather than an evidential consequence of the rewrite.

**Recommended action:** ask user

**Resolution:** Restored the incumbent `tags: [foundations]` in `candidate.md`. The experiment therefore makes no unauthorized navigation change; any later tag removal remains a separate human decision.

Status: resolved

**Anchor:** `original.md:10-22,28-34`; `draft.md:9-25,31-34`; `claim-revision-log.md:22-37,94-112`.

**Finding:** The remaining incumbent changes are justified by the revised claim. The draft drops the Borretti polemic, the categorical writing-is-thinking premise, the claim that a human is the load-bearing or strongest checker, the workshop-layer implementation detail, the human competence-floor digression, the connection-work payoff, and the bet that the loop thinks better than a solo writer. It retains the useful residue—commitment, criticism, response, anchoring, verification, and outcome separation—while replacing direct Borretti lineage with the more specific practitioner sources. The footer retains the LLM-relaxation, error-correction, inspectability, and persistence dependencies; it adds the allocation and route-evaluation dependencies. The omitted automation-boundary and Borretti links no longer support a unique body commitment that the retained links leave ungrounded.

**Recommended action:** keep

**Resolution:** Kept the source-directed removals in `candidate.md`; none of the dropped incumbent branches or claims was reintroduced.

Status: resolved

**Anchor:** `draft.md:11,15,17,31-39`; intended destination `kb/notes/` from `brief.md:28`.

**Finding:** Every Markdown target is correct relative to the intended `kb/notes/` destination: `./...` resolves to sibling notes, `../sources/...` to source snapshots, and `../instructions/...` to procedures. They do not resolve from the workshop location, but the brief defines the draft as destination-relative, so that is not a defect.

**Recommended action:** keep

**Resolution:** Kept destination-relative links and verified them separately against the intended `kb/notes/` parent.

Status: resolved

**Anchor:** `draft.md:36-39`; `kb/notes/COLLECTION.md:50-54,68-72`; `reconstruction.md:107-110`; `claim-revision-log.md:7-20`; `kb/instructions/composition-friction-gate.md:8-10,56-57`; `kb/instructions/critique-note.md:46-48`.

**Finding:** The new `Operationalized into:` footer does not assert honest lineage in its current form. The reconstruction and revision treat both procedures as upstream witnesses that a check can be specified and recorded, not as downstream procedures derived from the revised methodology. More importantly, the friction instruction still says it “reconstructs” the filter and that runner separation “gives the check teeth,” while the draft expressly withholds reconstruction and independence claims. The critique instruction's reverse link likewise describes freshness as a decorrelation condition on which the old defense depends. A clean `operationalized-from` edge would conceal these direction and claim-strength mismatches.

**Recommended action:** remove

**Resolution:** Removed the entire `Operationalized into:` footer from `candidate.md`. The procedures remain evidence inputs, not asserted downstream lineage.

## 2. Grounding

Status: resolved

**Anchor:** `draft.md:9-19`; `reconstruction.md:103-123`; `brief.md:32-38`.

**Finding:** Apart from the completion language in the next finding, the evidence posture is sound. The three-operation taxonomy is explicitly identified as synthesis; the linked human essays are described as reported practice rather than controlled evidence; LLM relaxation is called conjectural; anchoring and human false precision are attributed to practitioner accounts; route evaluation is presented with the absence of prose calibration; and the no-comparison conclusion stays within the supplied evidence. The scope and outcome distinctions are user-directed definitions and evaluation rules, not presented as observed results.

**Recommended action:** keep

**Resolution:** Kept the calibrated evidence posture in `candidate.md`, including explicit practitioner, conjectural, and no-comparison boundaries.

Status: resolved

**Anchor:** `draft.md:11,13,15,19`; `claim-revision-log.md:9-13,66-70`; `claim-skeleton.md:20-21`.

**Finding:** Several phrases cross from an auditable attempt into unsupported completion. `Challenge-and-locate` “identifies the load-bearing issue,” `Respond-and-decide` records a “supported rebuttal,” the acceptor handles “every load-bearing finding,” and performance culminates in “accurate findings” and “apt dispositions” or “appropriate rejection.” The revision log explicitly says that a trace can record a proposed localization but cannot establish that the localization is epistemically apt. As written, correctness is both the thing to be validated and an unexplained premise of the validation rule.

**Recommended action:** clarify

**Resolution:** Replaced success-coded wording in `candidate.md`: the challenger now *proposes* a possible issue, the responder records a disposition rather than a `supported rebuttal`, the acceptor records a disposition for every reported challenge to a load-bearing commitment (including finding the challenge unsupported), and outcome claims require independently upheld findings and adjudicated dispositions.

Status: resolved

**Anchor:** `draft.md:13`; `claim-skeleton.md:48-58`; `reconstruction.md:63-78`.

**Finding:** Calling the construction “a minimum auditable loop” is an unsupported completion. The sources and procedures witness one implementable allocation, but do not establish that every listed element is necessary, that none can be combined, or that no smaller trace suffices for a stated outcome. The skeleton planned this wording, so this is not a drafting deviation; it is a skeleton-level claim that did not earn evidential support.

**Recommended action:** clarify

**Resolution:** Changed `a minimum auditable loop` to `one auditable candidate loop` in `candidate.md`; no necessity or minimality claim remains.

## 3. Specificity

Status: resolved

**Anchor:** `draft.md:13,15`; `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md:17-24,46-56`; `kb/notes/reasoning-production-is-not-reasoning-evaluation.md:10-28`.

**Finding:** The performance rule is not yet measurable for the report-shaped critic the draft defines. TPR and FPR in the grounding note apply to an accept/reject oracle, while this critic emits objections, counterexamples, and uncertainty. The draft does not specify the scored unit, what counts as a positive, how support labels become ground truth, which error class is targeted, or how correlation is calculated across variable reports. Without those choices, “TPR must exceed FPR” is a valid borrowed condition but not yet a test an evaluator can execute.

**Recommended action:** clarify

**Resolution:** Operationalized the borrowed discrimination condition in `candidate.md` for each defined error class: reports become scored detections against independently adjudicated passages, with explicit true-positive and false-positive cases and separately measured error correlation.

Status: resolved

**Anchor:** `draft.md:9,13,19`; `brief.md:5,15,22,34`; `claim-skeleton.md:23`.

**Finding:** “Human-agent workflow” has no stable actor boundary in the draft. It says checker and acceptor may each be a human, agent, or policy, but does not identify the human contribution that makes the allocation human-agent rather than agent-policy. This matters because human re-derivation is required only for the human-understanding outcome, while the governing label appears to cover every outcome. The allocation can remain open, but the scope needs to state whether some human participation is constitutive or merely one candidate allocation.

**Recommended action:** clarify

**Resolution:** The first candidate defined `human-agent`, but direct semantic review showed that human participation did no work in the central auditability mechanism. The current `candidate.md` therefore removes that qualifier, calls the construction a distributed writing workflow, and treats human participation only where it is load-bearing for a human-understanding outcome or a chosen role allocation.

## 4. Relevance and audience

Status: resolved

**Anchor:** `brief.md:7-24`; `draft.md:9-25`.

**Finding:** The body stays on the intended decision for Commonplace maintainers. Each paragraph adds a distinct decision-relevant layer, and the draft avoids the incumbent's displaced polemic, corpus-scale connection benefit, architecture detail, and general human-capital claims. No undefined external dependency or irrelevant source detail is imported into the prose.

**Recommended action:** keep

**Resolution:** Kept the six-paragraph decision-focused body and did not add any displaced source detail.

## 5. Compression and prose

Status: resolved

**Anchor:** `draft.md:9-25`; `kb/notes/COLLECTION.md:23-25`.

**Finding:** No material prose edit should precede the content fixes above. The repeated evidential ceilings occur at different inferential joints—design, checker result, calibration, and final outcome—and keep the note from turning one caveat into a generic hedge. The prose is compact for the number of distinctions the brief requires; further compression now risks collapsing those distinctions.

**Recommended action:** keep

**Resolution:** Kept the evidential ceilings at their distinct inferential joints. Reconciliation removed the unsupported lineage footer but did not compress away the role and outcome distinctions required by the brief.
