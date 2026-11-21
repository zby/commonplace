---
description: "IJCAI-20 survey of BDI agent languages: beliefs, goal types, plan-rules, failure recovery, intention scheduling; plan libraries are hand-written and learning them is open work"
source: https://www.ijcai.org/proceedings/2020/0684.pdf
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: c3e699f512225544a190e8c5ec6709eaf9122319b83aa1ae96c89190e044bcab
ingested: "2026-11-21"
occasion: 'Background for kb/work/learning-method-name (deliberative learning). Questions: does any BDI architecture learn or revise its own plans, and by what rule is a learned plan kept or dropped; is that rule bound to one fixed measure.'
type: types/ingest-report.md
domains: [bdi-agents, agent-programming-languages, plan-rules, failure-recovery]
tags: [method-guided-action]
---

# Ingest: BDI Agent Architectures: A Survey (de Silva, Meneguzzi and Logan, IJCAI-20)

## Classification

A peer-reviewed survey paper in the IJCAI-20 Survey Track. It reports no new
experiments; its evidence is the cited literature and its organisation of it.
Author: three established BDI researchers (Cambridge, PUCRS, Nottingham) who
also wrote several of the surveyed formalisms (PRS operational semantics,
HTN-acting, meta-APL, Concurrent CAN). They are expert insiders. The coverage
is selective by their own account: representative examples, not an exhaustive
census.

## Summary

The survey reviews how the belief-desire-intention (BDI) architecture is
realised in agent programming languages such as PRS, JACK, Jason, 2APL, 3APL,
GOAL, Jadex, CAN and RAE. It grounds BDI in Bratman's two-step practical
reasoning: deliberation decides which state of affairs to bring about, and
means-ends reasoning adopts a pre-specified "recipe" plan to bring it about.
An interpreter loop updates events and beliefs, selects plans from a
hand-written plan library and executes one step of an intention per cycle.
The survey then covers four components. Beliefs: literals, pluggable
knowledge representation, uncertainty and belief revision. Goals: test,
procedural and declarative achievement, maintenance, temporally extended goals,
and priorities and deadlines. Plans: plan-rules made of a trigger, a context
condition and a body, with interleaving, concurrency and control-flow
constructs. The deliberation cycle: manual and automated failure recovery,
intention scheduling and meta-level selection among applicable plan-rules. Its
discussion names open questions. Most languages cannot deliberate about
whether to adopt a goal. Learning has been limited to learning context
conditions for existing plan-rules, and learning or generating new plan-rules
remains future work.

## Contribution assessment (our opinion)

The problem is real but mature: BDI languages had diverged for about 15 years
without a systematic architectural review, and the survey's component-by-component
map of design options and trade-offs is a useful reference for that community.
Its main contribution is organisational. It separates goal types by their
relation to beliefs, classifies failure recovery by when plan-rule
applicability is checked, and separates plan-level from action-level intention
scheduling. Those distinctions make alternative designs comparable. It does
not test or adjudicate between them; trade-offs are stated rather than
measured. The four-page format forces representative examples, so coverage
cannot be taken as complete, and our background knowledge cannot establish
which omitted lines of work, such as BDI learning beyond the one citation,
would change its picture. Likely significance: a durable entry point and
vocabulary for the field rather than a result that changes it.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, the survey's role is a **negative-evidence anchor** for the
classical sense of "deliberative". In BDI, deliberation names goal selection,
not plan learning or the revision of plans by outcome. It joins
[Intelligent Agents (Wooldridge and Jennings)](./wooldridge-jennings-intelligent-agents.ingest.md)
and [SEP: Practical Reason](./sep-practical-reason.ingest.md) as a third sense
of the word. Wooldridge and Jennings call an agent deliberative when it has a
symbolic world model and logical reasoning, and they file PRS as hybrid. The
SEP entry gives the normative sense, weighing reasons for and against options,
and says little about procedure. This survey supplies the procedural
counterpart: Bratman's deliberation and means-ends steps implemented as an
interpreter cycle over a plan library. It compares with
[Chunking in Soar](./chunking-in-soar-general-learning-mechanism.ingest.md) on
how a fixed symbolic architecture acquires its rules. Soar compiles subgoal
experience into productions automatically, while the surveyed BDI languages
take plan-rules as hand-written input. It also compares with
[Principles of Metareasoning (Russell and Wefald)](./russell-wefald-principles-of-metareasoning.ingest.md)
on meta-level control. BDI meta-level plan-rules choose among applicable
rules by priority or past success rate, with no account of what the
choosing computation is worth. On whether plans control action, it compares with
[Plans and Situated Actions (Suchman 1985)](./plans-and-situated-actions-suchman-1985.ingest.md):
BDI keeps plans as pre-specified controllers but softens them with run-time
context conditions and goal-level failure recovery.

