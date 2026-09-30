# Why the rerun still needed source-check repairs

The quote-matching change strengthened rejection, but did not finish aligning
the authoring workflow with the new rule. Fresh memory specialists were not
routed to the uniqueness requirement. Citation endpoints and some quote bytes
were still reconstructed during drafting. A separate structural validator also
rejected attribution syntax that the shared parser and authoring instructions
accepted.

These are different causes. Increasing matching strictness cannot itself make
the author supply the right occurrence, preserve every source character, or
produce an attribution accepted by a second grammar.

## Commission and evidence boundary

The operator requested this root-cause analysis after the
[three-pilot rerun](./quote-rerun-20260927.md). It explains the five failed
`verify-sources` invocations under Commonplace commit
`4a97ad715a4dbdcc6de09dea22417d1f88fbbbdf`. Evidence is the recorded drafting
commands, delivered tool outputs, diagnostics and corrections, plus the pinned
source blobs and the implementation/instructions at that commit. No new
system analysis, producer change or Git commit was performed.

The report distinguishes a directly observed construction error, an established
contract mismatch, and a plausible behavioral contribution. It does not infer
the model's private reasoning or claim a controlled intervention on its error
rate. The existing audit retains the complete run IDs, source pins, final
hashes and recovery history.

## What failed

| Failed invocation | Stage reached | Diagnostics | Mechanisms below |
|---|---|---|---|
| Dynamic Cheatsheet specialist | Source matching | One quote occurring 32 times | RC-1 |
| Dynamic Cheatsheet coordinator | Artifact validation, before source matching | Six bare-URL attributions; one relative image link | RC-3, RC-5 |
| Mem0 specialist | Source matching and ordinary source-anchor checks | Seven ambiguous quotes; three out-of-bounds ranges | RC-1, RC-2 |
| Mem0 coordinator | Ordinary source-anchor checks | Two out-of-bounds ranges | RC-2 |
| Napkin specialist | Source matching and ordinary source-anchor checks | One changed quote; three out-of-bounds range diagnostics | RC-2, RC-4 |

There are 23 citation/source diagnostics and one image-link diagnostic across
five failed calls. They are not 23 independent mistakes: one formatting helper
produced all six bare URLs, and Napkin reused the same bad end line across
three anchors. Mem0's separate comparison-schema failure is outside this
analysis. Availability probes and successful no-match searches are also excluded.

The distinction between stages matters.
[`verify_sources`](../../../src/commonplace/lib/agentic_publication.py) first
runs ordinary artifact validation, then quote matching and source-anchor checks.
The Dynamic Cheatsheet coordinator was stopped before the matcher ran. Calling
all five failures quote-matcher failures would misdiagnose that case.

## RC-1 — The uniqueness rule did not reach the specialist's prescribed reading path

**Established contract-delivery gap; likely contribution to author behavior.**

Commit `6374109c` added the unique-occurrence requirement to the main
[analysis skill](../../instructions/analyse-agentic-system/SKILL.md) and the
quotation section of the [result type](../../types/agentic-system-analysis-result.md).
It did not update the standalone
[memory instruction](../../instructions/analyse-agentic-system/jobs/memory.md) or
[memory-report type](../../types/agent-memory-analysis-report.md).
Those still explain that publication finds the text in the source, without
stating that exactly one occurrence is required.

This omission matters because memory analysis deliberately runs in a fresh
context. Its instruction explicitly directs the specialist to read only the
main result type's Memory comparison fields and Status fields, alongside its
own report type. The updated quotation rule is in a later section. The traces
show that the specialists followed this restricted reading path:

- Dynamic Cheatsheet read result-type lines 43–174 and 193–204.
- Mem0 read lines 43–215.
- Napkin selected the two named sections.

None of those reads includes the quotation rule at lines 247–266. The frozen
inputs do not add a uniqueness instruction. All eight ambiguous quotes came
from these specialists; neither coordinator introduced a new ambiguous quote
that failed its result check. Some messages are encrypted in the traces, so
this finding concerns the prescribed and recorded file-loading path, not proof
that no off-band message could have mentioned uniqueness.

The source repetitions were real and explain why occurrence alone was
insufficient. Dynamic Cheatsheet's short sentence appeared 32 times across
nine JSONL rows: 24 times under `steps` and eight under `final_cheatsheet`.
Mem0 duplicated five selected passages between synchronous and asynchronous
implementations. Its SQLite initialization statement appeared in both classes'
constructors and reset methods; another quotation appeared in both schema
migration and creation.

The old presence-oriented instructions could be satisfied by these exact
passages while the new uniqueness check rejected them. The contribution of
the missing instruction is plausible, but these runs cannot establish how
many failures updated guidance alone would prevent.

