Closure: not reached

# Closure check

Article: `kb/articles/automated-software-houses-with-fixed-llms.md`

Source commit: `50121b7178058782f7b264127bbd23d94f7eeff5`

Checked: 2026-09-04

## Free variables and decisions

| row | free variable | decision needed |
|---|---|---|
| F1 | Coherent software change and coherent later work have no decision rule. | Write the missing definition note, including the scope and observation by which coherence is decided. |
| F2 | Model availability at the 2026-09-02 cutoff is undefined. | Write the missing definition note fixing what release, access, or publication event makes a model available. |
| F3 | Learned component is undefined at the pinning boundary. | Write the missing definition note distinguishing learned components from derived or hand-authored machinery. |
| F4 | Relevant novelty and relevant demands have no inclusion test. | Write the missing definition note tying relevance to the declared product scope and request process. |
| F5 | Adequate state, theory, capacity, machinery, and successor have no shared decision rule. | Write the missing definition note or separate definitions that fix adequacy for each witness obligation. |
| F6 | Frontier model is undefined. | Write the missing definition note fixing the threshold and date dependence, or narrow the claim to a named access regime. |
| F7 | The boundary and snapshot of the reviewed system set are absent. | Write the missing definition note or retained review-set record that makes reviewed system decidable. |
| F8 | The claim that current harnesses with memory files and self-written rules are moving toward the conjecture lacks support. | Supply primary sources and locators for representative harnesses, or narrow the claim to the sourced cases. |
| F9 | The claim that architecture decision records already carry the needed rationale lacks an example or source. | Supply primary ADR examples whose premises perform the stated role, or narrow the claim. |
| F10 | The claim that an LLM can interpret design rationale without an explicit rule lacks direct evidence. | Supply a primary evaluation or reproducible test for an eligible fixed LLM, or narrow the claim. |
| F11 | The stated linguistic, programming, and reasoning capacity of fixed current LLMs lacks support. | Supply primary evaluations that establish the capacities the argument needs for an eligible model. |
| F12 | The claim that every frontier-model project is already in the fixed-model regime is unbounded. | Narrow the claim to projects whose model provider and access mode prevent weight updates. |
| F13 | The claim that such projects cannot retrain their model and therefore must retain all product learning elsewhere is unbounded. | Narrow the claim to the declared hosted-model case and separate inability to retrain from the conclusion about retained learning. |
| F14 | The claim that current LLMs can produce both notes and code lacks support. | Supply primary evaluations or reproducible examples for an eligible model. |
| F15 | The claim that no reviewed system is an empirical witness lacks a frozen review-set argument. | Supply a snapshot-bound comparison grounded in primary sources, or narrow the claim to a stated set. |
| F16 | The ranking of Fluent and the OpenAI account as the closest factories, and the claim that people retain the named roles, lacks a packaged comparison. | Supply a primary-source comparison on the witness obligations, or narrow the ranking claim. |
| F17 | The grouped claim about frozen models and retained artifacts across five named systems lacks complete packaged support. | Supply a primary-source locator for each system and state each model-pinning condition separately. |
| F18 | The claim that none of the named systems combines all four properties lacks the comparison argument. | Supply the primary-source comparison against each witness obligation, or narrow the claim. |
| F19 | The claim that the named harnesses instantiate the practice formalized by the article lacks traced examples. | Supply primary-source examples for memory files, self-written tests and tools, and retained failure rules. |
| F20 | The claim that the named accounts do not identify whose learning produced an improvement lacks an absence audit. | Supply a snapshot-bound primary-source audit that records where attribution was sought and absent. |
| F21 | The allocation of credit assignment to people, and the claim that accounts do not separate human and harness contributions, lacks packaged evidence. | Supply primary traces that identify the human acts and an explicit comparison with the harness acts. |
| F22 | The claim that Commonplace is the only reviewed construction aimed directly at holding and acquisition lacks both a review-set boundary and packaged Commonplace evidence. | Supply the bounded comparison and the primary Commonplace artifacts that establish this design target. |
| F23 | The claim that Commonplace has no witness run and is scored only as a design target lacks a retained status source. | Supply the primary status record and the review snapshot that assigns that score. |

## Test 1: Inventory

Result: failed closure. Every generated and reader-added row has a binding. The 23 rows listed above are bound as `free`; no binding cell is empty.

## Test 2: Links-disabled reading

The first fresh reader received only the link-disabled body, Appendices A–C, and References. It found package-local ambiguity in “mediation trace” and “clade metaproductivity”; both phrases were replaced with literal definitions. The existing program-theory argument was also revised to derive delayed feedback from the body's multi-tenant example. Dependencies without an inventory row were added as F1–F22.

The required single rerun used a second fresh reader with the same restricted packet. It still returned these substantive free variables: F9–F16, F18, F20, F22, and F23. It also returned `frontier model` (F6).

The rerun additionally returned these onward descriptions, which remain unchanged under the inventory's ordered classification rules because they direct the reader to optional further material rather than support the paper's substantive argument:

- row 15: the third article sets out the program from Commonplace to a witness;
- row 16: the companion map compares twenty constructions and records its evidence;
- row 17: the companion article states the rationale-reconstruction question as a hypothesis with a test;
- row 18: an open-domain theory builder may become a software house when new domains require production-machinery changes; and
- row 19: the companion article takes up the later training regime.

No further reading rerun is permitted by the procedure. All remaining substantive findings are represented by `free` rows above.

## Test 3: Placeholders and package-local links

Result: passed. No package file contains a forbidden placeholder marker, an opening template delimiter, or an empty section. No appendix or reference file links into the workshop tree.

## Test 4: Provenance

Result: passed. Every Appendix A and Appendix B entry ends with a provenance line naming source commit `50121b7178058782f7b264127bbd23d94f7eeff5`.

## Test 5: Commonplace validation

Result: the prescribed directory invocation did not satisfy the test because the validator accepts a directory only when it is a KB collection. Its complete output was:

```text
Directory is not a KB collection: /home/zby/llm/commonplace/kb/work/staging/automated-software-houses-with-fixed-llms
```

As the validator's narrow-target fallback, each of the eight Markdown files was then validated separately. Each invocation reported `VALIDATION SUCCESS`, with zero failures and zero warnings.
