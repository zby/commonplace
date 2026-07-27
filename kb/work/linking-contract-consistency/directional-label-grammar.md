# Directional label grammar

## Candidate invariant

Every directional identifier must complete the assertion:

> **source `<label>` target**

The source is the artifact containing the Markdown link; the target is the artifact named by its URL. A reader should be able to recover the asserted direction from the identifier without consulting a collection table to learn which endpoint is the grammatical subject.

Examples of the intended shape:

- `source extends target`;
- `source exemplifies target`;
- `source is-part-of target` (currently spelled `part-of`);
- `source implements target`;
- `source is-defined-in target` (currently spelled `defined-in`);
- `source is-derived-from target` (currently spelled `derived-from`).

Registered identifiers do not need to be elegant prose when expanded literally, but their grammatical voice must be stable and obvious. The current convention already omits helper verbs such as “is” in `part-of`, `defined-in`, and `derived-from`; that abbreviation is compatible with the invariant because it does not swap the endpoints.

## Why this is needed

The current vocabulary mixes two conventions:

1. **Source-as-subject identifiers:** `extends`, `exemplifies`, `part-of`, `implements`, `derived-from`.
2. **Target-role identifiers:** `grounds`, `mechanism`, `rationale`, `evidence`, and `procedure` currently mean that the target grounds, explains, evidences, or provides a procedure for the source.

The second group cannot be interpreted from `source <label> target`. For example, the current semantics of `evidence` are “target is evidence for source,” while the literal source-as-subject reading suggests “source evidences target.” This is why adding `evidence-for` did not make direction clearer: the vocabulary had never fixed which endpoint a label grammatically describes.

## Consequences for label design

### Directional labels

Every directional label needs a catalogue assertion template that uses the source as subject. If the current identifier reads in the opposite voice, either rename it or explicitly reject this invariant; do not rely on a reader-need gloss to reverse the grammar silently.

### Inverse pairs

When both directions earn authored labels, each identifier must independently satisfy the invariant and the pair should make the inversion recognizable:

- `source part-of target` / `source contains target`;
- `source implements target` / `source implemented-by target`;
- `source supersedes target` / `source superseded-by target`.

An inverse identifier does not require reciprocal authoring. Each edge still needs an independent reader need.

### Self-dual labels

Self-dual relations such as `contradicts` and `contrasts` retain one identifier because swapping endpoints does not change the semantic relation. Either endpoint may author the edge; neither is obliged to mirror it.

### Navigation and control-flow labels

Weak navigation (`see-also`) and procedural control-flow labels may not describe ontology-like relations, but they still need an explicit source→target assertion template or a declared grammar exception. “It is obvious from the collection context” is not sufficient for a shared identifier.

## Audit required

The evidence review exposed the rule, but the repair must cover the whole vocabulary rather than special-case `evidence`. Audit every asymmetric identifier in the shared catalogue and live collection contracts.

Initial high-confidence cases:

| current identifier | current meaning | source-as-subject result |
|---|---|---|
| `extends` | source builds on target | passes |
| `exemplifies` | source is an instance of target | passes |
| `part-of` / `contains` | source is part of / contains target | passes |
| `implements` / `implemented-by` | source implements / is implemented by target | passes |
| `supersedes` / `superseded-by` | source supersedes / is superseded by target | passes |
| `defined-in` | source is defined in target | passes with omitted “is” |
| `derived-from`; `abstracted-from`; `adapted-from`; `operationalized-from` | source has the named relation from target | passes grammatically; lineage carrier questions remain separate |
| `grounds` | target grounds source | fails current voice |
| `enables` | target enables source | fails current voice |
| `mechanism` | target is the mechanism for source | fails current voice |
| `rationale` | target is the rationale for source | fails current voice |
| `evidence` | target is evidence for source | fails current voice |
| `procedure` | target is the procedure for acting on source | fails current voice |
| `precondition` | target is a precondition for source | fails current voice |

The remaining procedural and weak labels need a worked-use audit before classification: `composition`, `invokes`, `applies-when`, `operates-on`, `compares-with`, and `see-also`.

For every failing or uncertain label, the audit should record:

1. the current catalogue meaning;
2. every authorized source→destination pairing;
3. representative corpus uses;
4. the source-as-subject assertion authors appear to mean;
5. candidate identifier or explicit exception;
6. overlap with neighboring labels;
7. migration size and ambiguous cases requiring judgment.

## Leading evidence-pair candidate

The [evidence direction review](./evidence-direction-review.md) establishes that both claim→observation and observation→claim reader journeys are real. It does not yet settle their identifiers.

The leading candidate is:

| identifier | assertion template |
|---|---|
| `evidenced-by` | claim source `evidenced-by` observation target |
| `is-evidence-for` | observation source `is-evidence-for` claim target |

Both complete the source-as-subject assertion without reversing endpoints. The explicit `is-` makes `is-evidence-for` a grammatical predicate rather than an ambiguous noun-like category. It asserts that the source bears evidentially on the target; it does not assert that the target already cites, incorporates, or accepts the source.

The pair remains provisional until the full audit tests its boundary against `grounds`, contradiction/counterevidence, qualification and boundary evidence, and the two existing off-vocabulary `supports` uses.

## Adoption status

Accepted as the workshop's candidate naming rule for subsequent analysis; not yet part of the shipped link vocabulary. Adoption requires an ADR/catalogue change and a migration plan for every affected identifier, not only the evidence pair.
