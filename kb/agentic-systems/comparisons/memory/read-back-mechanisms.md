---
type: types/note.md
description: "Compare whole-block loading, recency windows, model-directed reads and explicit recovery in Hermes, Nemsy, OpenKB, Hindsight and sqz, without equating delivery with reliance."
traits: [has-comparison, synthesis]
---

# How memory reaches the next decision

## Research question and scope

A memory store can contain the right information without supplying it to the process that needs it. This comparison asks: **what initiates read-back, what selects retained material, which representation reaches which consumer, and what evidence connects delivery to a decision?** The unit is a read-back route, not a database or a product's memory label. A catalog entry, a recoverable original and a model-visible body are different availability states.

This is a bounded qualitative comparison selected from the **243 current accepted analysis sets** at inputs commit `bf2da04db03fb4cb60be52d1bb04e638a79eda79`. That population contains 225 code-grounded and 18 doc-grounded sets; these are population identities, not prevalence results. The five examples here are code-grounded. Hermes and Hindsight retain contrasts in whole-block loading, selective access and internal versus external consumers. Nemsy adds question-independent recency selection and a separate human reading route. OpenKB contrasts internal model-directed reading with an instructed external host. sqz exposes the difference between retained content, estimated context residence and explicit recovery. This selection is for explanatory value, not representativeness or exhaustive coverage. The [memory landscape](agent-memory-landscape.md) supplies broader framing.

Only committed retained members and their canonical records supply findings. The successful shared matrix build supplies population membership and recorded identities; it is not new operational evidence. Its recorded SHA-256 is `19da70a6ca54b9c659dd9d1bf734e5f46885325d48f58b40685eccea083ce0bc`. Legacy reviews, archives, local run evidence and new external acquisition are excluded. No axis distributions or change-in-prevalence claims are made. This is one inputs-commit snapshot, not a comparison between historical populations.

### Selected evidence identities

Each boundary links the registered repository and source evidence. Cutoffs delimit applicability, not deployment dates. The last column records each accepted manifest's identity.

