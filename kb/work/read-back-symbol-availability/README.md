# Read-back symbol availability — review-system revision

Fold [symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) into the [agent-memory-system review](../../agent-memory-systems/types/agent-memory-system-review.md) framework's **Read-back placement** treatment, then plan re-characterizing the existing reviews' push paths under the sharper lens.

## Why

Before any trigger taxonomy, one scope cut and one axis:

- **Read-back returns *retained* content** — material the system holds from prior use, whether **authored** (a user's note, a project decision, a maintained KB artifact) or **trace-learned**. Both are memory; "authored" is not the opposite of "remembered." What read-back excludes is **shipped/static baseline documentation** — tool specs, repo docs, installed skills, system manuals — which the system ships with rather than accumulates. A "push" that carries only such documentation is *excluded* from read-back, not classified as a weak kind of it. (The boundary test: does the content *accumulate from use of this system*, or *arrive with the system*? The former is memory; the latter is baseline documentation.)
- **Targeting — coarse vs instance-identifying.** Among genuine memory pushes, one fired by an always-present or action-type symbol (always-load, session start, any `Write`) delivers *generic* recall, not selection for *this* instance.

**Always-load is the degenerate corner** for memory pushes — not instance-targeted, so barely a push. (Always-load of shipped *documentation* isn't even on the map: it is not memory.)

The real, hard case is **instance-targeted recall of remembered content**, and that is exactly where the symbol-availability bound bites: a system cannot *symbolically* select remembered content for an instance it has no symbol for. So genuine instance-relevant read-back either reacts to an already-emitted symbol or runs **semantic inference** over the current state. CrewAI's LiteAgent and REM, for instance, retrieve memory on **the current user message** — instance-targeted, but via the semantic route, not a symbol — so under this lens they are *semantic push*, not symbolic anticipation.

## Thread 1 — revise the review framework

Target: the `## Read-back placement` section of [agent-memory-system-review.md](../../agent-memory-systems/types/agent-memory-system-review.md).

- Add a **scope cut** up front: Read-back placement covers *retained memory* only (authored or trace-learned). Runtime injection of shipped/static baseline documentation is not read-back — exclude it; don't list it as a trigger type.
- Keep the **direction verdict (pull/push/both) about memory read-back only.** Pushing static baseline documentation does not upgrade a system from `pull` to `both`; note such documentation as a baseline context surface, separate from the read-back verdict.
- Split axis **2 (Trigger and relevance signal)** into **two fields** (decision: two fields, not one collapsed value):
  - **targeting** ∈ `coarse` (always-load / action-type — generic recall) | `instance` (selects for *this* instance).
  - **signal** (only when `instance`; n/a for `coarse`) ∈ `identifier` (matches an **identifier the instance carries by design** — tag, type, path, tool name, id, declared scope) | `inferred` (relevance **derived from content**). When `inferred`, record the mechanism sub-kind: `lexical` (keyword/BM25 — exact-token but content-derived; cheap, sense-blind), `embedding` (learned similarity — captures sense), or `judgment` (an LLM relevance call).
  - Discriminator: *does the signal match an identifier the instance was assigned* (`identifier`) *or derive relevance from the content's words/meaning* (`inferred`)? Classify by **what it keys on**, not by mechanism — keyword/BM25 keys on content words, not an assigned identifier, so it is `inferred / lexical`, not `identifier`, even though its mechanism is exact-match.
  - Maps onto the source note's regime split: `identifier` ≈ the note's *symbolic* selection, `inferred` ≈ its *semantic* selection; the sub-kinds refine the inferred side (so note ↔ framework stay consistent — see Inputs).
  - **Lexical caveat.** A keyword signal is symbolic processing approximating semantics, so it is **sense-blind**: it fires on a term even when the context negates or excludes it ("avoid X" still matches X). Tolerable when the injected payload is small (over-injection is cheap), corrosive when large (dilution) — a `selection/scope` concern to flag on `inferred / lexical` systems.
  - Worked examples — **`identifier`:** Atomic report scope/tag filters; a tool-name hook; a `project_id`-keyed store; type/tag-keyed injection on file open. **`inferred`:** CrewAI LiteAgent (`embedding` on the current user message), REM (current input as query), an LLM relevance `judgment`; keyword/BM25 overlap is `lexical`. **mixed:** EQUIPA narrows on `identifier`s (role/project/task-type) then ranks `inferred` (lexical + embedding + graph) — record the final selector and note the composition.
- Demote always-load explicitly: the degenerate non-push corner for memory; always-load of documentation is out of scope entirely — say so rather than listing it as a peer trigger.
- State the bound as reviewer guidance: a system cannot *symbolically* anticipate an instance it has no symbol for, so genuine instance-relevant read-back is either reacting to an earlier-emitted symbol or semantic inference. Name which.
- Add a `rationale` edge from the type spec to the source note (meta-reader link).

## Thread 2 — plan updating existing reviews

The push-tagged reviews were characterized under the old flat list; re-characterize under the sharper lens.

- **Scope:** reviews with `read_back_direction` ∈ `push`/`both` or `push_engineered = yes` in `systems.csv`.
- **Reformatting-only, flag-don't-guess** (same discipline as the lead-token retrofit): re-read each review's existing Read-back prose and classify in order — first the scope cut (retained memory vs shipped documentation? documentation leaves the read-back set), then coarse-vs-instance, then symbolic-vs-semantic — from what it already states; where the mechanism isn't described, flag rather than re-read source. Expect two outcomes: documentation-injection systems (shipped skills / tool docs, e.g. Agent Skills) leave read-back entirely, and "semantic-on-current-query" systems (CrewAI / REM style) move from symbolic-push to **semantic push**.
- **Run as a standalone pass now** (decision), driven by a **frontloaded hand-off instruction** — self-contained for an execution agent, like the lead-token retrofit instruction. The instruction carries: scope (which reviews), the gating order, the targeting/signal fields + discriminator + worked examples, the flag policy, and the ledger format.
- **Output:** a per-review ledger of the new classification + flags.

## Thread 3 — extractable fields (deferred until after one ledger pass)

Do **not** lock matrix fields now. Use prose guidance first (Thread 1), run one ledger pass (Thread 2), then add extractable fields only if the values prove stable. Candidates: `read_back_targeting` (`coarse` / `instance`) and `read_back_signal` (`identifier` / `inferred`, with the inferred sub-kind `lexical` / `embedding` / `judgment`). A `read_back_payload` field is now unlikely — shipped documentation is *excluded* from read-back rather than tabulated as a value, so the only payload distinction left inside read-back is authored-vs-trace-learned, which the ledger pass can show is worth a field or not. If adopted, extend the parser + retrofit in the [systems.csv](../../agent-memory-systems/systems.csv) toolchain (`scripts/build_systems_matrix.py`, `scripts/analyze_matrix.py`).

## Inputs

- Source note: [symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md).
- The note should get the same sharpening so note and framework stay consistent: frame it as **instance-identifying** symbol availability (coarse symbols can already route generic guidance), and note that push systems often retrieve on the current query/input (semantic), not on role/task-type alone. (An earlier Codex review of the note raised these; its inline marks have since been cleared — so this is a sharpening to apply, not pending marks to resolve.)

## Closure

Close when: (1) the Read-back placement scope cut + axis are in the type spec and it validates; (2) the direction-verdict-is-memory-only rule is stated; (3) a `rationale` edge to the note exists; (4) there is a written plan (or an executed pass) for re-characterizing existing reviews, with the symbolic-vs-semantic-push reclassification decided; (5) extractable fields are decided — adopted after the ledger pass or explicitly deferred; (6) the source note is sharpened to match the framework (instance-identifying symbol; semantic push) so its claim and the framework agree; (7) durable conclusions are promoted. Then remove this workshop's entry from `kb/work/README.md`.
