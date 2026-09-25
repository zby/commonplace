# Writing conventions for kb/instructions/

These defaults are ready to use. Customize them only when the project needs
different conventions; no sections require filling in. Use the project's
declared KB goals and scope to decide which subjects belong here. Do not invent
project requirements to customize this file.

Once installed, this contract belongs to your project. Commonplace does not
synchronize it with later template changes.

## Purpose and scope

This collection contains project-specific procedures, operational rules, and
how-to guidance for people and agents. Skills may live here as directories
containing `SKILL.md`. The shipped Commonplace procedures live in the installed
Commonplace library, whose location `.commonplace/library.md` gives; do not
copy them here merely to populate this collection. It may remain empty until the project needs its own instructions.

Put explanations and general claims in `kb/notes/`, descriptions of project
state and decisions in `kb/reference/`, and unfinished plans in `kb/work/`.

## Quality goal

An instruction is worth keeping when it helps an intended operator perform
a task correctly without reconstructing the procedure from other material.
Make the trigger, required inputs, intended result, and completion check clear.
Use established project requirements; do not invent permissions, policies,
tools, or acceptance criteria to make a procedure look complete. Identify
missing information and state when it must be resolved before proceeding.

## Title and body conventions

- Use an imperative title naming the task, such as "Review a draft" or
  "Record a source".
- Begin with what the procedure accomplishes and when to use it.
- State prerequisites and inputs, then give steps in execution order. Make
  consequential branches explicit and say how to check the result.
- Include the context needed to execute the steps without the original
  conversation. Keep explanations brief; link to longer rationale separately.
- When frontmatter includes a `description`, state when to use the instruction.

## Outbound links

Keep the main procedure understandable from its own text. Link to another
procedure when it must be executed, to reference when specific facts are
needed, and to notes for optional rationale. State at the link whether reading
or executing the target is required and under what condition.

Link when following the target helps a reader understand, verify, or use the
artifact. Put supporting links inline where they matter. Optional footer links
use `- [title](path) — label: specific reason to follow the link`. Do not add
links merely to fill a footer or create a reciprocal link.

Use these destinations and labels for connection discovery and authored links:

| Destination | When to search or link | Authorized labels and meanings |
|---|---|---|
| `kb/instructions/` | Find an existing prerequisite or procedure needed by a step. | `precondition`: identifies work that must already be done; `invokes`: identifies a procedure to execute; `see-also`: offers optional related guidance. |
| `kb/reference/` | Find the subject's contract, interface, or definition needed for execution. | `operates-on`: describes what the procedure acts on; `defined-in`: explains a term; `see-also`: gives relevant reference detail. |
| `kb/notes/` | Find rationale needed to understand or maintain the procedure. | `rests-on`: identifies a claim the procedure depends on; `see-also`: offers optional explanation. |
| `kb/sources/`, `kb/reports/retained/` | Find evidence for a procedural requirement. | `evidenced-by`: supports or qualifies the requirement; `see-also`: gives relevant context. |
| `external` | Cite identified official guidance or evidence. | `invokes`: identifies a procedure to execute; `evidenced-by`: supports a requirement; `see-also`: offers related guidance. |

Use relative Markdown links for local targets. Link only to existing artifacts.
Do not link to temporary work, ignored snapshots, report caches, or local
report state. Connection discovery does not search the open web; `external`
authorizes links to already identified targets.

## Type eligibility

A typed artifact in this collection may use a global Commonplace type, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path. Frontmatter-free Markdown is implicit `text`.
