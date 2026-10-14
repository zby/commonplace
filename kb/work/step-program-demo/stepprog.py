"""Step programs: memoized replay with two kinds of job, on top of cachier.

A step program is an ordinary function. Every `step()` replays it from the top.
cachier (https://github.com/python-cachier/cachier) is the disk cache.

- `@computed` job: on a cache miss, run it and store the result.
  Must be idempotent: replay may call it again.
- `@reported` job: its body only builds a prompt. On a cache miss, write the
  prompt for an outside worker (an agent); the caller gets MISSING. `fill()`
  stores the worker's answer in cachier under the same arguments.

A job called with a MISSING argument does nothing; the caller gets MISSING.
Plain code that reads a MISSING value raises Suspend, which ends the replay.
The only state is the cachier cache and the open prompts.
"""

import functools
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


class Reported(Exception):
    """Raised inside cachier on a reported miss, so cachier stores nothing."""


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
    so editing a job makes it miss again."""
    source = inspect.getsource(func)

    def hash_func(args, kwds):
        material = json.dumps([source, list(args), kwds], sort_keys=True, default=repr)
        return hashlib.sha256(material.encode()).hexdigest()

    return hash_func


def _cached(func, body, hash_func):
    if body is not func:
        body = functools.wraps(func)(body)  # cachier names the cache and reads the signature from func
    return cachier(cache_dir=CACHE, hash_func=hash_func)(body)


def _cachier_key(func, hash_func, args, kwargs):
    """The key cachier computes for this call: it passes every argument as a
    keyword, with defaults filled in, to `hash_func`."""
    bound = inspect.signature(func).bind(*args, **kwargs)
    bound.apply_defaults()
    return hash_func((), dict(bound.arguments))


def computed(func):
    """A job the program can do itself: cheap, or at least runnable here.

    The body is the work. It must be idempotent, because a later replay may
    run it again (for example after its code changed).
    """
    cached = _cached(func, func, _hash_with_source(func))

    def call(*args, **kwargs):
        # Case 1, an argument is missing: an upstream reported job has no
        # answer yet. Do nothing; no record, no run. The caller gets MISSING.
        if _has_missing((args, kwargs)):
            return MISSING
        # Case 2, cache hit: cachier returns the stored result without running the body.
        # Case 3, cache miss: cachier runs the body, stores the result and
        # returns it. The replay continues with a real value.
        return cached(*args, **kwargs)

    return call


_reported_jobs = {}


def reported(func):
    """A job the program cannot do itself: an agent or a person does it.

    The body does not do the work; it only builds the prompt that describes
    it. The answer arrives later through `fill()`. It must be cached, because
    it is expensive and asking twice could give a different answer.
    """
    hash_func = _hash_with_source(func)

    def on_miss(*args, **kwargs):
        # Case 3, cache miss: report it. The prompt is named by cachier's own
        # key for this call. The arguments are saved beside it because
        # `fill()` can store a value in cachier only through them
        # (`precache_value`). Then raise, so cachier stores nothing.
        key = _cachier_key(func, hash_func, args, kwargs)
        call_args = inspect.signature(func).bind(*args, **kwargs).arguments
        (PROMPTS / f"{key}.md").write_text(f"<!-- job: {func.__qualname__} -->\n{func(*args, **kwargs)}\n")
        (PROMPTS / f"{key}.json").write_text(json.dumps({"job": func.__qualname__, "args": call_args}))
        raise Reported

    cached = _cached(func, on_miss, hash_func)
    _reported_jobs[func.__qualname__] = (func, cached, hash_func)

    def call(*args, **kwargs):
        # Case 1, an argument is missing: the prompt cannot be built yet.
        # Do nothing; no prompt, no record. The caller gets MISSING.
        if _has_missing((args, kwargs)):
            return MISSING
        try:
            # Case 2, cache hit: an answer was filled earlier. cachier returns
            # it; the agent is not asked again.
            return cached(*args, **kwargs)
        except Reported:
            # Case 3 continued: the caller gets MISSING and the replay goes on,
            # so other independent prompts are reported in the same step.
            return MISSING

    return call


SHORT = 6


def short(key):
    """The prefix shown to agents. Files and cachier keep the full key, so a
    shared prefix can only make `fill()` ask for more characters."""
    return key[:SHORT]


def step(program, *args, **kwargs):
    """Replay the program once. Returns (result or MISSING, open prompt paths)."""
    PROMPTS.mkdir(parents=True, exist_ok=True)
    for stale in PROMPTS.iterdir():
        stale.unlink()  # prompts are recomputed by every replay
    try:
        result = program(*args, **kwargs)
    except Suspend:
        result = MISSING
    return result, sorted(PROMPTS.glob("*.md"))


def fill(key, answer):
    """Store an outside worker's answer for an open prompt.

    `key` is the prompt's name, which is cachier's key for the job call, or
    any prefix of it that matches one open prompt, as with git hashes. If
    the job's code changed since the prompt was written, the key no longer
    matches and the answer is refused: it answers a prompt nobody asks now.
    """
    matches = sorted(PROMPTS.glob(f"{key}*.json"))
    if len(matches) != 1:
        raise ValueError(f"{len(matches)} open prompts match {key!r}; give more characters")
    key = matches[0].stem
    meta = json.loads(matches[0].read_text())
    func, cached, hash_func = _reported_jobs[meta["job"]]
    if _cachier_key(func, hash_func, (), meta["args"]) != key:
        raise ValueError(f"{meta['job']} changed since prompt {key} was written; step again")
    cached.precache_value(**meta["args"], value_to_cache=answer)
