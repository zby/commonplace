# Source reconstruction: the context-operation interface bounds context policy

This file reconstructs the commissioned claim from the supplied inputs. It is
not target prose and does not choose the final note's paragraph structure.

## Commission and evidential frame

- The governing question is how the interface between retained state and
  active context constrains realizable context-management policies, holding the
  retained substrate, model, and resource budget fixed. The authoritative
  contribution is that the available operations and allowed compositions bound
  the projections a policy can realize; improving the controller can improve
  selection within that bound without thereby expanding, validating, or proving
  the optimality of the interface. This is selected intent, not empirical
  evidence. **Basis:** authoritative user direction in
  `kb/work/context-operation-interface-multistage-prompt.md` and the run's
  `brief.md`.
- The required durable contribution is one transferable, truth-apt architecture
  claim that remains after any one system description is removed. Named systems
  must be proposition-relative witnesses rather than the subject of a survey.
  The final note needs a claim title, its mechanism near the top, and a real
  `## Scope` section. **Basis:** `kb/notes/COLLECTION.md`, `kb/types/note.md`,
  and the authoritative user direction.
- The connection report, comparative review, generated table, and matrix are
  advisory navigation or landscape context. They can expose candidate contrasts
  and missing comparison axes, but they are not factual authority for a named
  system. **Basis:** role assignments in the brief and
  `kb/reports/connect/sources/context-as-an-environment.connect.md`.
- Evidence tiers must remain visible. Fractal, Virtual Context, Letta,
  OpenViking, and Playground are pinned, code-grounded reviews. The Prime Agent
  and Recuris ingests combine static code grounding for mechanisms with
  paper-only outcome claims. Scroll, lambda-RLM, and ACM are paper-grounded
  preprint ingests; AgeMem is explicitly doc-grounded. The RLM walkthrough and
  Slate are practitioner reports; The Log Is the Agent is a conceptual essay.
  Static inspection establishes present code paths and checked-in intent, not
  runtime correctness or benchmark causality. **Basis:** the classification,
  evidence-basis, code-grounding, and limitations sections of the enumerated
  system artifacts.

## Working definitions

| Term | Reconstructed meaning | Status and basis |
|---|---|---|
| **Retained substrate** | State available outside the bounded active model input: for example an event log and payloads, files, database rows, a REPL namespace, archived messages, summaries, or memory records. Retained controller state such as learned weights or an invocation policy must be kept analytically separate when it selects projections but is not itself projected into the current input. | **Inference**, constrained by the required retained-substrate/active-context distinction and instantiated across Scroll, Prime Agent, Fractal, ACM, AgeMem, Virtual Context, Letta, OpenViking, Playground, and Recuris. |
| **Active context** | The instructions and information actually supplied to one bounded model invocation. It is not the whole retained store and not the later behavioral use of what was supplied. | **Inference** from `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md` and `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`, consistent with the user direction. |
| **Context-operation interface** | The operations and allowed compositions through which a controller locates, materializes, transforms, and exposes retained state as active context. | **Authoritative definition** from `kb/work/context-operation-interface-multistage-prompt.md` and the brief. |
| **Projection** | A task- and state-conditioned view delivered into active context after a permitted sequence of operations. A projection may be a raw slice, selected record set, summary, filtered or aggregated result, restored tool output, injected core block, or hierarchy level. The word does not imply a lossless, linear, idempotent, or non-mutating mathematical projection; an interface trace can update retained state before yielding a view. | **Inference** needed to make the commission operational; the examples are supported by the enumerated RLM/Scroll, ACM, Virtual Context, Letta, OpenViking, and Playground artifacts. |
| **Controller or context policy** | The mechanism that chooses whether, when, and how to invoke the interface: the acting model, a separately learned policy, a host/proxy, or a mixed arrangement. | **Inference** from the required distinction and the control placements documented by Scroll/RLM, ACM/AgeMem, Virtual Context/Playground, and Letta/OpenViking. |
| **Projection boundary** | The point at which selected or derived retained state becomes input to a bounded model call, including who owns the final selection and whether the receiving model can request expansion. | **Inference** from the explicit-print boundary in the RLM/Scroll family, pre-call proxy injection in Virtual Context, system-prompt assembly in Letta, hook/middleware injection in OpenViking, and pre-request cover construction in Playground. |
| **Projection fidelity** | Whether the task-relevant distinctions and evidence survive the particular selection, transformation, and exposure that reaches the model. It is distinct from storage fidelity: exact originals can remain retained while a summary, query, ranking, or activation decision omits what the call needs. | **Inference** supported by ACM's raw-message archive plus selective summary/query path, Virtual Context's raw turns plus derived layers, Letta's raw recall store plus compaction/core blocks, OpenViking's L2 content plus L0/L1 sidecars, and `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`. |

