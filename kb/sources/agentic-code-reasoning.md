---
description: Semi-formal reasoning templates (explicit premises, execution traces, formal conclusions) improve LLM code verification by 5-12pp across patch equivalence, fault localization, and code QA tasks
source: https://arxiv.org/html/2603.01896v2
captured: 2026-03-07
capture: web-fetch
type: academic-paper
---

# Agentic Code Reasoning

Author: Shubham Ugare, Satish Chandra

Source: https://arxiv.org/html/2603.01896v2
Date: March 4, 2026 (arXiv:2603.01896v2)
arXiv: 2603.01896 (cs.SE)
DOI: https://doi.org/10.48550/arXiv.2603.01896

## Abstract

Can LLM agents explore codebases and reason about code semantics without executing the code? We study this capability, which we call agentic code reasoning, and introduce semi-formal reasoning: a structured prompting methodology that requires agents to construct explicit premises, trace execution paths, and derive formal conclusions. Unlike unstructured chain-of-thought, semi-formal reasoning acts as a certificate: the agent cannot skip cases or make unsupported claims. We evaluate across three tasks (patch equivalence verification, fault localization, and code question answering) and show that semi-formal reasoning consistently improves accuracy on all of them. For patch equivalence, accuracy improves from 78% to 88% on curated examples and reaches 93% on real-world agent-generated patches, approaching the reliability needed for execution-free RL reward signals. For code question answering on RubberDuckBench rubberduckbench, semi-formal reasoning achieves 87% accuracy, a 9 percentage point gain over standard agentic reasoning. For fault localization on Defects4J just2014defects4j, semi-formal reasoning improves Top-5 accuracy by 5 percentage points over standard reasoning. These results demonstrate that structured agentic reasoning enables meaningful semantic code analysis without execution, opening practical applications in RL training pipelines, code review, and static program analysis.

## 1 Introduction

Can an LLM agent explore a codebase and determine whether two patches are semantically equivalent, without ever running them? We study this capability, which we call agentic code reasoning: an agent's ability to navigate files, trace dependencies, and gather context iteratively to perform deep semantic analysis without executing code. This capability is essential for tasks like bug detection, code review, and patch verification in complex repositories where relevant context spans multiple files. However, evaluating whether an agent's reasoning is correct presents a fundamental challenge: how do we establish ground truth for code understanding? And how do we ensure agents reason thoroughly rather than guess?

Recent work has explored execution-free verification for code agents. SWE-RM shum2025swerm trains reward models to approximate test outcomes, Agentic Rubrics raghavendra2025rubrics decompose verification into LLM-generated criteria, and CodeJudge tong2024codejudge uses LLMs directly as evaluators. However, these approaches use unstructured reasoning, allowing models to make claims about code behavior without explicit justification. At the other extreme, formal verification approaches translate code or reasoning into formal languages like Lean ye2025verinabenchmarkingverifiablecode; thakur2025clevercuratedbenchmarkformally, Coq kasibatla2025cobblestonedivideandconquerapproachautomating or Datalog sistla2025verifiedcodereasoningllms, enabling automated proof checking. But fully formal methods require formalizing language semantics, which is impractical for arbitrary repository code spanning multiple frameworks and languages. Sultan et al. sultan2026llmsversushaltingproblem highlight this gap: LLMs can predict program properties like termination with competitive accuracy, yet often fail to provide valid proofs. Moreover, existing approaches tend to be task-specific, requiring separate architectures or training for each problem domain.

We introduce semi-formal reasoning, a general approach that bridges this gap. Rather than training specialized models or formalizing semantics, we prompt agents with structured reasoning templates that require explicit evidence for each claim. These templates act as certificates: the agent must state premises, trace relevant code paths, and provide formal conclusions. The structured format naturally encourages interprocedural reasoning, as tracing program paths requires the agent to follow function calls rather than guess their behavior.

### Motivating Example.

Patch 1: return format(self.data.year, "04d")[-2:] Patch 2: return '%02d' % (self.data.year % 100)