| System and source boundary | Reviewed source revision | Cutoff | Run ID | `ARTIFACT.yaml` SHA-256 |
|---|---|---|---|---|
| [Hermes Agent](../../../agentic-system-analyses/retained/nousresearch--hermes-agent/boundary.md#source-register) | `0e427d788d253630d38a3a51cd76849e73cd6925` | 2026-10-14 | `AAS-2026-10-14-hermes-agent-bfb4bdc54d37-01` | `a1c1c9c6d66287eecb408af1bea873f3a1a1f0a126eda4f970f1ebf45bd9bfcf` |
| [Hindsight](../../../agentic-system-analyses/retained/vectorize-io--hindsight/boundary.md#source-register) | `610c135b6f2d0d8b972da94146ae635943f36271` | 2026-10-14 | `AAS-2026-10-14-hindsight-34c2ca821edf-01` | `3e9e67f75bff2a28a6ffc32ceb894615058008641f960da1e24bc9d70fb38579` |
| [Nemsy](../../../agentic-system-analyses/retained/arrrr110--nemsy/boundary.md#source-register) | `2338bab0aab96a91efb90a80249f33510b630260` | 2026-11-09 | `AAS-2026-11-09-nemsy-2a6b7963bf65-01` | `c0e9844d367d94f2dae783f51c553672c7fdb69bec275744d1502858f2f45a6f` |
| [OpenKB](../../../agentic-system-analyses/retained/vectifyai--openkb/boundary.md#source-register) | `ff54396e575ee6feb0113b631a34caa082b441cc` | 2026-11-09 | `AAS-2026-11-09-openkb-bd9c4c38a842-01` | `673ab019297ae1f6c552df97d4333284c5fbe9cd0385584d6997acaffd6cdb24` |
| [sqz](../../../agentic-system-analyses/retained/ojuschugh1--sqz/boundary.md#source-register) | `495c078d8f4c94d060ecfbb4d919286670b87898` | 2026-11-09 | `AAS-2026-11-09-sqz-154fb86209ba-01` | `1a8bcd26e2520363f066a7da20713bba79b6c6dd7fad9273245c05476115fff2` |

Hermes and Hindsight have complete-artifact, partial-loop boundaries. The other three have whole-system boundaries with local inspection limits, not exhaustive implementation audits. None of the selected route evidence establishes observed consumer reliance, measured continuation benefit or a causal effect. “Wired” below means connected in inspected code; “afforded” means a supplied interface or instruction permits a route without establishing the deployed chain.

## Architectural distinctions

Read-back separates at least five questions:

1. **Initiation:** a user question, model tool call, lifecycle hook or ordinary file request starts the chain.
2. **Selection:** code or a model chooses retained items by availability, recency, query, address or another predicate.
3. **Representation:** bodies, snippets, summaries, images, references or derived answers cross the boundary.
4. **Consumer identity:** an answering model, maintenance model, external host or human receives that representation.
5. **Reliance:** delivered content changes the consumer's decision. Inclusion alone does not establish this.

A request does not determine every later selection. A user can request an answer while code supplies a question-independent memory window. Conversely, an automatic hook can request service retrieval and then supply the result to a host without the foreground model requesting those items. Here **pull** means fulfilling a consumer's request for retained material; **push** means supplying it without that request. Those operations can coexist in one chain. The terms describe individual crossings, not an entire product.

The route summaries below are grounded in the linked accounts that follow. They are not complete product classifications.

| Selected route | Initiation and selector | Delivered representation and consumer | Unestablished next step |
|---|---|---|---|
| Hermes notes/profile | Prompt load; enabled store, no query ranking | Whole prompt projection to foreground model | Reliance on a particular entry; immediate adoption after a write |
| Nemsy ordinary Wiki answer | User question; code chooses index plus recent pages | Full selected file text to answering model | Recovery of an omitted page through that model's tools |
| OpenKB internal query | User question; model chooses paths, pages or images | Tool results to internal answering model | Correct grounding; equivalence to external-host reading |
| Hindsight reflection / Claude hook | Reflection request or host event; retrieval plus route-specific controls | Selected prose to internal model / formatted context to external host | Actual model reliance or host incorporation |
| sqz native cache and recovery | Requested operation; cache probes, then optional query/hash recovery | Ref, delta, snippet or recovered content to caller/host | Body residency, automatic dereference or correct reconstruction |

## Concrete implementations

### Hermes: whole notes versus catalog-selected bodies

Hermes's enabled notes and user profile enter the system prompt as whole load-time projections. Threat replacement can change that projection; it is not necessarily byte-identical to the files. There is no question-specific ranking of those blocks. Whole-block loading removes the need to formulate a retrieval query for those stores, but does not establish relevance. Ordinary cached requests keep their previous snapshot until a refresh boundary; local admitted compaction can reload and rebuild it. A successful write therefore need not change the next request ([notes cycle](../../../agentic-system-analyses/retained/nousresearch--hermes-agent/memory.md#mem-rte-notes-cycle)).

Skills divide discovery from content delivery. Eligible names and descriptions enter an index; the foreground model can request a body or support file by name/path. Catalog visibility is not body visibility, and viewing a script does not establish execution. Automatic-load and preload alternatives also exist, with incomplete rendering coverage. The contrast is ordinary catalog advertising versus selective body loading, not a universal requirement for an explicit body request ([skill cycle](../../../agentic-system-analyses/retained/nousresearch--hermes-agent/memory.md#mem-rte-skill-cycle)). The [reconciliation](../../../agentic-system-analyses/retained/nousresearch--hermes-agent/reconciliation.md#disagreement-and-integration-dispositions) preserves the snapshot-horizon qualification: mutation neither immediately refreshes every prompt nor freezes it permanently.

### Nemsy: index visibility without body recovery

Nemsy's ordinary Wiki answer supplies a code-selected window. The loader includes the index in full, excludes index/log filenames from the other-page set, sorts recursive Markdown paths by modification time and takes up to thirty other files. It reads those bodies whole, without a local input-token budget. The question does not change that selector, and frontmatter/tags are not parsed to select pages. There is no model-accessible follow-link tool wired by this route. An old page can therefore remain named in the index while its body is outside the model's input ([answer annotation](../../../agentic-system-analyses/retained/arrrr110--nemsy/memory.md#on-rt-rte-wiki-answer), [index object](../../../agentic-system-analyses/retained/arrrr110--nemsy/memory.md#mem-obj-wiki-index)).

This is not equivalent to Hermes's catalog-plus-body route. A locator becomes useful for model recovery only when a reachable operation can follow it. Nemsy does provide a separate browser path: explicit file selection or a resolved citation returns current file text to a human-facing browser. That read does not automatically forward the file into chat. Citation resolution by stem also does not verify substantive support. Human inspectability and model availability are distinct endpoints ([browser route](../../../agentic-system-analyses/retained/arrrr110--nemsy/memory.md#mem-rte-browser-read)). The [current reconciliation](../../../agentic-system-analyses/retained/arrrr110--nemsy/reconciliation.md#current-conflict-disposition) explicitly retains this human read-back; it is not a remaining conflict or an absence of memory consumption.

Freshness is route-specific too. CLI chat selects twenty other pages at session start and keeps a string snapshot; Web chat reloads at each request. Neither a disk update nor a currently visible browser page proves that an ongoing CLI model call has the new body ([chat annotation](../../../agentic-system-analyses/retained/arrrr110--nemsy/memory.md#on-rt-rte-conversation-chat)).

### OpenKB: internal reading versus an instructed external reader

OpenKB's query agent receives a question and can request wiki files, numbered source pages and images. Tool results enter that same internal model's context before it answers. The page helper filters requested page numbers, but a plain file helper can also read an in-root JSON file whole. “Never fetch the whole document” is prompt policy, not a universal enforced volume limit; the 50-turn cap limits turns, not text volume ([query route](../../../agentic-system-analyses/retained/vectifyai--openkb/runtime.md#rt-rte-wiki-query), [read-back annotation](../../../agentic-system-analyses/retained/vectifyai--openkb/memory.md#on-rt-rte-wiki-query)).

The shipped external-agent skill describes a different route. It asks the enclosing host to discover the KB, scan its index, read pages directly and follow a small number of links, with `openkb query` as a fallback. Direct reading keeps selected source/page text in the host's own reasoning context. Fallback returns another model's answer, not all its retrieval history. This host route is **afforded by instructions**, not established as a deployed or observed host integration. Its claimed economy is not a measured result ([host-read record](../../../agentic-system-analyses/retained/vectifyai--openkb/memory.md#mem-rte-host-read)).

Other retained objects expose still different consumers. Saved explorations remain explicitly readable, but neither inspected save branch updates the index; saving does not guarantee catalog-mediated rediscovery. Persisted SDK chat history feeds the next selected-session turn, while filtered display arrays feed the browser. Image bytes in SDK history are replaced by reload hints, so an image can be retained on disk yet require a new model request to become visible again ([explorations](../../../agentic-system-analyses/retained/vectifyai--openkb/memory.md#mem-obj-explorations), [history](../../../agentic-system-analyses/retained/vectifyai--openkb/memory.md#mem-obj-session-history), [display](../../../agentic-system-analyses/retained/vectifyai--openkb/memory.md#mem-obj-session-display)). The [reconciliation](../../../agentic-system-analyses/retained/vectifyai--openkb/reconciliation.md#integration-dispositions-and-disagreements) confirms this distinction between readable storage and catalog rediscovery.

### Hindsight: an internal answer is not external host recall

Hindsight reflection takes a bank, query and controls, authorizes and scopes the request, loads applicable directives and runs an internal answering model with retrieval callbacks. Code forces an initial retrieval sequence according to enabled tools; the model can propose subsequent calls. Selected retained prose reaches later model calls before an HTTP answer returns. That answering role is distinct from the external host and from maintenance models ([reflection route](../../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-rte-reflect-request)).

Page delivery separates discovery from address-based recovery. Embedded-query search can inline a fitting top page and show other hits as 280-character snippets. The reflection model can then request page IDs. Explicit reads have a first-page floor: the first available page can exceed the budget; later non-fitting pages are skipped with IDs for retry. Thus a nominal budget does not establish a hard whole-payload ceiling, and a retry locator does not establish a retry ([page delivery](../../../agentic-system-analyses/retained/vectorize-io--hindsight/memory.md#mem-rte-page-delivery)). Recall separately budgets fact, chunk and source projections; source IDs can survive without readable justification. Provenance at rest is not necessarily provenance delivered ([recall selection](../../../agentic-system-analyses/retained/vectorize-io--hindsight/memory.md#mem-rte-recall-selection)).

The shipped Claude hooks create another chain: Stop-time transcript retention and UserPromptSubmit-time recall, score filtering and formatting into `additionalContext`. The service request is pull; the integration supplies selected context to the foreground host without that model requesting those items. Hook output is wired, but actual host loading and reliance remain unobserved. It is not the internal reflection answer path ([hook route](../../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-rte-claude-hooks)). The [reconciliation](../../../agentic-system-analyses/retained/vectorize-io--hindsight/reconciliation.md#integration-dispositions-and-independent-convergence) retains both the consumer distinction and the route-local budget exceptions.

### sqz: recoverable content is not resident content

sqz's native cache keeps admitted originals and compressed representations in SQLite. Within requested operations it probes exact identity, line containment and near-duplicates, potentially returning references or deltas instead of bodies. Exact/slice reference freshness uses access timestamps and a persisted compaction marker, with pins bypassing those checks. These are estimates of likely context residence, not queries of the host's model window. Repeated reference delivery can refresh access metadata without proving body visibility ([cache route](../../../agentic-system-analyses/retained/ojuschugh1--sqz/runtime.md#rt-rte-cache-recovery), [cache annotation](../../../agentic-system-analyses/retained/ojuschugh1--sqz/memory.md#on-rt-rte-cache-recovery)).

Predictive dependency pre-caching makes the distinction concrete. After recognized file reads, the CLI can resolve imports, read dependencies and admit their content, while returning at most a pre-cache count rather than dependency bodies. Later `[in context]` annotations consult stored path metadata, not the host window. A cached dependency is therefore not evidence that the model previously received it ([dependency route](../../../agentic-system-analyses/retained/ojuschugh1--sqz/memory.md#mem-rte-dependency-precache), [known-file metadata](../../../agentic-system-analyses/retained/ojuschugh1--sqz/memory.md#mem-obj-known-files)).

Recovery is a second operation. Recall uses FTS5/BM25 to return snippets and locators; expansion resolves a hash prefix and optional range. Original recovery requires captured originals and surviving storage, but not reference freshness. Searchability has additional indexing limits, so an expandable original need not be discoverable by recall. Neither a reference token nor a delta automatically dereferences itself through model attention ([recall route](../../../agentic-system-analyses/retained/ojuschugh1--sqz/memory.md#mem-rte-recall-search), [original object](../../../agentic-system-analyses/retained/ojuschugh1--sqz/memory.md#mem-obj-cache-original)).

These conclusions are local to the native paths. The delta baseline compares compressed data without the exact-reference freshness test. Session resume prints a bounded guide from typed session data; the installed compact-time SessionStart command does not establish a complete automatic session-capture and restoration loop. The [reconciliation](../../../agentic-system-analyses/retained/ojuschugh1--sqz/reconciliation.md#independent-convergence-and-integration-dispositions) explicitly separates those paths and withholds downstream reconstruction and host-consumption claims. Native recovery must not be generalized to browser/IDE transformations merely because they share the sqz name.

## Comparison and consequences

The decisive distinctions are not simply search versus no search, or pull versus push. **Initiation, selection and delivery can have different owners.** Nemsy answers a question using a recency window unrelated to that question. OpenKB lets an internal model choose reads, but its external-host alternative has only instructional support. Hindsight's hook initiates retrieval on behalf of another consumer. sqz automatically selects a representation inside an otherwise requested operation.

**A compact representation can move the next decision rather than eliminate it.** Hermes's catalog defers body selection. Hindsight's snippets defer page reads. OpenKB's image hints defer visual reload. sqz's references defer recovery. Nemsy's index can advertise an omitted body without a model recovery tool on that route. These mechanisms differ in whether the later consumer can follow the locator at all, not just in how much text they initially deliver.

**Budgets and freshness labels need their actual units.** A file count is not a token bound; a turn cap is not a volume cap; a first-item floor is not a hard ceiling. A refreshed timestamp is not a body-residency witness. Whole-block loading, retrieval calls and model-directed follow-up also incur different kinds of work, but these records do not establish comparative latency, token savings or task accuracy.

## Evidence limitations

Positive witnesses establish these named routes, not complete product inventories or population prevalence. Partial coverage does not establish that other selectors or consumers are absent. Static code establishes wired delivery; shipped host instructions establish an affordance. Neither establishes an exercised route, reliable model compliance or a benefit. Reported benchmark claims and evaluator definitions are not used here as observed read-back results.

The comparison also withholds ranking quality, compression fidelity, real host incorporation, provider-side context behavior and whether a particular retained claim changed an answer. Saved text, returned IDs and visible citations do not independently certify truth. No product ranking or Commonplace adoption recommendation follows from these mechanisms.

## Open questions and experiments

A useful trace would identify the retained item's version, trigger, selector, delivered representation, exact consumer input and subsequent action. It should distinguish an unavailable item, a missed selection, a reference without recovery, clipped justification and delivered-but-unused material.

Three bounded experiments would separate the remaining questions:

- **Catalog and recency selection.** Hold corpus, task and model constant while varying whole-block loading, recency windows and catalog-plus-body access. Measure relevant body delivery as well as outcomes; include old pages whose index descriptions remain visible but whose exceptions are buried in bodies.
- **Recovery after context loss.** For sqz, distinguish previously delivered bodies from pre-cached dependencies, then remove host context while preserving storage and metadata. Record reference/delta output, recall, expansion and reconstruction. Vary exact-reference freshness separately from delta selection; do not infer success from cache hits.
- **Consumer and projection boundaries.** Capture OpenKB internal tool inputs separately from a host receiving only its answer, and Hindsight internal reflection separately from hook delivery. Vary snippet/source budgets or permit follow-up body reads. Measure evidence preservation before attributing answer changes to retrieval or compression.

These are proposed tests, not results. A trace of inclusion establishes delivery; a behavior change tied to that content supports reliance. Performance differences support benefit only under the tested conditions, and component-level causal claims require independent variation of that component. The supported conclusion remains architectural: these systems wire materially different paths from retained state to later inputs. Which path improves the next decision remains an empirical question.

[Agent Memory topic](../../topics/memory.md) · [Memory comparisons and data](./README.md) ·
[Correction propagation](./correction-propagation.md) · [Methods & Data](../../methods.md)
