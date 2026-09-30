# Analyst instruction audit

- **Recorded:** 2026-09-30, at the operator's request, to hold the findings until work on the analysts' inputs resumes.
- **Status:** [Parameterized analyst instructions and direct launch delivery](./parameterized-analyst-invocations.md) is implemented and tested, including two commissioned Luna trials. It resolves the delivery and parameter findings and the memory and epistemic merge contradictions recorded below. Part of the runtime findings is fixed (commit `ae70fe59`). Undefined concepts and the runtime analyst's other open items remain pending.
- **Terms:** the three **analysts** are the runtime, memory and epistemic jobs (commit `85de9049`). A **trial** reruns one analyst on a recorded run's frozen inputs with `scripts/analyst_trial.py prepare` (commit `3ac5361f`).

## Operator decisions (2026-09-30)

These settle the contradictions that the proposal's merge rule could not settle from a type or shared rule, so the memory and epistemic merges are not blocked on them.

1. **Memory annotations go in an `## Annotations` section,** as in the runtime type. It holds only `#### On <ID> — label` headings on records declared elsewhere, carrying the memory-specific fields the memory type lists. The validator finds annotation headings anywhere; the rule is for one placement across the types.
2. **IDs across memory correction rounds:** a record that survives a correction round keeps its ID with the same referent; a new record gets a new number; a number is never reused, including one whose record was dropped. No withdrawal marker is needed: only the accepted round's report enters the set, and the only citations of an earlier round's IDs are the reconciliation's returned findings, which stay valid when numbers are not reused.
3. **Epistemic content/update relation values are a checking order, not first-fit.** Assign the first value whose test is established. `ampliative conjecture` requires positive evidence that the content does not follow from its inputs; when neither entailment nor non-entailment is shown, the value is `indeterminate`.
4. **Retiring the two merged method files:** approving the proposal approves the inbound-reference dispositions it lists — retarget each link to the merged job instruction, add a `properdocs.yml` redirect for each published page, and repoint workshop files by path only.

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
- **Run machinery** in the worker rules — "acceptance commands", "problem report", `<run-state-path>` — is undefined; the memory method uses a different placeholder (`<sibling-run-state-path>`). **Resolved by the proposal:** `run-state`, `problem` and `scratch` become supplied parameters, and the merge deletes the method's restated rules with their placeholder. "Acceptance commands" stays open.
- **Resolved by the proposal:** the linked-but-not-read gap in general, since code generates each job's `read-first` list from its declared dependencies; the epistemic member cited in memory correction rounds without being an input (it becomes the `epistemic` parameter); and the prompt-file exception in the worker rules (no worker reads a prompt file).

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

Inputs: `jobs/memory.md`, worker rules, judging norms, `analyse-agentic-system/jobs/memory.md`, memory report type, runtime report type (and the overview type).

**Undefined controlled values**, the largest gap:

- the **evidence bases** `claimed`, `afforded`, `wired`, `observed`, `causally supported` — undefined; order implied only by the judging norms' no-upgrade chain;
- the coverage assessments `absent`, `inapplicable`, `uninspected` — undefined (`known`, `partial`, `not-determinable` are defined); whether a yes/no axis uses `known` with `"no"` or `absent` is unsettled;
- most **axis values**: all four `lineage` values, the `behavioral_authority` values, `repo`/`files`/`sqlite`/`rdbms`, `service-object`, `prompt-registry`, `coarse`, the `inferred-*` signals, `offline`/`online`/`staged`, the `trace_source` values;
- the YAML shape of `memory-comparison` (map or list); there is no example profile.

