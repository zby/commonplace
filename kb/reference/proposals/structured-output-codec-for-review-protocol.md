---
description: "Proposal: make review output a pluggable codec, with sentinel markdown today and schema-validated structured output when harnesses expose it"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Structured-output codec for the review protocol

The review protocol's output side is one encoding: sentinel-delimited markdown blocks parsed by a hand-written state machine, with the decision recovered from a strict final result footer. Harnesses are starting to offer schema-validated structured output for sub-agent calls — Claude Code's dynamic workflows `agent(prompt, {schema})` forces a validated structured-output tool call and returns a parsed object, with validation retried at the tool-call layer. If that capability generalizes across harnesses, the remaining free-text failure classes disappear at the source. This proposal holds the design for making the output encoding a codec choice rather than a protocol property.

## Current state (as of 2026-07-01)

- One encoding: `=== PAIR REVIEW START: {note} :: {gate} ===` blocks ([ADR 029](../adr/029-review-execution-unified-on-note-gate-pairs.md)). `protocol/parser.py` extracts blocks into `ParsedPairBundle`; `protocol/decisions.py` requires exactly one final `## Result: PASS|WARN|FAIL|ERROR` line and canonicalizes result footers.
- The codec is contained in `protocol/` plus finalization/artifact rendering.
- Consumers downstream of parsing are mostly encoding-independent already: `review_pairs.decision` stores the parsed enum, a derived result artifact path points to the retained markdown review body, and `warn_selector` extracts findings from a `### Findings` section convention in that artifact.
- External executors receive the contract through rendered prompts created from selector JSON (`commonplace-create-review-jobs --input ... --grouping {note,gate}`), write job-owned output files, and return control to finalization.
- Trigger not yet met: schema-validated sub-agent output ships in one harness's workflow scripts; the subprocess CLIs (`claude -p`, `codex exec`) and the live-agent file-artifact path have no equivalent surface the review system could consume today.

## The design

A codec is the pair (render the output contract into the prompt, decode raw output into `ParsedPairBundle`). Two codecs:

- **markdown-sentinel** (today): contract rendered as sentinel instructions plus a block template; decoder is the existing parser + decision chain.
- **structured** (new): contract expressed as a JSON schema — per pair: note path, gate id, summary, findings (severity + text), optional suggested revision, decision as an enum. The decoder validates and maps to `ParsedPairBundle`; the decision fallback chain is bypassed entirely because the decision arrives as a constrained field. The per-pair markdown result file can be rendered from the structured fields, so warning extraction and human review still use the derived result artifact boundary.

`ParsedPairBundle` is already the codec-independent boundary type. Missing pairs and structural errors both translate to failed live finalization under the all-or-nothing policy; a structured decoder should still distinguish them so callers can report the cause.

## Free choices

- **Where codec selection lives.** A flag on prepare/ingest commands chosen by the orchestrator (it knows whether its harness supports schemas), a per-runner-adapter property, or a project-level default. The orchestrator-chooses option matches the medium-pluggability direction of ADR 030.
- **Schema shape for findings.** Mirror the current markdown sections one-to-one (summary/findings/revision) or take the opportunity to constrain severity to an enum and findings to a list — more validation power, but historical rationale text and the new format diverge in expressiveness.
- **Canonical retained form.** Keep the markdown result file as the single retained review-body representation (structured output rendered to markdown on ingest), or add a new structured artifact alongside it. The first keeps one read path; the second preserves machine-readable findings for the gate-statistics ambitions in [gate learning from accepted edits](./gate-learning-from-accepted-edits.md).
- **Whether the markdown codec ever retires.** Free-text markdown is the lowest common denominator every harness supports; retiring it would couple the review system to schema-capable harnesses.

## Adoption criteria

Adopt when a harness medium the project actually uses for reviews exposes schema-validated output at a surface the system can consume (a workflow orchestrating review batches, or a subprocess CLI flag). Adopting earlier buys nothing: the markdown codec must stay regardless, and the structured decoder cannot be integration-tested without the capability.

## Risks

- Two codecs mean two prompt contracts to keep semantically aligned; the codec interface must own both sides (render + decode) so a contract change cannot touch one encoding only.
- Schema validation failures look terminal but may be retryable at the harness layer; the decoder should distinguish "harness delivered invalid object" from "model omitted a pair" for diagnostics even though both fail live finalization.
- Findings-as-enum tightens what reviewers can express; the markdown codec's prose findings have carried nuance (multi-severity bullets, inline suggested rewrites) that a first schema draft may flatten.

---

Relevant Notes:

- [Claude Code dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md) — derived-from: the schema-validated `agent()` option whose generalization is this proposal's trigger
- [029-review execution unified on (note, gate) pairs](../adr/029-review-execution-unified-on-note-gate-pairs.md) — see-also: established the single grammar and `ParsedPairBundle` boundary a second codec would plug into
- [030-harness-facing seams: batch endpoints and runner adapters](../adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — see-also: the medium-pluggability seams codec selection would ride on
- [gate learning from accepted edits](./gate-learning-from-accepted-edits.md) — see-also: per-gate statistics would benefit from machine-readable findings, one of the free choices here
