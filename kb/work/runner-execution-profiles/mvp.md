# MVP: two execution profiles resolved by the runner

Status: brainstorm, not adopted.

## Candidate system

Start with two execution profiles:

- `main` — the orchestrator's model and effort, or a configured equivalent suitable for load-bearing judgment;
- `fast` — a configured cheaper/faster model and effort for bounded or easily verified work.

These are portable execution profiles, not concrete model names. Project configuration in `AGENTS.md` maps them onto each runner:

```yaml
agent_profiles:
  main:
    codex:
      model: inherit
      effort: inherit
    claude:
      model: opus
      effort: inherit

  fast:
    codex:
      model: <configured-codex-model>
      effort: low
    claude:
      model: sonnet
      effort: inherit

  fallback: main
```

The concrete syntax and mappings remain open. The invariant is the separation: instructions request a portable profile; the project's runner configuration decides what that profile means.

If a field is missing, malformed, or unsupported, execution defaults to `main`. A runner must not silently claim it used `fast` when it actually inherited the main model.

## Instruction declaration

Each instruction declares the minimum profile required for trustworthy execution:

```yaml
complexity: fast
```

or:

```yaml
complexity: main
```

`complexity` is not a measure of how intellectually interesting a task is. It is the minimum execution profile the procedure may use without weakening its result beyond the procedure's contract.

Candidate classification rule:

- `fast` — bounded inputs, narrow scope, constrained output, cheap failure, deterministic verification, or advisory output subsequently judged by `main`;
- `main` — semantic judgment, synthesis, adversarial reasoning, broad discovery, load-bearing mutation, accepted verdicts, or work whose false negatives are difficult to detect.

The eventual validator may require the field everywhere, but runtime resolution should continue treating absence as `main` for safety and compatibility with locally authored instructions.

## Composite instructions and role overrides

One frontmatter value cannot describe a heterogeneous procedure such as the full pass. Frontmatter should be the instruction default; each spawn site that differs declares an explicit override:

```markdown
Launch the copyeditor with:

- complexity: fast
- context: clean
```

The worker brief can carry a standard header:

```text
Execution profile: fast
Task: Revise for flow and readability...
```

This is execution metadata for the orchestrator. It is not proof that the requested model actually ran; observed provenance remains separate.

Generated work such as review jobs may eventually carry the same profile in the job object or prompt metadata. For the MVP, judgment-bearing generated review jobs remain `main`.

## Dispatch procedure

Before every sub-agent spawn, the orchestrator:

1. identifies the governing instruction and reads its `complexity`;
2. applies an explicit role override when the spawn site supplies one;
3. resolves `main` or `fast` through the current runner's `AGENTS.md` mapping;
4. checks whether the harness can honor the requested model, effort, context, and isolation;
5. if it cannot, follows the configured fallback—initially `main`—and reports the exception;
6. spawns the worker through the authorized harness mechanism; and
7. records or reports the actual runner, model, and effort when available.

Candidate fallback policy:

```yaml
fast_unavailable: use_main_and_report
```

No MVP path launches a nested `codex` or `claude` CLI merely to obtain a configured model when the harness does not expose an authorized worker selection surface.

## Conservative full-pass pilot

| Full-pass role | Initial profile | Reason |
|---|---|---|
| Compression report | `fast` | Structured criteria, advisory report, main synthesis downstream |
| Critique | `main` | Adversarial semantic judgment |
| Composition friction | `main` | Concretization and inferential-joint analysis |
| Semantic review | `main` | Accepted verdict evidence and difficult false negatives |
| Connect | `main` initially | Broad discovery plus relationship judgment remain combined |
| Editorial synthesis | `main` | Resolves disagreements and selects substantive edits |
| Applying substantive edits | `main` | Load-bearing mutation |
| Final flow copyedit | `fast` | Narrow prompt, semantic change forbidden, final diff inspectable |
| Report formatting and bookkeeping | `fast` | Mechanical, constrained, and verifiable |
| Closing semantic and critique reruns | Same as initial assay | Preserve comparison and review-partition honesty |
| Experimental controls | Same as compared assay | Avoid confounding model routing with the control |

Connect may later split into fast candidate generation plus main selection, but moving the combined procedure to `fast` is not part of the initial pilot.

## Relationship to skill model fields

Copy the skill convention's placement of execution policy in frontmatter, not its exact semantics.

Current skills may declare runner-facing fields such as:

```yaml
model: sonnet
context: fork
```

The Commonplace-portable source declaration would be:

```yaml
complexity: fast
```

In a later design, installation or runner projection could materialize runner-native fields from the project mapping:

```text
canonical complexity: fast
        -> Claude projection: model: sonnet
        -> Codex projection: configured model + effort
```

That projection is outside the first MVP. Initially:

- use `complexity` for instructions and explicit sub-agent dispatch;
- leave existing skill `model:` behavior intact;
- catalogue how each skill's current model corresponds to `main` or `fast`;
- do not claim cross-runner skill configuration until both projections are verified.

## Minimum implementation and evidence

The MVP would consist of:

1. an `Agent execution profiles` block in `AGENTS.md` defining `main`, `fast`, and fallback per runner;
2. `complexity: main|fast` in the instruction type contract, with absent-at-runtime meaning `main`;
3. a control-plane rule requiring profile resolution before every sub-agent dispatch;
4. a standard inline role override for composite instructions;
5. annotations for active delegation targets, not an immediate blind rewrite of every historical instruction;
6. the conservative full-pass pilot above; and
7. a run record containing requested profile, resolved configuration, actual runner/model/effort, fallback, latency, and whether main-agent review rejected or materially changed fast-agent output.

The pilot should answer:

- Did the harness honor the requested profile?
- How much latency and cost changed?
- Did fast output pass deterministic checks?
- Did main synthesis reject, substantially change, or escalate it?
- Did routing change any accepted review identity or invalidate a controlled comparison?

Only after those observations should the workshop decide whether to add escalation cascades, additional profiles, generated runner projections, or configuration outside `AGENTS.md`.