**Undefined or thin concepts:** the memory boundary ("retained objects accumulated or changed through use": "retained", "use", "accumulated" in narrow senses; whether a user-maintained memory file is in scope); "seeded record" and "supplied fact" (presumably the runtime member's); "trace" and "trace-fed write"; "load-bearing". A 2026-09-29 PageIndex trace audit had already found the specialist settling the ingestion-only scope question by reading validator code, and using `wired` as filler for a searched-for negative.

**Contradictions** (handled by the proposal's merge, which follows the type or shared rule unless the job cannot follow it; resolutions are to be recorded here):

- the method puts corrections to supplied facts under Core ideas (`analyse-agentic-system/jobs/memory.md:55`); the type puts them under Integration issues (type:216);
- the method's section order ("core ideas, shared records, write side, read-back") does not match the type's;
- three ways to stop — a `blocked` report, the worker rules' problem report, and "refused while not a valid member" — with no rule for which applies; "needed scope expansion" does not say beyond what;
- the job allows citing records the Source register declares; the type requires every cited record to be declared or annotated in the report itself;
- annotation placement: `On <ID>`, `#### On <ID>`, under Shared records or in an `## Annotations` section that the memory type, unlike the runtime type, lacks; the fields an annotation may carry are not listed;
- the memory type has no template; its six kind headings are named only in the runtime type;
- a correction round must "write the whole report again" while IDs are final; keeping the previous round's IDs and withdrawing a record are not addressed.

## Epistemic analyst

Inputs: `jobs/epistemic.md`, worker rules, judging norms, `analyse-agentic-system/jobs/epistemic.md`, epistemic report type, runtime report type (and the overview type).

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

**Contradictions** (handled by the proposal's merge, as for the memory analyst). Two are errors on the type's side, which the merge rule does not resolve in the type's favour: the Source register placed in the overview, and "each passage occurs once across the set". One is between the method and a shared rule (splitting containers), which the shared rule settles.

- the content/update relation values are to be tested "in the order listed"; read as first-fit, `ampliative conjecture` wins whenever entailment is merely unproven and `indeterminate` is never reached;
- method step 2 splits heterogeneous containers into new `EPI-` records, while the judging norms say only the reconciliation splits a record and records are never re-declared;
- the type locates the Source register in the overview, which does not exist when the job runs; the job and method say `boundary.md`;
- the method's `no relevant route found` differs from the type's value `no route found within boundary`; "global no-candidate statement" is not linked to the type sentence it means;
- "each passage occurs once across the set" cannot be guaranteed while the memory member is written in parallel;
- `EPI-RTE-*` records must carry every runtime-route field, including read-back and theory fields whose scope for epistemic routes is unclear.

## Proposed next steps, when this resumes

1. Fix the runtime analyst's open items — wording only, no design choices. The memory and epistemic contradictions are handled by the proposal's merge.
2. Draft a glossary per analyst type for the operator's review, since each definition is a decision: runtime (route first — an operation from trigger to effect, with interfaces as entry points into routes; then operative object, guarantee, material, forcing case, the evidence ladder); memory (evidence bases, assessments, axis values, an example profile); epistemic (epistemic object, consequential, warrant, candidate, the two senses of claim and check, the authority fields).
3. Rerun the luna and Sonnet runtime trials on the revised text, a few samples per cell, and compare route splits and tidy coverage.
4. Consider templates with labelled fields for the symbolic parts (record fields, placement rules), leaving the definitions as the semantic content the analysts need.


## Memory merge resolutions (2026-09-30)

The parameterized memory job now owns the complete method; its invocation
supplies `boundary`, `runtime`, and the correction inputs. These resolutions
follow the report contract and worker rules unless an operator decision below
supplies the choice.

| Conflict | Reading kept |
|---|---|
| Corrections under Core ideas versus Integration issues | Integration issues owns every correction to a supplied fact, as the report type requires. Core ideas explains the distinguishing mechanisms. |
| Incomplete method section order | Follow the type's full order, including Boundary and evidence, Comparison rationale, Integration issues, and Limitations and checks. The type now has a section template and names all six record-kind headings. |
| Blocked report, problem report, or validator refusal | A job that cannot complete because access is missing or scope must expand writes `problem`, under worker rules. The type now distinguishes that job protocol from a retained blocked report. Justified unknowns that only limit conclusions remain in a complete report. Code refusals handle malformed submissions. |
| Job permits cross-member citations; profile requires local declarations or annotations | The local requirement applies to profile references. Other prose may cite the supplied runtime and boundary records, and supplied epistemic records in a correction. |
| Annotation heading and placement | Operator decision 1: `## Annotations` contains only `#### On <ID> — Label` entries. The type now lists allowed memory-specific fields; it does not repeat generic identity or route progression. |
| Correction rounds and final IDs | Operator decision 2: surviving records keep their ID and referent, new records use new numbers, dropped numbers are never reused, and no withdrawal marker is needed. |
| Method duplicates source, quotation and prior-analysis rules | Worker rules retain those rules alone, including the agent-listing and style-exemplar prohibitions. The method keeps only the memory-specific validation and publication checks. |

The old memory method's live links now target the merged job, including the
navigation link in the dated recovery probe; that probe's narrative is
unchanged. Frozen trial-bundle copies and historical plain-text mentions are
preserved as observations, not active callers. Workshop paths are repointed
without rewriting their narratives. Both the old page and its older skill URL
redirect directly to the job, without a redirect chain.

Retirement checks found no freshness baselines for the deleted memory method.
Redirect validation also exposed a pre-existing redirect for the restored live
`agentic-systems/reviews/instinctual-memory.md` page; the shadowing key was
removed so its live URL remains the destination.


## Epistemic merge resolutions (2026-09-30)

The parameterized epistemic job now holds the whole method, including the
wrapper's parallel-worker citation limit and its correction/duplicate rules.

| Conflict | Reading kept |
|---|---|
| First-fit relation assignment makes indeterminate unreachable | Operator decision 3: the list is a checking order; assign the first established test. Ampliation needs positive evidence of non-entailment; otherwise unresolved entailment uses indeterminate. The type now states this too. |
| Method splits supplied containers into new EPI records; shared rules reserve splitting to reconciliation | Inventory heterogeneous parts in separate rows. Declare distinct newly established objects, but flag a needed split of a supplied record beside the finding; reconciliation alone splits it. |
| Type locates the Source register in an overview that does not exist yet | Correct the type: use the supplied boundary register, which code later copies into the overview. |
| Method's no-route and global no-candidate wording differs from the type | Use `no route found within boundary` and the type's exact global no-candidate statement. |
| Passage must occur once across the set, but memory is written in parallel and reports are never rewritten | Correct the overview contract: cite a record when a supplied member already retains its passage. Independent parallel discoveries may retain the same passage; reconciliation identifies overlapping support without rewriting the members. |
| Every EPI route must carry read-back and theory fields regardless of applicability | The type now makes scope explicit: read-back fields record inapplicability when neither retention nor read-back occurs; admission fields apply to admitting routes and theory fields to routes involving formulated theories. Inapplicability does not establish a missing epistemic phase. |

The substantive six-block method and its misuse guards remain. Shared evidence
and register-ownership rules are not restated. The old method's public page
redirects directly to the job; workflow dependencies, pinned method paths and
the composition test use the consolidated instruction. Workshop paths alone
are repointed; frozen copies and historical observations remain preserved.


## Parameterized invocation trials (2026-09-30)

After the merge and trial-preparation changes were committed at `4e4f4013`, the operator commissioned memory and epistemic trials with fresh `gpt-6-luna` sub-agents. Both used copied boundary and runtime inputs from `AAS-2026-09-30-instinctual-memory-02`. The [implementation record](./parameterized-analyst-invocations.md#commissioned-luna-trials) records source revision, trial IDs, temporary output location, and checks.

Both analysts wrote their expected report on the first attempt, with no problem report. Their actual workflow validators returned no errors. Quote-anchor checks verified five passages in the memory output and two in the epistemic output, with no failures. All eight declared dependencies per trial and both prompt hashes remained unchanged. This is evidence that the parameterized instructions work for these two jobs on this input; it does not resolve the earlier runtime coverage question or establish semantic completeness.
