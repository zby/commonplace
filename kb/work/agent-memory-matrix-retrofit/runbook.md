# Agent-memory matrix retrofit — orchestrator runbook

Retrofit every **code-reviewed** agent-memory-system review to the faithful
one-hot lead-token format, so `kb/agent-memory-systems/systems.csv` is *authored*
rather than mined. One sub-agent per system. When the worklist is empty and the
matrix builds with no missing-token flags, the workshop closes.

## Why

The matrix carried only three mined lead tokens (storage, form, read-back
direction). We expanded it to a faithful one-hot schema (multi-valued axes →
indicator columns, `1`/`0`/blank). The schema and parser are done; the code-backed
reviews are not — only `reviews/Zikkaron.md` carries the full set. This retrofit
authors the missing tokens across the corpus.

- **Authoring contract (authority):** `kb/agent-memory-systems/types/agent-memory-system-review.md` (Artifact analysis + Read-back placement + Trace-derived learning placement sections).
- **Parser (truth):** `src/commonplace/lib/systems_matrix.py`; build with `python3 scripts/build_systems_matrix.py`.
- **Worked example to mirror exactly:** `kb/agent-memory-systems/reviews/Zikkaron.md`.

## Scope

- **In:** the ~129 reviews in `kb/agent-memory-systems/reviews/*.md` (exclude `*.replaced.*`, `dir-index.md`, `README.md`).
- **Out:** `kb/agent-memory-systems/lightweight/*.md` — the lighter doc-grounded type; the consumption table is code-based only. Do not retrofit them.
- Median work per review ≈ 9 tokens; pull-only/non-trace reviews need only 3.

## The token contract

Each token is a **set** of backticked controlled values on its own lead line:
`**Label:** \`a\` \`b\` — justification`. The parser one-hots whatever tokens
appear. Author **only values the review's own prose/evidence supports** — never
guess. If the review genuinely cannot determine an applicable axis from the code
it read, write the lead line with only `` `not-determinable` `` plus a one-line
reason; do not invent a value, and do not omit the lead line. Omitted applicable
lead lines mean the retrofit is incomplete.

### Artifact analysis section (every review)

| Lead token | Allowed values (list all that apply) |
|---|---|
| `**Representational form:**` | `prose` · `symbolic` · `parametric` — replace any legacy `` `mixed` `` with the actual components |
| `**Lineage:**` | `authored` · `imported` · `trace-extracted` |
| `**Behavioral authority:**` | `knowledge` · `instruction` · `enforcement` · `routing` · `validation` · `ranking` · `learning` |

These usually already exist as *free prose* ("Lineage: authored via …",
"Behavioral authority: knowledge artifact when …"). Convert that prose into the
controlled lead token; keep the explanatory prose.

### Read-back placement section (only when direction is `push` or `both`)

| Lead token | Allowed values |
|---|---|
| `**Read-back signal:**` | `coarse` · `identifier` · `inferred / lexical` · `inferred / embedding` · `inferred / judgment` |
| `**Read-back timing:**` | `pre-action` · `post-action` |
| `**Faithfulness tested:**` | single `yes` or `no` |

`**Read-back:**` (`pull`/`push`/`both`) already exists in every review and needs
no change; `rb_pull`/`rb_push` derive from it for free.

### Trace-derived learning placement section (only when the `trace-derived` tag is set)

| Lead token | Allowed values |
|---|---|
| `**Trace source:**` | `session-logs` · `tool-traces` · `event-streams` · `trajectories` |
| `**Learning scope:**` | `per-task` · `per-project` · `cross-task` |
| `**Learning timing:**` | `online` · `offline` · `staged` |
| `**Distilled form:**` | `prose` · `symbolic` · `parametric` |

`storage_substrate` stays a single token (unchanged).

## Orchestration

1. Build the worklist: run `python3 scripts/build_systems_matrix.py`. Its `flags`
   output lists, per code-backed review file, every applicable axis still missing
   its lead token. That is the exact per-review task list. Lightweight notes are
   intentionally excluded by the builder.
2. For each review file with flags, spawn **one sub-agent** scoped to that single
   file (sequential, or bounded parallel — but never two agents on one file).
   Pass it the file path, this runbook, and the Zikkaron example.
3. After each sub-agent returns, re-run the build and confirm that file's flags
   are gone. Legitimately unknown applicable axes must use a
   `` `not-determinable` `` lead token, not an omitted line. Run
   `commonplace-validate <file>` and confirm `Overall: PASS`.
4. When the build reports **0 flags for repo-reviewed rows**, regenerate the
   human table (`python3 scripts/render_systems_table.py`) and close the workshop.

## Per-sub-agent procedure (one review file)

1. Read the whole review file.
2. Determine applicability from its frontmatter `tags` and `**Read-back:**`
   verdict: push/both → do the read-back signal/timing/faithfulness tokens;
   `trace-derived` tag → do the four trace tokens; the three Artifact-analysis
   tokens always apply.
3. For each applicable axis, read the relevant section's prose and map it to the
   controlled value set. Examples of the mapping are in Zikkaron. The information
   is almost always already stated in prose — your job is to *normalize it into
   the controlled vocabulary*, not to re-investigate the system.
4. Insert each lead token on its own line inside the correct section, immediately
   below the existing lead tokens / at the head of the relevant subsection
   (mirror Zikkaron's placement). For `Representational form`, **replace** the
   legacy `` `mixed` `` token with the component set.
5. Preserve all surrounding prose, citations, and CriticMarkup attributes. Match
   local style; one backticked token per value; end the lead line with a short
   `— justification` drawn from the review's own evidence.
6. Do **not** read or modify the reviewed system's source; do **not** change the
   review's claims; do **not** update `last-checked`.
7. Self-check: the lead line uses only allowed values; multi-valued axes list
   every value that applies; absent-by-evidence axes use a sole
   `` `not-determinable` `` token with a reason, not a guessed value.

## Guardrails

- **Faithful, not complete.** A blank cell from a `not-determinable` lead line is
  correct and honest; a guessed `1` pollutes the matrix. Missing applicable lead
  lines are still build flags.
- **Multi-value is normal.** A system can be `coarse` *and* `identifier` *and*
  `inferred / embedding` at once (Zikkaron is). List them all.
- **`mixed` is retired.** Never author `` `mixed` `` for representational or
  distilled form — decompose into components.
- **One file per agent.** No agent edits a review another agent is touching.

## Done when

`python3 scripts/build_systems_matrix.py` reports **0 flags** for repo-reviewed
rows, every changed review validates PASS, and the rendered table is rebuilt.
Then extract any durable findings and delete this workshop.
