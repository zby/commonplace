---
description: "Qwenputer reports a compiled RISC-V executor and exact recurrent-state file storage, separating symbolic operations and persistent records from learned model weights."
source: https://divagr.com/blog/qwenputer
captured: "2026-10-30"
capture: trafilatura
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: dc357730e6a66c67fd327188a607dfe01cd582943449aa4a435fbc0333cb0587
ingested: "2026-10-30"
type: types/ingest-report.md
domains: [agent-memory, symbolic-execution, recurrent-state]
tags: [computational-model]
learning_claims: true
---

# Ingest: Qwenputer — a deterministic RISC-V CPU inside Qwen3.5

## Classification

A first-person engineering report describing an experimental implementation, its mechanism, benchmark results, and deployment limits. Author: Divyansh Agrawal, the project's creator, who links code and downloadable checkpoints. Those releases make inspection possible but do not independently corroborate the reported results.

## Summary

Qwenputer adds compiler-assigned circuit weights to Qwen3.5-4B while leaving its pretrained weights unchanged. The author describes exact RAM built from Gated DeltaNet recurrent state by fixing the forgetting gate and write strength to one and using one-hot addresses. An added 11-layer RISC-V CPU executes through decoded trace tokens; a host driver boots firmware and isolates those tokens from Qwen's layers. In this combined configuration, arithmetic accuracy reportedly approaches an external Python-tool baseline and exceeds base Qwen, but the comparisons do not isolate internal executor placement as the cause. An experimental branch adds named-file operations over recurrent state, with cross-chat persistence through explicit state save/load. Its reported memory results concern that particular file interface and test setup, not general memory reliability. The central contribution is an implementation case separating learned interpretation, compiled execution, and writable state inside one model-serving system, at substantial checkpoint-size and latency cost.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a boundary-case comparison for [Code complements the weight–prompt pair with independently executed symbolic operations](../theory/code-complements-weight-prompt-with-symbolic-operations.md): the model chooses a calculation, while compiled rules execute it within forward passes rather than in an external Python runtime. Physical placement inside a checkpoint does not make the CPU a learned arithmetic competence. The reported arithmetic comparisons establish usefulness of the combined configuration, not superiority of that placement.

It also supplies a concrete operation-profile comparison for [Explicit retention provides direct targets for selective revision](../theory/only-explicit-retention-is-durable-writable-and-addressable.md). Named put/append/get/list/delete operations and state reload provide reported writability, file-level targeting, and cross-chat persistence in numerical recurrent state. They do not establish selective revision of semantic commitments or governed record authority. This is a candidate implementation example for the existing distinction, not evidence that the current note requires an exclusivity claim to be overturned.

## Learning Claims (our opinion)

The CPU is compiled, not trained; pretrained Qwen weights remain fixed. The adaptation mechanism is instead writing text into recurrent-state files and later consuming it, including after a saved state is reloaded. That is a reported route to persistent deployment-time adaptation without parameter learning. Memory is not thereby an autonomous learning process.

Against the [theory builder](../theory/definitions/theory-builder.md) conditions, the file interface supplies localized text at named targets, though the article does not establish how finely individual commitments can be isolated within them. Consumption has limited outcome evidence from the changed-fact tests. Content-directed criticism is not demonstrated: updating a fact is not by itself a stated attempt to refute what a retained unit says. Iteration from retained criticism is likewise not demonstrated, even though storage persistence across chats is reported. File-level addressing is therefore weaker evidence than [addressable theory](../theory/definitions/addressable-theory.md) with inspectable and separately revisable assumptions.

Improved changed-fact answers suggest useful memory access under the reported tests, not established improvement through a criticism-and-revision loop or across unrelated problems. The fixed CPU, directory layout, and file-operation interface lie outside any demonstrated adaptation process. As in [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), successful use within those boundaries does not show that alternative memory representations or operation sets would be worse.

## Extractable Value

1. **Executor placement need not determine execution semantics.** The reported compiled CPU offers a concrete comparison for the existing symbolic-operation note: numerical weights can implement assigned transitions rather than learned interpretation. Arithmetic gains concern the full CPU-plus-model configuration; they do not establish an advantage over external execution. [quick-win]
2. **Assess memory by available operations and persistence paths.** Exact row writes, named-file CRUD, and explicit state save/load make the experimental store a useful test case for the existing retention note. The file-level mechanism matters more than the label “inside the model”; semantic selection and selective commitment revision remain separate tests. [deep-dive]
3. **Separate exact storage from faithful use.** The reported changed-fact result of 90% versus 30% for pasted old chats, and the separate comparison of 83.3% versus 78.9% for Python memory tools, are context-bound prompts for testing retrieval and use separately. They are not one common benchmark or evidence that internal storage generally beats external memory. [experiment]

## Limitations (our opinion)

This is a promising architectural direction, but the evidence is one creator's report, not an established practical capability. Treat the source as a reported implementation example for distinguishing execution semantics from physical placement, not as grounds for adopting in-model execution over external tools. The failure envelope, runtime portability, maintenance burden, and end-to-end cost in practical workflows remain unresolved.

This is the creator's account of one experimental system. Neither implementation nor benchmarks were independently inspected or executed for this ingest. The reported official RISC-V tests, 18 million error-free free-running instructions, and roughly 230,000 replayed output positions are finite checks, not proof of exactness under every program, precision regime, or runtime configuration.

The arithmetic comparisons vary access to a calculator or Python tool against the base model; they do not isolate the contributions of exact Gated DeltaNet RAM, the compiled CPU, the driver, or the familiar tool-call protocol. Python-tool performance is often similar or better, so the numbers do not justify a general accuracy advantage for internal execution. The memory percentages lack enough protocol, sample-size, and uncertainty detail to establish robust superiority. Exact byte access also leaves filename selection, stale-fact resolution, and faithful use of returned text unresolved.

“No external tool calls” does not mean no host support: RvChat loads firmware and keeps execution traces out of Qwen's layers, and plain `generate()` is insufficient. The reported checkpoint is 18.8 GB, the file store is bounded at about 512 files and 53,000 tokens, and CPU instructions cost multiple decoded tokens. Cross-chat persistence requires carrying saved state; it is not automatic permanence in learned parameters. These costs and dependencies materially narrow the case for replacing ordinary external execution or KB storage.

## Recommended Next Action

Investigate Qwenputer as a reported implementation example for [Code complements the weight–prompt pair with independently executed symbolic operations](../theory/code-complements-weight-prompt-with-symbolic-operations.md), prioritizing independent reproduction and matched comparisons with external execution before recommending practical adoption.
