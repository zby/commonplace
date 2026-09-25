---
type: note
description: "AIDE2's nested harness-rewrite search, private grading and evolved context mechanisms, with documentary limits."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-aide2-01
source-identity: https://arxiv.org/abs/2609.26457
reviewed-revision: "sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-aide2-01/result.md
analysis-result-sha256: 79a52919eaf48fccaf3e2445c5c52a628ce1dd4076df6ba3840a10252d5dba15
---

# AIDE2

Evidence basis: [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457), captured 2026-09-24; doc-grounded analysis of the described two-loop improvement plane, without agent source or original run artifacts.

AIDE2 searches for better research-agent harnesses. An inner agent edits task code using public feedback. The outer agent rewrites the current research-agent code, grades each candidate on returned solutions' hidden task scores under fixed budgets, and retains the best agent. The aggregate private grade is visible to outer search, so further external benchmarks provide a separate generalization boundary.

The paper reports seven accepted rewrites in its main eight-day run and improved performance on four held-out benchmarks. The evolved AIDE85 changes both search allocation and context management: strategy-arm search replaces greedy expansion, bounded root/recent-candidate context replaces growing full history, and recurring error lines enter prompts when the bug rate reaches 15%. Accepted harness code persists across tasks; the exact storage and persistence of compact summaries are not established by the paper.

Several distinctions constrain interpretation. A robustness penalty reportedly never changed final candidate choice, so presence in the winning agent does not establish contribution. A reported patch also changes a held-out evaluator's failure handling; its independent admission and measurement-integrity boundary remain uninspected. Reduced reward hacking is reported for the evolved bundle, without identifying the responsible rewrite. The ignition experiment shows a discovered agent can drive further improvement but does not establish that it is a better self-improver than the human-engineered outer agent.

## Scope

The [exact retained analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-aide2-01/result.md) contains source anchors, route and authority records, both mandatory lenses and all fourteen memory-comparison axes. Self-improvement and reflection are claimed at the described harness-lineage boundary. Criticism-specific conjectural learning, exact model fixation, implementation enforcement and independently confirmed component effects remain unestablished. The reported outcomes support a bounded improvement finding; they do not establish accelerating self-improvement or a general guarantee against metric exploitation.
