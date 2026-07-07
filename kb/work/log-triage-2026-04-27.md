# Log triage - 2026-04-27

Source: `kb/log.md`

Classification legend:

- `PROMOTE`: candidate standalone note.
- `FOLD`: useful smaller update to an existing note, source ingest, or survey.
- `KEEP`: real signal, but not ready for promotion.
- `STALE/RESOLVED`: already covered, superseded, or misleading against current KB state.

## Live Queue

- `KEEP` - control-plane abstractions across repository, prompt, and learning-architecture levels. Current KB has control-plane notes and transfer-condition notes, but not this cross-level transfer mechanism. Keep until it predicts concrete transfer failures.
- `PROMOTE` - content-type axis plus hierarchy/access axis for agent memory. The multi-agent-memory ingest explicitly proposes this, and no current note owns the two-axis model.
- `FOLD` - verification cost as a decomposition/delegation constraint. The automation-boundary note owns the broad principle; the bounded-context decomposition note should gain verifiability as a stopping condition from the delegation source.
- `PROMOTE` - indiscriminate context loading as a double failure: false salience from irrelevant material plus non-activation of relevant material. Existing activation and soft-degradation notes are adjacent but do not name the combined failure.
- `FOLD` - `kb/notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md` should move some quantitative grounding from footer links into body prose.
- `PROMOTE` - well-specified OOD benchmarks stripping shortcuts. SuperARC, EsoLang-Bench, Sudoku, and induction-bias sources converge on a mechanism not owned by one current note.
- `FOLD` - `kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md` should add SuperARC's integer-vs-binary sequence gap.
- `PROMOTE` - diagnostic richness as an outer-loop search axis. The trace-derived survey now mentions it, but a standalone note could own the axis and Meta-Harness ablation.
- `FOLD` - `kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md` should account for Meta-Harness-style automated trace comprehension in hard-oracle domains.
- `PROMOTE` - filesystem-native tool use as a distinct long-context strategy. The source ingest proposes this and the current notes only imply it.
- `KEEP` - codification lifecycle across when/what/how to commit. Interesting, but currently reads like a phase grouping more than a mechanism.
- `FOLD` - coordination infrastructure versus memory infrastructure. Tracecraft is best used as a worked example inside the coordination-guarantees note rather than as a new synthesis note.
- `FOLD` - decomposition-policy acquisition should be added to the orchestration design-space note. The Mismanaged Geniuses ingest explicitly recommends this.

## Stale Or Resolved

- Trajectory-to-improvement mechanisms by output substrate: resolved by `treat-continual-learning-as-substrate-coevolution.md`, `axes-of-artifact-analysis.md`, `memory-management-policy-is-learnable-but-oracle-dependent.md`, and the trace-derived learning survey.
- Shared mutable state without coordination primitives: resolved by `agent-orchestration-needs-coordination-guarantees-not-just.md` and `topology-isolation-and-verification-form-a-causal-chain-for-reliable.md`.
- Oracle-gated learning from interaction: stale as written because the KB no longer treats deploy-time learning as only artifact-side; substrate coevolution and axes notes cover weight/prose/symbolic classes.
- GSM-DC quantitative cost surface: resolved by `effective-context-is-task-relative-and-complexity-relative-not-a.md`, which deliberately keeps the claim qualitative rather than adopting a brittle formula.
- Memory forgetting/pruning policy as inspectability-learnability spectrum: resolved by the "inspectability-learnability spectrum" section in `memory-management-policy-is-learnable-but-oracle-dependent.md`.
- Comparative review missing budget-constrained forgetting: superseded by the memory-management-policy note; the old path `kb/notes/related-systems/agentic-memory-systems-comparative-review.md` is also obsolete. Current path is `kb/agent-memory-systems/agentic-memory-systems-comparative-review.md`.
- Psychology-to-agent transfer methodology: resolved by `kb/notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md`.
- Three-space note missing Youssef psychology frameworks: resolved by the new psychology-transfer note rather than by expanding the Tulving note.
- Trace-derived policy compilation pipelines across Pi Self-Learning, ClawVault, and Synapptic: resolved by `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md`.
- SuperARC print-statement example: folded into `kb/notes/reverse-compression-is-when-llm-output-expands-without-adding.md`.
