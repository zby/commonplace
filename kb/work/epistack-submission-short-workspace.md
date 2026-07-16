# Epistack submission short workspace

Source workspace: [epistack-submission](./epistack-submission/README.md).

Status: separate working copy. Do not treat this as the live submission file. The goal here is a shorter draft spine centered on self-improving systems and Commonplace as a partially autonomous instance of one.

## Core claim

Commonplace is not being submitted as a finished epistemology engine. It is being submitted as a methodology and reference implementation for a self-improving epistemic work system.

The important claim is not that Commonplace already has perfect epistemic assessments. It does not. The important claim is that Commonplace has a loop for improving the methodology it runs on:

```text
search -> evaluation -> operative retention -> changed conditions for the next pass
```

Some parts of that loop are autonomous today: validators, type checks, quote grounding checks, review machinery, agent skills, and routing rules read Commonplace's own self-representations and change behavior accordingly. Other parts are still human-inclusive: noticing what matters, judging ambiguous semantic changes, and deciding which evaluation criteria are mature enough to trust. That split is the honest shape of the system.

This is why the current imperfection is not just a caveat. The system knows where the weak gates are, keeps humans there, records why, and has a procedure for hardening those gates one by one. Commonplace's epistemic value is therefore not only in the present checks. It is in the partially autonomous improvement loop that can make better checks operative.

## Judging criteria implications

The appendix says submissions are judged on epistemic uplift, generalizability, compounding and shareability, scalability, methodological transparency, adversarial robustness, and insight contribution. Strong submissions do not have to maximize every dimension, but they should engage most of them. Judges are also told to anchor against good off-the-shelf deep research or a careful Claude Code investigation, to value a clear spec over polish, and to run workflow submissions rather than merely read them.

That changes the short submission target:

- Lead with the **insight contribution**: self-improving epistemic methodology, not one-shot epistemic output, is the object that can compound.
- Show **epistemic uplift** with a concrete case walkthrough: the system makes load-bearing evidence, uncertainty, missing perspectives, and unsupported confidence visible in ways a narrative answer does not.
- Show **compounding and shareability** by pointing to structured, interrogable artifacts: source snapshots, ingests, notes, type contracts, validators, review criteria, rationale, and freshness records.
- Show **scalability** through the improvement loop: better models and more contributors increase search reach, adversarial scrutiny, and check coverage, while oracle domain still bounds unattended acceptance.
- Show **methodological transparency** by keeping the spec short and explicit: what the workflow does, why it is shaped that way, what it rejects, and where it is uncertain.
- Show **adversarial robustness** through conservative gates: quote grounding, provenance, refusal of unsupported scalar scores, labelled calibration before semantic gates get autonomy, and explicit human gates where oracles are weak.
- Treat **generalizability** as bounded: three differently shaped cases exercise the method, while clean-room replication remains designed rather than claimed.

Practical consequence: the main text should not spend pages on internal architecture. It should be a runnable, judge-facing spec plus one or two concrete examples of the loop improving the methodology. Details move to appendices.

## Short submission draft

### A self-improving methodology for agent-run epistemic work

Epistemic tools usually fail to compound for a mundane reason: their lessons do not become operative. A project discovers that a certain kind of evidence is correlated, that a source type needs special treatment, or that a review criterion is misleading. The insight is written somewhere, perhaps even elegantly. But the next investigator does not retrieve it, the next agent is not bound by it, and the next assessment silently starts over.

Against an off-the-shelf deep research baseline, the uplift is not that the system writes a longer or more confident report. The uplift is that it produces artifacts a later investigator can interrogate: source-grounded claims, visible uncertainty, explicit gaps, recorded rejections, and checks that can be rerun.

Our submission is a methodology for preventing that failure in agent-operated epistemic work. The unit is not a single claim, a scoring formula, or a finished assessment oracle. The unit is a self-improving methodology: a repository of rules, type contracts, validators, review criteria, design rationale, and case artifacts that agents read before acting, and that the system can revise when evidence shows the methodology is inadequate.

