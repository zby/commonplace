# Responsibility matrix for the base workflow system

Keep the extracted base usable without Commonplace while preserving the
guarantees that Commonplace needs from its workers.

Prepared 2026-10-19 at the operator's request. The
[workshop framing](./README.md) fixes the agreed scope. This matrix proposes
the detailed ownership boundary for extraction; it describes intended
responsibilities, not capabilities already verified in the implementation.

## Owners

- **Base:** the reusable execution and result-recording code, including its
  harness adapters. An adapter translates a request into a headless harness
  invocation and interprets the harness's execution evidence.
- **Workflow:** caller-written code that selects jobs, supplies their inputs
  and checks, and decides what follows their results. In Commonplace this
  includes the analysis sequence and correction cascade.
- **Artifact layer:** Commonplace's types, validation and interpretation of
  verification and correction records. The base must also work without it.
- **Host:** the caller's setup and operation of the working directory,
  installed tools, permissions and external services. This is a responsibility,
  not a proposed environment-provider API.
- **Publication:** Commonplace's assembly, publication and integration code.
  Other consumers supply their own handling of external effects.

Each row names one accountable owner. Other components may supply inputs or
execute a check without owning its policy.

## Execution and results

| Responsibility | Owner | Inputs and guarantee at the boundary |
|---|---|---|
| Choose model work and its order | Workflow | Calls into the base encode branches, loops and independent groups. The base does not infer a dependency graph or drive an orchestrator agent. |
| Compose the task | Workflow | Supplies task instructions, named input contents, output names and worker selection. Domain prompts stay outside the base. |
| Launch a headless worker | Base | Translates the supplied worker configuration for a supported harness, uses the supplied working directory, and reports launch outcome. Model choice remains the caller's. |
| Render delivery paths | Base | Materializes supplied inputs and the per-launch prompt/output paths. This mechanical frame does not add KB roles or type rules. |
| Separate launch outputs | Base | Every launch, including relaunches, receives fresh output paths. Collects only that launch's files; this is not filesystem access enforcement. |
| Detect delivery problems | Base | Distinguishes missing required outputs, a worker-reported inability to finish, and a failed process. File presence does not imply content acceptance. |
| Attribute results | Base | Retains exact returned content and its launch evidence, including available harness/session/model identity. Missing evidence remains explicit rather than guessed. |
| Limit concurrency | Base | Enforces the supplied launch limit. The workflow chooses which calls are independent and how their results are combined. |
| Relaunch after execution failure | Base | Implements a documented, bounded failure policy with fresh output paths and retained failure evidence. Does not equate every failed exit with a rejected document. |
| Select retry and correction allowances | Workflow | Supplies limits appropriate to the task. Limits apply to defined events; changing their meaning is a contract change. |
| Enforce supplied limits | Base | Records and counts the events defined by its contract, including across resume. The workflow passes the remaining role allowance when several calls share a budget. |
| Own a run's execution records | Base | Prevents competing controllers from concurrently updating the same run and commits reusable results without exposing partial records. Does not lock the whole project. |

## Checks and workflow decisions

| Responsibility | Owner | Inputs and guarantee at the boundary |
|---|---|---|
| Interpret output types | Artifact layer | Checks schemas, required members, identities, citations and other declared relationships. Returns findings over specified content. No KB parser or type registry is required by the base. |
| Select stable comparison inputs | Workflow | Freezes the sibling outputs and criteria a check is to use before a parallel round. Supplies that snapshot to checks; checks must not silently consult changing sibling state. |
| Apply a supplied check | Base | A bounded check-and-retry helper may invoke the caller's check on a delivered result and return findings. The base does not choose what constitutes a valid artifact. |
| Interpret verification and correction obligations | Artifact layer | Determines which exact subjects a verdict covers and what a correction must answer. Markdown blocker syntax and Commonplace verdict rules stay here. |
| Build correction requests | Workflow | Uses findings and prior outputs to commission the next task. Chooses correction order and when independent verification must run again. |
| Decide progression and stopping | Workflow | Interprets execution outcomes and domain judgments. Cached delivery alone never authorizes publication or establishes that a current check passes. |

The base's check helper, if retained, must accept caller-defined checks and
feedback construction. It must not import Commonplace's refusal parser to
make a generic retry work. Reuse of delivered content and reuse of an
acceptance decision are different: the workflow must rerun the check against
the intended snapshot, or explicitly establish that the prior judgment still
applies.

## Environment, resumption and effects

| Responsibility | Owner | Inputs and guarantee at the boundary |
|---|---|---|
| Prepare the execution environment | Host | Supplies the working directory and runnable harnesses. Worktrees, dependency installation, pinned code and environment checks remain outside the base. |
| Enforce worker access restrictions | Host | Configures sandbox, credentials, filesystem and network permissions. The base passes supported launch settings but does not claim to enforce restrictions itself. |
| Identify reusable calls within a run | Base | Keys delivered results by the declared request material, including supplied input contents and relevant worker settings. Does not discover ambient dependencies. |
| Establish whether reuse remains valid | Host | Maintains the environment required by the workflow's resume contract. A changed environment may require a new run. Cross-run caching is outside the initial scope. |
| Reconstruct workflow progress | Workflow | Re-executes its ordinary control flow using retained results. Controls its own decisions and budgets; the base does not persist a general scheduler. |
| Report interrupted or stopped execution | Base | Documents what survives a stop, what may repeat and what happens to launched processes. The exact contract must be settled before implementation; durable results do not promise exactly-once execution. |
| Authorize operational recovery | Host | Repairs environmental failures and decides when to resume or start anew, within the documented interruption contract. Automatic recovery from every failure is outside scope. |
| Assemble and publish | Publication | Uses exact accepted members and verifies publication conditions. Owns destination locks, replacement checks, effect journals and integration. A cached worker result is not a transaction around external effects. |

## Decisions still needed before extraction

The following choices need evidence from the independent implementation and
its example workflow. The [implementation plan](./implementation-plan.md)
proposes initial defaults and phases for resolving them; no decision waits
for the headless branch. They do not authorize widening the agreed scope:

- Which execution failures permit relaunch, and how launch failures, timeouts,
  incomplete outputs and content rejections spend their respective budgets.
- What a normal stop, timeout and abrupt controller loss guarantee about
  surviving workers, and what the operator must establish before resuming.
- Whether the example warrants a generic check-and-retry helper, or whether
  only launch/result primitives belong in the first release.
- Which harnesses have sufficient adapter and real-execution evidence to be
  supported initially, and what execution evidence each can actually provide.
- Where the package lives and whether Treadle is reused. These choices do not
  require compatibility with the earlier step-program protocol.

## Boundary acceptance

An ordinary-file workflow must launch, check, retry and resume without any
Commonplace imports or a Git worktree. This is the package's independent
acceptance boundary. A later Commonplace integration must retain its type
checks, verification rules and publication protections; it is not a package
release prerequisite. Exercise the failure and completion-order cases in the
workshop framing.

Record any unresolved ownership conflict before extraction reaches that
interface. In particular, a base helper that needs to understand a KB type,
prepare a worktree, or select a correction cascade has crossed this boundary.
