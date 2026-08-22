# Bound-variable sweep findings

## Result

No sampled title, description, or opening argument carries a free
choice-variable.

| Sample | Pass | Fail | Ambiguous | Observed failure rate |
|---|---:|---:|---:|---:|
| Top-level `kb/notes/` | 20 | 0 | 0 | 0/20 (0%) |
| `kb/notes/definitions/` | 7 | 0 | 0 | 0/7 (0%) |
| Combined | 27 | 0 | 0 | 0/27 (0%) |

This is a sample result, not proof that every note conforms. In particular,
the fixed definition sample did not select the machinery-first candidates
`answerability.md` and `text-contract.md`, or the mixed
`discovery-lifecycle.md`, from the separate definition audit.

## Sampling and judgment

The frame matched the task: 310 Markdown files directly under `kb/notes/` and
23 directly under `kb/notes/definitions/`. Within each set, files were sorted
by filename and numbered from one. The top-level sample contains ordinal
positions 15, 30, ..., 300. The definition sample contains positions 3, 6,
..., 21. This produces seven definition rows; the task's “approximately 8” is
the rounded value of 23/3, not an instruction to add a substitute or endpoint.

Each whole file was read. The measured verdict covers its title, description,
and opening argument. Later material was checked separately. The three-part
test in the task was applied conjunctively:

1. the claim names or presupposes a choice made by a particular system;
2. it presents as general without scoping that choice; and
3. changing the choice changes the claim's truth conditions.

Generic and conditional grammar counts as binding. “A system that chooses
X,” “for runtimes organized as X,” and “under X” range over systems or scope
the claim to the selected design even without the literal phrase “for any.”
An explicitly local report does not present as general. A named external or
local case used after a general claim is an illustration or witness.

For Commonplace vocabulary, the task's removal test controlled: if replacing
the local term with its general description leaves the claim intact, the term
is a label for the general pattern rather than a free variable.

## Top-level dispositions