Commonplace is the reference implementation. It is a knowledge-base framework whose artifacts are not merely documentation about the system. Many of them are behavior-determining parts of the system. Collection contracts tell agents what kind of artifact they are writing. Type specifications define required structure. Validators reject violations. Skills route work. Review criteria are stored, snapshot-pinned, and rerun. Architecture decisions and proposals retain why a rule exists and why alternatives were rejected.

That makes Commonplace a partial self-improving system. Its improvement loop has three functions:

- Search brings a candidate change into consideration: a maintainer notices a failure, an agent finds a stale convention, a review exposes a missing criterion, or a validator identifies an inconsistency.
- Evaluation decides whether the candidate may be retained: by tests, validators, quote checks, calibrated review criteria, human judgment, or a combination.
- Operative retention makes the accepted change consequential: the change lands in a type spec, validator, skill, collection contract, review criterion, or routing rule that a future process actually reads.

The word "operative" matters. A lesson filed in a note is not enough. A rule nobody retrieves is inert. A validator nobody invokes has no force. A review criterion nobody calibrates may be worse than nothing, because its fluent output can look like warrant while accepting bad changes. The contribution of Commonplace is to treat these as system design problems rather than diligence problems.

### Where Commonplace is autonomous, and where it is not

Commonplace is not one uniformly autonomous system. Its pathways split.

Where a validator or agent reads an explicit representation of the system and acts through it, the pathway is autonomous and reflective. For example, a type specification can become a schema and validator; the validator can reject a later artifact; an agent skill can skip a search because a tag index is marked complete and that mark is enforced. The system's own represented rules alter what the system later accepts, searches, and rejects.

Where the work depends on noticing a new problem, judging a semantic criterion, or deciding whether a proposed methodology change is the right shape, the pathway remains human-inclusive. That is not a failure of the frame. It is the boundary of warranted autonomy. Commonplace could hand those gates to a model tomorrow and become more autonomous in the bare sense. We do not claim that would make it more trustworthy. Autonomy is warranted only as far as the available oracle can assess the candidate with enough confidence.

This distinction is central to the submission. We are not selling unattended epistemology. We are showing a system that makes the boundary explicit and moves it when the oracle improves.

### The epistemic stack we built

For the case-study work, the method separates three layers:

- Ingestion: capture sources, preserve provenance, and check quote grounding against snapshots.
- Structure: represent contested claims, positions, dependencies, and gaps without flattening disagreement into premature verdicts.
- Assessment: apply criteria only where there is an oracle of known shape, and record rejected machinery when no such oracle exists.

The strongest checks today are mechanical. Quote grounding can be verified against captured snapshots. Schema constraints can be validated. Type contracts can be enforced. These are the places where unattended operation is most warranted.

The weakest layer is semantic assessment. That is also where the submission is most honest. We found that a semantic review criterion could be fluent and inert: it was ruled acceptable in blind reviews even when known-positive cases should have exposed it. The important result is that the failure was caught by a labelled calibration sample, repaired in-sample, and turned into a protocol: semantic gates should not advance toward autonomy until they have known-case regressions.

That is the improvement loop in miniature. A weak evaluator was not hidden. It produced evidence of failure. The system retained the lesson as a change to the methodology: do not trust semantic gates merely because their reports sound plausible; calibrate them against labelled fixtures before giving them unattended authority.

### Why this matters for epistemology

Epistemic casework has a special version of the compounding problem. It mixes source genres, institutions, methods, claims, and incentives. The system must preserve detail without pretending that every source can be reduced to the same score. It must distinguish what was forced by the world from what was chosen by the analyst. It must keep track of correlated evidence, missing evidence, contested joints, and rejected shortcuts.

Commonplace's answer is conservative. It standardizes the connective tissue rather than the contested substance. It records provenance, structure, rationale, and checks. It refuses scalar confidence, authority ranking, or crux scoring when we do not yet have an oracle that can warrant those numbers. Rejection is part of the method: an unverifiable score in frontmatter is not discipline, it is false precision made durable.

The three casebooks are stress tests for this methodology rather than proof that every assessment problem is solved:

