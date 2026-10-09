# Naming review of the engine and analysis vocabulary

Reviewed 2026-10-09, after ADR 115 and the report-verification rename,
against three sources: Code Complete's chapter on naming (a name says fully
and accurately what the thing is; problem-domain words over solution-domain
words; opposites paired exactly; no two names that differ by one qualifier
while meaning unrelated things; no word with several meanings in one
project; vague words such as options, data, info avoided; one convention
for separators and qualifier position), Clean Code's naming chapter (one
word per concept, one concept per word, no puns), and this repository's
rule that a code identifier is the concept's word. Proposed, not applied:
renames touch files the implementing session owns.

Names reviewed: the workshop [glossary](./glossary.md), the layout keys,
the compact plan's keys and modes, the prompt's line names, the engine's
addresses, relation and judgment fields, the standard handlers and reuse
modules, the CLI subcommands, the analysis type and instruction file names.

## Rename

Ordered by how much confusion the current name causes, highest first.

| Name | Where | Rule broken | Proposal |
|---|---|---|---|
| `worker-runtime` | prompt line, `worker-runtime.json` | differs from `runtime`, the runtime report's line in the same prompt, by one qualifier while unrelated: one is the analysed system's runtime, the other the worker's model and effort | `worker-identity` |
| `set` beside `artifact` | `set_check`, "whole-set validation", `set/` directory, the analysis type's name, against `artifact`, `ARTIFACT.yaml`, directory artifact | two words for one concept, the directory artifact instance; `set` is ADR 095's word, `artifact` the definition's | `artifact` in engine and reuse code now (`artifact_check`, "artifact validation"); the type name `agentic-system-analysis-set` later, by relocation, when a retained set is next regenerated |
| `report` (CLI) | `commonplace-analysis report`, module `report.py` | `report` already means the four analyst reports, `report-verification`, the `report` output and `kb/reports/`; the engine function the subcommand calls is `inspect()` | subcommand `inspect`, module `inspection.py` |
| `record-check` | the set-check job and its line | left behind by the `record-verification` rename; it checks the four reports as one artifact | `report-check` |
| `verify-records.md` | instruction file | same leftover; the role is `report-verification` | `verify-reports.md` |
| `reasons` against `findings` | `content_reasons`, `extension_reasons`, `protocol_reasons` in code; `## Findings` in the refusal packet; `Finding` in the validator | one concept, two words: code collects reasons and writes them as findings | `findings` in code; `reasons` retired |
| `<role>-seen` | derived apply inputs | the vocabulary word is `handed` (the address, the glossary); `seen` is a second word for it | `<role>-handed` |
| `type_spec` | plan key, `Plan.type_spec`, `Run.type_spec` | the manifest and the layout say `type`; `spec` is a solution-domain suffix | `type` in the plan; `type_spec` in code only where `type` is shadowed |
| `sha256` beside `plan_sha256` | `inspect()["declaration"]` | the unqualified name is the ambiguous one; qualifiers inconsistent | `declaration_sha256` and `plan_sha256` |
| `required: by:` | layout | `by` says nothing about what it does; it names the condition under which roles are required | `required: when: {role, field, values}` |
| underscores beside hyphens | plan YAML: `type_spec`, `max_attempts`, `order_only` against `frozen-source`, `prompt-section`, `verified-by`, `order-only` | one separator convention per file kind; YAML keys are data, not identifiers | hyphens in every plan key; `order_only` and `order-only` become one spelling |
| `verdict` | `apply_verdict`, prose | a third word beside verification (the member) and judgment (the engine record); it is the verification's Blockers and Limits read as a judgment | `apply_verification`; "verdict" in prose only for the Blockers and Limits content, or retired |
| member type names | `agent-memory-analysis-report`, `agent-memory-profile` against `agentic-system-runtime-report`, `agentic-system-epistemic-report` | one family, two prefixes, and one member says "analysis report" where its siblings say "report" | `agentic-system-memory-report`, `agentic-system-memory-profile`, by relocation |
| `synthesize-findings.md`, `fix-boundary.md` | instruction files | `findings` is the validator's word; `fix` reads as repair where it means establish | `synthesize-analysis.md`, `declare-boundary.md` |
| `handlers.py` twice | `artifactrun/handlers.py`, `lib/agentic_analysis/handlers.py` | two modules differing only by package; one holds the standard handlers, the other the analysis's opener, acquisition and declared checks | the analysis module after what it holds, such as `opening.py` plus `checks.py` |
| `profile` | worker profile against the memory profile and `profile-verification` | one word, two concepts; the file is already `worker-profiles.yaml` | `worker-profile` wherever the worker's is meant, including the manifest's `worker.profile` field read as qualified |
| `options` | code-job key, `attempt.options` | a vague word; it holds the frozen-source role and the declared checks and feedback | `extensions`, with `frozen-source` moved to a plan-level fact the handler reads from the run rather than per job |

