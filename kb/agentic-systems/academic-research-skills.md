---
description: "Academic Research Skills as a prompt-defined Claude Code research pipeline with narrow executable checks, host-dependent orchestration, protocol-only resume, and conflicting terminal gate rules"
type: kb/types/note.md
traits: [has-external-sources, has-implementation]
tags: [computational-model, context-engineering, evaluation, tool-loop]
---

# Academic Research Skills

**Evidence basis:** first-hand reading on 2026-09-03 of the
`Imbad0202/academic-research-skills` repository tree at commit
[`94436237`](https://github.com/Imbad0202/academic-research-skills/commit/94436237913091d4739870159d241660527e8338),
covering the plugin metadata, four skills, command and role prompts, hooks,
deterministic scripts and schemas, state and integrity protocols, alternate
entry paths, and architecture and control documentation. I did not operate the
plugin in Claude Code, call its external services, or inspect a real research
run.

This note is the compact projection of the retained replay result
[AAS-2026-09-03-academic-research-skills-02](../reports/retained/agentic-system-analysis-operability-replay-20260903/AAS-2026-09-03-academic-research-skills-02.md).
Use that result when exact run identity, source/register lineage, lens findings,
or acceptance evidence matters.

Academic Research Skills 3.21.1 is a Claude Code extension and prompt workflow,
not a complete agent runtime. The package exposes four skills, sixteen command
entries, thirty-nine role prompts, three plugin agents, and two hooks
([plugin metadata](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/.claude-plugin/plugin.json)).
Its `/ars-full` route declares a ten-stage progression from research design
through writing, integrity checks, review, revision, and finalization
([pipeline skill](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/SKILL.md#L101-L138)).
Claude Code remains the scheduler, context builder, model executor, tool
dispatcher, and permission boundary. The inspected artifact is therefore a
complete extension but only part of the material research loop.

The system's central architectural split is between a natural-language control
program and a narrower executable support layer. The pipeline skill and
orchestrator prompt choose stages, dispatch roles, request user decisions, and
interpret semantic findings. Python and shell code instead implement selected
operations with exact local semantics:

| Surface | What the artifact implements | What remains model-, host-, or participant-mediated |
|---|---|---|
| Pipeline progression | Skills, role prompts, state shapes, and declared transitions | Actual dispatch, context assembly, checkpoint compliance, retry, cancellation, and terminal consumption |
| Write confinement | A `PreToolUse` hook can deny Bucket A Bash calls and structured writes outside declared phase paths | Hook invocation and enforcement by Claude Code; unfenced roles and non-plugin channels |
| Citation checks | Resolver calls, exact outcome reduction, structured summaries, and a local SQLite cache | Whether metadata supports a manuscript claim and whether the orchestrator acts on the result |
| Review and package checks | Panel-arithmetic recomputation, schema/receipt validation, hashes, and named package predicates | Correctness of reviewer judgments, semantic preservation, and publication fitness |
| Material Passport | A detailed state schema, boundary-hash protocol, and resume instructions | The reset/resume transaction and context loader; no executable implementation was found |

This is the useful sense in which the system is “contract-audited.” Some
contracts are symbolic checks; others are instructions that the external host
and model must interpret. The implemented check establishes only its typed
target. For example, recomputing a panel decision can establish consistency
with submitted reviewer cards, not that the reviews are correct. Resolver
metadata can establish that a citation record exists in an index, not that it
supports the sentence that cites it
([citation gate](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/verification_gate/__init__.py#L192-L291)).

## Control depends on the route

The strongest control path is the installed Claude Code plugin. Its
`PreToolUse` hook runs a phase-aware write guard
([hook wiring](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/hooks/hooks.json),
[write guard](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/ars_write_scope_guard.py#L288-L438)).
Even there, confinement is conditional. The guard covers a named Bucket A role
set rather than every worker; it declares same-phase cross-skill and one
dual-phase union limitation; and its launcher passes the tool call through when
Python is missing, the guard times out, output is malformed, or the guard itself
fails
([launcher](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/hooks/run_guard.sh#L14-L28)).
The code therefore provides an enforcing decision for one healthy matched call,
not a fail-closed system-wide write boundary.

Direct single-skill modes bypass the full pipeline's acceptance sequence.
Skills-only copies, repository-clone installs, Cowork, Claude.ai Projects,
Claude Science, and the Pi adapter expose different combinations of hooks,
orchestration, delegation, and isolation
([control availability](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/docs/CONTROL_AVAILABILITY.md#L15-L100)).
The same output claim must therefore be qualified by entry mode, install
channel, enabled policy, and launcher health. Citation existence is advisory by
default; strict policy can emit a blocking marker, but the external orchestrator
must still consume it.

## Persistence is not one mechanism

The Material Passport is the intended cross-session state carrier. It names
artifact versions, verification status, pending decisions, hashes, and an
append-only reset/resume ledger. Its protocol requires an exact boundary hash,
rejects mismatch and double use, and describes a sidecar lock
([Passport protocol](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/references/passport_as_reset_boundary.md#L17-L125)).
But that document explicitly does not add runtime CLI tooling, and no Passport
writer, transaction, or context loader appears in the hooks, commands, scripts,
or Pi adapter. The `SessionStart` hook announces available commands and may add
an update reminder; it does not read the Passport or restore workflow state.
Passport resume is consequently a detailed participant protocol and affordance,
not a wired recovery path.

The citation-verification cache is different. Successful resolver outcomes are
written to SQLite and can replace later network calls under an exact
citation/resolver/query-form/version key and a ninety-day semantic TTL
([verification cache](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/verification_cache.py#L102-L276)).
That is executable read-back. It establishes neither that a cache hit reached a
model nor that it changed scholarly quality.

The fresh replay separated four other deterministic read-back routes. A
human-read ledger is recomputed at finalization and can promote, demote, or stop
a marker
([human-read resolver](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/human_read_attestation_resolver.py#L311-L413));
an inquiry ledger replays an exact Passport pointer at checkpoints
([inquiry ledger](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/inquiry_branch_ledger.py#L1129-L1190));
fresh update-check state may reach the `SessionStart` hook output
([update check](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/ars_update_check.sh#L92-L215));
and claim-standing artifacts can be replayed and freshness-checked
([freshness check](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/scripts/check_claim_standing_freshness.py#L102-L197)).
These consumers are wired in the tree, but host, model, provider, and human
activation remain uninspected. A human-read attestation is operational input,
not proof that reading occurred or that a claim is true. Static installed
prompts are retained instructions, not memory accumulated through use.

## Integrity is coverage-bounded

The integrity workflow usefully exposes denominators and unknowns for named
populations: registered claims, formal checks, sampled passages, citation
lookups, and package predicates. That prevents a checked subset from silently
presenting as an unqualified total. It does not establish that the claim
registry contains every substantive statement. Semantic claim extraction,
review, and synthesis remain model judgments, and no independently warranted
complete-population audit appears in the repository
([architecture](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/docs/ARCHITECTURE.md#L100-L112)).
`VERIFIED_ONLY` should therefore be read as a stage-output label for the named
checks, not as verification of every empirical claim, procedure, or data point.

The optional cross-model route adds another judgment source after explicit
per-session consent is requested. The transport validates request and receipt
shape, but its closed request schema carries no consent field or receipt; the
consent guarantee remains in the prompt/orchestrator layer. A different provider
also does not by itself establish independent errors or ground a judgment in
external evidence.

## Persistent failure has no single shipped transition

The frozen revision contradicts itself about a load-bearing recovery path. The
[pipeline skill](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/SKILL.md#L127-L136),
[state machine](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/references/pipeline_state_machine.md#L162-L176),
and architecture document permit up to three correction rounds followed by a
recorded user decision, including partially unverified continuation. The
[orchestrator prompt](https://github.com/Imbad0202/academic-research-skills/blob/94436237913091d4739870159d241660527e8338/academic-pipeline/agents/pipeline_orchestrator_agent.md#L490-L502)
says Stage 2.5 cannot be skipped or overridden and aborts Stage 4.5 after its
second failed check. No precedence rule resolves the conflict.

The shared behavior is narrower: PASS permits ordinary progression, and an
initial FAIL triggers correction and rechecking. The retry cap, override
availability, and final persistent-FAIL transition are not determinable from
this revision. That conflict is material because the system presents these as
mandatory integrity gates, not optional prose advice.

## Scope

This is a code-grounded artifact analysis, not an observed-run or causal
assessment. It does not establish that Claude Code supplied the declared
prompts, that workers followed them, that external services returned correct
records, that a human exercised the reserved decisions, or that any research
procedure, raw datum, result, or manuscript claim is authentic or reproducible.
A candidate-linked host trace could establish operation; an interventional
comparison would still be needed before attributing a quality effect to one
component.

---

Relevant Notes:

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — rests-on: supplies the responsibility split used to keep the plugin's prompts and scripts separate from Claude Code's scheduling, context, and execution duties.
- [Code complements the weight–prompt pair with independently executed symbolic operations](../notes/code-complements-weight-prompt-with-symbolic-operations.md) — rests-on: explains why the exact reducers, guards, and validators warrant stronger implementation claims than the surrounding prompt protocols.
- [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: separates the Passport and cache's persistence from context presence, behavioral uptake, and downstream benefit.
- [Runtime structure determines the control surfaces available to governance](../notes/runtime-structure-determines-governance-control-surfaces.md) — rests-on: explains why installation channel and host-exposed hooks determine which declared controls can actually enforce a decision.