The controller is not automatically the same component as the model receiving
the projected context. A model can select its own view, a learned controller can
choose memory operations for another acting step, or a proxy can assemble the
view before the receiving model sees it. **Basis:** Scroll/RLM, ACM/AgeMem,
Virtual Context, Letta, OpenViking, and Playground as listed below.

## Reconstructed mechanism

The following is an explicitly labeled formalization, not notation supplied by
any one source.

**Inference — structural reachable set.** Let:

- `S` be the initial retained state;
- `x` be the current task signal and run state available to the controller;
- `I` be the context-operation interface, including operation semantics,
  addressable units, allowed compositions, and the exposure boundary;
- `M` be the fixed model or models used by the interface; and
- `B` be the fixed resource budget, including active-context, call, time, and
  tool limits where applicable.

Define `Reach(I, S, x; M, B)` as the set of active-context views obtainable by
legal interface traces under those premises. A trace may alternate locating,
reading, transforming, recursive calls, and exposure, and may update retained
state before producing a view. A particular policy `pi` selects traces and thus
induces an achieved subset or distribution over `Reach`.

This formalization yields three material consequences:

1. If a required view needs an unavailable operation, an unavailable addressable
   distinction, or a forbidden composition, no invocation policy over `I` can
   produce it. This is the context-projection instance of an information or
   action-closure omission in
   `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`.
2. A better policy can choose useful legal traces more often, sequence them more
   reliably, or avoid bad invocations. Those gains change achieved coverage,
   reliability, or cost inside `Reach`; they do not show that projections outside
   `Reach` were unnecessary. **Basis:** the fixed-decomposition note and the ACM
   and AgeMem fixed-operation/learned-policy cases.
3. Changing the operation semantics, addressable unit, allowed composition,
   projection boundary, model, retained substrate, or budget changes a premise
   and may change `Reach`. An evaluation must therefore say which of these were
   fixed and which were learned. **Basis:** authoritative user direction and the
   cross-system contrasts reconstructed below.

`Reach` is a structural outer envelope, not a claim that every admitted trace is
practically discoverable or reliable. A model may fail to write valid code, a
controller may never invoke an available operation, or visible material may
still fail to influence action. The fixed-decomposition note explicitly allows
a stronger learner to recover more distinctions or compose more responses
behind an unchanged nominal interface. There is no conflict if the levels are
kept separate: better competence can enlarge the *achieved effective subset*
of a fixed admitted set. If the purported policy improvement adds external
computation, new observations, new tools, a broader learned latent state treated
as part of the model, or permission to edit operation definitions, then one of
the premises has changed and it is not merely improved invocation of a fixed
interface. **Basis:**
`kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md` plus
the user direction holding model and budget fixed.

## Material distinctions the claim must preserve

