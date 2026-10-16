---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Graphiti workflow account tracing the shipped LangGraph shoe-sales conversation from user submission through graph retrieval, tool delegation, response delivery and asynchronous memory admission."
run-id: AAS-2026-10-12-graphiti-1d535ca565a4-01
reviewed-boundary: "964bb11d1e7020e3cc67fab244268b0736b6c219"
---

# Graphiti workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped LangGraph shoe-sales notebook. It connects memory retrieval, an agent's tool decision, tool execution, another model invocation, user-facing delivery and a new memory write in one explicit graph. It is therefore a stronger workflow witness than joining independent MCP capabilities into an imagined assistant procedure. Its enclosing conversation route is already declared as [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop); this report adds workflow-specific annotations rather than redeclaring it. The core ingestion and retrieval routes remain [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) and [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval).

Evidence is SRC-1 implementation at the revision fixed by [boundary](boundary.md). This member inspected all notebook code cells, including setup, graph construction and the widget caller, and checked the quoted raw notebook source. SRC-1: `examples/langgraph-agent/agent.ipynb`. No notebook, provider, framework or database was executed. Historical outputs are not used as observed-run evidence. LangGraph and provider internals remain outside the frozen source; shipped wiring does not establish compatibility or successful operation.

### Request and context handoff

Setup clears the graph, builds indexes, awaits product ingestion and creates a user episode. It then selects the first node returned by searches for the user and ManyBirds to obtain center-node UUIDs. These identifiers are prerequisites for the later workflow, not authenticated user identities or verified entity matches. The notebook does not check those first-result selections before using them. SRC-1: `examples/langgraph-agent/agent.ipynb`.

The widget's submit callback captures and clears the input field and schedules `process_input`. That function passes a user-role message, user name and user-node UUID to `graph.astream`, with a persistent widget-session thread ID. The graph starts at `chatbot`; messages are accumulated using the framework's message reducer and `MemorySaver` checkpointer. Checkpoint state is distinct from Graphiti's retained graph and is not proof of graph persistence. SRC-1: `examples/langgraph-agent/agent.ipynb`; [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop).

At each chatbot invocation, the last message supplies a speaker-prefixed graph query. The notebook requests five facts centered on the user node, converts the returned edges to fact strings and inserts them into a system message along with sales instructions. It then sends that message and accumulated conversation to the tool-bound model. Only fact text crosses the edge-to-string transformation; graph source and temporal metadata do not accompany it. This is requested model influence, not a verified instruction or truth guarantee. SRC-1: `examples/langgraph-agent/agent.ipynb`; [RT-BAP-facts-context](runtime.md#rt-bap-facts-context).

### Tool delegation and next-step ownership

The model can request `get_shoe_data(query)`, the one bound tool. Its string query is handed to notebook tool code, which searches Graphiti for ten results centered on the ManyBirds node and returns fact text. `ToolNode` supplies the execution interface; the shipped graph routes back from tools to the agent, which retrieves user facts and calls the model again with the updated conversation. The model proposes the tool call; the scheduler executes the route selected by the notebook's conditional function. Neither Graphiti core nor a separate reviewer chooses the next conversational step. SRC-1: `examples/langgraph-agent/agent.ipynb`; [RT-CMP-chat-openai](runtime.md#rt-cmp-chat-openai).

> "    if not last_message.tool_calls:\n",
> "        return 'end'\n",
> "    # Otherwise if there is, we continue\n",
> "    else:\n",
> "        return 'continue'\n",
> --- `examples/langgraph-agent/agent.ipynb`

> "graph_builder.add_conditional_edges('agent', should_continue, {'continue': 'tools', 'end': END})\n",
> "graph_builder.add_edge('tools', 'agent')\n",
> --- `examples/langgraph-agent/agent.ipynb`

These conditions distinguish a tool round from completion. They do not evaluate whether a response answers the user's question, whether product facts are correct or whether the sales instructions were followed. The inspected notebook has no separate answer-review node or explicit retry budget; framework limits and tool-error behavior remain uninspected. There is no answer oracle supplied to this open conversation. SRC-1: `examples/langgraph-agent/agent.ipynb`.

### Memory handoff is not delivery verification

Every chatbot model response schedules `client.add_episode` before returning the response message. The episode contains the latest state message's string representation and the model's response content, with message source, a current timestamp and a Chatbot source description. This scheduling also occurs for responses that contain tool calls, not only for the final no-tool answer. Consequently, the source does not support describing this as retention of only completed user/assistant turns. On a post-tool round, the latest input message can be a tool result even though the episode prefix still uses the user name. SRC-1: `examples/langgraph-agent/agent.ipynb`.

> "    asyncio.create_task(\n",
> "        client.add_episode(\n",
> "            name='Chatbot Response',\n",
> "            episode_body=f'{state[\"user_name\"]}: {state[\"messages\"][-1]}\\nSalesBot: {response.content}',\n",
> --- `examples/langgraph-agent/agent.ipynb`

The core library owns subsequent extraction, resolution and persistence, as described in [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion). The notebook automatically proposes this mixed conversation content for admission, without a per-response human approval shown. Core schema/processing checks can reject or fail it, but those are not a factual-truth oracle. The notebook neither awaits the task nor retains its handle for completion checking or retry. Later graph retrieval can consume successfully stored content; availability before the next conversation step is not established. SRC-1: `examples/langgraph-agent/agent.ipynb`; [RT-CLM-write-envelope](runtime.md#rt-clm-write-envelope).

### Terminal result and failure path

A model response with no tool calls routes to graph end. In the widget caller, streamed events are inspected for a message whose last element is an `AIMessage` with string content. That text is appended to the conversation display. This can display intermediate model text as well as the terminal response; it does not wait for the memory task and is not an acceptance certificate for the answer. The direct `graph.ainvoke` demonstration returns graph state instead of using the widget display. SRC-1: `examples/langgraph-agent/agent.ipynb`.

> "                        conversation_output.append_stdout(last_message.content)\n",
> "    except Exception as e:\n",
> "        conversation_output.append_stdout(f'Error: {e}')\n",
> --- `examples/langgraph-agent/agent.ipynb`

This provides a concrete failure path: an exception escaping graph streaming reaches `process_input`, which displays an error. It does not repair graph state, retry the request or roll back already displayed text. A separately scheduled ingestion task is outside that streaming exception handler; its failure is not converted here into a failed conversation result. Tool exceptions may be intercepted by external framework code, whose policy is not established by this source. Thus delivered text, successful graph termination and completed memory persistence are separate outcomes. Successful execution and recovery reliability remain unobserved. SRC-1: `examples/langgraph-agent/agent.ipynb`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop)

Workflow delegation: the user submits a message; notebook code assembles context; the model proposes tool calls; the conditional graph delegates to the bound tool and then returns to the agent. No-tool output is the termination predicate, not answer-quality verification.

Workflow verification and delivery: widget code checks message type and string content before displaying streamed model text. There is no separate answer-review node in the inspected notebook. Display and graph termination do not certify memory completion.

Workflow recovery: escaping stream exceptions are displayed to the user. The notebook supplies no explicit retry or compensation for that path. Independently scheduled episode admission has no awaited completion or notebook-owned retry handle. External tool-node exception policy is uninspected.

Workflow memory handoff: admission is scheduled on each chatbot response, including tool-call rounds; the episode body prefixes the latest state message with the user name even when the latest message is a tool result. This limits interpreting each stored episode as a faithful completed human/assistant turn. Evidence and verbatim passages are retained in the Workflow account above.