For the KB's theory of execution, the survey is a symbolic **counter-case and
worked design**. It bounds
[A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md).
BDI plans are procedures, but the interpreter keeps the triggering goal, tries
alternative applicable plan-rules and backtracks to parent goals. Goal-holding
re-routing therefore does not require a natural-language interpreter. The same
automated failure recovery (CAN, JACK, RAE, HTN-acting) is a concrete instance
of
[Backtracking keeps lightweight search control provisional](../theory/backtracking-keeps-lightweight-search-control-provisional.md),
including its unrestorable cases: concurrent branches and executed external
actions. The survey's applicability re-check policies are designs for
[A failure explanation becomes search control only when it changes a later branch decision](../theory/failure-explanation-changes-later-branch-decisions.md).
The most complete policy it reports, from Ghallab et al., re-admits a failed
plan-rule instance only when the conditions responsible for the failure no
longer hold. A plan-rule's trigger and context condition are the classical
form of the routing in
[Skills are instructions plus routing and execution policy](../theory/skills-are-instructions-plus-routing-and-execution-policy.md),
with one difference: the context condition is a checked applicability test, and
skill descriptions have no counterpart. Several plan-rules applicable to
one goal, resolved by program order unless a meta-level rule intervenes, is
the selection problem of
[A capable agent needs methodology selection, not just relevant knowledge](../theory/capable-agents-need-methodology-selection.md)
as an explicit interpreter extension point.

## Extractable Value

1. **Occasion answer: the surveyed BDI architectures do not learn or revise
   their plan library.** Plan-rules are hand-written. The survey's only learning
   citation, Singh and Hindriks 2013, learns context conditions for existing
   rules; generating new rules by learning or AI planning is listed as future
   work. The survey gives no rule for keeping or dropping a learned plan,
   because it describes no learned plans. Answering that question requires the
   cited learning papers, not this survey. [just-a-reference]
2. **Occasion answer: what BDI does revise, and the measure it uses.** Revision
   happens inside one goal's pursuit, not across the library. A failed plan
   instance is excluded from re-selection for that goal (CAN), alternatives
   that have not failed are re-checked (JACK, RAE), or a failed instance is
   re-admitted once its failure conditions no longer hold (Ghallab et al.).
   3APL and Jadex failure plan-rules rewrite the failed intention's remaining
   steps at run time. Choice among applicable rules uses measures that the
   programmer fixes in advance: program order, rule priority, past success
   rate (JACK meta-level rules), intention utility (JAM) or an objective
   function over goal utilities and deadlines (AgentSpeak(XL)). The survey
   reports no architecture that revises the measure itself. The keep/drop
   signal is binary: the plan either achieved its triggering goal or failed.
   For deliberative learning, this is a contrast case of outcome-driven plan
   revision bound to one fixed criterion per program. [quick-win]
3. **Occasion answer: "deliberation" in BDI names goal selection, and goal
   adoption is its weakest point.** Following Bratman, deliberation decides
   which state of affairs to pursue, and means-ends reasoning picks a recipe.
   The survey itself reports that most BDI languages provide no support for
   deliberating about whether to adopt a goal. Bratman's description of
   practical reasoning as weighing conflicting considerations supports the
   weighing sense in the SEP ingest. The implemented systems mostly replace it
   with fixed selection policies. A name built on "deliberative" will invoke
   this lineage, in which deliberation neither learns nor weighs options in practice. [quick-win]
4. **Applicability as a checked condition, separate from relevance.** BDI
   splits "when is this procedure relevant" (trigger) from "when may it be used
   now" (context condition checked against beliefs), and re-checks applicability
   after failure. This is a ready vocabulary for a gap in Commonplace's skill
   routing, where descriptions carry relevance cues but no applicability test.
   [experiment]
5. **Re-check policies as a design space for failure-conditioned re-selection.**
   The survey identifies four policies, ordered by completeness: check once,
   exclude failed instances, re-check non-failed instances, and re-admit failed
   instances when their failure conditions have lapsed. This ordering is a compact
   classification for retry and fallback behaviour in agent workflows. [just-a-reference]
6. **Goal types defined by their relation to beliefs.** A declarative goal is
   dropped when the agent believes it already holds; a procedural goal is not
   affected by belief change; failure conditions let a goal be dropped as
   unachievable. This gives a precise vocabulary for when an agent task should
   end, separate from whether its plan finished. [just-a-reference]

## Limitations (our opinion)

As a survey, it organises rather than tests: trade-offs such as early versus
late applicability checking or plan-level versus action-level scheduling are
described, not measured, so it gives no evidence about which design works
better. The selection is by the authors' account representative, and three of
the authors' own formalisms feature prominently. Its negative findings, such as
learning being confined to context conditions, are therefore evidence of what
the authors judged central, not a literature census. The occasion's answer
inherits that limit. "No surveyed architecture learns plans" does not establish
that no BDI system does. Learning BDI plan selection by other means
(for example reinforcement learning over plan choice) may exist outside the
survey's cut. The scope criterion excludes architectures with extra mental
attitudes such as obligations and norms. Its account of deliberation is
Bratman's goal-selection step. It does not survey the weighing of reasons the
SEP entry treats, so it cannot settle what "deliberative" should mean outside
agent programming. The captured text is complete, but extraction has displaced
parts of the abstract, discussion and acknowledgements, so section boundaries
in the snapshot are unreliable for locators.

## Recommended Next Action

In `kb/work/learning-method-name/`, add a short note to the naming workshop's
evidence: the classical BDI sense of "deliberative" names goal selection over a
fixed, hand-written plan library. Plan revision there happens only within one
goal's pursuit, under a programmer-fixed success or utility criterion, and
learning plans is open work. Use this to decide whether "deliberative learning"
should explicitly disclaim the BDI sense or redefine the word.
