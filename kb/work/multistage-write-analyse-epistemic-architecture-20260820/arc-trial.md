# ARC-skill cold epistemic-architecture trial

Paths cited below are relative to `related-systems/arc-skill/`. Code module names without a longer prefix are under `skills/arc-skill/scripts/arc_skill/`.

## 1. Source-and-claim boundary

| field | boundary |
|---|---|
| system | `arc-skill`: the checked-in skill doctrine and Python harness that mediate an external coding agent's interaction with an ARC-AGI-3 environment. |
| reviewed revision/version | Clean checkout at Git commit `dba53c3799eab600a512dd73ed037d7ab6958c66` (`dba53c3`; commit date 2026-08-19; subject `docs: rewrite readme from site content`; origin `https://github.com/pbshgthm/arc-skill.git`). `git status --short` was empty before analysis and after the in-memory probes. |
| analysis question | Whether and how ARC-skill produces knowledge, especially through prediction admission, evaluation, retention, replay, and continued-use routes. |
| scope | Named routes in the ARC-skill-mediated agent/game loop. The inspected system includes the doctrine, launcher, CLI, broker adapter, journals, prediction grammar and grader, evidence reshaping, notes plumbing, executable-rules replay, search, and checked plan execution. It does not include the external agent's internals, ARC game source/private state, ARC servers, or the implementation of the declared `arc-agi==0.9.9` dependency. It is therefore not a complete analysis of every component in the larger agent-plus-ARC service. |
| implementation evidence | All tracked executable source in the checkout was inspected: `skills/arc-skill/scripts/arc`, `arc_cli.py`, `broker_server.py`, and every module in `scripts/arc_skill/` (`__init__.py`, `analysis.py`, `broker.py`, `cli.py`, `core.py`, `evidence.py`, `inspect.py`, `live.py`, `perception.py`, `predictions.py`, `rules.py`). Pure in-memory probes against this source confirmed that an empty prediction raises, a two-claim cell/region prediction grades true against a matching synthetic settled frame, and synthetic rules histories produce `HISTORY_FIT`, `MISMATCH`, and `INCOMPLETE` on the corresponding branches. These are implementation probes, not ARC-game runs. |
| doctrine/design evidence | `README.md` and `skills/arc-skill/SKILL.md` at the reviewed revision. `README.md` is public design explanation plus reported operation; `SKILL.md` is the instruction supplied to an agent. |
| reported-operation evidence | `README.md:16-30`, `README.md:45-51`, `README.md:79-119`, and `README.md:227-230` report a 25-game campaign, scorecard result, prediction counts, misses, context compactions, tool use, and differing miss rates. These are attributed project reports. The linked site and scorecard were not inspected under this source boundary, and no underlying run artifacts occur in the checkout. |
| observed-run evidence | None. No `.arc/`, `events.jsonl`, `mutations.jsonl`, receipts, notes from a run, `rules.py` from a run, plan, verification record, recording, or replay trace is present. `.gitignore:7-8` says run state is excluded because a run directory is never part of the repository. The synthetic probes above establish branch behavior only. |
| causal-experiment evidence | None. The checkout contains no treatment-control trace. Reported differences between single actions and planned sequences do not independently vary the prediction gate, notes, planning, model, task state, or agent, so they do not identify a component effect. |
| missing evidence -> conclusion prevented | No inspectable ARC-game run -> no conclusion that any prediction was actually generated, graded, used to revise a belief, written into notes, replayed, or continued in a batch. No campaign event corpus or scorecard inspection -> no verification of the reported 25/25 result, 7,627 predictions, 443 misses, 115 compactions, tool-use counts, replay success, or miss-rate split. No controlled comparison -> no causal conclusion that mandatory prediction, notes, batching, offline computation, or executable rules caused success or efficiency. No external-agent trace or state probe -> no conclusion that the agent learned, changed a policy, or treated a grade as belief revision. No run-specific `NOTES.md` or `rules.py` -> no conclusion that any mechanic claim was well formed, evidenced, accepted, or transferred. No inspection of ARC/`arc-agi` internals or independent sensor oracle -> no independent conclusion that returned public observations are complete or true of private game state. No unseen-transition tests -> no conclusion that a history-fitting model transfers beyond checked transitions. No component-isolating replay contrast -> no conclusion that a specific component produced a reported outcome. |
| system knowledge-production/warrant claims -> source or none found | Claims were found. The README says a prediction that holds leaves the game model "still standing" and a miss locates where belief and reality diverged (`README.md:45-47`); observations become rules in a persistent notes page (`README.md:79-89`); a hard gate requires a falsifiable claim (`README.md:93-97`); and executable rules can be fitted against recorded actions and used for search (`README.md:104-112`). The skill tells the agent to compare grades and repair notes after a miss (`SKILL.md:36-59`), batch only verified mechanics (`SKILL.md:61-74`), demote earlier verified claims on a new level until a test survives (`SKILL.md:77-86`), and replay-check executable rules before search (`SKILL.md:89-107`). The README also explicitly says no criterion for when a mechanic counts as verified is supplied (`README.md:114-119`). |

## 2. Epistemic-object inventory

