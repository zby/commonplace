# Confidence must be attributed, never a mark

Layer: assessment.

From the mark discipline in [`kb/types/tag-readme.md`](../../types/tag-readme.md) (ADR 026): a mark is a cache *recomputable from ground truth and validated by code*. A credence is not recomputable — a bare `confidence: 0.7` field would be exactly the "stale trusted cache is a trap" failure the mark rule forbids. Represent credences only as *attributed, sourced assessments* ("Analyst A's posterior: 70%") — claims about who-believes-what, not KB-blessed truth.

This is why bare confidence fields (`confidence: low-to-medium`, `extraction_confidence: high`) are rejected — see [rejected-candidates](./rejected-candidates.md).
