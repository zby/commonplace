# Case 5: harness offloading vs. base LLM competences

Frozen before launch, 2026-11-24. Origin: live session on 2026-11-24 where an
agent (Gemini 4 Neon) extracted `kb/theory/selection-based-learning-requires-five-base-llm-competences.md`
from the rewritten lead article (`d7b028047`). The agent mapped every loop
function of the deployed system onto five base LLM competences and stated them
as an unqualified requirement. The operator made two rulings:

1. **Harness offloading:** the list is too broad—several of those competences
   (enforcement, trace capture, replay, store bookkeeping, rollbacks) can be
   provided by harness code rather than required from the frozen LLM itself.
2. **Working-hypothesis modality:** the resulting competence split should be
   marked explicitly as a working hypothesis, not a settled requirement.

## Question

Given a writing commission matching that live session, what additional
information nudges a fresh writer to (1) separate harness-offloadable work
from irreducible base-LLM competences without being told the answer, and (2)
mark the resulting list as a working hypothesis?

## Setup

2×2 factorial design across four arms, three fresh headless Opus runs per arm
(12 writers + 2 blind scorers = 14 calls total), started in an empty working
directory with `--tools ''` and materials pasted into the prompt.

### Base packet (all arms)

1. `kb/theory/COLLECTION.md` verbatim from commit `785ffc64a` (note: already
   contains the standing rule that hypotheses stay recognizable in prose).
2. `materials/lead-article-pre-extraction.md` — the pre-extraction draft of
   the lead article (with zero reference to the five-competence or
   three-competence notes).

### Common commission (all arms)

> Write one `kb/theory/` note (complete Markdown file with YAML frontmatter,
> 30–65 lines) specifying what base competences a frozen LLM needs to run a
> selection-based learning system like Commonplace autonomously. Leave aside
> inference-time compression and speculative domain ceilings; focus strictly
> on the base competences the LLM needs to run the loop.

### Arms

| Arm | Additional input beyond base packet + commission | What it tests |
|---|---|---|
| **C** | None. | Baseline reproducing the live miss. |
| **R** | Two standing KB notes verbatim from `785ffc64a`: `kb/theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md` and `kb/theory/semantic-work-can-be-relocated-but-not-eliminated.md`. | Whether missing KB retrieval alone caused the miss—no extra instruction given. |
| **A** | One general authoring rule: *"Before attributing a required capability to one component (here, the frozen LLM), check each item against the rest of the system's architecture: do not assign a system-level function to the model if another layer can perform it."* | Whether a general component-attribution rule works without extra KB notes. |
| **RA** | Both **R** and **A**. | Whether retrieval and the general rule interact or either suffices alone. |

No arm adds an explicit reminder about working-hypothesis modality; all four
arms inherit `COLLECTION.md`'s existing rule verbatim so Dimension 2 measures
whether that standing rule fires on its own.

## Scoring

Two independent fresh scorers, blinded to arm, predictions, and later rulings,
grade all 12 shuffled anonymous drafts on two separate dimensions:

- **Dimension 1 — Harness offloading (`H` / `P` / `M`):**
  - `H`: Explicitly separates loop functions that code / the harness /
    software can supply (such as enforcement, context loading, trace capture,
    replay, store bookkeeping, or rollbacks) from the narrower set of
    irreducible semantic competences required of the frozen LLM, and keeps the
    LLM list narrowed accordingly.
  - `P`: Mentions that tools, code, or a harness assist the model, or moves
    one mechanical item off the model, without systematically factoring
    harness-offloadable work out of the base-LLM list.
  - `M`: Attributes system-level loop functions (such as enforcement, trace
    collection, replay, or store bookkeeping/pruning) directly to the frozen
    base LLM without factoring out what code/harness can supply.
- **Dimension 2 — Working-hypothesis modality (`W` / `U`):**
  - `W`: Explicitly marks the competence list/split as a working hypothesis or
    conjecture (in title, description, opening, or Scope) rather than an
    established requirement.
  - `U`: States the list as an unqualified or settled requirement.

Keep both scorer grades when they disagree; do not retry calls for quality.

## Predictions (recorded before launch)

| Arm | Dimension 1 (`H` / 3) | Dimension 2 (`W` / 3) |
|---|---|---|
| **C** | 0/3 | 1/3 |
| **R** | 1–2/3 | 1/3 |
| **A** | 2–3/3 | 1/3 |
| **RA** | 3/3 | 1/3 |

## What each outcome would show

- **R beats C on `H` without A:** The live miss was primarily a KB-retrieval
  miss; surfacing relevant architecture notes before drafting is the right
  fix.
- **A beats C on `H` without R:** A general component-attribution check in
  writing instructions (`cp-skill-write` or `kb/theory/COLLECTION.md`) is
  enough without pre-selecting KB notes.
- **Only RA hits `H` reliably:** Writers need both the standing architecture
  notes in context and the explicit attribution check.
- **C already hits `H` (≥2/3):** The live miss was model- or
  conversation-specific (e.g., momentum from immediately summarizing the four
  bars) rather than a general drafting failure on Opus.
- **Low `W` across all arms:** `COLLECTION.md`'s existing hypothesis rule is
  not firing reliably during cold drafting, justifying a separate modality
  check or Round 2 nudge.

## Limits

- Small sample (3 drafts per arm, one model by default) on a single case.
- The pre-extraction article is reconstructed from the live draft prior to
  extraction rather than committed separately in git; its hash is recorded in
  `run/packet.sha256`.
- Tests cold writing from supplied materials, not autonomous retrieval of the
  two KB notes in **R**.
