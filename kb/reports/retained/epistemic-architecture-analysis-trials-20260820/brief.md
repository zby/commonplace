# Brief: analyse an external system's epistemic architecture

## Governing question

What executable instruction should an agent follow to determine whether and how an external system produces knowledge rather than merely storing, reshaping, retrieving, or operationally using retained material?

## Audience and reader update

The immediate reader is an agent or maintainer performing a code- or document-grounded external-system analysis. After following the instruction, the reviewer should be able to identify the system's epistemic objects and transformations, trace candidate claims through evidence and acceptance routes, separate epistemic from operational authority, and state precisely what—if anything—the system warrants calling knowledge production.

## Target

- Path: `kb/instructions/analyse-external-system-epistemic-architecture.md`
- Mode: new write
- Collection: `kb/instructions/`
- Type: `kb/types/instruction.md`
- Provisional title: “Analyse an external system's epistemic architecture”

## User direction and retained intent

- Source: current user direction, 2026-08-20.
- Subject: promote the epistemic-architectures workshop result into a new review instruction for analysing how other systems generate knowledge rather than merely store memories.
- Required evaluation: have separate sub-agents apply the candidate instruction to `related-systems/arc-skill/` and to one previously reviewed memory architecture that performs non-trivial transformations.
- Selected held-out case: GBrain at `related-systems/gbrain/`, paired with `kb/agent-memory-systems/reviews/gbrain.md` for prior review context.
- Role: authoritative for purpose, scope, and required trials; it does not itself warrant factual claims about either system.

## Intended practical purpose

Produce one collection-neutral, source-grounded analysis procedure. It must work across memory subsystems and whole agentic systems. It should return route-level findings rather than force a system-wide taxonomy. It must distinguish generating novel candidate content from earning warrant for retained truth-apt content.

## Operativity

- Initial consumer: an agent or maintainer explicitly asked to analyse an external system's knowledge-production or epistemic architecture.
- Retrieval channel: the instruction's trigger-focused `description` plus explicit invocation by external-system review work.
- Force: prescriptive analysis procedure; its output informs a review but does not itself accept the external system's claims.
- Future conditional integration into `write-agent-memory-system-review` is a separate handoff. Do not edit that skill or the review type in this run.

## Required distinctions

- Storage, retrieval, consolidation, or fluent synthesis does not by itself establish knowledge production.
- Separate acquisition/import, non-ampliative reshaping, entailed derivation, ampliative conjecture, and behavior/policy adaptation.
- Separate epistemic objects: observation, source claim, derived claim, conjecture, explanation, executable model, plan, task outcome, scorecard, and other system-specific targets.
- Trace each applicable ampliative claim through the discovery lifecycle: observation, conjecture, consequence derivation, test, acceptance, integration.
- For each consequential check, name target, oracle, timing, force, epistemic authority, and operational authority.
- A grade or label is operative only on a route that consumes it to change rejection, revision, acceptance, retention, integration, rollback, use, or continued execution.
- Keep outcome checks, process checks, explanation warrant, and component attribution separate.
- Report lifecycle and authority per route; do not assign one unqualified epistemic status or oracle to a heterogeneous system.
- Separate code-enforced behavior, natural-language doctrine, reported operation, observed run evidence, and causal experiment evidence.

## Required instruction behavior

- Begin with prerequisites and a source/evidence boundary.
- Include an early short exit for systems that only retain or serve material and expose no relevant transformation or epistemic claim.
- Require an epistemic-object inventory before oracle assessment.
- Require at least one route ledger with an explicit output schema.
- Require a lifecycle disposition for every candidate truth-apt output.
- Require system-claim versus implemented-route comparison.
- End with a bounded conclusion stating what the system acquires, derives, conjectures, tests, accepts, integrates, or merely uses.
- Include misuse guards drawn from the six workshop cases without requiring the executor to load the workshop.
- Be executable on first reading and keep theory rationale out of the procedure body except where needed to make a decision.

## Scope

Include:

- natural-language, symbolic, and parametric retained outputs;
- human-, model-, program-, environment-, proof-, measurement-, and hybrid evaluation routes;
- systems that generate no claims, generate conjectures without acceptance, check consequences without accepting explanations, or integrate scoped accepted claims;
- route-level negative results and evidence gaps.

Exclude:

- ranking products by quality;
- treating benchmark success as component attribution;
- requiring every knowledge-producing system to use proposal comparison, natural-language claims, or the Commonplace storage model;
- designing a universal ontology of knowledge;
- adding controlled tokens or matrix schema before the trials show a stable need;
- editing the memory-review skill or type in this run.

## Collection and type constraints

- Follow `kb/instructions/COLLECTION.md`: executable and precise, frontloaded, explicit decisions and scope, minimal rationale.
- Follow `kb/types/instruction.md`: imperative title, trigger-focused description, prerequisites, steps, and verification where needed.
- Frontmatter must contain `description` and `type: kb/types/instruction.md` only unless a concrete runtime consumer requires more.
- The instruction must not depend on links into `kb/work/` during execution.

## Authoring evidence paths

### Workshop cases and result

- `kb/work/epistemic-architectures/README.md`
- `kb/work/epistemic-architectures/four-system-baseline.md`
- `kb/work/epistemic-architectures/ai-research-os-reading.md`
- `kb/work/epistemic-architectures/arc-skill-reading.md`
- `kb/work/epistemic-architectures/operator-response.md`

### Commonplace premises

- `kb/notes/definitions/discovery-lifecycle.md`
- `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`
- `kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md`
- `kb/notes/checked-outcome-licenses-episode-retention-not-abstraction.md`
- `kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `kb/notes/definitions/behavioral-authority.md`
- `kb/notes/an-action-model-matters-only-through-its-consumption-path.md`
- `kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md`
- `kb/reference/README-REVIEW-SYSTEM.md`

### Existing review machinery

- `kb/agent-memory-systems/types/agent-memory-system-review.md`
- `kb/instructions/write-agent-memory-system-review/SKILL.md`
- `kb/instructions/COLLECTION.md`
- `kb/types/instruction.md`

## Held-out trial boundary

GBrain is not an authoring source for reconstruction, disposition, skeleton, or first draft. Do not read `related-systems/gbrain/` or `kb/agent-memory-systems/reviews/gbrain.md` during those stages. After `draft.md` exists, two fresh trial agents will receive only the candidate instruction plus their assigned source paths and will write `arc-trial.md` and `gbrain-trial.md`. Their output tests executability and discrimination; it may justify revising procedure wording but cannot silently add new theoretical commitments.

## Known uncertainties and acceptance criteria

- The correct output may be a route ledger plus lifecycle disposition rather than a single knowledge-generation verdict. The instruction must resolve this operationally without inventing a system-wide scalar.
- It is unknown whether the same procedure will be concise on ARC and discriminating on GBrain. The trials are required evidence.
- The instruction passes only if both trial agents can execute it without clarification, keep source/doctrine/report distinctions, and produce different route-level findings appropriate to the systems.
- No missing evidence blocks drafting. Unsupported system-specific claims must stay in trial reports, not enter the instruction.
