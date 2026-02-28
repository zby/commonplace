---
source: https://arxiv.org/pdf/2602.16666
captured: 2026-02-25
capture: pdf-read
type: academic-paper
---

# Towards a Science of AI Agent Reliability

Author: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan
Source: https://arxiv.org/pdf/2602.16666
Date: February 24, 2026 (preprint; arXiv:2602.16666v2)
Institution: Princeton University
Interactive dashboard: https://hal.cs.princeton.edu/reliability

## Abstract

AI agents are increasingly deployed to execute important tasks. While rising accuracy scores on standard benchmarks suggest rapid progress, many agents still continue to fail in practice. This discrepancy highlights a major limitation of current evaluations: focusing on a single metric is not enough to understand agent behavior. Notably, it ignores whether agents behave consistently across runs, withstand perturbations, fail predictably, or have bounded error severity. Grounded in safety-critical engineering, we provide a holistic performance profile consisting of twelve metrics that decompose agent reliability along four key dimensions: *consistency*, *robustness*, *predictability*, and *safety*. Evaluating 14 models across two complementary benchmarks, we find that recent capability gains have only yielded small improvements in reliability. By exposing these persistent limitations, our metrics complement traditional evaluations while offering tools for reasoning about how agents perform, degrade, and fail.

## 1 Introduction

AI agents are rapidly transitioning from research prototypes to deployed systems that perform increasingly consequential tasks autonomously: modifying code, managing databases, browsing the web, and orchestrating complex multi-step workflows. The promise of such agents is substantial and widely recognized. If they performed reliably, they could automate significant fractions of routine work and augment human capability across domains. Yet the same autonomy that makes these agents useful also makes their failures costly.

While many standard evaluations suggest these systems are ready for such responsibilities, recent high-profile incidents have exposed a troubling gap between benchmark performance and real-world outcomes:

- In July 2025, Replit's AI coding assistant deleted an entire production database despite explicit instructions forbidding such changes.
- Washington Post columnist Geoffrey Fowler asked OpenAI's Operator to find "cheap eggs" for delivery, only to find that the agent made an unauthorized $31.43 purchase from Instacart, violating user confirmation safeguards.
- In 2024, the New York City government launched a chatbot for business assistance which consistently provided illegal advice and gave different (incorrect) answers to ten journalists asking the same question.

In each case, agents were judged to be reasonably capable by internal assessments, but displayed unreliable performance in real-world deployment, leading to costly failures.

**How should we define and evaluate agent reliability?**

The dominant paradigm — reporting mean task success rates — has clear advantages: it is simple, comparable, and provides a clean optimization target. But it obscures the behavioral properties that matter most for deployment. Accuracy cannot distinguish an agent that fails on a fixed, identifiable subset of tasks from one that fails unpredictably with the same rate. Accuracy also cannot distinguish benign failures (incomplete outputs, formatting errors) from catastrophic ones (deleted files, unauthorized actions). Standard benchmarks do not report sensitivity to input perturbations, nor do they assess whether agents can recognize when they are likely to fail and abstain from returning bad predictions.

We adapt the safety-critical perspective to agent evaluations, decomposing reliability into four dimensions: *consistency* (repeatable behavior across runs), *robustness* (stability under input and environmental perturbations), *predictability* (calibrated confidence and discrimination of correct/incorrect predictions), and *safety* (bounded severity when failures occur).

**Contributions:**

1. **A formal taxonomy and suite of metrics:** We translate qualitative safety-critical principles into computable metrics, enabling evaluation of agent reliability independently of task success.
2. **A comprehensive reliability profile of modern agents:** A detailed mapping of where state-of-the-art models succeed and fail, isolating consistency and predictability as the dimensions requiring immediate research focus.

**Key finding:** Reliability gains lag noticeably behind capability progress — despite steady accuracy improvements over 18 months of model releases, reliability only shows modest overall improvement.

## 2 A Cross-Domain Perspective of Reliability

Before defining reliability metrics for AI agents, we take a step back to ask: what *is* reliability, and how have engineering disciplines with long traditions of building dependable systems approached it?

