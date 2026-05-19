# Connect generalization for installed KBs

## Question

How should `cp-skill-connect` become a general installed-KB tool without losing the useful discipline it already has in this repository?

The current skill works well here because this repository's `AGENTS.md`, `COLLECTION.md` files, report types, and examples were all written for the same KB goal: methodology for agent-operated knowledge bases. In an installed KB, the project goals live in the user's `AGENTS.md`, while the shipped skill prose still carries examples and value assumptions from this repo.

The first step is not a redesign of graph discovery. It is a prose and goal-frame cleanup: keep the current discovery algorithm and report structure, but remove commonplace-specific assumptions from the generic skill and make the project goal frame explicit where needed.

The connection to the workshop's original "instructions notes" idea is frontloading. An instructions note frontloads the caller's decisions so a sub-agent can execute with clean context. Ingest, connect, and type-driven reviews are the specialized directed-reading case: they do the same kind of work with stable lenses and output contracts. Ingest frontloads source assimilation into a typed source report; connect frontloads graph integration into a candidate-link report; `agent-memory-system-review` frontloads a code-grounded comparison lens into the type spec. Connect's specific contribution is search, candidate filtering, articulation, and label authorisation that a later writer or instruction note can consume without redoing discovery.

## Current coupling

`cp-skill-connect` is coupled to this KB in several ways:

- **Domain examples.** The prose names cases like "when the claim describes behaviour the commonplace system exhibits", `learning-theory-index.md`, `kb/agent-memory-systems/`, snapshots, ingest reports, and `kb/log.md`. Those are valid examples here but not valid defaults in a payments, product-research, incident-response, or personal KB.
- **Reader-value framing.** The articulation test asks what an agent gains by following the link. The mechanism is sound, but an installed KB's intended consumer may be a maintainer, researcher, operator, auditor, or future agent acting under a different goal.
- **Goal-frame omission.** The skill reads the source collection's `COLLECTION.md` and treats it as the only linking-rules surface. That is correct for link authorisation, but the installed KB's project-level goals live in `AGENTS.md` and should filter what is worth surfacing at all.
- **Commonplace-shaped reflection.** The optional reflection step appends to `kb/log.md` and names abstractions, duplicated claims, synthesis opportunities, and note-owner competition. The underlying idea is useful, but installed KBs may not have the same log convention or promotion model.

## Scope for the first pass

### Keep

**Single target artifact.** Keep the one-note/source workflow for now. Multi-source directed reading belongs to the broader instructions-note pattern, not this first connect cleanup.

**`COLLECTION.md` hard requirement.** Keep hard-failing when the source collection has no `COLLECTION.md`. A collection contract is still the right authorisation surface for destinations, labels, search guidance, exclusions, and posture.

**Current report sections.** Keep `Discovery Trace`, `Connections Found`, `Bidirectional Candidates`, `Reverse-edge Candidates`, `Off-authorisation Candidates`, `Raw Text Candidates`, `Rejected Candidates`, `Index Membership`, `Synthesis Opportunities`, and `Flags`. These are mostly general enough. The problem is the prose around them, not the section set.

## Frontloading implications

The frontloading note gives this workshop a binding-time test: what can be known before the live semantic judgment, and what depends on the current target?

For connect, the layers are:

| Layer | Binding time | How it should appear |
|---|---|---|
| Project KB goals | installation/session start | `AGENTS.md` is the standing goal frame; connect should not rediscover or infer it |
| Collection contracts | repository state before the run | `COLLECTION.md` defines destinations, labels, exclusions, and posture |
| Target interpretation | current connect run | read the source artifact and identify what would make useful relationships |
| Candidate discovery | current connect run | run indexes/search/link-following and record what was tried |
| Candidate judgment | current connect run | apply project goals, collection rules, and articulation test |
| Later writing or synthesis | downstream run | consume the connect report instead of repeating discovery |

This splits connect's job from ingest and instruction-note handoff:

- Connect should **frontload graph-discovery state** for later writers and instruction notes: candidate paths, reasons, labels, rejected non-matches, off-authorisation signals, and synthesis opportunities.
- Connect should **not duplicate ingest's source-assimilation job**. If the target is an ingest report, connect should treat its classification and summary as input signal, then focus on relationship discovery and articulation.
- Connect should **not frontload away semantic judgment that is target-dependent**. The skill still needs to read the source and judge candidates in the current run.
- The connect report should preserve enough framing rationale that a downstream instruction note can cite it directly, not just list paths. A candidate without the reason it was selected forces the next agent to redo the expensive part.
- Because prompts carry judgment that schemas cannot express, avoid over-schemaing the first pass. The existing report sections can carry the caller/connector's judgment in prose.