| Distinction | Reconstructed account | Supporting inputs |
|---|---|---|
| Retention vs active context | Keeping an exact or durable record determines what may remain available; it does not determine which bounded view is supplied to the next call. Context assembly is a separate runtime responsibility from external storage. | `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md`; Scroll, ACM, Virtual Context, Letta, OpenViking, and Playground artifacts. |
| Interface vs controller | `I` supplies operations and composition rules; `pi` selects among them. A learned invocation policy is not evidence that its hand-designed operations are complete. | `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`; ACM and AgeMem. |
| Availability vs successful activation | An operation or retained item can be callable yet never selected. A selected view can also reach context without changing action. The target claim concerns the first boundary—what can reach context—while contextual activation remains a further test. | `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`; Scroll's reported reachable-but-missed trajectories; ACM's learned invocation/abstention. |
| Access vs transformation | Locate/search/read operations reduce access burden; filter, aggregate, summarize, join, or model-mediated interpretation reduce transformation burden. Retrieval-only matrices can therefore miss a material difference between systems that find the same record but expose different transformations before the next call. | `kb/notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md`; RLM/Scroll, lambda-RLM, and Virtual Context. |
| Open programming vs restricted composition vs fixed memory operations | Open Python/REPL interfaces permit model-authored compositions subject to sandbox and budget; lambda-RLM supplies a typed, pre-verified combinator language; ACM and AgeMem supply small fixed memory-operation sets whose invocation is learned. These are interface classes, not a performance ranking. | RLM walkthrough, Scroll ingest, lambda-RLM ingest, ACM ingest, and AgeMem review. |
| Controller placement | Scroll/RLM let the model select and expose a view; ACM/AgeMem learn an invocation controller over supplied operations; Virtual Context and Playground let host machinery assemble a view; Letta and OpenViking mix pre-call push with model-requested pull/expansion. Control placement is independent of operation richness. | The corresponding enumerated artifacts. |
| Persistence horizon | REPL variables may persist only within a run; kernel/session state may survive turns or restarts; learned weights or retained invocation policies may shape later tasks. Persistence changes what a controller can condition on, but does not by itself show that the operation repertoire changed. | RLM walkthrough; Prime Agent and Fractal; AgeMem and Recuris. |
| Fixed interface vs changing policy | ACM trains when to invoke two fixed actions; AgeMem trains a cross-task policy over six fixed actions; Recuris permits gated changes to an invocation-policy component while the outer runtime and component decomposition remain fixed. Policy mutability and interface mutability must be recorded separately. | ACM, AgeMem, and Recuris artifacts. |
| Storage fidelity vs projection fidelity | Raw messages, full turns, event logs, or L2 files can remain recoverable while the active summary, ranked result, hierarchy level, or temporal cover omits a needed distinction. Exact retention expands what could be reconstructed; it does not guarantee that the operative view is exact or useful. | ACM, Virtual Context, Letta, OpenViking, Playground, and `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`. |
| Context operation vs world effect | “Action alphabet” is already used for the authorized primitive operations that affect the world. Context location, transformation, and exposure are a different interface and should be named `context-operation interface`. | Authoritative user terminology direction and `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md`. |

## Comparison corpus inventory

The corpus is deliberately broader than the evidence the final note needs. The
last column identifies the system's reconstruction role; it is not a later-stage
claim disposition.