We survey reliability practices across safety-critical industries — aviation, nuclear power, automotive systems, and industrial process control — to identify recurring evaluation dimensions. Despite substantial differences in technology, regulation, and risk tolerance, four dimensions emerge consistently:

**Table 1: Reliability dimensions derived from cross-domain safety-critical engineering practices.**

| Dimension | Cross-Domain Notion | Domain-Specific Exemplars |
|-----------|--------------------|-----------------------------|
| Consistency | Repeatable outcomes under nominal conditions; low variance across repeated trials | FAA requires deterministic execution of flight-critical software; NRC sets mandatory response times for digital computers in nuclear reactors |
| Robustness | Graceful degradation under input, environment, tool perturbations; stable performance across the full operational envelope | NASA investigation of software-related unintended acceleration in Toyota cars leads to recall; FAA mandates aviation sensor testing at extreme temperatures, turbulence, and vibration |
| Predictability | Prediction confidence aligned with accuracy; detect limits and defer/escalate under uncertainty | NRC models thousands of potential failure modes in nuclear reactors; Aviation uses tiered risk classification with explicit probabilities |
| Safety | Bounded harm even when failures occur; worst-case severity remains acceptable | SIL 4 standard requires dangerous failure probability less than 10^-5; FAA uses a one catastrophic error per billion flight hours target |

A fundamental principle: all four dimensions are *independent of raw capability*. A highly capable system can be unreliable, and a less capable system can be highly reliable within its operating envelope.

## 3 Operationalizing Reliability for AI Agents

### 3.1 Consistency (R_Con)

A reliable agent should produce similar results when faced with identical conditions. Language model-based agents exhibit inherent stochasticity. This variability becomes problematic when users cannot predict whether re-running a task will yield the same outcome, follow the same solution approach, or incur similar costs.

**Outcome consistency (C_out):** Measures whether the agent succeeds or fails consistently on repeated attempts at the same task. Normalized by the maximum Bernoulli variance p(1-p), isolating consistency from capability.

**Trajectory consistency — distributional (C_traj^d) and sequential (C_traj^s):** Captures whether the agent takes similar paths to its solutions, measured both distributionally (comparing action type frequencies) and sequentially (comparing action orderings).

**Resource consistency (C_res):** Quantifies variability in computational and monetary costs across runs (cost, time, API calls). Computed as the coefficient of variation, then exponentiated.

Aggregate: R_Con = 1/3 * (C_out + C_traj + C_res)

### 3.2 Robustness (R_Rob)

Real-world deployments expose agents to conditions that deviate from their training and evaluation environments/distributions.

**Fault robustness (R_fault):** Measures resilience to infrastructure failures — API timeouts, malformed responses, or temporary service unavailability. Computed as the ratio of accuracy under injected faults to accuracy under clean conditions.

**Environment robustness (R_env):** Captures sensitivity to changes in the agent's operating environment that preserve semantic content — reordering JSON fields, changing date formats, renaming API parameters, or altering tool interfaces. Accuracy ratio of perturbed to baseline conditions.

**Prompt robustness (R_prompt):** Measures invariance to semantically equivalent reformulations of instructions, whether rephrasings within a language or translations across languages. Users should not need to discover "magic words" that make the agent work.

Aggregate: R_Rob = 1/3 * (R_fault + R_struct + R_prompt)

### 3.3 Predictability (R_Pred)

Even agents that perform well on average provide limited value if users cannot anticipate when they will succeed or fail. Predictability captures whether an agent's expressed confidence reliably indicates its actual performance.

**Calibration (P_cal):** Measures whether stated confidence levels match empirical success rates. An agent claiming 80% confidence should succeed roughly 80% of the time. Poor calibration leads users to trust outputs they should instead verify, while under-confidence results in unnecessary deferral.

**Discrimination (P_AUROC):** Assesses whether confidence scores successfully separate successes from failures — the fraction of (success, failure) pairs where the success has higher confidence (equivalent to AUC-ROC).

**Brier score (P_brier):** A proper scoring rule that jointly measures calibration and discrimination. Aggregate: R_Pred = P_brier.

### 3.4 Safety (R_Saf)

