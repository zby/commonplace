"""Step programs: memoized replay over two primitives, on top of cachier.

A step program is an ordinary function. Every `step()` replays it from the top.
cachier (https://github.com/python-cachier/cachier) is the disk cache.

Two primitives, which differ only in what happens on a cache miss:

- computed: the program runs the job and stores the result. Must be
  idempotent, because replay may run it again.
- external: the program waits for someone outside (an agent, a person) to
  produce the result. Here the only external job is an answer to a prompt,
  keyed by the prompt's text.

`@reported` composes them: a computed job builds the prompt, and an external
answer to that prompt is the job's result. Consumers depend on the answer, the
answer on the prompt, the prompt on its inputs. An answer is pinned to the
exact text the worker saw: change an input or the prompt wording and the
prompt changes, so the old answer no longer applies.

A job called with a MISSING argument does nothing; the caller gets MISSING.
Plain code that reads a MISSING value raises Suspend, which ends the replay.

Two kinds of state are stored. The cachier cache holds results (computed
values, prompts, answers); they are only added, never edited. The prompt
directory holds issued prompts: handed out and not yet answered. That is
operational state; it can be wrong (a worker died), so `release()` takes a
prompt back.
"""

import hashlib
import inspect
import json
from pathlib import Path

from cachier import cachier

ROOT = Path(".run")
CACHE = ROOT / "cache"
PROMPTS = ROOT / "prompts"


class Suspend(Exception):
    """Plain code needed a value that is not available yet."""


class Unanswered(Exception):
    """Raised inside cachier when an answer does not exist, so cachier stores nothing."""


class _Missing:
    def _suspend(self, *args, **kwargs):
        raise Suspend("a value this code reads is not available yet")

    __str__ = __bool__ = __iter__ = __len__ = __getitem__ = _suspend
    __eq__ = __add__ = __radd__ = __format__ = _suspend
    __hash__ = object.__hash__

    def __getattr__(self, name):
        self._suspend()

    def __repr__(self):
        return "MISSING"


MISSING = _Missing()


def _has_missing(value):
    if value is MISSING:
        return True
    if isinstance(value, (list, tuple)):
        return any(_has_missing(v) for v in value)
    if isinstance(value, dict):
        return any(_has_missing(v) for v in value.values())
    return False


def _hash_with_source(func):
    """cachier's key covers the arguments only; add the job's source code,
    so editing a computed job makes it miss again."""
    source = inspect.getsource(func)

    def hash_func(args, kwds):
        material = json.dumps([source, list(args), kwds], sort_keys=True, default=repr)
        return hashlib.sha256(material.encode()).hexdigest()

    return hash_func


def computed(func):
    """A job the program does itself.

    The body is the work. It must be idempotent, because a later replay may
    run it again (for example after its code changed).
    """
    cached = cachier(cache_dir=CACHE, hash_func=_hash_with_source(func))(func)

    def call(*args, **kwargs):
        # An argument is missing: an upstream answer does not exist yet.
        # Do nothing; no record, no run. The caller gets MISSING.
        if _has_missing((args, kwargs)):
            return MISSING
        # Cache hit: cachier returns the stored result without running the body.
        # Cache miss: cachier runs the body, stores the result and returns it.
        return cached(*args, **kwargs)

    return call


def prompt_key(prompt):
    """An answer's key: the hash of the exact prompt text."""
    return hashlib.sha256(prompt.encode()).hexdigest()


@cachier(cache_dir=CACHE, hash_func=lambda args, kwds: prompt_key(kwds["prompt"]))
def _answer(prompt):
    # The external primitive. The program cannot produce an answer, so a miss
    # stores nothing; `fill()` stores the answer under the prompt's key.
    raise Unanswered


_misses = {}  # prompt key -> (job, prompt), in replay order; collected by one step


def reported(func):
    """A job someone outside does: a computed prompt plus an external answer.

    The body builds the prompt; it is a computed job like any other. The job's
    result is the answer to that prompt, which arrives through `fill()`.
    """
    prompt_job = computed(func)

    def call(*args, **kwargs):
        # The prompt is computed; it is MISSING only if an argument is.
        prompt = prompt_job(*args, **kwargs)
        if prompt is MISSING:
            return MISSING
        try:
            # Answer hit: someone answered this exact prompt. Return the answer.
            return _answer(prompt)
        except Unanswered:
            # Answer miss: record the prompt as wanted. The caller gets MISSING
            # and the replay goes on, so other independent prompts are
            # collected in the same step.
            _misses.setdefault(prompt_key(prompt), (func.__qualname__, prompt))
            return MISSING

    return call


SHORT = 6


def short(key):
    """The prefix shown to agents. Files and cachier keep the full key, so a
    shared prefix can only make `fill()` ask for more characters."""
    return key[:SHORT]


def _issued():
    return {path.stem: path for path in PROMPTS.glob("*.md")}


def _withdraw(key):
    for suffix in (".md", ".job"):
        (PROMPTS / f"{key}{suffix}").unlink(missing_ok=True)


def _match(prefix):
    matches = sorted(PROMPTS.glob(f"{prefix}*.md"))
    if len(matches) != 1:
        raise ValueError(f"{len(matches)} issued prompts match {prefix!r}; "
                         "give more characters, or step again if it was withdrawn")
    return matches[0].stem


def job_of(path):
    """The name of the job that asked an issued prompt, for display."""
    return path.with_suffix(".job").read_text()


def step(program, *args, max_open=None, **kwargs):
    """Replay the program once and issue new prompts.

    Returns (result or MISSING, newly issued prompt paths, number issued in total).

    A wanted prompt that is already issued is not issued again: its worker is
    still on it. An issued prompt that is no longer wanted (an input or the
    wording changed) is withdrawn. New prompts are issued in replay order until
    `max_open` prompts are issued in total; None means no limit. The caller can
    pass the same `max_open` on every step: 10 for ten parallel workers, 1 to
    answer the prompts itself one at a time.
    """
    PROMPTS.mkdir(parents=True, exist_ok=True)
    _misses.clear()
    try:
        result = program(*args, **kwargs)
    except Suspend:
        result = MISSING
    issued = _issued()
    for key in issued.keys() - _misses.keys():
        _withdraw(key)
    issued = _issued()
    new = []
    for key, (job, prompt) in _misses.items():
        if key in issued:
            continue
        if max_open is not None and len(issued) + len(new) >= max_open:
            break
        (PROMPTS / f"{key}.job").write_text(job)
        (PROMPTS / f"{key}.md").write_text(prompt)  # exactly the text the answer is keyed by
        new.append(PROMPTS / f"{key}.md")
    return result, new, len(issued) + len(new)


def release(key):
    """Take back an issued prompt whose worker will not answer (it died or gave
    up). The next step can issue it again."""
    _withdraw(_match(key))


def fill(key, answer):
    """Store an outside worker's answer to an issued prompt.

    `key` is the prompt's key, or any prefix of it that matches one issued
    prompt, as with git hashes. The answer is stored under the prompt's text,
    so it answers exactly what the worker was shown, even if the program has
    since stopped asking it.
    """
    key = _match(key)
    prompt = (PROMPTS / f"{key}.md").read_text()
    _answer.precache_value(prompt=prompt, value_to_cache=answer)
    _withdraw(key)  # answered: no longer issued