We evaluate these techniques on three tasks that test different aspects of code reasoning. Our primary focus is patch equivalence verification: given two patches addressing the same specification, do they produce the same test outcomes? This task provides rigorous ground truth through test execution without requiring expensive human annotation. We additionally evaluate on code question answering (RubberDuckBench) and fault localization (Defects4J), which test nuanced semantic understanding and bug finding respectively. Patch equivalence and fault localization benefit from robust, objective ground truth (test execution outcomes and known buggy lines, respectively), while code question answering relies on expert-written rubrics evaluated by LLM graders.

### Contributions.

- We demonstrate that semi-formal structured reasoning consistently improves agentic code reasoning across three diverse tasks.
- For patch equivalence on curated challenging examples, we improve accuracy from 78% (standard reasoning) to 88% (semi-formal), a 10 percentage point gain.
- For patch equivalence on real-world agent-generated patches with test specifications, we achieve 93% verification accuracy with Opus-4.5, compared to 86% for single-shot and 73% for difflib-based similarity. This enables execution-free feedback for RL training pipelines.
- For code question answering on RubberDuckBench rubberduckbench, semi-formal reasoning achieves 87% accuracy with Opus-4.5, a 10.8 percentage point improvement over single-shot (76%) and 8.7 percentage points over standard agentic reasoning.
- For fault localization on Defects4J just2014defects4j, semi-formal reasoning improves Top-5 accuracy by 5-12 percentage points over standard agentic reasoning.

These results demonstrate that LLM agents can perform meaningful semantic code analysis without execution, potentially reducing verification costs in RL training pipelines by avoiding expensive sandbox execution. More broadly, structured agentic reasoning may offer a flexible alternative to classical static analysis tools: rather than encoding analysis logic in specialized algorithms, we can prompt LLM agents with task-specific reasoning templates that generalize across languages and frameworks.

### Data Contamination.

SWE-bench instances may appear in LLM training corpora, which could inflate absolute performance numbers. However, our primary conclusions are based on relative comparisons (ablations across reasoning formats) using the same model, where contamination affects all configurations equally. Additionally, our agentic setup requires the model to actively explore repository code at runtime rather than recall memorized solutions.

## 2 Background

We describe our experimental setup and define the three evaluation tasks.

### 2.1 Agentic vs. Single-Shot Verification

We distinguish between single-shot verification, where the model reasons from a static code snapshot, and agentic verification, where the model can actively explore the repository. Our work focuses on agentic verification using a minimal SWE-agent yang2024sweagent setup with access to bash tools. We set the maximum number of steps to 100 in all experiments. This allows the verifier to navigate the codebase, trace dependencies, and gather context that would otherwise be unavailable in a single-shot setting. Crucially, the agent cannot execute repository code or run its test suite: dependencies are not installed and the environment is not sandboxed. The agent may run independent Python scripts to probe general language behavior (e.g., how regex handles edge cases), but its primary mode of analysis is static. Git commands are also disabled to prevent investigating commit history.

### 2.2 Patch Equivalence

True semantic equivalence (determining whether two programs produce identical behavior for all valid inputs) is undecidable in the general case. Real-world code often lacks formal specifications, and developers may hold latent assumptions (e.g., a field self.year: int should only contain positive integers) that LLMs must infer from context. To make this problem tractable, we focus on patch equivalence: given two patches (code diffs that modify a repository) addressing the same task specification, do they produce the same test outcomes? Patches are well-suited for this study because they come with shared specifications (the problem statement) and associated test suites that define expected behavior.

Two patches are equivalent modulo tests if and only if executing the repository's test suite (F2P ∪ ∪ P2P) produces identical pass/fail outcomes for both patches.

### 2.3 Defects4J for Fault Localization

Defects4J just2014defects4j is a collection of reproducible bugs from real-world Java projects, widely used for evaluating fault localization and program repair techniques. Each bug includes the buggy and fixed versions of the code, along with at least one failing test that exposes the bug. For fault localization, the task is to identify the exact lines of buggy code given only the failing test, without access to stack traces, error messages, or execution information. Evaluation measures Top-N accuracy: the percentage of bugs where all ground-truth buggy lines are covered within the top N predictions.

### 2.4 Code Question Answering

