# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/articles/an-automated-software-house-as-an-alternative-test.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/articles/an-automated-software-house-as-an-alternative-test.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Trim this to about 1,900 words, and recast the comparison with the knowledge-base arrangement as a compact side-by-side table readers can scan.

## Retained intent

Source: retained commission for this document. Subject: `kb/articles/an-automated-software-house-as-an-alternative-test.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: software-house supplement

## Governing question

How does the earlier automated software house conjecture fit the theory-refinement research program as an alternative test, and what does it offer and cost compared with the knowledge-base arrangement pursued first?

## Audience and reader update

External technical readers arriving from the lead article, with no KB context. They should understand the dated conjecture, why Naur's program theory makes it non-trivial, what a witness house must show, and why software gives a stronger falsifier at the price of a harder existence claim.

## Target claim or purpose

Restate, as a draft supplement to the lead article, the conjecture that at least one automated software house capable of open-ended coherent change can operate practically with only models available by 2026-09-02, held fixed. Keep the conjecture's own boundary, cutoff, and conditions, which predate the program framing, then map them onto the program: a house supplies falsifier, objective, and outcome level through product operation and users' judgments.

## Must keep

- Definitions of operates practically, open-ended, witness house, and witness run, and the comparative human-agent-house standard; a finite run gives bounded evidence, not the open-ended claim.
- The role-based boundary: internal production roles versus user roles; seed built by people; pinned models; an internal human intervention ends the run.
- Naur's program theory with a concrete example (tenant isolation), the proposed mechanism for retained commitments, the compiler case as underdetermined between missing, unfound, and unapplied premises, and the reading of Naur's people-bound argument.
- The four witness conditions, with the controls separating explanatory use from instruction-following.
- The Gödel machine contrast (proof versus empirical admission) and brief partial constructions.
- The comparison: theory about the product versus theory as product, falsifier strength, claim form, required machinery, and why the knowledge base goes first. The lead article summarizes this as stronger falsifier, harder claim.

## Exclusions

- No reliance on the conjecture that open-domain builders must become software houses.
- No detailed survey of existing systems; the nearest-constructions supplement holds it.
- Not the program's paradigm case, and not a special case of the knowledge-base arrangement.

## Scope, modality, and terminology

Existential conjecture, stated as such; draft banner. Use "software house", "program theory", and "witness" consistently.

## Reserved decisions

- Changing the cutoff date or the four conditions.
- Reordering which arrangement the program pursues first.
