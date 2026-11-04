---
description: Frontloading can specialize instructions for known inputs; the partial-evaluation comparison requires preservation of meaning, which shared text alone does not establish
type: types/note.md
traits: []
tags: []
---

# Frontloading can specialize instructions around known inputs

[Frontloading](./frontloading-spares-execution-context.md) computes known instruction inputs before a consuming LLM call and inserts the results. When it replaces work that depends on those inputs while leaving the remaining task open, it resembles program specialization. This comparison helps identify what can be computed early and what behavior the replacement needs to preserve.

For example, an instruction can ask an agent to list a directory and choose a file relevant to the user's request. Frontloading supplies the listing in advance and leaves the choice to the agent. The listing is static for the specialization; the request is an input the resulting instruction still accepts. This constructs a candidate specialized instruction. Whether it preserves the original instruction's meaning is a separate question.

Partial evaluation (PE) specialises a program P with respect to known **static** inputs s, producing a **residual program** Ps that needs only the remaining **dynamic** inputs d:

```
[[Ps]](d) = [[P]](s, d)
```

| PE concept | Candidate mapping to frontloading |
|---|---|
| Program P | The instruction set (CLAUDE.md, skills, prompts) |
| Static inputs s | Inputs fixed at specialization time (paths, file listings, config, search results over stable content) |
| Dynamic inputs d | Inputs left open by that specialization, such as a later request or task state |
| Residual program Ps | The frontloaded instructions — static sub-procedures replaced with their results |
| Binding-time analysis | The author's judgment about what depends on runtime context vs what doesn't |
| Specialisation | The build-time/setup-time step that produces concrete instructions |

[Build-time template expansion](./generate-instructions-at-build-time.md) binds known values before execution. Its expansion rules can be checked separately from the behavior of the resulting prompt under a model. Correct expansion alone does not establish equivalence to a prompt that asks the model to resolve the values itself.

## What preservation requires

Applying the equivalence equation above to prompts requires a governing reference and a stated comparison:

- Under an adopted model package, precise semantics can exist. Whether a particular substitution can be checked affordably depends on the behavior of interest, available tools and budget, as the [definition of opacity](./definitions/representational-form.md#opacity-and-inspection) requires.
- Under English requirements, the caller, reviewer or stated conventions must settle the applicable reading before judging preservation. A substitution can satisfy that requirement without reproducing the original model behavior.
- Some substitutions may admit a proof of equivalence under the chosen reference. Where no affordable proof is available, behavioral tests provide evidence for the tested cases; they do not establish the equation for every remaining input.

The comparison must also say which effects matter. Replacing “list the files, then answer” with a supplied listing removes a tool call. Equality of the full execution trace is therefore different from preservation of the answer's required properties. The listing must remain valid for the consuming call, as the [frontloading note](./frontloading-spares-execution-context.md) requires.

Frontloading targets execution-context savings and may improve reliability. Those benefits need their own assessment; neither follows from semantic equivalence alone.

## What the shared medium establishes

Instructions and supplied results can both enter the [same token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md). This makes textual insertion convenient. It supplies neither the static/dynamic distinction nor the equivalence required by the equation. Those are obligations of the specialization, whatever representation carries the program and its inputs.

Breaking a task into stages describes its organization. Specializing instructions for known inputs describes a transformation and its preservation obligation. The two descriptions need not compete. Frontloading is useful even where equivalence has not been established; in that case, the partial-evaluation comparison guides the checks rather than certifying the transformation.

---

Relevant Notes:

- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — grounds: defines the frontloading operation and its context-saving rationale
- [LLM contexts interpret instructions and content through the same token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md) — enabling property: the shared token medium allows textual insertion; it does not establish semantic equivalence
- [Prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: the governing reference determines the comparison; inspection cost and evidence of preservation remain separate questions
- [Generate KB skills at build time, don't parameterise them](./generate-instructions-at-build-time.md) — exemplifies: template expansion binds known values before the consuming call
- [Model-resolved indirection adds interpretation work to LLM execution](./model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — exemplifies: upstream variable resolution removes work from the consuming call; behavior preservation is a separate check
- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — broader frame: the scheduling model treats frontloading as the single-step case