**Required outcome:** the specialist's actual required reading path must carry
the same occurrence, normalization and range rules that its checker enforces.
A coordinator knowing a rule does not supply it to a fresh worker. Prefer one
explicitly loaded contract over independently maintained paraphrases.

## RC-2 — Requested read bounds became unverified citation metadata

**Directly observed for three bounds; generated inaccurate endpoints for the rest.**

All eight range diagnostics were for ordinary source anchors, not quote blocks
whose supplied range failed containment. Making quote ranges optional therefore
did not remove this error surface.

The three Mem0 specialist endpoints reproduce its read-window endpoints:

| Source | Requested read ended at | Actual final line | Draft citation ended at |
|---|---:|---:|---:|
| `mem0/configs/prompts.py` | 1075 | 1062 | 1075 |
| `mem0/reranker/llm_reranker.py` | 190 | 173 | 190 |
| `mem0/utils/scoring.py` | 150 | 139 | 150 |

Those reads used `sed -n` without source line labels. Asking `sed` to print
through a line beyond EOF succeeds and returns the available lines. Its exit
status does not establish that the requested final line exists. The drafting
code then wrote the same upper numbers into the report without deriving them
from the actual blob length. This is an observable conversion of a selection
request into an asserted source location.

Mem0's coordinator wrote 1069 and 774 for files ending at 1062 and 772. Its
preceding reads requested other upper bounds, including 1070 and 775; the trace
does not establish an exact copy rule for these two numbers. Napkin wrote 215
for a 198-line file in three anchors. Its initial read delivered the complete
unnumbered `crud.ts`: the full blob is present inside the tool return even
though that multi-file return carries a truncation warning. Missing source
bytes therefore do not explain that particular error. The visible drafting
commands emitted these endpoints as literal prose, without a source-derived
endpoint calculation.

A contract conflict keeps this unnecessary metadata attractive: the main skill
makes Git ranges optional navigation, while the result type's Status fields
still asks for a full path and one or more ranges. The specialists did load
that latter section. This is an established inconsistency, not proof that it
caused each endpoint choice.

**Required outcome:** resolve whether ordinary ranges are optional. Omit
unneeded ranges; when a range identifies evidence, derive and check its actual
span against the pinned blob before emitting it. Do not treat a requested read
window as the returned interval. Automatically clamping a bad endpoint would
still require checking that the remaining passage supports the claim.

## RC-3 — Structural validation retained a competing attribution grammar

**Confirmed implementation/contract mismatch, not six missing sources.**

Dynamic Cheatsheet's coordinator used a Python helper to copy source lines
directly from pinned Git blobs. The helper ended each block with a bare
full-commit GitHub URL. This agrees with the main skill and result type's
stated URL alternative, and
[`_attributed_citation`](../../../src/commonplace/lib/quote_matching.py) parses
the URL into a source, revision and range.

However,
[`validate_quote_citations`](../../../src/commonplace/lib/validation.py)
then independently applies `_SOURCE_REF_RE`, which recognizes only Markdown
links and code spans. It reports that the bare URL names no source even
though the shared parser has recognized one. The same helper produced all
six rejected attributions. Wrapping them as Markdown links cleared these
diagnostics without changing their repository, revision, range or quote text.

This is residual duplicate syntax recognition after introducing a shared
parser. Telling the author to use Markdown links is a workaround. It does not
resolve the disagreement between the documented input, parser and validator.

**Required outcome:** define the accepted attribution form once and make
structural validation consistent with the parsed citation. If rendered links
are required for a separate reason, say so explicitly and report a formatting
error rather than claiming that a recognized source is absent.

## RC-4 — A code comment was rewritten as prose inside a verbatim quote

**Confirmed quote-body transformation.**

Napkin's specialist copied two lines from `bench/overview-exposure.ts` but
omitted their leading comment `*` characters. The words remained the same.
The Git-source matcher intentionally normalizes whitespace only, so the
modified passage did not occur in the blob. Restoring the two `*` characters
made it pass.

This was not typography noise or an incorrect source revision. The quote went
through a prose-style cleanup despite being represented as literal source
text. The trace does not establish why the model removed the markers. Its
instruction does require verbatim quotation, so this case cannot be explained
solely by the missing uniqueness rule.

**Required outcome:** preserve the chosen source bytes when forming code
quotations, including comment markers. Keep the author's interpretation outside
the quote. Do not weaken code normalization to conceal transcription errors.

## RC-5 — A source-relative image link was interpreted relative to the report

**Confirmed interaction between exact copying and host-document validation.**