This also exposes an infinite-regress risk. If every frontloaded artifact can itself be prepared by another frontloaded instruction, the system can spend all its effort writing preparation notes instead of doing the bounded semantic work. The boundary needs an explicit negative rule:

> Frontload when the pre-step removes repeated discovery, runtime indirection, or task-specific ambiguity from a later bounded call. Do not frontload when the pre-step merely restates a stable skill contract already loaded by the callee.

For connect, that means ordinary runs should not require a generated "connect instruction" that only repeats `cp-skill-connect`'s procedure. A connect-specific instruction note becomes worth considering only when the target has unusual goals, unusually high ambiguity, or expensive prior selection that the connect agent would otherwise have to rediscover.

### Fix now

**Remove repo-specific examples from generic skill prose.** Replace examples tied to this repository with generic phrasing or conditional examples:

- "when the claim describes behaviour the commonplace system exhibits" -> "when the source describes behaviour that destination collection is meant to document or explain"
- `learning-theory-index.md` -> "the relevant tag or topic index, when present"
- `kb/agent-memory-systems/` concrete reverse-edge case -> a generic reverse-edge example, or move the concrete case into this repo's own collection conventions
- snapshot / `.ingest.md` examples -> "immutable sources or artifacts whose authored surface is elsewhere"
- `kb/log.md` reflection -> "the KB's durable observation log, if one is defined"

**Separate goal frame from link authorisation.** The skill should read or rely on the loaded `AGENTS.md ## KB Goals` as the standing filter for candidate value, while still using `COLLECTION.md` as the authoritative source for destinations and labels.

Working formulation:

> Use the project KB goals to decide whether a candidate is worth surfacing at all. Use the source collection's `COLLECTION.md` to decide where to prospect, which labels are authorised, and how to classify candidates that pass the articulation test.

### Analyze before changing deeply

**Reader-value articulation.** The existing question "what does an agent gain by following the link?" should probably become "what does the intended KB consumer gain by following the link under this project's goals?" But this needs more analysis before being codified, because reader-need labels are one of the strongest parts of the current linking model.

Questions to resolve:

- Is the "reader" always the immediate agent, or the role named in `AGENTS.md ## KB Goals`?
- Should `COLLECTION.md` name reader roles per collection, or should project goals be enough?
- Should the articulation sentence include the standing goal explicitly, for example: "`[source] connects to [target] because [specific reason], which helps [consumer] [goal]`"?
- How should `connect` handle candidates that are locally articulable but off-goal for the KB?

**Report categories.** The current categories look broadly reusable, but they should be reviewed after one or two installed-KB trials. For now, prefer small wording changes over schema changes.

## Proposed first implementation slice

1. Rewrite `cp-skill-connect/SKILL.md` to remove commonplace-specific examples and replace them with installed-KB-safe language.
2. Add an explicit setup step: confirm the project goal frame from the loaded `AGENTS.md` or read `AGENTS.md` if it is not already in context.
3. Rewrite the articulation test to mention the intended KB consumer and project goals without changing the report schema.
4. Adjust the reflection step so it is conditional on the installed KB defining a durable log or equivalent observation inbox.
5. Make the same small language cleanup in `kb/reports/types/connect-report.md`, without changing its sections or schema.

## Non-goals

- Do not redesign connect for multiple input documents.
- Do not change the report schema in the first pass.
- Do not relax the `COLLECTION.md` requirement.
- Do not add a new search backend.
- Do not make shipped commonplace methodology a default candidate destination for user KBs. Installed KBs may link to `kb/commonplace/` deliberately, but user content should not be pulled toward the methodology library by accident.

## Prior work

- [Writing Directed Reading Instructions](./directed-reading.md) - grounds: directed reading as "read material X through lens Y"; ingest is a KB-assimilation instance and connect is a graph-integration instance of that pattern.
- [Workshop README](./README.md) - context: instructions notes and directed reading as clean handoff packets.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - mechanism: instructions notes and connect reports both pre-compute what can be known before the next bounded semantic call.
- [Ad hoc prompts extend the system without schema changes](../../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md) - related: instruction notes as clean context boundaries where the caller frontloads selection and relevance.
- [Link vocabulary and linking approach](../../reference/link-vocabulary.md) - current-state: reader-need labels, collection-owned outbound rules, and articulation tests.
- [Control-plane goals](../../reference/control-plane-goals.md) - current-state: installed KB goals live in `AGENTS.md`.
- [Ship library content under kb/commonplace](../../reference/adr/021-ship-library-content-under-kb-commonplace.md) - current-state: installed KBs have user collections plus a shipped methodology library boundary.
