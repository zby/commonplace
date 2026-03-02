---
source: https://arxiv.org/pdf/2510.21413
captured: 2026-03-02
capture: pdf-read
type: academic-paper
---

# Context Engineering for AI Agents in Open-Source Software

Author: Seyedmoein Mohsenimofidi, Matthias Galster, Christoph Treude, Sebastian Baltes
Source: https://arxiv.org/pdf/2510.21413
Date: 5 Feb 2026

## Abstract

GenAI-based coding assistants have disrupted software development. The next generation of these tools is agent-based, operating with more autonomy and potentially without human oversight. Like human developers, AI agents require contextual information to develop solutions that are in line with the standards, policies, and workflows of the software projects they operate in. Vendors of popular agentic tools (e.g., Claude Code) recommend maintaining version-controlled Markdown files that describe aspects such as the project structure, code style, or building and testing. The content of these files is then automatically added to each prompt. Recently, AGENTS.md has emerged as a potential standard that consolidates existing tool-specific formats. However, little is known about whether and how developers adopt this format. Therefore, in this paper, we present the results of a preliminary study investigating the adoption of AI context files in 466 open-source software projects. We analyze the information that developers provide in AGENTS.md files, how they present that information, and how the files evolve over time. Our findings indicate that there is no established content structure yet and that there is a lot of variation in terms of how context is provided (descriptive, prescriptive, prohibitive, explanatory, conditional). Our commit-level analysis provides first insights into the evolution of the provided context. AI context files provide a unique opportunity to study real-world context engineering. In particular, we see great potential in studying which structural or presentational modifications can positively affect the quality of the generated content.

**Keywords:** Software Engineering, Generative AI, AI Agents, Open Source