RubberDuckBench rubberduckbench is a benchmark of 15 code understanding questions across Python, Java, and C++ repositories, each with expert-written rubrics for evaluation. The questions require nuanced understanding of code behavior, including project-specific logic, library semantics, and edge cases. Unlike patch equivalence where ground truth is determined by test execution, code QA requires free-form answers that are evaluated against expert rubrics.

## 3 Semi-formal Reasoning

Given our evaluation tasks, we consider how the verifier should structure its reasoning. Recent work achim2025aristotleimolevelautomatedtheorem; olympiaddeepmind; yang2025position on LLM-based mathematical reasoning has shown that semi-formal approaches, which combine natural language intuition with structured logical steps, often outperform both purely informal and fully formal methods. Fully formal verification in Lean or Coq is tempting but introduces significant overhead: translating arbitrary repository code into a formal representation is nontrivial, and current LLMs still struggle with the precise syntax and proof tactics these systems demand. We therefore compare two reasoning approaches that introduce increasing structure in the agent's reasoning through templates provided in the prompt.

### Standard Reasoning

The agent receives a minimal prompt asking it to determine equivalence, with no structural constraints on its reasoning. It explains its thinking in natural language and concludes with YES/NO. This is fast but allows the agent to make claims without verifying them. For example, an agent might note that one patch modifies extra files but simply assume no tests depend on those changes.

### Semi-formal Reasoning

Semi-formal reasoning adds structure: the agent must state explicit premises, trace execution for each test, and write a formal conclusion. In practice, we enforce this by including a structured template in the agent's initial prompt that specifies the required format. The key insight is that by structuring the reasoning process, not just the output format, we force the agent to gather evidence before concluding, preventing the premature judgments common in unconstrained reasoning. We observed that this forces the agent to actually enumerate the program paths rather than make guesses, which naturally leads to deeper interprocedural reasoning as the agent traces function calls to justify its claims. For instance, in one example (django-13195), semi-formal reasoning caught that session-related tests existed and would fail when one patch omitted changes to the session middleware, something the informal mode missed. Figure 1 illustrates this with a concrete example where tracing a function call reveals a shadowed definition that causes one patch to fail.

The certificate template is task-specific: for patch equivalence, premises describe what each patch modifies and claims trace per-test behavior; for fault localization, premises describe suspicious code regions and claims trace whether each region could cause the observed test failure; for code question answering, the template requires a function trace table, data flow analysis, and semantic properties with explicit evidence. While the specific sections vary by task, all templates enforce the same principle: the agent must document verifiable evidence before reaching a conclusion. Figure 2 shows a condensed example for patch equivalence.

## 4 Evaluation

We present our experimental results on the three evaluation tasks: patch equivalence verification, code question answering, and fault localization.

### 4.1 Patch Equivalence

### 4.1.1 Curated Dataset Evaluation

We construct a challenging evaluation dataset as follows. A uniformly sampled dataset would be dominated by easily distinguishable patch pairs, offering limited signal for evaluating nuanced reasoning. To better stress-test the verifier, we deliberately curate a more challenging distribution that emphasizes subtle distinctions. We source patches from SWE-bench-Verified, drawing on the community-contributed collection of agent traces, generated patches, and test execution results. From this repository, we sample pairs of patches produced by different agents for the same underlying bug.

Our curation pipeline proceeds as follows. We first score each pair's surface-level similarity using both an LLM-based rating (0 to 10 scale) and difflib-based text similarity. We then exclude pairs with invalid test outcomes. Finally, we balance the dataset to include both high-similarity pairs where patches appear similar (LLM score ≥ \geq 7, difflib > > 0.3) yet differ in resolution status, and positive pairs where both patches pass all tests. The resulting dataset contains 170 challenging examples designed to probe the boundary between superficial code similarity and true semantic equivalence.

Evaluating whether an agent's reasoning is correct step-by-step is difficult as it requires expert review. Hence, in our evaluation we only focus on the final binary answer. Given two patches and a test suite, does the agent correctly predict whether both patches produce the same test outcomes? This is a binary task, and a random baseline achieves 50% accuracy. We acknowledge that an agent might sometimes arrive at the right answer through flawed reasoning, but the structured formats we introduce next are designed to reduce this by requiring explicit evidence for each claim.

