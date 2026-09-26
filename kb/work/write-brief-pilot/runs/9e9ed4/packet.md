# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/instructions/analyse-external-system-epistemic-architecture.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/instructions/analyse-external-system-epistemic-architecture.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Executors find the six output schemas hard to apply cold. Add one short worked example that runs a concrete system through the outputs, and tighten the ledger so results from different reviews line up and can be compared side by side.

## Retained intent

Source: retained commission for this document. Subject: `kb/instructions/analyse-external-system-epistemic-architecture.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: analyse an external system's epistemic architecture

## Governing question

What executable instruction should an agent follow to determine whether and how an external system produces knowledge rather than merely storing, reshaping, retrieving, or operationally using retained material?

## Audience and reader update

The immediate reader is an agent or maintainer performing a code- or document-grounded external-system analysis. After following the instruction, the reviewer should be able to identify the system's epistemic objects and transformations, trace candidate claims through evidence and acceptance routes, separate epistemic from operational authority, and state precisely what—if anything—the system warrants calling knowledge production.

## Target

- Path: `kb/instructions/analyse-external-system-epistemic-architecture.md`
- Collection: `kb/instructions/`
- Type: `kb/types/instruction.md`
- Provisional title: “Analyse an external system's epistemic architecture”

## User direction and retained intent

- Source: current user direction, 2026-08-20.
- Subject: promote the epistemic-architectures workshop result into a new review instruction for analysing how other systems generate knowledge rather than merely store memories.
- Role: authoritative for purpose and scope; it does not itself warrant factual claims about either system.

## Intended practical purpose

Produce one collection-neutral, source-grounded analysis procedure. It must work across memory subsystems and whole agentic systems. It should return route-level findings rather than force a system-wide taxonomy. It must distinguish generating novel candidate content from earning warrant for retained truth-apt content.

## Operativity

- Initial consumer: an agent or maintainer explicitly asked to analyse an external system's knowledge-production or epistemic architecture.
- Retrieval channel: the instruction's trigger-focused `description` plus explicit invocation by external-system review work.
- Force: prescriptive analysis procedure; its output informs a review but does not itself accept the external system's claims.
- Future conditional integration into `write-agent-memory-system-review` is a separate handoff.

## Required distinctions

- Storage, retrieval, consolidation, or fluent synthesis does not by itself establish knowledge production.
- Separate acquisition/import, non-ampliative reshaping, entailed derivation, ampliative conjecture, and behavior/policy adaptation.
- Separate epistemic objects: observation, source claim, derived claim, conjecture, explanation, executable model, plan, task outcome, scorecard, and other system-specific targets.
- Trace each applicable ampliative claim through the discovery lifecycle: observation, conjecture, consequence derivation, test, acceptance, integration.
- For each consequential check, name target, oracle, timing, force, epistemic authority, and operational authority.
- A grade or label is operative only on a route that consumes it to change rejection, revision, acceptance, retention, integration, rollback, use, or continued execution.
- Keep outcome checks, process checks, explanation warrant, and component attribution separate.
- Report lifecycle and authority per route; do not assign one unqualified epistemic status or oracle to a heterogeneous system.
- Separate code-enforced behavior, natural-language doctrine, reported operation, observed run evidence, and causal experiment evidence.

## Required instruction behavior

- Begin with prerequisites and a source/evidence boundary.
- Include an early short exit for systems that only retain or serve material and expose no relevant transformation or epistemic claim.
- Require an epistemic-object inventory before oracle assessment.
- Require at least one route ledger with an explicit output schema.
- Require a lifecycle disposition for every candidate truth-apt output.
- Require system-claim versus implemented-route comparison.
- End with a bounded conclusion stating what the system acquires, derives, conjectures, tests, accepts, integrates, or merely uses.
- Include misuse guards drawn from the six workshop cases without requiring the executor to load the workshop.
- Be executable on first reading and keep theory rationale out of the procedure body except where needed to make a decision.

## Scope

Include:

- natural-language, symbolic, and parametric retained outputs;
- human-, model-, program-, environment-, proof-, measurement-, and hybrid evaluation routes;
- systems that generate no claims, generate conjectures without acceptance, check consequences without accepting explanations, or integrate scoped accepted claims;
- route-level negative results and evidence gaps.

Exclude:

- ranking products by quality;
- treating benchmark success as component attribution;
- requiring every knowledge-producing system to use proposal comparison, natural-language claims, or the Commonplace storage model;
- designing a universal ontology of knowledge;
- adding controlled tokens or matrix schema before the trials show a stable need.

## Collection and type constraints

- Follow `kb/instructions/COLLECTION.md`: executable and precise, frontloaded, explicit decisions and scope, minimal rationale.
- Follow `kb/types/instruction.md`: imperative title, trigger-focused description, prerequisites, steps, and verification where needed.
- Frontmatter must contain `description` and `type: kb/types/instruction.md` only unless a concrete runtime consumer requires more.
- The instruction must not depend on links into `kb/work/` during execution.

## Known uncertainties and acceptance criteria

- The correct output may be a route ledger plus lifecycle disposition rather than a single knowledge-generation verdict. The instruction must resolve this operationally without inventing a system-wide scalar.
- Unsupported system-specific claims must not enter the instruction.
- The instruction passes only if both trial agents can execute it without clarification, keep source/doctrine/report distinctions, and produce different route-level findings appropriate to the systems.