**ACM Reference Format:** Seyedmoein Mohsenimofidi, Matthias Galster, Christoph Treude, and Sebastian Baltes. 2026. Context Engineering for AI Agents in Open-Source Software. In *23rd International Conference on Mining Software Repositories (MSR '26), April 13–14, 2026, Rio de Janeiro, Brazil.* ACM, New York, NY, USA, 5 pages. https://doi.org/10.1145/3793302.3793350

## 1 Introduction

The launches of GitHub Copilot in 2021 and ChatGPT in 2022 have started to transform how software is developed. Today, generative AI (GenAI) tools built around large language models (LLMs) support software engineers throughout the software development lifecycle (SDLC)—although most published work focuses on code and test generation. The *Devin AI* demo published in March 2024 fueled the first hype around agent-based software development, but it took until 2025 for agent-based software development to reach considerable adoption. In February 2025, Anthropic released *Claude Code*, a "command line tool for agentic coding", which represents a further step toward more autonomous AI-assisted software development, enabling developers to assign coding tasks to AI agents via a terminal interface. Human oversight is still built-in, but can be turned off by the developer. This brings GenAI assistants closer to the inherent meaning of an *agent* that operates autonomously, adapts to change, and creates and pursues goals (from the Latin 'agere', 'to do' in English).

*Context engineering* is the deliberate process of designing, structuring, and providing task-relevant information to LLMs. While *prompt engineering* focuses on how a task is described to the model (e.g., instructions and output indicators), context engineering focuses on what task-relevant information the model has access to, including relevant guidelines, configuration files, documentation, and exemplary code snippets. An advantage of agent-based tools compared to conversational tools is that they allow persistent, structured, and task-specific context to be provided in a more fine-grained and targeted manner. One way to "engineer" context is to add machine-readable AI context files to source code repositories. The AI agents then automatically add the content of these files to their prompts. While traditional README files are written for humans, AI context files are explicitly designed for AI agents, providing a central machine-readable source of contextual information. Their content can include everything from the required terminal commands to build and test the project over documentation links, common workflows, coding conventions, to instructions for creating pull requests.

AGENTS.md was introduced as an open tool-agnostic convention for such AI context files, and it was recently announced as a project in the Agentic AI Foundation. OpenAI's Codex tool relies on this format, while Claude Code by default searches for a file named CLAUDE.md. Anthropic's best-practice guide recommends teams to put that file into version control so that all team members benefit from consistent AI behavior. GitHub introduced a similar AI context file for Copilot named copilot-instructions.md.

Since prompts are only rarely preserved after content has been generated, AI context files offer a unique opportunity to study how developers customize AI agents to their needs, what information they consider relevant to include, how they present it, and how instructions and contextual descriptions evolve. This paper presents the first holistic empirical study that analyzes context files used to guide different AI agents in open-source software (OSS) projects. The research questions addressed are:

- **RQ1** How widely have OSS projects adopted AI context files?
- **RQ2** What information do open-source developers provide in AI context files and how do they present it?
- **RQ3** How do AI context files evolve over time?

An initial search in October 2025 suggested that tens of thousands of GitHub repositories already contained AI context files. However, there was no systematic analysis focusing on "engineered" software projects. This paper provides a first step toward filling this gap by mining GitHub repositories to study how AI context files are adopted, structured, and maintained, with the overarching goal of understanding how software teams engage in context engineering in practice. The results of our preliminary study are based on data collected from 10,000 GitHub repositories (RQ1). For RQ2 and RQ3, a detailed qualitative analysis of relevant repository data was performed, including file content, commits, and issues.

## 2 Related Work

Agentic GenAI tools promise to introduce autonomous decision-making and proactive problem-solving along the SDLC. Advances in LLMs, reinforcement learning, and multi-agent frameworks enabled the implementation of software agents that go beyond simple prompt-response interactions. One of the first agent-based software development tools was *Devin AI*, which allowed agents to search the web, edit files, and execute commands to complete tasks iteratively and independently. In the academic community, *SWE-agent* allowed LLM-based agents to communicate with the repository environment by reading, modifying, and executing bash commands. Another example is *AutoCodeRover*, which enabled AI agents to access code search APIs to help them find methods within specific classes for bug location identification.

Although context plays a critical role in guiding autonomous agents, prompts are typically treated as temporary artifacts and are rarely preserved or reused. This lack of prompt management limits reproducibility and underscores the need for making context and prompt information explicit and manageable by using versioned AI context files. Recently, researchers have started investigating AI context files as novel software artifacts. However, a holistic analysis across tools and formats has not been published yet.

## 3 Data Collection

AI context files were collected from OSS projects on GitHub. The starting point was the SEART GitHub search tool. Non-fork repositories were selected that have at least two contributors, have a license, and were created before 1st January 2024 with commits since 1st June 2024. Archived, disabled, or locked repositories were excluded, resulting in a first sample of 228,890 repositories. Repositories with an OSI-compliant open-source license were then selected and those with licenses not intended for software or with low adoption (used in fewer than 261 repositories) were manually filtered out. The focus was on the ten most popular languages (Python, TypeScript, JavaScript, Go, Java, C++, Rust, PHP, C#, and C) and excluded repositories with fewer than 271 commits (median) or fewer than 7 watchers (median). This resulted in a final sample of 48,795 repositories. From these, 10,000 repositories were selected based on a ranking approach that balances popularity (#stars, #watchers, #contributors) and maturity (#commits to default branch, project age, LOC).

These repositories were cloned and their default branch was scanned to find all types of context files that GitHub Copilot supports: Copilot instructions, CLAUDE.md, AGENTS.md, and GEMINI.md. Non-English and non-software projects were manually excluded. For RQ2 and RQ3, the focus was on AGENTS.md as the open tool-agnostic convention. The data collection and analysis scripts and the analyzed data are available online.

## 4 Results

### 4.1 Adoption (RQ1)

Only 466 (5%) of the repositories scanned had already adopted at least one of the formats considered, reflecting that this is still an early stage of adoption. One limitation is the focus on four selected tools.

Breakdown by file type:
- Copilot Instructions: 218 repos
- CLAUDE.md: 181 repos
- AGENTS.md: 118 repos
- GEMINI.md: 29 repos
- (Union: 466 repos)

The distribution of languages was roughly aligned with the languages' general representation in the sample, although Go was slightly overrepresented. AI context files were found in 135 repositories with TypeScript as main language, 58 Go, 58 Python, 56 C#, 36 Java, 34 JavaScript, 32 C++, 29 Rust, 19 PHP, and 9 C. Certain file types were more prevalent in certain programming languages. C#, for example, had a strong focus on Copilot, while Claude Code was very popular for TypeScript. The most commonly co-occurred pair was (AGENTS.md, CLAUDE.md) found in 25 repositories.

### 4.2 Information and Structure (RQ2)

Copilot instruction files were on average the longest (M = 310 lines, SD = 127 lines), followed by CLAUDE.md files (M = 287, SD = 112); GEMINI.md files were the shortest (M = 106, SD = 65). AGENTS.md files had the highest variation in file length (M = 142, SD = 231).

To answer RQ2, the section headings from the 155 AGENTS.md files in the sample were extracted, converted to lower case, removed special characters, and lemmatized to group semantically equivalent variations. 15 AGENTS.md files created before 1st January 2025 were excluded (before the AGENTS.md convention was introduced). For each lemmatized heading, the following were determined: (1) how many distinct repositories it occurred (#files > #repositories), (2) in how many distinct files it occurred (#files > #repositories), and (3) how many total occurrences it had. Five repositories that contained AGENTS.md files without any heading structure were excluded.

**Table 1: Categories of information provided in AGENTS.md files**

| Category | Description | # |
|---|---|---|
| Conventions | Outlines coding standards, naming/formatting conventions, and best practices for writing consistent and maintainable code. | 50 |
| Contribution guidelines | Provides instructions for contributing to the repository, such as branching, code reviews, or CI requirements. | 48 |
| Architecture/structure | Describes how the project or repository is organized, including key directories, modules, components, and relationships between them. | 47 |
| Build commands | Lists commands for building, running, or deploying. | 40 |
| Goals/purposes | Summarizes what the project or agent does, its goals or purposes, and high-level functionality or capabilities. | 32 |
| Test execution | Explains how to execute test suites or individual tests, including tools, commands, and environments. | 32 |
| Metadata | Contains file metadata or configuration (e.g., tags). | 29 |
| Test strategy | Describes the overall approach to testing (unit, integration, end-to-end), test organization, or principles guiding test coverage and design. | 24 |
| Tech stack | Lists programming languages, libraries, frameworks, or other dependencies used in the project. | 15 |
| Setup | Covers installation prerequisites, environment setup, and initial steps required to run/use the project locally. | 11 |
| References | Provides a concise list of frequently used commands, API references, or quick tips for developers or users. | 9 |
| Troubleshooting | Offers guidance for diagnosing and resolving common errors, failures, or configuration problems encountered during development or deployment. | 8 |
| Patterns/examples | Shows reusable patterns, sample agent configs, or example use cases to guide understanding or extensions. | 8 |
| Security | Highlights security-related advice, configurations, or precautions (e.g., managing secrets or access controls). | 6 |

Differences were also noticed in writing style when analyzing the files. All 50 sections labeled Conventions were analyzed, the most common category in the dataset. The writing style can be characterized along five stylistic dimensions:

- **Descriptive**: documenting existing conventions without giving explicit instructions, e.g., "This project uses the Linux Kernel Style Guideline." Such statements summarize current practices or configurations that the AI agent should be aware of, rather than prescribing behavior.
- **Prescriptive**: written as direct imperatives that instruct how to act, e.g., "Follow the existing code style and conventions." This style provides explicit behavioral rules and was often formatted as concise bullet points.
- **Prohibitive**: explicitly indicating what not to do, e.g., "Never commit directly to the main branch." These prohibitions set boundaries and clarify the constraints that AI agents should respect.
- **Explanatory**: short explanations added after the rules, e.g., "Avoid hard-coded waits to prevent timing issues in CI environments." Here, the justification provides context for why a convention exists.
- **Conditional**: formulations that specify what to do in certain situations, e.g., "If you need to use reflection, use ReflectionUtils APIs." This style encodes situational logic, specifying conditional actions that depend on the context of the agent's task.

In summary, AGENTS.md files vary widely both in the information they contain and how they are presented, yet some recurring patterns are emerging. Projects often document architecture, contribution processes, and coding conventions, but without a consistent structure. Stylistic choices range from descriptive to directive, reflecting experimentation with how best to communicate expectations to AI agents.

### 4.3 Evolution (RQ3)

The commit histories of all 155 AGENTS.md files were analyzed. 77 (50%) of them had not been changed, 36 (23%) only once, and 32 (21%) between two and seven times. For this study, the types of changes developers make in AI context files were examined. The focus was on the 10 files (6%) with at least 10 commits, which yielded a sample of 169 commits to annotate (37% of all collected commits). The resulting modification patterns varied per file, with some histories spanning a short period with many changes (e.g., neomjs/neo: 49 changes over 19 days) and others spanning longer periods with fewer changes (e.g., gofiber/fiber: 11 changes, 148 days).

**Table 2: Categories of changes for AGENTS.md files with >= 10 commits**

| Category | Description | # |
|---|---|---|
| Add instruction(s) | Add instruction line(s) to existing sections. | 78 |
| Modify instruction(s) | Modify instruction line(s) within a section (ignoring typo fixes and references additions). | 59 |
| Add section(s) | Add new section(s) to the AGENTS.md file. | 26 |
| Remove instruction(s) | Remove line(s) with instructions from existing sections. | 23 |
| Modify heading(s) | Modify existing section heading title or level. | 23 |
| Modify text | Minor changes to content of AGENTS.md file, such as fixing typos. | 19 |
| Reformat style | Changing visual appearance of content in AGENTS.md file (not related to structure). | 10 |
| Remove section(s) | Remove sections from AGENTS.md file. | 2 |
| Update reference(s) | Update references, e.g., URLs. | 2 |

The most frequent change categories are 'Add instruction(s)' and 'Modify instruction(s)'. For all examined AGENTS.md files, these categories occurred as the first or second change in the history of changes. An interesting commit message found for AGENTS.md in rsyslog states "AI support: Agent shall no longer call stylecheck.sh". The related change category is 'Remove instruction(s)', because the change deleted an instruction. A commit in eclipse-rdf4j/rdf4j fixed a flaky test and updated the AGENTS.md file to handle flaky tests during test execution.

In summary, the evolution of the AGENTS.md files in the sample varies, and no clear patterns were identified in terms of when and how often changes occur. However, common change categories were identified. Based on these categories, it appears that changes are mostly made to fine-tune and adjust instructions.

## 5 Conclusion

In addition to README files for humans, OSS projects increasingly include AI context files for AI coding agents. In other words, software developers are now writing and maintaining documentation for machines. The results show that conventions for this new software artifact are still in flux. Projects differ widely in what they encode (e.g., conventions, architecture) and how they express it (e.g., prescriptive vs. prohibitive). These stylistic variations mirror different prompt writing practices. Thus, OSS repositories serve as natural laboratories for studying how developers experiment with "talking" to agent-based AI tools.

AI context files are maintained software artifacts. They are versioned, reviewed, quality-assured, and tested. Future work needs to evaluate how their content, structure, and style affect agent behavior and task performance, and how automated feedback loops could update or refine these files based on observed results. Research should also investigate the co-evolution of source code and related AI context files, similar to the co-evolution of source code and comments. Open questions include whether standard schemas could improve interoperability, whether repositories should maintain one or multiple AI context files, and how to coordinate instructions for multiple agents. Beyond technical considerations, this new form of documentation has the potential to reshape communication, review, and collaboration patterns in software teams as instructions move from being written for humans to being negotiated between humans and AI. The systematic study of AI context files has great potential to provide actionable recommendations to practitioners.
