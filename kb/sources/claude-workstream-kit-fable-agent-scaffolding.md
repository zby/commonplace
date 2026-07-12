---
source: https://x.com/ChristopherA/status/2065234780497883259
captured: 2026-06-12T12:17:46.079283+00:00
capture: xdk
genre: tool-announcement
type: kb/sources/types/snapshot.md
status_id: 2065234780497883259
conversation_id: 2065234780497883259
post_count: 1
---

# Claude Fable 5 Made Most of My Agent Scaffolding Obsolete. Here's What Survived.

Author: @ChristopherA
Post: https://x.com/ChristopherA/status/2065234780497883259
Created: 2026-06-12T00:48:36.000Z

Fable follows short, principle-level instructions so reliably that the elaborate scaffolding I'd built to keep earlier models on track — checklists, compliance scripts, sync layers — became dead weight almost overnight. But one problem got more acute with stronger autonomy, not less: sessions still forget.
Every Claude Code session ends mortal. Clear the context, hit auto-compaction, close the laptop, switch machines — and everything the session knew about your project's goals, decisions, and loose ends is gone. So today I'm releasing claude-workstream-kit, a small open-source system that gives any Claude Code project durable, git-versioned work tracking, designed Fable-first. It's what survived when I rebuilt a much larger private system for the new model — and the throwing away turned out to be the interesting part.
The reconstruction tax
AI coding sessions are ephemeral by design. The work isn't. A feature lands across a week of sessions. A migration takes a dozen. A research question evolves for a month.
When the work's state lives only in conversation history, every new session pays what I've come to call the reconstruction tax: re-explaining the goal, re-discovering what was decided and why. The visible cost is time and tokens. The quieter cost is drift — a decision made carefully in session three gets remade differently in session nine, because nothing recorded the original reasoning.
Everyone who uses these tools seriously has felt this. The common workarounds each cover a slice:
A growing CLAUDE.md survives sessions — but it's loaded into every future session forever, and nothing in it ever closes. It becomes a junk drawer.
The harness's built-in task tracking and plan mode are good within a session, but their state isn't in your repository and doesn't travel.
Agent memory is for lessons and preferences — account-side, per-fact. It's not a ledger of a project's work.
GitHub Issues and PRs are the right answer for teams — but their state lives service-side, needs network and auth, and fits code delivery, not exploration.
A SPEC.md in the repo survives and travels — but has no resume pointer, no record of decided-versus-open, no definition of done.
What none of these provide: work state that is project-scoped, git-versioned, and portable — surviving everything the harness can do, and traveling with the repo like tests or docs.
Workstreams: two files in git
The kit's answer is deliberately small. A workstream is a unit of multi-session work tracked in two markdown files committed to your repo:
workstream.md — everything durable about one piece of work: purpose, a checkbox backlog, decisions with their reasoning, lessons learned, and — this part matters — falsifiable deletion criteria written at creation: the conditions under which this work is done and can be archived.
ACTIVE.md — a per-project pointer: what's active, the current task, the single next action, what's blocked.
Git does the heavy lifting. Clone the repo and the entire work state moves with it. The commit history is the progress journal. And because the files are flat frontmatter plus checkboxes, a shell one-liner — or a cheap small model — can read project status without any parsing machinery. That last property is what makes delegation and autonomous verification practical.
Around the two files:
four short lifecycle skills (create, work, close, handoff),
three pinned subagents (a read-only Haiku scout, a Sonnet worker that takes bounded packets, a fresh-context verifier),
a session-start hook that surfaces your state and flags staleness,
and an idempotent installer.
Zero dependency on user-level configuration. Copy it into a project and it works.
What building it taught me
Two findings reshaped the design when I rebuilt for Fable.
Strong models need less scaffolding, not more. My predecessor system had multi-phase checklists, compliance scripts that verified the model actually did the steps, sync layers to propagate rule updates. Most of that mass existed to manage the model, not the work. Fable-class models invert those economics: they follow principle-level instructions reliably — and over-prescription actively degrades their output. Every skill in this kit is about a hundred lines. The compliance machinery is replaced by one rule: a checkbox closes only with cited evidence — a commit hash, a command's output — that a human can check at the gate.
This was validated directly, and here's the part I find genuinely remarkable: the kit was designed, built, and tested largely by an autonomous Fable session operating under the very conventions the kit ships. In the acceptance tests, fully autonomous sessions ran the entire lifecycle and honored every human-authority constraint — no auto-starting work, no auto-passing checkpoints, no self-certifying its own closure — from the skill text alone. No enforcement code.
Work should end well. Most tracking handles starting and doing; almost nothing handles ending. Unclosed work is where knowledge dies. So closure is a first-class phase here: per-criterion evidence presented to a human who decides, lessons that must reach a named destination outside the workstream before archive, and an archive that's a git tag plus one index line — recoverable, searchable, and no longer taking up space in anyone's context window.
Try it
The kit is small on purpose, and it commits to staying that way: no sync layer, no rule tiers, no machinery duplicating what the platform already does. Everything in it had to clear one bar — does this produce an artifact or a human decision that nothing native already produces?
git clone https://github.com/ChristopherA/claude-workstream-kit ./claude-workstream-kit/install.sh /path/to/your/project
BSD-2-Clause-Patent licensed. The full design rationale — including what each alternative is genuinely good at — is in the repo's docs. If you run multi-session work through Claude Code, I'd like to hear what survives your compactions.
