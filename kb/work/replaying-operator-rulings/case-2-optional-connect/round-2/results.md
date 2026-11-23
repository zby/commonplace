# Round 2: the optional-invocation correction surfaced in both arms

After correcting the historical scenario's installed-library paths, 2 of 6 fresh reviewers picked the target as their single most important correction (round 1: 0/6). Both fresh condition-blind scorers agreed on every grade. Eight single-turn claude-opus-5-5 calls completed, including the scorers. Only the scenario in the experimental packet was changed, not the live file.

| Condition | Round 1 full hits | Round 2 full | Partial | Miss |
|---|---:|---:|---:|---:|
| No hint | 0/3 | 1 (a4) | 0 | 2 (a1, a3) |
| Ordinary-use hint | 0/3 | 1 (a2) | 1 (a5) | 1 (a6) |

The two full answers separate write-only cost (forks 1 and 2) from the cost if someone actually invokes connect (also fork 3). The partial answer assigned broad discovery to connect rather than write, but did not say that connect need not run. Two other answers chose omitted source-grounding costs; one chose the notes/theory collection path. These are descriptions of what workers proposed, not new operator rulings.

The [prediction](./design.md) of at least two full hits per arm was too high. Removing the issue that had taken all six first places was followed by the other accepted correction surfacing, even without a hint. It was not the majority choice, and these small independent samples do not establish a hint effect, a reliable causal effect size, or what any round-1 worker had already noticed. No new hint or live procedure is justified by this round alone.

Agreed full hits: [a4, no hint](../../positive-evidence/case2-optional-a4.txt) and [a2, ordinary-use hint](../../positive-evidence/case2-optional-a2.txt). [Exact two-paragraph substitution](./run.py) · [round 1](../results.md).
