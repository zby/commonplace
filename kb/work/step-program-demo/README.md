# Step program demo

Posed 2026-10-14 by the operator: a small demo of the step-program idea for a
vibe-coders meetup the same evening, and a starting point for deciding whether
the idea should be extracted from Commonplace as a standalone Python module.

## The idea

A step program is an ordinary function that is replayed from the top on every
step. Its jobs are memoized, and there are two primitives that differ only in
what happens on a cache miss:

- a computed job is run by the program, and its result is stored;
- an external job waits for someone outside (an agent, a person) to produce
  the result.

The demo's only external job is an answer to a prompt, keyed by the prompt's
text. A `@reported` job composes the two: its body is a computed job that
builds the prompt, and its result is the external answer to that prompt, which
the worker delivers with `fill()`. Consumers depend on the answer, the answer
on the prompt, the prompt on its inputs.

A job called with a missing argument does nothing, and the caller gets the
missing marker. Plain code that reads a missing value ends the replay.

Two kinds of state are stored. The cache holds results: computed values,
prompts and answers; entries are only added.
The prompt directory holds issued prompts, handed out and not yet answered.
That is operational state, and it can be wrong (a worker died), so `release`
takes a prompt back. Everything else, including what is ready and what comes
next, is recomputed by every replay.

The cache is [cachier](https://github.com/python-cachier/cachier), a disk
memoization library. A computed job is a plain cachier function. The external
answer is one cachier function keyed by the hash of the prompt text; on a miss
it raises, so cachier stores nothing, and `fill()` stores the answer with
cachier's `precache_value`. What `stepprog.py` adds is the missing marker, the
external answer and the prompt files.

A prompt file holds exactly the prompt text and is named by its hash, shown by
the first six characters; `fill()` accepts any prefix that matches one issued
prompt, as git does with commit hashes. Because the answer is keyed by the
text the worker saw, it stays correct for that text even if the program has
since stopped asking it.

The contract: computed jobs must be idempotent, because replay may run them
again; answers must be cached, because they are expensive and
nondeterministic; and a job's cache key must cover everything it reads.
cachier's key covers only the arguments, so computed jobs (prompt builders
included) use a `hash_func` that also hashes the job's source. Answers need no
such help: their key is the prompt itself. An edit that leaves the prompt text
unchanged, such as a comment in a prompt builder, rebuilds the prompt but keeps
the answer.

## Running the toy

From this directory:

```
uv run --no-project --with cachier python3 toy.py step [--max-open N]   # replay; prints new prompts
uv run --no-project --with cachier python3 toy.py fill ID FILE          # store an answer
uv run --no-project --with cachier python3 toy.py release ID            # take back an unanswered prompt
```

The toy drafts a paragraph per topic for three topics, reviews each draft and
assembles them. Without a limit, step 1 issues all three drafts; after they
are filled, the next step runs `word_count` and issues the three reviews; the
step after that assembles. Stepping again before answers arrive issues
nothing new. With `--max-open 2`, two drafts go out and the third waits for a
free slot; with `--max-open 1` the run takes seven steps, one prompt at a
time. Editing the `review` wording withdraws issued reviews and re-asks them;
restoring the old wording brings the old answers back, and a comment-only edit
to `draft` re-asks nothing. State lives in `.run/` (ignored); delete it to
start over.

## Using it as a workflow mechanism

This is how Commonplace runs its analysis workflow, with a step program in
place of the engine. A coordinating agent (a Claude Code or Codex session)
drives the program; workers do the reported jobs; the program decides what
comes next.

1. The coordinator runs `step --max-open N`. Computed jobs run; reported
   jobs whose inputs exist, that have no answer and that are not already
   issued come back as new prompts, until N prompts are issued in total.
2. The coordinator gets each new prompt answered. How is its choice: it can
   answer the prompt itself, give it to a sub-agent, run several sub-agents in
   parallel, or use a script or a person. The program cannot tell the
   difference, so a prompt must be self-contained.
3. Whenever an answer arrives, the coordinator runs `fill ID FILE` and then
   `step --max-open N` again, with the same N. A worker that will not answer
   is released with `release ID`.
4. When `step` returns a result, the workflow is done.

N is the coordinator's capacity, not a count it has to track: 10 for ten
parallel sub-agents, 1 for answering prompts itself one at a time. Prompts are
issued in replay order, so the order is deterministic.

The coordinator carries no workflow state in its own context. The schedule is
the program and the progress is the cache, so a crashed or ended conversation
resumes by running `step` again, possibly from a different agent.

