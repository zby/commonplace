# Workshop: Read-back placement
## Question
The [seed claim](./seed-claim.md) argues that the **read-back path** — how a stored memory gets back into an action — is a design surface with its own degrees of freedom, and that our review type and design notes under-specify it: they give the write/learn loop named stages and give "read" a single retrieval bullet.

The claim looks right. The question this workshop answers is **not** "is the claim true?" but **"what does the KB have to change to act on it, and in what order?"** Specifically: the vocabulary we will use, the theory we will lean on, the review methodology that fills a read-back section, and only then the review-system revision itself.
## Why a workshop, and what becomes of the seed note

{>>Reply to c1 — agreed, and your second sentence is the sharper point. Subtract what the library already states (push/pull and storage→context→action; the loading methods and faithfulness test; activation-as-an-operational-axis) and what is left of the seed note is a *prescription*: our reviews should describe read-back as systematically as trace-derived learning. A review prescription's home is the review contract — the type spec — not a theory note, and not kb/reference (which describes the shipped system rather than instructing how to review external ones). So the working assumption is now: the seed note is consumed into the type-spec section and discarded, unless thread 2's subtraction test finds a one-sentence kernel worth folding into an existing note.<<}{id="c2" by="AI" at="2026-05-30T14:55:00.000Z" re="c1"}

The seed note is held here as a **consumable** workshop artifact, not a promotion candidate — the earlier "polished enough to promote to `kb/notes/`" framing was wrong. The genuinely new content is a **methodology prescription** (give read-back a placement section parallel to the write-side one), and methodology's home is the review contract — the [type spec](../../agent-memory-systems/types/agent-memory-system-review.md) itself.

We still run this through a workshop rather than editing the type spec directly because the **vocabulary and axis list must be settled once and reused** by the type-spec section, the seed note, and any existing note that gets a folded sentence — and because thread 2 has to run the subtraction test before we know whether *any* durable note survives at all. Promoting or editing first would lock in `read-back path` / `read-back-when-relevant` and a six-axis list before deciding whether those are the terms the review system will actually adopt.
## What the KB already has (theory is mostly assembled, not missing)
The biggest surprise from grounding: the read-back theory largely exists, scattered across the write-side framing.

- [activate-behavior-changing-memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) — already lists the **loading methods** (always-loaded, on-reference, on-invoke, on-situation, symbolic enforcement), the **typed-cue fields** (trigger, lesson, source pointer, behavioral authority, consequence weight, placement target), and the **faithfulness test**. This is most of the seed note's "placement axes" — but stated as a _requirement_ ("memory must activate before the mistake"), not as a _placement section_ parallel to the write-side one.
  