| Ordinal | Path | Verdict | Basis |
|---:|---|---|---|
| 15 | `kb/notes/a-retained-instruction-preserves-what-testing-selected.md` | pass | The candidate-selection situation is generic. No particular retained instruction or system supplies the claim's truth. |
| 30 | `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md` | pass | “For runtimes organized as repeated bounded model calls” scopes the architectural premise; practitioner systems are later mappings. |
| 45 | `kb/notes/areas-exist-because-useful-operations-require-reading-notes-together.md` | pass | Replacing “areas” with “bounded note sets read together” preserves the title and argument. The `COLLECTION.md` sentence is removable local framing. Later choice residue is recorded below. |
| 60 | `kb/notes/candidacy-evidence-licenses-escalation-not-acceptance.md` | pass | The evidence roles range over staged workflows. The idealization assessment is explicitly the one worked witness. |
| 75 | `kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md` | pass | “A system that keeps revising...” binds the retained-change design; the named studies are evidence for the general measurement claim. |
| 90 | `kb/notes/decomposition-heuristics-for-bounded-context-scheduling.md` | pass | The claims range over programs and schedulers satisfying stated preconditions, not over one selected Commonplace schedule. |
| 105 | `kb/notes/elicitation-requires-maintained-question-generation-systems.md` | pass | The strategies and maintenance loop are general design claims; roles, checklists, and probes are illustrations. |
| 120 | `kb/notes/feasibility-is-the-heaviest-forks-net-load.md` | pass | “Under sub-agent decomposition” explicitly scopes the design choice whose consequence the note derives. |
| 135 | `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` | pass | The Gödel machine is a named comparison witness. Its selected proof gate establishes a claim about the design space rather than silently supplying local truth conditions. |
| 150 | `kb/notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md` | pass | The opening ranges over agents and domain KBs. The always-loaded premise is part of the kind described, while Commonplace's realization appears only as later current-state material. |
| 165 | `kb/notes/llm-code-boundaries-are-natural-checkpoints.md` | pass | The claim ranges over systems that interleave LLM components and deterministic code; no particular boundary layout is assumed. |
| 180 | `kb/notes/maintenance-capacity-must-match-harmful-artifact-inflow.md` | pass | “An agent-maintained system” binds the system class and the opening states its rate condition. The Codex repository and this KB are later applications. |
| 195 | `kb/notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md` | pass | The opening concerns any repair loop with the stated acceptance criterion. The 2026 repository pass is explicitly a later witness. |
| 210 | `kb/notes/process-structure-and-output-structure-are-independent-levers.md` | pass | Removing “that the KB has been treating as one” leaves the two-lever claim and its truth conditions unchanged. |
| 225 | `kb/notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md` | pass | Episodes and rules are generic retention forms. The choice is stated as a variable over memory designs, not as one system's unspoken selection. |
| 240 | `kb/notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md` | pass | “When” scopes the material-size condition, and the decomposition is argued as a general response rather than reported as a local implementation. |
| 255 | `kb/notes/stale-self-description-conceals-its-own-staleness.md` | pass | “A system that retains...” binds all three architectural premises. Commonplace's freshness baseline is explicitly a later witness. |
| 270 | `kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | pass | The title and opening assert a general relation between verification cost and automation; the five systems and domains are supporting cases. |
| 285 | `kb/notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md` | pass | The local sentence about how “This KB treats” the mechanisms can be removed without changing the causal-chain hypothesis attributed to Tu. |
| 300 | `kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md` | pass | The opening quantifies over checks, domains, and artifact classes. Exo is a later case used to test and bound the general claim. |

## Definition dispositions

| Ordinal | Path | Verdict | Basis |
|---:|---|---|---|
| 3 | `kb/notes/definitions/behavior-determining-organization.md` | pass | The term names retained structure that causally affects later behavior across systems; the self-improving-system definition is a use, not the source of its truth. |
| 6 | `kb/notes/definitions/constraining.md` | pass | Removing “In this KB, it names a core deploy-time learning mechanism” leaves the semantic-narrowing definition and spectrum intact. |
| 9 | `kb/notes/definitions/directed-reading.md` | pass | The workshop selected the label and sharpened its boundary, but the three-condition reading pattern survives without that local naming history. |
| 12 | `kb/notes/definitions/knowledge-artifact.md` | pass | The category states a cross-system distinction between advisory consumption and binding behavioral force. |
| 15 | `kb/notes/definitions/operative-part.md` | pass | The part-level unit follows from behavior-affecting consumption paths across artifacts and systems, not from a Commonplace package choice. |
| 18 | `kb/notes/definitions/representational-form.md` | pass | “This KB uses three coarse forms” reports local vocabulary, but the later two-axis derivation supplies a contestable cross-system classification independent of that report. |
| 21 | `kb/notes/definitions/storage-substrate.md` | pass | The location/form/authority distinction ranges over repositories, databases, vector stores, registries, services, and model stores. |

## Later choice-dependent residue

One sampled note contains free or direct choice propositions after its opening:
`kb/notes/areas-exist-because-useful-operations-require-reading-notes-together.md`.
They do not change its measured verdict under the task's stated boundary.

- “The split threshold of ~40 notes isn't arbitrary — it's the approximate
  point where an area stops fitting in working context.” The exact threshold
  is a Commonplace selection presented as though context limits determine that
  value generally. **Repair: bind.** State the general dependence on usable
  context budget and present Commonplace's former threshold as one witness.
- “Single-area membership is the default.” The default is a selected policy;
  the surrounding duplicate-load mechanism does not determine it uniquely.
  **Repair: relocate** the policy record, or **bind** the surviving theory as:
  for systems that load each area independently, multiple membership repeats
  context cost and must earn that cost.
- The assertions about the `areas:` field, Topics footers, “Related Areas”
  links, and `areas.md` describe selected machinery. **Repair: relocate** if
  they remain historically useful; otherwise retire them with the superseded
  area implementation. Their causal rationale can stay only after being
  restated over any system that chooses comparable machinery.

Other local-looking later passages do not meet all three conditions. The
Commonplace comparison in the Gödel-machine note is explicitly particular;
the repository episode in the narrowing note is an illustration; and the
freshness-baseline sentence calls itself “one witness.”

## Hard cases and what they expose

### A local label can sit inside a general claim

The areas note was the hardest top-level case. “Area” was also the name of
selected Commonplace machinery, but the opening mechanism survives as a claim
about bounded, related note sets. Treating every local noun as a failure would
misclassify this note; treating every use of the noun as harmless would miss
the later policy residue.

The opening clauses in the process/output and topology/isolation notes have
the same smaller shape. Each reports how this KB organized a subject, but the
substantive claim remains unchanged when that report is removed.

### A chosen name is not necessarily chosen machinery

Definitions necessarily select words and boundaries. That alone cannot make
every definition a free choice-variable. `directed-reading.md` explicitly
names workshop usage, `constraining.md` says how this KB uses the term, and
`representational-form.md` declares a three-form vocabulary. They pass because
their underlying distinctions can be stated and contested across possible
systems. A definition would fail when removing the local term also removes the
proposition because the term only records machinery Commonplace stipulated.

### Binding is often grammatical rather than formulaic

Several clear passes use “a system that...,” “for runtimes...,” “under...,” or
“when...” rather than “for any system that chooses....” A contract that
recognizes only the example's literal quantifier would create false failures.

## Contract-clause recommendation

State the clause flatly. The collection has long required titles and opening
arguments to be statable in general terms; binding makes that existing rule
operational rather than introducing a new obligation. Do not add a transition
provision or grandfather existing notes. The observed focal failure rate is zero
in both strata, and the late area residue was already contrary to the existing
general-form requirement. Handle it as ordinary targeted cleanup, not migration
debt caused by the clarification.

Before applying the proposed contract edit, make three wording changes so the
clause implements the test used here:

1. Name all three measured surfaces, which state the artifact's intended
   contribution: **title, description, and opening argument**.
2. Say that binding may be grammatical. Generic and conditional forms such as
   “a system that chooses X,” “for systems built with X,” and “under X” count
   when they range over or scope the choice.
3. Include the removal test: a system-specific term is not a free occurrence
   when replacing it with its general description leaves the claim's truth
   conditions unchanged. Require an existential witness to support a substantive
   feasibility, mechanism, or consequence claim; merely restating a local
   assignment with existential grammar does not turn it into theory.

The resulting clause can be written without re-reading this sample:

> **Formulation constraint — bind the choices you name.** The title,
> description, and opening argument must be statable in general terms, even
> when derived from a specific system. Where one of those surfaces names a
> choice some system made, bind it universally, existentially as a substantive
> witness, or through equivalent generic or conditional grammar. A
> system-specific term is not a free occurrence when replacing it with its
> general description leaves the claim's truth conditions unchanged.
> Existential grammar is not enough when the sentence merely restates the
> selected value. If no substantive claim remains after binding, move the
> artifact to `kb/reference/` because its intended contribution is what
> Commonplace selected or the state that selection produced. Claims offered as
> theory later in the body obey the same binding rule; explicitly scoped local
> reports and examples may support the theory without becoming the artifact's
> intended contribution.
