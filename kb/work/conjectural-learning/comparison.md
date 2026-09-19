# Modern-paper comparison

Coverage: four full papers, two author abstracts, one bibliographic record.
[Sources](./sources.md) records capture and access limits. Source-side details
below require the ingests' paired snapshots.

## Contributions and boundaries

| Source | What changes or is proposed | What the evidence establishes and leaves open |
|---|---|---|
| [Huang et al., POPPER](../../sources/automated-hypothesis-validation-sequential-falsifications.ingest.md) | Generates sub-hypotheses, tests, analyses, and execution code for a supplied main hypothesis | Implemented and evaluated; error control depends on valid claim-to-test implications and conditional statistical validity. Main-theory revision and retention are not demonstrated; data, agent roles, statistical interface, and decision policy remain supplied |
| [Thomas, Error-Centric Intelligence I](../../sources/error-centric-intelligence-beyond-observational-learning.ingest.md) | Proposes changes to representations, variables, mechanisms, intervention semantics, and hypothesis spaces | Theoretical programme with proposed conventions and conditional arguments, not an evaluated learner that originates and retains those changes |
| [Mills and Lewis 2025](../../sources/think-before-you-act-popperian-expectations-abstract.ingest.md) | Abstract proposes creating, updating, and reusing simulation-derived causal expectations through Expectation Event Calculus | Update rules, environmental refutation, persistence evidence, and revisability of the calculus or simulator cannot be assessed from the abstract |
| [Salmani and Lewis](../../sources/reflective-architecture-llm-based-systems-abstract.ingest.md) | Abstract combines formal social expectations and self-simulation to reconsider decisions | Reported alignment improvement lacks assessable methods and results here; changes to expectations, simulator, or learning machinery remain unknown |
| [Zhang et al.](../../sources/llms-scientific-method-hypothesis-to-discovery.ingest.md) | Surveys observation, hypothesis proposal, experimentation, and automation across arrangements using plans, code, skills, and trained representations | Perspective and cited cases, not a new controlled evaluation of one architecture that revises all those arrangements |
| [Mills and Lewis 2026](https://2026.acsos.org/details/acsos-2026-workshops/16/Popperian-Expectations-for-One-Shot-Adaptation-in-Dynamic-Environments) | Unknown | Title/authors/presentation only; no mechanism or outcome claim is assessable |
| [İşcan](../../sources/scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md) | Compares generated programs under full-skill, labels-only, placebo, and vanilla prompts; also tests small-model candidate selection | Controlled prompt study with an execution oracle; no separable full-skill advantage over labels-only in these settings. Fixed benchmark, tests, prompts, and model do not test persistent machinery learning |

Locators: POPPER §§2.3–3, §4, Figure 11, Appendix C; Thomas §§1.3–1.4,
§2, §§3–4; Zhang “Augmenting the scientific method,” “Validation,”
“Human–LLM interaction,” and “Conclusions,” pp. 4–10; İşcan experimental
design, Tier 1/Tier 2 results, and limitations. The two IEEE ingests cover only
the author-lab abstracts.

## Implications

**Separate epistemology from realization.** The [commission](./README.md)
rejects symbolic formalization as the general starting point. The papers help
compare implementations: POPPER starts with a free-form hypothesis and builds
tests; the expectations abstracts name a formal calculus. Neither arrangement
defines the general ontology supplied by the [Popper reading](./popper-foundation.md).

**Criticize the claim-to-test mapping.** POPPER's statistical aggregation
cannot guarantee that generated tests bear on the intended claim. Zhang also
warns that translating a hypothesis into a formal language can introduce
errors despite subsequent checking. Making that mapping criticizable is our
inference; neither paper demonstrates a fully reliable revision mechanism.

**Representation change is an option, not a guarantee.** Thomas's causal
non-identifiability argument limits observational evidence; it does not show
that every failure needs a new representation or that greater expressiveness
supplies missing evidence. A model's fixed hypothesis class must also be
distinguished from a whole agent's effective repertoire of programs, tools,
and retained state. Do not import the paper's stronger AGI definitions as
established necessities.

**Test the procedure, not its label.** İşcan's high-capability comparison is
near ceiling. Small-model full and labels-only prompts have equal aggregate
best-of-eight results but disagree by task: non-separation, not equivalence.
Best-of-eight success is not successful selection; the same-model selector
showed no advantage over its random references. Structural controls and
independent outcomes are needed to identify what criticism actually changes.

The set does not establish reliable general LLM conjectural learning,
sufficiency of fixed weights, the claimed efficiency advantage of retaining
theories over reconstructing them from records (including its dependence on
context limits), or cumulative gains from machinery revision. Reconstruction
is an implementation approach, not excluded by this evidence limit.
Missing full texts may change particular architecture assessments; abstracts
and titles supply neither positive nor negative findings about their omitted
mechanisms. These limits carry into the [definition drafts](./definitions/).
