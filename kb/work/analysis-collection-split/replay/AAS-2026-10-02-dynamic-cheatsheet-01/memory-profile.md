---
type: work/analysis-collection-split/drafts/agent-memory-profile.md
description: "Memory profile of Dynamic Cheatsheet's caller-supplied query context and returned cumulative sheet"
run-id: AAS-2026-10-02-dynamic-cheatsheet-01
source-identity: "https://github.com/suzgunmirac/dynamic-cheatsheet"
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
memory-comparison:
  scope: "Includes the caller-supplied cumulative cheatsheet, paired prior input/output examples, supplied embedding rows used as access structures, their in-process handling, cumulative writes, retrieval selectors, and later consumers. Excludes caller backing storage and the unregistered CLI persistence path, ordinary client chat history, provider-managed state, static templates, and external embedding production."
  axes:
    storage_substrate:
      assessment: partial
      values: [in-memory]
      evidence:
        in-memory:
          basis: wired
          records: [RT-OBJ-1, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-3]
          note: "The sheet, examples and vectors are passed through method arguments and local processing in memory. Caller backing storage and the documented CLI persistence implementation are outside the registered evidence."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-3]
      note: "In-process storage is established for the inspected memory objects. The records leave the caller's durable backing store and the documented CLI save/resume path unresolved, preventing a complete substrate classification."
    representational_form:
      assessment: known
      values: [natural-language, parametric]
      evidence:
        natural-language:
          basis: wired
          records: [RT-OBJ-1, MEM-OBJ-1, RT-RTE-1, RT-RTE-4, RT-RTE-5]
          note: "The cumulative sheet and paired example strings are text delivered as prompt context or reference."
        parametric:
          basis: wired
          records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
          note: "Caller-supplied dense embedding rows drive cosine ranking; the profile's parametric value classifies this distributed-parametric vector form."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
      note: "The scoped retained text and embedding access structure are both represented. The embedding producer is outside the boundary, but its numeric vector representation is inspected at consumption."
    lineage:
      assessment: partial
      values: [authored, trace-extracted]
      evidence:
        authored:
          basis: afforded
          records: [RT-OBJ-1, MEM-OBJ-1]
          note: "The annotation identifies caller-authored initial sheet text as an available lineage; the caller may also supply example strings, whose origins are not established."
        trace-extracted:
          basis: wired
          records: [RT-RTE-1, RT-RTE-3, EPI-OBJ-8]
          note: "Cumulative routes feed the current query and generator response to a curator, then extract a tagged proposal for return. This establishes a trace-extracted candidate route, not the provenance of every supplied sheet."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-3, EPI-OBJ-8]
      note: "Caller-authored initial text and curator-produced trace-derived candidates are supported. The provenance of supplied prior examples and vectors is unknown, so these values do not cover all included material."
    behavioral_authority:
      assessment: partial
      values: [knowledge, ranking, learning]
      evidence:
        knowledge:
          basis: wired
          records: [MEM-OBJ-1, RT-RTE-1, RT-RTE-3, RT-RTE-4, RT-RTE-5]
          note: "The cumulative sheet and prior examples are supplied to generators as query context or reference; actual model effect is unobserved."
        ranking:
          basis: wired
          records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
          note: "Embedding values determine cosine ordering and selection of paired examples for the current generator or curator request."
        learning:
          basis: afforded
          records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
          note: "The current query and answer feed automatic candidate production, and the returned sheet can be resubmitted to shape a later prompt. This is an afforded trace-fed route, not evidence of improved capacity."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
      note: "Context supply, vector-driven ranking and the afforded trace-fed update route are supported. Whether sheet contents also function as standing instructions is unresolved because the supplied template and sheet contents are unavailable; provider and caller effects are unobserved."
    write_agency:
      assessment: known
      values: [automatic, manual]
      evidence:
        automatic:
          basis: wired
          records: [RT-RTE-1, RT-RTE-3, EPI-OBJ-8]
          note: "The configured model proposes cumulative text and the wrapper automatically extracts a tagged segment into the returned candidate."
        manual:
          basis: afforded
          records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
          note: "The caller supplies the initial sheet and controls whether a returned candidate is stored and resubmitted across calls."
      records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
      note: "Both automatic in-call candidate production and caller-controlled supply or cross-call handoff are described. The caller's external storage mechanism is unresolved, but it does not change who supplies the initial value or chooses resubmission."
    curation_operations:
      assessment: not-determinable
      values: []
      evidence: {}
      records: [RT-RTE-1, RT-RTE-2, RT-RTE-3, EPI-OBJ-8]
      note: "Tag extraction identifies a response segment and its fallback, but the curator template and produced contents are unavailable. Reconciliation specifies that this literal extraction does not establish the unknown operation that produced the candidate, preventing classification among the curation operations."
    read_back_direction:
      assessment: known
      values: [pull, push]
      evidence:
        pull:
          basis: wired
          records: [RT-RTE-1, RT-RTE-3, RT-RTE-4]
          note: "Callers supply the current cheatsheet or choose full-history input, which the wrapper places in the current prompt."
        push:
          basis: wired
          records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
          note: "During retrieval routes, the current query vector automatically selects earlier paired examples by cosine ranking without a request for particular retained items."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
      note: "The supplied sheet/history routes are pull, while similarity selection is push. The route records distinguish the caller's request and approach choice from automatic selection within retrieval."
    read_back_signal:
      assessment: known
      values: [inferred-embedding]
      evidence:
        inferred-embedding:
          basis: wired
          records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
          note: "Push selection compares the current query embedding with earlier supplied embeddings and selects paired rows by cosine similarity and top-k rank."
      records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
      note: "The included push route uses supplied vector similarity as its selector. The embedding producer and vector semantics are unresolved, but the inspected selection signal is embedding-based."
    trace_learning:
      assessment: known
      values: ["yes"]
      evidence:
        "yes":
          basis: afforded
          records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
          note: "Cumulative routes automatically form a candidate from the current query and answer; the returned text can be retained by the caller and supplied to a later consumer. This establishes the afforded trace-fed write path, not observed reuse or improvement."
      records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
      note: "The source records support an afforded trace-fed candidate write whose later use depends on caller resubmission. This classification does not establish durable library storage, activation, or improved future capacity."
    trace_source:
      assessment: known
      values: [session-logs]
      evidence:
        session-logs:
          basis: wired
          records: [RT-RTE-1, RT-RTE-3]
          note: "Both cumulative routes pass the current query and full generated answer to the curator, wiring session conversational input and response into candidate production. This classifies the source feeding the update; later caller resubmission remains afforded and operation, activation, and benefit are unobserved."
      records: [RT-RTE-1, RT-RTE-3, EPI-OBJ-8]
      note: "For the afforded cumulative update route, the original inputs are the current query and answer turn. Other supplied corpus and vector origins remain unknown, and no event-stream, tool-trace or trajectory input is identified for this write."