For the experiments in this section the verifier has access to (1) both code patches, (2) the test patch applied to the codebase, and (3) the full repository. The verifier cannot execute tests but can read test implementations.

Semi-formal reasoning reduces errors by nearly half, improving overall accuracy from 78.2% to 88.8% and performing well on both equivalent and non-equivalent cases. This yields a roughly 10-point improvement over informal reasoning but requires about 2.8 × \times as many steps. Even with semi-formal analysis, 19 cases are incorrect. The primary issue (roughly half) is missed execution differences in non-equivalent cases. The agent claims the patches are equivalent when only one actually passes the tests. This typically happens because the agent fails to trace all relevant code paths or misses some assertions in tests.

### 4.1.2 LLM Verifier With Test Specifications

One practical use of patch equivalence is checking whether an LLM-generated patch matches a known reference solution i.e. the gold patch. If we can do this without actually running tests, we get much cheaper feedback for training pipelines. We could avoid the overhead of setting up the execution environment which involves running sandboxes or CI systems for each repository.

The verifier has access to (1) the generated patch, (2) the reference (gold) patch, (3) the test patch applied to the codebase (i.e., F2P test code is visible), and (4) the full repository including all P2P tests. Ground truth is determined by actual test execution.

- We tested this by comparing patches from live-swe-agent (gemini-3-pro) against the correct patches from SWE-bench-Verified dataset. Unlike the curated dataset in the previous section, here we sample randomly: we selected a balanced dataset of 200 examples, evenly split between correct and incorrect patches (100 each). The verifier's task is to check if the agent's patch is equivalent to the reference solution. We evaluate the following verification modes:
- difflib (No LLM): Recent work from SWE-RL wei2025swerl used the Python difflib library to compute a similarity score as the RL reward. For binary classification, one could set a threshold on this score, above which patches are considered equivalent. We evaluated various threshold values on the test set and found that a threshold of 0.4 yields the maximum accuracy. However, note that this optimal threshold may not be known a priori for a given benchmark. We present this value here in the table for reference.
- Single LLM Call: One LLM call with just the problem statement and patches. No tool use or codebase exploration.
- Single LLM Call + File Context: Same as above, but the prompt includes the full contents of all files modified by the patches.
- Agentic: The verifier explores the codebase using tools over multiple steps, reasoning from the problem description and existing code. We evaluate both standard reasoning and semi-formal reasoning formats. In all settings, accuracy is computed against actual test execution results.

Agentic: The verifier explores the codebase using tools over multiple steps, reasoning from the problem description and existing code. We evaluate both standard reasoning and semi-formal reasoning formats.

Opus-4.5 achieves 93.0% accuracy with semi-formal reasoning when given the fail-to-pass test patch. The single-call modes (80-87% accuracy) confirm that many verification tasks require exploring code beyond the immediate patch context.

Error Analysis for Verifier With Tests. We closely analyzed the remaining errors for Opus-4.5 with Semi-formal and found three primary failure modes: 1. Incomplete execution tracing despite the given instructions: The agent assumed function behavior without fully tracing concrete execution paths. 2. Third-party library semantics: The agent guessed behavior from function names when source code was unavailable. 3. Dismissing subtle differences: The agent identified semantic differences but incorrectly concluded they were irrelevant to test outcomes. While these results demonstrate strong verification performance when fail-to-pass test patches are available, this dependency limits applicability to scenarios without well-defined test patches. In the following section, we explore extending our approach to scenarios where test patches are unavailable.

Incomplete execution tracing despite the given instructions: The agent assumed function behavior without fully tracing concrete execution paths.

Third-party library semantics: The agent guessed behavior from function names when source code was unavailable.

Dismissing subtle differences: The agent identified semantic differences but incorrectly concluded they were irrelevant to test outcomes.

### 4.2 Fault Localization

We evaluate fault localization on Defects4J (see Section 2 ). Unlike patch equivalence where both patches are provided, fault localization requires the agent to find the relevant code in a large search space, then reason about why it causes the test failure. Appendix B shows the prompt we use for structured reasoning.

