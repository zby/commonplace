---
description: "Frozen protocol and provenance for the premise-cohort Luna replication"
type: kb/types/instruction.md
---

# Premise-cohort replication protocol

**Status:** frozen before scored dispatch on 2026-07-30T08:22:46.586751+00:00.

## Question and boundary

This run tests boundary reproducibility for the surviving legacy `grounds` premise cohort: when labels, production policy, candidate identifiers, and prior outcomes are withheld, do fresh Luna contexts describe the sampled source-to-target relationships as theoretical assertions depending for truth or applicability on the target proposition? It does not test vocabulary utility, formal spelling, reader use, authorability, or the truth of the prior ledger.

The experimental unit is one directed source-to-target tuple. The primary cohort is the finite sample of surviving manifest rows, not a claim about other models, collections, future links, or general link authoring.

## Rebaseline and frozen sample

The live manifest contains 374 rows, of which 292 are current `grounds` rows. The active-scope scanner found 292 `grounds` footer rows, all matching manifest tuples. Additions outside the manifest: 0; attrition/missing tuples: 0; duplicate tuples: 0; unsupported footer syntax: 0.

Frozen cohorts: primary=49, boundary-correction=8, prior-drift=5, negative-control=16; total=78. Primary selection is the first 49 ascending `SHA256("premise-primary-v1" + NUL + source + NUL + resolved_target)` digests. Controls are the first four ascending `SHA256("premise-control-v1" + NUL + source + NUL + resolved_target)` digests in each control disposition. Neutral IDs use a run-local salt and reveal no cohort or disposition.

The orchestrator-only mapping is [manifest.tsv](./manifest.tsv). Participants receive neither it nor the live disposition file.

## Ambient context and isolation

Repository revision at freeze: `e1bd481e66a301395f42cb4cc892a4ac6bcb8402`. Root governance, runbook, design instruction, and live-manifest SHA-256 digests are recorded in `ambient-context.json`. Scored participants run in fresh Codex CLI processes with no inherited conversation and a fixture root outside the checkout. Filesystem isolation is **not technically enforced** by the read-only sandbox: prompts restrict reads to named packet files and JSONL command traces are retained for audit. The fixture root contains only sanitized packets and stage-specific observations. Root AGENTS, system/developer instructions, tool descriptions, and installed skill descriptions remain ambient to the runtime. No participant is shown production contracts, the shared catalogue, live disposition, git history, another participant's output, or cohort names by design.

Requested model: `luna`. The direct alias is rejected by this ChatGPT-account CLI; the configured and verified model ID used for every scored pass is `gpt-5.6-luna`.

## Batch plan and prompts

Three observer passes use independent randomization seeds {'observer-1': 730101, 'observer-2': 730102, 'observer-3': 730103}; batches contain at most 26 cases. Every case appears once in each of three fresh observer contexts. Stage 2 uses a fresh mapper context for each corresponding frozen observation batch. Exact pass prompts are under `pass-prompts/`; base prompt texts are under `prompts/observer.md` and `prompts/mapper.md`. Packet content and transformations were frozen before any scored call.

## Scoring and gate

Each included case requires three valid observer records and three valid mapper records. Three identical classes are unanimous; two identical classes are a stable majority; three different classes are UNSTABLE. For the 49-row primary cohort, an adverse row is a stable majority other than C1 or an UNSTABLE result. The fixed gate is 0–4 adverse (survives), 5–9 (inconclusive; extend to the complete surviving baseline:P cohort), and 10 or more (reopens). If four or more of 16 negative controls receive a C1 majority, no “survives” conclusion is issued. Secondary cohorts never alter the primary denominator.

## Hash inventory and command

Prompt hashes at freeze: {"mapper-1-1": "ff548a419c236827f07eaee96242545e61797b14788fa1759fff0768511d15eb", "mapper-1-2": "c4f183b7a932d648114dbc4f19f9259535802cd8a23caa93d4b2b3f88ae356fd", "mapper-1-3": "11f760de70c9141c5c0a1f9f1119114cad36b80a750658c1588b2b9b6b189a87", "mapper-2-1": "f0486d1af852b8a27b022a654f2b0a6d3254b6725af5b9dcb3e92584874a98a8", "mapper-2-2": "6daa6296e15ee840c82e3ae22a1f386d101d411efae25f02ed01a7cbc55473e6", "mapper-2-3": "11326e81d001b9c18da78c67f148e4da7e64005689fa2f82b9872216cbbbfe98", "mapper-3-1": "6d838973cb851131000e48c92e7e11ab190a5ab9bf627886e1be42f5fe8712c3", "mapper-3-2": "206cf7495c6f6ac6831aa46196e1ddfd73957013493c5597648e6e6f587fa8b5", "mapper-3-3": "fe284ae3f3d8bf915e0a603ece59f814fcea69d1301ae4b3c1d34e4fb46a7490", "observer-1-1": "4bff0f49df0275b4457d451c0ba412f2507e2766e76a257f62f899b3a99a4849", "observer-1-2": "0d8768262713c5e1b84762a27256852f77b91500e231f1bc7b38b32bf18e81f7", "observer-1-3": "bec4cd67ca2ef487a11347bb3aa6c7673dbfa94c8d418ccae8db2ae40da28af8", "observer-2-1": "e8159a21a3e889e2b812e1accafda79e8564a51d2c0843e7e9067737bd23e6be", "observer-2-2": "34def7ed1a4a7dc7c9cddb106e39bedfe1c6ed953fa8e1e9c930eeab3cfb2285", "observer-2-3": "d0e77ce29b179954d1862c1c3764fb8a4479be861dfa348afb80d30bb422ee82", "observer-3-1": "ad043f460a902e6dbc3b347fa14e8e34124ef669b5f89618095defe359961c98", "observer-3-2": "2e0b90b06b03cd27b47cccd954ca524b856047998c4359b20f1ed5d8faf49224", "observer-3-3": "cfd91fd114a262f4c8b2853b33418c58d99b775113c409e3580e4fe80c9af92d"}. Packet hashes are in `packet-digests.tsv`. Exact scored command: `codex exec --ephemeral --sandbox read-only --skip-git-repo-check -C <fixture-root> -m gpt-5.6-luna --json '<pass prompt>'`; the outer orchestrator captures stdout/stderr and retains traces.

## Deviations

The only deviation is the CLI spelling of the model: `luna` is unsupported by the ChatGPT-account endpoint, while `gpt-5.6-luna` is accepted and reports the Luna model identity. No other model substitution is permitted. A malformed packet, unexplained rebaseline mismatch, missing model provenance, or unparseable scored surface stops the run and leaves failed outputs in place.