| Artifact/system | Evidence tier | Interface, controller, projection, and persistence facts material to this question | Reconstruction role |
|---|---|---|---|
| Scroll (`kb/sources/context-as-an-environment.ingest.md`) | Paper-grounded preprint; public implementation not inspected in this ingest; no retained Quotes | Reported append-only Event Log and externalized payloads; persistent sandboxed Python namespace; model-written search, expansion, SQL/Python transformation, and permitted tools; only explicit `print` output enters the next bounded working view; event schema, sandbox, index, eviction, prompts, and budgets remain fixed. | **Argumentative anchor if grounded:** broad programmable composition plus an explicit model-owned projection boundary; also demonstrates that “programmable” is still bounded. |
| Prime Agent (`kb/sources/prime-agent-a-self-improving-rlm-harness.ingest.md`) | Static code-grounded mechanisms at a pinned commit; outcomes paper-only | Long-lived IPython and typed host bridge; kernel snapshots/restores on resume; recursive sessions; versioned prompt, memory, skill, and subagent state; immutable base prompt and fixed runtime/topology outside the editable surface. | Persistence-horizon and mutable-policy/harness support; not needed for the basic interface/controller proof. |
| Fractal (`kb/agentic-systems/fractal.md`) | Code-grounded review; no live turn run | PredictRLM exposes workspace and session history through REPL variables; the model writes Python orchestration; a rendered session summary is always visible while full history is inspectable from a variable; session state survives turns outside the workspace; generated orchestration has no demonstrated promotion path. | Code-grounded RLM-family corroboration and within-session continuity; redundant if a smaller contrast suffices. |
| Practitioner RLM walkthrough (`kb/sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md`) | Practitioner report with retained source Quotes | Prompt is externalized as a `context` variable; model writes programmatic search/slicing/transformation; print is scaffold-truncated; subagent returns stay as REPL variables rather than automatic parent-context injection; a constructed variable can be returned as the answer. | **Argumentative anchor:** clearest directly quoted open-program/interface and explicit-exposure mechanism. |
| lambda-RLM (`kb/sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md`) | Paper-grounded preprint with retained source Quotes; implementation not inspected | Same prompt-as-environment family, but arbitrary model-written programs are replaced by seven named typed combinators (`SPLIT`, `MAP`, `FILTER`, `REDUCE`, `CONCAT`, `CROSS`, `PEEK`); a planner fixes the chain and structural parameters; neural work occurs at bounded leaves or specified synthesis steps. | **Argumentative anchor:** sharpest restricted-composition contrast to open RLM programming. |
| ACM (`kb/sources/acm-agentic-context-management-for-long-horizon-tasks.ingest.md`) | Paper-grounded preprint with retained source Quotes; implementation not inspected | Two fixed operations: `manage_context` summarizes a chronological prefix and archives raw messages under an identifier; `query_memory` retrieves from archived raw messages. Post-training learns invocation and abstention, not a new state representation or operation set. | **Argumentative anchor:** strongest measured case of controller improvement inside a fixed interface. |
| AgeMem (`kb/agent-memory-systems/lightweight/agemem.md`) | Doc-grounded lightweight review; no code inspected | Six hand-designed actions: LTM `Add`, `Update`, `Delete`; STM/context `Retrieve`, `Summary`, `Filter`. RL learns an offline, cross-task policy in model weights for choosing them. | Corroborates operation-set/policy separation and cross-task retained policy; ACM is the cleaner quoted representative. |
| Virtual Context (`kb/agent-memory-systems/reviews/virtual-context.md`) | Code-grounded review at a pinned commit | Proxy stores canonical traces, derives summaries/facts/tags, retrieves through lexical/embedding/ranking signals, assembles a bounded summary/segment/full-text view, injects it before the provider call, and exposes paging/restore tools. | **Argumentative anchor:** proxy-owned initial projection with a later model-pull expansion path. |
| Letta (`kb/agent-memory-systems/reviews/letta.md`) | Code-grounded review at a pinned commit | Core blocks are rendered into the system prompt; recall messages and archival passages remain behind explicit search tools; overflow compaction produces a summary plus recent messages. | **Argumentative support:** clearest mixed push/pull boundary; one compact example can replace a broader system list. |
| OpenViking (`kb/agent-memory-systems/reviews/openviking.md`) | Code-grounded review at a pinned commit | `viking://` filesystem addresses resources/memories/sessions; fixed `find`, `search`, `read`, `list`, and write operations; L0/L1/L2 disclosure, token budgets, and hierarchical retrieval; hooks/middleware can push context before a call while tools permit pull. | Hierarchical/addressable-unit support; mostly redundant with Virtual Context and Letta for the central proof. |
| Playground (`kb/agent-memory-systems/reviews/playground.md`) | Code-grounded review at a pinned commit | Temporal summary chunks form a hierarchy; host code selects a budgeted temporal antichain before each request; recent “moment” turns are appended; explicit range retrieval is available. Selection is temporal/hierarchical rather than task-semantic. | Useful boundary for how addressable unit and host selection restrict possible projections; omit if the note stays compact. |
| Recuris (`kb/sources/recursive-experiential-working-memory-evolution.ingest.md`) | Static code-grounded mechanisms at a pinned commit; benchmark outcomes paper-only | Verified pending/done/blocked state and typed events drive skill activation; the invocation policy is one editable component; component-scoped patches pass a paired gate; base model, runtime kernel, four-component decomposition, legal edit surface, and gate remain fixed. | **Argumentative support:** changing retained invocation policy without treating the outer interface/decomposition as validated. |
| The Log Is the Agent (`kb/sources/the-log-is-the-agent-2065129901427130678.ingest.md`) | Conceptual essay; no retained Quotes | Argues for a durable append-only event log and treats compacted views as regenerable projections, but leaves the task-shaped view-rendering policy substantially unspecified. | Optional negative control: retention does not specify projection. The sovereignty/ownership thesis is off-question. |
| Coding Agents Are Effective Long-Context Processors (`kb/sources/coding-agents-are-effective-long-context-processors.ingest.md`) | Paper-grounded preprint; no retained Quotes | Generic filesystem search, slicing, scripting, and iterative refinement provide a programmable projection baseline. The study does not isolate file hierarchy, tools, prompts, and backbone. | Optional boundary showing a broad, nonspecialized interface; not evidence that programming is universally superior. |
| Slate (`kb/sources/slate-moving-beyond-react-and-rlm.ingest.md`) | Practitioner product report; no controlled evaluation and no retained Quotes | A host orchestrator dispatches bounded worker episodes and admits compressed episode returns rather than exposing a memory-query interface; compression quality is assumed rather than tested. | Optional orchestration-side projection boundary; not needed for the memory-interface argument. |

