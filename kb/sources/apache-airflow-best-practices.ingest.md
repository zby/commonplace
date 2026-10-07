---
description: "Airflow's official guidance separates stable retry inputs, complete outputs, durable task handoffs, and failure-preserving status for workflow design."
source: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
captured: "2026-10-07"
capture: trafilatura
capture_scope: full-source
genre: official-statement
snapshot_sha256: 0f23bf98fa39fa0204b7a350a5b5d74a406dd35ae38e2e04769fddf9135c9f4f
ingested: "2026-10-07"
occasion: "We need a simple model that can support all of these interactions."
type: types/ingest-report.md
domains: [workflow-orchestration, retry-safety, task-communication, observability]
---

# Ingest: Apache Airflow best practices

## Classification

Official project documentation prescribing how to author, test, and operate Airflow workflows. Its examples explain intended behavior and author responsibilities; they are not a comparative empirical evaluation.

Author: Apache Airflow project, the maintainer of the system whose behavior and interfaces the page describes.

## Summary

Airflow recommends treating tasks like database transactions: avoid incomplete results and make repeated execution produce the same outcome. Its concrete rules include UPSERT rather than duplicate-producing INSERT, reading and writing named partitions rather than changing “latest” data, and avoiding wall-clock time in critical computation. Task communication should use small XCom messages and remote storage for larger payloads because workers may not share local files. Other guidance separates frequently repeated DAG parsing from task execution, describes a watcher that prevents successful teardown from masking upstream failure, and covers loading, structure, operator, integration, and output checks. The page also explains dependency-isolation tradeoffs and maintenance precautions. These are task-authoring obligations within Airflow, not a promise that the runtime makes arbitrary external effects atomic or exactly once.

## Quotes

> You should treat tasks in Airflow equivalent to transactions in a database. This
> implies that you should never produce incomplete results from your tasks.
> --- `kb/sources/.snapshots/apache-airflow-best-practices.md` @ `sha256:0f23bf98fa39fa0204b7a350a5b5d74a406dd35ae38e2e04769fddf9135c9f4f` — Creating a task

> Airflow can retry a task if it fails. Thus, the tasks should produce the same outcome on every re-run.
> --- `kb/sources/.snapshots/apache-airflow-best-practices.md` @ `sha256:0f23bf98fa39fa0204b7a350a5b5d74a406dd35ae38e2e04769fddf9135c9f4f` — Creating a task

> Read and write in a specific partition. Never read the latest available data in a task. Someone may update the input data between re-runs, which results in different outputs. A better way is to read the input data from a specific partition.
> --- `kb/sources/.snapshots/apache-airflow-best-practices.md` @ `sha256:0f23bf98fa39fa0204b7a350a5b5d74a406dd35ae38e2e04769fddf9135c9f4f` — Creating a task

## Connections Found

For the requested simple interaction model, this source is a concrete design reference for separating task dependencies from the guarantees at each task boundary. It compares with [Agent orchestration needs coordination guarantees, not just coordination channels](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md): passing a storage path solves payload access only if the downstream worker can reach the named data; choosing XCom does not settle ownership or semantic consistency. Its fixed-partition rule supplies a documented boundary example for [LLM↔code boundaries are natural checkpoints](../notes/llm-code-boundaries-are-natural-checkpoints.md), specifically the qualification that replay needs relevant state and external dependencies, not merely visible arguments.

The watcher pattern also compares with [Final task success does not establish intended-path health](../notes/final-task-success-does-not-establish-intended-path-health.md) on terminal-status information loss. In Airflow, a successful teardown leaf can mask an upstream failure; a watcher must depend directly on every task it monitors. This differs from successful model-generated fallback, but both show why a final success flag cannot replace intermediate execution evidence. These connections support a small boundary-checking model, not a claim that Airflow covers every agent interaction.

## Extractable Value

1. **Separate the task graph from boundary obligations.** A candidate simple model is a graph of tasks whose boundaries specify input identity, output publication, retry behavior, payload access, and failure reporting. Airflow supplies concrete failure cases for each dimension. This is our synthesis for the occasion, not a model proposed or validated by the source. It makes a graph's missing guarantees visible without introducing a different interaction primitive for every failure. [experiment]
2. **Stable inputs and duplicate-safe effects are different requirements.** Fixing a partition makes retries comparable; UPSERT avoids one form of duplicated mutation. Neither alone ensures complete output publication. This sharpens the checkpoint note's existing replay qualification into separate checks for a KB workflow's source observation and its write effects. Identical rerun outcomes should not be inferred for stochastic model calls. [quick-win]
3. **Pass payload references only with an access contract.** The XCom-plus-remote-storage pattern separates small control messages from large artifacts. Its useful transfer is the downstream-access check, not a requirement that Commonplace use remote storage: a shared local filesystem may suffice when the execution environment guarantees it. [quick-win]
4. **Preserve failure evidence independently of cleanup success.** The watcher example identifies a concrete aggregation defect and its Airflow-specific remedy. For KB workflows, the transferable requirement is to retain task failures when cleanup succeeds; the particular trigger rule and direct-parent wiring are context-bound. [quick-win]

## Limitations (our opinion)

The page is authoritative guidance about Airflow, not independent evidence of achieved reliability. It provides no measured failure rates or comparison of alternative orchestration models. The examples illustrate mechanisms, and the loader timing advice describes how to make a controlled local comparison; neither establishes that the proposed boundary model is sufficient for agent-operated KBs.

The database-transaction analogy does not supply a commit protocol across arbitrary database, object-store, or service effects. UPSERT addresses duplicate rows in the stated example, not every non-idempotent action. A named partition is stable only if the relevant contents remain unchanged. XCom and remote storage alone do not establish delivery, retention, concurrent-write safety, or semantic agreement, matching the distinction in the coordination-guarantees note.

The occasion leaves “all of these interactions” unspecified. This source can inform retry, handoff, and status requirements, but it cannot establish coverage of human approval, delegation authority, concurrent knowledge edits, or model-output interpretation. The captured stable URL is also a moving documentation target; the checksum identifies this observation, not future page contents. Version-specific APIs and historical isolation recommendations require checking before implementation.

## Recommended Next Action

Hold one focused design brainstorm to test a task graph with explicit boundary obligations—input identity, publication, retry safety, payload access, and failure reporting—against the interactions intended by the occasion, marking any interactions the model cannot express.
