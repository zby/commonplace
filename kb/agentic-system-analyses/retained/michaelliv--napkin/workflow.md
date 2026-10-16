---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Napkin's session-to-vault distill workflow: agent selection, CLI writes, post-write link checks and user delivery."
run-id: AAS-2026-10-12-napkin-2b85bef38252-01
reviewed-boundary: "7582d6a46f5a11995956e60a59c41a5b242109f1"
---

# Napkin workflow report

## Workflow account

The representative workflow is **distilling a working session into retained vault notes**. It was selected because one shipped skill connects the retention request, content selection, existing-note inspection, mutation, verification and final report. This is an instruction-grounded agent workflow with code-grounded command effects, not an observed execution. Its parent route is [RT-RTE-distill-session](runtime.md#rt-rte-distill-session); its executor is [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation). The external host supplies the session, loads the skill and runs the model. Napkin does not itself schedule this procedure or orchestrate worker agents. Automatic hook/timer invocation is contemplated by the instruction, not demonstrated by the frozen repository (SRC-1, `skills/distill/SKILL.md`; [boundary](boundary.md)).

### Request, selection and placement

A user can request retention; an automatic invocation has a stricter skip preference. The same external agent proposes and decides topic clusters. It can veto all writes and deliver “nothing worth distilling.” A user starting the workflow is not per-note human approval. The skill provides KEEP/SKIP criteria and a three-month usefulness test, not a reference-answer oracle. Session content is supplied as data under an explicit instruction trust boundary; actual host/model compliance is unobserved ([RT-RTE-distill-session](runtime.md#rt-rte-distill-session); SRC-1, `skills/distill/SKILL.md`).

> **SKIP** (say "nothing worth distilling" and stop) if all are true: the session
> was pure Q&A/planning/explanation, nothing surprising happened, and everything
> discussed is obvious from the docs.
> --- `skills/distill/SKILL.md`

The agent groups by topic rather than chronology, keeps conclusions and their reasons, and drops inconclusive exploration and already-retained content. It delegates orientation and duplicate discovery to `napkin overview --json` and a topic search limited to five hits. The returned folder map and search hits guide placement; `_about.md` is the designated folder-intent surface. A same-subject hit leads to merge; no hit leads to create. Because this decision uses a bounded search result interpreted by the model, no hit does not prove that the vault contains no overlapping note. Napkin returns evidence and paths; the model owns the next action ([RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval); SRC-1, `skills/distill/SKILL.md`).

### Writes and their consequential handoffs

For a merge, the agent reads the existing note and integrates new information into its sections. The instruction requests explicit treatment of contradictions rather than silently retaining both statements. Small additions use append/property operations; restructuring uses whole-file overwrite. The model decides content and target, and the CLI/SDK performs filesystem mutation. There is no separate reviewing agent or semantic acceptance callback in this traced write chain. The core's existing-file rejection is an I/O guard, not verification that a proposed claim is warranted ([RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation); SRC-1, `skills/distill/SKILL.md`, `src/core/crud.ts`, `src/commands/crud.ts`).

> Integrate — don't append a dated "update" section to the bottom. Fold new
> information into the sections where it belongs. If the new finding contradicts
> the note, say so in the note explicitly rather than silently keeping both.
> --- `skills/distill/SKILL.md`

For a new note, the agent is directed to inspect templates and use a match, otherwise create a declarative note with tags, summary, context and details. The template branch has two delivery limits. First, the skill's example treats `--path "<folder>"` as folder placement, but the executable treats `--path` as the complete file path and adds `.md` when absent; the positional title is not combined with it. Second, selecting a template replaces supplied content with template bytes in `createFile`. Thus executing that example literally does not establish a titled, distilled note within the selected folder, nor populated knowledge. The skill does not specify a separate template-population command sequence. A successful create status alone cannot close those gaps (SRC-1, `skills/distill/SKILL.md`, `src/main.ts`, `src/core/crud.ts`; workflow-specific details in the mutation annotation below). These are inspectable instruction/executor mismatches, not observed failed runs.

For both branches, writing guidance requires declarative knowledge, an inference marker for generalizations and links to existing notes. The model supplies those judgments; the core neither checks the inference marker nor reconstructs the session's evidential warrant. Whole overwrite persists the new bytes without a separate archive or transaction in the inspected function ([RT-RTE-distill-session](runtime.md#rt-rte-distill-session), [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation); SRC-1, `skills/distill/SKILL.md`, `src/core/crud.ts`).

### Verification, rejection and recovery

Verification occurs **after** writes. The agent invokes `napkin link unresolved --json`, interprets unresolved targets and is told to correct typos or drop links. The symbolic diagnostic does not accept/reject note content, stage writes or roll them back. It checks recognized wikilink targets across the vault, using loose basename resolution; it strips heading fragments before lookup. Consequently an empty result does not prove that a link names the intended duplicate note or a valid heading, much less that the knowledge is correct. Default JSON returns target names without source-file provenance; verbose mode can return that provenance, though the skill does not request it. The agent must locate and repair its affected links rather than treat every pre-existing unresolved link as its own new failure (SRC-1, `skills/distill/SKILL.md`, `src/core/links.ts`, `src/utils/files.ts`, `src/utils/markdown.ts`, `src/commands/links.ts`; [WF-RTE-distill-verification](#wf-rte-distill-verification)).

A concrete executable rejection path is create against an existing target without overwrite: core throws, and the CLI prints the error and exits with a user-error status. The instruction separately permits overwrite for integrated rewrites; it does not prescribe a retry/backoff or rollback sequence after unexpected write errors. Recovery belongs to the caller, not an internal supervisor. Link repair likewise belongs to that same agent after persisted edits. These paths establish rejection and requested repair, not successful recovery in a run ([RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation); SRC-1, `src/core/crud.ts`, `src/commands/crud.ts`, `skills/distill/SKILL.md`).

### Delivered result and later consumption

The intended successful terminal state is retained notes, repaired links, and a user-facing line for each new or merged note. If the session changes the project's fundamental architecture or direction, the instruction also requests a `NAPKIN.md` update under roughly 200 words. There is no additional human sign-off step or automated semantic read-back before the final report. The skill calls `NAPKIN.md` always-loaded, but automatic host injection remains outside the inspected implementation. Later CLI reads can consume the retained bytes; actual model reliance and usefulness remain unobserved ([RT-RTE-distill-session](runtime.md#rt-rte-distill-session), [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval); SRC-1, `skills/distill/SKILL.md`).

> Tell the user what was written, one line per note:
> --- `skills/distill/SKILL.md`

Added source coverage in this member is the complete distill skill, core CRUD and CRUD wrappers, complete core link index, and bounded CLI registration, SDK link delegation, unresolved-output, link-extraction and basename-resolver ranges. These supply doctrine/design and implementation only. No target, tests, examples, model calls or benchmark was executed. No execution trace is supplied. The selected workflow does not join benchmark ingestion to distill: the benchmark disables skills and constitutes a different caller path ([RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer); SRC-1, `bench/longmemeval-eval.ts`).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-distill-verification
Label: Distill post-write verification

Part of: [RT-RTE-distill-session](runtime.md#rt-rte-distill-session)

This part isolates the post-write diagnostic and repair handoff, whose symbolic check differs from the parent route's model-dependent knowledge admission. After mutation, the external agent requests a vault-wide unresolved-link diagnostic. The CLI constructs Napkin, the SDK delegates to the link index, and the CLI returns unresolved targets. The model interprets the result and owns typo correction or dropping links. It proposes and decides repairs without a prescribed per-link human veto or answer oracle. Operating mode is open session retention, not a bounded experiment. Guidance is the skill's requirement that newly written wikilinks resolve; the diagnostic is a filename-resolution check, not a correctness oracle. Repairs persist through the ordinary mutation executor [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation). There is no rollback gate in this diagnostic; the skill specifies repair rather than rejection of the whole note. Evidence: SRC-1, `skills/distill/SKILL.md`, `src/main.ts`, `src/sdk.ts`, `src/commands/links.ts`, `src/core/links.ts`, `src/utils/files.ts`, `src/utils/markdown.ts`.

- implementation conclusion status: wired
- instruction conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Default JSON object containing unresolved target names; verbose mode maps targets to referring files.
- Later read-back: The diagnostic reads notes already persisted by preceding commands; requested repairs become available to later retrieval invocations, without observed later consumption.
- Delegated visibility: Diagnostic stdout reaches the calling agent; the user later receives the skill's requested report, not necessarily the diagnostic output.
- Selection predicate: Listed Markdown files are scanned for recognized wikilinks; heading fragments are stripped and targets are resolved by exact path or loose basename rules. Missing targets enter the unresolved map.
- Invalidation or expiry: The index is rebuilt from current files on invocation; no diagnostic issue queue or stored acceptance certificate is established by this path.
- Activation or effect: Diagnostic computation and serialization are wired; agent-performed correction is requested, not observed. No note mutation occurs in the link-index function itself.
- Evidence limits: No run establishes repairs or correctness. Loose resolution can accept a duplicate basename; stripped heading references are not validated. The index checks wikilinks for unresolved targets, not every outgoing Markdown link or retained claim.

> Fix broken links (typo, or drop the link). If the session changed what this
> project fundamentally *is* — new architecture, changed direction — update
> `NAPKIN.md` (the always-loaded context note), keeping it under ~200 words.
> --- `skills/distill/SKILL.md`

> for (const target of links.wikilinks) {
>       const resolved = resolve(target);
>       if (resolved) append(incoming, resolved, file);
>       else append(unresolved, target, file);
>     }
> --- `src/core/links.ts`

> // Strip heading/block refs
>     const clean = target.split("#")[0].trim();
> --- `src/utils/markdown.ts`

> return { unresolved: entries.map(([k]) => k) };
> --- `src/commands/links.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation)

Workflow-specific invocation limit: the distill create example supplies a folder as `--path`, whereas the CLI describes a file path and the core prioritizes it over the name. A literal folder value becomes a Markdown filename, not a directory plus the title. Template selection supplies the template's bytes; a subsequent agent edit would be needed to populate knowledge, but that handoff is not explicitly sequenced in the skill. The immediate create result therefore certifies filesystem completion, not compliance with the intended note shape (SRC-1, `skills/distill/SKILL.md`, `src/main.ts`, `src/core/crud.ts`).

> napkin create "<Title>" --path "<folder>" --template "<Template>"
> --- `skills/distill/SKILL.md`

> .option("--path <path>", "File path from vault root")
> --- `src/main.ts`

> if (opts.path) {
>     targetPath = opts.path.endsWith(".md") ? opts.path : `${opts.path}.md`;
>   } else {
>     const name = opts.name || "Untitled";
>     targetPath = `${name}.md`;
>   }
> --- `src/core/crud.ts`

> if (templateRef) {
>       content = fs.readFileSync(path.join(v.contentPath, templateRef), "utf-8");
> --- `src/core/crud.ts`

The existing-target guard's failure reaches the caller through the create wrapper's error/exit branch. Recovery is not an automatic step of that command (SRC-1, `src/commands/crud.ts`; the core guard passage is retained in the annotated record).

> } catch (e: unknown) {
>     error((e as Error).message);
>     process.exit(EXIT_USER_ERROR);
>   }
> --- `src/commands/crud.ts`