## Keep the name, fix the definition

| Name | Issue | Fix |
|---|---|---|
| `check` | one word across the standard handler, the derived `check-<role>` job, the criteria group `check`, the `checks:` extension list and prose "content check"; all but one are the same concept, a structural check of a candidate | rename only the criteria group, to `contracts`, since it is a bundle of files, not a check |
| `open` | the analysis job `open` and its `opening` output against an attempt's `open` state and `membership: open` | the job is named after what it writes: `opening`; the two other uses are distinct enough once the job no longer shares the verb |
| `source` | `Input.source` (what an input addresses) against the run parameter `source` (the analysed system's location), `frozen-source` and `sources.py` (external acquisition) | the problem-domain word stays with the analysed source; the engine's `Input.source` is the solution-domain use. Rename it in YAML to `from`, which `identity` already uses for the same meaning, with a Python attribute that is not the keyword; or leave it and say so in the glossary |
| `pin`, `fix`, `freeze` | inputs are pinned at open, the declaration and type are fixed at start, external sources are frozen, the manifest pins members | four verbs for "held at a version"; define each once in the glossary: pinned for attempt inputs, fixed for the run's declaration and type, frozen for external sources; the manifest records digests |
| `status` | `commonplace-run status` lists members and hand-outs; `RunStatus` is what `advance` returns | distinct things; say so in the glossary or rename the dataclass to `AdvanceResult`, the name the glossary once replaced |
| `order-only` | solution-domain jargon for "must exist, change is no signal" | keep, with its definition beside every use in plan docs; no better short word found |
| `reads`, `files`, `inputs` | three keys for a model job's inputs: run-produced, library files, plan-level | keep; state the split once in the proposal's syntax section |
| `apply-<role>` | "apply" says little on its own | keep; `apply-report-verification` reads as applying that verification, which it is |
| `identity` | Astra's draft wanted `matches-fields-from`; the key is a noun for the relation | keep; the "copies" wording is already fixed to equality. `repeats` is the one-verb alternative if ever renamed |
| `accepted/refused`, `completed/failed`, `passes/fails/warns` | three outcome vocabularies | distinct levels: judgment outcome, attempt state, check result; state the three in the glossary |

## Already consistent

Opposite pairs are exact: `verifies` and `verified-by`, `candidate` and
`incumbent`, `origin` and `partner`, `producer-attempt` and
`verifier-attempt`, `answered-refusal` and `answers`. The prompt's line
names are uniformly hyphenated and the slots-are-lines rule gives them one
meaning each. The job named after its role, `check-<role>` and
`apply-<role>` as derived names, and `report-verification` with
`report-check` would make one family.

## Order

The first five renames are cheap now, while the retained area is empty and
no run is in flight, and each removes a collision a worker meets in its
prompt. The type relocations and the `set` to `artifact` change in the
analysis type name wait for the next regeneration of a retained set. The
rest are the implementing session's call as it touches each file.
