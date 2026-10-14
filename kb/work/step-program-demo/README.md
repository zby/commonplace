# Step program demo

Posed 2026-10-14 by the operator: a small demo of the step-program idea for a
vibe-coders meetup the same evening, and a starting point for deciding whether
the idea should be extracted from Commonplace as a standalone Python module.

## The idea

A step program is an ordinary function that is replayed from the top on every
step. Its jobs are memoized, and they come in two kinds that differ only in
what happens on a cache miss:

- a `@computed` job is run, and its result is stored;
- a `@reported` job is reported: its body builds a prompt, the prompt is
  handed to an outside worker (an agent), and the worker's answer is stored
  later with `fill()`.

A job called with a missing argument does nothing, and the caller gets the
missing marker. Plain code that reads a missing value ends the replay. The only
state is the cache and the open prompts.

The cache is [cachier](https://github.com/python-cachier/cachier), a disk
memoization library. A computed job is a plain cachier function. A reported job
is a cachier function whose body writes the prompt and raises, so cachier
stores nothing; `fill()` stores the answer with cachier's `precache_value`.
What `stepprog.py` adds is the missing marker, the reported kind and the prompt
files. A prompt is named by cachier's key for the job call and shown by its first six
characters; `fill()` accepts any prefix that matches one open prompt, as git
does with commit hashes. It recomputes
that key and refuses an answer to a prompt whose job has changed since.

The contract: computed jobs must be idempotent, because replay may run them
again; reported jobs must be cached, because they are expensive and
nondeterministic; and a job's cache key must cover everything it reads. cachier's
key covers only the arguments. The demo passes a `hash_func` that also hashes
the job's source, so changing a job's code or inputs makes it miss again.

`stepprog.py` documents each case in `computed` and `reported`.

## Running the toy

From this directory:

```
uv run --no-project --with cachier python3 toy.py step           # replay; prints the open prompts
uv run --no-project --with cachier python3 toy.py fill ID FILE   # store an answer, then replay again
```

The toy drafts a paragraph per topic, reviews each draft and assembles them.
Step 1 hands out both drafts together; step 2 runs `word_count` on the filled
drafts and hands out both reviews; step 3 assembles. Editing the `review`
prompt re-asks only the reviews. State lives in `.run/` (ignored); delete it to
start over.

## Using it as a workflow mechanism

This is how Commonplace runs its analysis workflow, with a step program in
place of the engine. A coordinating agent (a Claude Code or Codex session)
drives the program; workers do the reported jobs; the program decides what
comes next.

1. The coordinator runs `step`. Computed jobs run; every reported job whose
   inputs exist and that has no answer yet comes back as an open prompt.
2. For each open prompt the coordinator launches a fresh worker (a sub-agent)
   and gives it only the prompt file. Independent prompts come out in the same
   step, so their workers can run in parallel. The worker writes its answer to
   a file.
3. The coordinator runs `fill ID FILE` for each answer, then `step` again.
4. When `step` returns a result and no prompts, the workflow is done.

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
judgments pinned to input versions become cache keys over the inputs. Not
covered yet: a worker reporting failure or refusal, recording which worker and
model produced an answer, and locking for concurrent fills.

## Relation to Commonplace

The current engine (`src/commonplace/artifactrun/`, ADR 113) is not a replayed
program: a plan declares jobs and their inputs, and `advance` decides readiness
from pinned input versions. Its rule for a job whose producer is pending
matches the "does nothing" case here. Durable-execution libraries (DBOS,
Inngest) were checked and key steps by position, not content; memoization
libraries key by content but have no reported kind, which is why the demo
extends one.

## Known gaps

Results must be picklable and reported-job arguments JSON (the prompt file
records them for `fill()`); job modules are named `__main__` in cachier's cache
when run as a script; undeclared reads (files, globals) make the cache unsound
and are not detected; `str.join` over a missing value raises `TypeError`, not
`Suspend`; no failure or retry limits for reported jobs; no locking.

## Closes when

The operator decides whether to extract the idea as a module. The decision and
its reasons go to an ADR or proposal; this directory is then deleted.