---

# Dynamic Cheatsheet memory profile

## Comparison rationale

Reconciliation makes `MEM-OBJ-1` the canonical parent of the prior input and output parts `EPI-OBJ-2` and `EPI-OBJ-3`; `MEM-OBJ-2` is canonical for the embedding matrix, superseding `EPI-OBJ-4`. The broad runtime container `RT-OBJ-2` remains valid. `EPI-OBJ-8` remains the curator's proposed segment and is distinct from the admitted cumulative sheet `RT-OBJ-1`; its tag extraction does not identify the content operation that generated it. These dispositions keep the scope's text, vectors, and candidate stage separate.

The profile includes caller-supplied query memory and the routes that access or update it. It excludes direct client chat history, which the memory member classifies as ordinary current-run state, and provider-owned execution state. `RT-OBJ-1`, `MEM-OBJ-1`, and `MEM-OBJ-2` locate the inspected objects in process memory; the documented CLI checkpoint/resume implementation and caller backing store remain outside the registered evidence, so storage is partial. The text and vector objects establish natural-language and parametric forms. Initial caller text is afforded as authored; automatic curator candidates are trace-extracted. The example corpus and vector producer have unknown lineage, so lineage is partial.

The examples and sheet supply context or reference, and vectors rank which paired examples enter a prompt. Cumulative generation also affords learning authority because query and answer traces feed candidate text that can be resubmitted. The uninspected template and sheet contents leave possible instruction authority unresolved. Manual supply and automatic candidate extraction establish both write agencies. The exact content-level curation operation remains not-determinable: the observed extraction only selects a literal response segment, while the operation producing that segment is opaque.

Caller-supplied sheets and full history are pull read-back. Retrieval routes push selected examples using the current query embedding, which is the known read-back signal. The trace-learning value is `yes` at the afforded level for this automatic trace-fed candidate route; later cross-call use depends on caller action. The qualifying write consumes a current query and generated answer, so its trace source is session logs. Neither classification establishes observed activation or benefit. The missing caller persistence path prevents a stronger storage conclusion; missing template and content prevent instruction and curation conclusions; unknown example and vector provenance prevent complete lineage classification.