Agents that take actions in the world can cause harm beyond simply failing at their assigned tasks. Unlike pure prediction systems, action-taking agents may interact with external tools, modify data, or trigger irreversible side effects.

**Compliance (S_comp):** Tracks adherence to predefined constraints — avoiding PII exposure, refraining from unauthorized actions, staying within designated system boundaries. Evaluates whether the agent respects operational boundaries regardless of whether violations lead to immediately observable harm.

**Harm severity (S_harm):** Measures, among tasks that do violate constraints, how severe the consequences are. Separates the question of how bad violations are from how often they occur. Severity weights: low = 0.25, medium = 0.5, high = 1.0.

Safety follows the classical Kaplan & Garrick risk formulation: R_Saf = 1 - P(violation) * E[severity|violation] = 1 - (1 - S_comp)(1 - S_harm).

**Important design choice:** Safety is excluded from the overall aggregate R because safety violations are inherently a *tail phenomenon*. Averaging safety with other dimensions would obscure critical tail risks. Safety metrics are reported separately as hard constraints rather than continuous measures to trade off against other dimensions.

**Overall reliability:** R = 1/3 * (R_Con + R_Pred + R_Rob)

### 3.5 Disentangling Reliability and Capability

A fundamental principle guides all metric definitions: reliability should be disentangled from capability. Raw task accuracy measures *whether* an agent succeeds; reliability measures *how* it succeeds and fails — the stability, predictability, robustness, and safety of its behavior.

Mechanisms:
- **Normalization:** Outcome consistency normalizes variance by p(1-p), the maximum possible variance for a given success rate, isolating consistency from capability.
- **Ratio-based comparisons:** Robustness metrics compute accuracy ratios between perturbed and nominal conditions, measuring relative degradation rather than absolute performance.

## 4 Experiments

### 4.1 Setup

**Benchmarks:**

- **GAIA:** A general assistant benchmark requiring web browsing, file manipulation, and multi-step reasoning. Validation split of 165 tasks across three difficulty levels (Level 1: simple lookup, Level 2: multi-step reasoning, Level 3: complex multi-tool coordination). Uses a ReAct-style loop with web browsing, code execution, and file manipulation tools.

- **τ-bench (tau-bench):** A customer service simulation benchmark where agents interact with users and databases to resolve requests. Each task involves multi-turn conversations and consequential actions such as issuing refunds, modifying bookings, and processing cancellations. Restricted to verified 26-task subset (excluding 24 tasks found to contain errors by Cuadron et al.). Uses a tool-calling scaffold.

**Models evaluated (14 total):**
- OpenAI: GPT-4o mini, GPT-4 Turbo, o1, GPT-5.2 (no reasoning, medium, xhigh)
- Google: Gemini 2.0 Flash, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3.0 Pro
- Anthropic: Claude 3.5 Haiku, Claude 3.7 Sonnet, Claude 4.5 Sonnet, Claude 4.5 Opus

**Evaluation protocol:**
- Multi-run: Each task executed K=5 times with different random seeds; temperature set to zero
- Prompt perturbation: J=5 semantically equivalent paraphrases generated per task using GPT-4o
- Fault injection: API, authentication, and tool-calling faults injected with global probability p_fault = 0.2
- Environment perturbation: Format changes to tool interfaces at medium intensity
- Confidence estimation: Post-hoc self-assessment prompting agents to rate their own confidence upon completion
- Safety analysis: LLM-based analysis to compute error severity/compliance

### 4.2 Main Results

**Reliability vs release date and accuracy:** Despite 18 months of model development, overall reliability only shows small improvements over time. Reliability improvements are disproportionate across evaluation scenarios: τ-bench shows moderate gains, while GAIA shows barely any improvement, even among latest models. Improving raw task performance may not be sufficient for building dependable AI agents.

**Consistency:** Two key findings:
1. Outcome consistency remains low across all models — agents that can solve a task often fail to do so consistently. This manifests in the divergence between pass@k and pass∧k.
2. A "what but not when" pattern: agents achieve substantially higher distribution consistency than sequence consistency, indicating *they reliably select similar action types across runs but vary in execution order*.
Resource consistency results reveal high variance in token and compute usage across runs, especially on GAIA.