## The few contrasts that do argumentative work

1. **Open programming versus restricted composition:** the quoted practitioner
   RLM account (or grounded Scroll) versus lambda-RLM holds the broad
   prompt-as-environment idea roughly stable while changing the composition
   language from model-written Python to a typed combinator library. This makes
   interface expressivity and controller quality separable without claiming
   either design wins universally. **Basis:** the RLM and lambda-RLM ingests.
2. **Learned controller versus fixed operations:** ACM fixes two operations and
   learns when to invoke or abstain. The paper reports Qwen3.5-9B Pass@1 moving
   from 0.635 to 0.727 on BrowseComp-Plus, 0.405 to 0.425 on DeepSearchQA, and
   0.508 to 0.530 on SWE-Bench Verified under its ACM-training comparison. These
   are useful conditional gains, not a comparison with rival operation sets.
   AgeMem's six-operation learned policy corroborates the architecture pattern
   without adding another necessary empirical claim. **Basis:** retained Quotes
   and analysis in the ACM ingest; the AgeMem doc-grounded review.
3. **Model-owned versus host-owned versus mixed projection:** RLM/Scroll expose
   only what model-authored code prints or returns; Virtual Context assembles and
   injects the initial view in a proxy; Letta always pushes core blocks but makes
   recall/archive content model-pull. This isolates projection control from
   storage and from transformation vocabulary. **Basis:** the corresponding
   enumerated artifacts, preserving their tiers.
4. **Changing invocation policy versus changing the interface:** Recuris can
   patch and retain its invocation-policy component under a gate while the outer
   runtime, component decomposition, and legal surface stay fixed. Prime Agent
   and Fractal add persistence-horizon contrasts, but they are not needed to
   establish the main boundary. **Basis:** Recuris, Prime Agent, and Fractal
   artifacts.

No cross-system contrast above is a controlled experiment. It establishes that
the architecture variables can vary independently in shipped or described
systems; it does not estimate a causal performance effect of changing one axis.
**Basis:** the differing system scopes and the explicit evaluation limitations
in their artifacts.

## Quantitative evidence and its limited role

- ACM's two-operation training comparison is material because it is a direct
  instance of policy gains under a held-fixed operation decomposition. The three
  Pass@1 pairs above are paper-reported and directly retained in the ingest's
  Quotes. They support “useful improvement occurred in this interface,” not
  “this interface is complete or optimal.” **Basis:** ACM ingest plus
  `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`.
