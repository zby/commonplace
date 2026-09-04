# Writing conventions for kb/agentic-systems/

## Text contract

This collection covers external **agentic systems and harnesses as whole systems** — execution loops, orchestration APIs, sub-agent surfaces, scheduling, permissioning, and control — what each is built from and does. Analyses use Commonplace ontology to name comparable mechanisms while preserving the external system's native operation and evidence.

The quality goal is **fidelity + economy**: faithful to what the system actually does, in the minimum shared vocabulary needed to explain it. An analysis that misrepresents the analysed system or forces a mechanism into an ill-fitting Commonplace term is worse than none.

Memory and knowledge subsystems are carved out: they have their own collection, `kb/agent-memory-systems/`, with a full review methodology that runs largely automatically. This collection covers everything else about how agentic systems are built. If a memory-subsystem category here ever matures into its own methodology, it should follow the same path and split out.

## Structure

The collection root holds per-system and per-feature analyses plus navigation. No subdirectory structure yet — add one when a category accumulates enough artifacts to need its own conventions.

## Generated reviews

Every complete `analyse-agentic-system` run publishes one compact review in the
collection root. These files carry `generated-by: analyse-agentic-system`, the
producing `analysis-run`, a stable `source-identity`, and the
`reviewed-revision`. They are workflow-owned projections of a frozen analysis,
not hand-authored notes. Do not substantively hand-edit them. Correct the source
boundary or the shared review method, then rerun the skill and replace the
review from those inputs. Git history preserves earlier generated versions.
Publication cannot be waived per complete analysis. The workflow validates a
private candidate before replacing the review. If generation or validation
fails, the incumbent remains unchanged and a later run repeats the analysis.

This regeneration rule keeps system-specific judgment inside one declared
method. A human may change the method and request a new run, but may not tune one
published review independently and still present it as a generated review.
Unmarked per-system and per-feature analyses remain ordinary authored artifacts.

## Evidence basis

Open each analysis with a one-line **evidence basis**: what it is grounded in — docs, source code, papers, or first-hand operation of the system — and when that evidence was captured. There is no formal `source-tier` field yet; adopt one if the collection grows a comparison methodology.

## Ontology and local transfer

State the external mechanism in its own operational terms before applying a Commonplace concept. Explain why the concept fits and qualify partial or unresolved mappings. Commonplace chooses the analytical distinctions; it is not the comparison target, and a reader must be able to reject a mapping without losing the external-system account.

Current differences from Commonplace, borrowable ideas, and watch items are not part of the durable analysis. They depend on a current Commonplace baseline and interest brief. Produce them, when separately requested, as living transfer state under `kb/reports/state/agentic-system-transfer/`; never feed that scan back into the stable analysis or a public corpus comparison. Keep unresolved candidate judgments until disposition, then replace or delete the state report under its owning workflow.

## Title conventions

- **Descriptive coverage of one system or feature** — name the system (`claude-code-dynamic-workflows.md`).
- **Argumentative analyses** — analyses asserting a specific claim — use a claim-shaped title and the `title-as-claim` trait, following `kb/notes/COLLECTION.md` conventions.

## Outbound linking conventions

Organised per destination; label semantics in [link-vocabulary.md](../reference/link-vocabulary.md).

- **→ `kb/sources/`** — link the snapshots an analysis is grounded in. Labels: `derived-from`, `evidenced-by`, `see-also`.
- **→ `external`** — cite the source code, documents, papers, or first-hand records already used for the evidence basis; prefer version-pinned targets when available and do not prospect the open web. Labels: `evidenced-by`, `see-also`.
- **→ `kb/notes/`** — search when an analysis maps a system onto theory. Use `rests-on` when the theory explains the analysed design; use rare `is-evidence-for` when the observed system instead bears on the target claim. Promote a novel transferable claim to `kb/notes/` rather than author theory here. Labels: `rests-on`, `is-evidence-for` (rare), `see-also`.
- **→ `kb/agent-memory-systems/`** — when the analysed whole system has a memory, knowledge, or context-engineering subsystem reviewed there. Use `contains` from the whole-system analysis to the subsystem review; use `part-of` only from a subsystem-focused analysis back to the whole system. Labels: `part-of` / `contains`, `compares-with`, `see-also`.
- **→ `kb/reference/`** — scan when a design element has a direct Commonplace analogue. Labels: `see-also`.
- **→ `kb/instructions/`** — link a Commonplace procedure when the external system analysis directly maps onto an operating rule or workflow. Labels: `procedure`, `see-also`.

## Type eligibility

A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract. Frontmatter-free Markdown is implicit `text`.

## What does NOT belong here

- Memory, knowledge, and context-engineering subsystem reviews → `kb/agent-memory-systems/`
- Transferable claims about KB methodology or orchestration theory → `kb/notes/`
- Raw snapshots of external sources → `kb/sources/`
- Descriptions of the Commonplace system itself → `kb/reference/`
- Current Commonplace differences, borrowable ideas, and watch items → a selective transfer scan under `kb/reports/state/agentic-system-transfer/`
- Procedures and how-to guidance → `kb/instructions/`
- Work in progress → `kb/work/`
