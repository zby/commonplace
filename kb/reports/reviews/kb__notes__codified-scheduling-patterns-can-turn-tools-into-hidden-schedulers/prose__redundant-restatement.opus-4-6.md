## WARN — one instance of overlapping enumeration

**Paragraph 5 vs. paragraph 6:** Both enumerate the same categories of scheduling decisions.

Paragraph 5: "A `run_feature_workflow` tool that decides **which subtask to run, which tool surface to expose, when to recurse, and when to stop**…"

Paragraph 6: "When codified policy needs to **choose the next subtask, alter the next tool surface, or manage retries and stopping conditions** across task boundaries…"

These two enumerations cover the same ground (subtask selection, tool-surface choice, retry/stop logic) to make the same point: tools embedding scheduling become hidden schedulers. Paragraph 5 makes the point via a concrete example; paragraph 6 re-enumerates the same decision categories to restate the architectural consequence.

**Severity: WARN** — both fill the same argumentative role (demonstrating that scheduling decisions in tools create hidden runtimes). The second enumeration could be collapsed into a back-reference: "When codified policy needs these decisions across task boundaries, a framework that exposes tools but not progression forces that control logic to masquerade as tool implementation."
