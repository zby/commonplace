# Thread 1 — vocabulary decision

**STATUS: ACCEPTED 2026-05-30, with one revision.** Q1 and Q3 approved as written. **Q2 revised:** direction-axis values are **push / pull** (mechanism-neutral, names who initiates), *not* retrieval/activation — using "activation" as an axis value would collide with the `contextual activation` theory term, and "pull" already maps to the retrieval/access problem. Everything below that says "retrieval/activation" for the *direction values* should read "push/pull"; the umbrella ("read-back") and the Q1/Q3 decisions are unchanged. Durable record in the workshop README's Graduated changes. This file is the rationale trail and is discarded with the workshop.

Three questions to settle before any durable text is written. Recommendations are marked **REC**; react inline.

## The reframing that simplifies everything

The write side of the review type is **not** a declared global vocabulary term. CLAUDE.md's vocabulary block lists distillation, constraining, behavioral authority, frontloading, etc. — but **"trace-derived learning" is nowhere in it.** It is just the *name of a section* in `agent-memory-system-review.md` ("Trace-derived learning placement").

By symmetry, the read side does not need a global vocabulary term either. It needs a **section name** in the type spec. This matches the c1/c2 conclusion that this is review methodology, not theory — the label lives in the review contract, not in the global vocabulary.

**REC for Q1:** Do not declare a new CLAUDE.md vocabulary term. Name a section, parallel to "Trace-derived learning placement." This also means we are not coordinating with `vocabulary-governance` on a global-term declaration — the dependency in the README drops.

## Q2 — "read-back" is used two ways; fix it

The seed note uses *read-back* both as the umbrella (the whole path from stored memory back into an action) and as one pole of its own direction axis (*read-back-when-relevant* = push, vs pull retrieval). A term cannot be both the whole and one of its parts.

The cheapest fix is to **stop coining "read-back-when-relevant" for the pole** and name the two directions with terms we already have:

| | pull | push |
|---|---|---|
| **proposed name** | **retrieval** | **activation** |
| trigger | agent/user poses a query | system surfaces against the current action, unprompted |
| benchmark-visible? | yes (retrieval benchmarks) | no — this is the untested half |

So: **read-back = the umbrella** (the consumption path from stored memory to action); the **direction axis** has values **retrieval (pull)** and **activation (push)**. "Read-back-when-relevant" disappears as a coined term; it was just "activation."

**REC for Q2:** Keep "read-back" as the umbrella/section name only. Direction-axis values are *retrieval* and *activation*. Drop "read-back-when-relevant."

Alternative umbrella names considered, if "read-back" feels off:

- **Consumption path** — harmonizes with the artifact-analysis vocabulary (`behavioral authority` is already defined as "force at *consumption*"; "who *consumes* the artifact"). Most precise, slightly clunkier as a section title.
- **Activation placement** — rejected: "activation" is the push pole, so using it for the umbrella re-creates the exact whole/pole collision we are fixing, and it would wrongly exclude the pull/retrieval path.

**REC:** "Read-back" as umbrella; "consumption path" as the fallback if you prefer harmonizing with existing artifact-analysis language over the read/write parallel.

## Q3 — relationship to the existing `contextual activation` term

`knowledge-storage-does-not-imply-contextual-activation` defines **contextual activation** as the context→action transition: "the fact changes what the agent notices, says, checks, or does *without the user naming it directly*." That "without being named" clause makes contextual activation essentially the **push/activation pole's success condition** — not the whole read-back path.

So the two are not competitors and neither should be redefined:

- **contextual activation** (existing theory term) = the success condition of the *activation* direction — knowledge reaching behavior unprompted.
- **read-back placement** (new section) = the methodology for *describing the machinery* a system uses across the whole path: the pull/retrieval route it offers, the push/activation route it offers (if any), and the axes (trigger, direction, timing, scope, authority-at-consumption, faithfulness) that determine whether contextual activation is actually achieved.

In one line: **read-back placement describes how a system attempts contextual activation (and what pull-retrieval it offers); contextual activation is the property that attempt is trying to produce.**

**REC for Q3:** Leave `contextual activation` untouched as the theory term. The read-back section *cites* it as the success condition for the activation direction. No redefinition, no merge.

## Net effect on the workshop plan

- Q1 → no global term; the README's "coordinate with vocabulary-governance" item drops.
- Q2 → section/umbrella = **read-back** (fallback: consumption path); directions = **retrieval** / **activation**; "read-back-when-relevant" retired.
- Q3 → `contextual activation` stays; read-back placement cites it.

If you accept these, the axis list in thread 2 gets one rename: the seed note's "Direction: push or pull" axis becomes **"Direction: retrieval or activation,"** and any prose that said "read-back-when-relevant" says "activation."

## React here

- Q1 — section name, not a global term? **(REC: yes)**
- Q2 — umbrella term: **read-back** / consumption path / other?
- Q3 — keep `contextual activation` as-is and cite it? **(REC: yes)**