### Metric

For matching, we compare overlaps against buggy file regions: the lines in the patch, grouped per hunk into (file, min_deleted, max_deleted) ranges for deletions, and (file, insert_pos, insert_pos) for insertions. A prediction matches a region if their ranges overlap: pred_start ≤ \leq region_end and pred_end ≥ \geq region_start. This works for all patch types including deletion-only cases, which can be an issue with matching based on line number in the ground truth patch. We report two variants: All, where a bug is solved at Top-N only when every ground-truth hunk is covered by predictions in positions 1..N, and Any, where at least one ground-truth hunk must be covered. The All metric is stricter and penalizes multi-hunk bugs; the Any metric better reflects partial localization success.

### Available Information.

The agent has access to (1) the failing test name and source code, (2) source files scoped to classes loaded during test execution, and (3) the full repository. No stack traces, error messages, or execution information are provided (to avoid trivializing the task).

### Small-Scale Evaluation (50 bugs).

We first evaluate on 50 bugs from Defects4J where all relevant source files fit within the context window, enabling comparison between single-shot (all code provided upfront) and agentic (iterative file exploration) modes. We do this by estimating the token count in loaded classes and cap it to 100K. These projects contained 43 unique bugs that were evaluable; others had missing source or test files, or other errors.

Semi-formal reasoning improves accuracy across both metrics and exploration modes. Under the stricter All metric, Top-5 accuracy improves by +8pp for single-shot and +12pp for agentic. Under the Any metric, the gains are similar: +8pp for single-shot and +7pp for agentic. Agentic exploration with semi-formal reasoning achieves the best overall accuracy at 72.1% Top-5 (All) and 88.4% Top-5 (Any).

### Larger-Scale Validation (100 bugs).

To validate our findings on a larger sample, we evaluated on 100 Defects4J bugs randomly sampled across 14 Java projects (of which 90 were evaluable). Unlike the small-scale study, many of these bugs involve source files exceeding context limits, requiring genuine agentic exploration. Standard mode sometimes makes a quick, correct prediction on turn 1 from just the test code (e.g., Closure_129, where the agent predicts correctly from the test code alone without reading any source files).

### Error Analysis.

We analyzed failures for Opus-4.5 with semi-formal reasoning and identified four primary failure modes: 1. Indirection bugs: The bug is in a class not directly invoked by the test. For example, in Csv_12, the test calls CSVParser.parse() but the bug is in CSVFormat.withHeader() -a configuration class the model consistently overlooks. 2. Multi-file bugs: Bugs spanning multiple files require identifying all locations. Large ground-truth sets (5+ lines across 2+ files) are systematically harder. 3. Domain-specific bugs: Algorithmic bugs requiring specialized knowledge, such as numerical analysis issues in Math_81 (EigenDecomposition), exceed the model's domain expertise. 4. More than 5 fix regions: In a few cases (5/90), the number of distinct regions of changes in the ground truth was more than 5, which will result in a miss by our metric.

Indirection bugs: The bug is in a class not directly invoked by the test. For example, in Csv_12, the test calls CSVParser.parse() but the bug is in CSVFormat.withHeader() -a configuration class the model consistently overlooks.

Multi-file bugs: Bugs spanning multiple files require identifying all locations. Large ground-truth sets (5+ lines across 2+ files) are systematically harder.

Domain-specific bugs: Algorithmic bugs requiring specialized knowledge, such as numerical analysis issues in Math_81 (EigenDecomposition), exceed the model's domain expertise.

More than 5 fix regions: In a few cases (5/90), the number of distinct regions of changes in the ground truth was more than 5, which will result in a miss by our metric.

Appendix C gives a walkthrough of how semi-formal reasoning helps in the case of mockito_8.

### 4.3 Code Question Answering

We evaluate code question answering on RubberDuckBench (see Section 2 ).

### Available Information.

In single-shot mode, the agent receives only the function containing the code in question (approximately 20-50 lines of context). In agentic mode, the agent can explore the full repository using bash tools to read files, search for definitions, and trace dependencies.

### Evaluation.

