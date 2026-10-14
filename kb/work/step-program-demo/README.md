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