| object/part id | system name and description | representational form | source/input and lineage | producer/consumer | candidate truth-apt content or none | claimed role | evidence layer and source | gap/limit |
|---|---|---|---|---|---|---|---|---|
| O1 | Public observation, mutation, and event record: returned frames plus `state`, completed/total levels, available actions, causal action token, and reasoning metadata. | Symbolic numeric grids encoded as hexadecimal rows and JSON/JSONL metadata. | External ARC environment response -> broker encoding and mutation journal -> `normalize_observation` -> append-only event. | Producer: external environment through `ArcSession`/broker. Consumers: prediction grader, evidence views, offline analysis, notes author, rules replay/search, recovery. | The public board cells, frames, action availability, level counter, and environment state at a named event. | The numeric grid is treated as observation ground truth; the event history is the evidence base. | Implementation: `broker.py:99-225,283-326,458-548`; `core.py:258-326`. Doctrine: `SKILL.md:109-123`. | Import preserves the returned public payload under the local encoding, but neither the environment's internals nor its source truth/completeness was checked. Mutation reasoning is supplied to the environment but is not an oracle. |
| O2 | Exact evidence reshaping: grid text/crops, before/after masks, cell deltas, hashes, PNGs, histories, and NPZ exports. | Symbolic arrays/records, natural-language serialization of exact counts, and bitmap renderings. | O1 -> deterministic projection, comparison, hash, palette rendering, or export. | Producer: `evidence.py`, exact parts of `perception.py` and `inspect.py`. Consumers: external agent, plan freshness, status, replay provenance, offline analysis. | Exact grid-index values, equality/difference counts and locations, and identity of a settled grid within the implemented representation. | Make observations cheap to inspect and preserve cell-exact evidence. | Implementation: `evidence.py:37-112`; `perception.py:222-241`; `inspect.py:345-497,578-619`. | These operations do not establish game semantics. A PNG is a deterministic palette view, not an independent measurement. Hash equality supplies identity/freshness, not endorsement. |
| O3 | Heuristic scene dossier and prose hypotheses: monochrome components, repeated shapes, lattice candidates, motion stories, and salience-ranked click candidates. | Symbolic heuristic records and generated natural language. | O1/O2 geometry -> deterministic heuristics that introduce object identity, motion, lattice, or salience interpretations. | Producer: `perception.py` and `inspect.py`. Consumer: external agent through status/view and `.arc/dossier.json`. | Candidate propositions such as "this component moved", "this scale is a likely lattice", or "this component is a useful click hypothesis". | Help the agent notice structure and form/test hypotheses. | Implementation: `perception.py:14-220,243-522`; `inspect.py:87-174,389-497`. | Component identity across frames is heuristic. The UI labels lattice and click results as hypotheses/candidates. No route checks or accepts their semantic truth. The dossier is overwritten with the current scene. |
| O4 | Action prediction claim: one or more `noop`, `change`, `cell`, `move`, `vanish`, `region`, `level+1`, or `win` claims attached to an action; otherwise free prose becomes `change`. | Natural-language string parsed into symbolic claim dictionaries. | External agent's interpretation of O1-O3 and possibly O6/O7 -> CLI `--predict` or batch-step text. | Producer: external agent. Consumers: parser/admission gate, environment reasoning field, grader, batch controller, event log. | A falsifiable proposition about the settled public result or level/game status immediately after one named action. | Force prediction before action, expose belief, and make the next observation able to contradict it. | Doctrine: `README.md:33-75`; `SKILL.md:36-59`. Implementation: `predictions.py:1-128`; `live.py:81-173,177-266`. | The agent's inference is outside the checkout. Any non-keyword prose is admitted as the coarse claim `change`; specificity or support is not checked. Most claim types concern the settled frame, not intermediate dynamics or a general mechanic. |
| O5 | Per-claim grade, aggregate `predict_ok`, outcome receipt, and recent-history mark. | Symbolic booleans and actual-result strings in event/receipt JSON plus rendered text. | O4 + O1 immediately before and after the action -> grammar-specific comparison -> all-claims aggregate. | Producer: `grade_claims`, `execute_action`, or `execute_steps`. Consumers: receipt/status/history, batch controller, external agent, later offline analysis. | That a particular claim did or did not match the returned settled result under the implemented claim semantics. | Turn prediction into a checkable event and make a miss local to one action/claim. | Implementation: `predictions.py:131-255`; `live.py:115-266`; `inspect.py:345-387,502-532`. | A pass does not check the producing explanation, all board semantics, intermediate frames, unseen actions, transfer, or a general game model. Individual-action misses are reported but do not automatically block the next command. |
| O6 | `.arc/NOTES.md` and per-level note archives with `Verified`, `Assumed / open questions`, and `Plan` headings. | Agent-authored natural language. | External agent synthesis of O1-O5, O3, and optional O7/O8; copied to a level archive on completion. | Producer/editor: external agent. Consumers: `status` and the future agent context; archive reader. Harness creates the skeleton, displays it, and snapshots it. | Potential mechanic claims, event-attributed observations, assumptions, refutations, and intended tests. | Durable one-page recovery story across context compaction and retained distinction between verified and assumed mechanics. | Doctrine: `README.md:79-89`; `SKILL.md:50-59,77-86`. Implementation: `cli.py:194-207`; `live.py:58-66`; `inspect.py:285-319,502-532`. | No run note exists in the checkout. The harness does not parse claims, verify event citations, enforce the headings after creation, enforce a page limit, or define/validate the criterion for `Verified`. Archive/display is retention, not acceptance. |
| O7 | Agent-authored `rules.py`: executable state grounding, transition, action, goal, and observation model, with optional render, heuristic, key, and dead-state functions. | Symbolic executable code with potentially mixed natural-language comments and `Unknown` gap markers. | External agent's conjectural compression of O1-O6 -> contract functions. | Producer: external agent. Consumers: contract checker, history replay, A* search, live plan executor. | Propositions encoded as a state-transition model: how actions change state, what observations follow, and what constitutes a goal or dead state. | Escalate verified mechanics into a replayable world model and searchable planner. | Doctrine: `SKILL.md:89-107`; implementation: `rules.py:1-179`. | No run-specific `rules.py` is present. `observe` may expose only a user-chosen projection; `render` is optional. Determinism, semantic fidelity, omitted state, and premise warrant are not independently checked. |
| O8 | Rules replay verification record: `HISTORY_FIT`, `INCOMPLETE`, or `MISMATCH`, with counts, gaps, first mismatch, hashes, and checked event. | Symbolic JSON record and status text. | O7 replayed over O1; exact rendered grids, user-defined observation projections, goal/dead predicates, or explicit `Unknown` gaps are compared. | Producer: `_walk`/`replay_rules`. Consumers: status display and `solve_rules`; explicit replay is retained in `.arc/verify.json`. | That the model fits, leaves gaps in, or contradicts the checked recorded history under the selected comparison domain. | Verify executable rules against history before relying on search. | Implementation: `rules.py:181-350`; `cli.py:331-350,463-468`; `inspect.py:232-283`. | `HISTORY_FIT` is bounded to recorded, checked transitions and the model's projection; reset transitions are re-grounded rather than passed through `step`. `INCOMPLETE` still permits search. A saved result can become stale and is then only flagged. No verification instance is present. |
| O9 | Model-internal solve plan: an action path found by A* from a grounded current state to `goal(state)`. | Symbolic JSON action sequence plus model/search provenance. | O7 + current O1 + O8 replay disposition -> model graph search. | Producer: `solve_rules`. Consumer: solve-plan loader and live commit. | Within the executable model, the recorded action path reaches a state satisfying the model's goal predicate. | Convert a fitted/usable model into an efficient action sequence. | Implementation: `rules.py:354-489`; `live.py:268-335`. | Search is allowed after `INCOMPLETE`, not only `HISTORY_FIT`. User heuristic admissibility is instructed but not enforced. `PLAN_FOUND` establishes a path in the model, not in the external game; optimality is not warranted if the heuristic is inadmissible. No plan instance is present. |
| O10 | Solve-plan per-step prediction: exact `rows`, projected `observe` value, or final `level_up` expectation paired with each O9 action. | Symbolic JSON. | O7 trajectory along O9 -> rendered/projected successor or goal marker. | Producer: `solve_rules`. Consumer: `execute_solve_plan` and its live continuation gate. | That the next external settled board/projection will match the model, or that the final step will advance the level. | Keep model-generated execution prediction-checked and stop on the first surprise. | Implementation: `rules.py:446-489`; `live.py:296-426`. | These are entailed inside O7 but ampliative about the external environment. Projection checks can omit pixels/state. The last action is marked `level_up` because the model path ended at `goal`; that external consequence is not warranted until execution checks it. No plan run exists. |
| O11 | Paid-action mutation journal, append-only event timeline, and local replay/recovery consistency relation. | Symbolic JSONL plus exact encoded observations and mutation IDs. | Action/reasoning + external response -> mutation journal before CLI event -> event reconciliation; on local restart, journal -> fresh same-game/seed simulator replay -> exact comparison. | Producer: broker and CLI. Consumers: recovery, restart gate, current-state consistency check, all later routes. | The exact recorded public action-observation sequence and, after a successful restart check, its reproducibility under the current local simulator/cache/seed. | Crash-safe one-run continuity and exact local replay recovery. | Doctrine: `SKILL.md:9-23`; `README.md:176-181`. Implementation: `broker.py:283-326,399-548`; `cli.py:224-329`; `live.py:1-6`. | No journal or replay result is present. Remote competition mode is explicitly not reconstructible. Equality under the current cached simulator does not establish causal contribution, private-state identity, cross-version replay, or general game rules. |
| O12 | `arc python` analysis result: arbitrary offline computation over recorded boards, transitions, frames, and helper algorithms. | Arbitrary symbolic values, arrays, or printed natural language produced by user-supplied Python. | O1/O2 -> external agent/user program in a preloaded namespace. | Producer: supplied code plus helper library. Consumer: external agent via stdout; no automatic later consumer. | None fixed by ARC-skill; a supplied program may emit truth-apt results, conjectures, plans, or non-propositional data. | Cheap parsing, measurement, and pathfinding over already-recorded evidence. | Doctrine: `SKILL.md:109-123`. Implementation: `analysis.py:1-215`. | The route has no standardized target, check, retention, admission, or acceptance criterion. Output warrant depends entirely on the supplied program and its premises. |

