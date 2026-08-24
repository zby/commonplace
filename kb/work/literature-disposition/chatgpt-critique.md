# External critique: the navigation cluster restates established literature

Pasted verbatim from a ChatGPT conversation, 2026-08-24. Unedited external
input, not a Commonplace finding. Its central diagnosis — that several notes in
the navigation/pointer cluster are information-foraging and information-scent
theory expressed in local vocabulary — is a **hypothesis these workshops must
test against the actual sources**, not a settled premise. Its per-note
disposition table, its four-disposition menu, its proposed source corpus, and
its eight-step migration order are all candidate proposals in the same status.

---

Yes—but I would **not** turn every established-result note into a one-paragraph stub. That would preserve duplication in a cheaper form while adding another navigation hop.

The better rule is:

> **Source ingests replace the established argument. An internal note survives only when it provides graph structure, a transfer argument, a Commonplace-specific consequence, or an operative contract.**

## Four dispositions

### 1. Retire the note and route directly to sources

Do this when the note:

* merely paraphrases an established result;
* has little downstream use as a precise premise;
* adds no Commonplace vocabulary or boundary;
* and does not define current system behavior.

The relevant tag README or literature landing page should link directly to the authoritative ingests. There is no need for a note whose only content is "this is information scent; see Pirolli and Card."

This is probably the right treatment for much of:

* `agents-navigate-by-deciding-what-to-read-next`;
* `a-knowledge-base-should-support-fluid-resolution-switching`;
* the generic parts of `index-curation-adds-orientation-that-generation-cannot-produce`;
* substantial parts of `human-llm-differences-are-load-bearing-for-knowledge-system-design`.

The first of these currently presents follow-or-skip as the fundamental navigation unit, but that is essentially information-foraging and information-scent theory expressed in Commonplace vocabulary.

### 2. Keep a thin **claim adapter**

Sometimes the established claim is a useful atomic node in the Commonplace graph. Several downstream notes may need to link to one normalized proposition rather than directly to a long paper or to five separate source ingests.

Then retain a very small note containing only:

1. the exact normalized claim;
2. attribution and scope;
3. links to authoritative ingests;
4. one sentence explaining how Commonplace uses the claim;
5. a link to the genuinely new extension.

For example:

```markdown
# Information scent supports cost-sensitive pointer selection

This is an established result from information-foraging theory, not a
Commonplace contribution. A forager uses cues associated with a path or
information source to estimate its likely value before paying the cost of
following it.

See:
- Pirolli and Card ...
- information-scent empirical work ...

In Commonplace, titles, descriptions, index phrases, and contextual links are
treated as such cues. The LLM-specific question is how their value changes
when the cues themselves consume bounded inference context; see [...]
```

That note is not re-deriving the literature. It is a **stable internal interface to it**.

A claim adapter earns its existence when at least one of these is true:

* multiple downstream notes use the proposition;
* several sources jointly establish it;
* Commonplace needs a narrower formulation than any one source supplies;
* the human-to-LLM transfer boundary must be stated precisely;
* local terminology differs from the literature's terminology.

Otherwise, route straight from the README to the ingests.

### 3. Rewrite the note around the **delta**

This should be the most common treatment for notes that are partly rediscovery and partly interesting.

The established half becomes two or three sentences with citations. The body then begins where Commonplace actually adds something.

A good rewrite pattern is:

```markdown
# <Commonplace-specific claim>

## Established baseline

<Very short statement with authoritative source routes.>

## What changes for LLM agents

<The actual delta.>

## Commonplace consequence

<Effect on descriptions, READMEs, search, links, validation, etc.>

## Status

<Established application / supported conjecture / open question.>
```

The source ingests replace the exposition of the baseline, **not the transfer argument**. This distinction matters. A study of human information foraging does not by itself establish that LLM agents should use the same architecture. The surviving note must say which mechanism transfers, what changes in the consumer model, and which conclusion follows.

### 4. Keep operative documentation unchanged in role

ADRs, type specifications, and current-state reference documentation should not be shrunk merely because their rationale uses established theory.

For example:

* `kb/reference/navigation.md`;
* the `tag-readme` type specification;
* ADR 025;
* ADR 026.

These define what Commonplace currently does: curated heads, scoped search, description limits, completeness marks, coverage marks, and fallback behavior. Their job is not theoretical novelty.

They should link to the theoretical and source material, but they must remain self-sufficient enough to operate the system.

---

## First-pass disposition of the current cluster

| Current note                                                         | Proposed treatment                                    | What should remain                                                                                           |
| -------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `agents-navigate-by-deciding-what-to-read-next`                      | Retire or reduce to a thin claim adapter              | Attribution to information scent; one sentence mapping pointers to Commonplace                               |
| `link-following-and-search-impose-different-metadata-requirements`   | Rewrite around the application                        | The specific mapping from local links, indexes, search results, and descriptions to different metadata needs |
| `a-knowledge-base-should-support-fluid-resolution-switching`         | Mostly retire into the literature route               | Move practical "resolution dead-end" checks into navigation/audit documentation                              |
| `index-curation-adds-orientation-that-generation-cannot-produce`     | Rewrite and retitle around the local delta            | Curated tag heads retain role and relationship judgments that membership generation does not contain         |
| `human-llm-differences-are-load-bearing-for-knowledge-system-design` | Turn into a small routing hub                         | Route to specific differences: access mode, statelessness, instruction/content medium, activation            |
| `pointer-design-tradeoffs-in-progressive-disclosure`                 | Keep as a synthesis note                              | Fixed, query-time, and link-site pointer production; reliability as a separate axis                          |
| `design-for-the-first-time-human-except-on-access-cost`              | Keep as a delta note                                  | Access mode rather than consumer identity; separate materializations over one source of truth                |
| `charting-the-knowledge-access-problem-beyond-rag`                   | Keep as workshop/literature map, not settled theory   | Research decomposition and open questions                                                                    |
| `addressability-grain-not-compression-ratio...`                      | Keep and test                                         | This is a sharper local cost criterion, not merely generic progressive disclosure                            |
| `stale-indexes-reduce-discovery...`                                  | Keep, but position against search/stopping literature | The explicit control-flow claim about false completeness suppressing widening                                |
| `knowledge-storage-does-not-imply-contextual-activation`             | Keep                                                  | The storage -> context -> behavioral-effect decomposition and LLM evidence                                   |
| `an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract`    | Keep                                                  | It already has the right "established artifact plus Commonplace delta" structure                             |

