---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Funes workflow: source ingest through wiki delivery, shallow-compile rejection and later cited reuse."
run-id: AAS-2026-10-15-funes-a9e6dbb3946a-01
reviewed-boundary: 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11
---

# Funes workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a human-requested source ingest, compilation into the library wiki, and session closure. It is selected because the protocol explicitly orders these steps and supplies both a shallow-compile correction rule and mechanical checks. Later Q&A is a separately triggered consumer of the delivered wiki, not an automatic final stage of ingest. The relevant existing routes are [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [RT-RTE-health-audit](runtime.md#rt-rte-health-audit) and [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer).

This account uses SRC-1 within the [frozen boundary](boundary.md#source-register). Direct inspection covered `AGENTS.md`, `starter-library/AGENTS.md`, `protocol.md`, `tools/compile_lint.py` and `.github/workflows/funes-lint.yml` at the reviewed commit; these paths were already included by boundary. The protocol supplies doctrine/design evidence; the linter and CI configuration supply implementation evidence. The linter's historical failure account supplies only reported operation. No observed workflow run was supplied or executed. Thus this is an ordered shipped procedure with implemented local checks, not a demonstrated successful ingest or reliability claim.

### Request, responsibility and initial persistence

The human supplies a source to an external file-capable agent. Root instructions route that agent to the current library's local instructions and then to the shared protocol. The starter library's local file specifies scope as an adoption placeholder and declares no structural deviations. The external host must actually deliver those instructions; Funes does not implement the model scheduler or a delegate launch. See [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions) and [RT-ABS-model-driver](runtime.md#rt-abs-model-driver); SRC-1, `AGENTS.md`, `starter-library/AGENTS.md`.

The human delegates editorial ownership to the Librarian, not to a hierarchy of specialized agents:

> **You own the wiki**; the human feeds sources and asks questions, and rarely edits
> it directly.
> --- `protocol.md`

The first persistence handoff is source content to a verbatim date-prefixed file under `raw/` and a registry row with status `raw`. Unfetchable material can be URL plus pasted text. Binary originals remain alongside extracted text, with partial page coverage recorded when applicable. These are instructions to the same Librarian, not a software transaction or a second agent's return payload. The raw path and registry row preserve source identity for subsequent compilation. The selected ordinary text path needs no extraction helper; PDF and caption helpers are alternatives, not prerequisites. SRC-1, `protocol.md`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar), [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch).

### Compile decisions and handoff artifacts

The same Librarian next writes a source note containing source-specific summary, takeaways and a raw link. It extracts ideas into concept articles, merging into existing concepts rather than duplicating them. It then adds reciprocal links, places concepts in topic maps, updates wiki navigation, changes the registry status to `compiled` and appends the changelog. The ordered steps and minimum passage are retained in [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile); SRC-1, `protocol.md`.

Each handoff supplies different material to the next consumer: the source note supplies an interpreted summary plus a route to the original; concepts supply reusable explanations with source links; topic maps and the wiki index supply navigation. Those files persist for later invocations. Neither the `compiled` marker nor link existence certifies extraction fidelity. The Librarian judges idea boundaries and topic fit under natural-language instructions; ordinary in-library compilation has no requested per-article human approval. SRC-1, `protocol.md`; [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree), [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile).

A consequential branch occurs if compilation reveals a substantive connection to another library. The agent must propose the connection before writing it, and approval precedes both the link and its reciprocal backlink. Without approval, the prescribed path remains in-library. This is a human decision point, not an executable permission barrier. The exact rule and enforcement limit are already retained in [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile) and [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees); SRC-1, `protocol.md`.

### Verification, rejection and recovery

The protocol explicitly rejects a shallow compile rather than treating populated files as sufficient:

> Templated summaries, takeaways that only restate a concept's one-line
> lead, and stub articles that discard most of a source mean extraction did not
> happen. Redo the compile rather than padding it.
> --- `protocol.md`

The Librarian owns this editorial recovery. The retained raw source is the basis for recompilation; padding is not the requested repair. There is no automatic revert or retry coordinator on the ingest route. The instruction to redo establishes intended response, not an observed successful correction. SRC-1, `protocol.md`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile).

The implemented compile linter receives file text, not a source-and-answer gold standard. It compares source-note Summary sections and concept leads for repeated 8-grams and near-duplicate overlap. Echo detection compares substantive lines linking concepts against those concepts' first sentences. Word counts and the raw/wiki ratio are proxies surfaced for review. The code turns duplicate/echo findings into a nonzero exit; advisories affect exit only with `--strict`:

> if args.strict:
>         return 1 if (gate_problems or advisory_flags) else 0
>     return 1 if gate_problems else 0
> --- `tools/compile_lint.py`

These checks can reject selected textual patterns, not determine whether a claim follows from its source. Missing or unexamined sections can escape the comparisons. A structurally valid, nonduplicated but false article is not ruled out. The supplied baseline also bounds link/orphan/frontmatter checks and identifies the absence of a semantic answer oracle: [RT-RTE-health-audit](runtime.md#rt-rte-health-audit). SRC-1, `tools/compile_lint.py`, `protocol.md`.

CI is a separate caller: push or pull request causes checkout, Python syntax checking, link/orphan/frontmatter auditing and compile lint. Its compile command omits `--strict`, so short-note and compression advisories alone do not reject that check. It is not a mandatory per-ingest stage, and no branch-protection configuration establishes a merge barrier. A reported failure leaves correction to the agent or human; the linter prints findings and returns status rather than rewriting articles. SRC-1, `.github/workflows/funes-lint.yml`, `tools/compile_lint.py`; [RT-RTE-health-audit](runtime.md#rt-rte-health-audit).

On-request or periodic editorial health review separately asks the Librarian to inspect contradictions, grounding, gaps and other issues, write a dated report, fix safe items and propose the rest. This review is not shown to happen after every ingest. The protocol assigns the work; the mechanical checks do not dispatch a reviewer or prove editorial completion. SRC-1, `protocol.md`; [RT-RTE-health-audit](runtime.md#rt-rte-health-audit).

### Delivery and later reuse

The procedure's ingest completion consists of persisted raw and compiled files, connected navigation, the `compiled` registry marker, changelog updates and a human-facing summary. The protocol says:

> - The human rarely edits the wiki — you do. Act, then summarize.
> --- `protocol.md`

> - Close the loop each session: update `INDEX.md` files + `meta/CHANGELOG.md`.
> --- `protocol.md`

These are procedural completion signals, not an atomic commit, a signed acceptance certificate or a demonstrated quality outcome. Ordinary ingest does not prescribe commit/push as its delivery condition; explicit commit/push belongs to library provisioning, a different route. SRC-1, `protocol.md`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [RT-RTE-library-setup](runtime.md#rt-rte-library-setup).

When a later human question arrives, the Librarian is instructed to search INDEX → sources → concepts, answer with relative citations, acknowledge noncoverage and save substantial outputs under `outputs/`. It offers to file durable portions back into the wiki; the offer is not an automatic write-back trigger. This later consumer explains why the compilation handoffs matter: the files become available knowledge and navigation for another invocation, with links back to raw evidence. No populated-library trace establishes that these files were selected, changed an answer or improved its correctness. SRC-1, `protocol.md`; [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile)

Workflow role: selected primary procedure. Its handoffs are successive persistent artifacts managed by one Librarian, not established agent-to-agent delegation. Procedural completion depends on the navigation, registry and changelog steps as well as article production. The shallow-compile rejection returns editorial responsibility to that Librarian; no machine-generated retry payload is specified. Later Q&A requires a new human trigger rather than continuing automatically from registry completion.

#### On [RT-RTE-health-audit](runtime.md#rt-rte-health-audit)

Workflow role: available verification and maintenance branch, with two separately triggered consumers. Local/editorial review is requested or periodic; CI is push/pull-request triggered. Neither is established as a required stage before every ingest summary. A failed mechanical check communicates a bounded defect to its caller, not a rollback action or semantic verdict.

#### On [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)

Workflow role: subsequent read-back consumer of the ingest deliverable. Saving an output and offering durable filing are distinct from admission of another wiki change. The inspected procedure does not establish an autonomous repeating ingest–answer–rewrite cycle.
