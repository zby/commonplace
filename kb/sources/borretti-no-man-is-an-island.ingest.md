---
description: "Borretti essay: AI absorbs code and exposition, dissolving the human community that supplies shared work and motivation; bears on absorbable exposition and effort relocation"
source: https://borretti.me/article/no-man-is-an-island
captured: "2026-10-24"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 40605d2281801d1678b8066394830ad7b93b0e63f048d133c4625afd187c51f3
ingested: "2026-10-24"
type: types/ingest-report.md
domains: [human-ai-collaboration, effort-relocation, deskilling, audience]
---

# Ingest: No Man Is an Island

## Classification

A conceptual essay. Borretti argues a thesis about how intellectual activity is sustained, using his own experience of software engineering and a pointer to recent AI results in mathematics. It has no data, method or counterexample search. The argument is a causal model (community supplies inputs, which sustain private work, which feeds the community back) asserted from introspection and observation.
Author: Fernando Borretti, a software engineer and essayist (borretti.me) who writes on programming languages, type systems and tooling. He is an opinionated practitioner without institutional research standing. The essay thanks Luke Drago and Andy Matuschak for feedback. This is the third Borretti essay in the KB, and it partly revises his earlier position on human capital.

## Summary

Borretti claims that sustained private intellectual work depends on two inputs that cannot be acquired alone: a shared body of work to build on, and extrinsic motivation. By extrinsic motivation he means the sense that others use and value your contribution, measured through recognition. Intrinsic motivation is real but transient, so extrinsic motivation fills the gaps. The private work in turn feeds the community through publications, code and citations. AI breaks this loop by making contributions superfluous. Training runs absorb blog posts and tutorials, and the model then reproduces them without credit. Libraries are used by agents whose operators never learn who wrote them. New programming languages matter little when humans no longer read code. Borretti reports that software discourse has narrowed to "prompts, harnesses, loops", that prompting is a shallow skill, and that human capital formation has collapsed. He predicts that mathematics will follow, then every intellectual domain. He rejects the view that this purge will leave only the intrinsically motivated: without community you do not get isolated workers, you get nothing. Read it for one practitioner's account of absorbable exposition losing its audience, and for a mechanism that bounds optimistic effort-relocation claims. It contains no evidence beyond the author's experience.

## Quotes

No source quotes have been retained yet.

## Connections Found

The essay's in-scope surface is narrow. Most of it, including motivation theory and social flourishing, lies outside KB methodology. It acts as a practitioner counterpoint at three points.

First, it is field evidence for the "genuinely absorbable" scope case in [parametric reproduction alone cannot replace an authoritative record](../theory/parametric-reproduction-cannot-replace-an-authoritative-record.md). Tutorials, workaround posts and expository writing are absorbed by training and reproduced on demand. The attribution guarantee, which that note says reproduction does not carry, is lost in the process. The essay bears only on the scope boundary. It never discusses authority-bearing records, so it neither supports nor challenges the note's central claim.

Second, it is a counter-description to [increasing computational autonomy relocates human effort to the frontier instead of reducing it](../theory/increasing-computational-autonomy-relocates-human-effort.md). That note predicts that freed attention moves to a harder frontier. Borretti experienced the relocated work ("manager of AI agents", prompting) as shallow, and argues that without community the human contribution stops instead of moving outward. This exposes an assumption the note leaves implicit: the elastic backlog needs motivated humans to keep pulling attention to the frontier. The two may not truly conflict, since prompting is the routine interface rather than the residual judgment the note has in mind.

Third, it states the opposite premise to [human-LLM differences are load-bearing for knowledge system design](../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md). Commonplace treats LLM readers as a real audience for dual-audience documents. Borretti treats an agent reader as no audience ("Maybe Claude cares, for what that's worth"), and his claim that contribution is pointless depends on that judgment.