## 3. Authority-route ledger

### R1 — Public-observation acquisition and normalization

`object/candidate id:` O1<br>
`input-to-output transformation:` acquisition/import from the external environment response to normalized hexadecimal grids and event metadata.<br>
`check target:` payload representability: at least one frame, two-dimensional frames, colors in `0..15`, and normalizable status/action metadata.<br>
`oracle/evaluator and domain:` `normalize_observation`, `grid_to_rows`, and related type/range checks over the returned public interface.<br>
`timing:` after environment observation/step, before event use; mutation encoding occurs before the CLI event is appended.<br>
`possible or observed result:` normalized record or error; no ARC response was observed in this checkout.<br>
`implemented force:` an invalid payload aborts the command; an admitted payload becomes the evidence input for later routes.<br>
`epistemic authority and scope:` preserves what the public interface returned within the local encoding; it does not license source truth, completeness, or private-state claims.<br>
`operational authority: consumer, channel, force, horizon:` graders, evidence views, analysis, replay, and the external agent consume the event through JSONL/status/files for the rest of the run.<br>
`evidence layer and source:` implementation, `broker.py:208-225,283-326,458-548`; `core.py:216-326`.<br>
`system claim versus route:` supports acquisition of exact public grids and metadata, not production of game-mechanic knowledge.<br>
`gap/limit:` ARC/`arc-agi` internals and independent sensor validity were not inspected.

### R2 — Exact observation reshaping

`object/candidate id:` O1 -> O2<br>
`input-to-output transformation:` non-ampliative reshaping and algorithmically entailed grid facts: text/crop, palette image, hash, equality, cell delta, mask, or export.<br>
`check target:` numeric grid identity and differences under array coordinates and equality.<br>
`oracle/evaluator and domain:` deterministic NumPy/hash/palette functions over the public grid representation.<br>
`timing:` after each recorded event or on status/view/export.<br>
`possible or observed result:` derived artifact or validation error; synthetic grading used matching arrays, but no ARC artifact was observed.<br>
`implemented force:` artifacts are rendered/cached/displayed; observation/rules hashes also gate plan freshness and mark saved verification freshness.<br>
`epistemic authority and scope:` warrants array-level identity/difference relative to O1 and the implemented coordinate/palette conventions.<br>
`operational authority: consumer, channel, force, horizon:` external agent via CLI/PNG, rules and plan code via hashes/arrays; until the event or dependent artifact becomes stale.<br>
`evidence layer and source:` implementation, `evidence.py:37-112`; `perception.py:222-241`; `inspect.py:345-497,578-619`.<br>
`system claim versus route:` supports "see exact grid/diff" and provenance checks.<br>
`gap/limit:` establishes no semantic object, mechanic, explanation, or source truth.

### R3 — Heuristic scene-candidate generation

`object/candidate id:` O1/O2 -> O3<br>
`input-to-output transformation:` ampliative conjecture from pixels to component identity across frames, motion, lattice, line, repeated-shape, or click-salience interpretation.<br>
`check target:` none after generation; inputs are measured geometry, while semantic interpretations are candidates.<br>
`oracle/evaluator and domain:` fixed heuristic programs over monochrome 4-connected regions and grid runs, not an external oracle.<br>
`timing:` after each event for the dossier and during status/view.<br>
`possible or observed result:` candidate records/text; no accepted/rejected ARC candidate was observed.<br>
`implemented force:` stored in the current dossier or displayed, so it can attract the external agent's attention; it does not admit or reject an action.<br>
`epistemic authority and scope:` exact subfields such as counts inherit R2; semantic movement/lattice/object/salience claims receive no implemented authority.<br>
`operational authority: consumer, channel, force, horizon:` external agent through dossier/status/view; advisory until overwritten or context changes.<br>
`evidence layer and source:` implementation, `perception.py:14-220,243-522`; `inspect.py:87-174,389-497`.<br>
`system claim versus route:` supplies neutral instruments for free hypothesis formation.<br>
`gap/limit:` there is no test, acceptance record, or later-use gate keyed to these hypotheses.

### R4 — Prediction and action admission

`object/candidate id:` O4<br>
`input-to-output transformation:` candidate prediction string -> parsed claims plus an admitted action request, or rejection before a paid step.<br>
`check target:` prediction non-emptiness and grammar well-formedness; action token coordinates and current public availability.<br>
`oracle/evaluator and domain:` `parse_claims`, `parse_action`, and `check_public_action`; syntactic/action-interface domain only.<br>
`timing:` before `broker_step`.<br>
`possible or observed result:` admit or raise; an in-memory probe observed empty-prediction rejection, not a game action.<br>
`implemented force:` rejected requests spend no action; admitted requests may reach the environment.<br>
`epistemic authority and scope:` none over prediction truth, evidential support, specificity, or the agent's game model.<br>
`operational authority: consumer, channel, force, horizon:` broker/environment via the CLI; permission for exactly one requested action or one prevalidated batch element.<br>
`evidence layer and source:` implementation, `predictions.py:59-128`; `core.py:337-378,439-444`; `live.py:81-96,115-127,194-207`. Doctrine, `README.md:33-44`; `SKILL.md:36-48`.<br>
`system claim versus route:` implements a hard nonempty-prediction gate, but free prose is converted to generic `change`, so the route does not enforce a sharply falsifiable or mechanic-specific claim.<br>
`gap/limit:` no premise, citation, novelty, or warrant check occurs.

### R5 — Single-action prediction evaluation

`object/candidate id:` O4 -> O5<br>
`input-to-output transformation:` ampliative next-result conjecture -> retrospective per-claim and aggregate match/miss record after one action.<br>
`check target:` the exact proposition encoded by each claim against the next settled public grid, level counter, or game state.<br>
`oracle/evaluator and domain:` returned O1 plus `grade_claims`; each grammar form has a separate limited predicate.<br>
`timing:` immediately after the paid action and before receipt/status rendering.<br>
`possible or observed result:` all claims true (`PREDICTED`), one or more false (`SURPRISE`), or terminal outcome; the in-memory probe demonstrated a synthetic cell/region pass only.<br>
`implemented force:` persists grade and `predict_ok` in the event, writes a receipt, and displays the result. A miss does not itself block a later independent command.<br>
`epistemic authority and scope:` a pass licenses only that the named claim matched this returned settled result under its grammar; a miss licenses only the corresponding contradiction under that grammar.<br>
`operational authority: consumer, channel, force, horizon:` external agent through command output/status/history; advisory for later commands and retained for the run.<br>
`evidence layer and source:` implementation, `predictions.py:131-255`; `live.py:115-173`; `inspect.py:345-387,502-532`.<br>
`system claim versus route:` supports event-local comparison and the location of a miss, but not the README's broader implication that a whole model remains standing or that the agent updates belief.<br>
`gap/limit:` most claims inspect only the settled frame; no explanation, intermediate process, general mechanic, transfer, or agent-state update is checked.

### R6 — Batch prediction evaluation and continuation

