---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OpenKB workflow account: CLI deck generation from retained wiki content, optional visual critique and delivery checks."
run-id: AAS-2026-11-09-openkb-bd9c4c38a842-01
reviewed-boundary: "ff54396e575ee6feb0113b631a34caa082b441cc"
---

# OpenKB workflow report

## Workflow account

### Selected workflow and evidence

This account traces `openkb deck new <name> <intent> --critique` with the bundled default `openkb-deck-neon` producer. This is representative because it joins retained knowledge consumption, model-directed artifact production, a separate critic and code-owned delivery checks in one shipped path. It is not a model team that delegates its own work: Python fixes the producer/critic order; each model selects reads and writes inside its own SDK run. The baseline route is [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce); installed instruction authority is [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions).

Evidence is SRC-1 implementation and doctrine/design at the revision in [boundary](boundary.md). Added inspection within that pin covers the complete deck creator and skill runner, the bundled producer/critic bodies, deck path helpers, `Generator.run`, CLI `deck_new` and `_save_deck_iteration`, and validator checks. These are source-level mechanisms, not an observed deck-making run. No target, tests, examples, providers or browser were executed. Actual source selection, compliance, content preservation and visual benefit remain unobserved.

### 1. User request to driver admission

The CLI principal supplies a slug, natural-language brief, optional skill choice and critique flag. `deck_new` finds the KB and invokes shared name/wiki-content preflight. It verifies credentials and resolves configuration before removing any previous deck. On an existing output directory, noninteractive invocation must preauthorize overwrite with `-y`; interactive refusal aborts. Accepted replacement first copies the old directory into a numbered workspace iteration, then deletes the active directory. This is operator-controlled replacement with a retained copy, not per-slide human approval or automatic restoration after failure. SRC-1, `openkb/cli.py`, `openkb/deck/__init__.py`; [WF-CLM-cli-delivery](#wf-clm-cli-delivery).

The driver constructs `Generator(target_type="deck", ...)`. `Generator.run` calls `run_deck_create`, carries the producer validation result upward and returns the conventional output directory. This wrapper does not rerun validation after critique. SRC-1, `openkb/skill/generator.py`:

> self.validation = deck_result.validation
> return self.output_dir
> --- `openkb/skill/generator.py`

### 2. Driver to producer: explicit inputs, model-directed work

`run_deck_create` creates the conventional deck directory and calls `run_skill` with skill name, brief, KB root, model, slug and optional credential bundle. The producer cap is 120 turns when critique is requested, otherwise 80; the later critic gets its own 40-turn cap. These are separate budgets, not 120 turns shared across both agents. SRC-1, `openkb/deck/creator.py`, `openkb/agent/skill_runner.py`.

The runner discovers the named installed skill, parses its frontmatter and body, templates its output destination and prepends that destination to the intent. It clones the base query agent, appending the full skill body and intent to instructions. Grants are wiki reads plus constrained file writing and output/skill reads. The base schema remains instruction context; it is not replaced by the producer skill. The SDK starts from a short user seed, not from a previous chat history. Models can reread external files through tools, but the producer has no enclosing foreground conversation supplied by this path. See [RT-OBJ-agents-md](runtime.md#rt-obj-agents-md), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions).

The bundled skill asks the model to survey the wiki, choose a narrative, read relevant concepts and document slices, outline slide types, write the full HTML file and self-check it. Those are requested decisions, not a Python-enforced sequence of substeps. Its first handoff to knowledge reads is explicit. SRC-1, `skills/openkb-deck-neon/SKILL.md`:

> 1. **Survey first.** Use wiki-read tools to list `concepts/` and `summaries/`
>    and read `wiki/index.md`. Build a mental map before deciding the argument.
> --- `skills/openkb-deck-neon/SKILL.md`

The default metadata selects `output/decks/{slug}/index.html`, deck mode and a grammar of slide kinds. The model proposes artifact contents; the shared write helper admits writes by destination, without a human approval step. Its scope includes output and explorations, not an OS sandbox or a tool-level limitation to one deck file. See [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce) and [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) for the checked writer and its limits.

### 3. Producer completion to structural checks

After the SDK returns, the runner rejects a missing templated output file with a `RuntimeError`. For a deck-mode skill with a resolved output path it invokes `validate_deck`; the default producer meets those metadata conditions. The validator parses HTML and checks slide count, detected external references and declared grammar. Grammar violations such as missing required kinds become errors; insufficient variety and excessive same-kind runs become warnings. These are structural tests, not an answer-reference oracle or proof of factual fidelity, rendering or keyboard behavior. SRC-1, `openkb/agent/skill_runner.py`, `openkb/deck/validator.py`.

> Returns a :class:`ValidationResult` with categorised issues. Never
> raises for structural failures — those become entries in ``errors``.
> --- `openkb/deck/validator.py`

The runner stores that result and returns. It does not branch on structural error entries. Consequently critique can still run on a deck whose producer validation recorded errors. A custom skill without the relevant metadata can avoid these hooks; neither a skill name nor a model's claim of completion substitutes for the implemented conditions. [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce).

### 4. Artifact to critic: isolated context, shared effects

With critique enabled, Python calls the fixed `openkb-html-critic` skill in a fresh run. The handoff supplies the produced target path and original brief with an instruction not to change content. It does not supply producer reasoning, tool history or validation diagnostics. The critic reads the artifact through its file tool; the shared filesystem, not conversation inheritance, carries the work product across. It can write patches through the same scoped helper. SRC-1, `openkb/deck/creator.py`, `openkb/agent/skill_runner.py`.

> critic_intent = (
>     f"Critique and patch the HTML deck at: {target_path}\n"
>     f"Original user brief (for context, do NOT change content):\n{intent}"
> )
> --- `openkb/deck/creator.py`

The critic instructions ask for CSS specificity, navigation, slide structure and self-containment checks, a full-file atomic replacement and a short change report. They constrain it to visual repair, not factual correction. The same text also asks for conservative trimming of very long lists or slide bodies, creating instruction-level tension with its hard no-content-change rule. That tension prevents treating the prompt as an unambiguous content-preservation contract; no supplied execution resolves how a model follows it. SRC-1, `skills/openkb-html-critic/SKILL.md`:

> - **Bullet dump**: any slide with **more than 8 list items** in a single
>   list. Cut to the 5 strongest.
> --- `skills/openkb-html-critic/SKILL.md`

> The slide text, dollar figures, named products, quotes, attributions —
> all of that is the **original author's** work. You are a visual
> critic, not a content editor. Touch CSS, JS, and structural HTML; do
> NOT rewrite slide bodies.
> --- `skills/openkb-html-critic/SKILL.md`

This separation resembles a temporary task frame: selected inputs enter, private working history stays out of the caller, and the frame ends. But file mutations escape independently of the returned value. The wrapper ignores the critic result and returns the producer result; the critic's requested explanatory message is not the CLI delivery artifact. There is no iterative producer revision based on a returned critique in this wrapper. SRC-1, `openkb/deck/creator.py`, `openkb/agent/skill_runner.py`.

### 5. Rejection, recovery and delivered result

The CLI surfaces validation warnings and errors after the wrapper returns. Error entries cause exit status 1 while leaving the deck on disk; without errors it prints the output path. Thus file retention, successful command delivery and validated final bytes are different conclusions. In particular, the reported validation describes the pre-critic artifact: the wrapper never reruns the validator after critic writes. [WF-CLM-cli-delivery](#wf-clm-cli-delivery), [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce).

Failure ownership is code/ operator-specific. Missing producer skill becomes an installation-oriented `RuntimeError`. Turn-cap exhaustion becomes a `RuntimeError` recommending a narrower intent; the CLI reports runtime errors and exits. Missing critic alone is caught and tolerated, so the original deck remains usable. Other critic exceptions are not converted into that soft success by the wrapper. The inspected path does not automatically restore a prior iteration or undo partial model writes on failure. An operator can inspect retained files and rerun; the saved iteration supplies a prior copy, not a demonstrated recovery execution. SRC-1, `openkb/deck/creator.py`, `openkb/agent/skill_runner.py`, `openkb/cli.py`; [WF-CLM-cli-delivery](#wf-clm-cli-delivery).

The shipped workflow therefore establishes a bounded producer/check/optional-patch pipeline. It establishes neither semantic acceptance by an independent judge nor observed improvement from the second pass. Its endpoint is a retained HTML work product and CLI status, not installation of a revised producer method.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

#### WF-CLM-cli-delivery
Label: CLI deck delivery and replacement contract

Claimed operation: `deck_new` protects an old deck from key/config preflight failure, snapshots authorized replacement, reports structural validation errors as a failed command while retaining files, and otherwise announces the conventional deck path. Evidence is implementation in SRC-1, `openkb/cli.py`. Distinct identity: this claim concerns the outer CLI's overwrite and terminal-status contract; the closest supplied record, [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce), describes the inner producer/critic route and returned `SkillRunResult`. It is not a second declaration of that route. Implementation conclusion status: wired; operation conclusion status: uninspected. No automatic failure restoration is established by the inspected driver.

> if yes_flag:
>     _save_deck_iteration(kb_dir, name)
>     shutil.rmtree(target)
> --- `openkb/cli.py`

> if gen.validation.errors:
>     click.echo(
>         f"Deck written to {gen.output_dir / 'index.html'} but failed validation. "
>         f"Inspect and re-run.",
>         err=True,
>     )
>     ctx.exit(1)
> --- `openkb/cli.py`

> click.echo(f"Deck written to {gen.output_dir / 'index.html'}")
> --- `openkb/cli.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce)

Workflow-specific handoff: the CLI authorizes replacement before starting the producer; Python passes the artifact path and original brief, but not validation diagnostics or producer history, to the optional critic. Verification and delivery are temporally separated: the producer validation object reaches the CLI only after the critic can modify the file. Missing critic is a soft failure; structural errors produce a nonzero CLI result without deleting the artifact. The consumer-facing status extension is [WF-CLM-cli-delivery](#wf-clm-cli-delivery). These are implementation findings, not observed successful delivery or critic benefit.