- COVID stresses institutional incommensurability and correlated evidence.
- LHC safety stresses dependency chains and meta-critique of the argument.
- Eggs and nutrition guidance stresses competing syntheses and institutional reversal.

The point is not that Commonplace adjudicates these controversies by itself. The point is that it gives agents a way to build, check, revise, and retain the epistemic structure without losing why the structure looks the way it does.

### What should be judged

The submission should be judged as a working self-improving methodology, not as a claim of completed epistemic automation.

Its present strengths are:

- mechanical checks where the ground truth is shared;
- explicit boundaries where judgment remains human;
- retained design rationale for why rules exist and alternatives were rejected;
- a reference implementation where accepted methodology changes can become operative;
- a calibration program for moving semantic gates toward warranted autonomy.

Its present limits are also part of the contribution:

- semantic evaluation is under construction;
- some self-improvement pathways depend on human noticing and judgment;
- rationale lineage is retained by surfaces and author discipline, not enforced end to end;
- the clean-room replication protocol for transfer is designed but not yet run;
- the classification of Commonplace as self-improving rests on observed pathways, not a blanket claim about the whole system.

The honest headline is therefore:

> Commonplace is a partially autonomous self-improving system for epistemic methodology. It is not perfect at epistemology yet, but it has the loop needed to improve itself: it can notice failures, evaluate candidate fixes, retain accepted changes in artifacts that future agents and validators actually consume, and keep humans at the gates whose oracles are not yet strong enough.

That is the field-level contribution. As AI systems get stronger, the bottleneck is not only generating more analysis. It is making sure the lessons from analysis become operative and that unattended acceptance is limited to what the system can verify. Commonplace supplies a concrete architecture for that: improve the methodology, not merely the output.

## Minimal judge-facing structure

If this becomes the main submission, the shortest credible shape is:

1. **What fails in ordinary AI epistemic work:** lessons do not become operative, so the next run repeats or drifts.
2. **The method:** a self-improving methodology with search, evaluation, and operative retention.
3. **The implementation:** Commonplace artifacts that future agents and validators actually consume.
4. **The uplift:** one case walkthrough showing load-bearing evidence, uncertainty, missing perspectives, and checks in use.
5. **The boundary:** mechanical checks are strong; semantic gates are fallible and require labelled calibration.
6. **The scaling story:** better models and more contributors widen search and scrutiny, but warranted autonomy grows only as oracles harden.
7. **The insight:** evaluator quality, not generation quality, is the binding constraint on trustworthy epistemic automation.

## Preparation checklist

The judging appendix implies the submission and repos need to be prepared for a skeptical judge who will compare against a careful Claude Code/deep-research baseline and may try to run the workflow.

### Submission revisions

- Move the self-improving-system claim to the front. The submission should open with the mechanism: epistemic methodology compounds only when lessons become operative rules that future agents and validators consume.
- Add a short criteria map. Name the seven judging dimensions and state which evidence answers each. Do not leave judges to infer that Commonplace covers compounding, transparency, scalability, and adversarial robustness.
- Include one runnable walkthrough in the main text, not only as an appendix. Best current candidate: the LHC conclusion note, because it has source snapshots, a claim chain, deterministic validation, a semantic-review WARN, a revision, and a later PASS.
- Make the uplift baseline explicit: better than a narrative deep-research answer because the artifacts are interrogable, source-linked, checkable, and reusable by later agents.
- Frame imperfections as bounded state, not apology: semantic assessment is under construction; humans stay at gates whose oracles are weak; the system improves those gates by calibration and retention.
- Cut most internal architecture from the main text. ADR lists, full review-store architecture, replication protocol details, and Commonplace internals go to appendices.
- Do not claim three completed casebooks unless the artifacts exist and are clean. If only one casebook is mature by submission time, say the other two are scaffolds / intended stress tests / future evaluation rather than completed evidence.

### Prepare Commonplace

