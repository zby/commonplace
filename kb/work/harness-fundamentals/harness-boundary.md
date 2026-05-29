# Harness fundamentals — what is the boundary? (brainstorm)

Workshop note, **brainstorming phase**. Holding alternative formulations open — not converging yet. Each candidate is a way to draw the harness / not-harness line; we keep the arguments for and against.

Shared starting point: the joint system is model + the stuff around it. The harness is *some* of that stuff. Question: which.

---

## Candidate A — "the harness is the code part"

The harness is the executing code; the model is weights; everything read into a call (AGENTS.md, skills, prompts, state) is a retained artifact.

**For:**
- Crisp, mechanical test — code vs. not-code. No porousness.
- Clean division of labor with the retained-adaptation paper: that paper owns the nouns (artifacts), harness theory owns the verb (the loop).
- AGENTS.md falls out as obviously *not* harness — it's read, not run.

**Against:**
- Smuggles in a **substrate assumption**. The memory paper's own move is that representational form is orthogonal — a harness can have operative parts in **prose** (built-in ReAct scaffolding, a shipped system preamble) that genuinely constitute the loop, not just config.
- Over-includes: a **user-provided tool is also code**, yet intuitively not harness. So code is necessary-ish but not sufficient.

---

## Candidate B — "constitutive vs. consumed-as-input"

The harness is whatever *constitutes* the loop mechanism (control flow, selection, brokering); everything supplied per deployment to parameterize it is consumed config.

**For:**
- Drops the substrate assumption — a constitutive part can be code *or* prose.
- Sorts the clean cases right: hardcoded orchestration prompt = harness; project AGENTS.md = config.

**Against:**
- The discriminator (shipped/built-in vs. supplied-per-deployment) is **provenance-based and fuzzy** — the spectrum between "defines the loop" and "parameterizes it" is unresolved.
- Doesn't explain *why* it's fuzzy; just relocates the fuzz.

---

## Candidate C — "web framework / inversion of control"

The harness is the framework that owns the loop, **plus everything registered into its extension points**. Membership decided by control flow, not authorship: the harness *calls back into* its parts (Hollywood principle).

- harness **calls back** an extension → harness (a registered hook running on the loop's terms)
- harness **reads** an artifact → config
- model **chooses to invoke** something → tool

**For:**
- Explains *why* the boundary is fuzzy: it's the framework's extension surface — a real but principled blurry line, like every web framework.
- Makes the harness **extensible-by-construction**; author becomes irrelevant. A user can write a `select` strategy that *is* harness.
- Re-sorts cleanly: AGENTS.md is read, never called back → config. A user lifecycle hook is called back → harness.
- Keeps form orthogonal: a registered hook could even be prose spliced in at a callback point.

**Against:**
- Leans on a notion of "extension point" that the framework must define — circular if the harness is exactly what defines its own extension points.
- Harder mechanical test than Candidate A; requires knowing the control-flow relationship, not just inspecting the artifact.

---

## Candidate D — "the harness is the `select` function"

From the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md): the loop is `while (P := select(K)) is not None: r = call(P); K = K + r`. This candidate identifies the harness with **`select`** — the function that assembles the next bounded prompt `P` from state `K` (and decides when to stop). Everything else is either the model (`call`), the data (`K`), or trivial plumbing (the `while`, the `K + r` append).

**For:**
- Pins the harness to where the **actual difficulty and design judgment live** — the note's whole "what makes selection hard" section is about `select`. The loop wrapper and state append are mechanical; `select` is the harness's real content.
- Sharp boundary against the model: `call` is the model, `select` is the harness, `K` is the data. Three clean roles.
- **`select` is necessarily code** — it is a *function* that assembles `P` from `K`. Prose can't *be* `select`; prose is a value `select` reads from `K` and emits into `P`. This **re-grounds Candidate A**: the reason "the code part" felt right is that the genuinely-harness thing (selection) is code by nature. Built-in orchestration scaffolding (B's "constitutive prose") is, on this view, just a **constant prose value in `K`** that `select` always emits — data, not harness. So D + this point say: prose is *never* harness; it always lives in `K`.

**Against:**
- **Too narrow.** Tool brokering, lifecycle hooks, sandboxing, the call mechanism itself — none are `select`, yet all feel like harness. It identifies the harness with one function and exiles the rest.
- Conflates "the hard part" with "the whole part." `select` may be where the *interesting* design is, but a harness is also the unglamorous brokering and I/O.
- The `while` and `K + r` are doing real work (control flow, state maintenance) that this candidate dismisses as trivial — state maintenance is a dynamics axis in its own right.
- Tools that the model invokes mid-`call` don't route through `select` at all, so this says nothing about tool governance — a thing every other candidate has to place.

