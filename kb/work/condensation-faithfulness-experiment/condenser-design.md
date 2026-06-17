# Theory-grounded trace condenser (design)

Working design. The treatment in [protocol.md](./protocol.md) is **not** a tweak of ReasoningBank's condenser — it is a new trace-condensation step built from the KB's distillation/constraining/activation theory. We have never condensed traces before; our methodology condenses *authored* artifacts (notes, skills), human-in-the-loop and gated. This ports the load-bearing parts into an automatic, per-task condenser.

The three forks at the bottom stay **OPEN** — the live experiment resolves them.

## The fact that drives the design

ReasoningBank's seam is a single LLM call in `WebArena/induce_memory.py:main()`: `trajectory → one_step_chat(system_msg=SUCCESSFUL_SI|FAILED_SI) → markdown memory_items`. Retrieval (`memory_management.py`, embedding top-k) is separate and orthogonal.

Its condenser prompt **already** asks for the things naive intuition says produce good memory:

- *"first think why the trajectory is successful, and then summarize"* — ≈ `explanatory-reach`
- *"Prefer concrete, actionable procedures over abstract principles"* — ≈ actionability
- *"## Description … when or when NOT to use"* — ≈ a weak activation trigger
- fixed schema: Title / Description / Content, ≤3 items.

And the paper still finds its output behaviorally inert. **Therefore prompt-level exhortation is not the lever.** This is exactly what [constraining](../../notes/definitions/constraining.md) predicts: constraining narrows an artifact's interpretation space and *verifies* it; it is not achieved by asking nicely in prose. The native condenser sits in the "distilled but **not** constrained" quadrant despite good intentions.

Design consequence: our gain (if any) must come from **structure + enforcement**, not better wording. If our condenser were just a reworded prompt, the paper predicts it would also be inert.

## Design principles → note → failure mode attacked

| Principle | Grounding note | Paper failure attacked |
|---|---|---|
| Shape output for the **acting** consumer (a future agent mid-task, bounded context, selecting an action), not for a reader | [distillation](../../notes/definitions/distillation.md) | framing of the whole artifact |
| Each item is a **claim** — "In state S, do/avoid A, because R" — not a topic label | [constraining](../../notes/definitions/constraining.md); `title-as-claim` gate | §5.1 vagueness |
| Carry an explicit, **matchable Trigger** (task type / observed state / proposed action) so the memory can activate on-situation instead of being blindly prepended | [activate-behavior-changing-memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md); [knowledge-storage-does-not-imply-contextual-activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) | **§5.2 internal bias** (static prepend underweighted) |
| State **mechanism/why**, scoped to where it generalizes | `explanatory-reach` gate | §5.1 vagueness |
| **No overclaim** beyond the trace; mark scope and where NOT to apply | `grounding-alignment`, `load-bearing-qualifiers`, `source-residue` gates | §5.1 Table-1 failures (distraction / overreliance / premature) |
| **Codify the checkable**: if the lesson is a rule, emit a check/precondition, not prose (a check is not "underweighted by later layers") | [codification](../../notes/definitions/codification.md); representational-form | §5.2 internal bias |
| Pre-compute the lesson fully so the consuming call carries the answer, not the work | [frontloading](../../notes/frontloading-spares-execution-context.md) | context economy |
| **Self-check against gate criteria, then revise** before storing — enforcement, not exhortation | the `kb/instructions/` gate suite | the exhortation-fails fact above |

## Output schema (treatment)

Extends ReasoningBank's so the same retrieval/injection code can still consume it (the extra fields are additive markdown), but encodes the theory:

```
# Memory Item i
## Claim        <actionable proposition: in <state/situation>, do/avoid <action>>
## Trigger      <matchable condition: task type, observed page/tool state, or proposed action that should fire this>
## Mechanism    <why it holds — the causal reason, scoped>
## Scope        <where it generalizes; explicit "does NOT apply when …">
## Form         <heuristic | check>   # if check: a verifiable precondition the agent can apply mechanically
```

Generation is **not** one call. It is: draft → gate-check pass (against the load-bearing gate criteria) → revise → store. The gate-check is the automatic stand-in for the authoring workflow's review.

**Control stays** ReasoningBank's native condenser (SUCCESSFUL_SI/FAILED_SI, unchanged) — the fair baseline, not a strawman.

## Hypothesis (sharpened)

Because the native condenser already exhorts concreteness and still fails, any gain is attributable to **structure (Trigger/Mechanism/Scope/Form) + enforcement (gate-check loop)**, not wording. Predictions, measured by the [protocol](./protocol.md)'s perturbation set:

- Treatment shows a **larger** performance drop under Corrupt/Irrelevant/Filler than control → its content is causally load-bearing (more faithful) where the naive one is decorative.
- Treatment reduces the paper's Table-1 failure modes (distraction / overreliance / premature) → Scope and grounding prevent ungrounded over-application.
- Null result is informative: if treatment is *also* inert, faithfulness is not reachable by artifact form alone (supports the activation-channel half — fork A).

## Theory-transfer watch

Our condensation theory was built for authored artifacts. Forcing it onto raw traces in an automatic loop may strain it — e.g. the [system-definition vs knowledge-artifact](../../notes/definitions/system-definition-artifact.md) distinction, or register, may not map cleanly. Where it strains is a candidate durable note when the workshop closes, independent of the experiment's numeric result.

## Open forks (do not resolve here)

**Fork A — activation channel.** Change *only the artifact*, or also the *injection*? On-situation Trigger-matching vs ReasoningBank's top-k embedding prepend. Changing both confounds "better artifact" with "better activation." Candidate: two arms — (a) artifact-only swap, injection held constant; (b) artifact + Trigger-matched injection. The Trigger field is authored either way; whether it *drives* injection is the fork.

**Fork B — how much gate suite in-loop.** Full set per item is many LLM calls per task. Candidate load-bearing subset: `claim-strength`, `explanatory-reach`, `grounding-alignment`, trigger-presence — drop prose/style gates. The subset choice is itself a claim about what makes condensate faithful.

**Fork C — drop human review entirely?** The self-check pass is the automatic substitute for the authoring workflow's human gate. Whether gates-as-self-check preserve faithfulness without a human is a bet this experiment tests, not an assumption to bake in silently.
