---
type: types/note.md
description: "Turn a hunch into a note with your agent, connect it to what you already know, and revise it after reading sources you choose."
brief: getting-started.brief.md
tags: []
---

# Getting started with Commonplace

## How do I turn a rough thought into a note?

You don’t need a finished argument to ask your agent to write. Start with something you’ve noticed. Here’s one way the conversation might go.

**Ask for a first note.** “I have a hunch that when a job fails, retrying it sometimes hides the problem. Help me turn that into a short note for the team. Ask me for an example if that would help.” Read the note for your idea: is the worry that retries *cause* failures, or that a successful retry makes an earlier failure easy to miss? Correct the agent if it picked the wrong one.

**Connect it to what you already know.** “Do we already have notes about retries or failures that went unnoticed? Link the relevant ones from this note and tell me whether they support my hunch or describe something different.” A note about why a retry succeeds might help explain recovery without telling you whether anyone noticed the failure.

**Ask what would be worth reading.** “What sources would help us find out when retries hide failures and when they don’t? Suggest a few and tell me what each could settle. Don’t add them yet.” You might choose an incident report for what happened in practice and a guide for what should have been logged.

**Bring your choices into the KB, then revisit the note.** Once you’ve picked the sources, ask: “Ingest these two sources so we have a record of each. Then revise the note using what they actually say. Show me what changed and what’s still a hunch.” The result needn’t be a stronger claim. If a report shows that the job recovered but says nothing about what the team saw, it supports recovery, not a hidden failure.

## Other starting points

**How do I keep a decision we just made?** If you want a new note, ask: “Write down why we chose to retry only temporary failures. Link me to what you wrote.” Read it for the reason behind the choice. If you want to see a draft before anything is saved, say so.

**How do I make sense of a difficult note?** Ask: “Explain this note using an example from our project. Which part is the note’s claim, and which part is your illustration?” You can ask for a clearer explanation without asking the agent to rewrite the note.
