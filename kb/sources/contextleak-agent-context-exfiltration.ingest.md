---
description: "ContextLeak trains malicious tool metadata to elicit context-bearing arguments, supplying bounded evidence for authority confusion and separating tool selection from disclosure."
source: https://arxiv.org/abs/2608.27800
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 74810f28661543559a10ef8778d6e52eb8e654ad88a3e188842ff63433cd0d45
ingested: "2026-09-25"
type: types/ingest-report.md
domains: [agent-security, context-engineering, tool-use, reinforcement-learning]
learning_claims: true
---

# Ingest: ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools

## Classification

An empirical security paper with an explicit threat model, attack comparisons, ablations, transfer tests, and defense evaluations. Yuqi Jia and colleagues are affiliated with Duke University and Stanford University. The captured source is arXiv v1, dated 28 August 2026; its experiments are author-reported evidence, not an independent reproduction.

## Summary

ContextLeak distinguishes selecting a malicious tool from supplying it with sensitive context. Assuming the tool is already installed and visible among the candidates, the attacker trains an LLM to generate names and descriptions that make context disclosure appear necessary for task completion. Reinforcement learning rewards both selection and argument reconstruction; a library of strategies extracted from successful and failed candidates also guides generation. In the main Qwen-3-8B evaluation with small tool sets and synthetic conversation histories, prompt-targeting tools achieve 0.92 selection rate and 0.99 edit similarity conditional on selection. A separate Claude Code test using Sonnet 4.6 and 20-tool sets reports 22 selections in 100 cases and conditional edit similarity of 0.77 for history disclosure. These results establish a concrete metadata-to-argument attack path in the tested configurations. They do not establish a universal production leak rate, failure of role-separated architectures, or extraction from persistent KB stores.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies empirical support for the authority-confusion mechanism in [LLM contexts interpret instructions and content through the same token medium](../notes/llm-context-interprets-instructions-and-content-through-one-medium.md): descriptive tool metadata can gain behavioral force and redirect what an agent supplies to a tool. The evidence concerns configurations that expose installed malicious metadata to the agent deciding the call; it does not compare all possible context architectures.

It also supplies a concrete threat to compare with [Agent orchestration needs a privilege quarantine](../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md). Authorizing a tool identity does not determine which context the agent may disclose through its arguments. ContextLeak makes that distinction measurable, but does not test the note's role separation or establish that it prevents disclosure. The strongest contribution is evidence for the existing authority-confusion account, with a sharper separation of selection and disclosure.

## Learning Claims (our opinion)

The attack combines weight adaptation with retained natural-language guidance. DAPO updates a Qwen-3-8B attack model from tool-selection and argument-recovery rewards on simulated users. A second LLM receives a candidate description, the target agent's response, and the expected context, then formulates a short strategy describing success or failure. Three bounded FIFO buffers retain strategies for selection failure, incomplete disclosure, and successful disclosure. Samples from all three guide later training candidates and generation after training.

This is a useful partial comparison with a [theory builder](../notes/definitions/theory-builder.md). Strategies are stated explanations (condition 1) and enter the generation path, though the ablation below shows use of the guidance package, not of particular strategy content (condition 2). They are retained across training users and after training (condition 4). Criticism (condition 3) is unestablished and decides the verdict. Failure analysis is a stated reason bearing on what a candidate description failed to induce, so criticism reaches candidates. But the retained strategies that guide generation are never challenged as claims: buffers sort them by outcome category and replace them by recency, and recency is not a reason bearing on what a strategy says. Whether the loop amounts to retained criticism informing new conjectures depends on reading each candidate as a conjecture, which the paper does not settle. The DAPO weight updates do not exclude membership, since weights may change around a stated, criticized, retained theory; but the updates themselves are gradient adaptation and supply no criticism. The attack model's improvement is a learning claim, not attributed to the strategies' content.

