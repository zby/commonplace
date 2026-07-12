---
source: https://arxiv.org/html/2504.15965v2
description: Survey proposing a 3D-8Q taxonomy (object/form/time) for LLM memory mechanisms, mapping human memory types (sensory, working, explicit, implicit) to AI implementations across eight quadrants — useful for comparing how different systems position their memory architectures.
captured: 2026-06-09
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs

Author: Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, Ruiming Tang, Yong Liu (Huawei Noah's Ark Lab)
Source: https://arxiv.org/html/2504.15965v2
Date: 2025 (arXiv:2504.15965)

## Abstract

Memory enables encoding, storing, and retrieving information, forming the foundation for human growth and world interaction. In LLM-driven AI systems, memory allows retaining and recalling past interaction information to improve future responses. This survey systematically analyzes the relationship between human memory and AI system memory, proposing a comprehensive 3D-8Q (three-dimensional, eight-quadrant) taxonomy based on object (personal/system), form (parametric/non-parametric), and time (short-term/long-term) dimensions. The survey organizes existing memory research, identifies open challenges, and outlines future directions for LLM-era memory systems.

---

## 1 Introduction

Large language models have become central to AI systems, enabling applications spanning customer service, automated writing, translation, and information retrieval. Unlike traditional rule-based systems, LLM-driven AI offers flexibility and contextual awareness. Memory capabilities allow LLMs to "retain historical interactions with users and store contextual information, thereby providing more personalized, continuous, and context-aware responses in future interactions."

In neuroscience, human memory encompasses encoding, storage, and retrieval of information. The Multi-Store Model distinguishes short-term memory (sensory and working memory, lasting seconds to minutes) from long-term memory (explicit memory including episodic and semantic components; implicit memory including procedural knowledge).

LLM-powered autonomous agents exemplify memory-enhanced AI systems, incorporating planning, tool use, and multi-step reasoning. Memory enables these systems to overcome context window limitations, recall interaction history, and make informed decisions. Commercial implementations include ChatGPT Memory, Apple Personal Context, mem0, and MemoryScope.

Current reviews predominantly analyze memory through temporal dimensions alone. This survey proposes broader analysis across object, form, and time dimensions, addressing gaps in systematic AI memory organization.

---

## 2 Overview

### 2.1 Human Memory

#### 2.1.1 Short-Term and Long-Term Memory

**Short-Term Memory**

Short-term memory temporarily holds small information quantities for brief periods (seconds to minutes). It includes:

- **Sensory memory:** Brief storage of external sensory information (visual, auditory, tactile), lasting milliseconds to seconds. Some transfers to working memory or long-term episodic memory.

- **Working memory:** System temporarily storing and processing information, supporting decision-making and problem-solving. Enables tracking current thoughts alongside computational steps.

**Long-Term Memory**

Long-term memory stores information across extended periods (minutes to lifetime). It comprises:

- **Explicit memory (declarative):** Consciously recalled facts and events, divided into:
  - *Episodic memory:* Personal experiences and events (what you ate for lunch)
  - *Semantic memory:* Facts and knowledge (Earth orbits the Sun)

- **Implicit memory (non-declarative):** Unconscious skills and habits. Procedural memory encompasses learned movement patterns (bicycle riding, piano playing).

Multiple memory systems operate simultaneously across different brain regions, interacting interdependently. For example, hearing a new song activates sensory memory, transfers to working memory through conscious attention, triggers episodic memory of listening contexts, gradually forms semantic memory linking melody to title, and procedural memory stores motor patterns for playing the song.

#### 2.1.2 Memory Mechanisms

Memory involves three core processes:

**Encoding**

Memory encoding converts sensory information into brain-storable form through various approaches:
- Visual encoding: Processing color, shape, texture
- Acoustic encoding: Processing pitch, tone, rhythm
- Semantic encoding: Processing meaning

Enhancement techniques include mnemonics (acronyms, peg-word systems), chunking (breaking information into meaningful units), imagination (linking images to words), and association (connecting new information to prior knowledge).

**Storage**

Memory storage involves coordinated multi-brain-region activity:
- *Prefrontal cortex:* Associated with working memory and decision-making
- *Hippocampus:* Organizes and consolidates explicit memories
- *Cerebral cortex:* Stores and retrieves semantic memory
- *Cerebellum:* Responsible for procedural memory through repetition

**Retrieval**

Memory retrieval accesses stored information by reactivating neural pathways. Types include:
- *Recognition:* Identifying previously encountered information (familiar faces, learned facts)
- *Recall:* Retrieving information without external cues (phone numbers, addresses)
- *Relearning:* Reacquiring forgotten information, typically faster than initial learning

**Consolidation**

Memory consolidation converts short-term to long-term memory, stabilizing information through synaptic plasticity (neuron connection strengthening) and systems consolidation (hippocampus-to-neocortex memory transfer).

**Reconsolidation**

Memory reconsolidation reactivates previously stored memories, entering unstable states requiring restabilization. This process allows memory modification or updating in response to new information or contexts, influenced by emotions, cognitive biases, or new knowledge.

**Reflection**

Memory reflection involves actively reviewing and evaluating personal memory content and processes, enhancing self-awareness, adjusting learning strategies, and optimizing decision-making. This metacognitive process relies on prefrontal cortex monitoring and regulation.

**Forgetting**

Forgetting occurs through encoding failure (information not properly encoded), memory decay (fading without reinforcement), interference (competing or overwriting memories), retrieval failure (inaccessible despite storage), or motivated forgetting (conscious suppression or unconscious repression). Forgetting is necessary for filtering irrelevant information and prioritizing important content.

### 2.2 Memory of LLM-driven AI Systems

LLM-driven AI systems employ memory mechanisms analogous to human systems, encoding, storing, and recalling information for future use. Typical examples include LLM-driven agent systems leveraging memory for enhanced reasoning, planning, and personalization.

#### 2.2.1 Fundamental Dimensions of AI Memory

AI memory categorization uses three primary dimensions:

**Object Dimension**

The object dimension, tied to LLM-AI-human interaction, categorizes information by source and purpose:
- *Personal memory:* Human input and feedback from users
- *System memory:* Intermediate results generated during task execution

Personal memory improves user behavior understanding and enhances personalization. System memory strengthens reasoning capabilities, as in Chain-of-Thought and ReAct approaches.

**Form Dimension**

The form dimension addresses memory representation and storage:
- *Parametric memory:* Embedded within model parameters through training
- *Non-parametric memory:* Stored externally in databases or retrieval mechanisms

Non-parametric memory serves as supplementary knowledge sources, dynamically accessible in real-time, exemplified by retrieval-augmented generation.

**Time Dimension**

The time dimension defines retention duration and influence timescales:
- *Short-term memory:* Contextual information temporarily maintained within current conversations, enabling coherence and continuity
- *Long-term memory:* Information from past interactions stored externally, retrieved when needed, enabling user-specific knowledge retention and personalization improvement

#### 2.2.2 Parallels Between Human and AI Memory

**Sensory Memory**

LLM-driven AI systems convert text, images, speech, and video inputs into machine-processable signals. "This initial stage of information processing is analogous to human sensory memory, where raw data is briefly held before further cognitive processing." Further processing transitions information to working memory; absent processing, information is quickly discarded.

**Working Memory**

AI working memory serves as temporary storage and processing for real-time reasoning and decision-making. It encompasses personal memory (contextual information in multi-turn dialogues) and system memory (chain-of-thought reasoning). As short-term memory, it undergoes consolidation toward long-term memory (episodic memory). During inference, LLMs generate intermediate computational results like KV-Caches, acting as parametric short-term memory enhancing efficiency.

**Explicit Memory**

AI explicit memory divides into two components:
- Non-parametric long-term memory: User-specific information retention, analogous to human episodic memory
- Parametric long-term memory: Factual knowledge embedded in model parameters, corresponding to human semantic memory

Together, these enable past interaction recall and acquired knowledge application.

**Implicit Memory**

AI implicit memory encompasses learned processes and patterns for task execution, analogous to human procedural memory. This includes learning from successes and failures through non-parametric reflection and refinement, or encoding within model parameters for internalized task knowledge.

#### 2.2.3 3D-8Q Memory Taxonomy

The 3D-8Q taxonomy systematically categorizes AI memory by function, storage mechanism, and retention duration:

| Object | Form | Time | Quadrant | Role | Function |
|--------|------|------|----------|------|----------|
| Personal | Non-Parametric | Short-Term | I | Working Memory | Supports real-time context supplementation, enhancing coherent session interactions |
| Personal | Non-Parametric | Long-Term | II | Episodic Memory | Enables cross-session memory retention, allowing past user interaction recall for personalization |
| Personal | Parametric | Short-Term | III | Working Memory | Temporarily enhances contextual understanding, improving response relevance and coherence |
| Personal | Parametric | Long-Term | IV | Semantic Memory | Facilitates continuous knowledge integration, improving adaptability and personalization |
| System | Non-Parametric | Short-Term | V | Working Memory | Assists complex reasoning and decision-making through intermediate outputs like chain-of-thought |
| System | Non-Parametric | Long-Term | VI | Procedural Memory | Captures historical experiences and self-reflection, enabling reasoning and problem-solving refinement |
| System | Parametric | Short-Term | VII | Working Memory | Enhances computational efficiency through temporary parametric storage like KV-Caches |
| System | Parametric | Long-Term | VIII | Semantic/Procedural Memory | Forms foundational knowledge base in model parameters, serving long-term factual and task-related knowledge |

---

## 3 Personal Memory

Personal memory encompasses storing and utilizing human input and response data during LLM-driven AI system interactions. Development and application enhance personalization capabilities and user experience. This section explores personal memory across non-parametric and parametric approaches.

### 3.1 Contextual Personal Memory

Non-parametric contextual memory divides into short-term memory from current session multi-turn dialogues and long-term memory from historical cross-session dialogues.

#### 3.1.1 Loading Multi-Turn Dialogue (Quadrant-I)

In multi-turn dialogue scenarios, current session conversation history significantly enhances LLM-driven AI understanding of real-time user intent, enabling relevant and contextually appropriate responses. Modern dialogue systems like ChatGPT, DeepSeek-Chat, and Claude excel at maintaining coherence over extended interactions.

ChatGPT exemplifies multi-turn dialogue systems where current session conversation history serves as short-term memory supplementing dialogue context. Dialogue memory encodes in role-content format (roles: "User" and "Assistant"), maintaining speaker clarity and conversation flow clarity. Through effective dialogue management at different hierarchical levels ("Assistant," "Threads," "Messages," "Runs"), the system tracks conversation turn state and step state, ensuring continuity and consistency. When conversation length becomes excessive, the system truncates turns, preventing model length limitations while maintaining essential context.

#### 3.1.2 Memory Retrieval-Augmented Generation (Quadrant-II)

Cross-session dialogue scenarios retrieve relevant user long-term memories from historical conversations, supplementing missing information (personal preferences, character relationships). Memory retrieval-augmented generation advantages include avoiding loading all multi-session conversations (computationally efficient given extended context windows) and cost-effectiveness. Long-term personal memory encompasses users' behavioral history, preferences, and extended interaction records with AI agents.

Leveraging retrieval-augmented generation enables tailored system responses and behaviors, improving user satisfaction and engagement. Personal assistants remembering preferred news sources can prioritize those in briefings; recommendation systems understanding viewing habits suggest aligned content. Current commercial and open-source platforms construct long-term memory—ChatGPT Memory, Me.bot, MemoryScope, mem0. Long-term personal memory follows four core processing stages:

**Construction**

User memory construction extracts and refines raw memory data (multi-turn conversations), analogous to human memory consolidation—stabilizing and strengthening memories for long-term storage. Well-organized long-term memory enhances storage efficiency and retrieval effectiveness.

MemoryBank leverages memory modules storing conversation histories and key event summaries, enabling long-term user profile construction. RET-LLM retains essential external world knowledge, allowing agents to monitor and update real-time user-relevant environmental context. Various storage formats accommodate different memory types:

- *Key-value formats:* Enable efficient structured information access (user facts, preferences)
- *Graph-based formats:* Capture entity relationships (individuals, events)
- *Vector formats:* Encode semantic meaning and contextual information through textual, visual, or audio representation

**Management**

User memory management further refines previously constructed memories through deduplication, merging, and conflict resolution, analogous to human memory reconsolidation and reflection. Reflective Memory Management combines prospective reflection for dynamic summarization with retrospective reflection for retrieval optimization via reinforcement learning, addressing rigid memory granularity and fixed retrieval mechanisms.

LD-Agent enhances long-term dialogue personalization and consistency through personalized persona information construction for users and agents, integrating retrieved memories for response generation optimization. A-MEM introduces self-organizing memory systems inspired by Zettelkasten methodology, constructing interconnected knowledge networks through dynamic indexing, linking, and memory evolution, enabling flexible organization, updating, and retrieval.

MemoryBank incorporates memory updating inspired by the Ebbinghaus Forgetting Curve, allowing AI to forget or reinforce memories based on elapsed time and relative importance, enabling human-like memory and enhanced user experience.

**Retrieval**

Personal memory retrieval identifies memory entries relevant to current user requests, closely tied to memory storage methods. Key-value memory retrieval uses SQL queries over structured databases (ChatDB). RET-LLM employs fuzzy search retrieving triplet-structured memories. Graph-based memory retrieval uses HippoRAG, constructing knowledge graphs over entities, phrases, and summarization for comprehensive memory recall. HippoRAG 2 combines original passages with phrase-based knowledge graphs. Vector memory retrieval employs dual-tower dense retrieval models (MemoryBank) with FAISS indexing for efficient similarity-based retrieval.

**Usage**

Personal memory usage empowers downstream applications with personalization, enhancing individualized experience. Recalled relevant memory serves as contextual information enhancing personalized recommendation and response capabilities of conversational recommender agents, improving user experience. Beyond personalized dialogue and recommendation, personal memory enhances applications including software development, social-network simulation, and financial trading.

Memory-related benchmarks support in-depth personal memory research: long-term conversational memory (MADial-Bench, LOCOMO, MSC), everyday life memory (MemDaily), memory-aware proactive dialogue (ChMapData), multimodal dialogue memory (MMRC), egocentric video understanding (Ego4D, EgoLife), and long-context reasoning (BABILong).

### 3.2 Parametric Personal Memory

Beyond external non-parametric memory, user personal memory stores parametrically. Personal data can fine-tune LLMs, embedding memory directly in parameters (parametric long-term memory) for personalized LLMs. Alternatively, historical dialogues cache as prompts during inference (parametric short-term memory) for quick future reuse.

#### 3.2.1 Memory Caching For Acceleration (Quadrant-III)

Personal parametric short-term memory typically refers to intermediate attention states from LLM processing of personal data, utilized as memory caches accelerating inference. Prompt caching efficiently manages frequently requested personal data or information through pre-storage, such as user conversational history. During multi-turn dialogues, dialogue systems quickly provide personal context directly from parametric memory cache, avoiding recalculation or original data source retrieval, saving time and resources.

Major platforms (DeepSeek, Anthropic, OpenAI, Google) employ prompt caching reducing API call costs and improving response speed. Personal parametric short-term memory enhances retrieval-augmented generation performance through Contextual Retrieval, where prompt caching reduces contextualized chunk generation overhead. Current research specifically targeting personal memory caching remains limited; most existing work considers caching a fundamental system memory capability, particularly regarding key-value management and reuse.

#### 3.2.2 Personalized Knowledge Editing (Quadrant-IV)

Personal parametric long-term memory utilizes personalized knowledge editing technology, such as Parameter-Efficient Fine-Tuning, encoding personal data into LLM parameters for long-term parameterized memory storage.

Character-LLM enables specific character role-playing (Beethoven, Cleopatra, Julius Caesar) through model training remembering character roles and experiences. AI-Native Memory proposes using LLMs as Lifelong Personal Models, parameterizing, compressing, and continuously evolving personal memory through user interactions for comprehensive user understanding. MemoRAG utilizes LLM parametric memory storing user conversation history and preferences, forming personalized global memory enhancing personalization and enabling tailored recommendations.

Echo, an LLM enhanced with temporal episodic memory, improves multi-turn, complex memory-based dialogue applications. Parametric personal long-term memory presents challenges, notably requiring individual user data fine-tuning, demanding substantial computational resources, significantly hindering scalability and practical deployment.

### 3.3 Discussion

Personal memory encompasses non-parametric and parametric approaches. Personal non-parametric short-term memory requires efficient encoding and management mechanisms. Existing literature predominantly emphasizes constructing, managing, retrieving, and effectively utilizing user personal non-parametric long-term memory. Parametric short-term memory employs prompt caching reducing computational costs and enhancing efficiency. Parametric long-term memory offers memory compression advantages, supporting comprehensive user-accumulated experience representation. Recent trends indicate growing integration of short-term and long-term memory paradigms, wherein parametric and non-parametric components complement and reinforce one another.

---

## 4 System Memory

System memory constitutes critical LLM-driven AI system components, encompassing intermediate representations or results throughout task execution. Leveraging system memory enhances reasoning, planning, and higher-order cognitive functions. Effective system memory use contributes to self-evolution and continual improvement capacities. This section examines system memory across non-parametric and parametric perspectives.

### 4.1 Contextual System Memory

From temporal perspectives, non-parametric short-term system memory refers to reasoning and action result sequences from LLMs during task execution, supporting enhanced reasoning and planning within current task contexts. Non-parametric long-term system memory represents abstracted and generalized short-term memory, encompassing prior successful experience consolidation and historical interaction self-reflection mechanisms, facilitating continual AI system evolution and adaptive enhancement.

#### 4.1.1 Reasoning & Planning Enhancement (Quadrant-V)

Analogous to human cognition, LLM reasoning and planning produce intermediate output sequences reflecting task-related attempts (successful or erroneous). Regardless of correctness, such intermediate results serve as informative references guiding subsequent task execution, playing pivotal roles in LLM-driven AI systems. Empirical evidence demonstrates leveraging this memory structure significantly enhances LLM reasoning and planning.

ReAct integrates reasoning and action by generating intermediate reasoning steps alongside corresponding actions, enabling thought and execution alternation, facilitating intelligent planning and adaptive decision-making in complex problem-solving. Reflexion introduces dynamic memory and self-reflection mechanisms, allowing LLM self-evaluation and iterative behavior refinement based on prior errors or limitations, promoting continuous learning and optimization.

#### 4.1.2 Reflection & Refinement (Quadrant-VI)

System non-parametric long-term memory development parallels human learning from successes and failures, involving accumulated short-term memory trace reflection and refinement. This mechanism enables system retention and effective strategy replication from past experiences while extracting valuable failure lessons, minimizing repeated error likelihood. Continuous updating and optimization incrementally enhance decision-making capabilities and novel challenge responsiveness.

Buffer of Thoughts refines historical task chain-of-thoughts into thought templates stored in memory repositories, guiding future reasoning and decision-making. Agent Workflow Memory introduces reusable paths (workflows), guiding subsequent task generation through workflow selection. Think-in-Memory continuously generates conversation history-based thoughts, more conducive to reasoning and computation than raw data. Ghost in the Minecraft uses reference plans in memory, enabling efficient agent planner task handling. Voyager refines skills through environmental feedback, storing acquired skills in memory skill libraries for future similar situation reuse.

Retroformer leverages recent interaction trajectories as short-term memory and reflective failure feedback as long-term memory for decision-making and reasoning guidance. ExpeL enhances task resolution through contextualized successful examples and abstracted success/failure insights via comparative and pattern-based analysis.

### 4.2 Parametric System Memory

Parametric system memory refers to inference process knowledge information temporary storage in parametric forms (KV Cache) as short-term memory, or long-term model parameter knowledge information editing and storage. Parametric short-term system memory addresses high inference costs and latency issues. Parametric long-term system memory enables efficient long-timespan information storage and integration, forming continuously evolving knowledge systems.

#### 4.2.1 KV Management & Reuse (Quadrant-VII)

Parametric short-term system memory primarily focuses on attention key and value management in LLMs, addressing high inference costs and latency during reasoning. KV management optimizes memory efficiency and inference performance through cache organization, compression, and quantization techniques.

vLLM is high-efficiency LLM serving built on PagedAttention, virtual memory-inspired attention mechanisms enabling near-zero KV cache waste and flexible request sharing, substantially improving batching efficiency and throughput. ChunkKV compresses key-value cache in long-context inference by grouping tokens into semantic chunks, retaining informative ones, enabling layer-wise index reuse, reducing memory and computational costs. LLM.int8() employs mixed-precision quantization combining vector-wise Int8 quantization with selective 16-bit outlier feature handling, enabling memory-efficient inference without performance degradation.

KV reuse focuses on parameter reuse through token-level KV Cache and sentence-level Prompt Cache, reducing computational costs and LLM usage efficiency. KV Cache stores attention keys and values from neural network sequence generation, enabling reuse in subsequent inference steps, accelerating attention computation and reducing redundant computation. Prompt Cache operates at sentence level, caching previous input prompts with corresponding output results; similar prompts retrieve cached responses directly, saving computation.

RAGCache introduces multilevel dynamic caching for Retrieval-Augmented Generation, caching intermediate knowledge states, optimizing memory replacement policies based on inference and retrieval patterns, overlapping retrieval with inference reducing latency and improving throughput.

Parametric short-term system memory overlaps somewhat with parametric short-term personal memory technically. The difference lies in focus: parametric short-term personal memory improves individual input data processing; parametric short-term system memory optimizes task execution system-level context storage and reuse. The former addresses individual input information quick processing and adaptation; the latter aims inference cost reduction in multi-turn reasoning and global task consistency and efficiency improvement.

#### 4.2.2 Parametric Memory Structures (Quadrant-VIII)

From large language models as long-term parametric memory perspective, LLMs aren't merely immediate response tools; they store and integrate extended-duration information, forming ever-evolving knowledge systems. Transformer-based LLMs memorize knowledge primarily through self-attention mechanisms and large-scale parameterized training. Training on vast corpora teaches extensive world knowledge, language patterns, and task solutions. LLMs modify, update, or refine internal knowledge through parameterized knowledge editing, enabling precise task handling or user-aligned responses.

MemoryLLM demonstrates self-update capacity, injecting new knowledge effectively, integrating information with excellent model editing performance and long-term information retention. WISE is lifelong LLM editing framework employing dual-parametric memory design: main memory preserves pretrained knowledge; side memory stores edited information. Routing mechanisms dynamically access appropriate memory during inference; knowledge sharding distributes and integrates edits efficiently, ensuring reliability, generalization, and locality throughout continual updates.

Parameterized knowledge editing enables LLMs with dynamic, flexible knowledge updating capabilities, responding to constantly changing task requirements, domain knowledge, and real-world information, remaining efficient and accurate across application scenarios while customizing and optimizing according to user and environmental needs.

### 4.3 Discussion

System memory encompasses non-parametric and parametric approaches. Non-parametric short-term system memory enhances current task reasoning and planning. Non-parametric long-term system memory enables successful experience reuse and historical experience-based self-reflection, facilitating LLM-driven AI system capability evolution. Parametric short-term system memory reduces inference costs and improves efficiency. Parametric long-term system memory stores and integrates extended-duration information, forming continuously evolving knowledge systems.

---

## 5 Open Problems and Future Directions

Although substantial progress advances memory research across three dimensions (object, form, time) and eight quadrants, numerous open issues and challenges remain. Building upon recent advancements and recognizing existing limitations, promising research directions include:

### From Unimodal Memory to Multimodal Memory

LLM-driven AI systems gradually expand from single data type processing (text) to simultaneous multiple data type handling (text, images, audio, video, sensor data), enhancing perceptual capabilities and enabling robust complex real-world task performance. In medicine, combining text (medical records), images (medical imaging), and speech (conversations) enables more accurate condition understanding and diagnosis. Multimodal memory systems integrate different sensory channel information into unified understanding, approaching human cognitive processes. Multimodal memory expansion enables more personalized and interactive AI applications—personal AI assistants communicating textually while interpreting user emotions through facial expressions, voice intonations, or body language, providing personalized empathetic responses.

### From Static Memory to Stream Memory

Static memory represents batch-processing memory storage, accumulating information in discrete batches, typically processing, storing, and retrieving at specific intervals or predetermined times. As offline memory models, static memory emphasizes systematic large-volume information organization and consolidation, supporting long-term knowledge retention and structured learning. Stream memory operates continuously, real-time. Analogous to data stream processing, it handles arriving information, prioritizing immediacy and adaptability. As online or real-time memory models, stream memory emphasizes dynamic information updating and evolving context rapid responsiveness. These paradigms aren't mutually exclusive; they function complementarily—static memory supports stable long-term knowledge accumulation; stream memory enables agile ongoing task adaptation and real-time information demands.

### From Specific Memory to Comprehensive Memory

Human memory comprises multiple interconnected subsystems (sensory, working, explicit, implicit), each fulfilling distinct functions contributing to overall cognition. Current LLM memory architectures often concentrate on narrow or task-specific components (short-term immediate inference memory or domain-specific knowledge storage). While targeted memory mechanisms enhance specific scenario performance, their limited scope constrains overall flexibility, generalization, and adaptability.

Comprehensive and collaborative memory system development is essential. These systems should integrate diverse memory types supporting efficient interaction, self-organization, and continual updating, enabling LLMs managing increasingly complex and dynamic tasks. Closely emulating human memory's multi-layered, multi-dimensional, adaptive characteristics could significantly advance LLM-based AI system general intelligence and autonomy.

### From Exclusive Memory to Shared Memory

Currently, each LLM-driven AI system memory operates independently, confined to specific domains and isolated tasks or environments. As AI technologies evolve, memory systems are expected becoming increasingly interconnected, transcending domain boundaries and enabling model collaboration enhancement. Medical domain LLMs could share memory with finance-focused models, facilitating cross-domain knowledge transfer and cooperative problem-solving.

Shared memory paradigms would improve individual system efficiency and adaptability while empowering multiple LLMs dynamically accessing one another's domain-specific expertise. Collaborative memory architectures could create intelligent, resource-efficient AI system networks addressing complex, multi-domain challenges, broadening AI application scopes and accelerating integration into diverse, demanding real-world scenarios.

### From Individual Privacy to Collective Privacy

Data sharing increasing prevalence shifts privacy protection focus from traditional individual privacy toward emerging collective privacy concepts. Conventional privacy frameworks safeguard personal data, preventing unauthorized access, leakage, or misuse of individually identifiable information. LLM contexts aggregate individual data into group-level datasets for large-scale analysis and prediction. Collective privacy protects groups or communities whose aggregated data usage rights and interests, raising group-level profiling and excessive surveillance prevention questions.

As AI memory systems advance and interconnect, collective privacy becomes critical challenges. Addressing this requires innovative techniques effectively balancing data utility and privacy preservation trade-offs.

### From Rule-Based Evolution to Automated Evolution

Traditional AI systems evolve through past experience reflection—reusing successful strategies—based on accumulated knowledge and historical data. This evolution often depends on manually crafted rules and heuristic adjustments enabling self-reflection, limiting flexibility, scalability, and efficiency, with rule quality and generalizability directly constraining adaptive capabilities.

AI systems should achieve automated evolution, dynamically adjusting and optimizing themselves by leveraging personal and system-level memories in response to changing data and environmental contexts. Systems capable of autonomously identifying performance bottlenecks and initiating self-improvement without explicit human-defined rules would significantly enhance responsiveness, reduce human intervention needs, and enable intelligent, dynamic, continuously self-evolving paradigms.

---

## 6 Conclusion

Memory plays pivotal roles in large language model era AI system advancement, shaping personalization degrees and influencing adaptability, reasoning, planning, and self-evolution key capabilities. This article systematically examines human memory relationships with LLM-driven AI system memory mechanisms, exploring how human cognition principles inspire more efficient and flexible memory architecture design.

Analysis begins with various human memory categories (perceptual, working, long-term) compared with existing AI memory models. Building upon this, an eight-quadrant classification framework grounded in three dimensions (object, form, time) offers multi-level, comprehensive memory system construction theoretical foundations. Reviewing AI current memory development from personal and system memory perspectives follows. Finally, contemporary AI memory design key challenges are identified, outlining promising future LLM-era research directions.

With continued technological progress, AI systems will increasingly adopt dynamic, adaptive, and intelligent memory architectures, enabling robust applications across complex, real-world tasks.
