# Structure × governance matrix (commonplace)

The runtimes-decompose note answers what a runtime is made of (structure). The governance axis answers how it's monitored and corrected. This matrix crosses the two axes for commonplace.

## Matrix

|  | Inform | Validate | Correct | Detect drift |
|---|---|---|---|---|
| **Scheduler** | Skill descriptions tell the harness which workflows exist; routing table in CLAUDE.md tells the agent which instruction to load for which task | — | — | — |
| **Context engine** | CLAUDE.md routing table; WRITING.md checklist; escalation boundaries that tell the agent when to load deeper guidance | `/validate` checks frontmatter, links, description quality, required sections | Fix-descriptions instruction rewrites description fields; fix-review-warnings rewrites flagged passages | Review target selector detects `note-changed` and `gate-changed` pairs by comparing note/gate SHAs against accepted baselines |
| **Execution substrate** | Search patterns in CLAUDE.md; `/connect` discovery reports; index notes as navigation hubs | `/validate` checks link health (do targets exist?); git diff for uncommitted state | Fix system edits note files; review system writes to SQLite DB | Git tracks all file changes; staleness detection compares git blob SHAs; review sweeps scan for stale pairs across the note corpus |

## What the empty cells show

The scheduler row is mostly empty. Commonplace has minimal scheduler governance — no validation of skill orchestration, no correction of control flow decisions, no drift detection for how sub-agents are composed. This is consistent with the KB's design: the harness (Claude Code / Codex) owns scheduling, so commonplace governs what it controls (content and substrate) rather than what the harness controls (execution flow).

The validate column for the scheduler is empty because there's no structural check on "did the agent decompose the task correctly." That's an inherently harder problem — validating scheduling decisions requires understanding intent, not just checking form.

## Observations

- **Governance density tracks authorship control.** The context engine and substrate rows are dense because commonplace authors the artifacts those components operate on (notes, instructions, frontmatter, file layout). The scheduler row is sparse because the harness owns scheduling.
- **Inform is the most uniformly populated operation.** Every structural component has informing mechanisms. This makes sense — informing is the cheapest governance operation (just make knowledge available) and the prerequisite for the others.
- **Validate and correct are layered.** `/validate` is deterministic (Level A in the text testing pyramid); review gates are LLM-judged (Level B); the fix system applies corrections from review findings. The layers correspond to cost and confidence: cheap certain checks first, expensive probabilistic checks second, corrections third.
- **Drift detection is SHA-based throughout.** Both the context engine (note content SHAs) and the substrate (git blob SHAs) use content-addressed comparison rather than timestamps or manual tracking. This is a design choice that fell out of using git as the versioning layer.