Checks and correction loops are ordinary code. A check is a computed job; a
correction is a reported job whose arguments include the problems found, so
each round has a new key and is asked once:

```python
@computed
def check(text):                      # deterministic validation, rerun only on new text
    return problems_in(text)

@reported
def revise(topic, text, problems):
    return f"Revise this paragraph about {topic} to fix: {problems}\n\n{text}"

def program(topic, max_revisions=2):
    text = draft(topic)
    for _ in range(max_revisions):
        problems = check(text)
        if problems == []:            # a plain read: ends the replay until text exists
            return text
        text = revise(topic, text, problems)
    ...                               # out of revisions: report failure
```

The attempt limit is the loop bound; the verdict a check gave is pinned to the
text it judged, because the text is in its key. A plain read such as
`problems == []` ends the replay, so prompts that would come after it in the
program wait for a later step; put independent jobs before such reads.

Compared with the engine, the plan becomes the program, `advance` becomes
`step`, closing an attempt becomes `fill`, hand-outs become prompt files, and
judgments pinned to input versions become cache keys over the inputs. Issued
prompts play the part of open attempts. Not covered yet: a worker reporting
failure or refusal, recording which worker and model produced an answer, and
locking for a `step` and a `fill` running at the same time.

## Task systems and build systems

A discussion starter rather than a settled position.

With `--max-open` and `release` the issued set is a small task queue: `step`
hands tasks out, `fill` completes them, `release` takes them back. The
difference from a task system is where tasks come from. In a task system the
tasks are the record: someone creates them, and they last until someone
closes or cancels them. Here every replay derives them from the program and
the cache, and the issued set records only which of them were handed out. A
task whose job changed is withdrawn without anyone managing a backlog.

Most task systems for agents (and make, Airflow, issue trackers) schedule by
declared dependencies: the graph exists first, and ready work is whatever has
its dependencies done. A step program declares no graph. Dependencies follow
from data flow, since a job depends on whatever produced its arguments, and
the program reveals the graph one layer at a time; the current misses are the
frontier.

Build-systems theory names this split. Mokhov, Mitchell and Peyton Jones,
"Build Systems à la Carte" (ICFP 2018), separate applicative build systems,
which know all dependencies before building (make), from monadic ones, which
discover dependencies during the build, so a later dependency can depend on an
earlier result (Shake, Excel). Monadic systems are strictly more expressive: a
static graph is a monadic build whose shape does not depend on any result. In
their terms a step program is monadic, rebuilds from constructive traces
(results cached under keys over code and inputs, as Bazel does), and uses a
restarting scheduler (abort at a blocking read, replay from the top later).

What the step program expresses without extensions:

- fan-out decided by an answer (an outline, then one section job per item);
- conditional work (revise only if the check failed);
- loops that run until a condition holds, with a bound;
- tasks identified by content (`review(text)` is a new task when `text`
  changes, so stale work cancels itself);
- plans made by agents: a reported `plan(goal)` returns a list, and the
  program iterates over it. The code says how a plan is used, not what it
  contains.

A declared-dependency system handles these with extensions (Airflow's dynamic
task mapping) or by letting workers create tasks while they work, as beads
does. That is flexible, but the logic that creates tasks then lives outside
any program that can be replayed or checked.

What the step program gives up:

- no view of the whole plan before running: no full graph, critical path or
  cost estimate;
- less parallelism found: a restarting scheduler stops at the first blocking
  read, so independent work after it waits for a later step (Shake avoids
  this with a suspending scheduler, at the price of complexity);
- changing the plan means changing code, or reading plans from a reported job;
  a person cannot just add or reorder a task;
- control flow must be deterministic given cached results, or replays diverge.

The generality is not new; it is the monadic build system. What seems new is
the application: agent coordination in which some jobs are reported and the
agent is the executor.

Questions for discussion:

- Are agent task trackers reinventing make, when the work they coordinate is
  dynamic?
- Who should be able to change the plan mid-run: anyone with tracker access,
  or only the program (and agents through reported planning jobs)?
- Is a suspending scheduler worth its complexity for agent workflows, where
  each job takes minutes and the cost of a lost step is a slower run?
- Which coordination state may be lost? Here only results must survive;
  Beads Lite takes the same line for its coordination database.

## Candidate design: a step program plus a job queue

Posed 2026-10-14, undecided: package the step program with Beads Lite, which
becomes a job queue complementary to it. The step program decides what is
needed (the schedule, derived by replay, and the results, in the cache); the
queue decides who does it and when (claims, leases, worker identity and the
record of handoffs). Bazel with remote execution splits the work the same way.

The contract between them:

