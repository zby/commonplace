# Workshop: analyse an agentic system

- **Immutable run key:** `kb/instructions/analyse-agentic-system/SKILL.md`
- **Current intended target:** `kb/instructions/analyse-agentic-system/SKILL.md`
- **Mode:** new write
- **Collection:** `kb/instructions/`
- **Type:** `kb/types/instruction.md`
- **Acceptance review:** required — the eventual instruction will route several analyses and replace a functioning review workflow

## Goal

Design one public procedure for analysing an external agentic system as a whole. The procedure should establish one source and evidence boundary, analyse the runtime, invoke memory/context analysis when retained material can shape a later invocation, invoke epistemic analysis when a material route handles truth-apt content or makes a knowledge-production claim, and synthesize the findings without collapsing the lenses.

Memory is an internal lens of agentic-system analysis. Its current separate collection is historical: it was the first external-system review methodology to mature. This workshop does not treat memory as a peer system category.

## Current state

The initial assembly is complete: operative precedents are preserved, modular source/runtime/memory baselines are written, and independent reconstruction, disposition, and instruction-skeleton passes agree on the ownership split. No orchestrator draft has been written yet. The next stage is to realize the skeleton, then cold-run the exact candidate across the four lens combinations before any promotion or collection migration.

## Known instruction inputs

The `known-instructions/` directory preserves or extracts procedures whose behavior is already understood well enough to use as workshop baselines:

- `current-memory-review-skill.md` — byte-for-byte snapshot of the functioning local review skill.
- `current-memory-analysis-contract.md` — byte-for-byte snapshot of the functioning memory review type contract, which currently carries much of the analysis procedure.
- `current-epistemic-analysis.md` — byte-for-byte snapshot of the accepted and cold-trialled epistemic instruction.
- `current-agentic-comparison-instruction.md` — byte-for-byte snapshot of a bounded whole-system comparison instruction that produced a substantive review, retained as precedent rather than a general contract.
- `prepare-code-grounded-source-baseline.md` — a new modular extraction of the functioning GitHub checkout, revision-pinning, and citation preparation steps.
- `analyse-agent-runtime-baseline.md` — a new, deliberately narrow baseline built from the established scheduler/context/external-state distinction and repeated agentic-system review practice. It is understood but not yet independently trialled as a general instruction.
- `analyse-memory-context-baseline.md` — a new modular extraction of the stable memory/context parts of the current review contract. It preserves current distinctions while removing collection placement, comparison-with-Commonplace, and publication concerns.

Exact snapshots are inputs, not proposed final structure. The three extracted baselines are executable workshop artifacts, not promoted instructions.

## Design boundary

Fixed for this workshop:

- one public entry point;
- one `kb/agentic-systems/` collection for whole-system analyses and applicable lenses;
- one shared source/revision/evidence pass per reviewed system;
- runtime analysis for every in-scope agentic system;
- explicit applicability dispositions for memory/context and epistemic lenses;
- memory/context analysis when retained material accumulated or changed through use can shape later behavior;
- epistemic analysis when a route produces, transforms, checks, accepts, or authorizes truth-apt content, or when the system makes a knowledge-production or warrant claim;
- evaluation-driven behavior or policy adaptation with no evidenced truth-apt object and no knowledge/warrant claim remains a runtime finding and does not independently trigger the epistemic lens; if another trigger applies, the epistemic lens includes that adaptation route;
- synthesis preserves lens-specific findings and evidence limits.

Not fixed yet:

- whether a published system analysis is one file or a per-system package;
- whether lens instructions remain internal sections of one skill or become separately invocable instructions;
- the final output schema and which controlled values deserve parser support;
- the migration sequence for the existing memory corpus and comparison matrix.

These are design questions, not permission to mechanically relocate or patch the current corpus.

## Inputs

- `kb/agentic-systems/COLLECTION.md`
- `kb/agentic-systems/README.md`
- representative whole-system analyses under `kb/agentic-systems/`
- `kb/agent-memory-systems/COLLECTION.md`
- `kb/agent-memory-systems/types/agent-memory-system-review.md`
- `kb/agent-memory-systems/types/agent-memory-system-review.schema.yaml`
- `kb/instructions/write-agent-memory-system-review/SKILL.md`
- `kb/agent-memory-systems/review-framework-design.md`
- `kb/instructions/analyse-external-system-epistemic-architecture.md`
- `kb/work/multistage-write-analyse-epistemic-architecture-20260820/`
- `kb/work/pi-agent-zerostack-comparison/review-instruction.md`
- `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md`
- `kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`
- `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md`
- `kb/notes/runtime-structure-determines-governance-control-surfaces.md`
- `kb/notes/definitions/behavioral-authority.md`
- `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `kb/instructions/COLLECTION.md`
- `kb/types/instruction.md`

## Checklist

- [x] `brief.md`
- [x] `reconstruction.md`
- [x] `claim-disposition.md`
- [x] `claim-skeleton.md`
- [ ] `draft.md`
- [ ] lens-routing trials
- [ ] `audit.md`
- [ ] `candidate.md`
- [ ] `acceptance.md`
- [ ] promotion
- [ ] collection/type/schema migration design
- [ ] corpus regeneration plan

## Human decisions and blockers

- The user fixed the collection relationship: memory belongs inside agentic systems; its separate collection is historical, not conceptual.
- The user authorized this workshop and asked it to contain instructions already understood or already functioning.
- No blocker prevents reconstructing the unified instruction. Publication shape and corpus migration remain downstream decisions and must not be silently chosen by an early draft.

## Pending handoffs

- Revise `kb/agentic-systems/COLLECTION.md` only after the instruction and output shape survive representative trials.
- Replace or retire the current memory review type, schema, skill, matrix discovery, and separate collection only through a source-regeneration migration; do not mechanically retrofit semantic classifications.
- Reconcile the current memory type/schema trace-learning drift (`trace-learning`/`### Trace-learning` in the type versus legacy `trace-derived`/`### Trace-derived learning` in the schema) before treating the schema as the durable lens contract.
- Decide durable paths for any independently invocable lens instructions after routing trials show whether separate operativity is useful.

## What closes this workshop

The unified instruction has passed cold trials on systems that exercise different lens combinations; the target agentic-systems collection/type design is explicit; and the memory corpus has a source-regeneration migration plan. Promotion and migration may occur in separate atomic runs, but their decisions must no longer be implicit.