Since code QA requires nuanced assessment, we use multi-model LLM grading with rubric-based evaluation. Each answer is graded independently by Gemini-3-Pro and GPT-5.2 against the expert rubric, with weighted averaging to handle disagreements. The graders achieved 85% agreement across all evaluations, indicating consistent assessment.

### Reasoning Modes.

- We evaluate two reasoning approaches:
- Standard: Simple prompt asking for a code-grounded answer.
- Semi-formal: Structured output template requiring function trace tables, data flow analysis, and explicit evidence citations.

The results reveal that structured semi-formal reasoning provides substantial gains: Opus improves from 78.3% (standard agentic) to 87.0% with the semi-formal template (+8.7pp). For Sonnet, standard agentic reasoning already achieves 85.3%, and the semi-formal template does not yield further gains (84.8%), suggesting that the benefit of structured reasoning varies by model capability and may plateau when the base model is already strong. For Opus, the structured template forces the agent to document evidence systematically before answering, correcting its tendency to guess based on function names.

The structured template requires the agent to fill in a function trace table (listing every function examined with file:line locations and verified behavior), data flow analysis (tracing how key variables flow through the code), semantic properties with explicit evidence, and an alternative hypothesis check. This structured format reduces the tendency to guess based on function names, a common failure mode we observed in unstructured reasoning.

### Error Analysis.

The structured template forces the agent to document evidence systematically before reaching conclusions. For example, on a question about whether two API calls differ (cpp_3), standard reasoning stated "it provides proper error handling if an invalid key is somehow passed"-implying edge cases could occur. The semi-formal template required tracing both the map initialization and variable assignments, revealing they use the same enum values, thus proving invalid keys are impossible. This explicit verification step eliminated a deduction that standard reasoning incurred. Conversely, semi-formal reasoning can fail when agents construct elaborate but incomplete reasoning chains: on py_5, the agent thoroughly traced five functions but missed that downstream code already handled the edge case it identified, leading to a confident but wrong answer. See Appendix D for detailed examples with full reasoning traces.

## 5 Related Work

### LLM-Based Software Engineering Agents.

The emergence of LLM-based coding agents has transformed automated software engineering. SWE-agent yang2024sweagent introduced an agent-computer interface that enables LLMs to interact with codebases through specialized commands, achieving strong results on SWE-bench jimenez2024swebench. OpenHands wang2024openhands provides an open platform for building software development agents. Agentless xia2024agentless takes a different approach, decomposing bug fixing into localization and repair phases without persistent agent state. These systems rely on test execution for validation, which our work aims to reduce through semantic code reasoning.

### Execution-Free Verification for Code.

Most closely related to our work are recent approaches to verifying code without execution. SWE-RM shum2025swerm trains a reward model to provide execution-free feedback for software engineering agents, showing that learned verifiers can approximate test outcomes. Agentic Rubrics raghavendra2025rubrics propose using LLM-generated rubrics as contextual verifiers, decomposing verification into interpretable criteria. CodeJudge tong2024codejudge explores LLM-as-a-judge for evaluating generated code quality. Our approach differs by emphasizing structured semi-formal reasoning to improve verification accuracy, achieving 93% accuracy on real-world patches.

### LLM-Based Fault Localization and Code Understanding.

Beyond patch verification, agentic code reasoning encompasses fault localization and code understanding. AgentFL qin2024agentfl uses LLM agents for project-level fault localization, while FlexFL xu2025flexflflexibleeffectivefault demonstrates effective fault localization with open-source LLMs. For repository-level code understanding, CodePlan bairi2024codeplan combines LLMs with planning for multi-step repository edits. RubberDuckBench rubberduckbench provides a benchmark for evaluating AI coding assistants on code understanding tasks, measuring how well LLMs can answer questions about codebases. These works highlight the broader applicability of agentic reasoning for code analysis tasks beyond verification.

### Program Equivalence and Formal Verification.

