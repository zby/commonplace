# Analyst instruction audit

- **Recorded:** 2026-09-30, at the operator's request, to hold the findings until work on the analysts' inputs resumes.
- **Status:** parked. Reducing command redirection comes first; the analysts' inputs are considered after that. Part of the runtime findings is already fixed (commit `ae70fe59`); everything else here is open.
- **Terms:** the three **analysts** are the runtime, memory and epistemic jobs (commit `85de9049`). A **trial** reruns one analyst on a recorded run's frozen inputs with `scripts/analyst_trial.py prepare` (commit `3ac5361f`).

## Method

Two probes, both on the instructions as committed at `85de9049`–`ae70fe59`:

1. **Analyst trials.** The runtime analyst rerun on the frozen boundary of `AAS-2026-09-30-instinctual-memory-02`, varying only the model. The target observation is whether the member covers `mem tidy`, an LLM-judged, user-reviewed criticism route whose suppressions later consolidation reads (`src/tidy.rs`, `src/consolidate.rs:148-153`). Its absence from the published review made that review's "no criticism, no self-improvement" verdict rest on an incomplete route inventory.
2. **Fresh-eyes audits.** For each analyst, an agent with no project context read exactly the instruction files that analyst's prompt lists, and reported every term or rule it could not understand from those files alone: defined there, defined only in a linked file the worker is not given, or defined nowhere.

## Trial results so far

| Run or trial | Analyst | Model | `mem tidy` covered? | Route split |
|---|---|---|---|---|
| `AAS-2026-09-29-instinctual-memory-03` (failed run) | runtime / all | `gpt-6-astra` | by the epistemic analyst only | — |
| `AAS-2026-09-30-instinctual-memory-02` (published) | runtime / all | `gpt-6-luna` | no member | by interface (hooks, MCP, CLI and shell, …) |
| `AAS-2026-09-30-instinctual-memory-03` (stopped) | runtime / all | `gpt-5.6-sol` | by the memory analyst only | — |
| trial `…-trial-runtime-sonnet-…-01` | runtime | Claude Sonnet | yes, its own route (RTE-5) | by operation (injection, search, consolidation, change, tidy, erase, writeback) |
| trial `…-trial-runtime-luna-…-01` | runtime | `gpt-6-luna` | no | mixed |

In no full run did the runtime analyst, which owns the route inventory, record tidy; coverage came from whichever other analyst happened to. Both trial members pass the runtime validator. One sample per cell cannot separate model from chance, but the split pattern points at the missing definition of "route" (below): an interface-based split hides an operation inside a broader route.

Observation for the testing method: a weaker model exposes instruction gaps that stronger models recover from, so wording trials should run on the weakest model accepted in production, with stronger models as the ceiling.

## Findings common to all three analysts

- **Defined only in a file the analyst was not given.** The record-ID grammar, the full list of record kinds and their prefixes, the conclusion-status values, the source-anchor and quotation rules, and what the set, a member and the overview are, live in the overview type. The judging norms told the analysts to "load" it, by link only. **Fixed in `ae70fe59`:** all three analysts now get the overview type as a declared input.
- **References to things an analyst never sees:** "the reconciliation" (used both as a section and as an actor), "the set", other analysts' members, "Commonplace ontology".
- **Judging-norm rules of unclear scope:** the theory-builder conditions, learning, reflection and autonomy are phrased as rules for every judge; the memory and epistemic analysts cannot tell whether they apply to them. "Reach" is undefined everywhere.
- **The evidence ladder** in the judging norms (context presence → activation, claim → affordance → wiring → observation → causality, curation → warrant) has no test for any rung; only activation is defined, in the runtime type.
- **Run machinery** in the worker rules — "acceptance commands", "problem report", `<run-state-path>` — is undefined; the memory method uses a different placeholder (`<sibling-run-state-path>`).

## Runtime analyst

Inputs: `jobs/runtime.md`, worker rules, judging norms, runtime report type (and, since `ae70fe59`, the overview type).

**Undefined core concepts**, ranked by effect on the member:

- **route**, including "material route", "theory route" and "admitting route": used as a record kind, an execution path and a loop, with no definition and no membership test for theory routes;
- **operative object** and **behavioral-authority path**: record kinds with no definition; the latter's fields consumer, channel, force and horizon have no meaning attached;
- **guarantee**, **load-bearing**, **enforcement point** and **guarantee strength** (no scale);
- **material**, **forcing case**, **consequential claimed work**, **shipped entry paths**;
- "capability surface, current grant set, deployed isolation envelope": three distinctions the job requires, none defined and none with a field;
- **canonical**, used in two senses (declared by its owner; content-addressed);
- **representational form** and **distributed-parametric**: examples only.

**Fixed in `ae70fe59`:** "unprefixed IDs"; the rule that the runtime member states `none found` for a kind empty across the whole set, which it cannot know; "selected by the producing skill" (left from before the workflow); the jargon placement rules for component fixity and revision admission; the conflicting placement of decision roles; read-back fields on routes with no retention; "fixity fields" named nowhere in the type.

