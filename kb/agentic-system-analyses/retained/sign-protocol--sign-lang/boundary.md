---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SIGN's agent knowledge notation and deterministic toolchain at f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba, bounded before external model consumption."
run-id: AAS-2026-11-09-sign-lang-379ffbdd642c-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba"
analysis-cutoff: "2026-11-09"
evidence-tier: code-grounded
source:
  identity: https://github.com/sign-protocol/sign-lang
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sign-lang-a98eb4c6c701/related-systems/sign-protocol--sign-lang
  revision: "f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba"
  sha256: null
---

# sign-lang boundary

## Boundary and evidence

This run analyses SIGN as an agent-oriented knowledge contract: its notation, authored knowledge documents, validation and compilation gates, and source-coverage and change signals. It is in scope as a knowledge/context-engineering system, not as an enclosing agent runtime. The intended consumer is explicit in SRC-1, `README.md`:

> SIGN is the contract layer between a governed knowledge graph and the agents that consume it. It expresses structure, relationships, inference rules, constraints, clusters, and provenance in a form agents can reason over — not just retrieve from.
> --- `README.md`

The boundary is **complete artifact, partial loop**. The frozen repository provides the language and deterministic preparation/maintenance toolchain, but not an implemented enclosing model-consumption loop. The README's injection and `get_canon_doc(id)` snippets describe integration responsibilities; they are not a shipped provider client or retrieval service. The complete tracked tree was inspected, the CLI was traced into its modules, and the editor extension manifest was checked for additional execution entry points. The local `.agent/sign/` corpus is included as shipped knowledge and authoring rules, not silently excluded as a library caller. These checks establish the artifact boundary, not an end-to-end operational agent system (SRC-1, `README.md`, `validator/bin/sign.js`, `editor-support/vscode/package.json`, `.agent/sign/canon.source.json`).

The declared delivery split is:

> | **Layer 1 — Index** | Injected into every agent system prompt. ~400 tokens for a full corpus. Document identity, status, graph edges, one summary line per document. Orientation without rule text. |
> | **Layer 2 — Full document** | Retrieved on demand via `get_canon_doc(id)`. Agents only pay for documents they actually need. |
> --- `README.md`

Included executable responsibilities are source discovery and parsing; structural and bundle-level rules; compilation to persisted index, full bundle, manifest and checksum; repository-file coverage; Git-based drift; document-change classification; and the CLI's external-import delegation boundary. The compiler reads `.sign` sources, runs rules with strict link checking, selects active document identities, builds the index, passes through raw files contributing active documents for the full bundle, and writes four artifacts. This is not evidence that arbitrary Markdown in the README quick start is compiled by the inspected implementation (SRC-1, `validator/src/parse.js`, `validator/src/rules.js`, `validator/src/validate.js`, `validator/src/compile.js`). Its persisted artifact interface is directly visible:

> fs.writeFileSync(path.join(outputPath, 'canon-index.sign'),    finalIndex,                   'utf8');
> fs.writeFileSync(path.join(outputPath, 'canon-bundle.sign'),   bundleContent,                'utf8');
> fs.writeFileSync(path.join(outputPath, 'canon-manifest.json'), JSON.stringify(manifest, null, 2), 'utf8');
> fs.writeFileSync(path.join(outputPath, 'canon-bundle.sign.sha256'), sha256 + '\n',           'utf8');
> --- `validator/src/compile.js`

Maintenance signals remain distinct from a review workflow. The drift module itself states the split (SRC-1, `validator/src/drift.js`):

> // (no platform dependency); the platform layer turns these signals into review workflow.
> --- `validator/src/drift.js`

### Inspected coverage and remaining scope

This is not a whole-system coverage claim. All tracked paths at the pin remain available for later inspection under SRC-1; the initial reads below do not restrict that source to an allowlist.