Dynamic Cheatsheet's helper copied README lines 25–30, including an image
whose target was `figures/OverallPerformance.png`. The copied text was faithful
to the source. The report's Markdown link scanner includes links inside
blockquotes, and its resolver interprets relative targets from the report's
directory. It therefore looked for a local report-side image instead of the
image in the pinned external repository.

This was an artifact link-health failure, not a source-text mismatch. Exact
copying by itself cannot solve it: rewriting the target inside the quote would
change the quoted source. The coordinator removed the unnecessary image line
from the excerpt; the shortened passage still matched and supported the claim.

**Required outcome:** select only the necessary source passage. For a material
relative link that must remain quoted, the validation contract must distinguish
source content from links authored for the report. This does not justify
ignoring ordinary broken report links or silently rewriting verbatim URLs.

## What the evidence does not support

The current matching engine rejected the observed ambiguous or changed text as
specified. No source change, wrong source pin, unavailable blob or publication
race explains these five failures. Each failed source-check invocation was
followed by a successful check after correction; the final artifacts remain
verified. The procedure explicitly includes this correction loop.

Truncation and context volume can contribute to mistakes, but this trial did
not isolate their effects. Napkin's complete `crud.ts` delivery rules out one
simple truncation explanation. The restricted specialist reading path is
independent of truncation: it deliberately skips the new quotation section.
There is no basis here for attributing all failures to context size, model
capability, or a need for another reviewer.

Five rejected calls versus two previously also does not show that authoring
became worse. The checker now rejects ambiguities the earlier one accepted.
Some new failures expose old contract inconsistencies. The supported outcome
is stronger detection before publication, with remaining preventable repair
work.

## Repair priorities and a discriminating follow-up

1. **Align the actual contracts first.** Route the complete quote contract to
   the fresh specialist; reconcile optional ordinary ranges; remove the
   disagreement over accepted URL attribution. These are demonstrated gaps.
2. **Preserve measured evidence during construction.** Once the author chooses
   a passage, keep its exact text and actual source span together through
   rendering and integration. The citation helper already used in Dynamic
   Cheatsheet shows that exact copying is practical, but its accepted syntax
   also needs to agree with validation. The required outcome does not imply
   a new persistent evidence store or a larger workflow.
3. **Test the layer interactions before another full pilot.** Exercise a valid
   pinned URL through both parsing and artifact validation, source-relative
   links inside retained quotations, a requested window beyond EOF, duplicate
   implementations, and literal code comments. Keep negative checks for a
   genuinely missing source, altered quote and ambiguous occurrence.
4. **Then measure fresh authoring separately from final acceptance.** Hold the
   source pins and model setting fixed; count first-check failures by these
   categories and retain denominators. A clean final artifact measures the
   correction loop's success. Fewer first-check failures would support reduced
   authoring friction. Neither alone establishes semantic correctness.

These are proposed outcomes for follow-up work, not changes implemented or
adopted by this analysis.

## Trace map

Paths are under `/home/zby/.codex/sessions/2026/09/27/`. Numbers below are JSONL
line numbers, not source-code lines. The rerun's
[trace index](../../reports/cache/agentic-memory-refresh/quote-rerun-20260927/trace-index.json)
retains file hashes and model identities.

| Trace | Filename | Relevant records |
|---|---|---|
| Dynamic Cheatsheet coordinator | `rollout-2026-09-27T15-36-59-01a0e315-4fce-7b71-8c14-09e9af772ceb.jsonl` | 215 copying/URL helper; 324 structural rejection; 331 correction; 334 pass |
| Dynamic Cheatsheet specialist | `rollout-2026-09-27T15-39-02-01a0e317-309d-70b3-9169-2f6f4a73fe66.jsonl` | 22/27 contract reads; 92 ambiguity rejection; 104 correction; 111 pass |
| Mem0 coordinator | `rollout-2026-09-27T15-54-34-01a0e325-68c7-72a2-b2ac-1b6efb2ba4cc.jsonl` | 115/162 source reads; 190 draft anchors; 353 rejection; 358 reread; 365 correction; 367 pass |
| Mem0 specialist | `rollout-2026-09-27T15-56-29-01a0e327-2a68-7c60-9d0e-c56967531d54.jsonl` | 22/30 contract reads; 75/84/94 read windows; 120 draft; 145 rejection; 160 correction; 161 pass |
| Napkin specialist | `rollout-2026-09-27T16-15-49-01a0e338-ddd6-7da2-ab3b-17f80cc42eef.jsonl` | 22 contract reads; 33/34 complete CRUD source delivery; 121 comment read; 135 draft; 151 rejection; 156 reread; 163 correction; 165 pass |