- [knowledge-storage-does-not-imply-contextual-activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — the storage → context → action distinction, and the two failure points (storage-to-context, context-to-action). The push/pull split is implicit here as the expert-witness vs advisor pattern.
  
- [memory-design-adds-operational-axes-to-artifact-analysis](../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) — names **activation** as one of six operational axes (capture, derivation, activation, authority, lifecycle, evaluation). The seed note expands _one_ of those six axes into its own placement section.
  
- [charting-the-knowledge-access-problem-beyond-rag](../../notes/charting-the-knowledge-access-problem-beyond-rag.md) — charts the **pull** side (navigation modes, transformation burden). The seed note carves out the **push** side it lists as one dimension.
  
- [behavioral-authority](../../notes/definitions/behavioral-authority.md) — the force-at-consumption term the seed note reuses as one axis.
  

The gap is therefore **framing and contract**, not new mechanism: the existing requirement language needs to be turned into a read-back placement section that mirrors the write-side one, and the vocabulary needs to be named once and reused.
## The concrete defect to fix
The [agent-memory-system review type](../../agent-memory-systems/types/agent-memory-system-review.md) is the sharpest instance of the asymmetry:

- **Write/learn side:** a nine-point `Trace-derived learning placement` section (trace source, extraction, storage substrate, representational form, lineage, behavioral authority, scope, timing, survey placement).
  
- **Read side:** one bullet in the Comparison Lens — _"Activation: Can relevant behavior-changing memory load before the agent repeats a mistake, or is the system limited to question-answer retrieval?"_
  

The target end-state is a **read-back placement section** that stands parallel to the trace-derived one, applied whenever a reviewed system has a non-trivial activation path.
## Work threads (the order you asked for)
### 1. Vocabulary — RESOLVED 2026-05-30

Decided (see [vocabulary-decision draft](./2026-05-30-vocabulary-decision.md)):

- **No new global vocabulary term.** The write side ("trace-derived learning") is not a CLAUDE.md term either — it is a section name. The read side is a **section name** in the type spec, not a global term. The `vocabulary-governance` coordination item is dropped.
- **Umbrella term = "read-back"** (the consumption path from stored memory to action). The coined "read-back-when-relevant" is **retired** — the push pole is just "push." Fallback umbrella if "read-back" later grates: "consumption path."
- **Direction axis = push / pull, from the AGENT's perspective, by agent solicitation:**
  - **pull** — the agent's *own* deliberate memory lookup: a query/search tool call, a chosen file read, a followed link. This is the only source of pull.
  - **push** — memory enters the agent's context *without the agent soliciting it*, whatever the trigger: an always-on load, a hook on an agent action, a situation/risk match, a schedule, **or any user-initiated event** — a user question, or the user explicitly asking the system to retrieve a memory. User-initiated retrieval uses pull machinery but is **push from the agent's perspective**, because the agent did not ask. Net rule: *pull has one source — the agent's deliberate lookup; everything else is push.*
  - Corollary 1 (expansion is scope, not direction): documented related-record expansion on an agent query is still pull (the agent solicited the query contract); *how much* expands is a **selection/scope** property.
  - Corollary 2 (mixed): an agent query that *also* injects unsolicited behavior-shaping material — the unsolicited part is push ("push riding on the pull interface"), a notable design worth flagging.
  - Corollary 3 (multi-agent): pull is relative to *which* agent's context — an orchestrator's or sub-agent's pull is **push** for the agent that receives the handed-over context.
  - Consumer scope: the push/pull axis (and the six placement axes) describe read-back **to the agent**, the primary consumer. But the same memory can be consumed **directly by the human user** — and by schedulers, reviewers, or governance (the type spec's existing *Consumer surfaces* lens already enumerates these). That is a separate **consumer dimension**, not a push/pull value: focus the axes on the agent, and flag other consumers where a system serves them. (For file-based memory the dual agent/human readership is a feature, not an edge case.)
- **`contextual activation` is untouched.** It stays the theory term for the push direction's success condition (knowledge reaching behavior unprompted). The read-back section *cites* it; no redefinition, no merge. Using push/pull for the direction values (rather than retrieval/activation) keeps "activation" reserved for this theory term and avoids the value/term collision entirely.

### 2. Theory support — RESOLVED 2026-05-30

- **Subtraction test run.** After subtracting what the library already states (push/pull and storage→context→action; loading methods and faithfulness; activation-as-an-axis), one theory increment survived: *the operational axes are independent of each other — fully specifying the learning axes leaves the activation axis open.* **Folded** into the "Why the split matters" section of [memory-design-adds-operational-axes](../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) (two sentences, including the agent-centric push/pull framing). No standalone note; the seed note is fully consumed.
  
- **`activate-behavior-changing-memory` left as-is.** Not re-cut; the type-spec section will *cite* it for loading methods + faithfulness rather than restate them.
  
- **Axis list confirmed (six).** trigger/relevance, direction (push/pull, agent POV), timing, selection/scope, authority-at-consumption, faithfulness. Five are re-labels of existing requirement content; only **direction** is a genuinely new organizing axis. No gaps, no redundancy worth cutting. This list is what the thread-4 type-spec section reuses.
  
### 3. Methodology — RESOLVED 2026-05-30

Answer to the load-bearing question (can a read-back section be filled from code as reliably as the trace-derived one?): **yes — arguably more so**, because integration wiring (tools, hooks, prompt templates, always-load) is literal code. Decisions:

- **Structural vs quality layer.** Report the observable mechanism per axis; explicitly mark precision/recall, dilution, and effective authority as not-verified-from-code (same discipline as the trace-derived section).
- **Capability vs deployed behavior.** End-to-end agents → report what the loop wires. Libraries/SDKs → report the API surface as capability (`search(query)` can't push; `on_action(ctx)→memories` affords push), don't assert deployed push.
- **Direction is the spine.** Lead with pull / push / both from the agent's perspective; the discriminating finding is push-path-or-pull-only.
- **Gating rule.** One-line direction verdict **always**; full `## Read-back placement` section **only when relevance-gated or engineered** (matcher / scope budget / before-action hook / faithfulness test). Naive-pull-only and unconditional always-load get the one-liner.
- **Tag.** Added **`push-activation`**, gated on the same condition as the full section (tag + section tied to one finding, mirroring `trace-derived`).

### 4. Review-system revision — DONE 2026-05-30

Landed in `kb/agent-memory-systems/types/agent-memory-system-review.md` (validated PASS) and its schema:

- Comparison-Lens "Activation" bullet → "Read-back (activation)" with push/pull framing and a pointer to the new section.
- "Read for Mechanism" focus list → added a read-back model item + a push-path determination line parallel to the trace-derived one.
- "Write the Review" list → added a Read-back placement bullet.
- Frontmatter → `tags` guidance now covers both `trace-derived` and `push-activation`.
- New **`## Read-back Placement`** authoring section (7-point axis list: direction, trigger, timing, scope, authority-at-consumption, faithfulness, other consumers) + the two code-inspection cautions + the gating rule.
- Template → added a `## Read-back placement` block.
- Schema → new conditional: `push-activation` tag ⇒ body must contain "Read-back placement" (parallel to the trace-derived conditional); headings description updated.

**Remaining (thread 5 / handoff):** the ~94-review backfill. Not done here — handed to [agentic-memory-review](../agentic-memory-review/README.md). Default: new reviews carry it; existing ones get the one-line direction verdict opportunistically, full section only when re-reviewed and the system qualifies.
## Adjacent live work — coordinate, don't collide
- [agent-memory-design](../agent-memory-design/README.md) — its **thread 4 "Activation machinery"** ("make the typed cue index operational: what fields, matching rules, priority budgets") is the _design_ counterpart to this workshop's _specification-discipline_ angle. Same subject, different cut: that thread designs the machinery; this workshop specifies how to describe and review it. Keep the axis vocabulary shared.
  
- [agentic-memory-review](../agentic-memory-review/README.md) — owns the next review pass over ~94 systems. If a read-back section lands in the type, that pass is the natural place to apply it. Sequence: settle the section here, then hand the backfill question to that workshop.
  
## Working conventions
- Hold exploratory objections and alternatives here; do not edit the seed note in place to encode a decision until the vocabulary thread closes.
  
- Do not link from library notes into this workshop — promote first.
  
- Record durable decisions under "Graduated changes" before closing.
  
## Graduated changes
- **2026-05-30 — Methodology + payload (threads 3–4) done.** Code-inspection methodology decided (structural vs quality layer; capability vs deployed; direction-as-spine; one-line-always / full-section-when-engineered gating). `push-activation` tag added. **`## Read-back Placement` authoring section, Comparison-Lens bullet, Read-for-Mechanism items, Write-the-Review bullet, frontmatter tag guidance, Template block, and a schema conditional all landed in `kb/agent-memory-systems/types/agent-memory-system-review.md` (+ schema), validated PASS.** Backfill of ~94 reviews handed to `agentic-memory-review`.
- **2026-05-30 — Theory (thread 2) resolved.** Subtraction test run; one surviving increment (operational axes are mutually independent — learning spec ≠ activation spec) **folded into `kb/notes/memory-design-adds-operational-axes-to-artifact-analysis.md`** ("Why the split matters" section, two sentences incl. agent-centric push/pull). No standalone note; seed note fully consumed. `activate-behavior-changing-memory` left as-is (cite, don't re-cut). Axis list confirmed at six; only "direction" is new.
- **2026-05-30 — Vocabulary (thread 1) resolved.** No new global term; "read-back" is the type-spec section name; direction axis = **push / pull from the agent's perspective** (pull = the agent's own deliberate lookup; *everything else is push*, including user-initiated retrieval — push machinery, but the agent didn't ask; documented expansion is still pull; expansion breadth is a scope property; pull is relative to *which* agent in multi-agent setups; the axes describe read-back to the agent as primary consumer, but the same memory can serve the human user directly and other consumers — a separate consumer dimension, cf. the Consumer surfaces lens); "read-back-when-relevant" retired; `contextual activation` left as-is and cited (push/pull values avoid colliding with it).
  
## Closure
Close when: (1) vocabulary is decided, (2) the subtraction test is run and any surviving kernel is folded into an existing note — or it is recorded that none survives, (3) the review type carries a read-back placement section (or there is a recorded decision not to add one), and (4) the backfill question is handed to `agentic-memory-review`. The seed note is deleted with the directory; it is a consumed artifact, not an output. Then remove its `kb/work/README.md` entry.
