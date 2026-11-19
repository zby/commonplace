# How documentation reaches an agent, and what should be a skill

Notes from the operator's discussion with an agent (claude-fable-5-2) on 2026-11-19. They record the operator's positions and one session's observations. They are premises for the [organisation plan](./organisation-plan.md), not adopted rules.

## One session's reading

The agent changed the review commands in that session. What it opened:

- **Read closely:** `AGENTS.md`, which the harness loads; the `kb/work/` collection contract, because `AGENTS.md` says to read it before writing there; the review section of `commands.md`; two sections of the review guide; `tests/README.md`.
- **Read as lookup:** three ADRs, by searching for one rule or copying a format.
- **Edited without reading:** about 20 instruction files, changed by pattern.
- **Never opened:** most architecture documents, `navigation.md`, `content-routing.md`, every worked-case note.

It searched first and read 20 to 80 lines around a hit. It never read a reference document from the top. It checked every consequential claim against the code. It met two rules only when a check failed: a test that requires one entry module per command, and the validator's rule against links into the proposal archive.

This is one session of one task kind, a code change. It does not test the authoring rules, which a writing task would reach through a skill, a collection contract and a type spec.

## The operator's observations

- Agents use a command's `--help`. Instructions that use a command name it, so an agent does not need a list of commands. `uv tool list` gives the list to a person.
- The operator saw an agent read the review guide. `AGENTS.md` sends an agent there for any review or revision task, so the guide is on a route, and the route loads all 61 kB.

## Three ways a document reaches a reader

1. **On a route.** `AGENTS.md`, a skill body, a collection contract or a type spec loads it, or a tool prints it: `--help`, a validator message, a failing test. This is the documentation an agent reliably uses. A rule that matters belongs here.
2. **Human overview.** It serves an operator who decides what to run. It says what a workflow does, what it may publish, what it costs and when it needs a decision. It points to help for detail.
3. **Searchable background.** A reader finds it by search or from a theory note. Worked-case notes are of this kind.

A document that reaches no reader in any of these ways is a candidate for removal.

## Skill, or link from AGENTS.md

Both cost one line that is always loaded: a skill's description in the skill list, or a pointer in `AGENTS.md`. They differ in what the line does.

- **Skill.** The reader arrives with a task it can name, such as "review this note". A procedure with an outcome follows, and an operator may want to invoke it by name. The description matches the request, and the body loads only then, with the force of instructions. Skills are projected into consuming projects.
- **Link from `AGENTS.md`.** The content is knowledge or a constraint that applies across many tasks, with no single request that triggers it: vocabulary, where content goes, git rules, test selection. The agent needs it even when it does not think it is doing that task.
- **Neither.** Background found by search, or detail a tool prints at the point of need.

A pointer in `AGENTS.md` that reads "for task X, read Y" is a skill description in the wrong place.

Two limits. Each added skill makes matching among the listed skills less reliable, so not every routed document should become one. Architecture and authoring rules have no nameable request and fail the test.

## Applied to review and editing

The review pointer in `AGENTS.md` names recognizable requests, and the work is a procedure with decisions for the operator. The proposal is two skills that mirror the command split of [ADR 139](../../reference/adr/139-only-commonplace-revise-writes-a-note.md), because the authority differs:

- `cp-skill-review`: findings only; it never writes a note.
- `cp-skill-revise`: it may write the note; it covers the quick and full procedures, stops, `apply` and `publish`.

Each body says which command fits which intent, what the command may write, what a stopped run leaves, and which existing instruction to follow in each situation. The guide then keeps only what no skill, instruction or `--help` says. `cp-skill-revise-autoreason` exists, so its description must be told apart from `cp-skill-revise`.

## The operator's positions on the reference documents

Stated on 2026-11-19, before the [analysis](./reference-analysis.md):

- The subdirectories of `kb/reference/` stay.
- Retire `commands.md`. Use `uv tool list` for the installed command catalogue. Keep the instruction local to the operation. For example, the [write skill](../../instructions/cp-skill-write/SKILL.md) tells the agent to run `commonplace-validate` on the file it just wrote.
- The review guide is renamed for the review and editing system. It may keep a general introduction that agents also use.
- Architecture documents mostly repeat ADRs. Some high-level documents may stay; this needs rethinking.
- Authoring rules are probably useful, but only if agents read them.
- The worked-case notes are mostly theory for human readers. Some may move to theory. The rest go into a new directory.
- Plans, briefs other than a note's write brief, and records are removed.

The agent's two reservations: an ADR records a decision at its date, so something must hold the current state that several ADRs compose; and the session above does not test the authoring rules.
