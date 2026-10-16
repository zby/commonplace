---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "EQUIPA epistemic routes: software verdicts, retained experience and evidence-responsive instruction changes, with bounded warrant."
run-id: AAS-2026-10-15-equipa-32016e8dd9ae-01
reviewed-boundary: fa8f41a6948584ee53e804edbb08b7449d05cd14
---

# EQUIPA epistemic report

## Source-and-claim boundary

This asks which EQUIPA outputs can bear truth, what checks license reliance, and which results actually control later work. The frozen source and external-engine exclusions are those of the [boundary and Source register](boundary.md#source-register). All findings below use SRC-1 at that revision. Source inspection establishes implementation or doctrine, not exercised behavior. No run trace, production database, deployed configuration, independently checked output or causal experiment was supplied.

The supplied runtime is a provisional source-grounded account, not an inspection limit. Direct reads added the paths below. Uninspected included operations remain limits, not exclusions or absences. This is not a system-complete negative about acceptance, theory building or learning.

| Entry point or operation | Source path | Coverage and records | Remaining limit and prevented conclusion |
|---|---|---|---|
| Package/root CLI, task and alternate providers | `equipa/cli.py`, `equipa/dispatch.py`, `equipa/loops.py`, `equipa/agent_runner.py`, `ollama_agent.py` | Direct CLI mode-selector cross-check (MCP, initiatives, config, manifest, add/setup, auto, parallel goals, goal, tasks, default task); supplied [RT-RTE-dev-test](runtime.md#rt-rte-dev-test), [RT-RTE-gated-merge](runtime.md#rt-rte-gated-merge), [RT-RTE-ollama-tools](runtime.md#rt-rte-ollama-tools), [RT-RTE-isolated-agent](runtime.md#rt-rte-isolated-agent) | No independent full reread; project-test validity and real results unavailable |
| Goals, RLM and role extensions | `equipa/manager.py`, `equipa/rlm_decompose.py`, `equipa/role_resolver.py` | Supplied [RT-RTE-goal-rounds](runtime.md#rt-rte-goal-rounds), [RT-RTE-rlm-review](runtime.md#rt-rte-rlm-review), [RT-RTE-role-extension](runtime.md#rt-rte-role-extension) | No execution; completeness of review and goal satisfaction unestablished |
| MCP registry and retained-content handlers | `equipa/mcp_server.py` | Direct registry and lessons/logs/context/notes handlers; [EPI-RTE-mcp-retrieval](#epi-rte-mcp-retrieval); dispatch/create/status principally supplied runtime/boundary | Create/status validation not independently audited; no client use evidence |
| Lifecycle checks | `equipa/hooks/__init__.py`, `hooks/preflight_build.py`, `hooks/post_agent_lint.py` | Registry/caller supplied [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks); direct build/lint bodies in [EPI-RTE-hook-checks](#epi-rte-hook-checks) | Built-in plugin bodies and deployed registrations uninspected; no universal veto |
| PreToolUse and integrity admission | `hooks/pretooluse_bash_gate.py`, `equipa/security.py` | Supplied [RT-CLM-skill-integrity](runtime.md#rt-clm-skill-integrity) and runtime controls account; file/function search only for Bash hook | No independent classifier audit or deployed activation evidence |
| Episodes and reflection | `equipa/reflexion.py`, `equipa/lessons.py`, `equipa/prompts.py`, `lesson_sanitizer.py` | Direct generation, storage, sanitizer entry/markup/caps, injection and value updates; [EPI-RTE-episode-memory](#epi-rte-episode-memory), [EPI-RTE-episode-values](#epi-rte-episode-values) | Episode ranking internals, embedding provenance and sanitizer detector internals incompletely inspected; semantic preservation unestablished |
| Failure rules | `scripts/forgesmith_simba.py`, `forgesmith.py` | Direct synthesis prompt, validator/store, before/after scorer/pruner, template generator and active lesson query; [EPI-RTE-simba-rules](#epi-rte-simba-rules) | Full optimizer and template-extraction callers not audited; no actual rules supplied |
| Positional context handling | `forgesmith_litm.py`, `equipa/prompts.py` | Direct audit detector/weight update and actual reordering; [EPI-RTE-context-reorder](#epi-rte-context-reorder) | Numerical weights do not enter the inspected reordering logic; attention benefit unestablished |
| Prompt/config evolution | `forgesmith.py`, `forgesmith_gepa.py`, `scripts/autoresearch_loop.py` | Supplied [RT-RTE-forgesmith-changes](runtime.md#rt-rte-forgesmith-changes), [RT-RTE-gepa-prompts](runtime.md#rt-rte-gepa-prompts), [RT-RTE-autoresearch-prompts](runtime.md#rt-rte-autoresearch-prompts) | OPRO/GEPA numerical internals and complete rollback semantics not independently inspected |
| Output rubric | `rubric_quality_scorer.py` | Direct scoring functions; [EPI-RTE-rubric-scores](#epi-rte-rubric-scores); runtime supplies ForgeSmith scoring caller | Persistence consumer beyond supplied runtime not deeply traced; no quality validation data |
| Training utilities | `tools/ingest_training_results.py`, `tools/prepare_training_data.py` | Direct marker validator/insert/process; export function inventory only; [EPI-OBJ-training-marker](#epi-obj-training-marker) | Import records external claims, not weight training; export and downstream model consumers uninspected, preventing a whole-system no-training conclusion |
| Interactive session/context maintenance | `.claude/skills/forge-end/SKILL.md`, `equipa/tasks.py`, `equipa/sessions.py` | Boundary supplies instruction-driven writes and later reads; MCP context consumer inspected | Full interactive skills and maintenance/revision contracts uninspected; knowledge acceptance there not determinable |
| Other included drivers/evaluators | `equipa/initiative_runner.py`, `tools/forge_arena.py`, `scripts/equipa_harness_sweep.py`, `scripts/nightly_review.py`, `skills/`, `tests/` | Supplied boundary inventory/shared task routes only | Measurement semantics, skill-specific criticism and complete alternate scheduling not independently inspected; prevents system-complete claims |

Consequential public claims are [EPI-CLM-self-improvement](#epi-clm-self-improvement), [EPI-CLM-semantic-memory](#epi-clm-semantic-memory) and [EPI-CLM-task-testing](#epi-clm-task-testing). The integrity claim is already declared as [RT-CLM-skill-integrity](runtime.md#rt-clm-skill-integrity). No source-native general guarantee of producing true scientific theories is established by these passages.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-task-branch](runtime.md#rt-obj-task-branch) | Code/artifact candidate; behavior and task satisfaction propositions depend on task/domain | Product | See record | Tests are not the product itself |
| [EPI-OBJ-agent-episodes](#epi-obj-agent-episodes) | Approach/outcome descriptions and explanations of failure or success | Past experience | SRC-1, `equipa/lessons.py`, `equipa/reflexion.py` | No actual episode; truth-apt unit contents not determinable |
| [EPI-OBJ-lessons-learned](#epi-obj-lessons-learned) | Descriptive premises and behavioral advice; imperative alone is policy, not a truth assertion | Lessons/rules | SRC-1, `scripts/forgesmith_simba.py`, `forgesmith.py` | Specific generated propositions unavailable; rationale requested but omitted by inspected SIMBA insert |
| [RT-OBJ-role-prompts](runtime.md#rt-obj-role-prompts) | Mostly instructions, possibly descriptive claims | Role authority | See record | Mutation can change policy without producing knowledge |
| [EPI-OBJ-episode-q-value](#epi-obj-episode-q-value) | Bounded feedback priority, not a truth estimate | Episode ranking | SRC-1, `equipa/lessons.py` | Uniform outcome reward does not isolate usefulness |
| [EPI-OBJ-effectiveness-score](#epi-obj-effectiveness-score) | Difference in recorded success rates | Rule pruning | SRC-1, `scripts/forgesmith_simba.py` | Association, not causal effect |
| [EPI-OBJ-rubric-scores](#epi-obj-rubric-scores) | Computed lexical/file-indicator scores | Maintenance measurement | SRC-1, `rubric_quality_scorer.py` | Not independently validated quality |
| [EPI-OBJ-prior-summary](#epi-obj-prior-summary) | Supplied prior-work descriptions | Reordered history | SRC-1, `equipa/prompts.py` | Formatting preserves sections, not necessarily source order |
| [EPI-OBJ-training-marker](#epi-obj-training-marker) | Imported training provenance and claimed accuracy statistics | Model registry metadata | SRC-1, `tools/ingest_training_results.py` | Structural/range validation does not reproduce training or measurement |
| [RT-CMP-claude](runtime.md#rt-cmp-claude), [RT-CMP-ollama](runtime.md#rt-cmp-ollama) | Distributed-parametric inference state opaque | Candidate/evaluator providers | See records | Parameter changes, exact weights and mutable endpoint contents uninspected; no inference from prompt evolution to weight learning |

## Authority-route ledger

Rows separate checking, disposition, retention and later use even where one declared route contains several functions. All architectural statuses here concern inspected or supplied implementation, not observed activation. Claim scope, admission roles and evidence passages are owned by the cited records.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-dev-test](runtime.md#rt-rte-dev-test) | check/evidence production | implemented | [RT-OBJ-task-branch](runtime.md#rt-obj-task-branch) | truth-apt transformation: indeterminate | Candidate task implementation | Tester model/project tests; count-consistency checks | Selected dev-test cycle | Proposed pass/fail/blocked/no-tests | Result supplied to parser | At most named tests/task judgment, not arbitrary correctness | Supplies continuation decision | Loop, parsed text, advisory to code, cycle | See record | [EPI-CLM-task-testing](#epi-clm-task-testing) | Alternate bypasses | Test execution unobserved; no-tests and audit routes qualify universal claim |
| [RT-RTE-dev-test](runtime.md#rt-rte-dev-test) | disposition/acceptance | implemented | See record | no content change | Continue or return task outcome | Python rejects inconsistent pass counts; admits defined outcomes | After candidate verdict | Retry/termination/eligible outcome | Enforcing cycle branching | Conditional operational task acceptance, not infallible truth | Another developer call or end | Loop outcome, enforcing, current task | See record | [EPI-CLM-task-testing](#epi-clm-task-testing) | No independent global oracle | No actual accepted claim instance supplied |
| [RT-RTE-gated-merge](runtime.md#rt-rte-gated-merge) | disposition/acceptance | implemented | [RT-OBJ-task-branch](runtime.md#rt-obj-task-branch) | no content change | Merge candidate with reviewed provenance | Reviewer findings plus gate/diff/Git checks | After eligible outcome | Merge/block/noop | Enforcing merge admission | License bounded to configured severity/provenance policy, not vulnerability absence | Admit selected commits to default branch | See [RT-BAP-merge-policy](runtime.md#rt-bap-merge-policy) | See record | none | Review opt-outs | Non-Git effects and generated conflict resolutions qualify scope |
| [RT-RTE-goal-rounds](runtime.md#rt-rte-goal-rounds) | operational admission/selection/consumption | implemented | Goal/task proposals; see record | truth-apt transformation: indeterminate | Goal satisfaction and follow-up tasks | Model judgment plus task validation/caps | After task rounds | Done/blocked/new tasks | Code branches on model assessment | No independently warranted goal-completion proposition supplied | End goal or schedule tasks | Manager, parsed evaluator result, permissive, goal rounds | See record | none | none | No reference answer or actual goal trace |
| [EPI-RTE-episode-memory](#epi-rte-episode-memory) | content transformation | implemented | [EPI-OBJ-agent-episodes](#epi-obj-agent-episodes) | truth-apt transformation: indeterminate | Output tail or structured reflection to experience narrative | Model generation or parser | Task completion; fallback if reflection absent | Candidate approach/reflection | Candidate production only | No new truth license | Can proceed to retention | Recorder, text, permissive candidate, task end | SRC-1, `equipa/reflexion.py` | [EPI-CLM-self-improvement](#epi-clm-self-improvement) | none | Could summarize or conjecture; actual proposition needed to distinguish |
| [EPI-RTE-episode-memory](#epi-rte-episode-memory) | check/evidence production | implemented | See record | no content change | Agent-authored text safety | Sanitizer injection patterns, not factual evaluator | Before insert and delivery | Safe text or rejection | Reject-mode filter | Pattern nonmatch only; no truth endorsement | Determines availability to next stage | Sanitizer result, code condition, enforcing, write/read | SRC-1, `lesson_sanitizer.py`, `equipa/lessons.py` | none | Safety versus truth | Detector not exhaustively audited |
| [EPI-RTE-episode-memory](#epi-rte-episode-memory) | retention | implemented | See record | truth-apt transformation: indeterminate | Sanitized candidate into episode table | Recorder accepts available sanitized fields | Post-task | SQLite row, optional null reflection | Durable storage | Retention before epistemic acceptance | Makes candidate retrievable | SQLite, episode fields, permissive, future tasks | SRC-1, `equipa/lessons.py` | none | Retention is not acceptance | Sanitization can remove/truncate content |
| [EPI-RTE-episode-memory](#epi-rte-episode-memory) | operational admission/selection/consumption | implemented | See record | truth-apt transformation: indeterminate | Selected episode to model-visible experience | Feature/project/ranking/filter gates | Prompt assembly | Summary capped at 120 chars, reflection at 150 | Advisory prompt delivery | Source warrant unknown; truncation degrades completeness | Supplies context without factual approval | Agent, derived untrusted text, advisory, invocation and later tasks | SRC-1, `equipa/prompts.py`, `equipa/lessons.py` | [EPI-CLM-semantic-memory](#epi-clm-semantic-memory) | Delivered is not used | Ranking internals partially uninspected; final budget can trim context |
| [EPI-RTE-episode-values](#epi-rte-episode-values) | behavior/policy adaptation | implemented | [EPI-OBJ-episode-q-value](#epi-obj-episode-q-value) | non-truth-apt policy/content update: Q-value increment/decrement | Previously injected episode rankings | Host outcome tests_passed/no_tests versus others | Completion after injection tracker lookup | +0.1 or -0.05, clamp [0,1] | Ranking | No individual usefulness attribution | Changes eligibility/score in later retrieval | Retriever, SQLite Q-value, ranking, future prompts | SRC-1, `equipa/lessons.py` | [EPI-CLM-self-improvement](#epi-clm-self-improvement) | Outcome credit is not causal credit | All tracked episodes get same signal |
| [EPI-RTE-simba-rules](#epi-rte-simba-rules) | content transformation | implemented | [EPI-OBJ-lessons-learned](#epi-obj-lessons-learned) | truth-apt transformation: indeterminate | Contrast episodes to rules | Claude requested to explain patterns | Maintenance synthesis | Candidate rules/rationale | Generation only | No verified causal mechanism | Candidate may be stored | Synthesizer, episode excerpts, advisory, maintenance run | SRC-1, `scripts/forgesmith_simba.py` | [EPI-CLM-self-improvement](#epi-clm-self-improvement) | none | Imperatives are policy; actual claims unavailable |
| [EPI-RTE-simba-rules](#epi-rte-simba-rules) | disposition/acceptance | implemented | See record | no content change | Rule admissibility for lesson table | Shape/length/class/word-overlap checks | Before rule insertion | Reject or allow | Enforcing storage gate | Structural admission for prompt guidance, not truth acceptance | Allows durable candidate | Store function, validator tuple, enforcing, insertion | SRC-1, `scripts/forgesmith_simba.py` | none | Admission versus knowledge acceptance | No evidential test of rule's rationale |
| [EPI-RTE-simba-rules](#epi-rte-simba-rules) | retention | implemented | See record | no content change | Accepted-by-shape rule to lesson table | Store writes source simba_generated | After validation | Lesson/error signature retained | Durable | No added warrant | Later active lesson query can retrieve | SQLite lesson text, permissive, future tasks | SRC-1, `scripts/forgesmith_simba.py`, `forgesmith.py` | none | Rationale omitted | Dedicated get_active_simba_rules source filter differs; generic active query includes these rows |
| [EPI-RTE-simba-rules](#epi-rte-simba-rules) | check/evidence production | implemented | [EPI-OBJ-effectiveness-score](#epi-obj-effectiveness-score) | truth-apt transformation: entailed derivation | Difference in role-level outcome rates before/after rule creation | SQL counts and arithmetic; conditional on recorded labels | At least 10 injections and 3 episodes each period | Rounded after_rate minus before_rate | Score stored for pruning | Arithmetic association within selected rows, not rule effect | Supplies pruning criterion | Evaluator, effectiveness_score, advisory to prune code, maintenance | SRC-1, `scripts/forgesmith_simba.py` | [EPI-CLM-self-improvement](#epi-clm-self-improvement) | Causal attribution exceeds comparison | Concurrent changes, task mix and other rules uncontrolled |
| [EPI-RTE-simba-rules](#epi-rte-simba-rules) | disposition/acceptance | implemented | [EPI-OBJ-lessons-learned](#epi-obj-lessons-learned) | no content change | Continued rule availability | Injection threshold and null/nonpositive score | Maintenance prune, unless dry-run | active=0 | Enforcing generic active-query withdrawal | Operational withdrawal, not refuted proposition | Suppresses future generic prompt selection | Lesson query, active flag, enforcing, future prompts | SRC-1, `scripts/forgesmith_simba.py`, `forgesmith.py` | [EPI-CLM-self-improvement](#epi-clm-self-improvement) | Withdrawal not universal | MCP lesson query does not check active |
| [EPI-RTE-mcp-retrieval](#epi-rte-mcp-retrieval) | content transformation | implemented | [EPI-OBJ-lessons-learned](#epi-obj-lessons-learned) | truth-apt transformation: acquisition/import | Retained statements to requesting client | SQL filtering/limit, not truth check | Exposed tool invocation | Returned row dictionaries | Informational delivery | Unknown original warrant; table source labels omitted from response | Client may interpret, no target-side acceptance | MCP JSON response, advisory, request horizon | SRC-1, `equipa/mcp_server.py` | [EPI-CLM-semantic-memory](#epi-clm-semantic-memory) | Pruned rules still queryable | Does not require active=1 or prompt sanitizer |
| [EPI-RTE-context-reorder](#epi-rte-context-reorder) | content transformation | implemented | [EPI-OBJ-prior-summary](#epi-obj-prior-summary) | truth-apt transformation: non-ampliative reshaping | Prior Work Summary sections | Deterministic cycle-number sort/reorder | More than two parsed sections | Newest, middle, oldest | Positional context supply | No truth or attention license | Changes visible order only | Agent prompt extra_context, advisory, invocation | SRC-1, `equipa/prompts.py` | none | Weight-to-order disconnect | alpha/beta/gamma unused in body |
| [EPI-RTE-rubric-scores](#epi-rte-rubric-scores) | check/evidence production | implemented | [EPI-OBJ-rubric-scores](#epi-obj-rubric-scores) | truth-apt transformation: entailed derivation | Lexical/file-list indicators in result text | Regex deltas, role weights and clamping | Scoring caller | Dimension and normalized scores | Measurement supplied to maintenance | Warrant for computed score only, not actual code quality | Supports tuning analysis, not direct product correctness gate | ForgeSmith pipeline per runtime, numeric score, advisory, later maintenance | SRC-1, `rubric_quality_scorer.py` | [EPI-CLM-self-improvement](#epi-clm-self-improvement) | Proxy versus target quality | Text/file names can differ from actual behavior |
| [EPI-RTE-hook-checks](#epi-rte-hook-checks) | check/evidence production | implemented | [RT-OBJ-task-branch](runtime.md#rt-obj-task-branch) | truth-apt transformation: indeterminate | Syntax/build/lint of configured project | Compiler/linter, conditional on tool and language | Registered lifecycle call if configured | Exit code/log output, including skip-as-zero | Result returned; caller controls consequence | Python compile licenses syntax only; no-tool zero licenses nothing | No unconditional block proved | External hook exit mapping via runtime, advisory unless consumed, event | SRC-1, `hooks/preflight_build.py`, `hooks/post_agent_lint.py` | [EPI-CLM-task-testing](#epi-clm-task-testing) | Zero conflates success and skip | Lint timeout returns zero; pre-agent results can be ignored |
| [RT-RTE-forgesmith-changes](runtime.md#rt-rte-forgesmith-changes), [RT-RTE-gepa-prompts](runtime.md#rt-rte-gepa-prompts), [RT-RTE-autoresearch-prompts](runtime.md#rt-rte-autoresearch-prompts) | behavior/policy adaptation | implemented | [RT-OBJ-role-prompts](runtime.md#rt-obj-role-prompts) | non-truth-apt policy/content update: instruction/configuration replacement | Own runtime guidance | Different gates and outcome proxies; see each record | Maintenance/benchmark routes | Proposal, installed variant, retained/reverted prompt | Config/prompt selection | Operational tuning does not itself establish true method claims | Future agent instruction changes | See [RT-BAP-role-instructions](runtime.md#rt-bap-role-instructions) | See records | [EPI-CLM-self-improvement](#epi-clm-self-improvement) | Improvement versus installation | Grouped only for shared policy-update conclusion; gates remain record-specific |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-self-improvement](#epi-clm-self-improvement) | Tomorrow's agents measurably better; failure lessons, prompt evolution and rollback | SRC-1, `README.md`; doctrine/design and attributed reported operation | Three named maintenance systems | [EPI-RTE-simba-rules](#epi-rte-simba-rules), [EPI-RTE-episode-values](#epi-rte-episode-values), [RT-RTE-forgesmith-changes](runtime.md#rt-rte-forgesmith-changes), [RT-RTE-gepa-prompts](runtime.md#rt-rte-gepa-prompts), [RT-RTE-autoresearch-prompts](runtime.md#rt-rte-autoresearch-prompts) | None supplied | Before/after association cannot isolate rules; A/B selection code is no completed experiment | Improvement-directed own-organization change is wired | Actual benefit and exercised dependence on update unestablished; ForgeSmith can return before later phases |
| [EPI-CLM-semantic-memory](#epi-clm-semantic-memory) | Similar experiences automatically reach agent context; graph priorities | SRC-1, `README.md`; doctrine/design | Prompt retrieval claim | [EPI-RTE-episode-memory](#epi-rte-episode-memory), [EPI-RTE-mcp-retrieval](#epi-rte-mcp-retrieval) | None supplied | Delivery and ranking are not usefulness or truth | Feature-gated past-experience supply is implemented | Generic lesson query inspected is frequency/recency, not semantic; full vector/graph mechanisms uninspected here; no universal denial |
| [EPI-CLM-task-testing](#epi-clm-task-testing) | Every coding task developer→tester; human reviews what ships | SRC-1, `README.md`; doctrine/design | Explicit public workflow | [RT-RTE-dev-test](runtime.md#rt-rte-dev-test), [RT-RTE-gated-merge](runtime.md#rt-rte-gated-merge), [EPI-RTE-hook-checks](#epi-rte-hook-checks) | None supplied | Tests can check scoped behavior but actual test coverage unknown | Review/test routes and executable gate exist | Every-task tester and per-change human approval cannot be generalized across supplied alternate routes |
| [RT-CLM-skill-integrity](runtime.md#rt-clm-skill-integrity) | Dispatch guard checks manifest hashes | See record; implementation | See record | See record | None supplied | Authorized byte identity, not safety/truth; direct callers differ | Scoped integrity protocol | Not universal epistemic endorsement |

## Bounded conclusion

EQUIPA has materially different truth-bearing and policy-bearing paths. The product loop can consume project tests, model diagnoses and provenance checks to decide continuation and merge. Their licenses differ: syntax validity, a particular test's result, reviewer findings, and commit provenance do not jointly imply complete product correctness. The supplied bypasses and opt-outs defeat a universal independently-tested or human-approved-each-change reading without erasing the ordinary gated route.

The inspected memory route retains model-authored descriptions and reflections without an evidence-consuming factual acceptance decision. Sanitization rejects selected instruction patterns; retrieval, truncation and untrusted wrappers manage delivery, not truth. The actual stored truth-apt units are not supplied. Relations from output to reflection and from episode contrasts to advice are therefore indeterminate: a specific unit could be a summary, an explanation exceeding the evidence, or a policy instruction. No accepted ampliative claim instance or post-acceptance lifecycle integration is established in these inspected routes. This is not a claim that no such route exists anywhere in the included but uninspected skills or maintenance code.

Arithmetic derivation is narrower and explicit. Q-values change by host labels, not by a separately measured contribution of each episode. SIMBA effectiveness is an arithmetically derived before/after association conditional on table contents; imported labels are not independently warranted premises about real success. The generated lesson can carry general explanatory content, but a request for rationale and a score do not establish that content's truth or causal mechanism. Its shape gate admits operational guidance. Pruning changes future generic selection but does not remove the lesson from the MCP read surface. The evaluator's result thus has consumer-specific force, not universal withdrawal.

Deterministic reordering is non-ampliative at the section level. It can change model behavior by position but yields no new warranted claim. The separate LITM detector's clarification/read patterns do not establish a middle-attention cause; the inspected reordering body does not use its numeric weight arguments. Source text supports this implementation-level disconnect, not an observed attention failure.

The improvement plane supports standing, evidence-responsive self-change of the system's own prompts, configuration and retrieval priorities, with independently named performance objectives. Later prompt/selector consumers are wired. No supplied trace closes the final causal link from installed change to subsequent exercised behavior, and no outcome comparison establishes improved capacity. Reflection-like self-representation exists as a requested narrative derived from own outcomes and fed back to later prompts; actual representation-mediated behavior remains unobserved. Learning benefit, autonomy, reflection and theory building are independent questions. No inference about provider weight learning follows from these symbolic updates; the supplied component records keep distributed-parametric maintenance opaque. Complete theory-builder assessment is not determinable from absent actual rule/criticism content and the uninspected method-writing paths. These limits do not negate the implemented retry, retention, evaluation or self-change capacities.

## Shared records

### Operative objects

#### EPI-OBJ-agent-episodes
Label: Agent episodes

Source-native identity: `agent_episodes` approach_summary, reflection, outcome and error_patterns. Natural-language narrative and symbolic outcome metadata in SQLite; optional embeddings are a separate, incompletely inspected numerical representation. SRC-1, `equipa/lessons.py`, `equipa/reflexion.py`. No counterpart after comparison with supplied task-branch and role-prompt objects; these describe execution rather than constitute product or standing role instructions. Evidence is in [EPI-RTE-episode-memory](#epi-rte-episode-memory).

#### EPI-OBJ-lessons-learned
Label: Lessons learned

Source-native identity: `lessons_learned`, including SIMBA-generated rules. Natural-language advice/descriptive premises, symbolic role/source/active fields, SQLite substrate. SRC-1, `scripts/forgesmith_simba.py`, `forgesmith.py`. Distinct from [RT-OBJ-role-prompts](runtime.md#rt-obj-role-prompts): task-varying retrieved guidance rather than role-file body. Evidence is in [EPI-RTE-simba-rules](#epi-rte-simba-rules).

#### EPI-OBJ-episode-q-value
Label: Episode Q value

Source-native identity: agent_episodes.q_value. Symbolic bounded priority number in SQLite. SRC-1, `equipa/lessons.py`; implementation. No counterpart in supplied operative objects; distinct from narrative episode content because numerical outcome feedback changes retrieval independently of its truth. Evidence is in [EPI-RTE-episode-values](#epi-rte-episode-values).

#### EPI-OBJ-effectiveness-score
Label: Effectiveness score

Source-native identity: lessons_learned.effectiveness_score for SIMBA rules. Symbolic rounded rate difference in SQLite. SRC-1, `scripts/forgesmith_simba.py`; implementation. No counterpart in supplied operative objects; distinct from rule text because it controls pruning without evaluating what the rule says. Evidence in [EPI-RTE-simba-rules](#epi-rte-simba-rules).

#### EPI-OBJ-rubric-scores
Label: Rubric scores

Source-native identity: scores, total_score, normalized_score and details from score_agent_output. Symbolic numbers and pattern descriptions in Python result dictionaries, with storage tooling not deeply inspected here. SRC-1, `rubric_quality_scorer.py`; implementation. No counterpart in supplied operative objects; distinct from task outcomes and SIMBA effectiveness because these measure lexical/file-list indicators. Evidence in [EPI-RTE-rubric-scores](#epi-rte-rubric-scores).

#### EPI-OBJ-prior-summary
Label: Prior Work Summary

Source-native identity: `extra_context` history sections headed Prior Work Summary. Natural-language content with symbolic cycle headers, Python strings supplied to prompts. SRC-1, `equipa/prompts.py`. Distinct from persistent role-file bodies in [RT-OBJ-role-prompts](runtime.md#rt-obj-role-prompts); runtime mentions this context but declares no object for it. Evidence in [EPI-RTE-context-reorder](#epi-rte-context-reorder).

#### EPI-OBJ-training-marker
Label: Training marker

Source-native identity: marker JSON consumed by `process_marker_file` and mapped to `model_registry`. Symbolic metadata with text provenance/notes, filesystem JSON then SQLite. No counterpart among supplied objects. SRC-1, `tools/ingest_training_results.py`, implementation. Required-field and range checks license metadata import, not truth of claimed training, directional accuracy or deployed weight changes. The inspected importer commits a registry row and moves the marker to a processed directory; failure to move does not undo insertion. Downstream registry consumers uninspected.

> required_fields = ["model_type", "version", "trained_on", "trained_at"]
> --- `tools/ingest_training_results.py`

> if avg_da is not None and not (0.0 <= avg_da <= 100.0):
> --- `tools/ingest_training_results.py`

> row_id = insert_model_record(conn, project_id, marker)
> conn.commit()
> --- `tools/ingest_training_results.py`

### Routes

#### EPI-RTE-episode-memory
Label: Episode reflection memory

Endpoints/progression: task output/host outcome → parsed approach/reflection or fallback model reflection → reject-mode sanitization → SQLite → feature-gated selected, sanitized, capped experience in later prompts. Owner: recorder/reflexion and prompt builder. Not a duplicate of [RT-RTE-dev-test](runtime.md#rt-rte-dev-test): this is post-task narrative retention/read-back rather than task phase execution. SRC-1, `equipa/reflexion.py`, `equipa/lessons.py`, `equipa/prompts.py`, `lesson_sanitizer.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: recorder/fallback return no substantive value; formatter returns prompt text or empty text.
- Later read-back: stored summaries/reflections can reach later feature-enabled tasks as Past Experience.
- Delegated visibility: fallback sees task title, outcome, turns and last 1500 output characters, not full causal history; later agent receives 120/150-character capped summary/reflection and outcome.
- Selection predicate: parse existing reflection; otherwise fallback agent; storage sanitizes authored fields; read-back requires feature/project/ranking filters and injectable content.
- Invalidation or expiry: rejected fields become null; read-time poisoned episodes are dropped; token pressure can trim delivered material; full ranking/expiry policy uninspected.
- Activation or effect: storage and conditional prompt supply implemented; changed subsequent decisions unobserved.
- Evidence limits: no actual narrative or factual acceptance trace; truncation/sanitization may lose meaning; vector and ranking internals incompletely inspected.

Admission: original agent or fallback model proposes text; software checks response success/minimum length and sanitization, not factual support; operator launching tasks does not approve each reflection. Operating mode: open completed-task reflection, not expected-answer curriculum. Oracle: none for reflection truth. Recovery: discard failed/short/poisoned reflection, leaving absent field; record failures are telemetry failures. Guidance asks what worked/failed and what to do differently. What persists is narrative and outcome metadata, not an evidence-consuming acceptance decision. A later model may treat the delivered text as advice; wrapper is not reliable model compliance.

> output_tail = result_text[-1500:] if len(result_text) > 1500 else result_text
> --- `equipa/reflexion.py`

> reflection_text = sanitize_episode_text(reflection_text, "reflection")
> if not reflection_text:
> --- `equipa/reflexion.py`

> reflection = sanitize_episode_text(parse_reflection(result_text), "reflection")
> approach = sanitize_episode_text(
>     parse_approach_summary(result_text), "approach_summary"
> )
> --- `equipa/lessons.py`

> (task_id, role, task_type, project_id, approach,
>  num_turns, outcome, error_patterns, reflection, q_value),
> --- `equipa/lessons.py`

> if len(summary) > 120:
>     summary = summary[:117] + "..."
> if len(reflection) > 150:
>     reflection = reflection[:147] + "..."
> --- `equipa/lessons.py`

> reason = detect_injection(text)
> if reason:
>     _log.warning(
>         "lesson_sanitizer: rejected %s (%s); content not stored or injected",
>         label, reason,
>     )
>     return ""
> return neutralize_markup(text).strip()
> --- `lesson_sanitizer.py`

#### EPI-RTE-episode-values
Label: Episode value update

Endpoints/progression: task outcome plus tracked injected IDs → bounded SQL increments → future retrieval score/threshold. Owner: lesson module and prompt tracker. No counterpart after comparison: [RT-RTE-dev-test](runtime.md#rt-rte-dev-test) supplies outcomes but does not denote this retrieval-policy update. SRC-1, `equipa/lessons.py`, `equipa/prompts.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: no substantive return; Q-values persisted and log emitted.
- Later read-back: get_relevant_episodes uses Q-value in threshold/scoring for subsequent prompts.
- Delegated visibility: updater receives IDs and outcome only; later agent receives selected narratives, not contribution measurements.
- Selection predicate: process-local task tracker has injected IDs; tests_passed/no_tests is success.
- Invalidation or expiry: tracker entry popped on completion; values clamped to [0,1]; no isolated usefulness test.
- Activation or effect: durable ranking changes wired; benefit unobserved.
- Evidence limits: host labels are proxies; every tracked episode gets the same reward independent of actual use or causal relevance.

Proposer/decider: fixed software rule; human policy enters through task/configuration, not per-episode content approval. No answer oracle for usefulness. Trigger/objective: completion feedback intended to favor useful experience. Admitted change: numeric retrieval priority, not narrative truth; no validation/rejection beyond missing IDs and bounds; explicit rollback uninspected. Operating mode: open task feedback. The docstring's usefulness condition is stronger than the implementation: only success Boolean and IDs are supplied.

> task_succeeded = outcome in ("tests_passed", "no_tests")
> update_episode_q_values(ep_ids, task_succeeded)
> --- `equipa/lessons.py`

> if task_succeeded:
>     delta = 0.1
> else:
>     delta = -0.05
> --- `equipa/lessons.py`

> SET q_value = MIN(1.0, MAX(0.0, q_value + ?))
> --- `equipa/lessons.py`

#### EPI-RTE-simba-rules
Label: SIMBA rule synthesis

Endpoints/progression: selected success/failure/hard-case episodes and existing rules → model proposals → structural/duplicate validation → lesson storage → generic active lesson retrieval; separate before/after scoring → conditional active-flag withdrawal. Owner: SIMBA maintenance code, generic ForgeSmith query and prompt builder. No counterpart after comparison with [RT-RTE-forgesmith-changes](runtime.md#rt-rte-forgesmith-changes): SIMBA writes lesson rows, not config or role-file patches. SRC-1, `scripts/forgesmith_simba.py`, `forgesmith.py`, `equipa/prompts.py`, `equipa/lessons.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stored rule descriptors, evaluated count or pruned row list depending on operation.
- Later read-back: active role/global lessons can enter feature-enabled prompts via generic query/dedup/sanitizer/wrapping; stored scores enter pruning.
- Delegated visibility: synthesizer sees capped episode approach/reflection and failure information; future task agent sees lesson text, not requested rationale or original comparisons.
- Selection predicate: rule shape/20–250 character length/class/word overlap checks; rate evaluator requires at least ten injections and three pre/post episodes; prune requires injection threshold and null/nonpositive score.
- Invalidation or expiry: rejected proposals not inserted; pruning sets active=0; no text deletion, and MCP retrieval can still expose inactive rows.
- Activation or effect: candidate storage, score persistence and active-flag withdrawal implemented; actual rules, uses and benefits unobserved.
- Evidence limits: uncontrolled before/after periods do not isolate individual rule effects; actual generated content and full generation caller are unavailable/uninspected respectively.

Proposer: Claude asked to contrast cases and give specific rules plus rationale. Decider/veto: software structural/dedup checks; no per-rule human approval shown. Answer oracle: none for general advice; episode success labels supply proxy comparisons. Operating mode: trace-fed maintenance on open tasks. Guidance requires concrete observed behavior and no duplicates. What persists in the inspected insert is rule text, role, failure class/signature and source; rationale is read but not inserted. Generic active lesson retrieval includes these rows, while `get_active_simba_rules` asks for source simba/forgesmith, not simba_generated. That helper mismatch does not prove rules never reach prompts: the generic query is a counterexample.

Conjectural explanatory content could be formulated in natural language, but actual units are absent. Theory-builder conditions 1–4: condition 1 uninspected at content-instance level; condition 2 uninspected for dependence on what an actual rule says; condition 3 uninspected for claim-targeted criticism/blame, because rate scoring alone does not establish it; condition 4 uninspected for iteration of such criticism. The loop does wire repeated selection and numerical evaluation independently of these unresolved theory properties. Addressability is afforded at per-row text level; actual assumptions/parts uninspected. Persistence reaches future tasks through active queries. Learning benefit is uninspected. Reflection is afforded as trace-fed representation/feedback, not observed causal use. No autonomous or reflective theory-builder conclusion follows.

> Analyze the contrast between successes and failures. Identify specific, actionable patterns that distinguish them. Then generate up to {MAX_RULES_PER_ROLE} new rules.
> --- `scripts/forgesmith_simba.py`

> if error_type not in valid_types:
>     return False, f"invalid failure_class/error_type: {error_type}"
> --- `scripts/forgesmith_simba.py`

> if overlap > 0.6:
>     return False, f"too similar to existing rule #{existing['id']}"
> --- `scripts/forgesmith_simba.py`

> (role, error_type, error_signature, lesson, source, times_seen)
> VALUES (?, ?, ?, ?, 'simba_generated', 1)
> --- `scripts/forgesmith_simba.py`

> before_rate = before["successes"] / before_total
> after_rate = after["successes"] / after_total
> score = round(after_rate - before_rate, 3)
> --- `scripts/forgesmith_simba.py`

> AND times_injected > ?
> AND (effectiveness_score IS NULL OR effectiveness_score <= 0)
> --- `scripts/forgesmith_simba.py`

> UPDATE lessons_learned
> SET active = 0, updated_at = datetime('now')
> WHERE id = ?
> --- `scripts/forgesmith_simba.py`

> conditions = ["active = 1"]
> --- `forgesmith.py`

> WHERE active = 1 AND (source = 'simba' OR source = 'forgesmith')
> --- `equipa/lessons.py`

#### EPI-RTE-mcp-retrieval
Label: MCP lesson retrieval

Endpoints/progression: tool request → bounded SQL query → row dictionaries returned to client. Owner: MCP handlers. Distinct from [RT-RTE-ollama-tools](runtime.md#rt-rte-ollama-tools) and runtime's MCP dispatch account: this reads retained content rather than executes a task. Material subroute assessed here is lessons; registry also exposes task dispatch/create/status, agent logs, project context and session notes. SRC-1, `equipa/mcp_server.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: lessons/count/limit JSON-compatible result, or analogous logs/context/notes response.
- Later read-back: uninspected — requesting clients may retain/use content, but no client trace is supplied.
- Delegated visibility: lesson text, error type/signature, count and creation date; not active/source/effectiveness lineage fields.
- Selection predicate: clamped limit, optional LIKE error-type filter, frequency/recency order; no active predicate in lessons handler.
- Invalidation or expiry: inapplicable — handler does not modify source state or revoke already returned responses.
- Activation or effect: exposes retained candidate statements, including inactive ones; subsequent client reliance unobserved.
- Evidence limits: no model instruction compliance or truth check; source authority unknown and some provenance omitted.

Admission/selection is deterministic software, not human endorsement. Open informational request; no answer oracle. This read-only route does not admit a knowledge or machinery change. Its consumer-specific consequence qualifies any claim that active-flag pruning fully withdraws a rule from all readers.

> SELECT lesson, error_type, error_signature, times_seen, created_at
> FROM lessons_learned
> WHERE error_type LIKE ?
> ORDER BY times_seen DESC, created_at DESC
> LIMIT ?
> --- `equipa/mcp_server.py`

> "lessons": [dict(r) for r in rows],
> --- `equipa/mcp_server.py`

#### EPI-RTE-context-reorder
Label: LITM context reordering

Endpoints/progression: extra-context history → Prior Work Summary parsing → cycle sort → newest/middle/oldest sequence → prompt context. Owner: prompt builder. This is a material part of the prompt-assembly behavior discussed in [RT-RTE-dev-test](runtime.md#rt-rte-dev-test), not another developer/tester route.
Part of: [RT-RTE-dev-test](runtime.md#rt-rte-dev-test)

SRC-1, `equipa/prompts.py`, `forgesmith_litm.py`; implementation. Concrete implementation deduction, not target execution: for sections Cycle 1=A, Cycle 2=B, Cycle 3=C, pairing/sort yields [1,2,3], then append last, interior, first yields C,B,A, with preamble preserved. With at most two sections the input is unchanged. The numeric alpha/beta/gamma parameters are not read by the inspected body. Thus a persisted audit weight nudge alone does not establish changed output ordering in this consumer.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reordered history string or original string when ineligible.
- Later read-back: inapplicable — this function writes no retained state; retained history upstream is described by runtime.
- Delegated visibility: agent receives reordered extra context, not the full audit or numerical weight rationale.
- Selection predicate: marker present and more than two parsed pairs; cycle-number parsing determines order.
- Invalidation or expiry: current prompt assembly only; no cached result or persistent revision in this function.
- Activation or effect: text-order change implemented; attention improvement not observed.
- Evidence limits: audit patterns detect clarification/read mentions, not a measured positional-cause contrast; missing evidence columns cause audit skip.

The separate audit proposes beta nudges when heuristic miss count reaches threshold, software decides/persists outside dry-run, operator controls configuration. No expected-answer oracle for attention. That persistence is not proven effective in this inspected consumer. No general claim about every possible weight consumer is made.

> paired.sort(key=lambda x: extract_cycle(x[0]))
> --- `equipa/prompts.py`

> reordered.append(paired[-1])
> --- `equipa/prompts.py`

> for item in paired[1:-1]:
>     reordered.append(item)
> --- `equipa/prompts.py`

> reordered.append(paired[0])
> --- `equipa/prompts.py`

> if miss_count >= threshold:
>     # Increase beta (middle attention) by WEIGHT_NUDGE
>     old_beta = new_weights["beta"]
>     new_weights["beta"] = min(old_beta + WEIGHT_NUDGE, BETA_MAX)
> --- `forgesmith_litm.py`

#### EPI-RTE-rubric-scores
Label: Rubric quality scoring

Endpoints/progression: result text/file list/role → regex counts → file heuristics → role weighting/clamps → numeric result → maintenance scoring caller supplied by runtime. Owner: rubric program and caller. Distinct from [RT-RTE-dev-test](runtime.md#rt-rte-dev-test): measures reported output style/file indicators, not executable pass counts. SRC-1, `rubric_quality_scorer.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: dimension scores, total, normalized score and matched-pattern details.
- Later read-back: uninspected — runtime supplies maintenance scoring/evolution consumer, but this pass did not deeply trace score storage and every later query.
- Delegated visibility: scorer sees text, named changed files and role; does not execute the product to verify claims.
- Selection predicate: scoring call; regex matches and role weights determine values.
- Invalidation or expiry: scores reflect supplied snapshot; persistence/expiry internals uninspected.
- Activation or effect: numeric derivation implemented; quality discrimination and tuning benefit unobserved.
- Evidence limits: syntactic indicators/file naming do not independently measure behavior, correctness or robustness.

Decider: deterministic score code; no human per-output rating in this function. Open task-output evaluation, no reference correct product oracle. This check supplies a proxy result, not a direct product admission gate. Concrete implementation deduction: with scores test_coverage=5 and a single file named test_example.py, `_apply_file_heuristics` raises that component to 7 without examining or executing the file. That derives a heuristic score, not evidence that the product has adequate tests.

> if test_files:
>     scores["test_coverage"] = min(10, scores["test_coverage"] + 2)
> --- `rubric_quality_scorer.py`

> for pattern, delta in config["negative"]:
>     matches = re.findall(pattern, text, re.IGNORECASE)
>     if matches:
>         score += delta * min(len(matches), 3)
> --- `rubric_quality_scorer.py`

#### EPI-RTE-hook-checks
Label: Build lint checks

Endpoints/progression: lifecycle invocation/project directory → language/tool detection → compile/build/lint → exit status and text → registry result → caller-dependent force. Owner: external script plus lifecycle caller. These are concrete check-producing parts of [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks), not a new universal gate.
Part of: [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks)

SRC-1, `hooks/preflight_build.py`, `hooks/post_agent_lint.py`; implementation. Target/domain: Python source syntax via compile, or detected language build/linter contract. Neither supplies complete task correctness. Build skip/missing tool can return zero; lint timeout and no linter also return zero. Runtime's ignored pre-agent results demonstrate why a returned code does not alone establish veto authority.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: integer status and printed diagnostics; async hook wrapper maps exit status for its caller.
- Later read-back: inapplicable — inspected scripts do not persist check findings as retained knowledge.
- Delegated visibility: scripts inspect project files/tool output; event caller receives status/diagnostics, not an independently verified causal explanation.
- Selection predicate: configured event, detected language and installed tools; Python branch compiles source excluding listed directory patterns.
- Invalidation or expiry: check applies to inspected working snapshot; no durable approval or revocation record in these scripts.
- Activation or effect: executable checks wired; effective blocking depends on actual caller consumption, not script name.
- Evidence limits: registration/deployment and actual check execution unobserved; skipping can share success code.

Proposer: current project work from task route; check program computes status; caller decides/vetoes continuation; operator may install/configure hook. No per-content human approval. Operating mode: open project check. Compiler/linter contracts are bounded evaluators, not arbitrary reference answers. No product or machinery change admitted by these scripts themselves; rollback of preceding work belongs to other routes.

> compile(source, filepath, "exec")
> --- `hooks/preflight_build.py`

> except FileNotFoundError:
>     print(f"[preflight_build] Build tool not found: {cmd[0]}")
>     return 0  # Don't block if tool is missing
> --- `hooks/preflight_build.py`

> except subprocess.TimeoutExpired:
>     print(f"[post_agent_lint] Lint timed out after 120s")
>     return 0  # Don't block on timeout
> --- `hooks/post_agent_lint.py`

### Claims

#### EPI-CLM-self-improvement
Label: Self improving agents

Claimed operation: repeated outcome-driven evolution makes later agents measurably better and automatically rolls back harmful changes. SRC-1, `README.md`; doctrine/design plus target-attributed reported operation, not observed results. No counterpart after comparison with [RT-CLM-skill-integrity](runtime.md#rt-clm-skill-integrity), which concerns byte-integrity dispatch only. Runtime mutation routes describe implementation, not this broader public performance claim.

> Then it gets better at its job. A three-layer self-improvement system benchmarks agent performance, evolves prompts using genetic optimization, and auto-rolls back changes that hurt results. Your agents tomorrow are measurably better than your agents today.
> --- `README.md`

#### EPI-CLM-semantic-memory
Label: Semantic memory supply

Claimed operation: automatic similarity-based experience supply and graph ranking of useful lessons. SRC-1, `README.md`; doctrine/design. Distinct from runtime's integrity claim; no supplied claim counterpart.

> Lessons and past experiences are embedded as vectors (via Ollama) and retrieved by semantic similarity — not just keyword matching. When a task resembles something EQUIPA has seen before, relevant lessons get injected into the agent's context automatically. A knowledge graph tracks which lessons are most connected and influential, prioritizing the most useful ones via PageRank.
> --- `README.md`

#### EPI-CLM-task-testing
Label: Task testing workflow

Claimed operation: all coding tasks pass through developer/tester iteration, while the operator reviews shipping. SRC-1, `README.md`; doctrine/design, not run evidence. No supplied claim counterpart; [RT-RTE-dev-test](runtime.md#rt-rte-dev-test) and [RT-RTE-gated-merge](runtime.md#rt-rte-gated-merge) give qualified routes.

> Every coding task runs through a developer -> tester cycle. If tests fail, the developer gets the failure context and tries again — up to 5 cycles. No human babysitting required.
> --- `README.md`

> You direct. EQUIPA executes. You review and decide what ships.
> --- `README.md`
