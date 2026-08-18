---
description: "A strong architectural argument for recursive code–inference execution, plan-as-program workflows, and compiling natural-language guardrails into typed deterministic middleware."
source_snapshot: "kb/sources/jdegoes-recursive-agent-architecture-2081854216264392934.md"
ingested: "2026-07-28"
type: kb/sources/types/ingest-report.md
domains: [computational-model, self-improving-systems, constraining, agentic-systems]
---

# Ingest: Your Old Agent Architecture Is Dead… Meet Its Replacement

Source: [Your Old Agent Architecture Is Dead… Meet Its Replacement](./jdegoes-recursive-agent-architecture-2081854216264392934.md)
Captured: 2026-07-28
From: https://x.com/jdegoes/status/2081854216264392934

## Classification

Genre: conceptual-essay -- an argumentative architecture essay built from current-system examples, analogies, and a proposed runtime direction, with a product disclosure for Golem rather than a controlled evaluation.
Domains: computational-model, self-improving-systems, constraining, agentic-systems
Author: John A. De Goes is an experienced programming-languages and Scala practitioner proposing a strong thesis about agent architecture; the article's implementation and performance claims are not independently verified here.

## Summary

The article argues that the familiar model/tool loop is only the surface of capable agents. Its proposed replacement is a recursive structure in which code invokes inference, inference writes code, and generated programs invoke further scoped inference to perform decomposition, iteration, aggregation, retries, and verification. Plans should be reified as programs that can be typed, tested, simulated, reviewed, and only then executed; natural-language rules should be compiled into deterministic middleware and per-task capability boundaries; and a durable runtime should supply suspension, exactly-once effects, failure recovery, and capability-bounded execution. The essay supports this with Claude Code dynamic workflows, large software-porting examples, and a contrast between small reversible filesystem work and large or irreversible tasks.

## Connections Found

The source is a strong counterpoint and technical basis for the computational side of Commonplace's code–prompt argument. It agrees with [Any symbolic program with LLM calls is a select/call program](../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) and [LLM↔code boundaries are natural checkpoints](../notes/llm-code-boundaries-are-natural-checkpoints.md) that reliable bookkeeping belongs in explicit code while inference handles bounded judgment. It also directly compares with [Deploy-time learning is the missing middle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) and [moving the interpretation–enforcement boundary requires cross-form coverage](../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md). The overlap is real but not identity: the article's co-recursion is primarily execution-time nesting plus one-way compilation of natural-language rules into middleware, whereas Commonplace's coevolution is a deploy-time lifecycle in which prompts remain live system-definition artifacts and movement along the verifiability gradient can reverse when a constraint loses its warrant.

## Extractable Value

1. **Code–inference alternation is an execution architecture, not merely a tool-loop variant.** The article gives a vivid operational form to the claim that inference can write the symbolic scheduler that later invokes inference, with nesting at multiple depths. This sharpens the distinction between a fixed top-level loop and a host-language program containing bounded calls. [quick-win]
2. **Plan-as-program is a concrete reliability boundary for large or irreversible work.** Reifying a plan before effects creates an artifact that can be type-checked, simulated, reviewed, and reused; this extends Commonplace's scheduler-separation argument from bookkeeping to pre-effect analysis. [experiment]
3. **The article supplies a useful two-axis trigger for leaving interactive execution.** Reversibility and scale distinguish the filesystem-sized, cheaply revertible quadrant from work where a plan must exist before execution; this is a candidate routing heuristic, not yet a validated universal boundary. [deep-dive]
4. **Compiled guardrails are a strong witness for the codification side of the verifiability gradient.** Middleware can turn a rule with a formal-enough meaning into an enforced property rather than a context-dependent request. The source is most useful here as a counterpoint: it treats the remaining natural-language text as decoration, while Commonplace preserves judgment-bearing natural language and a reverse relaxing path. [experiment]
5. **Recursive execution makes runtime guarantees part of agent architecture.** Suspension, exactly-once effects, durable state, and failure isolation are not optional implementation polish once generated programs act on long-lived or irreversible state. This expands the design space beyond prompts, models, and orchestration into the execution substrate. [deep-dive]

## Limitations (our opinion)

This is a persuasive conceptual essay, not evidence that the proposed universal architecture is necessary or that its claimed guarantees follow from using code. The examples are selectively chosen from software engineering, where test suites provide unusually strong oracles; the article does not establish transfer to domains with weak verification. “Code” is treated as perfectly reliable, but generated programs, middleware, runtimes, type models, tests, and containment boundaries can all be wrong or incomplete. The claim that natural-language rules are merely decoration conflates non-enforcement with non-effect: prompts can still route, explain, scope, and supply irreducible judgment even when they cannot guarantee a property. The article also moves from observed restricted systems to an unrestricted recursive future, and its Golem disclosure creates an incentive to emphasize durable-runtime requirements. Claims about Anthropic, Cloudflare, token savings, and large ports should be captured and checked independently before carrying quantitative weight.

## Recommended Next Action

Add this snapshot as an `evidenced-by` link from [Deploy-time learning is the missing middle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), with a counterpoint phrase distinguishing the article's one-way natural-language-to-middleware thesis from Commonplace's reversible coevolution of prompts and code.
