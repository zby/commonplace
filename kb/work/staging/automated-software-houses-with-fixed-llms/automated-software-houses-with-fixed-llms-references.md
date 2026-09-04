---
description: "Primary sources for The Automated Software House Conjecture paper"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
---
# References

These primary sources bind the paper's explicit citations and its named comparison cases.

### Peter Naur — Programming as Theory Building

Peter Naur. “Programming as Theory Building.” 1985. Primary text: [PDF](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf). Locators used here: §2 for the compiler case; §§3–5 for theory, similarity, and modification; §6 for program life and transfer; §8 for the human-only claim.

KB provenance: `kb/sources/programming-as-theory-building.ingest.md`.

### Jürgen Schmidhuber — Gödel Machines

Jürgen Schmidhuber. “Gödel Machines: Fully Self-Referential Optimal Universal Self-Improvers.” Technical Report IDSIA-19-03, version 5, 2006; first version 2003. Primary record: [arXiv cs/0309048](https://arxiv.org/abs/cs/0309048). Locators used here: §§2.2 and 3.2 for the rewrite and proof gate; §2.4 for the unprovable-improvement limit; Theorem 4.1 for conditional global optimality; §6.1 for the writable scope.

Quoted passage retained from §2.4, printed p. 5 and PDF p. 6: “must ignore those self-improvements whose effectiveness it cannot prove”.

KB provenance: `kb/sources/goedel-machines-schmidhuber.ingest.md`.

### Mrinal — How I built a self-improving software factory

Mrinal (`@mrinal`). “How I built a self-improving software factory.” 2026. Primary locator: [X thread 2081823472016335059](https://x.com/mrinal/status/2081823472016335059), posts 1–5. The thread describes Fluent's human-guided brief, behaviour-specification, technical-approach, review, and retained-expertise roles.

KB provenance: `kb/sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md`.

### Ryan Lopopolo — Harness Engineering: Leveraging Codex in an Agent-First World

Ryan Lopopolo. “Harness Engineering: Leveraging Codex in an Agent-First World.” 2026. Primary locator: [OpenAI](https://openai.com/index/harness-engineering/), especially the sections on domain context, architectural constraints, and entropy management. The report assigns capability diagnosis and the resulting tools, linters, and structural tests to engineers.

KB provenance: `kb/sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md`.

### Jenny Zhang and colleagues — Darwin Gödel Machine

Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. “Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents.” 2026. Primary locator: [arXiv 2505.22954](https://arxiv.org/abs/2505.22954), §3 and Appendix C.2. These passages specify frozen foundation models, the separate diagnostic model, child viability admission, and benchmark-weighted parent selection.

KB provenance: `kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md`.

### Wenyi Wang and colleagues — Huxley-Gödel Machine

Wenyi Wang, Piotr Piekos, Li Nanbo, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, and Jürgen Schmidhuber. “Huxley-Gödel Machine.” 2026. Primary locator: [OpenReview paper T0EiEuhOOL](https://openreview.net/pdf?id=T0EiEuhOOL), especially the method and benchmark-result sections on estimating a lineage's later descendant productivity and using that estimate for lineage selection.

KB provenance: `kb/sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md`.

### Jenny Zhang and colleagues — Hyperagents

Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, and Tatiana Shavrina. “Hyperagents.” 2026. Primary locators: [arXiv 2603.19461](https://arxiv.org/abs/2603.19461) and the [reviewed repository commit](https://github.com/facebookresearch/Hyperagents/commit/59a68f672dfb92c74aeb7e61535d776fb36e172d). The repository's generation loop and patch utilities show executable patch-lineage retention around model calls.

KB provenance: `kb/sources/hyperagents.ingest.md`; code inspection recorded in `kb/agent-memory-systems/reviews/hyperagents.md`.

### Mirac Suzgun and colleagues — Dynamic Cheatsheet

Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, and James Zou. “Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory.” 2025. Primary locators: [arXiv 2504.07952](https://arxiv.org/abs/2504.07952) and the [reviewed repository commit](https://github.com/suzgunmirac/dynamic-cheatsheet/commit/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9). The cumulative implementation retains natural-language cheatsheet state and injects it into later solver prompts.

KB provenance: code inspection recorded in `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md`.

### Guanzhi Wang and colleagues — Voyager

Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. “Voyager: An Open-Ended Embodied Agent with Large Language Models.” 2023. Primary locators: [arXiv 2305.16291](https://arxiv.org/abs/2305.16291) and the [reviewed repository commit](https://github.com/MineDojo/Voyager/commit/55e45a880755d0c8c66ca7fb5fe7962ac8974f89). The action, critic, and skill-manager paths show critic-gated promotion of generated JavaScript skills and later retrieval.

KB provenance: code inspection recorded in `kb/agent-memory-systems/reviews/voyager.md`.