`object/candidate id:` O4/O5<br>
`input-to-output transformation:` sequence of per-step conjectures -> sequential actions and grades until pass continuation, miss, level/game termination, or game over.<br>
`check target:` each step's O4 claim against its immediately returned O1.<br>
`oracle/evaluator and domain:` same claim-specific grader as R5.<br>
`timing:` after every batch step, before the next queued action.<br>
`possible or observed result:` pass and continue; miss/terminal and discard all remaining steps; no ARC batch was observed.<br>
`implemented force:` a miss or terminal event halts the queue and reports how many steps were discarded; a pass authorizes the next queued step in this batch.<br>
`epistemic authority and scope:` each pass/miss retains R5's one-transition scope. Continued execution is an operational license, not warrant for a general mechanic.<br>
`operational authority: consumer, channel, force, horizon:` batch executor consumes grades in memory; pass continues and fail stops within the current command only.<br>
`evidence layer and source:` implementation, `live.py:177-266`. Doctrine, `SKILL.md:61-74`.<br>
`system claim versus route:` the first-miss halt is implemented. The antecedent "proven mechanic" is not checked by the harness.<br>
`gap/limit:` no observed queue and no evidence that batching or this gate improved outcomes.

### R7 — Notes retention and manual mechanic promotion

`object/candidate id:` O1/O3/O5/O8 -> O6<br>
`input-to-output transformation:` indeterminate external-agent synthesis into `Verified`, assumed, refuted, or planned natural-language content; later file display and archive copy are non-ampliative retention.<br>
`check target:` none for note truth, event citations, heading semantics, or the `Verified` label.<br>
`oracle/evaluator and domain:` external agent is the uninspected author/evaluator; the harness checks only file existence for display/archive.<br>
`timing:` doctrine requests updates after misses and during play; archive occurs after level advance.<br>
`possible or observed result:` arbitrary edited note and optional archive; no run note was observed.<br>
`implemented force:` status prints note text and level completion snapshots it; no command is rejected because notes are stale, long, unsupported, or uncorrected.<br>
`epistemic authority and scope:` none implemented for mechanic claims. A `Verified` heading is an agent label, not a harness acceptance result.<br>
`operational authority: consumer, channel, force, horizon:` future external-agent contexts consume the file through `status`; archive persists by level for the run.<br>
`evidence layer and source:` doctrine, `SKILL.md:50-59,77-86`; implementation, `cli.py:194-207`, `live.py:58-66`, `inspect.py:301-319`.<br>
`system claim versus route:` retention/recovery plumbing exists, while correction, compression, evidence citation, and verification remain doctrine.<br>
`gap/limit:` the README expressly leaves the verified-mechanic criterion to the agent (`README.md:114-119`); no model-state or note-use trace is available.

### R8 — Cross-level notes warning

`object/candidate id:` O6<br>
`input-to-output transformation:` archive/live-note modification times -> warning that earlier verified claims are only assumed on the new level.<br>
`check target:` whether the live note file's modification time is later than the completed-level archive, not whether any claim was retested.<br>
`oracle/evaluator and domain:` filesystem `mtime` comparison in `_demotion_banner`.<br>
`timing:` status on a nonterminal level after at least one level completion.<br>
`possible or observed result:` banner or no banner; no run result observed.<br>
`implemented force:` warning text only; the note content and labels are not mutated, and action admission is unaffected.<br>
`epistemic authority and scope:` none about cross-level transfer or mechanic truth.<br>
`operational authority: consumer, channel, force, horizon:` external agent via status, advisory until the note file is modified.<br>
`evidence layer and source:` implementation, `inspect.py:285-299`; doctrine, `SKILL.md:77-82`.<br>
`system claim versus route:` implements a reminder, not the claimed test-survival criterion.<br>
`gap/limit:` any edit clears the banner, even if it does not retest or demote a claim.

### R9 — Executable-rules contract and grounding admission

`object/candidate id:` O7<br>
`input-to-output transformation:` agent-authored code plus a recorded board -> contract-checked, grounded model state or explicit gap/error.<br>
`check target:` presence of required callables and ability of `initial(grid, context)` to return a state rather than `None`/`Unknown`.<br>
`oracle/evaluator and domain:` `check_contract`, `_ground`, Python execution, and user model code.<br>
`timing:` before replay/search and whenever replay re-grounds an opener, reset, level transition, or gap.<br>
`possible or observed result:` state, acknowledged gap, or command error; no run model observed.<br>
`implemented force:` missing contract rejects replay/search; `Unknown` becomes an `INCOMPLETE` gap; an ungroundable current board rejects solve.<br>
`epistemic authority and scope:` contract success warrants interface conformance only. Grounding success says the model produced a state, not that the state is faithful.<br>
`operational authority: consumer, channel, force, horizon:` rules replay/search in process; permission to enter later model routes for the current loaded file/history.<br>
`evidence layer and source:` implementation, `rules.py:37-179`. Doctrine, `SKILL.md:89-107`.<br>
`system claim versus route:` supports honest explicit gaps but does not enforce "model only verified mechanics".<br>
`gap/limit:` arbitrary agent code supplies semantics and may omit relevant state.

### R10 — Pixel-exact rules-history check

`object/candidate id:` O7 -> O8<br>
`input-to-output transformation:` modeled successor plus `render(state)` -> exact comparison with a recorded settled O1 grid.<br>
`check target:` full pixel array and shape for a nonterminal recorded transition.<br>
`oracle/evaluator and domain:` NumPy equality between user model render and public settled grid.<br>
`timing:` during history replay when `render` is defined.<br>
`possible or observed result:` explained transition, first `MISMATCH`, or an earlier explicit gap; the in-memory synthetic probe exercised fit and mismatch branches.<br>
`implemented force:` contributes to aggregate O8; first mismatch stops replay and later blocks search.<br>
`epistemic authority and scope:` warrants exact rendered-output fit for that recorded input/action under the current code, not source truth, hidden state, explanation, uniqueness, or unseen transitions.<br>
`operational authority: consumer, channel, force, horizon:` O8 and `solve_rules`; permits/blocks current-model use until rules/history changes.<br>
`evidence layer and source:` implementation, `rules.py:181-328`.<br>
`system claim versus route:` this is the strongest implementation of cell-for-cell history fit.<br>
`gap/limit:` optional; a model without `render` takes R11 instead.

### R11 — Projection-level rules-history check

`object/candidate id:` O7 -> O8<br>
`input-to-output transformation:` `observe(step(model_state, action))` and `observe(initial(actual_grid))` -> equality or mismatch.<br>
`check target:` only the JSON-freezable state projection chosen by the author of O7.<br>
`oracle/evaluator and domain:` equality under the model's own `observe` function after re-grounding from O1.<br>
`timing:` during nonterminal history replay when no `render` function exists.<br>
`possible or observed result:` explained transition, gap, or first mismatch; no ARC instance observed.<br>
`implemented force:` contributes to O8 and can block solve on mismatch.<br>
`epistemic authority and scope:` warrants equality of the chosen projection on the recorded transition only.<br>
`operational authority: consumer, channel, force, horizon:` O8/search through in-memory replay and optional saved status.<br>
`evidence layer and source:` implementation, `rules.py:267-311`.<br>
`system claim versus route:` supports replay fit at an author-selected abstraction, not necessarily cell-for-cell fit.<br>
`gap/limit:` a weak or lossy `observe` can hide consequential mismatch; encoding fidelity and omitted variables are unchecked.

### R12 — Terminal rules-history checks

`object/candidate id:` O7 -> O8<br>
`input-to-output transformation:` predicted successor plus recorded level/game metadata -> comparison with `goal` or optional `dead`.<br>
`check target:` whether a recorded level-completing move reaches model `goal`, or a recorded `GAME_OVER` reaches model `dead`.<br>
`oracle/evaluator and domain:` public O1 terminal metadata and user model predicates.<br>
`timing:` during history replay at level advance or game over.<br>
`possible or observed result:` explained, gap, or mismatch; no ARC instance observed.<br>
`implemented force:` contributes to aggregate O8; mismatch blocks solve, gap yields `INCOMPLETE`.<br>
`epistemic authority and scope:` warrants agreement of terminal classification for that recorded transition.<br>
`operational authority: consumer, channel, force, horizon:` O8/search for the current model/history.<br>
`evidence layer and source:` implementation, `rules.py:209-266`.<br>
`system claim versus route:` checks goal/dead consequences separately from ordinary state projection.<br>
`gap/limit:` it does not check why the level ended, and reset transitions are re-grounded rather than modeled.

