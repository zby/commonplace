# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/instructions/analyse-agentic-system/SKILL.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/instructions/analyse-agentic-system/SKILL.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

This skill is too long to load comfortably. Get it to about three-quarters of its current length without changing what the executing agent does. Also add a line on where the result goes when the system under analysis is mainly a memory system, since the agent-memory-systems collection exists for those.

## Retained intent

Source: retained commission for this document. Subject: `kb/instructions/analyse-agentic-system/SKILL.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: analyse-agentic-system skill

## Governing question

What single procedure lets an agent analyse one external agentic system — a runtime, harness, orchestration framework, agent operating layer, or any narrower system whose deployed behavior depends on model calls — and return a bounded, evidence-disciplined synthesis that covers runtime structure, memory/context, and epistemic handling without the three views drifting apart?

## Audience and reader update

The executing reader is an orchestrating agent (forked context, Opus) that has been handed a system identifier and some source input, with no prior conversation. A secondary reader is the maintainer editing the skill. The executor should finish able to run the whole analysis end to end: open a run, freeze evidence, fix vocabulary and record ownership, run a runtime baseline, run both lenses at proportionate depth, reconcile, and emit one logical result with verification. It should not need to open other documents except the epistemic procedure it is told to invoke.

## Target claim or purpose

Replace separate, loosely coupled reviews of external systems with one owned run: one run ID, one declared boundary of a stated kind, one frozen evidence cutoff, one source register, one set of canonical records that every lens cites, and one synthesis organized around how the deployed system progresses rather than as concatenated lens reports. Both lenses always run; evidence decides depth, never whether. The result must never claim more than its evidence layer and boundary support.

## Must keep

- The opening goal, consumption path (explicit invocation or trigger-matched loading), and the explicit prohibitions: no rankings, generic adoption advice, universal taxonomy or maturity ladder, or claims beyond the evidence boundary. The skill owns the whole run; lens workers never set boundary or publication.
- Hard stops: no reachable source means stop, never analyse from recollection; no coherent boundary or no stable inspectable evidence means a blocker report.
- The scope test with both routes (named system kinds; narrower systems whose behavior depends on model calls they issue or serve), including systems whose model runs outside their boundary, such as MCP servers and tools; an out-of-scope exit.
- A functional boundary definition and the three boundary kinds (whole-system, subsystem-only, complete artifact with partial loop), each bounding what may be concluded, with external participants listed as exclusions paired with the conclusions they prevent.
- Source freezing branched by source kind, a single analysis cutoff, per-layer evidence recording for mixed sources, and the rule that the evidence packet is finalized only after the runtime baseline mints canonical records. Lens workers never reacquire or widen sources; targeted reads are registered centrally and invalidate dependent findings.
- The evidence vocabulary: one overall tier judged over in-boundary material loops; five per-source evidence layers; exactly seven conclusion statuses; the non-upgrade rules; and the explicit separation from the epistemic procedure's `implemented` status, so the two vocabularies never merge.
- Self-sufficient definitions of memory read-back (per-instance, consumer-invocation boundary, derived values count), activation, truth-apt, and behavioral authority as consumer/channel/force/horizon, kept separate from epistemic and operational authority.
- The canonical record table with ownership; orchestrator-only ID minting, lens-local proposal tags with identity for merge; evidenced absences only when they bound a conclusion; the correction branch for defective records (including accurate-but-misleading); amendments for returns that fit no record kind.
- Worker topology: prefer fresh workers on the prepared packet, fall back to sequential execution, otherwise stop with a capacity blocker. A written artifact outranks a worker's self-report or a harness failure notice.
- The mandatory runtime baseline per material loop, with the anti-conflation rules and conditional inspection of other surfaces only when material.
- Lens scoping records for both lenses, the brief-output floor, `uncertain` never an exit, and the direct-adaptation exception handed to the epistemic procedure as classify-only.
- The memory/context lens items, including representational form defined inline, write side versus read-back, presence versus wiring versus activation versus effect, and what to omit.
- Invocation of the epistemic procedure by path without restating its method, with the handoff contents and wrapper rules.
- Reconciliation ownership, eleven logical records in reading order (not writing order, not physical layout), the publication rule (only into an authorized contract that can represent the result, otherwise stage and report a blocker), and verification including the explicit distinction checklist and the "no deterministic validation applicable" case.

- The explicit record of the skill's own consumption path in the opening (consumer, channel, force), so a maintainer editing it knows the edit deploys to the next run.
- The ordering dependency spelled out where it bites: the evidence tier (record 2) is judged over the runtime baseline, so it is written after step 4 but presented first.

## Exclusions

- No physical file layout, collection contract, or reuse of the agent-memory review schema; publication targets are not invented here.
- No restatement of the epistemic route-analysis method.
- No checkout or publication mechanics, Commonplace comparison, borrowable ideas, or watch items in the memory lens; transfer to Commonplace is a separate skill's job.
- No system-wide epistemic grade.
- Rationale for the design lives in linked notes through `rests-on`, not in the body.

## Scope, modality, and terminology

Prescriptive, imperative, executable on first reading, with explicit decision branches and stop conditions. Use the fixed status strings and ID prefixes exactly. Say "orchestrator" for the executing agent throughout. Keep "retained state", "read-back", "activation", "boundary", and "evidence layer" as defined terms and do not substitute synonyms. Frontmatter carries the harness fields for a forked, user-invocable skill.

## Reserved decisions

- Adding or renaming a conclusion status, record kind, or boundary kind; downstream results and the transfer-scan and landscape-synthesis skills depend on them.
- Making either lens optional or conditional.
- Fixing a physical result layout or creating a result contract or publication target.
- Merging the epistemic procedure into this skill or changing its invocation interface; that sibling must change in the same edit.
- Changing the model, context, or tool permissions in frontmatter.
