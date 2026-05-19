# Plan: universalize connect and ingest

## Goal

Revise `cp-skill-connect` and `cp-skill-ingest` so they work as installed-KB skills, not as skills that quietly assume this repository's methodology-KB shape.

The first pass should preserve the current algorithms and report schemas as much as possible. The work is mainly contract cleanup: remove local examples, make collection contracts primary, clarify value judgments, and tighten direct write boundaries.

## Scope

Primary files:

- `kb/instructions/cp-skill-connect/SKILL.md`
- `kb/instructions/cp-skill-ingest/SKILL.md`

Likely alignment files:

- `kb/reports/types/connect-report.md`
- `kb/reports/types/connect-report.schema.yaml`
- `kb/sources/types/ingest-report.md`

No broad schema redesign in this pass. Small schema alignment is in scope when the prose contract adds or removes a required section.

## Skill/type split

The implementation should make the division mechanical, not subtle.

Add this rule to both skills:

```markdown
The skill owns execution. The type owns the report contract.
Use this skill for routing, setup, tool use, delegated skill calls, and file writes.
Use the loaded type spec for section meanings, quality standards, and the template.
If the skill and type both mention the same report-content rule, prefer the type.
```

Operational test for every instruction:

- If deleting the skill would make the agent unable to know what command flow to run, keep it in the skill.
- If deleting the type would make the agent unable to know what the output artifact should mean or contain, keep it in the type.
- If both files currently say the same report-content rule, move it to the type unless it is about execution order, delegated calls, or file writes.

This means the first pass should also de-duplicate the existing skill/type overlap. The skills should become thinner orchestration wrappers that load the type specs. The type specs should carry the stable directed-reading lens, section semantics, quality standards, and templates.

## Connect

### 1. Keep `COLLECTION.md` primary

`connect` should continue to treat the source collection's `COLLECTION.md` as the operational contract for link discovery:

- destination collections to prospect
- excluded destinations
- authorised labels per source-destination pair
- reader needs attached to labels
- collection posture, such as frontloading or rare outbound links
- reverse-edge hints

