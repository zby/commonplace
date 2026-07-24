---
description: "Theory, description, prescription are recurring attractors, not a provable partition; formulation constraint and maintenance asymmetry make the split real; content is orthogonal to operational roles"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
---

# A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking

Many knowledge bases repeatedly need three default text-contract profiles, each with a different quality priority:

| Default profile | What it does | Quality priority | Context-efficiency strategy | Example query |
|---|---|---|---|---|
| **Theory** | Makes transferable claims about what is true | [Explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) | One claim covers many situations — compress *across* contexts | "Why is X a good idea?" |
| **Description** | Accounts for what exists in a particular system | Fidelity + economy | One account covers the system in minimum tokens — compress *within* a single context | "How does X work here?" |
| **Prescription** | Directs what to do or not do | Executability + precision | One instruction says exactly what to do — compress to what's *actionable* | "How do I do X?" |

These are recurring defaults, not a partition of all knowledge. A stance-neutral dialectical/evidential collection, for example, needs a different quality bar: faithful attribution of a live disagreement rather than the collection's own claim about what is true. [ADR 042](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) therefore makes the [profile](./definitions/text-contract.md) library open and worked-case-gated. A default earns its place when adopting the bundle saves repeated contract decisions and improves writing or review. A collection whose needs do not fit should write its own contract.

All profiles face bounded-attention pressure. In LLM-operated KBs, [context is the single scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), so excess or ambiguous text directly competes with the next action. Reach, fidelity, economy, executability, and precision are not exclusive properties—every artifact benefits from several—but each profile identifies the failure its writers and reviewers should treat as decisive.

## Why the profiles are useful

**Formulation discipline.** Commonplace's theoretical profile requires a claim to stand without reference to any particular system. Descriptions may supply evidence, but removing any one described system should not collapse the claim. This constraint enables transfer across contexts. It is a deliberate convention of this profile, not a claim that system-specific causal explanations are never theories in ordinary language.

**Distinct review priorities.** A theoretical artifact fails when it merely records local fit without a transferable explanation. A descriptive artifact fails when it misstates its referent or spends context without improving fidelity. A prescriptive artifact fails when a first-time executor cannot determine what to do. The profiles are useful to the extent that these bundled priorities recur together.

## Maintenance follows dependency and authority edges

Profile membership does not itself determine change impact. The primary record is the authored dependency: what cites what, under which relationship, plus the operational authority of the consuming path. Profiles supply useful defaults for which dependencies are common, but explicit edges override the default.

| Authored dependency | Meaning | Revision trigger |
|---|---|---|
| Theory cites description as `evidence` | The observation supports the claim | If the description or its referent changes, reassess the theory; other evidence may let it survive |
| Prescription cites theory as `rationale` | The procedure is justified by the claim | If the theory changes, reassess the procedure |
| Description cites theory as `rationale` | The system was shaped by the claim | If the theory changes, check the rationale; the description still follows the implemented referent |
| Prescription cites description as `operates-on` | The procedure acts on the described system | If the system changes, revise the procedure |

The asymmetry is therefore characteristic rather than absolute. Theoretical artifacts often accumulate descriptive evidence and provide the rationale for prescriptions; descriptions track changing referents; prescriptions track both their rationale and the systems they operate on. But a schema-first description can be upstream of implementation, and a theory that rests on one volatile observation can be downstream of that evidence. Maintenance should follow the recorded dependency, not an inference from genre.

## One common path connects the profiles

Derivation and implementation often connect the profiles in a deliberately designed system:

```
theory  →  prescription  →  implementation  →  description
(claim)    (procedure)      (working system)    (account of what exists)
```

Theory explains why. A prescription condenses that reasoning into executable guidance. Implementation encounters constraints the theory did not settle, and description records what was actually built. The description must remain faithful even when implementation deviates from the originating rationale.

This is one common path, not an origin law for descriptions. Existing systems are often described before anyone writes a theory about them; observations can revise theory; schema-first descriptions can direct implementation; and procedures can arise from local necessity without a general principle. These feedback and independent-origin paths are why the dependency edges, rather than the diagram, control maintenance.

## Content profiles and operational roles are independent

Profiles classify what an artifact *says*—its linguistic content. Artifacts also have operational roles: what they *do* in the KB.

| Operational role | What the artifact does |
|---|---|---|
| Evidence | Supports or challenges a claim |
| Executable instruction | Directs behavior at runtime |
| Generated report | Records the output of an operation |
| Routing surface | Helps consumers find other artifacts |

These roles cross-cut content. A generated review report is descriptive; an index is a routing surface whose text describes what exists. An agent instruction illustrates the important dual case: it is prescriptive by content and executable by operational role. Its immediate maintenance consequence comes from that authority path—changing loaded instruction text changes system behavior—not from prescriptive wording alone. The content profile tells a writer how to formulate the artifact; operational roles and dependency edges tell a maintainer what the artifact can affect.

## Evidence from this KB

Commonplace's existing collections instantiate the three defaults:

- `kb/notes/` → theoretical register (transferable claims, [title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md), optimized for explanatory-reach)
- `kb/reference/` → descriptive register (how the shipped system works, topical titles, optimized for fidelity)
- `kb/instructions/` → prescriptive register (procedures and conventions, imperative titles, optimized for executability)
- `kb/agent-memory-systems/` → another descriptive collection for an external landscape

This separation emerged from practical pressure: `kb/reference/` was created because shipped-system documentation did not fit theory-oriented conventions. This worked example shows that the bundles can organize one KB, but it does not establish how often they recur elsewhere.

## Practical consequences

1. **Declare the actual contract.** Adopt a default profile when its orientation, quality priority, maintenance semantics, and link grammar travel together. Extend or replace it when they do not.
2. **Choose an encoding that matches operation.** A KB may attach profiles to directories, types, metadata, or conventions. Commonplace uses directories because collection-wide rules must cover every artifact in a subtree. This choice is an implementation detail, not part of the content taxonomy.
3. **Review dependencies explicitly.** Use profile defaults to guide prospecting, but use authored relationship labels and operational authority to decide what a change can invalidate.

## Open questions

- Across independently designed KBs, do orientation, quality goal, title convention, and maintenance semantics covary strongly enough for these three bundles to remain useful defaults?
- After explicit dependency kinds and operational authority are known, what additional maintenance or review decision does profile membership predict?
- How robust must a theory's evidence base be? A theory with one supporting observation is fragile. Is there a practical threshold (two systems? three?) or is this a judgment call?

---

Relevant Notes:

- [First-principles reasoning selects for explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — foundation: the explanatory-reach concept that serves as the quality criterion for the theoretical register
- [Why directories despite their costs](./why-directories-despite-their-costs.md) — extends: the three-register split provides a principled reason for directory-level separation beyond topic grouping
- [Skills derive from methodology](./skills-derive-from-methodology.md) — exemplifies: methodology → skill is an instance of the theory → prescription derivation path
- [Instructions are typed callables](./instructions-are-typed-callables.md) — extends: the instruction duality (prescriptive content, executable authority) is a specific case of treating documents as typed callables; the callable framing captures the operational-authority axis
- [Text contract](./definitions/text-contract.md) — defined-in: the requirement and profile vocabulary that replaces "register" as the taxonomy name
- [ADR 042: register becomes a default profile under open-ended text contracts](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — rationale: the decision that weakens this note's exhaustiveness claim to an attractor claim and opens the profile set
