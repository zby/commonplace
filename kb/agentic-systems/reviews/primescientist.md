---
type: kb/types/note.md
description: "PrimeScientist's research-plan tree, retained rationale and diagnostics, with score-dependent inheritance and bounded budget/evaluator guarantees"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-primescientist-01
source-identity: https://github.com/Henri-XYu02/PrimeScientist
reviewed-revision: 29971beac6f4f4b41309b1326762e1b83ceece98
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-primescientist-01/result.md
analysis-result-sha256: 58b89868169553221ef6677c5b3e89034ae8411c58c244ab51a7966d6539dd66
---

# PrimeScientist

**Evidence basis:** source code, embedded prompts and README claims at commit `29971beac6f4f4b41309b1326762e1b83ceece98`, inspected 2026-09-25. No model execution or benchmark reproduction.

PrimeScientist searches over experimental plans. A reflector writes a plan, a coding agent executes it, a benchmark returns a score, and Python selects which branch to execute or expand next. Plans, hypotheses, diagnostics and parent workspaces persist across trials. The reviewed boundary includes tree search, its linear baseline, shipped AutoLab/FIRE-Bench adapters and Codex/evaluator interfaces. External model interiors and comprehensive benchmark validity are excluded: this is a complete artifact and a partial operational loop. See the [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-primescientist-01/result.md) — see-also: source register, route audit and mandatory memory/epistemic lenses.

## Search and execution

Budget-Adaptive Value Traversal samples branches using retained quality and prior estimates. As remaining logged token/time budget falls, its exponent increases and favors higher-valued branches more strongly. Evaluated nodes use Q; unvisited nodes use parent Q and a softened proposal prior. A node's Q includes backpropagated accepted-descendant rewards. It is therefore different from that node's own execution score, even though a child inherits that node's retained sandbox. The final “best” summary selects highest Q. [Tree implementation](https://github.com/Henri-XYu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/search/tree.py) — evidenced-by: RTE-2 and OBJ-3 in the exact result.

The executor stages a native Codex skill and copies either baseline or eligible parent code. AutoLab uses a compact incremental plan; FIRE uses a full updated experimental plan with change files. A configured repeated-run node keeps the maximum-scoring execution's artifacts. Low-scoring children can be hidden from traversal while their records survive; their scores do not reduce ancestor averages. Other retained scores do update the tree. [Search orchestration](https://github.com/Henri-XYu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/run_search.py) — evidenced-by: RTE-3 and RTE-4.

Budget checks occur around completed operations and depend on parsed usage estimates. They are not universal in-flight token or time caps. Reflector and verifier timeouts differ from task-agent calls; missing usage can leave no ledger entry. Execution permissions also vary: the reflector and AutoLab agent request unrestricted host execution, while FIRE supports host workspace restrictions or container modes. These interfaces do not establish one deployment-wide isolation guarantee.

## What persists and returns

The most explicit rationale artifact is `prior.json`: hypothesis, reasons, expected benefit and risks. Later reflectors are directed to consult it and diagnose outcomes using verifier evidence. Admission checks only that a plan file exists and that its prior estimate can be parsed or defaulted. They do not enforce grounded rationale, novelty, size limits or the prescribed plan-transformation procedure. [Reflector prompts and launcher](https://github.com/Henri-XYu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/search/reflector.py) — evidenced-by: RTE-5.

Memory includes more than plans: retained score statistics, log head/tail excerpts, filtered verifier diagnostics, failed-branch reminders and the linear baseline's last-ten-attempt history all affect later consumers. Pruned reminders receive special prompt delivery when all children have been pruned. The baseline normally has scores and keep/revert actions but empty prose summaries under the shipped adapters. Cross-task insight files can be imported and supplied, but the inspected search paths do not implement a closed automatic extraction/write-back loop. A saved reflector session identifier requests external resume; it does not reveal the resumed memory contents.

The memory profile consequently records per-task, online/staged trace learning at **wired** strength, including deterministic continuation summaries and numerical selection state. That classification does not establish scientific learning or improved capacity. Model-directed reads and native-skill activation remain **afforded**. Full representational form remains not determinable because inherited sandboxes can contain arbitrary experiment payloads. Faithful use of recalled material remains not determinable.

## Evaluation and warrant

AutoLab invokes task-specific correctness/performance verifiers. The inspected Gaussian-blur example checks a reference image and then computes a runtime reward; that supports a bounded task contract. FIRE extracts the agent's conclusion, uses a model to remove concrete numbers, methods and artifact details, and compares the resulting general claim with bundled expected conclusions through RAGChecker. That measures reference agreement under a model judgment, not independent verification that the scientific experiment was reproduced. [FIRE evaluator](https://github.com/Henri-XYu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/benchmarks/fire_bench/eval/RAGChecker/eval.py) and [conclusion extraction](https://github.com/Henri-XYu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/benchmarks/fire_bench/eval/RAGChecker/utils.py) — evidenced-by: RTE-4.

The source affords a substantive theory route: formulate competing hypotheses, retain reasons and compare expected effects with diagnostic evidence. Actual operative theory use, content-directed criticism and attributable future capacity remain **uninspected**, so conjectural learning is unestablished. A procedural self-improvement route for plans and task code is **wired**; observed improvement remains uninspected. Reflection on the system's own plans and failures is **afforded**, without an observed reflective theory-builder. [Conjectural learning](../../notes/definitions/conjectural-learning.md) and [reflective system](../../notes/definitions/reflective-system.md) — defined-in: these separate distinctions.

## Scope

The source establishes outer-loop control and persistent continuation mechanisms. It does not establish task-suite performance, exact model-weight identity, actual recalled-content activation or the scientific warrant of every retained explanation. The README's wider benchmark report is attributed rather than reproduced. Candidate-linked experiments, verified context use and controlled comparisons would resolve those limits.
