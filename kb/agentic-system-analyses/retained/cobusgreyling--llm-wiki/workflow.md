---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LLM Wiki workflow account: human-requested incremental source ingest, its maintenance handoffs, optional diagnostics and bounded recovery."
run-id: AAS-2026-10-14-llm-wiki-b437987c5802-01
reviewed-boundary: a424e6875aa2d5736d9c0d03d7c28bdbe32892a5
---

# llm-wiki workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is **incremental ingest of one human-selected raw source into an existing wiki**. It is selected because the shipped maintainer instructions connect a single request to source reading, interpretation, several dependent page updates and durable bookkeeping. This is one prescribed operation, not a chain invented by joining independent CLI capabilities. Its canonical route is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), performed by [RT-CMP-agent](runtime.md#rt-cmp-agent). SRC-1: `src/llm_wiki/scaffold/AGENTS.md`.

> Triggered when the human adds a file to `raw/` and asks you to ingest it.
> --- `src/llm_wiki/scaffold/AGENTS.md`

The ingest procedure is doctrine/design. Toolkit scaffolding, coverage reporting and CLI failure handling are inspected implementation. None of these sources establishes that an agent completed a real ingest, read every required page or delivered a correct integration. The external host supplies model execution, filesystem editing and conversational delivery; it is outside the frozen implementation. The analysis does not execute the target. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/new_page.py`, `src/llm_wiki/ingest.py`, `src/llm_wiki/cli.py`; see the [boundary](boundary.md#boundary-and-evidence).

### Request, interpretation and human guidance

The human supplies the source by adding it to `raw/`, then delegates the integration request to the maintainer. The input handoff supplies the raw document and a request; the project protocol supplies page ownership, templates and maintenance obligations. [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions) describes the authority channel. Host loading and compliance remain unobserved. The source is prescribed read-only, while the maintainer owns wiki writes. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`.

The maintainer is instructed to read the entire source, view images separately where present and discuss takeaways before writing. The human can guide emphasis and decide what matters. Batch mode removes that discussion step; it does not supply an alternative content verifier. Discussion is an opportunity for guidance, not an explicit per-page acceptance handshake or software-enforced veto. The model interprets the source and selects what to integrate; there is no expected-answer oracle. These control limits are already recorded in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). SRC-1: `src/llm_wiki/scaffold/AGENTS.md`.

### Semantic work and dependent writes

The source page is the first prescribed durable result. Its template asks for a short summary, key takeaways, entities, concepts, quotes and a raw reference. The template offers structure but does not generate content or judge fidelity. In particular, `raw_file` starts empty; the agent must supply the source mapping. SRC-1: `src/llm_wiki/scaffold/templates/source.md`.

> raw_file: ""
> author: ""
> date_published: ""
> --- `src/llm_wiki/scaffold/templates/source.md`

The maintainer next updates every affected entity and concept page, creating missing pages. It conditionally revises synthesis if the source changes the overall picture and flags conflicts with existing claims in the contradiction ledger. The workflow therefore delegates both page selection and semantic revision to the same agent. It does not delegate a review to an independent worker. The source supports an integrated multi-page maintenance request, not automatic parallel execution or coordinated transactions. The synthesis and conflict obligations, and their theory-assessment limits, are recorded in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). SRC-1: `src/llm_wiki/scaffold/AGENTS.md`.

Finally the maintainer updates the index for new or changed pages and appends the dated ingest entry. These are part of delivery, rather than optional metadata after the source summary. The shipped checklist makes the completion criteria explicit:

> - [ ] Source page created
> - [ ] Entity pages updated/created
> - [ ] Concept pages updated/created
> - [ ] Synthesis revised (if warranted)
> - [ ] Contradictions flagged (if any)
> - [ ] index.md updated
> - [ ] log.md appended
> --- `src/llm_wiki/scaffold/AGENTS.md`

