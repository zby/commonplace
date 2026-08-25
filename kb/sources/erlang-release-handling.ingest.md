---
description: "Official Erlang/OTP attestation that live definition change is governed as deployment through versioned appup/relup plans, synchronized state migration, rollback, and explicit permanence"
source: https://www.erlang.org/doc/system/release_handling.html
captured: "2026-08-19"
capture: web-fetch
genre: technical-documentation
snapshot_sha256: a4a1c18c7d4575f917f40504d2a2009660ea34aa2207bee802f877a60e177e9a
ingested: "2026-08-19"
type: kb/sources/types/ingest-report.md
domains: [erlang-otp, release-engineering, deployment-governance]
---

# Ingest: Release Handling

## Classification

Official Erlang/OTP system documentation specifying the SASL release-upgrade and downgrade framework built on runtime code replacement.
Author: Ericsson AB maintains the Erlang/OTP documentation; it is authoritative for the framework's declared workflow and constraints, but not an independent empirical study of release-handling practice.

## Summary

OTP turns its runtime code-replacement capability into a versioned release procedure. Modified applications receive `.appup` files that map explicit prior versions to upgrade and downgrade instruction lists; `systools` compiles these into an ordered release-wide `relup`; and `release_handler` unpacks and installs the package on the running system. Simple functional-module changes may load directly, while state-format changes use synchronized replacement: find affected supervised processes, suspend them, invoke `code_change/3` through the system protocol to transform state and switch code, remove the old version, and resume. Installation is reversible and staged: failure can reboot into the old release, success still requires a separate `make_permanent` step before the new version becomes the reboot default. A runtime famous for hot swapping therefore treats nontrivial definition change as governed deployment, not as an ordinary execution step.

## Quotes

- **Source extract (verbatim):** This file describes how to upgrade and/or downgrade between the old and new version of the entire release.
  - **Source location:** “Release Handling Workflow,” Step 6 description of `relup`
- **Source extract (verbatim):** If a more complex change has been made, for example, a change to the format of the internal state of a `m:gen_server`, simple code replacement is not sufficient. Instead, it is necessary to: - Suspend the processes using the module (to avoid that they try to handle any requests before the code replacement is completed). - Ask them to transform the internal state format and switch to the new version of the module. - Remove the old version. - Resume the processes.
  - **Source location:** “Release Handling Instructions,” `update`
- **Source extract (verbatim):** If an error occurs during the installation, the system is rebooted using the old version of the release. If installation succeeds, the system is afterwards using the new version of the release, but if anything happens and the system is rebooted, it starts using the previous version again.
  - **Source location:** “Installing a Release,” post-install behavior
- **Source extract (verbatim):** To downgrade from `Vsn` to `FromVsn`, `install_release` must be called again:
  - **Source location:** “Installing a Release,” downgrade procedure

## Connections Found

This page is direct technical evidence for the change-as-deployment claim in [instantiation alone cannot model agent learning across sessions](../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md): the fence consists of versioned artifacts, ordered transitions, synchronized migration callbacks, rollback, and explicit commitment. It is also a concrete governance-ritual attestation for [domain pricing routes an exception to idealization assessment but does not decide it](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md). Its evidential role must remain the one that note now assigns to pricing: it routes the exception to assessment and blocks a purely post-hoc "edge case" label; it does not establish frequency, bounded consequences, or explanatory dominance. The companion [Code Loading snapshot](https://www.erlang.org/doc/system/code_loading.html) supplies the lower-level current/old module semantics on which this procedure operates.

## Extractable Value

1. **Hot swapping is wrapped in release engineering.** OTP divides the workflow between offline script/package generation and an online release handler, making live change consume precomputed, inspectable deployment artifacts. This is the strongest direct attestation for the requested governance-ritual signature. [quick-win]
2. **Upgrade intent is version-indexed and bidirectional.** Each `.appup` names the current application version, the versions it can upgrade from or downgrade to, and the instructions for each path; `relup` composes application plans into a release-wide ordered program. Definition change is stated as a transition between identified versions, not an unqualified rewrite. [quick-win]
3. **State migration is a synchronized protocol.** For advanced updates the handler suspends affected supervised processes, triggers `code_change/3`, removes old code, and resumes execution. The current documentation supports `code_change/3` specifically; it also names the coordinating `sys:change_code/4,5` calls, not a `code_change/2` callback. [quick-win]
4. **Acceptance and permanence are separate states.** A release can be unpacked, installed, tested while running, rolled back by reboot, and only later made permanent. This staged commitment prevents "the new code ran" from meaning "the new definition is now the durable default." [quick-win]
5. **The framework exposes mixed-version hazards rather than erasing them.** Non-affected processes continue, new processes can enter old code during an upgrade window, dependency order can be unsafe, and runtime/core upgrades may briefly mix new core applications with old application versions. OTP therefore recommends small, backwards-compatible steps. [just-a-reference]

## Limitations (our opinion)

This is a normative mechanism document, not evidence that Erlang operators commonly exercise the full workflow or that the ceremony is costly relative to ordinary deployments. Release handling is an OTP/SASL framework layered on the language's lower-level replacement feature, so it does not establish that every use of runtime code loading receives this governance. More importantly for the pricing argument, a ritual can govern an ordinary operation; `.appup`, `relup`, and `code_change/3` establish a marked process but do not decide whether definition change is rare, consequence-bounded, or subordinate to an immutable-definition first-order model. The page is also version-specific to Erlang/OTP 29.0.5 and summarizes `code_change/3` rather than reproducing each behaviour's complete callback contract.

## Recommended Next Action

In a later note-edit pass, add this snapshot as `evidenced-by` support for the governance-ritual example in `kb/notes/domain-pricing-routes-an-exception-to-idealization-assessment.md`.