### R13 — Aggregate rules disposition and search admission

`object/candidate id:` O8, governing O7 -> O9<br>
`input-to-output transformation:` transition results and gaps -> `MISMATCH`, `INCOMPLETE`, or `HISTORY_FIT`; solve then applies a separate operational criterion.<br>
`check target:` presence of a first contradiction and presence of any acknowledged/uncheckable gap across the replayed history.<br>
`oracle/evaluator and domain:` `_walk` aggregation over R9-R12.<br>
`timing:` explicit `rules replay` and again inside every `rules solve`.<br>
`possible or observed result:` all three statuses were produced by in-memory synthetic histories; no ARC history result was observed.<br>
`implemented force:` explicit replay can persist O8. During solve, `MISMATCH` rejects search; both `INCOMPLETE` and `HISTORY_FIT` permit search if the current board is groundable.<br>
`epistemic authority and scope:` `HISTORY_FIT` licenses only no gaps/mismatches in the implemented checks over recorded transitions. `INCOMPLETE` withholds full fit; `MISMATCH` identifies a contradiction.<br>
`operational authority: consumer, channel, force, horizon:` `solve_rules` consumes the fresh in-memory result; status consumes saved O8 until event/rules/observation hashes make it stale.<br>
`evidence layer and source:` implementation, `rules.py:181-376`; `cli.py:331-350,463-477`; `inspect.py:232-283`.<br>
`system claim versus route:` history-fit status is implemented, but operational model use requires only "not mismatched", not complete historical verification.<br>
`gap/limit:` fit does not establish unseen mechanics, causal explanation, unique model, transfer, or reset behavior.

### R14 — Model-internal plan derivation

`object/candidate id:` O7/O8 -> O9/O10<br>
`input-to-output transformation:` grounded model state -> A* exploration of author-supplied actions/step/goal/dead/heuristic -> action path and per-step model consequences.<br>
`check target:` reachability of a state satisfying the model's `goal`; search bounds, known/unknown edges, and optional dead predicate.<br>
`oracle/evaluator and domain:` A* over O7's symbolic transition domain; no external environment check at this phase.<br>
`timing:` after R13 permits solve.<br>
`possible or observed result:` `PLAN_FOUND`, no plan in model, time limit, or node limit; no plan observed.<br>
`implemented force:` a found path writes `.arc/plan.json`; other outcomes do not.<br>
`epistemic authority and scope:` warrants a goal-reaching path within the executable model if its functions behave consistently; no external-game warrant transfers from search alone.<br>
`operational authority: consumer, channel, force, horizon:` live commit may consume the saved plan, subject to R15; horizon ends when source event, board, or rules changes.<br>
`evidence layer and source:` implementation, `rules.py:354-489`.<br>
`system claim versus route:` implements model-based search and explicitly reports bounds/unknown edges.<br>
`gap/limit:` model premises may be incomplete or false; heuristic admissibility is not enforced; `INCOMPLETE` replay is allowed.

### R15 — Solve-plan provenance and freshness admission

`object/candidate id:` O9/O10<br>
`input-to-output transformation:` saved plan plus current run/rules state -> fresh admitted plan or stale rejection.<br>
`check target:` plan kind and shape, one prediction per action, path containment, current event ID, settled-grid hash, and rules-file hash.<br>
`oracle/evaluator and domain:` `_load_solve_plan` and exact provenance comparisons in `execute_solve_plan`.<br>
`timing:` before any plan action is sent.<br>
`possible or observed result:` admitted or rejected as malformed/stale; no plan instance observed.<br>
`implemented force:` rejection prevents all plan actions; admission permits live execution.<br>
`epistemic authority and scope:` applicability/freshness only; it does not endorse the model or predictions.<br>
`operational authority: consumer, channel, force, horizon:` live plan executor via JSON; one current source event/rules version.<br>
`evidence layer and source:` implementation, `live.py:268-335`.<br>
`system claim versus route:` supports safe use of the plan against the state from which it was derived.<br>
`gap/limit:` hashes establish identity, not semantic validity or replay safety.

### R16 — Pixel-exact live plan check

`object/candidate id:` O10 -> O5-like plan-step result<br>
`input-to-output transformation:` model-rendered next-board prediction -> comparison with the next external settled O1 grid.<br>
`check target:` full predicted `rows` array and shape for one plan step.<br>
`oracle/evaluator and domain:` exact NumPy equality against the returned public board.<br>
`timing:` after each applicable paid plan step, before the next queued step.<br>
`possible or observed result:` match and continue, or divergence and discard remaining actions; no ARC plan step observed.<br>
`implemented force:` pass authorizes the next plan step; failure halts the plan and reports `SURPRISE`.<br>
`epistemic authority and scope:` accepts only the realized settled board prediction for this action/event.<br>
`operational authority: consumer, channel, force, horizon:` in-memory plan executor; force is current-queue continuation for one next step.<br>
`evidence layer and source:` implementation, `live.py:337-398`.<br>
`system claim versus route:` implements cell-exact live falsification when `rows` exist.<br>
`gap/limit:` does not validate hidden state, intermediate frames, explanation, or future plan suffix.

### R17 — Projection-level live plan check

`object/candidate id:` O10 -> O5-like plan-step result<br>
`input-to-output transformation:` model `observe` prediction -> ground actual returned board -> compare its `observe` projection.<br>
`check target:` user-selected model observation projection for one plan step.<br>
`oracle/evaluator and domain:` model `initial`/`observe` plus equality, using O1 as grounding input.<br>
`timing:` after a paid nonterminal plan step without exact `rows`, before continuation.<br>
`possible or observed result:` projection match, grounding failure, or mismatch; no ARC plan step observed.<br>
`implemented force:` match continues; failure halts/discards the suffix.<br>
`epistemic authority and scope:` only the selected projection on the realized transition.<br>
`operational authority: consumer, channel, force, horizon:` current plan queue, one step.<br>
`evidence layer and source:` implementation, `live.py:358-398`.<br>
`system claim versus route:` implements a weaker alternative to pixel-exact live checking.<br>
`gap/limit:` omitted pixels/state can diverge while the projection matches.

### R18 — Live level-consequence plan check

`object/candidate id:` O10 -> O5-like plan-step result<br>
`input-to-output transformation:` expected final `level_up` or expected nonterminal step -> returned level counter -> pass/mismatch.<br>
`check target:` whether level advance occurs exactly on the predicted step.<br>
`oracle/evaluator and domain:` external O1 `levels_completed` metadata comparison.<br>
`timing:` after each paid plan step.<br>
`possible or observed result:` predicted advance, missing advance, or earlier-than-predicted advance; no ARC result observed.<br>
`implemented force:` correct final advance ends successfully; missing/early advance halts and discards the suffix.<br>
`epistemic authority and scope:` accepts only the event-local level-advance proposition.<br>
`operational authority: consumer, channel, force, horizon:` current plan executor and receipt at that step.<br>
`evidence layer and source:` implementation, `live.py:337-411`.<br>
`system claim versus route:` enforces level-exact plan execution.<br>
`gap/limit:` does not establish which mechanic caused the level advance or that the remaining model is correct.

### R19 — Exact local mutation replay

