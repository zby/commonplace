"""Toy step program: draft a section per topic, review each draft, assemble.

    uv run --no-project --with cachier python toy.py step            # replay; prints the open prompts
    uv run --no-project --with cachier python toy.py fill ID FILE    # store an answer, then step again
"""

import sys
from pathlib import Path

from stepprog import MISSING, computed, fill, reported, short, step

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


TOPICS = ["memoized replay", "agents as executors"]

if __name__ == "__main__":
    if sys.argv[1] == "fill":
        fill(sys.argv[2], Path(sys.argv[3]).read_text())
    result, prompts = step(program, TOPICS)
    for path in prompts:
        print("open prompt:", short(path.stem), "->", path.read_text().splitlines()[0])
    print("DONE\n" + result if result is not MISSING else f"{len(prompts)} prompt(s) open")