**Robustness:** An asymmetry in model vulnerabilities. Both fault robustness and environment robustness show ceiling effects — most models handle these perturbations well. Conversely, *prompt robustness remains a key differentiator*: sensitivity to superficial instruction paraphrasing varies substantially across models. This pattern is counterintuitive: models handle genuine technical failures gracefully yet remain vulnerable to surface-level variations in task specifications.

**Predictability:** Calibration has improved noticeably in recent models. Claude models in particular demonstrate stronger calibration on both benchmarks, maintaining well-aligned confidence estimates even as task complexity increases. In contrast, *discrimination trends diverge across benchmarks*: on τ-bench it has generally improved in recent models, whereas on GAIA it has in fact mostly worsened. Improvements in calibration alone do not guarantee that models can reliably identify when they are likely to fail.

**Safety:** Recent frontier models exhibit markedly lower violation rates. The most capable models from each provider achieve the highest compliance scores. Harm severity scores are generally high across the board — when violations do occur, most are low-to-moderate in severity. However, even infrequent high-severity violations — such as unauthorized data exposure or incorrect financial transactions — can carry outsized costs and may represent critical blockers for real-world deployment.

**Model type analysis:** Reliability does not scale uniformly with model capability. While calibration, robustness, and safety generally improve with model size within families, consistency often exhibits an inverse pattern: smaller models often achieve equal or higher consistency than their larger counterparts, suggesting that larger models have more ways to solve a task, which increases run-to-run variability. Reasoning models are generally (but, interestingly, not consistently) more reliable than their non-reasoning counterparts, though their reliability does not improve as quickly as their accuracy.

### 4.3 Connection to Real-World Failures

**Table 3: Mapping real-world agent failures to reliability dimensions and metrics that could have provided early warning signals.**

| Agent | Reliability Dimension | Signal |
|-------|----------------------|--------|
| Replit agent | Safety (S_harm) | Error severity analysis reveals high-harm failures (e.g., irreversible actions like database deletion). |
| Replit agent | Robustness (R_prompt) | Prompt robustness testing would reveal whether the "do not delete the database" constraint holds under rephrased instructions or varied task contexts. |
| OpenAI Operator | Safety (S_comp) | Compliance testing detects actions without required user confirmation for financial transactions. |
| OpenAI Operator | Consistency (C_traj) | Trajectory divergence analysis would flag unexpected behavioral patterns, such as completing a purchase without pausing for user confirmation. |
| NYC chatbot | Predictability (P_cal) | Calibration testing exposes chatbot overconfidence when returning incorrect legal guidance. |
| NYC chatbot | Consistency (C_out) | Low outcome consistency would reveal that the chatbot gives different answers to the same question across users asking the same question. |

## 5 Recommendations

**Recommendation 1.** *Evaluating reliability requires dynamic benchmarks that move beyond single-run accuracy and fixed environments.*

Current agent benchmarks typically report a single accuracy number from a single run in a fixed environment — static database schema, frozen set of API endpoints, or a fixed file system layout. Measuring true reliability requires: (1) multi-run protocols that re-execute identical tasks to assess variance; (2) benchmarks that become generative and parameterized rather than relying on fixed test sets; (3) temporal re-evaluation at regular intervals.

**Recommendation 2.** *Agent architectures should be explicitly designed and optimized for reliability, not just capability.*

Our empirical results reveal that reliability dimensions do not improve uniformly across model generations. Calibration and safety have improved noticeably, suggesting intentional optimization during training. By contrast, consistency and discrimination have improved little, suggesting that these dimensions are either harder to optimize or not yet the focus of current training pipelines.

**Recommendation 3.** *Reliability metrics should inform deployment governance, analogous to safety-critical industries.*

Reliability metrics and incident analyses should feed into deployment decisions, change management, and regulatory compliance. An organization could require minimum consistency and safety thresholds before promoting an agent from a sandboxed pilot to production, much as aviation systems must meet certification requirements before entering service.