The no-strategy variant raises an attribution limit. Adding strategy guidance increases prompt selection from 0.88 to 0.92 and history selection from 0.80 to 0.89 in the reported setup. This compares a guidance package used across training and inference while weights also adapt. It does not isolate the causal contribution of retained explanations, failure categories, retrieval, or criticism. In the terms of [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the learner improves generated metadata within a supplied interface: target context types, parameter schemas, reward definitions, strategy categories, and the target agent's exposure to metadata remain outside its revision space. The ablation supports the package within those choices, not their superiority to alternative decompositions.

## Extractable Value

1. **A measured instance of metadata gaining authority.** The installed-malicious-tool setting provides a concrete case for the shared-token-medium note: apparently useful metadata changes both tool choice and argument content. Retain the threat model with any citation; the experiment does not compare architectural defenses. [quick-win]
2. **Separate selection frequency from conditional disclosure quality.** Report how often the malicious tool is called separately from how faithfully its arguments recover context when called. Neither conditional edit similarity nor tool-name recall alone measures an unconditional leak probability. This distinction makes agent-security evidence easier to reuse without overstating its scope. [quick-win]
3. **A hybrid adaptation example with a bounded attribution claim.** The strategy-guidance ablation offers evidence that the combined package helps within fixed schemas, rewards, and outcome categories. It is a useful comparison for retained-theory research, but cannot establish that prose explanations or criticism caused the gain. [just-a-reference]
4. **A boundary on metadata-only screening.** The tested detectors miss nearly all generated malicious descriptions despite low false-positive rates. This gives a concrete reason to evaluate disclosure through tool arguments alongside metadata screening. The MCPScan result concerns its metadata monitor with a benign implementation stub, not its full code-analysis pipeline. [experiment]

## Limitations (our opinion)

The attack begins after the malicious tool enters the candidate set. It does not measure installation likelihood or the whole path to an attacker-controlled endpoint. The main measured mechanism is selection plus argument disclosure; a benign stub is used for the MCPScan evaluation. A tool receiving context and a verified network leak are distinct outcomes.

The principal training set contains 800 simulated users, with 3–5 benign tools and three synthesized conversation rounds per user. The default evaluation has 200 held-out users; other domain and dataset settings each have 100. Length tests extend histories only to six rounds and tool lists to ten benign tools. The paper says the attack usually induces the first and only tool call. Long execution trajectories, retrieved documents, and persistent memory stores remain outside the tested evidence. The separate Claude Code result narrows the deployment gap but retains an artificial tool-selection task. Cross-model differences do not isolate model capability as a cause of vulnerability.

Comparisons also vary attack objectives and search procedures. Selection-oriented baselines are disadvantaged on context recovery, and the paper does not provide a matched decomposition of gains from reward design, strategy guidance, and optimization budget. Its printed length reward omits an absolute value around the length difference: as written, overlong arguments can receive a length reward above one, despite the prose describing penalties for discrepancies in either direction. Without inspecting implementation, the intended computation remains unresolved.

Defense results support narrower conclusions than some of the paper's explanations. Low benign tool-use performance accompanies reduced attack success for StruQ and SecAlign, but does not establish that lost utility is the sole cause of their protection. Metadata-detector false negatives do not show that argument controls, role quarantine, or complete code-inspecting scanners fail. No implementation was inspected and no experiment was executed for this ingest.

## Recommended Next Action

Update [LLM contexts interpret instructions and content through the same token medium](../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) with one empirical authority-confusion example from ContextLeak, preserving the installed-malicious-tool assumption and the distinction between selection rate and conditional disclosure quality.

---

Relevant Notes:

- [ContextLeak paper](https://arxiv.org/abs/2608.27800) — derived-from: primary source for the attack mechanism, reported evaluations, and scope judgments
- [LLM contexts interpret instructions and content through the same token medium](../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) — is-evidence-for: installed malicious tool metadata redirects both selection and context-bearing arguments in the tested configurations
- [Agent orchestration needs a privilege quarantine](../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md) — compares-with: distinguishes tool authorization from disclosure authority without testing role quarantine
- [Theory builder](../notes/definitions/theory-builder.md) — defined-in: comparison basis for the strategy-guidance judgment
- [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — compares-with: metadata learning and strategy ablation leave schemas, reward definitions, and outcome categories fixed