Among sources, it pairs with [Bainbridge's Ironies of Automation](./ironies-of-automation.ingest.md) as a second deskilling mechanism. Bainbridge's is individual and operational: operators lose practice but must still take over. Borretti's is communal and motivational: without an audience there is no reason to practise or publish. It also revises the same author's [Human Bottlenecks](./fernando-borretti-human-bottlenecks.ingest.md), which held that human capital is not becoming worthless. The two are reconcilable, because that essay concerns existing capital and this one concerns its formation. A note citing Bottlenecks should not present its conclusion as Borretti's settled view. It generalizes [Human Routers of Machine Words](./borretti-human-routers-of-machine-words.ingest.md) from a writer to a field: delegating composition skips the thinking, and delegating code skips the systematic practice and shared discourse that sustained the field.

## Extractable Value

1. **The relocation premise depends on motivation** -- the effort-relocation note assumes attention will flow to the frontier. This essay names the condition under which it does not: when the relocated work feels shallow and nobody uses its products. A scope bullet on that note could state the dependence on operator motivation and on the residue being experienced as real work. The support is one opinion essay, so this is a qualification, not a refutation. [quick-win]
2. **A practitioner instance of absorbable exposition** -- it gives a concrete report of the parametric-reproduction note's absorbable case: workaround posts and tutorials answered by a model without credit. This makes the scope bullet's example, and its point about losing attribution, recognizable to readers. Context-bound to public expository writing. [just-a-reference]
3. **Communal deskilling as a distinct mechanism** -- together with Bainbridge, the essay separates two routes to losing human competence. Practice can atrophy in individuals, or the community that trains and motivates the next practitioners can disappear. The combination implies a claim the KB does not hold: automation that removes practice may also remove the supply of competent human judges that human-in-the-loop designs rely on. Whether this changes KB operation, for example treating operator review as a capacity the system must sustain, is an open question. It needs more than this essay. [deep-dive]
4. **An explicit "agents are not an audience" premise** -- the essay states clearly the premise that dual-audience writing rejects. It is useful as a named counter-position when discussing why a KB writes for agent readers. [just-a-reference]

## Limitations (our opinion)

The central claim is a causal model with no test. Borretti does not show that community output has actually fallen, that people have stopped publishing, or that intrinsic motivation cannot sustain long-term work. Counterexamples such as hobbyist communities with no external audience, or isolated long-term projects, go unexamined. The evidence is one person's experience during a fast transition. A simpler account fits it: early-transition disorientation, which may settle into a new community around new topics rather than none.
The essay also judges a field's depth by the discourse that reaches a practitioner. That discourse is a sample of what gets amplified, and in a new, commercially hot area, marketing and onboarding material dominate amplification. The narrowness of "prompts, harnesses, loops" may describe that filter rather than the subject. The essay treats prompting and the new computing model as one thing. Prompting alone may be shallow, but harness design raises the questions that languages and libraries raised: what to make explicit, where interfaces sit, what to check and what state to keep. Published work treats these as technical problems, for example a [survey that decomposes the agent harness](./agent-harness-large-language-model-agents-survey.ingest.md), [matched guidance ablations](./asi-bench-at-the-dawn-of-artificial-superintelligence.ingest.md) and [transferable harness improvements](./aide2-recursive-self-improvement-research-agents.ingest.md). These show the problems can be treated deeply, not that such work is common or decisive. The essay does not address this literature, and it skips the test that would separate its account from the filter account: whether deep work is actually rare or only drowned out. The essay assumes, rather than argues, that AI "would solve software engineering" and that humans no longer read code or make structural decisions. Those premises carry the conclusion, and the KB's [effort-relocation note](../theory/increasing-computational-autonomy-relocates-human-effort.md), which expects the human residue to be a harder frontier, suggests they are at least contested. The "fuel and oxidizer" framing is an analogy, not a mechanism. "Without community ... you get nothing" is stated as a law and is hard to falsify as phrased. The extension from software to mathematics and "every other domain" rests on a single linked reaction post. The author also has an interest: he is describing the loss of a practice he values, which may colour how shallow he judges the replacement work to be.

## Recommended Next Action

Add a scope bullet to [increasing computational autonomy relocates human effort to the frontier instead of reducing it](../theory/increasing-computational-autonomy-relocates-human-effort.md) stating that relocation presumes operators stay motivated to take on frontier work. Cite this ingest with an `evidenced-by` link as a qualifying practitioner report, not as corroboration.