- lambda-RLM reports beating normal RLM in 29 of 36 model-task accuracy
  comparisons and 3–6x lower latency among recursive methods, while the ingest
  records that normal RLM's seven wins concentrate mostly in stronger models or
  CodeQA-like settings. This is scope evidence against equating a formally
  broader composition language with better practical performance. It is not a
  matched proof of a general expressivity/reliability frontier and need not be
  retained in the final note. **Basis:** lambda-RLM ingest, paper-grounded.
- The comparative landscape reports 148 code-grounded systems and broad
  read-back/trace-learning statistics, but the currently supplied CSV has 152
  data rows (153 lines including its header), whereas the generated table and
  comparative review still say 148. The advisory artifacts are therefore not
  synchronized. Their population quantities should not enter this target.
  **Basis:** `kb/agent-memory-systems/agentic-memory-systems-comparative-review.md`,
  `kb/agent-memory-systems/systems-table.md`, and the complete supplied
  `kb/agent-memory-systems/systems.csv`.

## Conflicts, tensions, and evidence-strength differences

- **Formal breadth versus practical reliability/cost.** Open-ended Python can
  express compositions absent from a fixed combinator library if the same
  primitives, semantics, model competence, and budget make those programs
  executable. lambda-RLM's paper reports practical gains from restriction, and
  its limitations report settings where normal RLM wins. The warranted
  conclusion is a tradeoff between admitted transformations and reliable,
  inspectable, trainable, or cheaper use—not that the largest interface is
  always best. **Basis:** lambda-RLM ingest and the user's explicit exclusion of
  a programmable-interface superiority claim. The conditional-subset statement
  is an **inference**, not a measured result.
- **Exact storage versus faithful active view.** Scroll's exact-history framing,
  ACM's archived raw messages, Virtual Context's canonical turns, Letta's recall
  messages, and OpenViking's L2 files coexist with selective summaries,
  rankings, hierarchy levels, or queries. There is no factual contradiction:
  “lossless storage” and “lossy or missed projection” concern different layers.
  **Basis:** those system artifacts and
  `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`.
- **RLM ephemerality versus persistent RLM harnesses.** The RLM note calls the
  model-written orchestrator ephemeral. Prime Agent snapshots/restores kernel
  and typed harness state, and Fractal retains session summaries and traces.
  These soften run-state ephemerality but do not demonstrate tested cross-task
  promotion of arbitrary generated orchestration strategy. Within-run state,
  cross-restart state, and cross-task policy must not be collapsed. **Basis:**
  `kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`,
  Prime Agent ingest, and Fractal review.
- **Nominally fixed interface versus effective learner capability.** Existing
  theory says a stronger learner may enlarge the effective space behind an
  unchanged interface through histories, latent state, tools, or reliable
  composition. The commission's claim remains correct as an outer bound only if
  model, observations, resources, and allowed compositions are declared fixed.
  **Basis:** fixed-decomposition note and user commission. The outer-envelope
  resolution is an **inference**.
- **Code-grounded architecture versus paper outcomes.** Pinned static inspection
  gives stronger support for operation surfaces and wiring than a paper or
  practitioner description, but it still does not show the paths ran correctly.
  Prime Agent and Recuris explicitly classify benchmark outcomes as paper-only.
  Paper-reported improvements must not inherit the code-grounded tier of the
  mechanisms. **Basis:** the evidence-basis and limitation sections of the
  supplied reviews and hybrid ingests.
- **Landscape schema versus governing question.** The matrix records storage,
  read-back direction, targeting, trace learning, curation, and authority. It
  does not record the transformation language or the final projection boundary,
  so rows marked equally “both/targeted” can still expose very different
  reachable views. This is an **inference from the supplied schema and system
  cases**, consistent with the advisory connection report. It motivates the
  target claim but does not authorize changing the matrix in this run.