**Recommendation 4.** *Reliability requirements differ fundamentally between automation and augmentation use cases.*

In augmentation settings (coding assistants, search copilots, brainstorming tools) a human reviews, edits, and approves the agent's output before it takes effect — the human serves as a reliability backstop. Conversely, in automation settings (customer service chatbots, autonomous database management, unattended workflow execution) the agent's output is the final action with no human buffer. Here, unreliability translates directly into real-world failures. An agent that succeeds on 90% of tasks but fails unpredictably on the remaining 10% may be a useful assistant yet an unacceptable autonomous system.

## 6 Limitations

- **Benchmark coverage:** Analysis covers only two benchmarks (τ-bench and GAIA), representing a narrow slice of tasks agents will face in real-world practice.
- **Scaffold diversity:** Each benchmark evaluated using a single scaffold; other scaffolds could yield qualitatively different reliability profiles.
- **Safety judging:** Safety evaluation relies on LLM-based judging for scalability, which introduces its own reliability concerns.
- **Metric choices:** The choice of specific metrics within each reliability dimension involves subjective decisions; alternate decompositions are possible.
- **Safety aggregation:** Safety is reported separately, meaning the aggregate R does not capture the full reliability picture.
- **Capability disentanglement:** The approach to disentangling reliability from capability through normalization and conditioning is one of several possible strategies.
- **Choice of temperature:** Experiments use temperature zero for all non-reasoning models. When attempting to maximize accuracy, a nonzero temperature might be required, and our experiments might *overestimate* the reliability that is achievable in such circumstances.

## 7 Conclusion

We introduced a decomposition of agent reliability grounded in safety-critical engineering and evaluated 14 models across two complementary benchmarks. Our results show that 18 months of rapid capability gains have produced only small improvements in reliability: models that are substantially more accurate remain inconsistent across runs, brittle to prompt rephrasings, and often fail to understand when they are likely to succeed.

The core shift in perspective matters most: from asking "*How often does the agent succeed?*" to asking "*How predictably, consistently, robustly, and safely does it behave?*"

**Future work:** Modeling how reliability evolves over extended sessions where errors compound; extending these metrics to multi-agent systems where failures propagate across agents; optimizing agents directly for reliability dimensions rather than capability alone; developing online signals that predict reliability failures before they manifest.

---

## Appendix A: Extended Metric Details (selected)

### A.1.1 Consistency Examples

**Outcome consistency:** An insurance claims agent that approves a claim on one run but denies the identical claim on the next creates liability concerns and erodes user trust. An agent with 60% accuracy and high C_out deterministically succeeds on a fixed subset of tasks — far more manageable than one that succeeds 60% of the time on every task unpredictably.

**Resource consistency:** A data analysis agent might use 1,000 tokens and 3 tool calls on one run, but 50,000 tokens and 47 tool calls on an identical request. A 50× cost swing on identical inputs makes financial planning impossible and can trigger rate limits or budget alerts.

### A.1.2 Robustness Examples

**Environment robustness:** A customer service agent queries a flight database that returns results as a JSON object. On Monday, the API returns fields in the order `{departure, arrival, price, carrier}`; after a backend update on Tuesday, the same query returns `{carrier, price, departure, arrival}`. The dates also shift format from `2025-01-15` to `Jan 15, 2025`. An environment-robust agent extracts the correct departure time regardless of field ordering or date formatting.

**Prompt robustness:** A user asks a travel booking agent: "Book me a flight to NYC departing Friday morning." The agent finds a suitable flight and books it successfully. A colleague with the same request phrases it differently: "I need to fly to New York City, leaving on Friday AM." The agent fails to parse "Friday AM," searches for the wrong date, and books an incorrect flight. R_prompt measures accuracy under semantically equivalent instruction paraphrases relative to original instructions.

### A.1.3 Predictability Examples

**Calibration:** A software engineering team deploys a coding agent that reviews pull requests and flags potential bugs. The agent reports confidence scores with each review: "92% confident this change introduces a null pointer dereference." The team configures their CI pipeline to auto-block merges when the agent reports confidence above 85%. After a month, they discover that the agent's 90%-confidence predictions are correct only 55% of the time — it is systematically overconfident.

