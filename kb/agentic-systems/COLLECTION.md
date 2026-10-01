# Writing conventions for kb/agentic-systems/

## Text contract

This collection covers external **agentic systems and harnesses as whole systems** — execution loops, orchestration APIs, sub-agent surfaces, scheduling, permissioning, and control — what each is built from and does. Analyses use Commonplace ontology to name comparable mechanisms while preserving the external system's native operation and evidence.

The quality goal is **fidelity + economy**: faithful to what the system actually does, in the minimum shared vocabulary needed to explain it. An analysis that misrepresents the analysed system or forces a mechanism into an ill-fitting Commonplace term is worse than none.

Memory and knowledge are lenses of the whole-system analysis. The separate
`kb/agent-memory-systems/` collection is the legacy review corpus; new comparison
procedures consume the main analysis and its memory/context findings directly.
The memory analyst of `analyse-agentic-system` returns a typed report within
the run. Code copies the accepted report unchanged into the set's memory
member, which carries the comparison profile. Downstream comparison reads
that retained member; a trial report supplies no independent semantic clearance.

## Structure

The collection root is reserved for collection-level operating material:
`README.md`, `COLLECTION.md`, and the collection-owned `instructions/`,
`types/` and `reports/` areas.
Per-system and per-feature analyses live under `reviews/` so the growing
analysis corpus does not obscure those operating documents. Generated cross-system
matrices and tables live under `comparisons/`.

## Collection-owned method

`instructions/` holds the analysis method, its shared contracts, landscape
synthesis and taxonomy maintenance. These procedures serve this collection.
The Commonplace transfer scan stays in `kb/instructions/` because its result
serves Commonplace design work. Generic instruction and type-spec contracts
remain global. There are no nested collection contracts.

For authoring instructions here, use executability and precision as the quality
goal. State the goal, authority, inputs, result, acceptance and stop conditions.
Keep the goal at the top; retain reasons only where an edge case or decision
needs them. Put transferable explanations in notes. Use imperative titles and
trigger descriptions; plain instructions declare `type: types/instruction.md`.
Skills add their invocation metadata. Shared definition contracts may retain
`type: types/note.md`.

An instruction must be self-contained for its declared consumption path. Rely
on root doctrine, collection/type contracts and skills only when the runtime
verifiably supplies them with binding force. Carry task-specific exceptions
and constraints explicitly. A worker packet states purpose, consequential
choices, authority, inputs, owned output, coordination, acceptance and return
conditions that the verified baseline cannot determine. Delegation does not
expand authority; the parent retains scheduling, integration and recovery.
An unstated consequential choice must follow an inherited rule, use deliberately
delegated judgment from authorized evidence, be irrelevant to acceptance, or
be returned as a gap. Use clean context only for a specific benefit.

Treat instruction edits as deployments. Name the consumer and consumption
channel before changing them. Search this collection's and `kb/instructions/`'s
instructions for exact filenames, skill names and named result literals. Read
direct callers, callees, conditional loads and argument/result consumers before
drafting. Update every affected interface in the same change, or report the
unresolved mismatch. An inherited rule is also a composition dependency:
changing a verified baseline requires reviewing its commissioning cohort.

Executing instructions must not depend on an incidental link chase. Outbound
links within instructions serve context transfer, conditional deviations or
meta-readers; keep chains shallow. Use the general instruction labels
`composition`, `precondition`, `invokes`, `applies-when`, `see-also`,
`operates-on` and `rests-on` for those purposes. Never add reciprocal links
solely to mirror an edge. Search the local method and types plus
`kb/instructions/`, `kb/notes/`, `kb/reference/` and `kb/tags/`; execution inputs
are passed through the workflow's declared dependencies. Do not link
instructions into the review corpus, archives or workshops as execution inputs.

Edit canonical files here. Repo skill discovery uses relative projections in
`.agents/skills/` and `.claude/skills/`. These research skills are not promoted
into every initialized project. Inspect promotion and stub generation if a
skill's name, metadata or promotion status changes.

## Report lifecycle

`reports/state/<run-id>/` holds ignored local working analyses. The workflow
owns their cleanup. Ordinary collection validation skips this area through its
validation marker; explicit validation still checks a selected run-state file
and output set. A run retains its opening method commit. An unfinished run from
an earlier method must finish there or remain recovery evidence; never change
its method commit to make it resume under a different method.

`reports/retained/<run-id>/` holds tracked frozen analysis sets. Other explicitly
retained research reports may occupy distinct directories that do not impersonate
analysis run IDs. `reports/retained-archive/` holds exact historical analyses
under their producing contracts. Its marker excludes them from current-schema
collection validation. Historical reviews pin those exact archived bytes;
they are excluded from current comparison populations.

A recorded layout migration may change only declared paths, type identities,
relative link targets needed by relocation, and checksums derived from those
changes. Its retained migration report must map old and new hashes and verify
unchanged analytical content, sources and record identities. This is a bounded
exception to frozen-set immutability, not authority to correct findings.
Historical method commits and commit-bound synthesis provenance stay unchanged.

## Generated reviews

Every complete `analyse-agentic-system` run publishes one compact review in the
`reviews/` directory. Each file records `generated-by: analyse-agentic-system`,
the producing `analysis-run`, a stable `source-identity`, and the
`reviewed-revision`, and the retained `analysis-artifact` path and
`analysis-artifact-sha256`. They are workflow-owned projections of a frozen
analysis set, not hand-authored notes. Do not substantively hand-edit them. Correct the source
boundary or the shared review method, then rerun the skill and replace the
review from those inputs. Git history preserves earlier generated versions.
Publication cannot be waived per complete analysis. The workflow validates a
private candidate as its intended destination before replacing the review. A
correctable pre-publication failure leaves the incumbent unchanged and the run
open. The complete run state is the sole declaration that publication
succeeded.