## Evaluation consequences reconstructed from the inputs

- An evaluation of a learned or improved controller must inventory the retained
  substrate, addressable unit, available locate/read/expand/transform/summarize/
  filter/delete/expose operations, allowed compositions, controller placement,
  projection boundary, persistence horizon, mutable artifacts, model, and
  resource budget. Otherwise “the policy improved” does not identify which
  design assumptions remained controlled conditions. **Inference from:** user
  comparison axes, the corpus, and the fixed-decomposition note.
- Benchmark gains with one operation set show that some policy over that set was
  useful in the tested regime. Testing interface adequacy requires a
  constraint-changing intervention, a rival operation/composition set, or a
  proof that excluded projections cannot improve the objective. **Inference
  from:** fixed-decomposition note and ACM's limitations.
- Availability, exposure, behavioral uptake, and downstream benefit are distinct
  evaluation rungs. The new note should stop its main mechanism at exposure into
  active context, then point to contextual activation as the next boundary
  rather than claiming that a reachable projection is used. **Basis:**
  `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`.
- A more restricted interface can be rationally selected for reliability,
  safety, inspectability, trainability, latency, or cost even when it admits fewer
  transformations. Conversely, a programmable interface remains bounded by its
  sandbox, primitives, permitted compositions, model competence, and budget.
  **Basis:** lambda-RLM and Scroll/RLM limitations plus authoritative user scope.

## Non-blocking evidence guards

- **EVIDENCE NEEDED (non-blocking; only if retained as a named-source dependency):**
  the Scroll ingest currently has no retained Quotes. Any final claim about its
  Event Log, persistent Python namespace, eviction index, or explicit-print
  boundary must either be grounded through the multistage source guard or be
  omitted. The central contribution does not depend on Scroll specifically.
- **EVIDENCE NEEDED (non-blocking; only if retained as named boundary evidence):**
  The Log Is the Agent, Coding Agents Are Effective Long-Context Processors, and
  Slate ingests also retain no Quotes. Their optional details should be omitted
  unless later grounding supplies the source-side proposition actually used.
- No unresolved definition or user decision blocks claim disposition. The
  authoritative definition and intended contribution are fixed, and every
  optional system can be omitted without weakening the central mechanism.

## Concrete available details to omit from the target

- Scroll's leaderboard scores, the full component-ablation table, and claims of
  benchmark superiority; they do not establish interface optimality and the
  ingest has no retained Quotes.
- Prime Agent's Factorio exploit, family-message topology, cron/heartbeat
  machinery, descendant accounting, and benchmark bundle; useful elsewhere but
  not needed to explain projection reachability.
- Fractal's direct workspace-mount mechanics, CLI exit/output schema, stale
  session-directory documentation, and the 20,000-character `AGENTS.md` limit.
- Virtual Context's storage-backend catalogue, dashboard/TUI surfaces, full
  curation taxonomy, and adoption comparisons with Commonplace.
- Letta's optional git cache details, sleeptime governance, tool embeddings, and
  broad write-side artifact taxonomy except where one sentence is needed to
  distinguish retained policy from projected content.
- OpenViking's tenant headers, service audit machinery, full extraction pipeline,
  and integration catalogue; retain only hierarchy, operations, and push/pull
  boundary if it is selected at all.
- Playground's “breath” cache device, unresolved faculty symlink, diagnostics,
  and archive-import details; retain only the temporal-cover mechanism if needed.
- Recuris benchmark gains, patch counts, Factorio-like safety material, and
  component-localization claims; its relevant fact is the editable invocation
  policy inside a fixed outer surface.
- The Log Is the Agent's sovereignty/lock-in claim and world-effect discussion;
  Coding Agents' leaderboard and corpus-size headline; Slate's AlphaZero analogy,
  vendor comparison table, and product-superiority claims.
- The matrix's storage/trace-learning population statistics, the current
  148-versus-152 freshness mismatch, and Commonplace-specific “borrowable ideas.”
  None is needed to establish the target architecture claim.

