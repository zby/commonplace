# Focused web-search plan

## Research target

Find a small number of primary, inspectable cases that bear on this chain:

```text
locally admissible unit encountered
  -> global role represented
  -> role conflict noticed
  -> restructuring subgoal originated
  -> move / merge / delete / reframe considered
  -> global rather than merely local repair selected
  -> later behavior, comprehension, or revision is better
```

Also search, as a distinct curiosity track, for active generation of a possible mismatch:

```text
load-bearing structural rule available
  -> consequence if false articulated
  -> case-specific boundary cue identified
  -> discriminating probe originated
  -> rule, artifact, plan, or uncertainty updated
```

The search is not a survey of whether AI-generated code or prose is “good” or “bad.” A source earns inclusion by exposing at least one transition in one of those chains and preferably comparing interventions on the same task or artifact. Software and natural-language evidence remain separate until a matched intervention justifies a cross-domain inference.

## Software primary-source queue

### 1. CodeTaste — discovery versus specified execution

[CodeTaste: Can LLMs Generate Human-Level Code Refactorings?](https://arxiv.org/abs/2603.04177) is the highest-priority software source. It mines 100 large multi-file refactorings and separates an instructed track from an open “improve this focus area” track. GPT-5.2 reached 69.6% alignment with a detailed transformation and 7.9% in direct open mode; the latter still had an 87% repository-test pass rate. Planning helped on average and raised GPT-5.2 alignment to 15.1%; oracle selection among several plans raised that model to 20.6% but did not help every model.

Two cases are unusually diagnostic:

- On Mockito, direct mode produced typos, import cleanup, and small renames rather than the historical package reorganization; plan mode remained superficial, while oracle multiplan produced a partial package reorganization but missed associated type and method renames.
- On AWS CLI, one agent inserted a `sys.modules` compatibility shim so tests could keep using obsolete imports, bypassing the intended migration.

**Audit next:** released tasks, exact prompts, traces, scoring rules, and whether the human refactoring is one reasonable target or uniquely compelled by later changes. Re-run selected cases with representation-only, anomaly-only, and supplied-alternative conditions.

### 2. Earlier refactoring study — a narrower discovery/execution contrast

[An Empirical Study on the Potential of LLMs in Automated Software Refactoring](https://arxiv.org/abs/2411.04444) uses 180 real Java refactorings. Generic opportunity identification was weak, while naming subcategories and narrowing the search space greatly improved identification. In a separate solution experiment, the prompt supplied the refactoring type, explanation, and exact code entities; the model then produced many expert-acceptable solutions.

**Audit next:** how much narrowing leaks the answer, whether opportunity labels are independent, and which misses involve responsibility structure rather than local refactoring. Use it as stage-contrast evidence, not as a clean architectural study.

## Natural-language primary-source queue

### 1. Model criticism for long-form generation — topicality can survive while structure fails

[Model Criticism for Long-Form Text Generation](https://aclanthology.org/2022.emnlp-main.815/) explicitly separates topical structure from high-level discourse coherence and coreference. Its experiments find that the studied transformer generators capture topics better than structural coherence or coreference. This is the closest primary grounding for the distinction between local topical fit and global organization.

**Limits:** the study uses 2022-era generators and an external latent structural critic. It does not test current coding-style agents, document revision, spontaneous noticing, or move/delete choices. Inspect its perturbations and released code for fixture-design ideas rather than treating it as direct evidence for the proposed agent mechanism.

### 2. TETRA — professionally revised fixture substrate

[Towards Automated Document Revision](https://aclanthology.org/2024.bea-1.21/) introduces TETRA, 64 ACL papers revised by three professional editors, with document- and paragraph-level revisions and feedback. The authors emphasize both coherence/consistency edits and the impossibility of treating one reference revision as the only valid answer.

**Use:** mine candidate move, merge, fold, and deletion cases; create an explicit section-role and argument-dependency rubric; then independently validate local coherence and global misplacement before running an agent.

**Limits:** TETRA is a human revision corpus, not evidence that LLMs miss these edits. Multiple references reduce but do not eliminate editorial non-uniqueness.

## Conditional methods and control leads

These do not test locally connected global misplacement. Keep them quarantined until a concrete fixture needs their method or control:

- [EditPropBench](https://arxiv.org/html/2605.02083) supplies fact graphs and direct-target/required-update/protected-unit scoring for global edit propagation. The edit is specified and the task is not placement.
- [DELEGATE-52](https://arxiv.org/html/2604.15597) finds prescribed split/merge and classification operations harder than local string operations across heterogeneous reversible document tasks. It is an execution boundary, not spontaneous noticing evidence.
- [LAMP](https://arxiv.org/html/2409.14509) shows that a cued span-level editing pipeline can delete prose. It can serve as counterevidence to pure inability, not as document-role evidence.
- [Agents Explore but Agents Ignore](https://arxiv.org/abs/2604.17609) separates information surfacing from later interaction in artificial agent tasks. It may inform trace labels.
- [SlopCodeBench](https://arxiv.org/abs/2603.24755) offers a later longitudinal erosion follow-on after the one-shot code fixture is established.
- [More Code, Less Reuse](https://arxiv.org/abs/2601.21276) remains excluded unless a public diff exposes the relevant anomaly, alternatives, and selection trace; aggregate addition counts are insufficient.

## Search tracks and queries

### A. Refactoring-goal origination

- `"LLM" "refactoring opportunity" identification specified refactoring`
- `"coding agent" discover refactoring intent multi-file`
- `"architectural issue localization" LLM repository`
- `"LLM" code generation critique generation gap refactoring`
- citation chains and released benchmarks from CodeTaste and the 2024 refactoring study

Look for matched conditions where the same model sees an open area, an ownership map, a named anomaly, a refactoring category, balanced candidates, and a detailed transformation.

### B. Additive bypass and later requirements

- `"coding agent" compatibility shim bypass refactoring`
- `"LLM" subtractive edit delete move code`
- `"test passing" architecture violation coding agent`
- `"coding agent" iterative requirements structural erosion`
- `"held-out requirements" maintainability coding agent`

Prefer concrete diffs and later changes: flags threaded through layers, duplicate ownership, wrappers that preserve obsolete APIs, and local conditionals that require another edit later.

### C. Locally coherent, globally misplaced prose

- `"large language model" local coherence global coherence discourse generation`
- `LLM topically coherent structurally incoherent long-form text`
- `LLM discourse role paragraph placement argument structure revision`
- `LLM document revision move merge delete paragraph benchmark`
- `LLM outline adherence section purpose long-form generation`

The target is a unit whose local window passes human review while a full-document view assigns it a different role. Random sentence shuffling, obvious intrusion detection, and pure chronology tasks are too easy unless they include a topically compatible hard stratum.

### D. Structural operation selection in prose

- `LLM text editing additive edits deletion preservation bias`
- `LLM document revision structural edits versus surface edits`
- `LLM critique rewrite delete merge sections`
- `LLM professional editor revision corpus coherence consistency`
- citation chains from TETRA, LAMP, and DELEGATE-52

Look for separate measures of problem detection, operation choice, and execution. A study that supplies the span and says “delete” is a capability ceiling, not spontaneous structural revision evidence.

### E. Prospective structural boundary probing

- `LLM spontaneous counterexample generation software architecture invariant`
- `LLM agent question generation responsibility boundary code design`
- `LLM problem finding document argument structure section role`
- `language model boundary condition discovery architectural rule`
- `LLM argument structure blind spot counterfactual testing`

Look for tasks where an ownership, section-role, argument-structure, or decomposition rule is available but the applicability question is not supplied, and where the model must connect an organizational consequence to observable evidence that this case may be exceptional. Prefer matched rule-holds, rule-fails, and plausible-false-lead controls. Generic problem-finding or scientific-hypothesis work may supply an experimental method, but it is not evidence for this workshop unless it exposes the structural transition. Generic question counts, unsupported speculation about an author's background, and benchmarks that hand the model the exact hypothesis do not test origination.

### F. Conditional global propagation and delayed prose outcomes

- `LLM manuscript edit propagation downstream claims`
- `LLM document revision consistency dependency graph`
- `LLM iterative document editing degradation`
- `argument dependency reading comprehension sentence placement`
- citation chains and released artifacts from EditPropBench

Defer this track until the base placement effect is established. Then prefer explicit dependency graphs, protected units, reader tasks, later edits, or blinded editorial comparisons over generic LLM-as-judge coherence scores.

### G. Conditional cross-domain intervention or learned origin

- `LLM code natural language shared planning local global coherence`
- `language model training local objective global structure transfer`
- `cross-domain transfer structural editing programming prose`
- `LLM hierarchical planning code text generation`

This is the last search track, not the first. Behavioral homology and intervention transfer should be established before pursuing claims about a shared learned faculty.

## Evidence ladder

1. **Best:** released artifacts, prompts, trajectories, role annotations, and matched interventions on the same cases, followed by a later-change or reader outcome.
2. **Strong:** controlled benchmarks separating open detection, global-model supply, candidate ranking, and specified execution.
3. **Useful:** human revision corpora or repository histories with inspectable structural edits that can become independently validated fixtures.
4. **Lead only:** practitioner incidents with frozen code/text and traces that can be independently checked.
5. **Vocabulary only:** essays about taste, slop, vibes, writing style, or engineering judgment.

Static smells, aggregate line counts, sentence perplexity, and generic preference scores can locate cases but do not show where the process failed. Broad correctness, security, hallucination, and content-quality studies are excluded unless they contain a matched role-to-subgoal transition or a discriminating global outcome.

## Capture schema for each case

- Artifact, snapshot, task, model, harness, budget, and available context.
- What local behavior, edit, or continuation was requested?
- What makes the target locally admissible?
- What global role expectation makes it misplaced, and who supplied that expectation?
- What structural rule or claimed invariant was available, what organizational consequence would follow if it failed here, and what observable boundary cue could motivate testing it?
- Was the applicability question self-originated, generically prompted, or supplied exactly?
- Did the proposed probe discriminate failure from compliance, and did its result update anything?
- Was the global model available, constructed, or absent?
- Did the agent mention the anomaly before editing?
- Did it create and retain an investigation or restructuring subgoal?
- Which local and structural alternatives were generated?
- Which candidate was selected, by what operative oracle?
- What did tests, local fluency, or sentence correctness prove, and what did they leave undiscriminated?
- Is there a future requirement, reader task, dependency graph, or expert role judgment that separates the designs?
- Can the same model diagnose, rank, or implement the missed design when directly prompted?
- Which rival explanations remain: missing knowledge, representation, context, significance, risk, candidate search, selection, or execution?
- Evidence strength, judge reliability, and source limitations.

## Concrete-note queue

The source and experiment work should try to earn these in order, with titles revised to match the evidence:

1. **Agents under-originate prose-rehoming goals they can execute when a document-role conflict is specified.**
2. **Semantic value and local connection do not establish a prose unit's positional value.**
3. **Agents under-originate refactoring goals they can execute when responsibility conflict is specified.**
4. **Prompted structural criticism does not imply autonomous structural intervention.**
5. **Agents under-originate consequential structural boundary probes they can answer when the exact applicability question is supplied.**

Only after matched intervention evidence should the workshop attempt a synthesis relating taste, global representation, surprise, curiosity, structural search, and oracle discrimination. Masking after local closure requires an explicit concern-before/absence-after trace; longitudinal erosion is a separate follow-on.

The first and third claims intentionally avoid “LLMs lack taste” and “LLMs lack curiosity.” They identify an observable stage gap while leaving room for different causes.

## Current evidence gap

The initial search found no controlled document-level study that runs the full transition:

```text
open-ended review
  -> notice topically connected but misplaced material
  -> originate move / merge / delete
  -> choose against additive accommodation
  -> improve a later global outcome
```

That absence is more useful than filling the workshop with generic coherence papers. TETRA and the local accepted revisions can supply human-grounded substrates; the matched experiment must supply the missing transition evidence.

## Stop rules

Stop broad search when the corpus has:

- two independent software sources for discovery versus specified execution;
- two inspectable software bypass cases;
- two independently validated prose fixtures that are locally coherent but globally role-incongruent;
- one genuine-bridge control, one prose capability ceiling for move/merge/delete, and one countercase where local repetition is beneficial;
- one matched intervention ladder in each domain; and
- at least one countercase in each domain where an open-ended agent originates and carries through the structural concern.

At that point, spend effort on re-running or analyzing cases rather than accumulating complaints. If a source cannot expose a process transition, furnish a fixture, or provide a discriminating global outcome, leave it out even if its headline agrees with the workshop.
