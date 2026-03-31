The note cites seven linked notes/sources across its five dimensions. Central claims traced below.

---

**Claim: scheduler placement — LLM-mediated vs. symbolic**

Cited to [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md] and [bounded-context-orchestration-model.md]. The framing as "clean-model / degraded-model split" accurately represents the relationship between these two notes. ✓

**Claim: RLM is a boundary case — scheduler on exact substrate, but model authors some of the scheduler code**

Cited to [rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md]. The characterization captures RLM's distinctive feature: the model writes code that runs outside the chat context. ✓

**Claim: coordination forms "are not reducible to one another and can combine with any scheduler placement"**

Cited to [conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md]. This is the independence claim — coordination form varies independently of scheduler placement. INFO — I have not read the cited note to verify that it demonstrates irreducibility and independence. The claim is structurally important to the multi-dimensional thesis; if the cited note shows these forms are merely variants of the same underlying mechanism, the independence claim would be weakened.

**Claim: coordination form ≠ coordination guarantee**

Cited to [agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md]. I have read this note — it argues that the same channel can exist with or without guarantees, which is exactly what the current note uses it for. ✓

**Claim: "Slate adds a new combination because it changes persistence horizon and boundary-return artifact simultaneously"**

Cited to [slate-moving-beyond-react-and-rlm.ingest.md]. INFO — this is an empirical characterization of Slate I cannot verify without reading the source. The argumentative role is exemplification (showing the multi-dimensional framing handles new systems), which is modest.

**Claim: "Forking changes coordination form without changing scheduler placement"**

Cited to [voooooogel-multi-agent-future.ingest.md]. INFO — same as above; I cannot verify this characterization. The claim is modest (one dimension varies while another holds constant).

**Overall scope**

The note's claims are appropriately modest — it proposes a framing (multi-dimensional space) rather than strong causal claims. The linked notes provide the theoretical content for individual dimensions; this note's contribution is the separation argument. The risk of grounding misalignment is lower for framing notes than for mechanistic claims.

---

No WARN. Three INFOs: unverified independence claim from coordination forms note, and two unverified empirical characterizations (Slate, forking).