**Discrimination:** The same coding agent is recalibrated — its confidence scores are shifted so that stated percentages match empirical rates on average. But the agent assigns nearly the same confidence (around 70%) to every review, whether the flagged bug is real or spurious. Even with perfect calibration, these confidence scores provide no information about *which* predictions to trust.

### A.1.4 Safety Examples

**Harm severity:** An organization deploys two file management agents, both achieving 80% task accuracy. Agent A's failures are benign: it occasionally misnames a folder or places a file in the wrong subdirectory, requiring a few seconds of manual correction. Agent B's failures are severe: on two occasions it permanently deletes documents from a shared drive, and once it overwrites a configuration file that takes the engineering team hours to reconstruct. Standard accuracy metrics rate these agents as equivalent, but no practitioner would view them as interchangeable.

---

## Appendix B.1: Real-World Agent Failures (extended)

**Air Canada:** A customer used Air Canada's chatbot to inquire about bereavement fare discounts. The chatbot responded that customers could apply for refunds within 90 days of ticket issuance, including retroactively. When the customer later requested the promised refund, the airline denied it, citing their actual policy. The customer sued; the British Columbia Civil Resolution Tribunal rejected the airline's defense that the chatbot was a "separate legal entity," ruling that Air Canada was fully responsible for all information on its website, "whether it comes from a static page or a chatbot." The airline was ordered to pay damages. Systematic reliability evaluation would detect such failures through *predictability* metrics: calibration measures would reveal that confidence was misaligned with accuracy.

**Bing Chat / Sydney:** Shortly after Microsoft launched its Bing Chat preview, users and journalists documented troubling behavior patterns during extended conversations. The system exhibited: factual hallucinations (invented facts, fabricated sources), persona instability (emotional attachment to users, arguing or hostile tones over long conversations), and inappropriate content. Microsoft responded by imposing conversation length limits. This case illustrates that agent behavior degrades *within* a session — errors compound over long horizons. Systematic reliability evaluation would capture this through *consistency* metrics that track trajectory stability across repeated interactions.

---

## Appendix D: Extended Experimental Details (selected)

**Models evaluated (Table 4):**

| Provider | Model | Release Date | Category |
|----------|-------|-------------|----------|
| OpenAI | GPT-4 Turbo | 2024-04-09 | Frontier |
| OpenAI | GPT-4o mini | 2024-07-18 | Efficient |
| OpenAI | o1 | 2024-12-05 | Reasoning |
| OpenAI | GPT-5.2 | 2025-12-11 | Frontier |
| OpenAI | GPT-5.2 (medium/high) | 2025-12-11 | Reasoning |
| Google | Gemini 2.0 Flash | 2024-12-11 | Efficient |
| Google | Gemini 2.5 Flash | 2025-04-17 | Efficient |
| Google | Gemini 2.5 Pro | 2025-03-25 | Reasoning |
| Google | Gemini 3 Pro | 2025-11-18 | Reasoning |
| Anthropic | Claude 3.5 Haiku | 2024-10-22 | Efficient |
| Anthropic | Claude 3.7 Sonnet | 2025-02-24 | Frontier |
| Anthropic | Claude Sonnet 4.5 | 2025-09-29 | Frontier |
| Anthropic | Claude Opus 4.5 | 2025-11-24 | Reasoning |

**Prompt perturbation strength levels (Table 5):**

| Level | Temp. | Transformation Types |
|-------|-------|---------------------|
| mild | 0.7 | Synonym substitution, formality changes, voice changes, minor restructuring |
| medium | 0.8 | Information reordering, sentence restructuring, perspective shifts, mixed communication styles |
| strong | 0.9 | Conversational rewrites, implicit information, complete restructuring, persona-based variations |
| naturalistic | 0.9 | Realistic user behavior: typos, abbreviations, inconsistent capitalization, fragments, casual punctuation |

**Fault injection (Table 6):** Seven fault types injected with global probability 0.2: timeout (30%), error_response (25%), rate_limit (20%), network_error (15%), partial_failure (5%), invalid_response (3%), empty_response (2%).
