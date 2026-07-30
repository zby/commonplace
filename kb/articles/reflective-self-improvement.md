---
description: "Outward article, examples-first: four worked examples open the argument, then the pattern, its verification structure, and the bitter-lesson constraint are abstracted from them"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/self-improving-system.md
  - kb/notes/definitions/reflective-system.md
  - kb/notes/definitions/reach-assessment.md
  - kb/notes/reflection-buys-addressability.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/retrieval-failure-is-reflection-failure.md
  - kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/methodological-and-computational-closure-track-different-changes.md
  - kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md
  - kb/notes/self-improvement-is-relative-to-a-declared-objective.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/exact-implementation-does-not-validate-a-requirement.md
  - kb/notes/commitment-not-derivation-creates-new-ground-truth.md
  - kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md
  - kb/notes/parametric-reproduction-cannot-replace-an-authoritative-record.md
  - kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md
  - kb/reference/commonplace-as-a-reflective-system.md
  - kb/agentic-systems/exo.md
---

# Reflective self-improvement

Start with an episode from the system this article describes. An index page in a knowledge base promised to list every note carrying its tag. It also had to stay short, because index pages are loaded into the agent's context, where space is scarce. The two demands pull against each other, and nothing enforced either: staying complete made the page grow as notes accumulated, and by the time anyone measured, it was far past its context budget — and too large for anyone to still check that it was complete. The repair went further than trimming the page: a recorded decision turned the completeness promise into a machine-checked mark and put size gates on the page type — a warning as a page approaches the cap, a failure beyond it — so the next page outgrowing its completeness gets flagged before the promise breaks. Bringing the pages into compliance then caught a member the documented search recipe had missed, and the recipe was corrected as well. Operation revised the system's definition, and the revised definition changed operation. The whole trail is in the commit history.

Three smaller examples set up the rest.