---

## Candidate E — "the complement of the model" (everything not the model)

From [The Anatomy of an Agent Harness](../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.md) (@Vtrivedy10): *"Agent = Model + Harness. If you're not the model, you're the harness. A harness is every piece of code, configuration, and execution logic that isn't the model itself."* Explicitly includes system prompts, tools/skills/MCPs and their descriptions, bundled infrastructure (filesystem, sandbox, browser), orchestration logic, and hooks/middleware.

This is the **maximal** definition — the opposite pole from D. The harness is defined by subtraction: `harness = agent − model`.

**For:**
- Dead simple, zero edge cases: the model/not-model line is sharp, so there is never ambiguity about membership.
- Author/substrate/role all irrelevant — config, prose, tools, code all included. No fuss about user extensions or "constitutive prose."
- Pedagogically forcing: "design systems *around* model intelligence" — the framing the author explicitly wants.

**Against:**
- It's a **perimeter, not a decomposition** — our own runtime note's critique. "Everything not the model" names what's left over, not a thing with structure. It groups the filesystem, a system prompt, and the control loop as one category despite their having nothing architecturally in common.
- It **re-collapses exactly what "Where It Lives" and this whole brainstorm pull apart.** Under E, AGENTS.md, tools, state, and the loop are all "harness" — which is the lump the memory paper rejected. E and the retained-adaptation vocabulary are incompatible by construction.
- Useless for the dynamics work: if everything-not-model is harness, "harness theory" has no specific object — it's just "agent engineering."
- The author admits it: *"many messy ways to split the boundaries... this is the cleanest definition because it forces us to think about designing systems around model intelligence."* The justification is **rhetorical/pedagogical**, not architectural — chosen for what it makes you think about, not for carving at a joint.

**Note:** E is the inherited default (the survey's `E/T/C/S/L/V` is E with the leftover sorted into six bins). The narrowing candidates (A–D) are all reactions against E. So the real spectrum is: **E (everything) → A/B/C (the loop mechanism) → D (just `select`).**

## Cross-cutting observations (not yet a decision)

- **Is form orthogonal, or does the boundary force code?** A, B, C treat representational form as orthogonal (the memory-paper move) — a harness part could be prose. **D denies this**: `select` is a function, so the harness is necessarily code, and all prose lives in `K` as data. This is now a live disagreement, not a settled observation. If D is right, "constitutive prose" (B) is a category error — built-in scaffolding is just a constant value in `K`.
- The four typed relationships recur across B, C, D: **calls** (model, tools), **reads** (config), **maintains** (state `K`), **is** (the loop / `select`). Disagreements: where user extensions land (A vs. C), and whether the harness is the *whole* loop or just `select` (D vs. the rest).
- **Width axis among the candidates.** Order by inclusiveness: **E (everything not the model) ⊃ A/B/C (the loop mechanism) ⊃ D (just `select`).** The central question is *how much to subtract from E*: is the harness everything-not-model, the loop mechanism, or one function? Each narrowing buys a sharper object for theory at the cost of E's zero-edge-case simplicity.
- **What we're reacting against.** E is the inherited default and the foil. The whole brainstorm is an argument that E is a *perimeter, not a decomposition* — so the interesting candidates are the ones that subtract something principled from it.
- Kernel analogy (sibling to C): harness = OS kernel (loop + syscall interface); tools = userland behind syscalls; AGENTS.md = config files; model = the processor scheduled onto.
- Recurring edges every candidate must answer: (1) **tool vs. internal helper** — model-invokable vs. loop-internal; (2) **user extension** — the case that splits A from C.

## Open question — the term itself

"Harness" is inherited from the survey literature and we are not committed to it. It carries a **horse/yoke image** — a thing strapped onto an animal to restrain and steer it — which both anthropomorphizes the model and frames the surround as *mere restraint* rather than the active loop that does the assembling and control. The connotation fights the content.

Candidate replacements (each leans toward a different one of A–D):

- **scheduler** — already our term in the bounded-context model for the control/`select` part; leans D/A. Risk: narrower than the whole loop.
- **runtime** — the executing environment around the model; leans A/B. Neutral, but vague and overloaded.
- **orchestrator / driver** — emphasizes active control of bounded calls; leans C/D.
- **framework** — leans C directly (owns the loop, exposes extension points).
- **kernel / shell** — the OS analogy; leans A/C.

No decision. Note that the right name may depend on which boundary candidate wins: if D, "scheduler" is almost exact; if C, "framework" fits; if A, "runtime."

## Next

Pick the dynamics axes work (boundary placement, verification, state locus, coordination) — but keep these three formulations live until one earns the commitment.
