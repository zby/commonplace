---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of the instruction-only recall skill (recall/) of Parcha-ai/parcha-skills at c82883b1: the find/verify outcome from request to receipt-backed answer, with its match-evidence check, empty-result recovery and stop paths"
run-id: AAS-2026-11-05-parcha-skills-d5ad184aa4af-01
reviewed-boundary: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
---

# Recall (parcha-skills) workflow report

## Workflow account

### Selection and what the account can establish

The traced workflow is the local **find/verify** outcome: a user asks whether
or how earlier work happened, and the host model answers from a retrieved
prior session with the session path as its receipt. It is selected because it
is the skill's first-listed outcome and the base of the other three. Continue,
repeat and skill-ify reuse its search and read steps and change only what is
read and delivered (SRC-1, `recall/skills/recall/SKILL.md`). It is also the
only workflow whose acceptance, rejection and recovery steps are all stated in
the shipped package. The runtime baseline gives its route as
[RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read); this account
traces the decisions inside that route and the branches that end it.

> Search, read the best hit's relevant window, answer with the session path
>    as the receipt.
> --- `recall/skills/recall/SKILL.md`

Evidence limits apply to every step. The procedure is natural-language
instruction to the host model ([RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions)).
Its text establishes what the model is asked to do, not that any model does
it. The engine that ranks, gates and prints results
([RT-CMP-recall-engine](runtime.md#rt-cmp-recall-engine)) is absent from SRC-1
([RT-ABS-engine-code](runtime.md#rt-abs-engine-code)). SRC-1 contains no
Recall run trace, so no step below is observed.

### Participants and handoffs

The workflow has three participants and no agent-to-agent delegation
([WF-ABS-agent-delegation](#wf-abs-agent-delegation)).

| Participant | Role in the workflow | Evidence layer |
|---|---|---|
| User | Supplies the question; resolves an ambiguous outcome; receives the answer | `implementation` (instruction to ask) |
| Host model ([RT-CMP-host-model](runtime.md#rt-cmp-host-model)) | Chooses the outcome, writes the query and filters, judges match evidence, chooses the window, writes the answer | `implementation` (instruction) |
| Recall engine | Ranks sessions, applies its evidence gate, prints `WHY` lines and `show` windows | `doctrine/design` only |

The handoffs run in this order:

1. **User → model: the request.** The host loads the skill when its
   description matches. Selection is host behavior outside the boundary. The
   model classifies the request among four outcomes. It asks the user only
   when the classification is unclear:

   > Ask only if the outcome is genuinely ambiguous.
   > --- `recall/skills/recall/SKILL.md`

2. **Model → interface decision.** [RT-RTE-interface-selection](runtime.md#rt-rte-interface-selection)
   either routes to the local CLI, routes to the remote Brain procedure, or
   stops with a dependency report. The stop is the workflow's first terminal
   failure. It delivers a report, not an answer, and it forbids recovery by
   fetching archived engine code.

3. **Model → engine: the query.** The model supplies the user's phrasing,
   any identifiers it has, and filters as flags (time, cwd, harness, branch).
   The skill's stated reason for including identifiers is evidential strength:
   they are "the strongest evidence and are matched exactly"
   ([RT-CLM-exact-identifier-matching](runtime.md#rt-clm-exact-identifier-matching)).
   The model also converts local days to UTC bounds. The engine's handling of
   these inputs is declared contract only.

4. **Engine → model: candidates.** The engine returns ranked sessions with a
   snippet and a `WHY` line, or empty output when nothing cleared its evidence
   gate ([RT-CLM-evidence-gate](runtime.md#rt-clm-evidence-gate)). A missing
   index produces a different return, which hands off to
   [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan).

5. **Model: acceptance of a candidate.** This is the workflow's verification
   step, [WF-RTE-match-evidence-check](#wf-rte-match-evidence-check). The
   model reads the `WHY` lines of the top few results and selects by match
   evidence, not rank. A candidate whose `WHY` shows only generic words is
   weak evidence. Rejection here is a judgment, not a code gate. The gotcha
   list states why it matters: lexically adjacent sessions can appear for
   work that never happened.

6. **Model → engine → model: the bounded read.** `show <path> --around
   <timestamp>` returns a ±3-turn window around the matched time. The handoff
   supplies the exact session path from the search output and the timestamp
   printed there. The skill gives size as the reason for this bounded read.

7. **Model → user: delivery.** The model answers with the session path as
   the receipt.

### What verification can accept or reject

Two checks can reject material before delivery; both are stated in the skill
and both depend on other components.

- **Engine evidence gate (declared).** The engine is said to suppress
  results that do not clear a gate. Its criterion is not stated in SRC-1. The
  model cannot inspect or adjust it beyond rewording the query or widening the
  window.
- **Model match-evidence check (instructed).** The model is asked to reject
  generic-word matches and to read `WHY` before asserting that a session
  answers the question. Nothing records the judgment, and nothing checks it.

No step checks the delivered answer against the shown window. No code path,
second agent or user approval step does so
([WF-ABS-independent-answer-check](#wf-abs-independent-answer-check)). The
receipt lets a reader check the answer afterwards; the skill does not ask
anyone to do so. The remote variant has a stricter citation rule. The model
may cite only opened receipts whose text supports the answer, and it must
state gaps when evidence is clipped, unavailable or incomplete:

> Cite only `opened_receipts` whose returned text supports the answer. State
> gaps when evidence is clipped, unavailable, or incomplete.
> --- `recall/skills/recall/references/central-brain.md`

That is still model-enforced. The local find/verify playbook has no matching
instruction to state clipped evidence. Its ±3-turn window can omit context,
and the skill does not say what the model should do when the window is
insufficient beyond reading again.

### Failure and recovery

The host model recovers from every failure; nothing else does. The skill
defines four failure branches:

| Failure | Recovery owner and action | Terminal result |
|---|---|---|
| No interface (no MCP tools, no central signal, no `RECALL_SCRIPT`) | Model reports the missing dependency and stops | Dependency report; no answer |
| Index missing (`search` reports no index, or `doctor` shows `db exists=False`) | Model runs a raw-transcript `rg` scan and starts a detached `index` build ([RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)) | Answer labelled as coming from a cold scan |
| Empty search output | Model retries once with a distinctive identifier or a wider window, then reports ([WF-RTE-empty-result-recovery](#wf-rte-empty-result-recovery)) | Report of what was searched and that no supported match was found |
| Stale-looking results | Model runs incremental `index` ([RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance)); `index --rebuild` needs explicit user request | Retry of search; no separate terminal state is stated |

The retry budget is explicit: one retry, then a bounded negative report. That
report is not a claim that the work never happened. SKILL.md says empty
output "does not prove the work never happened". The cookbook's scripting
note calls empty stdout a "confident no-answer". The runtime baseline records
this wording conflict under G5. In this workflow, the SKILL.md wording
governs the user-facing report, because it is the instruction attached to
the search step. The cookbook line describes `--paths` scripting output.

A wrong but non-empty hit has no recovery route other than the
match-evidence check. If the model accepts a lexically adjacent session, no
later step in the workflow detects the error.

### What makes the result delivered

Delivery is an answer in the host session that names the session path as
receipt. The cold-scan branch adds a label, and the remote variant cites
opened receipts and states gaps. The workflow defines no other completion
criterion. The skill writes no record of the answer. It does not persist the
query, the rejected candidates or the receipt
([RT-OBJ-recall-receipt](runtime.md#rt-obj-recall-receipt) persists only if
the answer repeats it). The found session can be delivered to another skill
instead of to the user. `recap` tells its agent to find a prior session with
Recall and then pass "its exact path or stable receipt"; it stops on
ambiguous identity rather than choosing by time (SRC-1,
`recap/skills/recap/SKILL.md`):

> If identity is ambiguous, stop with the candidates. Never choose the nearest transcript by time.
> --- `recap/skills/recap/SKILL.md`

That stop rule and the page checks in `recap/skills/recap/scripts/recap.py`
belong to `recap`, which is outside the functional boundary. They show a
consumer that rejects an unsupported handoff. They are not a Recall
verification step.

### Evidence limits and unsupported steps

- Successful execution, compliance with the `WHY` instruction, retry
  behavior and answer quality are unobserved; no trace exists in SRC-1.
- The engine's ranking, gate criterion and `show` window extraction are
  declared only; whether the window printed contains the matched text is
  uninspected.
- Host skill selection, which starts the workflow, is outside the boundary.
- Absence findings below cover the eight shipped `recall/` files at the
  reviewed commit. They do not cover the engine, the Brain service or host
  behavior, which could add checks this package does not show.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-match-evidence-check

Label: Match evidence check

Part of: [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read)

This is the candidate-acceptance step inside the runtime's local search
route. It is declared separately because its decision owner, criterion and
failure mode differ from the engine's ranking and from the read step. No
other supplied record covers it; [RT-CLM-evidence-gate](runtime.md#rt-clm-evidence-gate)
is the engine's prior filter, a distinct referent.

- Endpoints: ranked search output → one accepted session path and timestamp,
  or no accepted candidate.
- Progression: read `WHY` on the top few results → discount generic-word
  matches → prefer identifier, phrase or exact-entity matches over rank 1 →
  pass the chosen path and printed timestamp to `show --around`.
- Owner: host model ([RT-CMP-host-model](runtime.md#rt-cmp-host-model)); the
  engine supplies the `WHY` text.
- Context/state/action effects: decides which session window enters context;
  writes nothing.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: the selected session path and timestamp, held in the model's context.
- Later read-back: inapplicable — the judgment and the rejected candidates are not retained.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: model judgment of engine-produced `WHY` match evidence; identifiers, phrases and exact-entity matches outrank generic words.
- Invalidation or expiry: inapplicable — evaluated per search.
- Activation or effect: determines the window from which the answer is written; activation is unobserved.
- Evidence limits: the `WHY` format and its relation to the engine's actual scoring are declared only; model compliance is unobserved.

> Matches on only generic words
> are weak evidence.
> --- `recall/skills/recall/SKILL.md`

> A query about work that never happened can still return lexically-adjacent
>   sessions.
> --- `recall/skills/recall/SKILL.md`

Conditional fields (candidate comparison): the engine proposes ranked
candidates; the host model decides; the user can veto only after delivery or
by redirecting the conversation. No answer oracle: `WHY` is match evidence
produced by the engine, not an expected answer. Operating mode: open
requests.

#### WF-RTE-empty-result-recovery

Label: Empty result recovery

Part of: [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read)

This is the failure branch of the runtime's local search route when search
output is empty. It differs from [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan),
which handles a missing index, not an empty result from an existing index.

- Endpoints: empty search output → one retry → either candidates (rejoining
  [WF-RTE-match-evidence-check](#wf-rte-match-evidence-check)) or a bounded
  no-match report to the user.
- Progression: retry once with a distinctive identifier or a wider window →
  if still empty, report what was searched and that no supported match was
  found.
- Owner: host model.
- Context/state/action effects: a second search call; the terminal report
  enters the conversation; no write.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: the retried search output, or nothing.
- Later read-back: inapplicable — neither query is retained by the skill.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: empty output from `search`; the retry query is the model's choice of identifier or window.
- Invalidation or expiry: inapplicable — single retry per request.
- Activation or effect: bounds the search effort and fixes the negative report's content; activation is unobserved.
- Evidence limits: whether empty output means "nothing cleared the gate" depends on the absent engine; the cookbook's "confident no-answer" wording conflicts at face value with the instruction not to treat empty output as proof.

> Retry once with a distinctive
>   identifier or a wider window. If output is still empty, tell the user what
>   you searched and that no supported match was found.
> --- `recall/skills/recall/SKILL.md`

### Claims

none declared in this member

### Evidenced absences

#### WF-ABS-independent-answer-check

Label: No independent answer check

No supplied counterpart after comparison:
[RT-ABS-engine-code](runtime.md#rt-abs-engine-code) concerns absent engine
code, and [RT-ABS-tool-restriction](runtime.md#rt-abs-tool-restriction)
concerns tool grants.

- Status: absent
- Searched: all eight tracked files under `recall/` at
  `c82883b15e5e8f02483bee513b3c8dcac48e3c9e`, with `SKILL.md`,
  `references/central-brain.md` and `references/query-cookbook.md` read in
  full; query `grep -rn -i -E "subagent|delegat|spawn|verify|confirm|review"`
  over `recall/`.
- Evidence: the matches are the outcome name "Find / verify", the repeat
  playbook's "confirm fresh inputs", the indexed-subagent gotcha and a sample
  query string. No step asks code, another agent or the user to check the
  delivered answer against the read window. The only answer-side rules are
  instructions to the answering model itself: the receipt and, remotely,
  citing supporting opened receipts.
- Conclusion supported: within the shipped package, the find/verify answer
  is accepted by the same model that wrote it, and nothing verifies it before
  delivery. Conclusion prevented: whether the engine, the Brain service or a
  host adds such a check, since these are outside SRC-1.

#### WF-ABS-agent-delegation

Label: No agent delegation

No supplied counterpart after comparison; the runtime account states
single-agent coordination in prose but declares no record for it.

- Status: absent
- Searched: the same eight `recall/` files at
  `c82883b15e5e8f02483bee513b3c8dcac48e3c9e`, same query.
- Evidence: the only subagent mentions describe subagent transcripts as
  indexed sessions. No step delegates work to another agent or sub-agent.
  Skill-ify hands a recipe to an external skill creator, which is a tool
  handoff outside the find/verify workflow.
- Conclusion supported: the find/verify workflow runs in one host-model
  context, with the engine as a tool and the user as requester. Conclusion
  prevented: whether a host runs the skill inside a sub-agent; that is host
  behavior outside SRC-1.

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read)

- Workflow role: the representative workflow traced in this member; its
  acceptance step is [WF-RTE-match-evidence-check](#wf-rte-match-evidence-check)
  and its empty-output failure branch is
  [WF-RTE-empty-result-recovery](#wf-rte-empty-result-recovery).
- Delivery criterion: an answer naming the session path as receipt; no
  persisted completion record.
- Verification of delivered answer: none in the package
  ([WF-ABS-independent-answer-check](#wf-abs-independent-answer-check)).

#### On [RT-RTE-interface-selection](runtime.md#rt-rte-interface-selection)

- Workflow role: first terminal failure branch; delivers a dependency report
  and forbids recovery by fetching archived engine code.

#### On [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)

- Workflow role: recovery branch for a missing index; its delivered answer
  must carry a cold-scan label, the only provenance label the local workflow
  requires besides the receipt.

#### On [RT-RTE-session-export](runtime.md#rt-rte-session-export)

- Workflow role: alternate delivery of a found session to another skill
  instead of to the user; the receiving `recap` procedure stops on ambiguous
  identity, a consumer-side rejection outside the functional boundary.