**Still open:** the Runtime account's required fields are one run-on list; several job steps need another passage loaded first ("fields the type's Runtime account and Routes records require … read-back fields the Routes records list"); probe capsules' relation to the boundary's `SRC-*` namespace is unstated.

## Memory analyst

Inputs: `jobs/memory.md`, worker rules, judging norms, `analyse-agent-memory.md`, memory report type, runtime report type (and the overview type).

**Undefined controlled values**, the largest gap:

- the **evidence bases** `claimed`, `afforded`, `wired`, `observed`, `causally supported` — undefined; order implied only by the judging norms' no-upgrade chain;
- the coverage assessments `absent`, `inapplicable`, `uninspected` — undefined (`known`, `partial`, `not-determinable` are defined); whether a yes/no axis uses `known` with `"no"` or `absent` is unsettled;
- most **axis values**: all four `lineage` values, the `behavioral_authority` values, `repo`/`files`/`sqlite`/`rdbms`, `service-object`, `prompt-registry`, `coarse`, the `inferred-*` signals, `offline`/`online`/`staged`, the `trace_source` values;
- the YAML shape of `memory-comparison` (map or list); there is no example profile.

**Undefined or thin concepts:** the memory boundary ("retained objects accumulated or changed through use": "retained", "use", "accumulated" in narrow senses; whether a user-maintained memory file is in scope); "seeded record" and "supplied fact" (presumably the runtime member's); "trace" and "trace-fed write"; "load-bearing". A 2026-09-29 PageIndex trace audit had already found the specialist settling the ingestion-only scope question by reading validator code, and using `wired` as filler for a searched-for negative.

**Contradictions:**

- the method puts corrections to supplied facts under Core ideas (`analyse-agent-memory.md:55`); the type puts them under Integration issues (type:216);
- the method's section order ("core ideas, shared records, write side, read-back") does not match the type's;
- three ways to stop — a `blocked` report, the worker rules' problem report, and "refused while not a valid member" — with no rule for which applies; "needed scope expansion" does not say beyond what;
- the job allows citing records the Source register declares; the type requires every cited record to be declared or annotated in the report itself;
- annotation placement: `On <ID>`, `#### On <ID>`, under Shared records or in an `## Annotations` section that the memory type, unlike the runtime type, lacks; the fields an annotation may carry are not listed;
- the memory type has no template; its six kind headings are named only in the runtime type;
- a correction round must "write the whole report again" while IDs are final; keeping the previous round's IDs and withdrawing a record are not addressed.

## Epistemic analyst

Inputs: `jobs/epistemic.md`, worker rules, judging norms, `analyse-external-system-epistemic-architecture.md`, epistemic report type, runtime report type (and the overview type).

**Undefined core concepts:**

- **epistemic object** / **operative part**: nothing says what counts as one, or whether an object with no truth-apt content gets a row;
- **consequential** (function, claim, consumer, force): decides which ledger and claim rows exist;
- **warrant**, "warranted premises", source warrant "preserved, degraded, or unknown": the "derived warranted content" verdict rests on it;
- "checked interpretation or formal domain": the gate for carrying warrant into an entailed derivation;
- **candidate**: every truth-apt output, or only ampliative ones (blocks 2 and 4 disagree);
- **admission**, easily confused with acceptance and with the runtime type's revision admission;
- the behavioral-authority fields consumer, channel, force (two value sets: path force versus `implemented force`) and horizon;
- "route families", "route classes", "knowledge production" (defined only negatively).

**Overloaded words:** "claim" is both a system's claim (`CLM-*`) and a truth-apt proposition; "check" is an evaluation of content here and a probe in the runtime type.

**Contradictions:**

- the content/update relation values are to be tested "in the order listed"; read as first-fit, `ampliative conjecture` wins whenever entailment is merely unproven and `indeterminate` is never reached;
- method step 2 splits heterogeneous containers into new `EPI-` records, while the judging norms say only the reconciliation splits a record and records are never re-declared;
- the type locates the Source register in the overview, which does not exist when the job runs; the job and method say `boundary.md`;
- the method's `no relevant route found` differs from the type's value `no route found within boundary`; "global no-candidate statement" is not linked to the type sentence it means;
- "each passage occurs once across the set" cannot be guaranteed while the memory member is written in parallel;
- `EPI-RTE-*` records must carry every runtime-route field, including read-back and theory fields whose scope for epistemic routes is unclear.

## Proposed next steps, when this resumes

1. Fix the contradictions — wording only, no design choices; one commit per analyst.
2. Draft a glossary per analyst type for the operator's review, since each definition is a decision: runtime (route first — an operation from trigger to effect, with interfaces as entry points into routes; then operative object, guarantee, material, forcing case, the evidence ladder); memory (evidence bases, assessments, axis values, an example profile); epistemic (epistemic object, consequential, warrant, candidate, the two senses of claim and check, the authority fields).
3. Rerun the luna and Sonnet runtime trials on the revised text, a few samples per cell, and compare route splits and tidy coverage.
4. Consider templates with labelled fields for the symbolic parts (record fields, placement rules), leaving the definitions as the semantic content the analysts need.
