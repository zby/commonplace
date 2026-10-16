---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AutoSci runtime baseline: prompted research, wiki producers and consumers, browser and scheduled writers, and optional Hiera execution at the frozen commit."
run-id: AAS-2026-10-15-autosci-430df584df8f-01
reviewed-boundary: f5c2fe009c6683b6aa5b668de759a0610c938aaf
---

# AutoSci runtime report

## Runtime account

### What performs the work

AutoSci ships procedures for an enclosing Claude Code agent, plus Python tools that make selected operations deterministic. It does not itself implement the foreground model/tool loop. The ordinary knowledge workflow is a user invoking `/ingest` with a paper, followed in a later invocation by `/ask`; the broader research workflow delegates ideation, experiments, verdicts and paper production to skills. The claimed end-to-end workflow and the actual enforcement boundary differ: stage order, scientific judgment and most human confirmations are instructions interpreted by an external agent; individual CLI functions enforce narrower data-integrity rules. See [RT-RTE-knowledge-cycle](#rt-rte-knowledge-cycle), [RT-RTE-research-verdict](#rt-rte-research-verdict) and [RT-CLM-writer-contract](#rt-clm-writer-contract).

All evidence below is SRC-1 at the boundary's frozen revision. Executable passages supply **implementation** evidence; skill, policy and setup guidance supplies **doctrine/design** unless an executable mechanism is identified. No registered observed run or causal experiment was supplied. Target commands, tests, examples and services were not executed. Operation, actual model compliance, deployment permissions, scientific validity and benefit remain unobserved; missing execution evidence is not evidence that these behaviors never happen.

Additional inspection beyond the boundary's initial scope covered bodies of `tools/research_wiki.py` (edge admission, context compilation, metadata writes and worktree rebuild guard), `tools/serve.py` entity/edge writes, `.github/workflows/daily-arxiv.yml` model invocation and writeback, `tools/daily_arxiv.py` direct provider call, `.claude/skills/research/SKILL.md` stage progression, `.claude/skills/exp-run/SKILL.md` execution gate, `.claude/skills/exp-eval/SKILL.md` verdict/update procedure, `.claude/skills/init/references/parallel-ingest.md`, `.claude/skills/hiera-experiment/SKILL.md`, and Hiera CLI, contract, ledger, evaluator, remote adapter and remote worker execution bodies. MCP thread and native-search handling, setup activation and the example host grant were also inspected. Correction inspection additionally covered `.gitignore`, the full parallel-ingest reference, init's handoff instructions, CI staging, and the tracked-file inventory for sources, checkpoints and wiki scaffold; these supply implementation and doctrine/design evidence, not execution evidence. These remain the same registered source, not new sources or observed executions.

### Ordinary invocation, producer to later consumer

A user supplies a local paper or arXiv URL. The foreground agent resolves the interpreter, reads the ingest skill and schema/templates, resolves the source and consults literature services when available. It generates a slug, checks for an existing matching paper, interprets the source, and decides which entities to create or merge. It writes Markdown pages and links; graph edges go through `research_wiki.py add-edge`. The helper validates edge type/attributes, canonicalizes identifiers, warns about unresolved references, deduplicates and appends JSONL. The agent logs the operation, requests context/gap rebuilds and returns page counts and follow-up suggestions. API failure fallbacks and slug collisions have prompt-level recovery instructions. The source is not an execution transcript proving that these steps were followed (SRC-1: `.claude/skills/ingest/SKILL.md`, `tools/research_wiki.py`).

On a later `/ask`, the user supplies a question. The agent is instructed to load the compressed context and gaps, match index keywords and context relevance, choose at most 15 pages, read them in full, optionally read relationship edges and synthesize a cited answer. A model recommendation is not write authorization: crystallization requires the flag or a user confirmation. However, answer-only mode still specifies an audit-log write, and missing context may cause rebuilds. Thus “answer only” is not a universal filesystem-read-only guarantee (SRC-1: `.claude/skills/ask/SKILL.md`). [RT-RTE-knowledge-cycle](#rt-rte-knowledge-cycle) records the admission and selection roles.

Working-context control has two different owners here. Python compilation deterministically selects summaries by per-section character budgets, connectivity, status and ordering; the model chooses relevant full pages under a prompt-level page cap. The compiler keeps methods, gaps, failed ideas, papers, experiments, recent edges and stale-entity summaries, omitting or truncating the rest. This is not a token-perfect fit or a full-content copy. The original files remain reachable for later reads. Neither inspected path implements foreground old-turn eviction or host compaction; those host internals are uninspected. The model weights and endpoint fixity are separately assessed in [RT-CMP-claude-code](#rt-cmp-claude-code) and [RT-CMP-review-llm](#rt-cmp-review-llm).

### Four forcing cases and what they overturn

1. **Parallel initialization** changes both write coordination and context ownership. `/init` specifies one ingest per isolated worktree/subagent, sequential fan-in of committed results, then rebuild/dedup/lint in the parent. The intended handoff is one selected source path plus inherited scaffold/manifests, with committed artifacts and a task result returning. However, `.gitignore` excludes generated raw sources, wiki entities/graph and checkpoints, while the prescribed pre-fan-out `git add` is unforced and explicitly names ignored checkpoint files. That staging recipe does not establish those inputs in `BASE_COMMIT`; a relative path in a task prompt does not copy its payload into the worktree. Likewise, an ingest commit need not contain newly ignored wiki output, so successful Git fan-in alone does not establish its transport. The protocol is supported as intent; visibility and persistence require supplied tracking/staging conditions absent here (SRC-1: `.gitignore`, `.claude/skills/init/references/parallel-ingest.md`). This resembles a per-task frame, but Git branches preserve files beyond the agent's window and the host controls actual context isolation. A CLI guard refuses selected rebuild entry points inside linked worktrees, not every possible filesystem write or direct call to the context compiler. See [RT-RTE-parallel-ingest](#rt-rte-parallel-ingest).
2. **Unattended intake** overturns any blanket claim that a person approves every paper. Scheduled/manual CI can grant Write/Edit/Bash/Skill/Agent and ask the model to select high-confidence papers for sequential ingest, then commit and push changes without a per-paper approval step. The alternative OpenAI-compatible recommender is inform-only in code, not a second ingest executor. See [RT-RTE-daily-intake](#rt-rte-daily-intake).
3. **Browser and direct CLI writes** overturn a role-based authorization interpretation of writer policy. The browser can invoke `set-meta` and `add-edge` without a skill identity, and direct file tools/Bash are a wider path. A lifecycle transition helper therefore cannot enforce lifecycle policy on all writes. See [RT-RTE-browser-write](#rt-rte-browser-write) and [RT-CLM-writer-contract](#rt-clm-writer-contract).
4. **Optional Hiera local/remote execution** adds real contract and snapshot checks, budget reservation and receipts, but not an operating-system sandbox or authenticated proof of human approval. CLI approval is a command available to its caller. The remote worker may explicitly wrap the supplied command in a configured shell environment. Finalization emits an exploratory report, not formal wiki confirmation. See [RT-RTE-hiera-search](#rt-rte-hiera-search).

These are source-supported counterexamples, not exploit tests. They are the selected forcing set, not an exhaustive audit of every helper, translation or provider path.

### Research progression, control and guarantees

`/research` is a model-interpreted coordinator. It can bootstrap an empty wiki, call `/ideate`, select an idea, call `/exp-design`, deploy experiments through `/exp-run`, persist a progress file, end the session while jobs run, collect later, call `/exp-eval`, iterate and optionally write/compile a paper. Interactive Gate 1 lets the user choose or stop; `--auto` chooses top priority. Gate 2 can request more experiments, stop or proceed; auto mode proceeds. The inspected Stage 3 body explicitly describes ending the session and manual collection. The opening also promises automatic CronCreate monitoring, but the inspected stage body does not establish that activation. Automatic resumption should therefore not be treated as demonstrated or uniformly specified (SRC-1: `.claude/skills/research/SKILL.md`).

The execution skill places manual inspection before deployment, but also specifies a small-scale sanity run before that gate. “No execution before approval” is consequently too broad even as doctrine. Normal deployment uses local screen/shell commands or remote helper operations; actual host grants and remote isolation are not supplied (SRC-1: `.claude/skills/exp-run/SKILL.md`). Experiment outputs can update idea status and failure reasons under `/exp-eval`; details of retained-memory revision belong to the later memory analysis. Here [RT-RTE-research-verdict](#rt-rte-research-verdict) establishes ownership and the control path.

| Load-bearing guarantee | Owner, strength and enforcement | Covered and alternate paths; external contract | Separate conclusions |
|---|---|---|---|
| Skill-specific writer ownership and graph tool ownership | Skill authors/foreground agent; **policy**, interpreted prompts and `writers.yaml` | Intended skill behavior only. Browser metadata CLI and generic Edit/Bash have no writer-identity check. Requires host/agent compliance, not merely schema validity. | doctrine conclusion status: claimed; operation conclusion status: uninspected |
| Edge shape and duplicate checks | Python edge helper; **invariant** within the inspected function | `add-edge`, including browser forwarding; node existence problems may warn rather than reject. Batch has its own attribute checks. Direct JSONL editing bypasses helper checks; truthful evidence text still requires judgment. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Parent-owned derived rebuild in INIT MODE | Prompt plus selected CLI wrappers; **protocol** | `rebuild-context-brief` wrapper refuses linked worktrees. Direct `compile_context` lacks that guard; shell/file writes and host fan-in are separate. Requires successful Git/worktree discipline and payload inclusion: shipped ignore rules contradict the unforced scaffold staging recipe, so required input inheritance and output transport are not established. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Human research/experiment gates | Foreground agent/user; **protocol** | Interactive stage gates and deployment inspection. Research auto mode bypasses its human gates; exp-eval auto bypasses update confirmation; sanity execution precedes deployment inspection. Requires agent obedience and actual human interaction. | doctrine conclusion status: claimed; operation conclusion status: uninspected |
| Hiera frozen contract/candidate and evaluation budget | Contract/evaluator/ledger code; **invariant** within shipped evaluation path | Local and remote dispatched evaluation verify frozen contract and snapshot, then reserve budget. Caller can invoke approve; preflight runs commands without reserving evaluation budget. Direct subprocesses or mutable filesystem access are outside this invariant. Requires filesystem/lock integrity and trusted OS/SSH host. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Hiera no formal wiki writeback | Sidecar finalizer plus skill; **protocol** | Finalizer emits report with `wiki_writeback: none`; source snapshots detect selected wiki changes. Arbitrary candidate execution is not confined by a cwd or digest, so this is not a security guarantee against hostile candidate writes. | implementation conclusion status: wired; operation conclusion status: uninspected |

The capability surface includes file tools, shell, MCP model review/native search, worktree subagents, SSH and browser mutation. The current grant set is **not supplied**. The example local grant allows broad Bash/Read/Edit/MCP and enables project MCP servers; setup preserves an existing local settings file. CI declares its own broad allowed-tools set. Neither is evidence of a deployed sandbox. Browser defaults to loopback but accepts another host; no network-isolation guarantee is inferred from that default (SRC-1: `config/settings.local.json.example`, `setup.sh`, `.github/workflows/daily-arxiv.yml`, `tools/serve.py`).

Instruction and capability changes can enter through setup's language activation, local settings, externally configured model endpoints, user-driven edits and admitted Hiera code/config snapshots. No inspected route autonomously installs revised AutoSci method texts from its own evaluation results. This is a bounded statement about these routes, not an evidenced whole-tree absence. [RT-RTE-setup-skills](#rt-rte-setup-skills) describes executable activation rather than treating static shipped text as retained experience. Provider-native search and mutable/fallback endpoints are kept separate in [RT-RTE-review-call](#rt-rte-review-call).

## Shared records

### Components

#### RT-CMP-claude-code
Label: Claude Code foreground model

External distributed-parametric decision component used by ingest, retrieval and research skills. Parameters reside in the host/provider rather than this repository. Invocation messages and natural-language skills reach it through Claude Code; tool calls reach local or remote executors. Exact model/version is not pinned by the inspected skill files. In-operation parameter changes and endpoint resolution are uninspected host/provider facts; source contains no basis to call the weights immutable. A mutable service may resolve a model alias differently; no fixed model identity is established here. SRC-1: `.claude/skills/ingest/SKILL.md`, `.claude/skills/research/SKILL.md`, `.github/workflows/daily-arxiv.yml`.

> uses: anthropics/claude-code-action@v1
> --- `.github/workflows/daily-arxiv.yml`

This supplies a host integration, not inspectable model weights or evidence of scientific operation.

#### RT-CMP-review-llm
Label: Review LLM and compatible recommendation endpoint

External distributed-parametric model service, stored at a configurable provider. The MCP adapter reads `LLM_BASE_URL`, `LLM_MODEL` and fallback configuration; chat callers can override the model. The direct daily recommender also uses those environment-selected identifiers. Exact weight version is not pinned; mutable endpoint/alias resolution can change the responding model and fallback can explicitly select another. Parameter updates during operation and provider internals are uninspected. The adapter does not train weights. These findings concern the adapter's observable interface, not an absence of provider learning. SRC-1: `mcp-servers/llm-review/server.py`, `tools/daily_arxiv.py`.

> current_model = use_model if attempt < 2 else FALLBACK_MODEL
> --- `mcp-servers/llm-review/server.py`

#### RT-CMP-research-wiki
Label: research_wiki helper

Symbolic Python implementation on the local filesystem. It loads schema, parses metadata, checks edge writes, compiles context and writes JSON/Markdown. Deterministic code rules are distinct from natural-language evidence and summaries carried through them. It does not own the external model/tool loop. SRC-1: `tools/research_wiki.py`, `runtime/loader.py`.

> """Append a typed edge to graph/edges.jsonl with dedup and entity validation."""
> --- `tools/research_wiki.py`

### Operative objects

#### RT-OBJ-writers
Label: writers.yaml

Source-native field/edge writer contract, persisted as YAML at `runtime/policy/writers.yaml`. Its field names and writer lists are symbolic data, but its authorization consequences are natural-language policy interpreted by authors/agent, not a write-time gate. The same distinction applies to the freeze marker. SRC-1: `runtime/policy/writers.yaml`.

> # STATUS: SPEC, NOT A RUNTIME GATE.
> --- `runtime/policy/writers.yaml`

#### RT-OBJ-context-brief
Label: context_brief.md

Derived natural-language query pack stored at `wiki/graph/context_brief.md`; symbolic headings, labels and extracted values organize a model-consumed text summary. Python chooses and truncates sections; the model interprets the surviving claims. The brief is replaceable and purpose-specific, not all source content. Original pages remain on disk. SRC-1: `tools/research_wiki.py`.

> items2.sort(key=lambda x: x[0], reverse=True)
> text = "\n".join(line for _, line in items2[:15])[:b_papers]
> --- `tools/research_wiki.py`

#### RT-OBJ-task-contract
Label: Hiera task_contract

Symbolic evaluation contract stored as `task_contract.yaml` under a sidecar run, including evaluation argv, score path/direction, resources, source snapshot and approval digest. The candidate source files it governs are separately admitted immutable snapshots; their executable code and numerical configuration are symbolic, not model weights. The approval flag/digest is a local integrity state, not authenticated human identity. SRC-1: `tools/hiera/contract.py`, `tools/hiera/cli.py`.

> if canonical_digest(immutable) != expected:
>     raise HieraError("approved contract changed after approval")
> --- `tools/hiera/contract.py`

### Routes

#### RT-RTE-knowledge-cycle
Label: Paper ingest and later question synthesis

User → foreground agent → source/literature helpers → wiki entity and graph writes → derived compiler → later `/ask` retrieval → cited answer, optionally crystallized. Agent decisions use natural-language paper/skill/wiki content; helper decisions use symbolic schema, identifiers and predicates. The agent proposes summaries/entities and chooses merges and relevance; the user supplies the paper/question and can choose crystallization. Ingest itself has no specified per-page human acceptance gate. No expected-answer oracle is supplied: source papers and citations are evidence, not a guaranteed answer key. Operating mode is open requests; the writeback trigger is source ingestion or a worthwhile synthesized finding plus crystallization authorization.

- implementation conclusion status: afforded
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Ingest counts and follow-up suggestions, or a question answer with citations, gaps and crystallization recommendation.
- Later read-back: Wiki pages, index, graph and brief can reach later ask/research invocations; crystallized findings become further retrievable pages or appended content.
- Delegated visibility: Foreground agent sees selected files and helper results; external literature services see submitted identifiers/queries. INIT delegation has a separate route below.
- Selection predicate: Ingest checks identity and similarity, importance and entity criteria; ask combines index keyword matching and model relevance, capped by instruction at 15 pages. Compiler ranks connectivity and limits section characters before delivery.
- Invalidation or expiry: Brief is overwritten on rebuild; pages remain until edited/deleted. Missing brief triggers rebuild; answer-only is not a promise of no audit or repair writes.
- Activation or effect: Skill requests use of retained claims and citations in answers and later proposals; compilation and writes are implemented, but actual model dependence and benefit are unobserved.
- Evidence limits: Prompted end-to-end sequence is not an implemented scheduler or supplied run; provider source quality and compliance are external.

Admission/recovery: Model may omit unjustified entities, merge instead of create, stop on an existing matching paper, or recommend rather than crystallize. The user can withhold crystallization unless already flagged. Writes persist pages/edges/log; source-priority and conservative-entity rules guide the proposal. Errors have source/API/collision fallbacks; no transactional rollback of the complete multi-file ingest is established by this inspection. SRC-1: `.claude/skills/ingest/SKILL.md`, `.claude/skills/ask/SKILL.md`, `tools/research_wiki.py`.

> **Crystallize requires confirmation**: unless the user explicitly specifies `--crystallize`, only recommend but do not write
> --- `.claude/skills/ask/SKILL.md`

> Sort by relevance, select top-K pages (K ≤ 15 to avoid exceeding context window)
> --- `.claude/skills/ask/SKILL.md`

#### RT-RTE-parallel-ingest
Label: Init worktree fan-out and fan-in

Intended protocol: `/init` parent → scaffold/manifests and BASE_COMMIT → one ingest agent/worktree per paper → paper-specific commits → sequential parent merge → dedup/rebuild/lint. The shipped ignore/staging contradiction prevents treating that entire payload flow as established: `.gitignore` excludes generated raw inputs, wiki entities/graph and `.checkpoints/`, while the reference prescribes unforced `git add`, including explicitly named ignored manifests. These files are not thereby included in `BASE_COMMIT`; an ignored-path staging failure also needs handling before the specified commit can be relied upon. Existing tracked changes can still be committed, but neither a commit nor a successful merge proves inclusion of newly ignored payloads. Parent agent owns scheduling, source selection and conflict resolution under the prompt; host supplies agent context boundaries, Bash and Git execution. Natural-language handoff plus symbolic manifest/path/commit state crosses the boundary. This is corpus construction, not an answer-oracle comparison. Admission is model-directed merge under conservative dedup guidance; a human supplies initialization/topic but not necessarily every entity decision.

- doctrine conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Protocol requests a per-task ingest result/commit and initialized wiki report; a returned commit alone does not establish source availability or inclusion of new wiki output.
- Later read-back: Included committed pages can survive fan-in and feed later skills; local checkpoint metadata supports intended recovery in the parent. Generated pages/graph/manifests are ignored, so repository transport and later availability of these payloads are conditional on actual inclusion, not established by the prescribed staging.
- Delegated visibility: Prompt supplies one canonical relative source path; worktree creation exposes files actually in BASE_COMMIT, not ignored local files merely named by that path. Required generated scaffold/source/manifests are not established there. Parent receives only committed artifacts through Git, not uncommitted ignored output or necessarily the full delegated conversation.
- Selection predicate: Planner shortlist rank determines fan-out and merge order; semantic conflicts are merged conservatively rather than multiplying entities.
- Invalidation or expiry: Protocol removes worktrees/branches after merge; only included committed files are transported. Cleanup is not evidence that ignored output was preserved. Stash-pop failures keep the local checkpoint.
- Activation or effect: Requested isolated work and parent-only fan-in; CLI rebuild wrapper refuses linked worktrees, but neither confines generic file writes nor ensures payload staging. Git can transport committed content; the prescribed recipe does not establish the required generated input/output payload.
- Evidence limits: Beyond unobserved host/model compliance, a known source contradiction blocks unconditional inheritance and fan-in claims: generated payloads are ignored and scaffold staging is unforced. No supplied tracking override or alternative transfer mechanism resolves it.

Trigger is init's selected paper list. Parent may reject an empty ingest branch and must stop/fix it; Git conflict recovery and retained checkpoints are specified. The nonempty-commit check does not verify that the commit carries the intended generated pages. No general atomic rollback of all merged papers is established, and no repair to the shipped protocol is assumed. SRC-1: `.gitignore`, `.claude/skills/init/references/parallel-ingest.md`, `.claude/skills/init/SKILL.md`, `tools/research_wiki.py`.

> git add wiki/ raw/papers/ raw/tmp/ raw/discovered/ .checkpoints/init-prepare.json .checkpoints/init-plan.json .checkpoints/init-sources.json
> --- `.claude/skills/init/references/parallel-ingest.md`

> raw/tmp/*
> !raw/tmp/.gitkeep
> --- `.gitignore`

> wiki/papers/*
> !wiki/papers/.gitkeep
> --- `.gitignore`

> wiki/graph/*
> !wiki/graph/.gitkeep
> --- `.gitignore`

> # /init session state
> .checkpoints/
> wiki/.checkpoints/
> --- `.gitignore`

> Merge only committed worktree branches. A branch with no ingest commit is an error to stop and fix, not something to merge through.
> --- `.claude/skills/init/references/parallel-ingest.md`

#### RT-RTE-research-verdict
Label: Research orchestration and experiment verdict

User direction/brief → research agent → ideate/design/run/status/eval → idea updates and optional paper. Progress Markdown stores stage/idea/experiment identities for later sessions; local/remote jobs outlive the foreground session. Agent interprets hypothesis/results and skill policy, invokes symbolic CLIs, and requests model review through [RT-RTE-review-call](#rt-rte-review-call). Interactive user gates can veto idea selection and paper continuation; auto mode delegates those decisions. Exp-eval presents proposed changes for confirmation unless auto; the normal deployment skill separately requests manual code/config approval, after its sanity run. Review LLM recommends; foreground model synthesizes and physically writes. No expected-answer oracle is furnished by a model verdict. Experiments provide measurements and baselines whose validity is not guaranteed by the workflow.

- doctrine conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Deployment status and return-time instructions while jobs run; later partial/final pipeline report and optionally paper PDF.
- Later read-back: Pipeline progress restores selected slugs/stage; experiment results, idea status/failure reasons and graph edges feed later evaluation, ideation and paper planning.
- Delegated visibility: Sub-skills receive selected slugs/parameters; reviewer receives hypothesis, setup, results and sibling summary without requested foreground prejudgment. Exact host skill-context isolation is uninspected.
- Selection predicate: Auto chooses highest priority; verdict sufficiency checks validated primary idea or a succeeded supporting experiment. Failed baseline collection terminates; other failures remain evidence for evaluation/refinement.
- Invalidation or expiry: Stage checkpoints persist until overwritten; malformed progress may be reconstructed from wiki statuses. Completed stages should not be rerun. Stated iteration limits contain inconsistent phrasing (one retry versus maximum two iterations), so an exact enforced round bound is not established.
- Activation or effect: Requested result-dependent changes to idea reliance, failure memory and subsequent experimental plan; persistence helpers are available, but exercised criticism/revision is not observed.
- Evidence limits: Model-dependent orchestration, scientific judgments, actual human review and automatic monitoring are not established by a source-only account.

Admission/recovery: Failure can trigger `/refine` on experimental blocks and a new execute/evaluate round; inconclusive results leave idea status unchanged. Explicit failure reasons and evidence-bearing graph edges persist. User stop saves partial progress; no whole-pipeline rollback is specified in the inspected procedure. Guidance includes independent-review request, conservative synthesis on disagreement and fatal-methodology priority. SRC-1: `.claude/skills/research/SKILL.md`, `.claude/skills/exp-run/SKILL.md`, `.claude/skills/exp-eval/SKILL.md`.

> **If `--auto` is not set**: display verdict and planned changes first, wait for user confirmation.
> --- `.claude/skills/exp-eval/SKILL.md`

> **Fatal findings take priority**: if either party finds a methodological issue (data leakage, unfair comparison), that finding takes precedence
> --- `.claude/skills/exp-eval/SKILL.md`

Theory account: Hypothesis/approach/risks and novelty argument are localized theory-bearing page sections; the verdict requests criticism against results and methodological auxiliaries. It may change reliance through status or failure reason and request revised tests, not necessarily rewrite the hypothesis. Retained idea/experiment pages and criticisms can reach another round. **theory-builder conditions 1–4**, separately: condition 1 conclusion status: afforded (whole hypothesis sections can be authored); condition 2 conclusion status: claimed (verdict prompt explicitly requests hypothesis-dependent decisions); condition 3 conclusion status: claimed (methodological concerns, concrete failure cause and resulting status/test changes requested); condition 4 conclusion status: claimed (refinement and rerun requested with retained results). None is an observed theory-building episode. Addressability is section/page-level in the procedure, with no claim of formal dependency tracking. Persistence is designed across sessions through Markdown/progress; attained use is unobserved. Under **learning**, improved future action and causal benefit remain uninspected. Reflection about AutoSci's own method is not established by criticism of external scientific hypotheses. Reflective theory building and full autonomous theory building remain uninspected: user gates, externally implemented agents and unspecified internal proposal quality prevent that attribution. No exercised self-improvement claim follows from product-idea revision alone.

#### RT-RTE-daily-intake
Label: Scheduled recommendation and optional ingestion

GitHub schedule/manual trigger → prepare evidence context → Claude action or compatible recommendation call/tool fallback → decisions/digest → optional ingest commits/push. CI code owns branch conditions and writeback; model owns paper judgment, with prompt-level high-confidence and maximum-count instructions. No reference-answer oracle; literature/wiki evidence guides an open-ended recommendation task. Operator mode/config and credentials enable the path; they are not per-content approvals.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Decision JSON, digest/artifacts, optional email and job status; auto-ingest may push wiki/raw changes.
- Later read-back: Actually committed wiki/raw content can reach future sessions/context preparation, but newly generated entities/graph/raw sources are ignored and CI uses unforced staging. Repository retention of every new payload is not established; tracked index/log changes can still persist. Actual subsequent consumption is unobserved.
- Delegated visibility: Action receives prepared arXiv/wiki/S2/DeepXiv evidence and broad tool permissions; compatible API receives compacted evidence, not arbitrary repository access from this caller.
- Selection predicate: Action instruction admits only high-confidence selections up to configured max_auto_ingest; compatible recommender requires inform mode in code. Missing Claude credentials selects recommendation/fallback instead of auto-ingest execution.
- Invalidation or expiry: Daily decision/digest files are run artifacts; actually committed wiki changes survive, not necessarily newly ignored payloads. Credential/provider errors and missing decisions can lead to fallback paths, not guaranteed model judgment.
- Activation or effect: Shipped workflow wires model-selected ingestion to a git writeback attempt in auto-ingest mode; unforced staging does not establish retention of every generated payload. Inform mode writeback exits without committing.
- Evidence limits: No CI trace, actual secrets, branch protection, push success or adherence to paper-count guidance is supplied.

Admission/rejection: The model can skip or mark maybe; operator can disable auto-ingest. Shell code attempts unforced staging of wiki and raw/discovered, commits only a nonempty staged diff and pushes. `.gitignore` excludes new entity/graph/raw payloads; already tracked files such as index/log can still be staged. Withhold unconditional cross-run repository-persistence claims for new payloads without tracking/staging conditions. No per-paper human veto or automatic semantic rollback is established in this route. The direct compatible path cannot perform ingestion through its `run_third_party_recommendation` entry. SRC-1: `.github/workflows/daily-arxiv.yml`, `tools/daily_arxiv.py`, `.gitignore`.

> git add wiki raw/discovered
> --- `.github/workflows/daily-arxiv.yml`

> raise RuntimeError("third-party LLM recommendation is inform-mode only; auto-ingest requires Claude Code runtime")
> --- `tools/daily_arxiv.py`

> --allowedTools "Read,Write,Edit,Bash,Skill,TodoWrite,Agent"
> --- `.github/workflows/daily-arxiv.yml`

#### RT-RTE-browser-write
Label: Browser and direct metadata admission

HTTP PATCH entity → server validates kind/slug/body → `research_wiki.py set-meta` subprocess → atomic metadata replacement → audit log and JSON response. Edge POST forwards to add-edge. Direct CLI callers reach the same helper without HTTP and without declaring a skill. Symbolic field/path/value controls drive writes; natural-language strings are retained without semantic truth validation. Browser caller supplies the content; its identity does not prove human authorship or review. No model or expected-answer oracle is needed for this path. Mode is direct requested editing, not a bounded experiment.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Helper result/error JSON; list appends may return partial success with per-item errors.
- Later read-back: Modified page metadata reaches subsequent browser queries, compiler scans and model page reads; audit records reach the wiki log.
- Delegated visibility: Python subprocess receives path/field/value, not a skill role or reviewer verdict.
- Selection predicate: API requires known entity type, valid slug, existing page and provided field/value; set-meta parses/replaces fields. This does not assert that every possible schema value or lifecycle transition is approved.
- Invalidation or expiry: Persisted metadata lasts until another edit; atomic replacement protects a single write, not a multi-item transaction or semantic rollback.
- Activation or effect: Direct file mutation is implemented. A later behavioral change through model consumption is not observed.
- Evidence limits: Current server exposure, authenticated principal and human edit intent are not supplied; loopback default is not a deployment guarantee.

Admission is caller-selected replacement/append. Server/helper can reject malformed input, but they do not consult writer-role policy. Recovery is an explicit subsequent edit or repository restoration, not a demonstrated automated semantic rollback. SRC-1: `tools/serve.py`, `tools/research_wiki.py`, `runtime/policy/writers.yaml`.

> args = ["set-meta", str(path), field, v]
> --- `tools/serve.py`

> tmp.write_text(new_content, encoding="utf-8")
> tmp.replace(p)
> --- `tools/research_wiki.py`

#### RT-RTE-hiera-search
Label: Hiera candidate admission and bounded evaluation

Explicit optional-path request → sidecar init from existing experiment → semantic point/draft authoring → admit immutable candidate → approve task contract → preflight/run/tune/loop → receipts/ledger → exploratory final report. Model/user author proposals; symbolic admission checks paths, editable files, config schema, semantic point, entrypoint, parents and operation label. Approve validates/freezes the contract, but code does not authenticate a human. Skill requires explicit human source/contract review. Executor is local subprocess or SSH remote worker, not the foreground model. Numeric score extraction and direction support candidate comparison; a finite score is not an expected-answer oracle. Benchmark truth/reference outcomes depend on the user-supplied evaluator and are uninspected.

- implementation conclusion status: wired
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: IDs/digests/readiness errors, preflight result, evaluation receipt/score or recovery instruction; finalize returns and persists FINAL_REPORT.json.
- Later read-back: Ledger reservations, evaluations and candidate state feed loop scheduling, summaries and experience counts. Wiki experiment/design source is snapshotted, not overwritten by finalization.
- Delegated visibility: Local child receives formatted argv/cwd and inherited process environment; remote worker receives bound job/candidate payload, runtime configuration and optional GPU selection. Provider model delegation is not necessary to run an admitted candidate.
- Selection predicate: Admission validates explicit candidate content; loop selects existing eligible candidates using ledger/scheduler state until rounds/budget/STOP. Screen/deep are orchestration labels, not automatic seed/model changes.
- Invalidation or expiry: Changed frozen contract or candidate digest is rejected; changed linked wiki source requests a new run. Existing candidate IDs cannot be overwritten by admit. Pending remote attempts retain reservations and are recovered rather than blindly resubmitted.
- Activation or effect: Code executes admitted argv, records result/receipt and updates candidate/ledger state; finalizer marks wiki_writeback none. Arbitrary executable code is not confined to sidecar by cwd alone.
- Evidence limits: No actual run, trusted evaluator, deployed remote configuration, scientific gain or secure isolation envelope is established. Detailed tuner/acquisition scoring internals were not fully inspected; their presence does not establish theory criticism or learning.

Admission/rejection/recovery: Proposal guidance is the selected experiment/design, semantic space, editable files, config schema, scoring objective and resource contract. User can withhold skill approval; software can reject invalid inputs and changed snapshots. Local failed/timeout/invalid-score attempts become receipts. Local preflight is explicit and does not reserve evaluation budget; evaluate does not itself require a stored successful preflight. Remote worker runs preflight before evaluation. Remote adapter reserves before submit and preserves recoverable handles on interruption. New immutable children are the revision unit; no automatic wiki promotion/formal winner is established. SRC-1: `.claude/skills/hiera-experiment/SKILL.md`, `tools/hiera/cli.py`, `tools/hiera/evaluator.py`, `tools/hiera/contract.py`, `tools/hiera/ledger.py`, `tools/hiera/remote_adapter.py`, `tools/hiera/remote_worker.py`, `tools/hiera/experience.py`.

> raise HieraError("candidate snapshot changed after admission")
> --- `tools/hiera/evaluator.py`

> if used >= budget:
>     raise HieraError(f"evaluation budget exhausted ({budget})")
> --- `tools/hiera/ledger.py`

> return ["bash", "-lc", env_setup + " && " + shlex.join(result)]
> --- `tools/hiera/remote_worker.py`

> "wiki_writeback": "none",
> --- `tools/hiera/cli.py`

Hiera's inspected loop compares scores and retains input/outcome records. This establishes executable search capacity, not content-directed criticism of a formulated explanatory theory. Candidate code could encode scientific models; its actual content is not supplied. No inference of theory-builder conditions, learning, reflection or exercised self-improvement is made from the loop's name or ledger alone.

#### RT-RTE-review-call
Label: Review MCP chat and provider-native search

Foreground tool request → local MCP adapter → configured Chat Completions provider → text result and optional thread ID. Agent chooses prompt/system/model and decides whether to act on returned text; provider decides response. Chat-reply appends current thread messages; failure pops the attempted user turn. Web search is a separate direct provider-tools request, not local host browsing or the retry/fallback chat branch. There is no answer oracle just because a reviewer is independent by instruction. Provider-native search behavior and external evidence quality are uninspected.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Text or structured error; successful chat returns threadId for follow-up.
- Later read-back: Process-local thread history reaches later chat-reply calls while the server lives; no durable cross-restart thread reload is established by this implementation. Foreground skills may separately retain verdicts in wiki pages.
- Delegated visibility: Provider receives supplied messages and model ID; native-search request additionally grants the provider-specific web_search tool. The adapter does not automatically send the whole wiki.
- Selection predicate: Chat caller can override configured model; third retry selects fallback. Chat-reply requires an existing thread ID; search uses default model and a separate tools payload.
- Invalidation or expiry: Thread dictionary is volatile process state; restart persistence is not wired here. Failed reply rolls back that user message; retries handle selected errors with finite limits.
- Activation or effect: Review text returns to model caller; exp-eval requests using it to admit status/edge changes, but the adapter itself does not write wiki verdicts.
- Evidence limits: Actual provider independence, live search support, model version and review correctness remain uninspected.

SRC-1: `mcp-servers/llm-review/server.py`, `.claude/skills/exp-eval/SKILL.md`.

> "tools": [{"type": "web_search", "max_keyword": 3, "force_search": True, "limit": 5}]
> --- `mcp-servers/llm-review/server.py`

#### RT-RTE-setup-skills
Label: Language and host configuration activation

Operator invokes setup with language selection → shell copies selected root contract/skill bodies/references → host later loads active files. Symbolic file-copy rules activate natural-language behavioral instructions. Operator chooses language and can edit files/configuration; script does not compare scientific performance or use an answer oracle. This is installation/configuration mode, not an evidence-responsive learning loop.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Activation messages and selected-language marker.
- Later read-back: inapplicable — shipped static instruction activation is not accumulated experience read-back; later host loading is nevertheless a behavioral-authority path.
- Delegated visibility: Host receives active CLAUDE.md/skill text; project MCP configuration and local permission settings can affect the available tool surface.
- Selection predicate: Selected i18n language directory supplies source files; existing local settings are preserved instead of overwritten.
- Invalidation or expiry: Re-running activation can overwrite active instruction copies; source-language tree persists. No measured regression check or automatic rollback is established in the inspected copy stage.
- Activation or effect: Copy operations install a different instruction surface for later host use; actual compliance/behavioral change remains unobserved.
- Evidence limits: Language equivalence, all platform activation details and actual host settings are not established by this Unix setup inspection.

Admission is operator invocation and file selection, followed by unconditional language copying, not per-skill human review. Replacement/recovery can use source copies or repository changes; an automatic performance-based veto is not established. SRC-1: `setup.sh`, `config/settings.local.json.example`.

> cp "$I18N_DIR/CLAUDE.md" CLAUDE.md
> --- `setup.sh`

### Claims

#### RT-CLM-writer-contract
Label: Writer ownership is policy, not authorization

AutoSci explicitly describes field/edge writer permissions as a declarative contract for skill authors and the agent, not runtime authorization. This is supported by the browser/direct CLI counterpath, not merely inferred from a search miss. The controlled guarantee is prompt-level writer discipline; the helper's symbolic integrity checks have narrower coverage. SRC-1: `runtime/policy/writers.yaml`, `tools/research_wiki.py`, `tools/serve.py`.

> # at the CLI. We deliberately did not plumb a `--skill` arg through set-meta /
> # add-edge: research workflows are fluid, and `/edit` exists as a designed
> # escape hatch for "per user request" overrides — runtime enforcement here
> # would either fight `/edit` or grow a long exception list.
> --- `runtime/policy/writers.yaml`

#### RT-CLM-sidecar-confirmation
Label: Exploratory search is not formal confirmation

The Hiera skill claims search isolation and requires a return to normal experiment workflow for confirmatory claims. The finalizer supports the narrower implementation claim of report-only writeback. Neither the label nor source snapshot checks establish a sandbox against arbitrary candidate code. SRC-1: `.claude/skills/hiera-experiment/SKILL.md`, `tools/hiera/cli.py`, `tools/hiera/evaluator.py`.

> It does not replace /exp-design, /exp-run, /exp-eval, or /research. A confirmatory result must return to the normal, user-gated workflow.
> --- `.claude/skills/hiera-experiment/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-instructions
Label: Activated skill instruction authority

Consumer: external foreground/delegated coding agent. Channel: active root contract, skill text, references and selected schema/template content loaded into its invocation. Force: model-interpreted operating instructions, not OS confinement or authenticated role restrictions. Horizon: installed files can influence many sessions until replaced; actual loading/compliance is external. Setup can replace this surface from a language source. SRC-1: `setup.sh`, `.claude/skills/ingest/SKILL.md`, `runtime/policy/writers.yaml`; see [RT-RTE-setup-skills](#rt-rte-setup-skills).

> cp -R "$skill_dir"/. ".claude/skills/$name/"
> --- `setup.sh`

#### RT-BAP-retained-context
Label: Retained wiki context into future judgment

Consumer: ask/research/experiment agent. Channel: generated context_brief plus requested full page reads. Force: evidential and task-guiding natural-language content; symbolic selectors determine what is delivered, but delivery is not proof of behavioral dependence. Horizon: later invocations/sessions while retained pages/brief survive; actual attained activation unobserved. Experiment failures can be summarized as anti-repetition guidance. SRC-1: `.claude/skills/ask/SKILL.md`, `tools/research_wiki.py`; see [RT-OBJ-context-brief](#rt-obj-context-brief) and [RT-RTE-knowledge-cycle](#rt-rte-knowledge-cycle).

> sections.append(f"## Failed Ideas (avoid repeating)\n{text}\n")
> --- `tools/research_wiki.py`

## Annotations

none
