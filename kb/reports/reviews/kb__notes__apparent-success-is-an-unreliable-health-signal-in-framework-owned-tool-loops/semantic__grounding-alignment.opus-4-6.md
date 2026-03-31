The note cites seven KB notes. Central claims traced below.

---

**Claim: "traditional debugging intuitions break when tool loops can recover semantically"**

Cited to the note of the same name. The current note extends this: "Programmers trained on traditional systems are particularly vulnerable" because success was a rough proxy for mechanism health. ✓

**Claim: tool-loop index argues for keeping orchestration visible**

Cited to [tool-loop-index.md]. The inference — hidden orchestration hides failure handling — is a valid extension of the visibility argument. ✓

**Claim: the phenomenon sits at the boundary between scheduler and execution substrate**

Cited to [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md]. The characterization — "The scheduler asks for a capability; the substrate attempts the tool call; the runtime decides whether the error is terminal or recoverable" — maps accurately to the three-part decomposition. ✓

**Claim: "does not modify the bounded-context orchestration model"**

Cited to [bounded-context-orchestration-model.md]. The note says the clean model "abstracts over how a bounded call is realised" and the issue is "one layer down, in execution substrate policy." This accurately places the concern below the scheduler abstraction level. ✓

**Claim: enforcement without structured recovery is incomplete; recovery without observability is also incomplete**

Cited to [enforcement-without-structured-recovery-is-incomplete.md]. The note extends: "Recovery strategy is only half the problem. The other half is observability." INFO — this extension adds a claim (observability is the other half) that may not be in the cited note. The extension is plausible but is the current note's own contribution.

**Claim: unit testing with mocked tool boundaries catches instruction regressions but not path/credential failures**

Cited to [unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md]. The limitation claim is reasonable — mocks by definition don't test real tool infrastructure. ✓

---

No WARN. One INFO: the observability extension of the enforcement-without-recovery note.