This regeneration rule keeps system-specific judgment inside one declared
method. A human may change the method and request a new run, but may not tune one
published review independently and still present it as a generated review.
Unmarked per-system and per-feature analyses remain ordinary authored artifacts.

Publication retains the run's set byte for byte under
`kb/agentic-systems/reports/retained/<run-id>/`: the manifest
`ARTIFACT.yaml`, `overview.md`
(identity, boundary, source register, amendment index, synthesis,
limitations), `runtime.md` (runtime account, runtime-declared
records), `memory.md` (memory findings, memory-declared records, comparison
profile), `epistemic.md` (the five epistemic blocks), and `reconciliation.md`
(record amendments, supersessions and unresolved conflicts). The public review
pins ARTIFACT.yaml, which pins every member; comparison
readers need neither ignored run state nor the legacy corpus to reproduce
their fields. Correct or enrich the analysis through a new run, never by
hand-editing a retained member.

## Evidence basis

Open each analysis with a one-line **evidence basis**: what it is grounded in — docs, source code, papers, or first-hand operation of the system — and when that evidence was captured. Comparison readers use the overview's `evidence-tier`: `code-grounded` or `doc-grounded`. Keep those populations separate, and preserve each field's evidence basis within its tier.

## Ontology and local transfer

State the external mechanism in its own operational terms before applying a Commonplace concept. Explain why the concept fits and qualify partial or unresolved mappings. Commonplace chooses the analytical distinctions; it is not the comparison target, and a reader must be able to reject a mapping without losing the external-system account.

Describe a theory pathway through the conditions of a
[theory builder](../notes/definitions/theory-builder.md): localized content,
consumption, criticism of that content, and iteration, where the result of
criticism shapes the next round. Each condition holds only at the
strength supported by its own evidence. Improved capacity for future action
attributable to that criticism is a separate learning claim. Persistence
(within an episode, a run, across runs, or across problems) is a separate
graded finding above condition 4's minimum. Addressability is a separate
graded finding above condition 1's minimum. Record its degree and boundary; whole
replacement, or reconstruction from retained criticisms, can qualify, while
stored rules or parameters alone do not classify the process. Missing
historical rationale does not establish absent criticism; inaccessible model
processing remains unestablished. Reflection additionally requires a
causally connected self-representation of selected aspects inside the
declared system boundary: changes in those aspects can update the
representation, and operations mediated through it can affect later
behavior. Link the defining notes with `rests-on` or `defined-in`.

Current differences from Commonplace, borrowable ideas, and watch items are not part of the durable analysis. They depend on a current Commonplace baseline and interest brief. Produce them, when separately requested, as living transfer state under `kb/reports/state/agentic-system-transfer/`; never feed that scan back into the stable analysis or a public corpus comparison. Keep unresolved candidate judgments until disposition, then replace or delete the state report under its owning workflow.

## Title conventions

- **Descriptive coverage of one system or feature** — name the system (`claude-code-dynamic-workflows.md`).
- **Argumentative analyses** — analyses asserting a specific claim — use a claim-shaped title and the `title-as-claim` trait, following `kb/notes/COLLECTION.md` conventions.

## Outbound linking conventions

Organised per destination; label semantics in [link-vocabulary.md](../reference/link-vocabulary.md).

- **→ `kb/sources/`** — link the tracked ingests an analysis is grounded in, never the local snapshots. Labels: `derived-from`, `evidenced-by`, `see-also`.
- **→ `external`** — cite the source code, documents, papers, or first-hand records already used for the evidence basis; prefer version-pinned targets when available and do not prospect the open web. Labels: `evidenced-by`, `see-also`.
- **→ `kb/notes/`** — search when an analysis maps a system onto theory. Use `rests-on` when the theory explains the analysed design; use rare `is-evidence-for` when the observed system instead bears on the target claim. Promote a novel transferable claim to `kb/notes/` rather than author theory here. Labels: `rests-on`, `is-evidence-for` (rare), `defined-in`, `see-also`.
- **→ `kb/agent-memory-systems/`** — when the analysed whole system has a memory, knowledge, or context-engineering subsystem reviewed there. Use `contains` from the whole-system analysis to the subsystem review; use `part-of` only from a subsystem-focused analysis back to the whole system. Labels: `part-of` / `contains`, `compares-with`, `see-also`.
- **→ this collection's `reports/retained/`** — cite a retained set's overview or the member that holds the record, evidence, or normalized field a comparison needs. Labels: `see-also`.
- **→ `kb/reports/retained/`** — cite separately retained research evidence. Labels: `evidenced-by`, `see-also`.
- **→ `kb/reference/`** — scan when a design element has a direct Commonplace analogue. Labels: `see-also`.
- **→ `kb/instructions/`** — link a Commonplace procedure when the external system analysis directly maps onto an operating rule or workflow. Labels: `procedure`, `see-also`.

## Type eligibility

A typed artifact in this collection may use a global type, named by its path under the library root such as `type: types/note.md`, or a local type spec under this collection's `types/` directory, named by its path under the KB root such as `type: agentic-systems/types/<name>.md`. Frontmatter-free Markdown is implicit `text`.

## What does NOT belong here

- Transferable claims about KB methodology or orchestration theory → `kb/notes/`
- Raw captures of external sources → `kb/sources/.snapshots/`, each analysed by a tracked ingest in `kb/sources/`
- Descriptions of the Commonplace system itself → `kb/reference/`
- Current Commonplace differences, borrowable ideas, and watch items → a selective transfer scan under `kb/reports/state/agentic-system-transfer/`
- General Commonplace procedures and how-to guidance → `kb/instructions/`
- Work in progress → `kb/work/`
