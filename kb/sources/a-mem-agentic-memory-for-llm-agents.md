---
source: https://arxiv.org/abs/2502.12110
captured: 2026-02-28
capture: pdf-read
type: academic-paper
---

# A-Mem: Agentic Memory for LLM Agents

Author: Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang (Rutgers University; Independent Researcher; AIOS Foundation)
Source: https://arxiv.org/abs/2502.12110
Date: 8 Oct 2025

Code for Benchmark Evaluation: https://github.com/WujiangXu/AgenticMemory
Code for Production-ready Agentic Memory: https://github.com/WujiangXu/A-mem-sys

## Abstract

While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. Moreover, these systems' fixed operations and structures limit their adaptability across diverse tasks. To address this limitation, this paper proposes a novel agentic memory system for LLM agents that can dynamically organize memories in an agentic way. Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking. When a new memory is added, we generate a comprehensive note containing multiple structured attributes, including contextual descriptions, keywords, and tags. The system then analyzes historical memories to identify relevant connections, establishing links where meaningful similarities exist. Additionally, this process enables memory evolution — as new memories are integrated, they can trigger updates to the contextual representations and attributes of existing historical memories, allowing the memory network to continuously refine its understanding. Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making, allowing for more adaptive and context-aware memory management. Empirical experiments on six foundation models show superior improvement against existing SOTA baselines.

## 1 Introduction

Large Language Model (LLM) agents have demonstrated remarkable capabilities in various tasks, with recent advances enabling them to interact with environments, execute tasks, and make decisions autonomously. They integrate LLMs with external tools and delicate workflows to improve reasoning and planning abilities. Though LLM agent has strong reasoning performance, it still needs a memory system to provide long-term interaction ability with the external environment.

Existing memory systems for LLM agents provide basic memory storage functionality. These systems require agent developers to predefine memory storage structures, specify storage points within the workflow, and establish retrieval timing. Meanwhile, to improve structured memory organization, Mem0, following the principles of RAG, incorporates graph databases for storage and retrieval processes. While graph databases provide structured organization for memory systems, their reliance on predefined schemas and relationships fundamentally limits their adaptability. This limitation manifests clearly in practical scenarios — when an agent learns a novel mathematical solution, current systems can only categorize and link this information within their preset framework, unable to forge innovative connections or develop new organizational patterns as knowledge evolves.

Such rigid structures, coupled with fixed agent workflows, severely restrict these systems' ability to generalize across new environments and maintain effectiveness in long-term interactions. The challenge becomes increasingly critical as LLM agents tackle more complex, open-ended tasks, where flexible knowledge organization and continuous adaptation are essential. Therefore, *how to design a flexible and universal memory system that supports LLM agents' long-term interactions* remains a crucial challenge.

In this paper, we introduce a novel agentic memory system, named as A-MEM, for LLM agents that enables dynamic memory structuring without relying on static, predetermined memory operations. Our approach draws inspiration from the Zettelkasten method, a sophisticated knowledge management system that creates interconnected information networks through atomic notes and flexible linking mechanisms. Our system introduces an agentic memory architecture that enables autonomous and flexible memory management for LLM agents. For each new memory, we construct comprehensive notes, which integrates multiple representations: structured textual attributes including several attributes and embedding vectors for similarity matching. Then A-MEM analyzes the historical memory repository to establish meaningful connections based on semantic similarities and shared attributes. This integration process not only creates new links but also enables dynamic evolution when new memories are incorporated, they can trigger updates to the contextual representations of existing memories, allowing the entire memories to continuously refine and deepen its understanding over time.

Contributions:

- We present A-MEM, an agentic memory system for LLM agents that enables autonomous generation of contextual descriptions, dynamic establishment of memory connections, and intelligent evolution of existing memories based on new experiences. This system equips LLM agents with long-term interaction capabilities without requiring predetermined memory operations.
- We design an agentic memory update mechanism where new memories automatically trigger two key operations: link generation and memory evolution. Link generation automatically establishes connections between memories by identifying shared attributes and similar contextual descriptions. Memory evolution enables existing memories to dynamically adapt as new experiences are analyzed, leading to the emergence of higher-order patterns and attributes.
- We conduct comprehensive evaluations of our system using a long-term conversational dataset, comparing performance across six foundation models using six distinct evaluation metrics, demonstrating significant improvements. Moreover, we provide T-SNE visualizations to illustrate the structured organization of our agentic memory system.

## 2 Related Work

### 2.1 Memory for LLM Agents

