---
description: "Use before running an exploratory or comparative experiment in Commonplace when repository instructions, collections, prompts, or prior work may influence the result"
type: kb/types/instruction.md
---

# Design experiments in Commonplace

Use these guardrails when designing experiments inside the Commonplace repository. They prevent ambient instructions and existing artifacts from silently answering the question under study.

This is not a complete experimental protocol. The experimenter still chooses the question, cases, comparisons, measurements, replication, and decision rule. Exploratory work may change those choices as it learns; record the changes rather than forcing an early hypothesis or presenting post-hoc choices as pre-registered.

## Treat context as part of the apparatus

An agent receives more than the files named in its task. Before a run, inventory the context that could bear on the result:

- system and developer instructions;
- root and scoped `AGENTS.md` files;
- available skill names and descriptions;
- inherited conversation turns;
- the task prompt and any supplied packet;
- the working directory, visible paths, and files read with tools;
- prior results or working files present in the repository;
- requested and actual model/runtime settings.

Snapshot or hash the material context with the run. In particular, root [`AGENTS.md`](../../../AGENTS.md) is supplied independently of ordinary file reads and may contain both general governance and concepts specific to the subject under study.

`fork_turns: "none"` removes inherited conversation turns. It does not remove system or developer instructions, `AGENTS.md`, tool descriptions, or the skill catalogue.

## State isolation literally

A prompt prohibition is not an access prohibition. "Do not read X" constrains agent behavior; only a filesystem or tool boundary prevents the read. When technical isolation is unavailable:

- make the allowed and disallowed context explicit;
- inspect the execution trace for actual reads;
- report deviations rather than silently retaining them;
- describe the run as instruction-isolated or trace-audited, not technically isolated.

Avoid bare claims that a run was "blind" or that an agent "saw only" listed inputs. Name exactly what was withheld, how it was withheld, and what ambient context remained.

## Avoid testing the supplied answer

Loading an existing collection contract, instruction, rubric, or answer-bearing example can turn an intended investigation into a conformance check. That is valid when conformance is the question. It is circular evidence for whether the supplied rule captures something deeper.

Keep discovery or observation separate from mapping to current policy when that distinction matters. Freeze the observation before exposing the policy, or make policy exposure an explicit treatment. Score the result against evidence independent of the treatment whenever the experiment claims more than instruction-following.

## Keep judgment axes separate

A single-choice taxonomy is interpretable only when its options answer the same question and are mutually exclusive at that level. Do not put these into one outcome list:

- semantic relation — what the source asserts about the target;
- representation — whether that relationship deserves a formal edge, connective prose, or no link;
- epistemic state — whether the supplied evidence is sufficient to judge either question.

A relationship may have a semantic class while remaining too weak or local for mechanical registration, and insufficient evidence does not imply a semantic class. Record these as separate fields and aggregate them separately. If a decision depends on a conjunction such as “premise relation that earns a footer edge,” report both component results before applying the combined gate.

When a run claims that participants can recognize or reject a semantic class, include known positive examples and close negative examples. Negative controls alone detect indiscriminate overcalling; they cannot detect systematic undercalling. Treat constructed controls as calibration of the supplied definition, not independent evidence that the class occurs naturally in the corpus.

For an observation-then-mapping pipeline, calibrate the mapping on known cases and compare it with a matched direct-classification arm when information loss could explain the result. A failed staged classification supports a semantic conclusion only after the apparatus demonstrates that it can recover clear positives.

## Use test collections for alternative contracts

When a collection contract is the variable under study, create temporary test collections with their own `COLLECTION.md` files. Test collections let agents operate through Commonplace's normal write path while receiving an alternative local contract.

Across comparison collections:

- use neutral arm names that do not disclose the intended interpretation;
- keep artifacts and non-treatment instructions equivalent;
- vary only the contract feature being tested;
- keep the arm mapping outside participant context;
- prevent or audit reads across arms and into production collections.

Some contract changes necessarily bundle several elements, such as identifiers, definitions, token count, and instructional complexity. When those elements cannot be varied separately, name the complete treatment bundle, retain the exact cross-arm contract diff, and attribute the result to the bundle rather than one element within it.

Repository-level instructions still remain visible. Their influence is not removed, but it is held constant across arms. A test collection is an experimental fixture, not production authorization; no experimental result changes a live collection until separately reviewed and adopted.

## Consider a separate CLI for instruction variants

To vary `AGENTS.md` itself rather than a collection contract, an experimenter can copy the fixture outside the Commonplace repository, give that root the experimental instruction file, and invoke a fresh CLI process there. Current Codex supports non-interactive runs with a positional prompt:

```bash
codex exec --ephemeral --sandbox read-only --skip-git-repo-check -C <fixture-root> "<prompt>"
```

In Codex, `-p` selects a configuration profile; it is not the prompt flag. A separately launched Claude CLI can serve the same purpose, but verify the installed command and flags rather than assuming parity.

This is an optional sensitivity check, not the default design. A separate CLI can change system instructions, tools, configuration, global instruction files, model selection, and trace format alongside the project-level instruction. Comparing Codex with Claude is therefore a cross-harness comparison, not a clean `AGENTS.md` ablation. Prefer one CLI with matched settings across instruction variants, record the exact command and remaining ambient context, and accept the extra machinery only when instruction-file isolation matters to the claim.

## Check for indirect leakage

The answer may be exposed without opening the obvious file. Inspect cases and prompts for:

- existing labels, verdicts, or annotations in artifact bodies and footers;
- suggestive filenames, paths, arm names, and cohort identifiers;
- category definitions that already encode the proposed distinction;
- prior results, adjudication packets, manifests, and git history;
- collection descriptions or skill summaries that paraphrase the answer;
- outputs from another participant or arm.

Not every exposure is contamination. Some are the treatment or necessary operating context. Classify each exposure before the run and report unexpected ones afterward.

## Protect independence and reproducibility

When outputs are meant to be independent, use fresh contexts and do not expose participants to one another's answers. Record enough provenance to distinguish genuine replication from repeated work inside one contaminated context.

Declare the experimental unit and intended scope of replication. Fresh contexts over the same case and model estimate run stability, not generalization across cases or models; broader claims require variation at the corresponding level.

Before scored execution, freeze or version:

- the prompt and supplied inputs;
- assignment or randomization decisions;
- scoring and exclusion rules;
- the point at which exploration ends and confirmatory scoring begins.

Reuse a prior decision threshold only when the scored event still has the prior event's meaning. A threshold proposed for “design dependence rather than theoretical dependence” does not automatically govern a broader outcome such as “any non-target class or instability.” A broadened event may receive its own pre-registered gate, but report it as a new operational decision rather than literal confirmation of the older reversal condition.

Retain raw outputs, actual model provenance, execution traces, exclusions, and any mid-run amendments. Do not rewrite a protocol after seeing results without preserving the version that governed the run.

## Bound the conclusion

Report:

- what question was actually run, including whether it remained exploratory;
- what information each participant received by design;
- what ambient context remained and what isolation was technically enforced;
- what unplanned reads or leaks occurred;
- what was observed and what interpretation was added afterward;
- which broader claims the run does not support.

Repository-native context does not automatically disqualify an experiment. It narrows the result to behavior under that context. Likewise, agreement with an existing contract may be useful operational evidence while remaining weak evidence for the contract's underlying theory.

An experiment report is complete when another reader can distinguish the intended treatment from ambient Commonplace context, reproduce the supplied inputs, audit unexpected exposure, and tell which conclusions follow from the run rather than from the repository's existing rules.
