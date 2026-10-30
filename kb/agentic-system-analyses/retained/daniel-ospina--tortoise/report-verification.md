---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of Tortoise's selected capture, correction and context-delivery routes at the frozen partial-loop boundary."
run-id: AAS-2026-10-30-tortoise-0c919b4ca77d-01
reviewed-boundary: "54922a800f96858935b58ef250da569a4896df44"
---

# Tortoise report verification

## Verification

The reports support a bounded implementation account, with the local inventory limit below. I read every supplied member and its governing contract. The four answers files are empty; the structural report-check says `none`. There are no structural failures to route or correction claims to accept on trust. I independently checked SRC-1 HEAD against the boundary revision and found no checkout changes. Source inspection remained read-only; no target execution, provider call or experiment was performed. The [boundary](boundary.md#boundary-and-evidence) correctly describes a complete artifact with a partial loop, not verified whole-system coverage.

### Runtime and workflow

I traced SDK capture's empty-window gate before session writes, provider-less and replay branches, the v2 adapter, source materialization ordering, and the emission return paths in SRC-1, `tortoise/sdk.py`. [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) correctly separates storing a trace from extracting derived memory and makes retry conditional rather than universal. [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission) correctly distinguishes graph feed, JSONL append and subsequent optional record write. The no-journal and failed-append branches do not support all-store atomicity; the report does not claim it.

The inspected hosted recording gate and independent extraction setting in SRC-1, `tortoise/hosted_api.py`, support [RT-RTE-hosted-capture](runtime.md#rt-rte-hosted-capture). Direct local capture and [RT-RTE-direct-point](runtime.md#rt-rte-direct-point) are alternate admission doors, not exceptions silently covered by hosted policy. The positional and coerced property kind checks and content type check support the latter's limited admission finding. The consent check before commit dispatch supports [RT-RTE-production-commit](runtime.md#rt-rte-production-commit); its remote-consumer and recovery uncertainties remain explicit. None of these records establishes per-proposition human endorsement or a global consent guarantee.

I independently followed SRC-1, `tortoise/volunteer.py`, from validation and intent selection through both search arms, why assembly, eligibility, suppression, sorting and block creation. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) preserves the consequential distinctions: why assembly still supplies confidence with `why=False`; the supersession arm can surface flagged predecessors; validation and unbound-search failures differ from guarded retrieval degradation. Framework mutation in SRC-1, `tortoise/framework.py`, supports [RT-BAP-framework-block](runtime.md#rt-bap-framework-block), including ADK's list argument, LangGraph's default user message and Semantic Kernel's post-render prepend. HTTP timeout and opt-in completion-SLO branches in SRC-1, `tortoise/hosted_api.py`, do not establish a universal 300-ms deadline or worker cancellation. The report rejects those overreadings.

[RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model) distinguishes an unpinned remote alias from inspected client behavior. The v2 adapter selects the stated default. [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) is supported by the revision constant and revision-bearing SentenceTransformer load in SRC-1, `tortoise/embeddings.py`. Neither graph vectors nor these load paths demonstrate parameter training or provider-internal fixity.

For [WF-RTE-gap-review](workflow.md#wf-rte-gap-review), I followed S1 chunk continuation, S2 failure/partial handling, VET call sites, S3, the story-triggered S4 call and union rules in SRC-1, `tortoise/extractor_v2.py`. S4 failure preserves S2; usable sections can merge despite other malformed sections; identity collisions favor S4. This establishes code-owned continuation, not semantic verification or transaction rollback. The workflow appropriately requires a later caller sharing state for framework delivery rather than inventing a scheduler between the two invocations.

### Memory and epistemic findings

The writer/adapter distinction supports [MEM-OBJ-session-turns](memory.md#mem-obj-session-turns), [MEM-OBJ-derived-points](memory.md#mem-obj-derived-points) and [EPI-OBJ-extracted-points](epistemic.md#epi-obj-extracted-points): transformed episodic text, admitted graph products and transient payload parts are not interchangeable. Record-capable turn storage does not prove graph-only expansion completeness. The memory report retains that compatibility uncertainty rather than declaring missing turns.

Checkpoint schema/hash/semantic-dedup handling and diary write/read code in SRC-1, `tortoise/sdk.py`, support [MEM-OBJ-authored-points](memory.md#mem-obj-authored-points) and [MEM-RTE-checkpoint-diary](memory.md#mem-rte-checkpoint-diary). The account separates generic caller agency from human approval and dedup from factual checking. SRC-1, `tortoise/capture_spool.py`, supports the filing/backoff interpretation of [MEM-OBJ-capture-spool](memory.md#mem-obj-capture-spool). Its incomplete producer and race/recovery coverage is not presented as exactly-once capture.

I compared the hook's nonblank-output and harness branches with the CLI digest and local session-context queries. [MEM-RTE-hook-volunteer](memory.md#mem-rte-hook-volunteer) and [EPI-RTE-hook-context](epistemic.md#epi-rte-hook-context) describe the same seam. [MEM-RTE-start-digest](memory.md#mem-rte-start-digest) and [MEM-BAP-start-digest](memory.md#mem-bap-start-digest) correctly identify a different recency selector and advisory channel. The local digest lacks terminal-status exclusion. Thus [MEM-RTE-point-retraction](memory.md#mem-rte-point-retraction) and [EPI-RTE-point-withdrawal](epistemic.md#epi-rte-point-withdrawal) cannot warrant universal withdrawal from context. Their source-level CAS, ignored append result, message invalidation and dirty-marking findings hold; the reconciliation preserves the reader-specific qualification.

SRC-1, `tortoise/session_reinjection.py`, supports the seeded Session traversal, distinct-item budgets and retained original pool on fetch failure in [MEM-RTE-source-expansion](memory.md#mem-rte-source-expansion). Its shipped evaluation caller is not dismissed as external. Neither candidate-pool expansion nor the located caller establishes final reader reliance, graph/record parity or live reflex integration.

I traced numerical parameter reads and confidence arithmetic, the volunteer floor, dream batch write-back and correction sweep. [MEM-OBJ-belief-state](memory.md#mem-obj-belief-state), [EPI-OBJ-belief-state](epistemic.md#epi-obj-belief-state), [MEM-RTE-dream-writeback](memory.md#mem-rte-dream-writeback), [EPI-RTE-belief-evaluate](epistemic.md#epi-rte-belief-evaluate) and [EPI-RTE-belief-retain](epistemic.md#epi-rte-belief-retain) preserve their different scopes. Posterior/prior arithmetic, scalar materialization and freshness stamps do not establish calibrated truth. Failed convergence can still permit scalar write-back; stale-run suppression is separate. The epistemic account correctly notes posterior-first readers rather than treating the scalar alone as the universal gate input.

For [EPI-RTE-source-address](epistemic.md#epi-rte-source-address), the quote matcher and value-span predicate support occurrence, not entailment, and a failed span does not universally reject the payload. [EPI-RTE-vet-check](epistemic.md#epi-rte-vet-check) and [EPI-RTE-vet-disposition](epistemic.md#epi-rte-vet-disposition) correctly separate judgment from effect: mechanical decisions survive arbiter failure/NOOP, while dependency repair can retain or restore a referenced entity. The declared flags, injected arbiter and content-bearing candidates make these supported branch distinctions; they are not inferred from types or an unchecked hypothetical bypass.

[EPI-OBJ-review-verdict](epistemic.md#epi-obj-review-verdict), [EPI-RTE-review-disposition](epistemic.md#epi-rte-review-disposition) and [EPI-RTE-review-integration](epistemic.md#epi-rte-review-integration) are supported by SRC-1, `tortoise/review_verdicts.py`, and the SDK promotion tail. Sweep's automatic keep requires its opt-in flag and threshold; explicit decisions remain a separate route. Measurement is disclosed but not an acceptance gate. Promotion eligibility can refuse keep, and prior wiring/supersession can be partial after promotion. The reports neither convert these operational decisions into independent factual certification nor infer learning, exercised self-improvement or a complete theory-builder loop.

The passages for [EPI-CLM-evidence-authority](epistemic.md#epi-clm-evidence-authority) and [EPI-CLM-belief-propagation](epistemic.md#epi-clm-belief-propagation) are target doctrine. Conditional source addressing and numerical propagation support the stated narrower comparisons, not the README's universal quoted-evidence claim or validated real-world probabilities.

### Relations, omissions and stopping decision

I checked all declarations, source-anchor meanings, evidence-status choices and annotations. Wired/implemented findings describe source behavior; no observed or causal layer is smuggled in through names or comments. No evidenced-absence records are declared. The four explicit `Part of:` relations—S4 review, source addressing, VET judgment and VET disposition within SDK capture—are supported containment relations. The parent remains valid. The [reconciliation](reconciliation.md#reconciliation)'s two supersessions correctly identify duplicate hook and retraction routes. Payload/admitted products, overlapping numerical objects and maintenance/evaluation/retention functions retain distinct referents rather than receiving unjustified whole-record supersessions. No unresolved inter-report conflict or missing mandatory part was established. Reader-specific withdrawal and record/graph compatibility are qualifications, not contradictory findings erased by reconciliation.

Omission questions were selected from the frozen tree and producer/consumer dependencies: could another context consumer defeat withdrawal generalizations; could alternate admission paths defeat consent or measured-only interpretations; could an answer-producing lane change the deterministic-reflex account; and could a separate authority restriction make the correction inventory incomplete? The digest, direct writes, explicit verdicts and baseline-capable volunteer gate answer the first two without overturning the reports' already bounded wording. Searches beyond the listed anchors located SRC-1, `tortoise/ask_lane.py`, and its evaluation callers. The retained ask lane is explicitly evaluation-only and is not used here to characterize the product reflex or establish an observed answer result. Complete evaluation/reader coverage remains unclaimed.

The last question found the local omission below: claim-class restrictions are an additional authority mechanism, not evidence of factual acceptance. New inspection of SRC-1, `tortoise/claim_class.py`, and SDK create/supersede/operator gates supplies implementation evidence only. The marker rule is explicit:

> return any_derived(source_classes) and any_asserted(target_classes)
> --- `tortoise/claim_class.py`

The supersession consumer can refuse the transition:

> if _claim_class.blocks_override(
>                 _supersede_classes.get(new_id),
>                 _supersede_classes.get(old_id)):
>             raise ValueError(_claim_class.supersede_refusal(
>                 old_id=old_id, new_id=new_id))
> --- `tortoise/sdk.py`

This finding does not warrant a universal override-safety claim: all import, propagation and alternate edge paths were not audited. It also does not equate the source's `derived` label with independently established entailment. The emitted conclusions remain valid because the reports make no exhaustive authority inventory or universal acceptance/absence claim. Further optional omission expansion stopped here: the selected questions have dispositions, remaining coverage is explicitly partial, and no identified material challenge remains without a disposition. Additional repository artifacts alone would not justify treating this selective account as complete or demanding an exhaustive audit.

## Blockers

none

## Limits

- The authority inventory is incomplete beyond the selected correction and belief routes: [EPI-RTE-review-integration](epistemic.md#epi-rte-review-integration), [EPI-RTE-belief-evaluate](epistemic.md#epi-rte-belief-evaluate) and [RT-RTE-direct-point](runtime.md#rt-rte-direct-point) do not inventory the separate caller-supplied claim-class marker and its derived-over-asserted override restrictions (SRC-1, `tortoise/claim_class.py`, `tortoise/sdk.py`; checked passages above). The partial-loop account and its supported acceptance/selection findings remain valid. Readers should withhold a complete comparison of authority restrictions, class-aware supersession and propagation safeguards; the omitted mechanism is neither proof of factual truth nor an audited all-path invariant.
