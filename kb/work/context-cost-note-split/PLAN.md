# Plan: split the context-cost note family
Restructure the context-efficiency / framework-overhead material into a clean three-note ladder, compatible with title-as-claim. Redline this before any note is touched.
## Why
Two problems with the current state:

1. `context-efficiency-is-the-central-design-concern-in-agent-systems.md` is large and, read literally, argues only the **feasibility why** (per-window soft degradation). The **cost why** (aggregate token economics) is barely present.
  
2. `framework-overhead-splits-into-feasibility-and-cost-budgets.md` (just written, committed `8057bc7e`) currently has to carry the _general_ feasibility/cost distinction itself, even though that distinction is framework-agnostic and belongs upstream.
  

Key structural insight from the design discussion: **the feasibility/cost split is constitutive of the scarcity argument, not downstream of it.** Context is scarce for two _different reasons_ with two _different mechanisms_:

- **feasibility why** — within one window, attention degrades → a per-window competence ceiling (capability mechanism; low degree-of-freedom; can't tier or expand without architecture change)
  
- **cost why** — processing tokens costs money/latency, summed across calls (economic mechanism; ordinary-resource-like; higher degree-of-freedom — tier, batch, cache, just spend more)
  

The contrast between the two whys is exactly what justifies the ranking: **feasibility binds first.** A feasibility violation is a hard constraint (impossible at any price); a cost overrun is a soft, continuous penalty.
## The trap we are avoiding
Context's _centrality_ is grounded in the feasibility why. So "context efficiency is the central design concern" and "context efficiency impacts feasibility" are nearly the same claim. Splitting naively produces two overlapping notes (fails body-composability).

**The discipline that makes the split clean:** the hub states _that_ both faces exist and ranks them, but never develops the per-window mechanism. All per-window mechanics live in the feasibility child.
## Proposed note set
### Note 1 (hub) — keep title "Context efficiency is the central design concern in agent systems"
Lean. Owns:

- context is _the_ scarce resource (contrast with traditional compute/memory/storage/bandwidth)
  
- it is scarce via **two distinct mechanisms** (feasibility why + cost why, as above)
  
- therefore efficiency has two impacts: feasibility and cost
  
- **feasibility binds first** (the degree-of-freedom argument)
  
- the cost face stated in ~1 paragraph (secondary, ordinary-resource-like) — no separate cost note yet (YAGNI)
  

Does NOT develop: degradation mechanics, volume×complexity, architectural responses. Links down to 1a and 2.
### Note 1a (new) — feasibility deep-dive
Candidate claim title: **"Per-window context inefficiency makes tasks infeasible, not just expensive"** Absorbs the bulk of the current hub body:

- soft-degradation consequences (per-window ceiling)
  
- volume × complexity dimensions
  
- growing windows address volume but not complexity
  
- task-relativity of the usable budget
  
- architectural responses (frontloading, sub-agent isolation, navigation, progressive disclosure, context management, instruction-notes)
  

Grounds in: `agent-context-is-constrained-by-soft-degradation-not-hard-token-limits`, `effective-context-is-task-relative-...`.
### Note 1b (cost face) — DEFER
One paragraph in the hub for now. Promote to its own note only when something needs to cite it.
### {==Note 2 — framework overhead (refactor existing `framework-overhead-splits-into-feasibility-and-cost-budgets`)==}{>>Now I think that the second note will be trivial - it is a straightforward application - so we don't need it. We might add it later when we develop more ideas about what is special about the framework overhead<<}{id="c1" by="user" at="2026-06-06T14:52:29.048Z"}
Possible retitle (current title now partly restates Note 1's split): candidate **"A framework's overhead is net context charged against both budgets"** — or keep current title. DECIDE. Keeps, and stops re-deriving the general split (cites Note 1 instead):

- framework overhead is a **net** quantity (instructions added − content spared); net-tax vs net-enabler
  
- under forking: per-agent feasibility (heaviest fork) + summed cost
  
- **gross-vs-net refinement to preserve:** spared-content credit applies to the feasibility signal only; the cost total counts every re-paid token as real spend (current line 33)
  
- evaluation consequence (feasibility signal + cost signal; the amortization error)
  

Grounds in: Note 1 (the bifurcation + ranking), Note 1a (the per-window mechanism).
## Grounding edges
Note 2 → grounds → Note 1a → grounds → Note 1. Plus Note 2 → grounds → Note 1 directly for the ranking.
## {==Open decisions for redline==}{>>do as recommended above<<}{id="c2" by="user" at="2026-06-06T14:54:36.219Z"}
1. {==**Architectural responses placement** — proposed: all in Note 1a. Alternative: keep a thin catalog in the hub. (They are mostly per-window/feasibility responses, so 1a is the lean choice.) — DECIDE==}{>>do as recommended above<<}{id="c2" by="user" at="2026-06-06T14:54:36.219Z"}
  
2. {==**Note 1a title** — is "infeasible, not just expensive" the right claim, or something narrower? — DECIDE==}{>>do as recommended above<<}{id="c2" by="user" at="2026-06-06T14:54:36.219Z"}
  
3. {==**Note 2 retitle** — retitle to foreground the _net_ insight, or keep "Sub-agent decomposition splits…"? — DECIDE==}{>>do as recommended above<<}{id="c2" by="user" at="2026-06-06T14:54:36.219Z"}
  
4. {==**Prior-work section** (Simon/Miller/Toffler) — stays in hub, or moves to 1a with the mechanics? — DECIDE==}{>>do as recommended above<<}{id="c2" by="user" at="2026-06-06T14:54:36.219Z"}
  
5. {==**Cost face** — confirm defer (no 1b yet). — DECIDE==}{>>do as recommended above<<}{id="c2" by="user" at="2026-06-06T14:54:36.219Z"}
  
## Sequencing
1. This plan approved.
  
2. Write Note 1a (move per-window mechanics out of the hub).
  
3. Slim the hub to bifurcation + ranking + cost paragraph; add down-links.
  
4. Refactor Note 2 to cite Note 1 for the split; keep net + eval + gross/net refinement.
  
5. Validate each; refresh indexes separately; reviews run by the other agent.
