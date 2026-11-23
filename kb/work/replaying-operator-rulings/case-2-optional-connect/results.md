# Case 2 results: six reviewers chose the other accepted correction

Six independent single-turn `claude-opus-5-5` reviewers saw the three files at `8db5c7666`. Two fresh tool-free Opus scorers graded anonymized answers without the arm key. The [design](./design.md) specified one most important correction and predicted at least two full hits in each arm. Both predictions missed.

| Condition | Full | Partial | Miss |
|---|---:|---:|---:|
| No hint (a2, a4, a6) | 0 | 0 | 3 |
| Follow one ordinary use (a1, a3, a5) | 0 | 0 | 3 |

Both scorers gave all six M. None said that suggesting connect incurs no third invocation until connect actually runs. These were free proposals under a single-answer limit, not choices between supplied alternatives. Zero mentions do not establish that a worker would fail to recognize the correction if asked to compare workflows.

**An unplanned but checkable success:** all six independently challenged the installed-project path assumptions instead. For example, a2 says that global type specs and skill bodies are read from the installed package rather than copied into the consuming project, and explains why measuring project-local paths would give the wrong budget. This is not merely a plausible alternative answer: the historical agent already named this issue alongside optional connect (session line 300), the operator accepted the proposed work (301), and `git show c30982be0 -- tests/scenarios/write-a-note.md` confirms that the accepted patch corrected both. The agreement is on that specific distinction, not an endorsement of every incidental detail of every answer. It was not a preregistered hit and does not change the 0/6 result.

**Implication:** on this packet and budget, the ordinary-use hint did not change which issue took first place. The strongest lead for amplification is detecting *a cost estimate built from the wrong physical inputs*. Freeze that as a positive-control target on a fresh, analogous case before looking at new answers. To learn whether optional-connect was crowded out rather than unrecognizable, vary only the number of permitted corrections on this same packet in a separately authorized run. No follow-up was run.

Positive evidence: [a2, no hint](../positive-evidence/case2-paths-a2.txt); all six answers are retained as `case2-paths-*` for the unexpected installed-path correction, not as optional-connect hits. [Packet construction](./run.py). All eight calls completed on their first launch. Small purposive sample; no general model or hint effect is established.