| Paths | Treatment and role | Limit on conclusions |
|---|---|---|
| `README.md`, `validator/README.md`, `spec/skill-reference.md` | Inspected: declared knowledge contract, integration sketches, validator contract and authoring/governance instructions. | Documentation supplies intent, not proof of agent compliance or achieved token savings. |
| `validator/package.json`, `validator/bin/sign.js`, `validator/src/parse.js`, `validator/src/rules.js`, `validator/src/validate.js`, `validator/src/compile.js` | Inspected: installed CLI entry point through discovery, admission checks and output persistence. | Source supports implementation analysis, not successful execution. |
| `validator/src/coverage.js`, `validator/src/drift.js`, `validator/src/diff.js` | Inspected: file-tree coverage, Git changes, corpus comparison and emitted signals. | Does not establish external review completion or automatic knowledge repair. |
| `.agent/sign/canon.source.json`, `.agent/sign/src/SL-OVERVIEW.sign`, `.agent/sign/src/SL-ARCH.sign`, `.agent/sign/src/SL-DEPS.sign`, `.agent/sign/src/SL-STANDARDS.sign` | Inspected: local corpus location, four knowledge documents, architecture and authoring constraints. | Configuration and documents do not demonstrate a running loader or agent using this corpus. |
| `editor-support/vscode/package.json` | Inspected: declarative language, grammar and icon contributions. Other editor-support files remain available but uninspected. | No assessment of highlighting correctness or editor usability. |
| `.github/workflows/ci.yml`, `validator/package.json` | Inspected: CI dispatch and named Node test suites. `validator/test/` bodies remain uninspected. | No claim of passing tests or behavioral evaluation coverage. |
| `proposals/2026-07-codebase-canon-reinforcement.md` | Inspected as proposed design, including external compiler/platform references and unresolved decisions. | Does not establish those external implementations or ratification. |
| `spec/sign-v1.0.md`, `spec/sigil-reference.md`, `examples/`, `decisions/`, remaining `proposals/` | Tracked and available; not yet inspected. Included for later language/design analysis, not an access gap. | No initial claim of exhaustive specification fidelity, example validity or roadmap reconciliation. |
| Remaining root metadata and contribution/security files; `.github/` issue and PR templates | Deliberately excluded from functional analysis after tree enumeration. | No conclusions about project governance effectiveness, security process or licensing interpretation. |

External dependencies are Node.js (package engine requirement >=18), local filesystem access, Git for historical comparisons, and a separately discovered `@sign-tools/sign-ingest` process for `sign import`. The CLI's discovery/spawn/error behavior is included; that other package's internals and outputs are not frozen here. Likewise the external `sign-draft` skill copy and `ch-canon-tools`/platform work mentioned in the inspected documentation are not acquired sources. Their exclusion prevents conclusions about ingestion, model drafting, human landing, platform resolution or review orchestration beyond this repository's declared interfaces (SRC-1, `validator/package.json`, `validator/bin/sign.js`, `spec/skill-reference.md`, `proposals/2026-07-codebase-canon-reinforcement.md`).

The excluded enclosing application's model selection, prompt assembly in production, retrieval implementation, enforcement of semantic constraints, durable agent memory and feedback loop must not be attributed to this toolchain. No execution traces, provider calls, benchmarks or causal experiments were supplied or performed. README production-validation and efficiency statements remain attributed claims only. The frozen evidence is the Git repository at the full commit above, verified against checkout HEAD with a clean status; applicability ends at the run's 2026-11-09 cutoff. Overall evidence is code-grounded for the inspected toolchain, with doctrine/design evidence for intended agent use.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/sign-protocol/sign-lang` | f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sign-lang-a98eb4c6c701/related-systems/sign-protocol--sign-lang`. Implementation: CLI, all seven validator source modules, package and CI wiring, editor manifest. Doctrine/design: README, validator README, skill reference, all four `.agent/sign/src/` documents, corpus config, July codebase-canon proposal. Reported operation: README production-validation and token-efficiency assertions only. Initial file-by-file coverage is above. | Implementation: [CLI](https://github.com/sign-protocol/sign-lang/blob/f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba/validator/bin/sign.js), [compiler](https://github.com/sign-protocol/sign-lang/blob/f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba/validator/src/compile.js), [drift](https://github.com/sign-protocol/sign-lang/blob/f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba/validator/src/drift.js). Doctrine/design: [skill reference](https://github.com/sign-protocol/sign-lang/blob/f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba/spec/skill-reference.md), [local standards](https://github.com/sign-protocol/sign-lang/blob/f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba/.agent/sign/src/SL-STANDARDS.sign). Reported operation and delivery intent: [README](https://github.com/sign-protocol/sign-lang/blob/f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba/README.md). | No access failure within the acquired repository. External consumer/ingestion/platform implementations and inspectable production runs are outside this frozen source; prevents end-to-end efficacy, runtime enforcement and causal performance conclusions. Available but uninspected files are distinguished above, not treated as missing evidence. |
