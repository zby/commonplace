"""Toy step program: draft a section per topic, review each draft, assemble.

    uv run --no-project --with cachier python toy.py step [--max-open N]   # replay; prints new prompts
    uv run --no-project --with cachier python toy.py fill ID FILE          # store an answer
    uv run --no-project --with cachier python toy.py release ID            # take back an unanswered prompt
"""

import sys
from pathlib import Path

from stepprog import MISSING, computed, fill, job_of, release, reported, short, step

@reported
def draft(topic):
    return f"Write one paragraph about {topic} for a meetup of vibe coders."


@reported
def review(topic, text):
    return f"Review this paragraph about {topic}. Reply with the corrected paragraph.\n\n{text}"


@computed
def word_count(text):
    return len(text.split())


@computed
def assemble(sections):
    return "\n\n".join(f"## {topic}\n\n{text}" for topic, text in sections)


def program(topics):
    drafts = {t: draft(t) for t in topics}                # all handed out in step 1
    reviewed = {t: review(t, drafts[t]) for t in topics}  # does nothing until its draft exists
    counts = {t: word_count(drafts[t]) for t in topics}   # runs as soon as a draft is filled
    print("word counts:", counts)
    return assemble([(t, reviewed[t]) for t in topics])


TOPICS = ["memoized replay", "agents as executors", "prompt IDs"]

if __name__ == "__main__":
    command, rest = sys.argv[1], sys.argv[2:]
    if command == "fill":
        fill(rest[0], Path(rest[1]).read_text())
    elif command == "release":
        release(rest[0])
    elif command == "step":
        max_open = int(rest[1]) if rest[:1] == ["--max-open"] else None
        result, new, issued = step(program, TOPICS, max_open=max_open)
        for path in new:
            print("new prompt:", short(path.stem), "->", job_of(path))
        print("DONE\n" + result if result is not MISSING else f"{issued} prompt(s) issued, {len(new)} new")