Prior works on LLM agent memory systems have explored various mechanisms for memory management and utilization. Some approaches complete interaction storage, which maintains comprehensive historical records through dense retrieval models or read-write memory structures. Moreover, MemGPT leverages cache-like architectures to prioritize recent information. Similarly, SCM proposes a Self-Controlled Memory framework that enhances LLMs' capability to maintain long-term memory through a memory stream and controller mechanism. However, these approaches face significant limitations in handling diverse real-world tasks. While they can provide basic memory functionality, their operations are typically constrained by predefined structures and fixed workflows. These constraints stem from their reliance on rigid operational patterns, particularly in memory writing and retrieval processes. Such inflexibility leads to poor generalization in new environments and limited effectiveness in long-term interactions.

### 2.2 Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) has emerged as a powerful approach to enhance LLMs by incorporating external knowledge sources. The standard RAG process involves indexing documents into chunks, retrieving relevant chunks based on semantic similarity, and augmenting the LLM's prompt with this retrieved context for generation. Advanced RAG systems have evolved to include sophisticated pre-retrieval and post-retrieval optimizations. Building upon these foundations, recent researches has introduced agentic RAG systems that demonstrate more autonomous and adaptive behaviors in the retrieval process. These systems can dynamically determine when and what to retrieve, generate hypothetical responses to guide retrieval, and iteratively refine their search strategies based on intermediate results.

However, while agentic RAG approaches demonstrate agency in the retrieval phase by autonomously deciding when and what to retrieve, our agentic memory system exhibits agency at a more fundamental level through the autonomous evolution of its memory structure. Inspired by the Zettelkasten method, our system allows memories to actively generate their own contextual descriptions, form meaningful connections with related memories, and evolve both their content and relationships as new experiences emerge. This fundamental distinction in agency between retrieval versus storage and evolution distinguishes our approach from agentic RAG systems, which maintain static knowledge bases despite their sophisticated retrieval mechanisms.

## 3 Methodology

Our proposed agentic memory system draws inspiration from the Zettelkasten method, implementing a dynamic and self-evolving memory system that enables LLM agents to maintain long-term memory without predetermined operations. The system's design emphasizes atomic note-taking, flexible linking mechanisms, and continuous evolution of knowledge structures.

### 3.1 Note Construction

Building upon the Zettelkasten method's principles of atomic note-taking and flexible organization, we introduce an LLM-driven approach to memory note construction. When an agent interacts with its environment, we construct structured memory notes that capture both explicit information and LLM-generated contextual understanding. Each memory note m_i in our collection M = {m_1, m_2, ..., m_N} is represented as:

m_i = {c_i, t_i, K_i, G_i, X_i, e_i, L_i}

where c_i represents the original interaction content, t_i is the timestamp of the interaction, K_i denotes LLM-generated keywords that capture key concepts, G_i contains LLM-generated tags for categorization, X_i represents the LLM-generated contextual description that provides rich semantic understanding, and L_i maintains the set of linked memories that share semantic relationships. To enrich each memory note with meaningful context beyond its basic content and timestamp, we leverage an LLM to analyze the interaction and generate these semantic components via a note construction prompt P_s1.

To enable efficient retrieval and linking, we compute a dense vector representation via a text encoder that encapsulates all textual components of the note:

e_i = f_enc[ concat(c_i, K_i, G_i, X_i) ]

### 3.2 Link Generation

Our system implements an autonomous link generation mechanism that enables new memory notes to form meaningful connections without predefined rules. When the constructed memory note m_n is added to the system, we first leverage its semantic embedding for similarity-based retrieval. For each existing memory note m_j in M, we compute a similarity score using cosine similarity. The system then identifies the top-k most relevant memories. Based on these candidate nearest memories, we prompt the LLM to analyze potential connections based on their potential common attributes via prompt P_s2.

By using embedding-based retrieval as an initial filter, we enable efficient scalability while maintaining semantic relevance. A-MEM can quickly identify potential connections even in large memory collections without exhaustive comparison. More importantly, the LLM-driven analysis allows for nuanced understanding of relationships that goes beyond simple similarity metrics. The language model can identify subtle patterns, causal relationships, and conceptual connections that might not be apparent from embedding similarity alone. We implements the Zettelkasten principle of flexible linking while leveraging modern language models. The resulting network emerges organically from memory content and context, enabling natural knowledge organization.

### 3.3 Memory Evolution

After creating links for the new memory, A-MEM evolves the retrieved memories based on their textual information and relationships with the new memory. For each memory m_j in the nearest neighbor set, the system determines whether to update its context, keywords, and tags. The evolved memory m_j* then replaces the original memory m_j in the memory set M. This evolutionary approach enables continuous updates and new connections, mimicking human learning processes. As the system processes more memories over time, it develops increasingly sophisticated knowledge structures, discovering higher-order patterns and concepts across multiple memories. This creates a foundation for autonomous memory learning where knowledge organization becomes progressively richer through the ongoing interaction between new experiences and existing memories.

### 3.4 Retrieve Relative Memory