`object/candidate id:` O11<br>
`input-to-output transformation:` recorded action/data/reasoning mutation sequence -> re-execution in a fresh local same-game/seed environment -> exact encoded-observation comparison.<br>
`check target:` every journaled mutation's returned public frames and metadata, plus the initial event, under current cached game/runtime.<br>
`oracle/evaluator and domain:` current local ARC session and exact dictionary equality against the mutation journal.<br>
`timing:` broker startup/restart in local mode.<br>
`possible or observed result:` full exact replay or `LOCAL_REPLAY_DIVERGED`; no repository run supplied a result.<br>
`implemented force:` divergence aborts broker readiness/resume; complete replay reconstructs the live session and permits continuation.<br>
`epistemic authority and scope:` after a pass, warrants reproducibility of that recorded public sequence under the current local simulator, cache, seed, and action journal.<br>
`operational authority: consumer, channel, force, horizon:` broker/CLI via startup gate; allow or refuse the resumed local run until the next mutation.<br>
`evidence layer and source:` implementation, `broker.py:399-476`; `cli.py:224-329`. Doctrine, `README.md:176-181`; `SKILL.md:9-23`.<br>
`system claim versus route:` exact local replay recovery is implemented; remote competition runs are explicitly excluded.<br>
`gap/limit:` no observed pass, cross-version test, private-state comparison, or evidence that replay caused a campaign outcome.

### R20 — Mutation recovery and current-head consistency

`object/candidate id:` O11/O1<br>
`input-to-output transformation:` broker mutation lacking a corresponding event -> recovered event; current broker observation and latest event -> equality decision.<br>
`check target:` mutation-ID coverage and exact current public observation equality.<br>
`oracle/evaluator and domain:` journal/event membership plus broker observation encoding.<br>
`timing:` command entry and start/resume after possible CLI failure.<br>
`possible or observed result:` recovered event count, matching head, or state-divergence error; no run result observed.<br>
`implemented force:` missing events are appended; a local or remote head mismatch stops use of the run.<br>
`epistemic authority and scope:` warrants journal/event continuity and current public-state consistency, not correctness of predictions or notes.<br>
`operational authority: consumer, channel, force, horizon:` all later commands via reconciled timeline; force lasts to the next mutation/check.<br>
`evidence layer and source:` implementation, `broker.py:301-355`; `cli.py:224-329,413-430`.<br>
`system claim versus route:` supports crash recovery around paid actions.<br>
`gap/limit:` remote state cannot be reconstructed after owner loss; recovered events have no prediction grade if the CLI died before grading.

### R21 — Arbitrary offline analysis

`object/candidate id:` O1/O2 -> O12<br>
`input-to-output transformation:` arbitrary; supplied Python can reshape, derive, conjecture, search, or merely display recorded data.<br>
`check target:` none fixed by ARC-skill.<br>
`oracle/evaluator and domain:` supplied program plus preloaded NumPy/perception/pathfinding functions.<br>
`timing:` on explicit `arc python`.<br>
`possible or observed result:` arbitrary value/output or execution error; no run analysis observed.<br>
`implemented force:` prints output only; the harness does not retain, accept, or act on it automatically.<br>
`epistemic authority and scope:` none supplied by the route; warrant depends on program semantics and warranted inputs.<br>
`operational authority: consumer, channel, force, horizon:` external agent via stdout for the current context; any later action influence is outside the inspected implementation.<br>
`evidence layer and source:` implementation, `analysis.py:149-215`; doctrine, `SKILL.md:109-123`.<br>
`system claim versus route:` implements free offline computation over recorded evidence.<br>
`gap/limit:` no standardized lineage, persistence, test, acceptance, or observed use.

## 4. Per-candidate lifecycle disposition

- `candidate object ID: O1` | `relevant route IDs: R1, R19, R20` | `transformation: acquisition/import` | `discovery lifecycle: not applicable` | `applicable lineage, derivation, or update route and warrant:` the environment's public payload is normalized and retained with exact replay/reconciliation checks; its interface-level content is preserved, while independent source truth and private-state completeness remain unknown | `missing evidence/limit:` no ARC observation or independent environment oracle is in the boundary.

- `candidate object ID: O2` | `relevant route IDs: R2` | `transformation: non-ampliative reshaping or entailed derivation in an array/coordinate domain` | `discovery lifecycle: not applicable` | `applicable lineage, derivation, or update route and warrant:` exact grid text, crops, hashes, masks, deltas, and exports follow deterministically from O1 under named functions | `missing evidence/limit:` semantic labels and source truth do not follow from pixel operations; bitmap rendering is not an independent observation.

- `candidate object ID: O3` | `relevant route IDs: R3` | `transformation: ampliative conjecture` | `observation/anomaly: evidenced — O1 grids and frame deltas are implementation inputs` | `conjecture: evidenced — the implementation emits motion, lattice, object, and salience candidates, explicitly labeling some as hypotheses` | `derived consequence: absent — no automatic route derives an action consequence from an O3 candidate` | `test/evidence: absent — no candidate-specific comparison is implemented` | `acceptance: evaluator: none; criterion: none; intended use: draw external-agent attention; state: absent; accepted scope: none` | `integration: retention/later-use consumer: current dossier and status/view consumer; state: evidenced; evidence: R3 stores/displays candidates, but this is operational exposure rather than epistemic integration` | `missing phase/evidence:` semantic test, acceptance, candidate identity across time, and observed agent use.

- `candidate object ID: O4` | `relevant route IDs: R4, R5, R6` | `transformation: ampliative conjecture` | `observation/anomaly: not determinable — current observations are available, but the external agent's actual evidential input and reasoning are not inspectable` | `conjecture: evidenced — R4 requires and parses a next-result claim before an admitted action; this evidences the route, not a run instance` | `derived consequence: evidenced — the parsed claim names a consequence of one action for the next settled frame/state` | `test/evidence: evidenced — R5/R6 compare it with the returned next observation in the implementation` | `acceptance: evaluator: claim-specific program using O1; criterion: every parsed claim predicate is true; intended use: report this event and, in R6, decide whether to execute the next queued step; state: not determinable for any ARC candidate in this checkout; accepted scope: one action's returned settled result under the grammar` | `integration: retention/later-use consumer: event/receipt/history and batch controller; state: evidenced as an implemented route; evidence: R5/R6; no actual integrated instance is claimed` | `missing phase/evidence:` actual candidate, premises, agent belief update, and any criterion that promotes an event pass to a general mechanic.

- `candidate object ID: O5` | `relevant route IDs: R5, R6` | `transformation: entailed derivation from O4, the before/after O1 pair, and the implemented claim predicate` | `discovery lifecycle: not applicable` | `applicable lineage, derivation, or update route and warrant:` each boolean/actual string is computed from the named claim and public result; aggregate success is conjunction over gradable claims | `missing evidence/limit:` no actual ARC grade is present, and the derivation warrants only its narrow grammar predicate, not the producing process or mechanic.

- `candidate object ID: O6` | `relevant route IDs: R7, R8` | `transformation: ampliative conjecture when notes generalize mechanics; acquisition/retention for copied observations` | `observation/anomaly: not determinable — doctrine requests event citations, but no note exists and the harness does not validate citations` | `conjecture: not determinable — no run content is available` | `derived consequence: not determinable — plans/tests may be written in prose but have no schema` | `test/evidence: not determinable — a note may cite grades or tests, but R7 does not check them and R8 checks only modification time` | `acceptance: evaluator: external agent; criterion: unspecified by the system; intended use: future action selection and context recovery; state: not determinable; accepted scope: not determinable` | `integration: retention/later-use consumer: status-fed future agent and per-level archive; state: evidenced for the file route but not for any truth-apt claim; evidence: R7/R8` | `missing phase/evidence:` an actual note, claim identity, evidence links, verification rule, observed revision after misses, and observed later use.