| Operation | Called by | Meaning |
|---|---|---|
| `post(key, prompt, producer)` | step | offer a job; idempotent by key |
| `withdraw(key, producer)` | step | the job is no longer needed; only its producer withdraws it |
| `claim(worker)` | worker | take the next open job, with a lease |
| `complete(key, answer, worker, model)` | worker | deliver the answer and record who produced it |
| `release(key)` or lease expiry | worker or timeout | put the job back |
| `completed()` | step | answers waiting to be collected into the cache |

`step` becomes a reconciliation: post new misses, withdraw stale jobs, collect
completed answers. `fill` disappears into `complete`, and `--max-open` into
the number of workers pulling. The queue has no dependencies, since
scheduling belongs to producers. Claims and leases are ephemeral; completion
records are provenance and worth keeping, which revises Beads Lite's choice to
make all coordination forgettable.

Every job comes from a program. Authored work goes through a standard inbox
program that posts one reported job per file in `inbox/`: adding a file posts
a job, editing it withdraws the old job and posts the new one, deleting it
withdraws the job. Ordering between authored jobs is where a small program
becomes worth writing. So that a new inbox file needs no manual `step`, the
queue reconciles on `claim`.

Beads Lite's motivating relay (implement, verify, paste findings back, repair)
is then a step program with reported `verify` and `repair` jobs; the queue
holds the claims and the history of who did each round.

How to characterise it. The build system is the core and the queue is how its
jobs are handed out, so "beads-like" works only as a qualifier: unlike Beads,
the queue holds no written tasks and no dependency links.

- General: a monadic build system whose actions are done by agents, with a
  beads-style queue for handing them out.
- For build-system people: Shake for agent work; reported actions are claimed
  from a queue instead of run locally.
- For coders who do not know the build-system terms: a task tracker where
  tasks are computed, not written; a program decides what work is needed, and
  agents pull it from a queue.
- For Beads users: Beads without dependencies; the dependencies live in a
  program that is replayed, so the queue holds only what is ready now.

Open: whether the package keeps cachier or stores results in the queue's
SQLite database, which would remove cachier's three dependencies; how much of
Beads Lite's current 4,700 lines survives once dependencies and authored task
fields go.

## Relation to Commonplace

The current engine (`src/commonplace/artifactrun/`, ADR 113) is not a replayed
program: a plan declares jobs and their inputs, and `advance` decides readiness
from pinned input versions. Its rule for a job whose producer is pending
matches the "does nothing" case here. Durable-execution libraries (DBOS,
Inngest) were checked and key steps by position, not content; memoization
libraries key by content but have no external kind, which is why the demo
extends one. Luigi has both primitives (`Task` and `ExternalTask`, the latter
waiting for an output to exist); the same split of a reported job into a
computed prompt and an external answer would fit it without failing a task
on purpose.

## Relation to Colvin's "The code IS the graph"

Samuel Colvin ([ingest](../../sources/the-code-is-the-graph-2110055467007303729.ingest.md))
argues from building and partly removing pydantic-graph that ordinary control
flow is the orchestration graph, and that a graph API gives only two of type
safety, parallel nodes and resumable snapshots, because parallel writers to a
shared state object need merge rules no type checker can verify. The step
program takes his side: the workflow is a program, jobs pass values and share
no mutable state, so a join is the line of code after the calls. Its split
between computed and external jobs is his effect-boundary declaration, with
idempotency as the retry contract.

His two durability routes are Temporal replay, which keys recorded results by
position and needs the code to stay deterministic and stable, and Monty
snapshots of a resource-free interpreter at host-call barriers. A step program
is a third route: replay against results keyed by content. An edited job
misses, an unedited one hits, and restoring an edit brings its old answers
back, so the code need not stay stable. That fits his Pydantic AI Harness
pattern, where a model rewrites the orchestration script every turn: a
rewritten step program reuses every answer whose prompt did not change, so
the script is disposable and its results are not.

Monty snapshots when every in-flight branch waits on a host call, which is a
suspending scheduler; a step program written with `async` and `gather` could
do the same and lift the restarting scheduler's limit at blocking reads.

## Known gaps

Results must be picklable and prompts strings; job modules are named `__main__` in cachier's cache
when run as a script; undeclared reads (files, globals) make the cache unsound
and are not detected; `str.join` over a missing value raises `TypeError`, not
`Suspend`; no failure or retry limits for answers; no locking; an issued prompt
whose worker died stays issued until someone runs `release`.

## Closes when

The operator decides whether to extract the idea as a module. The decision and
its reasons go to an ADR or proposal; this directory is then deleted.