The enforced-tag-README note is a particularly good model. It openly says that the curated hub is inherited from the Map-of-Content tradition and identifies the machine-checked completeness or coverage contract as the added part.

## A likely rewrite of the index-curation claim

The present title:

> Index curation adds orientation that generation cannot produce

is too broad. It sounds like a general novelty claim and is also slightly too absolute: sophisticated generation can produce useful orientation, though not necessarily the same reviewed judgment.

A stronger local title would be something like:

> **A tag README should retain relevance judgments that tag membership cannot mechanically recover**

Then the note can say:

* generated membership supplies exhaustive enumeration;
* descriptions supply artifact-local characterization;
* the curated head supplies reviewed judgments about role within this tag: foundational, competing, prerequisite, warning, recommended route;
* query-time generation may propose such judgments, but unless retained and reviewed they are transient navigation, not durable source-of-truth structure.

That is much harder to dismiss as rediscovered IA.

## The source corpus should be deliberately small

I would ingest a canonical baseline rather than collecting every related paper.

### Human information seeking and navigation

* Bates on berrypicking;
* Pirolli and Card on information foraging and scent;
* Marchionini on exploratory search;
* Teevan and colleagues on orienteering.

### Classification and multi-route organization

* Ranganathan or a careful primary account of the faceted tradition;
* Broughton on faceted classification as general knowledge organization;
* Hearst/Yee or equivalent primary faceted-navigation work.

### Generated and adaptive navigation

* Scatter/Gather;
* a foundational adaptive-hypermedia source.

### LLM-specific deltas

Keep these separate from the baseline:

* long-context position and interference research;
* repository-navigation and coding-agent interface experiments;
* hierarchical and agentic retrieval;
* evidence separating discovery from actual use.

Hedden can remain useful practical support, but should not be treated as the authoritative foundation for the taxonomy/navigation distinction.

Each ingest should extract more than a general summary:

* the exact claims the source establishes;
* what population or system it studies;
* the modeled costs;
* the navigation operations considered;
* the scope conditions;
* what transfers directly to LLM agents;
* what does not transfer without an additional argument;
* which existing Commonplace notes it subsumes.

That final field makes the cleanup mechanical rather than impressionistic.

## Preserve the atomic-claim graph without preserving redundant exposition

The clean architecture is:

source ingest -> optional thin established-claim adapter -> Commonplace delta claim -> operative design consequence

For example:

```text
Pirolli/Card ingest
    | supports
Information scent supports cost-sensitive pointer selection
    | baseline-for
Navigation cues have a context shadow price for LLM agents
    | motivates
Descriptions and curated heads must justify their context cost
    | implemented-by
navigation reference + tag-readme type + ADRs
```

That is better than either extreme:

* retaining a long Commonplace note that re-explains information scent;
* or linking an LLM-specific ADR directly to a human information-foraging paper and silently skipping the transfer argument.

## Tag README structure after the cleanup

The relevant README could expose epistemic routes rather than mixing everything together:

### Established foundations

Direct routes to source ingests or very thin claim adapters:

* information foraging and scent;
* berrypicking and exploratory search;
* facets and overlapping navigation views;
* adaptive and generated navigation.

### Commonplace applications

* descriptions as pre-read routing cues;
* local links versus global search;
* curated heads plus generated membership;
* progressive resolution layers.

### LLM-specific extensions

* navigation context competes with task evidence;
* effective context has a soft boundary;
* selectable-unit cost matters;
* discovery does not guarantee activation;
* route generation can be moved into fresh contexts but requires a faithful handoff.

### Open design questions

* persistent versus generated versus dynamic routing;
* context shadow price;
* route amortization;
* task-specific cohort construction;
* activation-aware evaluation.

That makes novelty status visible at the navigation layer. A reader immediately sees which material is inherited, applied, extended, or unresolved.

## Migration order

I would not start by shortening prose. The safe order is:

1. **Build a subsumption matrix**: current note, paragraphs or claims, authoritative source, local delta, downstream dependents, proposed disposition.
2. **Ingest the canonical sources**, extracting claim-level support and scope.
3. **Identify graph-value claims** that deserve thin internal adapters.
4. **Rewrite delta notes**, deleting the established exposition and making their titles state the delta.
5. **Rewire inbound links**: established-premise links go to the source or adapter; LLM-specific links go to the delta note.
6. **Retire redundant notes**, rather than leaving unnecessary stubs.
7. **Rewrite tag READMEs** to separate foundations, applications, deltas, and open questions.
8. **Add a review check**: a new theoretical note that mostly restates literature should be routed to source ingestion unless it identifies a clear local delta or graph role.

The central rule is:

> **A source-backed note should not repeat the source merely to make the idea local. It should exist only to normalize an atomic premise, justify transfer, state the local delta, or carry an operative consequence.**

That would significantly shrink this cluster while making the genuinely interesting LLM-specific theory much easier to see.