- `candidate object ID: O7` | `relevant route IDs: R9-R13` | `transformation: ampliative conjecture` | `observation/anomaly: not determinable — doctrine says to model verified mechanics from history, but no model instance or author trace is present` | `conjecture: not determinable — the checkout supplies only a placeholder template and contract` | `derived consequence: not determinable for a run; the implementation can execute step, render/observe, goal, and dead on any supplied model` | `test/evidence: evidenced as an implementation route — R10-R12 compare model consequences with recorded history; no ARC test result is present` | `acceptance: evaluator: _walk; criterion: HISTORY_FIT means no implemented mismatch or gap over the checked history; intended use: characterize historical fit and inform search; state: not determinable for any model instance; accepted scope: recorded transitions and the exact render or author-selected projection. Operational search admission is weaker: any result except MISMATCH` | `integration: retention/later-use consumer: O8 status, O9 search, and O10 live checks; state: evidenced as an implementation route, not as an actual model use` | `missing phase/evidence:` actual rules, warranted premises, full-state observability, replay result, unseen-transition test, and transfer boundary.

- `candidate object ID: O8` | `relevant route IDs: R10-R13` | `transformation: entailed derivation in the replay check's declared domains` | `discovery lifecycle: not applicable` | `applicable lineage, derivation, or update route and warrant:` the status follows from whether R9-R12 encounter a contradiction or gap; if executed, it warrants only the stated history-fit/gap/mismatch relation | `missing evidence/limit:` no ARC result exists; `HISTORY_FIT` omits reset-step modeling and cannot warrant unseen mechanics, while `INCOMPLETE` still permits operational search.

- `candidate object ID: O9` | `relevant route IDs: R13-R15` | `transformation: entailed derivation within the executable model` | `discovery lifecycle: not applicable` | `applicable lineage, derivation, or update route and warrant:` A* records a path whose iterated O7 states reach `goal` in O7; this licenses model-relative reachability and fresh-plan applicability only | `missing evidence/limit:` no plan exists; external-game success, optimality under an unchecked heuristic, and premise truth do not follow.

- `candidate object ID: O10` | `relevant route IDs: R14-R18` | `transformation: ampliative conjecture about the external game, although entailed from O7 inside the model` | `observation/anomaly: evidenced as route inputs — current O1, O7, and O8 feed solve; no run instance is present` | `conjecture: evidenced as an implementation output route — solve serializes per-step external expectations` | `derived consequence: evidenced — predictions are generated by stepping O7 along O9 and taking render, observe, or final goal` | `test/evidence: evidenced — R16-R18 compare each prediction after live execution` | `acceptance: evaluator: exact public-grid equality, model-projection equality after grounding, or level-counter comparison; criterion: the applicable one-step comparison passes; intended use: authorize only the next plan step or recognize the predicted level completion; state: not determinable for any ARC plan; accepted scope: one realized public transition in the selected comparison domain` | `integration: retention/later-use consumer: live plan executor and receipt; state: evidenced as an implementation route; evidence: pass continues and failure discards the suffix` | `missing phase/evidence:` actual plan, external premises, exact checking when only `observe` exists, and any warrant for the unexecuted suffix.

- `candidate object ID: O11` | `relevant route IDs: R19, R20` | `transformation: acquisition/import plus entailed exact-consistency derivation` | `discovery lifecycle: not applicable` | `applicable lineage, derivation, or update route and warrant:` the mutation/event records preserve action-response lineage; a successful local replay or head equality check warrants exact public-sequence consistency under the current run configuration | `missing evidence/limit:` no journal/result exists; remote reconstruction, cross-version replay, hidden state, and causal contribution are outside the license.

No separate lifecycle record is possible for O12 because ARC-skill fixes no candidate truth-apt output for arbitrary supplied Python. Any such candidate would require its own program-specific lineage and disposition.

## 5. System-claim versus route comparison

| claim id | claimed operation or warrant | claim source and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| C1 | A press without a prediction/falsifiable claim is refused for free. | `README.md:33-44`, `README.md:93-97`; `SKILL.md:36-48` — doctrine/design. | Explicit and repeated. | R4 | None. | None. | A nonempty parseable prediction and publicly available action are required before `broker_step`; rejection therefore precedes a paid action in the inspected call order. | Any unrecognized free prose is accepted as generic `change`; evidential support, specificity, and mechanic falsifiability are not checked. No live refusal was observed. |
| C2 | Each prediction is graded; a pass leaves the game model standing, while a miss dates where belief and reality diverged/corrected the agent. | `README.md:45-57`; `SKILL.md:40-59` — doctrine/design. | The grammar and compare loop are specified. | R5, R6 | None; only a synthetic grader branch probe. | None. | The harness records which immediate claim predicates match the returned settled result and localizes a miss to an event/claim. | One claim pass does not test the whole game model; a miss does not expose which belief or explanation failed; agent correction is instructed but not enforced or observed. |
| C3 | Proven mechanics can be batched, and execution halts on the first miss. | `README.md:65-74,114-119`; `SKILL.md:61-74` — doctrine/design. | Explicit batch rule. | R6 | None. | None. | Per-step claims are graded sequentially; miss or terminal state discards the remaining queue. | "Proven" has no implemented criterion. No evidence shows the agent batches only warranted mechanics or that halting improves outcomes. |
| C4 | A one-page notes file preserves verified/assumed/refuted knowledge through context compaction and is repaired after misses. | `README.md:79-89`; `SKILL.md:50-59` — doctrine plus reported operation. | Skeleton, headings, update instruction, and status recovery are specified. | R7, R8 | None; reported campaign note lengths/compactions only. | None. | The file is created once, displayed by status, and archived on level completion. | Page size, headings after creation, citations, `Verified`, refutation, and post-miss repair are not validated. Compaction survival and actual later use are unobserved. |
| C5 | Earlier verified mechanics are only assumed on a new level until one test survives. | `SKILL.md:77-82` — doctrine/design. | Explicit instruction. | R8, with possible evidence from R5/R6 | None. | None. | Status may warn when the note file has not been modified since the prior level archive. | The implementation checks only `mtime`; it neither demotes claims nor requires/links a test. Any edit removes the warning. |
| C6 | Executable rules are replay-verified against the entire recorded history, with honest gaps; a fitting model can be searched. | `README.md:104-112`; `SKILL.md:89-107`; `rules.py:1-59` — doctrine/design. | Detailed contract and gap language. | R9-R14 | None; synthetic replay branches only. | None. | The implementation distinguishes mismatch, explicit/inability gaps, and no-gap history fit under pixel, projection, and terminal checks; mismatch blocks search. | `INCOMPLETE` also permits search; `observe` may be lossy; reset transitions are re-grounded rather than stepped; history fit does not establish unseen mechanics or causal explanation. No actual model fit was observed. |
| C7 | Every model-generated plan step has a prediction and live execution stops at the first surprise. | `README.md:65-74,104-112`; `SKILL.md:89-107` — doctrine/design. | Explicit plan-execution rule. | R14-R18 | None. | None. | The plan file contains one expectation per action; provenance is gated, and each returned step is compared before continuation. | Some checks use only the model's `observe` projection. A fresh plan or prior history fit is not external-game endorsement. |
| C8 | Local `start` is idempotent/crash-safe and replays the run exactly; remote competition does not recover. | `README.md:176-181`; `SKILL.md:9-23` — doctrine/design. | Explicit mode distinction. | R19, R20 | None. | None. | Local restart re-executes the mutation journal in a fresh current simulator and requires exact encoded observations; orphan mutations are reconciled; remote loss is rejected as unrecoverable. | No run replay pass is present. The license is current simulator/cache/seed and public observation, not cross-version/private-state equivalence. |
| C9 | The reported campaign completed 25/25 games and 183/183 levels at RHAE 100 with 7,645 actions; all recorded presses replayed without divergence. | `README.md:16-30,227-230` — reported operation. | Publicly asserted with a scorecard link. | R19/R20 can implement local replay mechanics; completion metadata can be recorded in O1. | None within the boundary; linked scorecard and run corpus not inspected. | None. | Only that the repository reports these outcomes and contains routes capable of recording completion and checking local replay. | The checkout cannot substantiate the counts, score, or replay result. It contains no campaign events and ignores `.arc/`. |
| C10 | Across the campaign there were 7,627 graded predictions/443 misses, notes survived 115 compactions, tools were used at reported frequencies, and planned presses missed much less often than single probes. | `README.md:49-51,79-89,98-119` — reported operation. | Publicly asserted. | R5-R8, R12-R18, R21 provide corresponding capabilities. | None within the boundary. | None; the compared action modes are selected under different uncertainty/task conditions. | Only that the implementation could generate these artifact kinds and that the README attributes these measurements to a campaign. | Counts, selection process, denominators, note contents, and raw traces are missing. The miss-rate contrast cannot identify planning, prediction, notes, or another component as the cause. |