Do not add a goal-loading step. `AGENTS.md ## KB Goals` is always-loaded context: `kb/reference/control-plane-goals.md` documents this as a load-bearing invariant of the shipped control plane — `AGENTS.md` is loaded on every agent invocation, so its goals are in context without any tool call. Connect relies on that invariant; `COLLECTION.md` is the working surface for connect. (An empty or unfilled `## KB Goals` section is an install-time failure, not connect's concern — see `control-plane-goals.md`.)

The skill prose should cite `kb/reference/control-plane-goals.md` so the absence of a goal-loading step reads as a sourced decision, not an omission. If a future harness violates the always-loaded invariant, the failure is then traceable to a named contract rather than a silent goal-frame gap.

Later work may let collections declare their own explicit goals. This first pass should not invent that mechanism.

### 2. Use goals only as an outer scope check

Where a candidate is semantically plausible but weakly relevant, connect should ask whether it serves the installed KB's declared purpose. This is an outer scope check, not a replacement for collection label authorisation.

Working split:

- `COLLECTION.md` decides where to prospect and which links are authorised.
- The KB goal frame filters whether a plausible candidate is worth surfacing at all.
- Candidate acceptance still depends on the articulation test and authorised labels.

### 3. Generalize the articulation test

Current wording asks what an agent gains by following a link. Keep the test, but make the consumer local to the collection contract.

Preferred direction:

> Every candidate must complete: `[source] connects to [target] because [specific reason].` Keep the candidate only if an agent, or another intended KB consumer named by the collection contract, gains something concrete by following the link.

This keeps the link quality bar while avoiding the assumption that every installed KB is primarily for methodology agents.

This resolves `connect-generalization.md`'s open articulation question conservatively: agents stay the default consumer, and the collection contract may name another. The remaining questions it raised — whether the articulation sentence should embed the standing goal, and whether `COLLECTION.md` should name reader roles per collection — are deferred, not settled here.

### 4. Remove local methodology examples

Replace examples tied to this repository with generic or conditional examples.

Examples to remove or rephrase:

- `when the claim describes behaviour the commonplace system exhibits`
- `learning-theory-index.md`
- concrete `kb/agent-memory-systems/` reverse-edge case
- snapshot and `.ingest.md` examples when they imply this repo's source model is universal
- `kb/log.md` as a side-write destination

Generic examples are fine when they describe a class of artifact, such as immutable sources or artifacts whose authored surface is elsewhere.

Concrete replacement candidates:

| Current shape | Proposed universal shape | Why |
|---|---|---|
| "when the claim describes behaviour the commonplace system exhibits" | "when the source matches the destination's trigger" | Let `COLLECTION.md` carry the concrete trigger. |
| "`tags: [learning-theory]` -> `learning-theory-index.md`" | "`tags: [topic]` -> matching tag/topic index, if present" | Keep the heuristic without this repo's taxonomy. |
| concrete `kb/agent-memory-systems/` reverse-edge case | "when the useful direction is inbound, surface reverse-edge candidates" | Preserve the pattern without naming a local collection. |
| "snapshots in `kb/sources/` typically author links through the matching `.ingest.md`" | "`kb/sources` snapshots are immutable; the matching `.ingest.md` is normally their authored surface" | Keep the installed source model. |
| "`kb/log.md` reflection" | "`Maintenance Observations` inside the connect report" | Remove the side write. |
| "`notes elsewhere` should link to this source" | "artifacts elsewhere may link to this target under their own collection rules" | Avoid assuming every artifact is a note. |
| "what does an agent gain by following the link?" | "what does an agent, or another collection-named consumer, gain?" | Keep agents as default. |

Candidate revised prose for the breadth step:

```markdown
Use the outbound section's triggers, latitude cues, and direction hints to set prospecting breadth. If the source has no plausible match for a destination's trigger, note that in the trace and skip that destination.
```

Candidate revised prose for reverse edges:

```markdown
When the useful direction is inbound, prospect for artifacts elsewhere that should link to this target under their own `COLLECTION.md` rules. Surface those as Reverse-edge Candidates; do not edit the other artifacts.
```

Candidate revised prose for immutable or wrapper-authored artifacts:

```markdown
Snapshots in `kb/sources/` are immutable; their authored connection surface is normally the matching `.ingest.md`. For other non-authored artifacts, use the authored companion named by the collection contract, if one exists. If none exists, keep the suggestion in the connect report.
```

### 5. One direct write: the connect report

`connect` should directly write only:

- `kb/reports/connect/<source-collection>/<note-name>.connect.md`

Do not edit source artifacts, notes, indexes, collection files, or `kb/log.md`.

During setup, load `kb/reports/types/connect-report.md` before candidate discovery. The type owns section meanings and quality standards, so connect needs it before judging candidates, not only when formatting output.

### 6. Segregate maintenance observations inside the report

The connect report has two audiences:

- ingest and link-enrichment agents, which mostly need candidate connection sections
- later maintenance or triage agents, which may care about stale links, duplicated artifacts, or collection-contract gaps

To avoid a side report while keeping consumer noise segregated, add a report-local section:

```markdown
## Maintenance Observations

Report-local observations discovered during traversal that are not connection candidates.

Use this section only for durable issues or follow-up signals:
- stale or broken links
- clear contradictions
- duplicated or redundant artifacts
- competing ownership between artifacts
- repeated unnamed mechanisms or abstractions
- collection-contract gaps, such as useful candidates with no authorised label
- synthesis opportunities durable enough for later promotion

Do not include routine candidate links, ordinary topical overlap, weak associations, or anything already captured in the connection sections.

Downstream connection consumers may ignore this section. A later explicit maintenance or triage step may promote entries from this section into `kb/log.md`, notes, reference docs, instructions, ADRs, collection rules, or other local artifacts.
```

This replaces the current reflection side write to `kb/log.md`. Note the tradeoff: a `kb/log.md` append is durable and committed, while the connect report is gitignored and regenerable, so a maintenance observation is lost if the report is regenerated before a triage step consumes it. This is an accepted cost — decoupling connect from a local log convention is the point — but it makes `Maintenance Observations` a best-effort signal rather than durable state. A KB that needs durable capture should run the triage/promotion step before regenerating connect reports.

`Maintenance Observations` should be a required connect-report section. Update `kb/reports/types/connect-report.schema.yaml` to require the heading, not just the prose template. If implementation later decides the section should be optional, revise this plan and the type doc explicitly; do not leave the schema/prose contract ambiguous.

### 7. Align the connect-report type doc

Update `kb/reports/types/connect-report.md` so it:

- uses the intended-reader articulation language
- includes `Maintenance Observations`
- states that the report is the only direct write
- keeps all existing connection sections

Update `kb/reports/types/connect-report.schema.yaml` so `## Maintenance Observations` is required alongside the existing report headings.

Move detailed report-section semantics from `cp-skill-connect` into this type doc when they are duplicated. Leave the skill with a compact checklist: load the type, discover candidates, verify paths, and write a valid report.

## Ingest

### 1. Keep ingest as KB-assimilation directed reading

`ingest` should still:

- snapshot URLs through `cp-skill-snapshot-web`
- run `cp-skill-connect`
- read the connect report (treat its `Maintenance Observations` section as non-actionable context — ingest may note durable signals from it but must not act on them, consistent with the no-promotion rule)
- classify the source
- summarize it
- extract value relative to current KB context
- state limitations
- recommend one next action
- write the `.ingest.md` report next to the snapshot

Update ingest's connect-report lookup to match the current connect output path:

- connect writes `kb/reports/connect/<source-collection>/<note-name>.connect.md`
- for source snapshots, ingest should read `kb/reports/connect/sources/<snapshot-name>.connect.md`

Do not keep the old flat lookup `kb/reports/connect/<snapshot-name>.connect.md`.

### 2. Interpret "our" locally

Keep natural language like "our theory", "our stack", "our codebase", and "our practices", but add a rule:

> Interpret "our" through the installed KB's goals and local collection contracts.

In this repository, "our" means agent-operated KB methodology. In another installed KB, it means that project's declared system, work, codebase, policy, product, or domain.

### 3. Tighten direct write scope

Ingest's own direct write should be only the `.ingest.md` report.

Delegated steps may write their own artifacts:

- snapshot capture may write a snapshot
- connect may write a connect report

Ingest itself should not directly modify notes, reference docs, instructions, runbooks, policies, ADRs, indexes, collection files, or `kb/log.md`. Promotion belongs to a later explicit step.

### 4. Generalize extractable value

Keep source-type classification, but make extraction prompts goal-relative instead of methodology/software-stack-specific.

Also align the ingest type prose with the schema: `source_type: code-repository` is already allowed by `kb/sources/types/ingest-report.schema.yaml`, so add `code-repository` to `kb/sources/types/ingest-report.md` and to the skill's classification guidance when the skill keeps any source-type summary.

Useful generic value classes:

- evidence for an existing claim, decision, policy, or practice
- contradiction or limitation affecting current KB content
- reusable method, workflow, or procedure
- data point, benchmark, measurement, or empirical result
- vocabulary or framing that improves retrieval and discussion
- operational warning, risk, failure mode, or incident signal
- candidate artifact to write, update, retire, or review

Notes remain the default promotion target for transferable claims, but the recommended action may point to another local artifact type when collection contracts make that the better home.

### 5. Recommended action is advisory

The recommended action should name one explicit next step and its target, but ingest must not perform it.

Allowed recommendation shapes include:

- write or update a note for a transferable claim
- update a reference document or runbook
- update an instruction, policy, ADR, product requirement, dataset, or incident note
- file as source-only reference
- schedule a focused review or brainstorm

The right destination is determined by local collection/type contracts.

### 6. Align ingest-report type doc

Update `kb/sources/types/ingest-report.md` so it:

- says extractable value is relative to the installed KB's goals and current connections
- includes `code-repository` in the source type list
- allows recommended actions beyond note writes
- keeps the existing section set and schema

Move detailed classification, extractable-value, limitations, recommended-action, and template guidance out of `cp-skill-ingest` when it duplicates the type. Leave the skill with execution order: resolve target, snapshot if needed, run connect, read connect report, load the type, write the `.ingest.md`. While editing the skill, fix the duplicate `kb/sources/types/ingest-report.md` read instruction in its Step 3 (the path is currently listed twice).

## Supporting change: control-plane-goals.md

`connect` and `ingest` both run `context: fork`. `kb/reference/control-plane-goals.md` currently says `AGENTS.md` "is loaded on every agent invocation"; sharpen that one clause to state explicitly that this covers forked skill contexts (`context: fork`), so a reader checking whether a forked skill can rely on the goal frame does not have to infer it. This is a one-clause edit, not a redesign — it makes the invariant the two skills now cite unambiguous.

## Validation

After implementation, run:

```bash
commonplace-validate kb/instructions
commonplace-validate kb/reports/types/connect-report.md
commonplace-validate kb/sources/types/ingest-report.md
commonplace-validate kb/reference/control-plane-goals.md
```

Also review `git diff` to confirm the patch only changes instruction/type wording, the `control-plane-goals.md` clause, and the planned connect-report schema heading, and does not introduce unrelated schema or generated-index churn.

## Non-goals

- Do not build the general directed-reading skill in this pass.
- Do not make connect multi-source.
- Do not redesign the ingest report schema.
- Do not remove `cp-skill-connect` from ingestion.
- Do not collapse snapshots and ingest reports.
- Do not make ingest or connect directly promote content into library artifacts.
- Do not introduce explicit collection goals yet; keep that as a future design question.
- Do not clean up `kb/instructions/ingest-directory.md` in this pass. The directory-ingest lens needs the same goal-frame treatment plus code/data-specific guidance (pinning, file manifests, cross-file evidence); scope that as a follow-up so this pass stays a contract cleanup of the two primary skills.
