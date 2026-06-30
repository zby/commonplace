# Case 03: adversarial loop writing filter

Target note: `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md`

## Frozen material

- [baseline-working-tree](./baseline-working-tree.md) — copied from the current working tree on 2026-06-16.

Snapshot hash:

```text
6bddeedeaeecbe3f8b900c7b5c172e9dccdefbd8b2e368295eb5a322cfa34947  baseline-working-tree.md
```

## Experiment log

### 2026-06-16: prune weak expansions

Instruction under test: [case 01 prune instruction](../case-01-llm-generation-relaxes-goals/instruction-prune-weak-expansions.md).

Report: [prune-weak-expansions-report](./prune-weak-expansions-report.md).

Result: strong fit.

What it found:

- It preserved the note's strongest claim: the writing-is-thinking filter can be relocated into an adversarial human-agent loop.
- It identified the central precision fix: the architecture cannot "force" human judgment; it can make the condition explicit, routed, and auditable.
- It treated corpus connection work as a valuable but under-integrated branch.
- It flagged the final "better thinking than the solo pen" payoff as an empirical bet rather than an established result.

Takeaway: the prune instruction works well on a cohesive note that still has a few overconfident branches. It did not attack the core claim; it narrowed the promises around it.

### 2026-06-16: split and rehome critique

Instruction under test: [case 01 split/rehome instruction](../case-01-llm-generation-relaxes-goals/instruction-split-rehome-critique.md).

Report: [split-rehome-critique-report](./split-rehome-critique-report.md).

Result: useful branch diagnosis.

What it found:

- It kept the reconstructed-filter mechanism as the main note.
- It identified corpus connection work as the only real rehoming candidate.
- It recommended deleting or narrowing the "no solo equivalent" and "better than the solo pen" claims.

Takeaway: the split/rehome instruction remains useful when there is only one branch. It does not force a large decomposition, but it names the branch cleanly enough that the applied edit can demote it to a secondary payoff.

### 2026-06-16: marginal-value redundancy gate

Gate under test: [case 02 marginal-value redundancy gate](../compression/marginal-value-redundancy.md).

Report: [marginal-value-redundancy-report](./marginal-value-redundancy-report.md).

Result: success.

The gate produced two WARN findings:

- the standalone corpus-connection paragraph consumes a full chunk on a second thesis;
- the closing paragraph repeats the division-of-labor condition and adds an unearned comparative payoff.

Takeaway: the new gate catches a different weakness from ordinary semantic review. The issue is not that either passage is false; it is that their current size and placement cost more context than their marginal contribution earns.

### 2026-06-16: no-DB compression bundle

Instruction under test: [run-compression-bundle-on-note](../run-compression-bundle-on-note.md).

Bundle under test: [compression](../compression/README.md).

Sub-agent report: [compression-bundle-review](./compression-bundle-review.md).

Result: stronger signal than the single-gate pass.

Gate results:

| Gate | Result | Main signal |
|---|---|---|
| `compression/core-claim-obscured` | INFO | The title and bold sentence expose the core claim, but the corpus-connection branch changes the remembered center of gravity. |
| `compression/branch-bloat` | WARN | The corpus-connection paragraph is a separate defense of agent-operated KB work and should be removed or rehomed. |
| `compression/detail-overhang` | WARN | The opening concession, architecture inventory, and Relevant Notes grounds carry more detail than needed. |
| `compression/marginal-value-redundancy` | WARN | The note restates the human/adversarial condition in several places; the condition can be carried by fewer chunks. |

Takeaway: the full compression bundle is more useful than the marginal-value gate alone. It preserves the earlier branch-bloat finding while also catching detail proportion and footer-grounding verbosity.

### 2026-06-16: applied workshop draft

Applied draft: [revised-from-prune-and-gate](./revised-from-prune-and-gate.md).

Result: promising local improvement.

Changes:

- compressed the frontmatter description;
- rewrote "architecture exists to force the condition" as "make the condition explicit, routed, and auditable";
- demoted corpus connection work from a separate proof branch to a secondary payoff;
- narrowed the final payoff from "produces better thinking than the solo pen" to a conditional bet about relocating the stall into review.

### 2026-06-16: applied compression-bundle draft

Applied draft: [revised-from-compression-bundle](./revised-from-compression-bundle.md).

Result: stronger compression than the prune/gate draft.

Changes relative to the baseline:

- compressed the opening concession to the minimum needed to establish Borretti's critique;
- removed the standalone corpus-connection paragraph and folded it into the competence-floor paragraph as a secondary payoff;
- shortened the architecture inventory while preserving the condition that judgment must remain human and adversarial;
- merged the separate failure section into the closing paragraph;
- shortened Relevant Notes grounds so they route rather than re-argue.

## Interim judgment

This case supports the current workshop hypothesis. The improved critique instructions and the marginal-value redundancy gate can improve a note that is already mostly cohesive by finding where interesting support has grown into a second thesis. For this target, the best review signal is not "split the note" but "keep the reconstructed-filter claim, demote corpus connection work, and narrow architecture guarantees."