- Keep the self-improvement notes and classification internally consistent: Commonplace is pathway-mixed, with reflective-and-autonomous pathways where validators/agents consult self-representation and human-inclusive pathways where judgment remains external.
- Ensure the submission can link to a compact Commonplace evidence bundle:
  - definition of self-improving system;
  - proposal-selection loop;
  - warranted autonomy / oracle domain;
  - Commonplace reflective-system classification;
  - design rationale management;
  - calibration proposal for semantic gates.
- Provide exact verification commands for framework claims. At minimum: `pytest`, `commonplace-validate`, and any quote-grounding / review-bundle commands that are intended to be judge-runnable.
- Make one "what to run" appendix or README that starts from a fresh clone and ends in visible PASS/FAIL output. The judges are explicitly told to run workflow submissions.
- Avoid making new machinery on the critical path. If a feature is not needed for the LHC walkthrough or the submission's core claim, record it as a future hardening step.
- Clean or explain validation noise. If type-spec warnings or source-orphan INFO remain, state which are expected and why; do not leave a judge to discover unexplained warnings.

### Prepare epistack-casebooks

Observed current state: `../epistack-casebooks` is clean. LHC has 3 source snapshots and 5 case notes; `commonplace-validate kb/lhc/notes`, `commonplace-validate kb/lhc/sources`, and `commonplace-validate kb/notes` pass. COVID and eggs currently appear to have collection scaffolds only.

Must ship:

- A top-level casebooks README for judges. It should say what exists, how to navigate, and exactly what to run.
- One polished casebook walkthrough, probably LHC:
  - open source snapshots;
  - read conclusion note;
  - follow the three-layer argument and Plaga crux;
  - run validation;
  - inspect review-run 1 WARN and review-run 2 PASS;
  - show what changed between runs.
- Commit or preserve the review traces as deliberate evidence, not incidental reports. They are the best demonstration that the methodology catches mis-grounding and confidence drift.
- Add a short "baseline comparison" note: what a normal deep-research answer would give, and what the casebook artifact adds (traceable premises, visible crux, rerunnable checks, retained method changes).
- Add a "limitations" note in the casebooks repo:
  - span-level source locator is still a workaround;
  - semantic gates are opt-in;
  - non-adjudication gate is not yet built;
  - COVID and eggs are incomplete unless finished before submission.
- If time permits, build ultra-thin COVID and eggs slices rather than broad unfinished casebooks. One source cluster + one note + one visible gap per case is enough to support "different shapes were considered" without overclaiming completion.

Nice to have:

- A small falsification demo: plant a broken quote or mis-grounded claim, show validation/review catching it, then restore the clean state.
- A non-adjudication review gate for one high-pressure note, especially COVID, but only if it can be calibrated or explicitly presented as experimental.
- A casebook package script or README command block that reproduces the validation outputs judges should see.

### Submission honesty rule

The main text should state exactly what has been run:

- LHC: worked casebook slice with clean validation and a review repair trace.
- COVID / eggs: only claim completion if the artifacts exist; otherwise present them as planned stress-test shapes or partial scaffolds.
- Semantic evaluator calibration: one caught failure and designed protocol, not a solved assessment layer.
- Generalization: bounded by worked cases and a designed clean-room replication protocol, not proven.

## Keep short

If this becomes the main submission, cut aggressively:

- Keep: self-improving methodology, partial autonomy, oracle boundary, one concrete failure caught and turned into a stronger method, three casebooks as stress tests.
- Compress: design rationale management, case walkthroughs, review-store architecture, ADR lists.
- Move to appendix: replication protocol, full machinery tables, command walkthroughs, detailed Commonplace internals.
- Avoid: claiming solved assessment, blanket autonomy, safe transfer, or generic machinery from one instance.

## Source notes to stay inside

- [Self-improving system](../notes/definitions/self-improving-system.md): self-improvement is operative change to the system's own behavior-determining organization, responsive to evidence bearing on an improvement objective.
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md): Commonplace is pathway-mixed; some pathways are reflective and autonomous, others human-inclusive.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): the loop frame is search, evaluation, retention with behavioral authority.
- [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): bare autonomy is cheap; trust follows only the oracle.
