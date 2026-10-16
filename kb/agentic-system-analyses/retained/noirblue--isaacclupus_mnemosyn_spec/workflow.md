---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of IsaacCLupus_mnemosyn_spec: proposed source-to-published-knowledge lifecycle, rejection and later query at the frozen specification revision."
run-id: AAS-2026-10-15-isaacclupus-mnemosyn-spec-1887e13dcc13-01
reviewed-boundary: "0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92"
---

# IsaacCLupus_mnemosyn_spec workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is ingest a document, compile a draft, audit it, approve and publish it, then consume it through a later query. This is selected because the source explicitly joins these stages and provides both a rejection branch and file-level delegation contracts. It is a proposed workflow, not a demonstrated multi-agent execution. The target supplies a memory substrate to external agents; model roles inside its compilation design are not evidence of independent agents coordinating an enclosing task. The canonical referent is [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle). SRC-1, `ARCHITECTURE.md`, `GETTING_STARTED.md`, `python_thoughts/05-heavy-llm-compilation.md`.

> *The "happy path" of a raw source through Mnemosyne: ingest → compile → audit → publish → query. Rejected drafts loop back for recompilation. Every stage is logged to `audit_log`.*
> --- `ARCHITECTURE.md`

The [boundary](boundary.md#boundary-and-evidence) establishes a complete specification artifact but only a partial implemented loop. Here, source inspection covers the complete architecture and heavy-compilation study, plus the getting-started guide's ingestion-through-query sections. The latter adds doctrine/design coverage of explicit audit failure actions, approval commands and query delivery. No target code, examples or tests were run; no execution trace was supplied. These sources establish intended coordination, not successful activation, quality improvement or reliable enforcement. The legacy bridge is treated separately, not used to fill missing implementation between proposed stages.

### Request and delegation

The initiating principal is an external operator or agent client. The guide illustrates ingestion of a Markdown note in `raw/self/` or a PDF in `raw/world/`, with a namespace supplied to the proposed CLI. It explicitly qualifies the ingestion CLI as “when implemented.” The document extractor is assigned to a Python satellite: it parses heading-aware segments; a fast model extracts concepts, entities and claims; the proposed store retains a `RawDocument` with provenance; a compile job is queued. The guide describes extraction again at compilation, so it does not establish that extraction runs exactly once. SRC-1, `GETTING_STARTED.md`.

> 1. **Document extractor** (Python satellite) parses the file into heading-aware segments
> 2. **Fast LLM** (`ingest_fast` model) extracts concepts, entities, and claims
> 3. A `RawDocument` with provenance metadata is stored in `state.db`
> 4. A **compile job** is queued for the heavy model
> --- `GETTING_STARTED.md`

The compilation study allocates orchestration between a Rust core and a Python satellite. This is task delegation through an intended process contract, not a demonstrated sub-agent conversation. The Rust core delegates compilation, audit and structured extraction via JSON-over-stdout. The illustrated satellite commands make the handoffs concrete: extraction takes `/tmp/raw.json` and emits `/tmp/concepts.json`; compilation receives both and emits `/tmp/article.json`; audit receives that article and emits `/tmp/audit.json`; finalize receives article and audit files and emits `/tmp/final.json`. Templates and fast/heavy tier selectors accompany the relevant stage commands. The study assigns actual publication to the Rust core; satellite finalization only prepares it. These are example contracts, not an installed command chain. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

> **Mnemosyne Decision:** Python satellite for all heavy LLM compilation tasks. Rust core delegates compilation, audit, and structured extraction to the Python satellite via JSON-over-stdout.
> --- `python_thoughts/05-heavy-llm-compilation.md`

The compiler's intended inputs include source material, extracted concepts, related-page summaries and flagged contradictions. The template requests citations, cross-links, confidence and maturity, as recorded in [RT-OBJ-compile-template](runtime.md#rt-obj-compile-template) and [RT-BAP-compile-guidance](runtime.md#rt-bap-compile-guidance). The template shortens related-page summaries and source content with Jinja filters; the source's use of a variable named `max_tokens` does not demonstrate tokenizer-based fitting. The example model call supplies the rendered prompt as one user message. Consequently neither complete source visibility nor enforced instruction/source separation follows from the handoff. The proposed `ArticleOutput` carries title, summary, sections with citations, cross-links, confidence, maturity and contradiction notes. The guide places the resulting Markdown under `wiki/.drafts/` and records a content hash. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`, `GETTING_STARTED.md`.

### Verification, rejection and recovery

Verification has two different targets. Structured-output validation checks whether a response fits a declared shape; it does not establish factual correctness. The study's compilation example requests `ArticleOutput` with `max_retries=3`. It describes validation feedback to the model and proposes a plain-text/manual-parsing fallback for repeated failures in its risk table. No inspected deployed handler establishes that fallback or who performs the manual parsing. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

Content admission is a later audit-and-approval decision. The guide specifies three passes and different failure actions:

> | **1. Structural lint** | Orphan pages, missing wikilink targets, broken frontmatter | Block publication |
> | **2. Contradiction detection** | Claims that conflict with existing `wiki/` pages | Block or warn (configurable) |
> | **3. Adversarial review** | Devil's advocate critique of argument structure | Block if critical flaws found |
> --- `GETTING_STARTED.md`

The heavy-compilation study assigns the audit stage to a heavy model and expects an `AuditResult` containing score, issues and recommendations. Its contradiction example compares the new article with supplied existing-page text. Neither the file contract nor that example establishes how all comparison pages are selected. The proposal therefore supports an audit intended to inspect structure, inconsistency and argument quality, not exhaustive detection. No expected-answer oracle is supplied for ordinary article acceptance. Existing pages are comparison material, not independently certified truth. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`, `GETTING_STARTED.md`.

The study describes threshold-based disposition with a configurable human gate:

>     - Score >= threshold: promote to wiki/
>     - Score < threshold: return to drafts/ with feedback
>     - Human approval gate (if configured)
> --- `python_thoughts/05-heavy-llm-compilation.md`

Thus models propose article content and audit judgments; orchestration is intended to apply the score threshold; a human can withhold approval when that gate is configured. The guide illustrates explicit approval of one draft or all passing drafts before publish. Starting ingestion or compilation is not per-article approval. The documents describe policy alternatives, not a single proven ordering between every audit blocker, numeric threshold and human approval. No unconditional human veto across all configurations is inferred. SRC-1, `GETTING_STARTED.md`, `python_thoughts/05-heavy-llm-compilation.md`.

On the rejection branch, the intended recovery is a draft retained with feedback and returned for recompilation. This is a content-revision opportunity, not evidence that criticism actually changed another output. The architecture names a rejection-feedback loop, while the study leaves automatic contradiction-driven recompilation versus human review as an open question. The responsible next-step owner is therefore only partly specified: core orchestration owns the proposed stage progression, but the inspected texts do not settle who initiates every new attempt, its stopping rule or its retry limit. The bounded three-retry example concerns malformed model output, not the number of audit/recompile rounds. SRC-1, `ARCHITECTURE.md`, `python_thoughts/05-heavy-llm-compilation.md`.

> 4. **Contradiction resolution workflow:** When contradictions are detected, should the satellite auto-recompile with contradiction context, or flag for human review?
> --- `python_thoughts/05-heavy-llm-compilation.md`

### Delivery and later consumption

For this workflow, admission reaches delivery when an accepted draft is promoted into published knowledge and made available to later consumers. The architecture assigns atomic promotion and coordinated search-index, graph and pack rebuilding to the publish engine. That is the design invariant recorded in [RT-CLM-publish-atomicity](runtime.md#rt-clm-publish-atomicity), not evidence of a deployed transaction. A prepared `/tmp/final.json`, a model's confidence score or an approval command alone is not that delivered state. SRC-1, `ARCHITECTURE.md`, `python_thoughts/05-heavy-llm-compilation.md`, `GETTING_STARTED.md`.

The guide then follows a later `ask` request: hybrid search selects relevant pages, graph retrieval adds neighbors, context budgets trim sources, and a chat model generates a cited, cross-linked answer stored in `wiki/synthesis/`. This supplies a source-supported later consumer for the published material, without demonstrating answer correctness, actual budget enforcement or downstream agent compliance. SRC-1, `GETTING_STARTED.md`.

> 1. **Hybrid search** (BM25 + optional vector re-ranking) finds relevant pages
> 2. **Graph context** retrieval adds inbound/outbound neighbors
> 3. **Context budget** enforcement trims sources to fit `context_budget`
> 4. **Chat model** generates a cited, cross-linked answer stored in `wiki/synthesis/`
> --- `GETTING_STARTED.md`

The statically inspected legacy paths do not instantiate this whole workflow. [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools) dispatches ingest, compile and audit as separate backend calls; compilation does not automatically call publication. [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish) describes a separate sequential copier/index/reload path, including its asymmetric draft filtering and ignored subprocess exit codes. That record's passages support the contrast: apparent completion need not mean all recipients synchronized, and no coordinated rollback is established. [RT-RTE-client-query](runtime.md#rt-rte-client-query) returns backend outputs rather than enforcing the proposed query budgets. External backend implementations are outside the frozen source. These limits prevent treating the design's approval, recovery and delivery claims as demonstrated bridge guarantees. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.

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

#### On [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

Workflow-specific handoff boundary: the satellite's extraction, compilation, audit and finalize examples exchange explicitly named JSON files; finalization is preparation, with publication assigned to the Rust core. The source-to-query account above follows this route, not a newly established second lifecycle. Verification distinguishes schema validation/retry from content audit and configured approval. Rejection preserves a feedback-bearing draft, but automatic initiation and termination of successive recompilations remain unspecified in the inspected passages. Delivery is proposed publication plus availability to later retrieval, not merely successful generation. None of these source-level contracts establishes exercised recovery or delivery.
