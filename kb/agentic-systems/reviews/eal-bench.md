---
type: note
description: "EAL-bench's frozen authorization-memory writer/executor workflow, checkpoint controls and limits of its causal-attribution protocol"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-eal-bench-01
source-identity: https://github.com/tommasocerruti/eal-bench
reviewed-revision: 51648690bc52d7a9c7ac080a2c67a784fe9d56cb
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-eal-bench-01/result.md
analysis-result-sha256: 29384a1855e4f53322b20f00f064691f4a215a050816fe850d4b5bc7e415ad3f
---

# EAL-bench

**Evidence basis:** source code and repository documentation at commit `51648690bc52d7a9c7ac080a2c67a784fe9d56cb`, inspected on 2026-09-25. No benchmark experiment was executed or historical result evaluated.

EAL-bench's inspected core is a model-dependent benchmark workflow: a writer compresses organizational authorization history into memory, an executor receives that frozen memory and a new request, and deterministic code compares the resulting tool choice with a hidden authorization ledger. The selected subsystem covers the four core writer conditions, current study orchestration, checkpoint recovery and reusable evaluation tracks. Detailed domain semantics are grounded in procurement; optional mitigation and extension studies are outside this review.

## Runtime and control

One-shot writers receive the whole history. Incremental writers receive the previously accepted profile and the next block, then propose a free-text or typed replacement. Validation checks the update operation, schema, visible source references and budget. A bounded optional repair call can consume a rejected update and validation feedback; failed updates retain the prior accepted state. These checks enforce representation and protocol constraints, not semantic faithfulness. The accepted profile is frozen before executor evaluation. See exact-result OBJ-2, OBJ-7, RTE-7 and RTE-10; [writer/executor pipeline](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/experiments/authorization_memory/pipeline.py) — evidenced-by.

The executor proposes a terminal tool action. The core scorer selects the first consequential action when present and evaluates its arguments against the domain oracle. It does not execute a real purchase. Provider errors, malformed responses and authorization decisions remain distinct outcomes. A separate generic tool-loop helper can invoke caller-supplied handlers; its effects and deployment permissions belong to that caller, so the benchmark scorer is not a universal authorization gate. See RTE-2, RTE-5 and RTE-6; [generic model client](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/src/eal_bench/llm/client.py) — evidenced-by.

Current study execution writes a pre-executor checkpoint containing memory evidence, execution plans, hashes and logs. Resume checks the frozen files and planned calls, rejects inconsistent histories, and schedules missing successful calls. This controls benchmark replay population and identity; it does not establish exactly-once execution at a remote provider. Source-level provider and model names do not pin inaccessible model weights. See OBJ-6 and RTE-3; [study checkpointing](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/experiments/authorization_memory/study_engine.py) and [resume validation](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/experiments/authorization_memory/resume.py) — evidenced-by.

## Memory and evaluation

Retained profiles live in Python state and JSON/JSONL artifacts. Free-text and symbolic typed records both have later writer and executor consumers. The comparison's trace-learning classification identifies these staged trace-to-memory routes, including rejected-update repair; it does not assert improved behavior. Packaged writer-memory retrieval additionally affords requested replay. The case/session organization does not settle whether the retained knowledge spans tasks or projects.

Memory payloads supply authorization evidence. Included checkpoint metadata also determines validation, routing and refusal of invalid resume operations. That authority is scoped to benchmark continuation, not organizational permission. Automatic whole-profile delivery and identity joins are clear, but intermediate typed checkpoint diagnostics also select witnesses using substantive-overgrant screening; the aggregate read-back signal remains not determinable in the comparison vocabulary. These distinctions and the complete fourteen-axis profile are retained in the exact result.

The reusable evaluator separates preservation, propagation and end-to-end attribution. Its end-to-end rules combine memory formation, an unauthorized executor action and comparison with exact memory, while checking matched resource, surface and executor identity. Free-text preservation requires accepted hash-bound annotations. These are implemented evaluation protocols; their presence alone supplies no observed effect size or causal result. See RTE-4 and CLM-3; [end-to-end evaluation](https://github.com/tommasocerruti/eal-bench/blob/51648690bc52d7a9c7ac080a2c67a784fe9d56cb/src/eal_bench/eval/end_to_end.py) — evidenced-by.

## Epistemic assessment and scope

The strongest supported contribution is an executable way to distinguish memory formation errors from downstream propagation and baseline executor behavior. Structural admission of memory, semantic evaluation against a ledger, action classification and attribution have separate authority. Typed structure exposes individual authorization fields to inspection; it does not make their content true. Supplied ledger semantics are benchmark ground truth by construction, not independent evidence about real organizational policy.

The workflow can criticize memory content. Whether that criticism improves future capacity remains **uninspected**: no linked improvement experiment or automatic theory-revision and successor-deployment loop is established at this boundary. Reflection and self-improvement are separately **uninspected**, not inferred from storing profiles or scores. Packaged replay artifacts exist, but their original production and acceptance lifecycle is not determinable from the inspected fixture bytes.

Provider and LangMem internals, excluded studies, other domains' detailed semantics and deployment effects remain outside the evidence boundary. Current-pin paired memory/control runs, audited free-text interpretations and repeated interventions would change the empirical assessment. The full routes, quotations, limitations and specialist reconciliation are in the [retained exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-eal-bench-01/result.md) — see-also.

- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: the separate requirement for criticism to improve future capacity.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: a connected self-representation, not memory persistence alone.
