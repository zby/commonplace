---
gate: prose/pseudo-formalism
verdict: pass
---

The pseudocode block (`while not satisfied(K): P = select(K); r = call(P); K = K + r`) is doing structural work. The note's claim is that any bounded-call program can be mechanically converted *into this specific loop*. Making the target structure explicit is essential — without it, "the base loop" is an opaque reference to another note.

The notation also enables a non-obvious consequence: by seeing the loop structure, the reader can verify that the three invariants (bounded context per call, explicit state in K, symbolic orchestration) hold by construction.

Mentally deleting the pseudocode leaves the passage less clear: "converted into the base loop" would require following the link to understand the claim. The formalism earns its place.