Program equivalence is a fundamental problem in computer science, known to be undecidable in the general case rice1953classes. Traditional approaches rely on formal methods such as translation validation pnueli1998translation and equivalence checking necula2000translation. Recent work has explored using LLMs for formal verification first2023baldur, though translating arbitrary code to formal specifications remains challenging. EquiBench wei-etal-2025-equibench benchmarks LLM reasoning about program equivalence across several transformation types, but focuses on small self-contained code pairs rather than repository-level patches with test suites. Sultan et al. sultan2026llmsversushaltingproblem show that LLMs can predict program termination with surprising accuracy, ranking competitively with specialized tools on SV-Comp benchmarks, though they often fail to provide valid proofs.

A complementary line of work focuses on post-hoc verification of LLM reasoning sistla2025verifiedcodereasoningllms, translating LLM responses into Datalog facts and using static analysis to verify reasoning steps, successfully validating judgments on uninitialized variable errors and catching incorrect equivalence judgments. Our approach differs in focusing on the "input side": improving what the agent is asked to do through structured semi-formal reasoning, rather than post-facto output verification. The semi-formal certificates we require are designed to be easier to manually validate than examining full agent trajectories, though they lack the automated checkability of fully formal approaches. These approaches are complementary: structured reasoning improves agent thoroughness during analysis, while formal verification can provide additional guarantees on outputs.

### LLM Reasoning and Chain-of-Thought.

Our semi-formal reasoning approach builds on work showing that structured reasoning improves LLM performance. Chain-of-thought prompting wei2022chain demonstrated that intermediate reasoning steps improve mathematical problem solving. ReAct yao2023react combines reasoning with action for agent tasks. CodeAct wang2024codeact shows that executable code actions improve agent performance. We extend these ideas to code reasoning, showing that task-specific structured templates (requiring premises, execution traces, and formal conclusions) improve semantic verification accuracy by up to 11 percentage points.

### Training and Scaling SWE Agents.

Recent work has focused on training pipelines for software engineering agents. SWE-Gym pan2024swegym provides a training environment with 2,438 real-world Python tasks, enabling both agent and verifier training through reinforcement learning. R2E-Gym jain2025r2egym scales this further with procedural environment generation and hybrid verifiers combining execution-based and LLM-based feedback, training agents on 89K instances. SWE-RL wei2025swerl advances reasoning capabilities through reinforcement learning on open software evolution, using difflib-based similarity as a reward signal. Our work complements these efforts by providing execution-free verification that could reduce the computational cost of RL training.

## 6 Conclusion and Future Work

- We studied agentic code reasoning across three tasks: patch equivalence verification, code question answering, and fault localization. Our key findings include:
- Semi-formal structured reasoning consistently improves agentic code reasoning across all three tasks, with gains of 5-12 percentage points over standard agentic baselines.
- For patch equivalence, we achieve 93% verification accuracy on real-world patches, a 7 percentage point improvement over single-shot baselines, enabling execution-free feedback for RL training pipelines.
- For code question answering, semi-formal reasoning achieves 87% accuracy on RubberDuckBench, a 9 percentage point gain over standard agentic reasoning.
- For fault localization on Defects4J, semi-formal reasoning consistently improves accuracy over standard reasoning, with gains of up to 12 percentage points on fit-in-context bugs and 5 percentage points on a larger 90-bug evaluation. These results demonstrate that LLM agents can perform meaningful semantic code analysis without execution. Structured reasoning templates offer a complementary approach to classical static analysis: rather than encoding analysis logic in specialized algorithms, we can prompt agents with task-specific formats that generalize across languages and frameworks, though without the formal guarantees of traditional tools.

For fault localization on Defects4J, semi-formal reasoning consistently improves accuracy over standard reasoning, with gains of up to 12 percentage points on fit-in-context bugs and 5 percentage points on a larger 90-bug evaluation.

- Several directions for future work emerge:
- Post-training for code reasoning: Fine-tuning models to internalize the semi-formal template structure could further improve accuracy while potentially eliminating the prompt overhead.
- Extending to other static analysis tasks: The semi-formal reasoning approach could be applied to other code analysis tasks such as security vulnerability detection, code smell identification, and API misuse detection.
- Hybrid verification: Combining LLM-based reasoning with lightweight formal methods or symbolic execution could provide stronger guarantees while maintaining flexibility.