Suppose last month your agent recorded a rule: "always pin the dependency versions." Kept as a note, the rule is an object. You can find it, ask what incident produced it, tighten it, or retire it. Trained into the weights, the same lesson has no address. Weight changes are not beyond intervention — they can be rolled back, trained over, and [model editing](https://arxiv.org/abs/2202.05262) can even target a specific stored association — but every one of those handles is indirect. None gives you the lesson as an object with a stated scope, a rationale, and a boundary you can point at.

"Retry the flaky login test" and "tests that read the wall clock flake, so freeze the clock" can be distilled from the same incident. The first is a lesson: it helps with one test. The second is a theory: it states why the test flakes, and it keeps working on tests that have not been written yet.

"The deploy fails on Tuesdays," distilled honestly from one misread trace, is a false rule — and once it sits in the instruction path it is obeyed like a true one. A directive smuggled in through a tool result and written into memory enters through the same path. Anything that writes to the instruction path modifies the system.

The examples show the rules this article generalizes: retained knowledge should be addressable like the pinned-versions note, selected for explanation like the wall-clock theory, and guarded on the write path against Tuesday rules. The index episode adds the condition that makes the pattern reflective: the artifacts kept under these rules were the system's own operative definition — the pages, checks, and recipes that steer its behavior — so improving them improved the system that uses them. Applied to an agent's own instructions and scaffolding, the pattern is **reflective self-improvement**. The rest of the article says what it is, why it needs structure rather than good intentions, and where its limits are.

## The pattern

An agent can read its own source: the prompts and instruction files that steer it, and the code that forms its scaffolding — the harness, the tools, the validators. It can interpret that source, reason about it, and change it. Software that acts on a representation of itself has a decades-old literature under the name *computational reflection*. What is new is who does the reading: with LLM agents, part of the interpretation, criticism, and rewriting moves inside the system. We believe this combination can produce systems that [improve themselves](../notes/definitions/self-improving-system.md) by analyzing and rewriting their own definitions.

Many ingredients of such systems have precedents in systems with weaker versions of the self-improvement loop. Agents already retain verbal lessons ([Reflexion](https://arxiv.org/abs/2303.11366)), grow libraries of executable skills ([Voyager](https://arxiv.org/abs/2305.16291)), evolve the prompts that steer them ([Promptbreeder](https://arxiv.org/abs/2309.16797)), and rewrite their own scaffolding code ([STOP](https://arxiv.org/abs/2310.02304), the [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954)). Each differs from what we propose on a different axis:

- Reflexion retains natural-language lessons, but they are episodic and unreviewed: scoped to retries of the current task, generated and consumed without criticism, not durable objects anyone governs.
- Voyager retains durable artifacts, but of one kind and in one direction: executable skills accumulate, while the instructions and scaffolding that run the loop are not themselves objects of improvement.
- Promptbreeder does change the text that steers the system, but by mutation and benchmark selection: the surviving prompt carries no rationale, so there is nothing to criticize, scope, or revise — only a tournament to re-run.
- STOP and the Darwin Gödel Machine rewrite their own scaffolding code, but their justification is a benchmark score, which admits only changes a benchmark can see. The original Gödel machine is the limiting case: full access to its own code, but it may adopt only changes it can prove beneficial, and for most useful changes no proof exists.

Across the list, each system either retains without governing, or justifies its changes through a channel — proof, fitness, benchmark — that admits only what the channel can measure. Our approach is to create a single operative self-representation spanning natural language and code, and to use LLMs to reason about it and change it. Reasoning in natural language widens the set of changes that can be proposed, criticized, and adopted; the cost is that such judgment needs verification structure outside itself, which much of this article is about.

The closest system is a peer rather than a precedent. [Exo](../agentic-systems/exo.md) already spans both forms: it keeps the complete event history, retains natural-language facts and skills, installs validated tools pinned to exact source commits, and can rebuild its own harness, recording a reason with each self-update. It starts from the substrate: record everything, make every kind of change adoptable, and let a capable model decide in the moment what deserves to persist. What it does not yet have is the selection and governance layer: a retained conclusion carries no type, scope, review state, or invalidation path, and the retention policy is at most a standing instruction rather than a maintained, revisable theory. We start from the opposite end — the theory of what to retain and the structure that governs it — with much less runtime substrate.

The paths were also independent: Commonplace's first commit is from February 2026, Exo's from May 2026, and we discovered Exo only recently. In our case the pattern was found by operating, not designed — running the system on its own methodology proved the most efficient way to improve it, and the loop ran as practice before it had a name. Two projects arriving at the same pattern from opposite ends, without knowledge of each other, is some evidence the pattern is natural.

## The bootstrap, with the author inside

A useful comparison is the self-hosting compiler. Once a language compiles itself, every improvement to the compiler is written in the language it improves. But the compiler never analyzes its own source. It has no opinion about its code: every change was searched for, judged, and adopted by humans; self-hosting contributed only the causal wire from artifact to behavior. Agents move part of the author inside the system. An agent can analyze its own instructions and code, find what is wrong with them, and propose better ones — and once a proposal is accepted, the improved artifacts define the next run, without touching the weights.

This is *reflection* in the older, computational sense — [a system containing a causally connected representation of itself](../notes/definitions/reflective-system.md) — not "the model reflects on its mistakes."

The pinned-versions example showed the first payoff: [addressability](../notes/reflection-buys-addressability.md), which fine-tuning cannot buy. Every retained lesson can be inspected, explained, revised, or deleted one at a time, and each of those operations has a place to happen.

For safety-minded readers the important property is that the loop is legible. Self-improvement in weights hands oversight a tensor delta: behavior can be measured before and after, but the change itself cannot be read. Self-improvement in artifacts hands oversight a plain-text diff that carries its own rationale. This narrows the audit surface without removing the need to evaluate behavior: the diff is legible as an intended commitment, but its consequences still depend on the model, the surrounding context, and retrieval — and a readable rationale can be mistaken or post-hoc.

A second payoff is [openly a conjecture: sample efficiency](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). It depends on turning most lessons into theories, as in the wall-clock example. A theory that captures structure surviving a task shift may adapt the system with fewer new observations than retraining or fine-tuning would need.

Defining a self-improving system also requires saying what improvement means. Nothing in the loop supplies that: a system that searches, judges, and retains can only report that something changed. [Improvement is relative to a declared objective](../notes/self-improvement-is-relative-to-a-declared-objective.md), and the objective must be named independently of the changes it is later invoked to license — otherwise the objective gets fitted to whatever happened and the loop certifies itself. Two systems with identical loops can be improving toward different things, or one of them toward nothing at all.

## What the compiler had and the agent loses

Two safeguards do not survive the transfer.

The compiler's wire is exhaustive: every build consumes the whole source, and nothing depends on being found. The agent's wire is retrieval, and retrieval is best-effort. A retained lesson counts only if a later run finds it; the note that would have prevented today's mistake, sitting unread two directories away, might as well not exist. That is why [retrieval failure is reflection failure](../notes/retrieval-failure-is-reflection-failure.md).

The compiler bootstrap also carries at least a fixed-point check: recompile the compiler with itself and compare the outputs. Ken Thompson [showed in his Turing Award lecture](https://dl.acm.org/doi/10.1145/358198.358210) that even this check can be fooled — a compiler corrupted in the right spot reproduces its own corruption while passing cleanly — so it was never proof of soundness, only a tripwire for accidental breakage. The agent has no tripwire at all. There is no fixed-point check for "this rewritten instruction is better," and the agent judges its proposed changes using the very instructions being changed — trusting trust again, with fuzzier tools.

## What the structure must cover

A serious agent bootstrap must therefore supply the verification that self-hosting never had built in. The opening examples cannot do that job by themselves: the loop has to handle lessons, changes, and failure modes no example anticipated, so the requirements must be stated generally. Any retained claim needs a contract saying what kind of claim it is. Validation has to run as code rather than as self-assessment. Review has to be able to say no from outside the text it judges. Navigation has to make retrieval reliable, because an artifact that is not found does not exist for the run that needed it. Commonplace is that structure: its [typed artifacts](../notes/why-notes-have-types.md) declare what kind of claim a note makes; its validators are code; its [review gates](../reference/README-REVIEW-SYSTEM.md) apply fixed criteria in a fresh context, so a note never grades itself; its curated indexes give retrieval a maintained map. The adoption decision itself still sits with a human maintainer. That is a current allocation, not a fixed feature: in our case improving includes becoming more autonomous — moving adoption judgments to checks that have earned them, so the same knowledge work costs less human judgment. What earning a migration takes is discussed below.

The Tuesday rule showed why the write path needs guarding: [a writable self-representation is an attack surface](../notes/a-consumption-channel-delivers-force-without-the-history-that.md). Whatever sits in the instruction path gets obeyed, and a path not built to check how its contents arrived will not ask. Provenance, write authority, review, and rollback are therefore part of the reflective architecture, not optional repository hygiene.

Guarded writes still say nothing about what is worth writing. A memory file that accumulates lessons without selection does not improve anything. The loop aims at theories with [explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md): retained claims that explain why something works and therefore hold beyond the episodes that produced them — the wall-clock theory rather than the retry lesson. The episodes are not discarded when the theory is written: a claim stays revisable only alongside the evidence that could overturn it. Review exists to test [whether a claimed reach is genuine](../notes/definitions/reach-assessment.md).

Reach is more than a target; it is the methodology: selecting for explanations is how this system decides what to retain. The commitment is itself a theory — that explanation-first retention yields more useful, better-warranted knowledge work per unit of human judgment spent — and the running checks [test its achievement, not its warrant](../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md): review asks whether a claimed reach is genuine, never whether pursuing reach serves the objective. Like every theory in the system, the methodology stays open to revision if the evidence goes against it.

The index episode from the opening is this structure working end to end. [Commonplace retains its own methodology as a Commonplace knowledge base and improves through it](../reference/commonplace-as-a-reflective-system.md), so episodes like it are [traced](../reference/tag-readme-trace-observed-causal-connection.md) rather than anecdotal. One detail matters for what counts as improvement: the quality bar — an index claiming completeness must not mislead a reader who trusts it — was named before the fix. That is what makes the episode improvement rather than mere change.

The division of labor in that episode should be stated precisely. Automation did the checking: the validator enforced the mark and caught the missed member. The maintainer did the rest — noticed the strain, initiated the fix, and accepted the result — with an agent drafting the candidate change in between. That is an allocation of functions, not a rung on an autonomy ladder: [which functions are human, joint, or computational](../notes/methodological-and-computational-closure-track-different-changes.md) is read per decision, and moving a judgment to a model changes who decides without establishing that the decision is sound.

Migration inward has to be earned. Writing a criterion down is only the first step: the criterion must be settled rather than merely named, and then executed by [a check that discriminates well enough for what is at stake](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md). A passing gate establishes that its criterion was met, not that meeting it made the system better — that second claim needs evidence of its own. Until it has some, the structure's value is that each acceptance is localized, evidenced, and reversible.

## Use is part of the test

The index episode demonstrates a causally connected improvement loop. It does not show that the chosen decomposition is right; use supplies that test. Whether the pieces compose into the intended capability shows only when they run together, and local checks cannot stand in for that: [an artifact can implement its requirement exactly while the requirement itself is a proxy for the capability](../notes/exact-implementation-does-not-validate-a-requirement.md). Passing a contract does not show the contract was the right one to write.

Running the framework on its own methodology generates the data for that test. The signals are missed retrievals, indexes that mislead, corrections that recur, and effort spent repeatedly on the same problem — the index episode began as one. Human workarounds have to be counted as failures too: when a maintainer patches around a bad artifact by hand, nothing in the system records a failure, but the maintainer's time was still spent. This is why the objective is measured per unit of human judgment.

## The bitter lesson constrains the loop

Commonplace is built from hand-designed structure — typed artifacts, link grammars, review criteria. The obvious objection is the bitter lesson: systems organized around knowledge supplied by their designers have repeatedly lost to methods that exploit increasing computation through search and learning. The classic computer-vision features — hand-crafted edge and keypoint detectors like SIFT — captured real regularities, met their specifications exactly, and were displaced by learned features anyway.

The objection constrains where this project should end up; it does not rule out the artifact layer. [The lesson selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md): it binds how useful structure is discovered and revised, not the form in which it is retained. A scalable loop can search over theories, instructions, tests, schemas, and programs; evaluate candidates; retain the selected ones as addressable artifacts; and later revise or retire them. In that architecture the artifacts are products and working state of learning — no more contrary to the lesson than learned weights are. Early fragments of that loop already run: prompt optimizers, evolutionary code search, automated harness engineering — though none yet manages a large, interdependent corpus over time.

Commonplace is not yet that loop. Humans still perform much of the diagnosis, the credit assignment — deciding which artifact a failure implicates — and the acceptance. But the loop needs scaffolding to run at all, and because the pattern is reflective, the scaffolding can be a simpler, less autonomous version of the system itself — the way a compiler is bootstrapped through earlier compilers. The current hand-worked version is that stage: it discovers the representations, operators, and checks a more autonomous version would need, and the improvements it accepts are improvements to itself. No artifact here is expected to be permanent: stronger models may absorb stable guidance, and structure whose value stops exceeding its cost should be relaxed or removed.

The remaining question is empirical, and the declared objective exists to answer it: does an evolving, addressable artifact layer improve adaptation, reliability, governance, or the objective itself, compared with stronger base models and simpler memory? Self-hosting generates the evidence; it does not settle the comparison.

Absorption itself, when it comes, mostly counts as success: an artifact whose lesson a stronger model internalizes served as curriculum and can be retired. What reproduction does not automatically transfer is governed current state: [which commitments are operative right now, on what evidence, adopted by whom](../notes/commitment-not-derivation-creates-new-ground-truth.md). "Retry with backoff" is general knowledge; "we retry with backoff, adopted after the March incident, owned by the platform team" is one deployment's fact — and [a copy in weights does not inherit the record's authority](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md): a model that memorized the decision log answers with the log as of its training cut. Even that claim is modest: it requires an authoritative, currently revisable representation somewhere in the system, not that it stay in Markdown.

The rest of the defense portfolio — which artifacts deserve codification, [whether external structure recurs as deployments move to harder tasks](../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md), where explanatory reach fits — is [catalogued separately, with one member load-bearing](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md); none of it is a prerequisite for this article's claim.

## Where to go next

If your agent stack retains lessons about its own operation and later uses them to alter that operation, you are already running a loose version of this loop. Four questions measure how loose. The first decides whether there is anything to measure: what notion of better is your loop responding to, and was it specifiable before the changes it now licenses? [The other three come from the loop itself](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): where do candidate changes come from, where can the loop say no, and which artifact carries an accepted change into the next run?

The pattern is being measured, too. A July 2026 preprint on [knowledge-centric self-improvement](https://arxiv.org/abs/2607.19592) keeps its agents generic and disposable, makes a curated knowledge base the only object that improves, and reports gains that survive freezing the artifact and handing it to a different model family. What that knowledge base retains is task knowledge, not a representation of the learner's own organization — so the study tests the retention-and-curation half of this program rather than reflective self-improvement as defined here, while showing that an external artifact can stay useful after the agent and the model family are swapped. We test our theory by profiling such systems claim by claim: [what is retained, when it becomes operative, what is addressable, and where its warrant stops](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md). The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps that theory, and [the repository](https://github.com/zby/commonplace) contains the framework itself, developed in the open with its own methodology.
