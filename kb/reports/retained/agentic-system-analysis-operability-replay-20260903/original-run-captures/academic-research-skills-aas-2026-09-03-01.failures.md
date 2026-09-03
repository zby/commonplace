# Academic Research Skills analysis run failures

This is a replaceable diagnostic for `AAS-2026-09-03-academic-research-skills-01`.
It is not the canonical analysis, a publication decision, or unresolved protocol
state. Deleting it loses no authoritative result.

## Inputs and regeneration

- Producer: `.agents/skills/analyse-agentic-system/SKILL.md`
- Requested target: `https://github.com/Imbad0202/academic-research-skills`
- Frozen target: commit `94436237913091d4739870159d241660527e8338`
- Captured archive SHA-256:
  `e298af69dc06ffb6642e5a64141954f3b4169e793626db907bedb0decd22d08c`
- Recovered canonical response capture:
  `kb/reports/cache/agentic-system-analysis/AAS-2026-09-03-academic-research-skills-01.md`
- Operation: rerun `$analyse-agentic-system` against the frozen commit URL with
  response-only disposition, then request a cache record of run failures.

The source commit and the producer skill are authoritative. Operational failures
may not recur, so this record is useful as a run diagnostic rather than a
byte-reproducible derivation.

## Failures and recoveries

| Phase | Failure | Recovery | Effect on result |
|---|---|---|---|
| Source acquisition | Two shallow HTTPS `git clone` attempts, including the escalated retry, failed because Git attempted to obtain credentials for the public repository. | Resolved the immutable revision through the GitHub API and downloaded the commit-pinned codeload archive; recorded its byte size and SHA-256 before inspection. | No moving-head evidence entered the result. Git history and repository-local metadata outside the archive were unavailable, but neither was needed for the declared boundary. |
| Repository inspection | Broad searches produced truncated tool output, and one targeted search initially ran from the wrong source directory. | Re-ran narrower searches and line-bounded reads from the extracted commit root. | No known evidence loss. Final citations point to specific files and line spans in the frozen revision. |
| Parallel lens coordination | The first epistemic lens packet was already in flight when central inspection found a same-revision conflict in persistent-FAIL recovery rules. Its affected conclusions therefore depended on a superseded canonical register. | Issued a conflict-only correction packet with the revised register and accepted only the corrected affected records. | Unaffected lens work was retained. The exact exhausted-retry transition is reported as not determinable rather than silently choosing one source. |
| Deterministic validation | The first `commonplace-validate` call on the temporary response artifact returned success while reporting zero analysed text files. | Re-ran `commonplace-validate --full` on the exact artifact. It identified type `agentic-system-analysis-result` and passed frontmatter, title, filename, links, and schema with no warnings or failures. | The zero-subject result was not treated as validation evidence. The canonical artifact is clean under the full validator. |
| Output routing | The run initially treated the request as response-only because no exact file path was supplied, despite the preceding user message naming `kb/agentic-systems/` as the purpose of the new workflow. | Re-read the publication rule, treated the named collection as authorization to derive its conventional per-system path, read the collection and note contracts, and wrote the compact durable analysis before handoff. | The final run record distinguishes its response-only canonical result from the separately published collection analysis. Both were revalidated after the correction. |
| Canonical-result retention | After validation, the exact 302-line canonical Markdown report was emitted in the response and its temporary file was deleted. The compact collection analysis was saved, but the full report had no filesystem copy. | At the user's direction, recovered the exact stable report under `kb/reports/cache/agentic-system-analysis/AAS-2026-09-03-academic-research-skills-01.md` and checked it against the previously recorded line count, byte length, and SHA-256. | The report is now available locally, but only in ignored, replaceable cache storage. Changing the producer instructions so future runs retain it remains separate work. |
| Shared-worktree coordination | Unrelated untracked KB files appeared or changed during the run, with no ownership signal tying them to this task. | Kept the analysis in `/tmp`, wrote only this explicitly requested cache record, and left all unrelated paths untouched. | No source, conclusion, or repository artifact from the other work was incorporated. |

## Source-side integrity failure encountered

The frozen revision contains incompatible persistent-FAIL rules. The pipeline
skill, state machine, and architecture document permit up to three correction
rounds followed by a recorded user decision, including a partially unverified
continuation. The orchestrator prompt says the Stage 2.5 gate cannot be skipped
or overridden and aborts Stage 4.5 after its second failed check. No precedence
rule was found.

This is an analysed source conflict, not a tooling failure. The canonical result
therefore preserves only the common behavior: PASS permits ordinary progression,
and an initial FAIL triggers correction and rechecking. Retry exhaustion,
override availability, and the final transition are not determinable from this
revision.

## Deliberate non-actions

- No dynamic probe ran because it would not establish excluded host adherence or
  research quality without a separately designed, candidate-linked execution.
- The legacy agent-memory review workflow was not invoked because the target's
  primary offered work is academic research and writing, not memory or context
  delivery.
- The canonical run result's declared physical form remains response. Its exact
  stable block is now separately captured in ignored cache storage, while a
  compact durable analysis is published under `kb/agentic-systems/`. Neither
  cache file is an input to that durable analysis.