In each interaction, A-MEM performs context-aware memory retrieval to provide the agent with relevant historical information. Given a query text q from the current interaction, we first compute its dense vector representation using the same text encoder used for memory notes. The system then computes similarity scores between the query embedding and all existing memory notes in M using cosine similarity, then retrieves the k most relevant memories from the historical memory storage to construct a contextually appropriate prompt.

These retrieved memories provide relevant historical context that helps the agent better understand and respond to the current interaction. The retrieved context enriches the agent's reasoning process by connecting the current interaction with related past experiences stored in the memory system.

## 4 Experiment

### 4.1 Dataset and Evaluation

To evaluate the effectiveness of instruction-aware recommendation in long-term conversations, we utilize the LoCoMo dataset, which contains significantly longer dialogues compared to existing conversational datasets. While previous datasets contain dialogues with around 1K tokens over 4-5 sessions, LoCoMo features much longer conversations averaging 9K tokens spanning up to 35 sessions, making it particularly suitable for evaluating models' ability to handle long-range dependencies and maintain consistency over extended conversations. The LoCoMo dataset comprises diverse question types: (1) single-hop questions answerable from a single session; (2) multi-hop questions requiring information synthesis across sessions; (3) temporal reasoning questions testing understanding of time-related information; (4) open-domain knowledge questions requiring integration of conversation context with external knowledge; and (5) adversarial questions assessing models' ability to identify unanswerable queries. In total, LoCoMo contains 7,512 question-answer pairs across these categories.

We also use DialSim to evaluate the effectiveness of our memory system. It is question-answering dataset derived from long-term multi-party dialogues from popular TV shows (Friends, The Big Bang Theory, and The Office), covering 1,300 sessions spanning five years, containing approximately 350,000 tokens, and including more than 1,000 questions per session from refined fan quiz website questions and complex questions generated from temporal knowledge graphs.

For comparison baselines, we compare to LoCoMo, ReadAgent, MemoryBank and MemGPT. For evaluation, we employ two primary metrics: the F1 score to assess answer accuracy by balancing precision and recall, and BLEU-1 to evaluate generated response quality by measuring word overlap with ground truth responses.

### 4.2 Implementation Details

For all baselines and our proposed method, we maintain consistency by employing identical system prompts. The deployment of Qwen-1.5B/3B and Llama 3.2 1B/3B models is accomplished through local instantiation using Ollama, with LiteLLM managing structured output generation. For GPT models, we utilize the official structured output API. In our memory retrieval process, we primarily employ k=10 for top-k memory selection to maintain computational efficiency, while adjusting this parameter for specific categories to optimize performance. For text embedding, we implement the all-minilm-l6-v2 model across all experiments.

### 4.3 Empirical Results

**Performance Analysis.** In our empirical evaluation, we compared A-MEM with four competitive baselines including LoCoMo, ReadAgent, MemoryBank, and MemGPT on the LoCoMo dataset. For non-GPT foundation models, our A-MEM consistently outperforms all baselines across different categories, demonstrating the effectiveness of our agentic memory approach. For GPT-based models, while LoCoMo and MemGPT show strong performance in certain categories like Open Domain and Adversarial tasks due to their robust pre-trained knowledge in simple fact retrieval, our A-MEM demonstrates superior performance in Multi-Hop tasks achieving at least two times better performance that require complex reasoning chains.

On the DialSim dataset, A-MEM consistently outperforms all baselines across evaluation metrics, achieving an F1 score of 3.45 (a 35% improvement over LoCoMo's 2.55 and 192% higher than MemGPT's 1.18).

**Cost-Efficiency Analysis.** A-MEM demonstrates significant computational and cost efficiency alongside strong performance. The system requires approximately 1,200 tokens per memory operation, achieving an 85-93% reduction in token usage compared to baseline methods (LoCoMo and MemGPT with 16,900 tokens) through its selective top-k retrieval mechanism. This substantial token reduction directly translates to lower operational costs, with each memory operation costing less than $0.0003 when using commercial API services — making large-scale deployments economically viable. Processing times average 5.4 seconds using GPT-4o-mini and only 1.1 seconds with locally-hosted Llama 3.2 1B on a single GPU.

### 4.4 Ablation Study

To evaluate the effectiveness of the Link Generation (LG) and Memory Evolution (ME) modules, we conduct the ablation study by systematically removing key components of our model. When both LG and ME modules are removed, the system exhibits substantial performance degradation, particularly in Multi Hop reasoning and Open Domain tasks. The system with only LG active (w/o ME) shows intermediate performance levels, maintaining significantly better results than the version without both modules. Our full model, A-MEM, consistently achieves the best performance across all evaluation categories, with particularly strong results in complex reasoning tasks. The ablation study validates that the link generation module serves as a critical foundation for memory organization, and the memory evolution module provides essential refinements to the memory structure.

### 4.5 Hyperparameter Analysis