There is no toolkit-generated ingest return object on this route. The prescribed delivered result is the integrated wiki state with catalog and timeline updated. A conversational report alone would not satisfy that checklist. Conversely, a dated entry alone does not establish that the semantic writes were completed. Later maintenance and question-answering are intended consumers of those changed files through [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query); actual read-back and benefit are unobserved. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`.

### Verification and rejection boundaries

The ingest checklist is a protocol, not an executable acceptance gate. The post-ingest helper invokes `wiki ingest-status` and then prints unchecked checklist text. It neither verifies all obligations nor performs missing writes. SRC-1: `scripts/ingest-checklist.sh`.

> echo "== Ingest status =="
> wiki --root "$ROOT" ingest-status
> --- `scripts/ingest-checklist.sh`

Coverage reporting checks raw filenames against source-page `raw_file` mappings. It labels a raw file ingested when it has a mapped page, pending otherwise; source pages without a mapping are incomplete and mappings without a raw file are orphaned. This can diagnose bookkeeping omissions, not accept summary fidelity, entity coverage or synthesis decisions. The decisive predicate is inspected implementation, not model judgment. SRC-1: `src/llm_wiki/ingest.py`.

> status="ingested" if source_page else "pending",
> --- `src/llm_wiki/ingest.py`

Structural lint is separately requested or periodic; the ingest instructions do not mandate lint before completion. [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) diagnoses structure, asks the agent to fix errors and proposes warning fixes. Its CLI can reject the diagnostic invocation with exit 1 at the configured severity threshold, but this occurs after inspecting existing files. It does not block or roll back ingest writes. MCP diagnostic delivery likewise does not provide a transaction gate. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/cli.py`; the runtime record supplies the threshold quotation and enforcement limits.

### Failure and recovery path

A concrete rejection path is available **if the maintainer chooses the optional template-creation tool**. [RT-RTE-page-create](runtime.md#rt-rte-page-create) rejects an existing destination unless forced. The CLI catches the helper's existing-file, missing-template and invalid-input exceptions and converts them to a user-facing Click error; it does not automatically retry or assign another agent. SRC-1: `src/llm_wiki/new_page.py`, `src/llm_wiki/cli.py`.

> except (FileExistsError, FileNotFoundError, ValueError) as exc:
>     raise click.ClickException(str(exc)) from exc
> --- `src/llm_wiki/cli.py`

An existing source page can instead be read and updated by the maintainer, a different slug can be supplied, or the caller can deliberately force replacement. The first two are manual recovery choices consistent with the update protocol, not wired retries. Force is an implemented override and may discard existing content; it is not proof that the replacement passed semantic review. A successful tool call only writes rendered template text and returns a path. Its CLI reminder leaves index and cross-link work to the caller. SRC-1: `src/llm_wiki/new_page.py`, `src/llm_wiki/cli.py`; see [RT-RTE-page-create](runtime.md#rt-rte-page-create).

For interrupted multi-page integration, the prescribed completion obligations identify unfinished work, but the inspected procedure does not specify checkpoints, atomic commit or automatic rollback. The external maintainer and human must inspect and repair the files. Optional Git history is not an ingest transaction or an automatic commit. The source neither establishes deployed history coverage nor host-level recovery. These limits prevent an all-or-nothing delivery or reliability claim. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/new_page.py`; see [runtime coordination](runtime.md#ordinary-invocation-from-project-creation-to-a-filed-answer).

### Inspection coverage

This member directly inspected the complete bundled `AGENTS.md`, source template, `new_page.py`, `ingest.py` and `scripts/ingest-checklist.sh`, plus the lint and page-creation handlers in `cli.py`, all at SRC-1's frozen commit. The source template adds inspected doctrine/design coverage to the boundary's initial inspection; the other paths refine already-inspected mechanisms. No external sources, examples as execution traces, host internals or target tests were used. The account does not infer sub-agent scheduling, automatic semantic ingest from watch notifications, or actual completion from the presence of a source page.

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

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Workflow role: the selected end-to-end maintenance operation. Its completion obligations include semantic updates plus index/log work; no independent review or executed success is established. Discussion is bypassable in batch mode. Coverage reporting and lint are optional diagnostic follow-ups, not an enforced ingest admission gate.

#### On [RT-RTE-page-create](runtime.md#rt-rte-page-create)

Workflow role: optional scaffold substep, not the semantic writer for the complete ingest. Rejection returns to the caller through the CLI exception path; successful creation still leaves integration, index and cross-links unfinished. Force bypasses existing-file rejection rather than completing or validating those obligations.

#### On [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)

Workflow role: separate periodic/requested verification and repair operation. Its threshold can fail a CLI invocation after writes exist, but cannot reject the complete ingest before persistence. The external agent owns subsequent corrections; no automatic rollback or independent semantic acceptance is established.