## 6. Bounded conclusion

- O1 is acquired, not produced. R1 preserves the ARC interface's returned public frames and metadata in a typed local representation. R19/R20 can preserve and check action-observation lineage. The source's interface-level warrant is preserved under exact encoding and equality checks, but the environment's own truth, completeness, and private state remain unknown because neither the environment nor an independent oracle was inspected.

- O2 is non-ampliative reshaping or an entailed derivation in a narrow array domain. R2 warrants such claims as which represented cells differ, what a crop contains, or whether hashes identify the same settled grid. Its consumers are the external agent, replay/provenance code, and offline analysis through CLI text, images, JSON, and arrays. It does not produce a semantic game mechanic.

- O3 does generate ampliative semantic candidates from O1/O2, including movement, lattice, component, and click-salience interpretations. R3 has no evidence-consuming test or acceptance transition. Caching/display lets those candidates influence a later external agent, but this channel is advisory and its horizon is the current dossier/context. No candidate produced by R3 is warranted as knowledge within the inspected boundary.

- O4 is ARC-skill's clearest knowledge-production route. An external agent conjectures a truth-apt consequence of one action. R4 admits it on syntax/nonemptiness and public action availability, which grants operational permission for that action but no epistemic authority. R5 tests the candidate against the returned next settled result; R6 does the same inside a queue. When its predicate passes, the accepted scope is one realized action/event under the particular grammar, the intended uses are event reporting and, in R6, permission to execute the next queued step, the consumers are the event/history display and batch executor, the channels are persisted grade/receipt and in-memory control, and the force lasts for the run record or one queue transition. A miss rejects that event-level prediction. Neither result warrants the agent's explanation, the whole model, intermediate dynamics, transfer, or a general mechanic.

- O5 is therefore narrow checked knowledge about the relation between a named prediction and a returned observation, conditional on the ARC public interface and the claim predicate. This route produces more than mere storage or later use because it consumes evidence and records a pass/fail disposition. The checkout nevertheless contains no actual O4/O5 instance, so no claim can be made that an ARC run acquired such knowledge, revised a belief, or benefited from it.

- O6 retains possible knowledge claims but does not itself warrant them. R7 gives natural-language notes a durable future-agent consumer through `status` and a per-level archive. It does not validate evidence, truth, the `Verified` label, or post-miss correction. R8's consumer is also the future agent, but its channel is only an `mtime`-based warning and its force is advisory until any edit. Mechanic conjecture, testing, acceptance, and integration in actual notes are `not determinable`; the project explicitly leaves the acceptance criterion to the agent.

- O7 can encode a mechanic conjecture as executable rules. R10 can test exact rendered consequences, R11 can test an author-selected projection, and R12 can test recorded terminal consequences. R13 accepts only the bounded proposition `HISTORY_FIT` when no implemented gap or mismatch occurs over the checked history. Its intended use is historical fit assessment and search input; its scope is the recorded transitions and chosen comparison domain. `MISMATCH` operationally blocks O9 search, while `INCOMPLETE` and `HISTORY_FIT` both permit it. This means operational continuation is deliberately weaker than epistemic acceptance. A history-fit result would warrant retrospective fit, not unique explanation, hidden-state fidelity, unseen mechanics, transfer, or that the model produced an observed success.

- O9 is derived from O7 by R14. A found path is warranted as goal-reaching within the executable model's formal domain, provided its transition functions are the operative premises. The truth of those premises about the external game is not established by search, and R13 may have admitted an incomplete model. R15 checks only whether plan provenance still applies to the current event, board, and rules file; freshness does not endorse the plan.

- O10 turns model-internal consequences into external-game conjectures. R16 accepts an exact settled-board prediction for one executed step; R17 accepts only an author-selected observation projection; R18 accepts only level advance at the named step. Their intended use is current-plan continuation, their consumer is the live executor, their channel is the in-memory comparison plus receipt, their force is to execute the next step or halt/discard the suffix, and their horizon is one transition. Passing steps do not warrant the unexecuted suffix or the general rules model.

- O11 supports a separate replay-knowledge route. If R19 passes, it warrants that the recorded public action-observation sequence reproduces exactly under the current local game cache, seed, simulator, and journal. The broker/start consumer uses this through a startup gate to allow continuation or abort on divergence. R20 warrants journal/event continuity and current-head consistency. Neither route establishes cross-version replay, remote recovery, private-state identity, game rules, or the causal effect of replay. With no journal in the checkout, no actual replay pass can be asserted.

- O12 supplies arbitrary computation but no fixed truth-apt object, evaluator, acceptance criterion, retention channel, or force. Any entailed derivation or conjecture produced there inherits the warrant of its particular program and premises. Its stdout may affect an external agent, but the inspected source does not show that continued-use route in operation.

- The only implemented behavior changes evidenced without inspecting the external model are control-flow changes: R6 and R16-R18 continue or stop queued actions, R13 admits or refuses search, R15 admits or refuses a plan, and R19/R20 admit or refuse run continuation. These are operational adaptations keyed to checks, not evidence of model-weight learning or a changed agent policy. Status nudges are advisory. The external agent's belief/policy response is not determinable.

- The public campaign results, prediction/miss counts, note-compaction behavior, tool-use frequencies, model use, scorecard, and replay success remain reported operation only. No implementation inspection establishes that these routes ran in the reported campaign, and no causal evidence attributes any outcome to prediction gating, notes, batching, planning, offline computation, or another component. ARC-skill therefore has several route-bounded mechanisms capable of producing checked event facts and retrospective fit/replay facts, but the source boundary supports no system-wide epistemic verdict and no unqualified claim that it produced general game knowledge in operation.

## Cold-execution notes

- The lifecycle schema asks for one phase state per candidate, while this checkout contains route implementations but no run-instance candidates. I used `not determinable` for actual ARC dispositions and separately stated which generation, test, acceptance, and integration transitions are implemented.
- "System" could mean the harness alone or the larger agent/harness/ARC environment. I fixed the scope to inspectable ARC-skill-mediated routes and recorded the external agent, dependency internals, game source, and servers as evidence gaps rather than silently treating their behavior as implementation evidence.
- No required field appeared to be missing, and no clarification from the requester was needed.
