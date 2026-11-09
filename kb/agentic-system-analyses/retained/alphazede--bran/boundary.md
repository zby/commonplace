---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "BRAN's shipped repository context system and optional connected execution at commit 7bc428b2ccdfad38e05caa0c0cba2bb19041993a."
run-id: AAS-2026-11-08-bran-2be75f1c9e69-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "7bc428b2ccdfad38e05caa0c0cba2bb19041993a"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/alphazede/bran
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/bran-894749d0ce24/related-systems/alphazede--bran
  revision: "7bc428b2ccdfad38e05caa0c0cba2bb19041993a"
  sha256: null
---

# BRAN boundary

## Boundary and evidence

This run covers BRAN as shipped in the public repository, not merely its Rust library API. Its intended use is deterministic repository evidence selection and bounded context delivery to agents, with optional connected model execution. The primary class is **memory/knowledge/context-engineering system**: offline retrieval and packet assembly are first-class operations; model calls are not a prerequisite for that classification. Optional runtime coordination is included, but BRAN is not classified here as the enclosing agent that decides and implements an outer task. SRC-1, `README.md`, `skill/use-bran/SKILL.md`, `crates/bran-cli/src/main.rs`.

> BRAN locates and cites repository evidence. It does not decide or implement the
> outer task; the outer agent owns all decisions and changes.
> --- `skill/use-bran/SKILL.md`

The boundary kind is **whole-system** for this shipped context system. It includes the CLI and terminal driver, library components, document admission, repository policy, shipped agent instructions, retention and later consumption of query evidence and connected results, maintenance, export, deployment wrappers, and source-defined evaluators. Same-repository callers are included rather than treated as external hosts. The workspace declares the CLI, core, document, TUI, and release packager together. SRC-1, `Cargo.toml`, `crates/bran-cli/Cargo.toml`, `crates/bran-cli/src/main.rs`.

### Entry-point and state-loop coverage

Initial implementation inspection traced these shipped paths, rather than inferring a whole-system boundary from the repository name:

- The `bran` binary enters `main`, dispatches through `CliApp::run_inner`, and invokes a terminal driver for interactive `tui`. Query scans the root, creates graph input, ranks sources, compiles a view, expands evidence dependencies, and emits selected sources. Packet repeats that production chain with bounded packet assembly and optional SQZ evaluation. SRC-1, `crates/bran-cli/Cargo.toml`, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/scan/mod.rs`.
- Query's `--record` path persists evidence, and the evidence-summary and proposal paths load those records and compare them with repository evidence; replay evaluation rebuilds query evidence from live roots. This is a shipped feedback path, not just a hypothetical library consumer. It remains inside the boundary. SRC-1, `crates/bran-cli/src/main.rs`.
- TUI Apply writes `.bran/settings.conf`; subsequent packet and connected invocations load project settings. Connected headless execution constructs a grounded repository request, invokes `AgentRuntime` through configured ports, and opens the filesystem result store. `get` opens that store and decodes retained results. These persistence and consumption responsibilities belong to BRAN. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-tui/src/lib.rs`.
- Document evidence discovery calls the format adapter and admission layer, then ranks admitted anchors and attaches digest, fidelity, and locator data to query/packet results. Native document parsers and their conformance tests are included, not excluded as unrelated utilities. SRC-1, `crates/bran-cli/src/document_evidence.rs`, `crates/bran-document/src/admit.rs`.
- Maintenance is a shipped CLI path through `RepairCoordinator`, proposal digests, explicit authority, and revalidation. The inspected CLI validator requires a fixture-authority marker; merely seeing a maintenance command does not establish unrestricted production self-repair. Derived-state and database modules are included library surfaces, whose actual consumers and wiring must be distinguished from their available APIs. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/derived_state.rs`, `crates/bran-core/src/database/mod.rs`.
- The shipped agent skill directs an outer agent to consume packet/query evidence and continue its own task. The Obsidian example exercises export and reparse. The headless guide includes propose/apply/revalidate instructions. These prompts, instructions, and examples are part of the system's consumption and maintenance surfaces. SRC-1, `skill/use-bran/SKILL.md`, `docs/integrations/agent-setup.md`, `examples/obsidian/usage.rs`, `examples/headless/README.md`.
- CI definitions invoke source-defined contract checks and Rust tests; benchmarks exercise controlled scanner, graph, and packet workloads. They are inspectable evaluators, not observed successful executions in this run. SRC-1, `.github/workflows/bran-fast.yml`, `tools/ci/check.sh`, `benches/context_packet.rs`.

The persistence boundary is explicit in shipped source configuration:

> # BRAN's policy is source; everything else below .bran is local runtime state.
> --- `.branignore`

The connected result-store access root is visible in implementation:

> let state = root.join(".bran");
> checked_directory(&state)?;
> let directory = state.join("results");
> checked_directory(&directory)?;
> --- `crates/bran-cli/src/main.rs`

### Top-level tracked coverage

All rows refer to SRC-1 at the frozen commit. “Included” sets functional scope; it does not mean every implementation statement has already been audited. Initial reads and tree inventory are distinguished below. Available internals awaiting detailed analysis are not access gaps.

| Top-level tracked file or directory | Classification and material paths | Initial inspection / role and limits |
|---|---|---|
| `.bran-export.json` | Included: public-export manifest | Read manifest header and initial entries. Export provenance is attributed metadata, not verification of the private source repository. |
| `.bran/` | Included: `.bran/policy.yaml` | Read repository metadata requirements, coverage declarations, and public-boundary policy. Runtime state is not present as tracked contents. |
| `.branignore` | Included | Read scanner exclusion for local state. |
| `.github/` | Included: `workflows/bran-fast.yml`, `workflows/release.yml`; issue templates and Dependabot configuration are auxiliary | Read fast-workflow entry into CI. Release workflow and auxiliary files inventoried, not yet audited; no claim of successful release execution. |
| `.gitignore` | Included | Read distinction between retained policy and ignored runtime/build state. |
| `CHANGELOG.md` | Included: version history | Inventoried, not yet inspected; no historical performance or behavior conclusion from its presence. |
| `CODE_OF_CONDUCT.md` | Excluded: contributor conduct | Deliberate administrative exclusion; no conclusion about community governance or enforcement. |
| `CONTRIBUTING.md` | Included: build and contribution instructions | Inventoried; detailed contributor workflow not yet inspected. |
| `Cargo.lock` | Included: dependency pinning | Inventoried; dependency internals and supply-chain integrity not established. |
| `Cargo.toml` | Included: workspace members | Read workspace membership to find shipped callers. |
| `LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT` | Excluded: legal texts | Deliberate legal exclusion; no legal compliance assessment. |
| `README.md` | Included: product intent, commands, connected setup, release and integration guidance | Read completely as doctrine/design, not as proof of advertised effectiveness. |
| `SECURITY.md` | Included: security reporting instructions | Inventoried, not yet inspected; no vulnerability-response assessment. |
| `assets/` | Included: `tui/raven-*.txt`, TUI and brand provenance, brand image | Inventoried; TUI library references were read. Decorative bytes are not mechanism evidence and have not been inspected. |
| `benches/` | Included: `context_packet.rs`, `knowledge_graph.rs`, `repository_scan.rs` | Read controlled packet benchmark setup; other benchmark internals await analysis. No measurements were run. |
| `crates/` | Included: `bran-cli/src/main.rs`, `document_evidence.rs`, source revision and SCIP helpers; `bran-core/src/scan/`, metadata/frontmatter, graph/query/view/packet, adapters/provider/SQZ, agent coordination/receipts/results, repair/derived state, database, export, policy/profile/schema/bundle/migration; `bran-document/src/` parsers/admission/conformance; `bran-tui/src/` domain/settings/render/diagnostics; crate tests and manifests | Entry-point and loop traces above were inspected in bounded ranges, including CLI producers, persistence, consumers and maintenance, scanner, runtime coordination, document admission and TUI exports. The tree supplies additional included internals and tests for later detailed inspection; these are not omitted functional paths. |
| `deny.toml` | Included: dependency-policy configuration | Inventoried; policy contents not yet inspected. |
| `deploy/` | Included: `systemd/bran-check@.service`, `oci/build_image.py` | Read complete systemd unit and OCI builder configuration. They ship registered-root CLI wrappers; they do not supply an observed running service. |
| `docs/` | Included: `integrations/agent-setup.md`, `deployment-profile.md`, `database-boundary.md`, enterprise-document adapter, conformance, dependency and evidence-envelope documents | Read agent setup completely and initial deployment/database contracts. Other documents inventoried, available for analysis. Design and implementation must remain distinct. |
| `examples/` | Included: `headless/README.md`, `obsidian/usage.rs` | Read completely. Shipped consumption and maintenance guidance, not excluded enclosing applications. |
| `fixtures/` | Included: conformance/policy, scanner/graph/view/packet/query/symbol/source-metadata, repair/derived-state/database, enterprise-document, Google-attestation, public-boundary, release and Obsidian fixtures | Inventoried evaluator inputs; no fixture executions or outcome claims. Recorded Google artifacts remain attributed fixture evidence until their conditions are inspected. |
| `schemas/` | Included: repository/profile/release, graph/view/packet/scan/metadata/symbol, OKF bundle, document-envelope, Google-attestation and SQZ schemas | Inventoried contracts; schema internals not yet inspected. A schema's presence does not establish runtime enforcement. |
| `skill/` | Included: `use-bran/SKILL.md` | Read completely. This is the shipped outer-agent evidence-consumption instruction. |
| `tools/` | Included: `ci/check.sh`, contract/security/export/deployment/release/attestation checks, release construction/sealing and test-budget tooling | Read CI dispatcher through its performance gate; remaining internals inventoried. Evaluator source is included without treating CI as a successful observed run. |
| `xtask/` | Included: `Cargo.toml`, `src/main.rs`, `src/archive.rs` | Read packager entry and build path; archive internals inventoried, not yet inspected. No produced binary or archive was tested. |

### External responsibilities and evidence limits

The immutable evidence boundary is the public Git repository at `7bc428b2ccdfad38e05caa0c0cba2bb19041993a`, with an applicability cutoff of **2026-11-08**. The acquired checkout's HEAD was checked against that full commit. The access path is not a second source identity. All tracked files at this revision remain eligible for later source inspection under SRC-1, including included paths not yet inspected in detail.

The overall evidence tier is **code-grounded**. Initial reads establish inspectable producers, admission, retention, consumers and shipped drivers. Product documentation supplies doctrine/design. No target code, examples, tests, benchmarks, model calls, or services were executed for this boundary. Source-defined checks therefore support an account of intended verification, not measured retrieval quality, operational reliability, token savings, or causal superiority.

External responsibilities are excluded as follows:

- **Outer agent hosts and model providers:** BRAN's configured-host integration and runtime ports are included; the external executable's implementation, provider execution, credential store and enclosing task loop are not supplied. This prevents conclusions about the external host's actual tool enforcement, model reasoning quality, credential safety or completion of outer tasks. Requested capabilities must not be treated as attested effective ones. SRC-1, `docs/integrations/agent-setup.md`, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs`.
- **External SQZ implementation:** BRAN's packet/agent SQZ adapters and receipts are included, but an independently configured compressor is not frozen here. This prevents conclusions about its actual compression, fidelity or model behavior. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs`.
- **SCIP producers and external repositories:** BRAN's existing-index consumer is included, not a SCIP indexer's implementation or a user's indexed repository. This prevents conclusions about index-generation correctness or real repository freshness. SRC-1, `docs/integrations/agent-setup.md`.
- **Deployment infrastructure:** the shipped systemd unit, OCI builder and registered-root CLI are included; SSH, job runners, real container bases, mounted repositories and live systemd enforcement are not observed. This prevents claims about a deployed service or real isolation effectiveness. The deployment document explicitly distinguishes remote CLI from a future service. SRC-1, `deploy/systemd/bran-check@.service`, `deploy/oci/build_image.py`, `docs/deployment-profile.md`.
- **External specifications, databases and cloud services:** in-repository schema, adapter, database and attestation contracts are included; linked upstream OKF, database engines, Google services and their operational accounts are not separately frozen sources. Their live conformance and behavior cannot be established from links or fixtures alone. SRC-1, `README.md`, `docs/database-boundary.md`, `tools/ci/check.sh`.
- **Private development history:** the export manifest identifies a private source origin, but only this public revision is frozen. Unexported code or private review history is unavailable, preventing conclusions about that larger development system. SRC-1, `.bran-export.json`.