We conducted extensive experiments to analyze the impact of the memory retrieval parameter k, which controls the number of relevant memories retrieved for each interaction. The results reveal that while increasing k generally leads to improved performance, this improvement gradually plateaus and sometimes slightly decreases at higher values. This pattern suggests a delicate balance in memory retrieval — while larger k values provide richer historical context for reasoning, they may also introduce noise and challenge the model's capacity to process longer sequences effectively. Moderate k values strike an optimal balance between context richness and information processing efficiency.

### 4.6 Scaling Analysis

To evaluate storage costs with accumulating memory, we examined the relationship between storage size and retrieval time across A-MEM and two baseline approaches: MemoryBank and ReadAgent. All three systems exhibit identical linear memory usage scaling (O(N)), confirming that A-MEM introduces no additional storage overhead. For retrieval time, A-MEM demonstrates excellent efficiency with minimal increases as memory size grows. Even when scaling to 1 million memories, A-MEM's retrieval time increases only from 0.31μs to 3.70μs, representing exceptional performance.

### 4.7 Memory Analysis

T-SNE visualization of memory embeddings demonstrates the structural advantages of the agentic memory system. A-MEM (shown in blue) consistently exhibits more coherent clustering patterns compared to the baseline system (shown in red). This structural organization is particularly evident in Dialogue 2, where well-defined clusters emerge in the central region, providing empirical evidence for the effectiveness of the memory evolution mechanism and contextual description generation.

## 5 Conclusions

In this work, we introduced A-MEM, a novel agentic memory system that enables LLM agents to dynamically organize and evolve their memories without relying on predefined structures. Drawing inspiration from the Zettelkasten method, our system creates an interconnected knowledge network through dynamic indexing and linking mechanisms that adapt to diverse real-world tasks. The system's core architecture features autonomous generation of contextual descriptions for new memories and intelligent establishment of connections with existing memories based on shared attributes. Furthermore, our approach enables continuous evolution of historical memories by incorporating new experiences and developing higher-order attributes through ongoing interactions. Through extensive empirical evaluation across six foundation models, we demonstrated that A-MEM achieves superior performance compared to existing state-of-the-art baselines in long-term conversational tasks.

## 6 Limitations

While our agentic memory system achieves promising results, we acknowledge several areas for potential future exploration. First, although our system dynamically organizes memories, the quality of these organizations may still be influenced by the inherent capabilities of the underlying language models. Different LLMs might generate slightly different contextual descriptions or establish varying connections between memories. Additionally, while our current implementation focuses on text-based interactions, future work could explore extending the system to handle multimodal information, such as images or audio, which could provide richer contextual representations.

## Appendix B: Prompt Templates

### B.1 Prompt Template of Note Construction (P_s1)

Generate a structured analysis of the following content by:
1. Identifying the most salient keywords (focus on nouns, verbs, and key concepts)
2. Extracting core themes and contextual elements
3. Creating relevant categorical tags

Format the response as a JSON object:
```
{
  "keywords": [ several specific, distinct keywords that capture key concepts and terminology, ordered from most to least important, at least three keywords ],
  "context": one sentence summarizing main topic/domain, key arguments/points, intended audience/purpose,
  "tags": [ several broad categories/themes for classification, including domain, format, and type tags, at least three tags ]
}
```

### B.2 Prompt Template of Link Generation (P_s2)

You are an AI memory evolution agent responsible for managing and evolving a knowledge base.
Analyze the new memory note according to keywords and context, also with their several nearest neighbors memory.
The new memory context: {context} content: {content}
keywords: {keywords}
The nearest neighbors memories: {nearest_neighbors_memories}
Based on this information, determine: Should this memory be evolved? Consider its relationships with other memories.

### B.3 Prompt Template of Memory Evolution (P_s3)

You are an AI memory evolution agent responsible for managing and evolving a knowledge base.
Analyze the new memory note according to keywords and context, also with their several nearest neighbors memory.
Make decisions about its evolution.
The new memory context: {context}
content: {content}
keywords: {keywords}
The nearest neighbors memories: {nearest_neighbors_memories}
Based on this information, determine:
1. What specific actions should be taken (strengthen, update_neighbor)?
1.1 If choose to strengthen the connection, which memory should it be connected to? Can you give the updated tags of this memory?
1.2 If choose to update neighbor, you can update the context and tags of these memories based on the understanding of these memories.

Return decision in JSON format:
```json
{
  "should_evolve": true/false,
  "actions": ["strengthen", "merge", "prune"],
  "suggested_connections": ["neighbor_memory_ids"],
  "tags_to_update": ["tag_1",...,"tag_n"],
  "new_context_neighborhood": ["new context",...,"new context"],
  "new_tags_neighborhood": [["tag_1",...,"tag_n"],...,["tag_1",...,"tag_n"]]
}
```
