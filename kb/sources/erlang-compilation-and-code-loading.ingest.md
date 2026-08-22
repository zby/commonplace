---
description: "Official Erlang/OTP evidence that runtime definition change uses explicit current/old module versions, a qualified-call transition, bounded coexistence, and load-time activation checks"
source: https://www.erlang.org/doc/system/code_loading.html
captured: "2026-08-19"
capture: web-fetch
genre: technical-documentation
snapshot_sha256: a6a0711854629a3ca085a052271a4c040182f2963a92e68e0e55ca9aba5f7574
ingested: "2026-08-19"
type: kb/sources/types/ingest-report.md
domains: [erlang-otp, code-replacement, deployment-governance]
---

# Ingest: Compilation and Code Loading

## Classification

Official Erlang/OTP system documentation that specifies the runtime's code-loading and replacement semantics.
Author: Ericsson AB maintains the Erlang/OTP documentation; this is an authoritative description of the shipped runtime contract, not independent evidence about how often operators use it.

## Summary

Erlang can replace a module while the system is running, but the runtime does not blur that change into ordinary execution. It gives each loaded module explicit `current` and `old` versions, allows both to run concurrently, and switches a lingering process only when it makes a fully qualified call into the module. Loading a third version purges the old one and terminates processes still executing it. The page also describes an `on_load` activation check: new code becomes callable only if its hook returns `ok`, while existing current code remains available during the check. The result is a small, explicit runtime protocol for definition change; the companion [Release Handling documentation](https://www.erlang.org/doc/system/release_handling.html) adds the release-level deployment ceremony.

## Connections Found

This snapshot is the technical substrate behind [instantiation alone cannot model agent learning across sessions](../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md): a running process can cross from one definition version to another, but only through named version states and an explicit call path distinct from local continuation. It also supplies bounded routing evidence for [domain pricing routes an exception to idealization assessment but does not decide it](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md): code replacement is a marked runtime path, but this mechanism alone says nothing about whether the immutable-class idealization remains adequate for a declared use. The release-handling snapshot is the stronger governance-ritual attestation because it adds versioned plans, migration, rollback, and permanence.

## Extractable Value

1. **Definition versions are explicit runtime state.** A module has at most a current and an old code version; replacement changes their roles instead of silently mutating one undifferentiated definition. This gives the KB a precise mechanism behind the looser phrase "hot code swap." [quick-win]
2. **Crossing versions is a marked control transfer.** A process lingering in old code moves to current code through a fully qualified module call; ordinary local recursion can continue in the old version. The fence is therefore operational, not merely naming. [quick-win]
3. **Coexistence is bounded and has a destructive edge.** Loading a third instance purges the old version and terminates processes still in it. Runtime mutability does not imply unbounded simultaneous definitions or cost-free migration. [quick-win]
4. **Activation can fail without displacing working code.** An `on_load` hook must return `ok` before new code becomes current and callable; failure unloads it while prior current code remains available. This is a narrow pre-activation gate, separate from release-level state migration. [just-a-reference]

## Limitations (our opinion)

This page specifies runtime semantics, not operational prevalence, safety outcomes, or community practice. It establishes a marked code-version mechanism but cannot by itself show that live code replacement is rare, expensive, or exceptional enough for any particular idealization; those are adequacy questions the domain-pricing note keeps open. Its unit is an Erlang module, not an object-oriented class, so using it for the class/instance analogy depends on the narrower shared feature—governed definition change—rather than structural identity between modules and classes. It is also a point-in-time capture of Erlang/OTP 29.0.5.

## Recommended Next Action

In a later note-edit pass, add this snapshot as `evidenced-by` support for the current/old-version mechanism asserted in `kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md`.