There is no identified unavailable material shipped path that prevents inspection of BRAN's own context-system loop. The external gaps above limit operational conclusions; they do not turn BRAN's complete shipped artifact into an analysis of only its library subsystem.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/alphazede/bran` | 7bc428b2ccdfad38e05caa0c0cba2bb19041993a | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/bran-894749d0ce24/related-systems/alphazede--bran`. Implementation: tracked tree, workspace and CLI/core manifests; bounded ranges of `crates/bran-cli/src/main.rs` covering dispatch, query, packet, TUI settings, repair, query-evidence persistence/summary/replay, grounding, result storage/get and connected invocation; `crates/bran-cli/src/document_evidence.rs`; scanner, core exports, derived-state/database module entries, agent coordinator, connected adapter, document admission and TUI exports; packet benchmark setup; CI dispatcher and fast workflow; OCI configuration, systemd unit, packager entry, Obsidian example, policy/ignore/export-manifest setup. Doctrine/design: complete `README.md`, `docs/integrations/agent-setup.md`, `skill/use-bran/SKILL.md`, `examples/headless/README.md`; opening deployment/database sections. Detailed per-path coverage and not-yet-inspected areas are recorded above. | Implementation: [CLI](https://github.com/alphazede/bran/blob/7bc428b2ccdfad38e05caa0c0cba2bb19041993a/crates/bran-cli/src/main.rs), [document admission](https://github.com/alphazede/bran/blob/7bc428b2ccdfad38e05caa0c0cba2bb19041993a/crates/bran-document/src/admit.rs), [runtime coordination](https://github.com/alphazede/bran/blob/7bc428b2ccdfad38e05caa0c0cba2bb19041993a/crates/bran-core/src/agent/coordinator.rs), [CI gates](https://github.com/alphazede/bran/blob/7bc428b2ccdfad38e05caa0c0cba2bb19041993a/tools/ci/check.sh). Doctrine/design: [README](https://github.com/alphazede/bran/blob/7bc428b2ccdfad38e05caa0c0cba2bb19041993a/README.md), [agent skill](https://github.com/alphazede/bran/blob/7bc428b2ccdfad38e05caa0c0cba2bb19041993a/skill/use-bran/SKILL.md), [agent setup](https://github.com/alphazede/bran/blob/7bc428b2ccdfad38e05caa0c0cba2bb19041993a/docs/integrations/agent-setup.md). | No identified checkout access gap. External hosts/providers/compressors, live services and private development source are outside the frozen source; their effectiveness and enforcement are not established. No observed run or causal experiment is registered. |
