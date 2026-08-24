---
description: Use when deciding whether to create, keep, generate, relocate, or remove system documentation intended for an LLM reader.
type: kb/types/instruction.md
---

> **Status: deliberately not promoted to `kb/instructions/` (2026-08-23).**
>
> The recurring, write-time half of this procedure — search for an existing
> home before writing, and ask whether the passage closes the reader's question
> or leaves the source to be read anyway — is folded into
> [`kb/reference/COLLECTION.md`](../../reference/COLLECTION.md)'s economy tests,
> where it fires while someone is actually writing. A third clause sends
> change-loop warnings to the code site rather than to a reference document.
>
> What stays here is the audit half: the disposition table, the cache-value
> test, and the maintenance-form branch. Those fire when working through an
> existing corpus, which is one-off migration work, and nothing routes an agent
> to a standing instruction for a task nobody starts by name. Shipping it would
> add an unrouted artifact while this workshop is open about unrouted artifacts.
>
> Promotion condition: a second audit needs it. This procedure changed
> materially after its first worked case (`lib-modules.md`, where
> recovery-by-search caught two wrong keeps and one wrong wholesale relocation),
> so the six remaining artifacts are its test rather than its ceremony. An
> external article is the more likely destination for the reasoning, after those
> six show which steps survived contact.

# Decide What Documentation an LLM Needs

Apply this procedure to documentation about a system whose authoritative
artifacts are available for inspection. Decide per independently useful claim,
table, or section. One file may contain units that need different dispositions.

The possible dispositions are:

- **author or keep** — retain content that no other source can recover;
- **relocate or consolidate** — put unique content where its consumer will
  encounter it, or keep one authoritative copy instead of several paraphrases;
- **generate or check** — retain a useful recoverable value without trusting a
  hand-maintained copy;
- **manage as a cache** — retain a judgment-dependent summary whose measured
  reading value exceeds its review cost; or
- **omit and read live** — let the reader search the authoritative source.

## Scope

Use this procedure for system descriptions, architecture overviews, module and
command references, routing maps, and similar material. An external retention
obligation, such as a public contract or compliance requirement, is an input
constraint: satisfy it before optimizing for an LLM reader.

This procedure does not establish whether a claim is correct. Verify important
claims separately. Do not remove an existing document until every unique unit
marked for relocation has reached its new home.

## Prerequisites

- Identify the candidate or existing documentation and the authoritative
  artifacts it concerns: code, tests, schemas, configuration, command help,
  contracts, decisions, or other records.
- Name the LLM consumer and its task. If actual use is unknown, treat the value
  of the documentation as an untested hypothesis rather than an established
  need.

## Steps

1. **Create a disposition table.** Add one row per independently useful unit
   with these columns:

   | Unit | Consumer question | Required reliability | Recovery result | Source grain | Document grain | Recurrence and saving | Maintenance form | Disposition | Retrieval path |
   |---|---|---|---|---|---|---|---|---|---|

   Split mixed sections until each row can receive one disposition. Do not use
   a whole file as the decision unit merely because it is already a file.

2. **Name the consumption event.** Complete this sentence for each unit:
   "When `<consumer>` is `<doing task>`, it needs `<answer>` to decide or do
   `<next action>`." State whether the answer must be exact or whether an
   orientation-level approximation is enough. Record how the consumer would
   encounter the unit: an always-loaded instruction, a task-specific route, a
   search result, a link from the change site, or an explicit invocation.

   If no concrete task, answer, and retrieval path can be named, record **no
   demonstrated LLM use**. Continue the recovery test before deciding whether
   the content can be removed; unique records may still need retention for a
   non-LLM purpose.

3. **Search for an existing home.** Search the authoritative artifacts and the
   repository's contracts, decision records, and existing documentation for the
   same rule or fact. Search for distinctive terms, likely synonyms, relevant
   symbols, and the rejected alternative when one is named.

   If a stronger source already records the same content, mark the current unit
   **duplicate**. Keep the stronger home. Retain only a short pointer from the
   current location when that pointer closes a demonstrated routing need. Do
   not keep a weaker paraphrase that may cause the reader to stop before finding
   the complete statement.

4. **Attempt recovery from the authoritative artifacts.** Without using the
   candidate unit, try to reconstruct the same answer at the required
   reliability. "Plausible prose on the same subject" is not recovery. The
   reconstruction must preserve the decisions the original supports.

   - If recovery succeeds, mark the unit **recoverable cache**. The source
     remains authoritative.
   - If recovery fails, mark it **unique content**. Common examples are intent,
     rejected alternatives, coverage boundaries, cross-component invariants,
     layering rules, protocol order, and the reason a boundary exists.
   - If only part is recoverable, split the row and run the remaining steps on
     each part separately.

5. **Place unique content in the strongest consumption path.** Choose the first
   applicable destination:

   - Express a mechanically enforceable rule as a test, schema, validator, or
     configuration constraint.
   - Put a warning about a local change in a test when practical; otherwise put
     it in a comment or docstring at the code or configuration site it
     constrains.
   - Put a cross-component invariant, protocol, architectural boundary, intent,
     or rejected alternative in the repository's durable decision or
     architecture surface.
   - Keep orientation prose only when it answers the consumption event named in
     step 2.

   Ensure the relevant change loop reaches the chosen destination. Content that
   no changing or executing process reads is archival, not operative. Add a
   route, relocate it again, or record that archival status explicitly.

6. **Test whether a recoverable cache substitutes for source reading.** Run one
   representative consumer question through both paths. Start with the terms
   the consumer would know before reading either path; do not assume it already
   knows the source's symbol names.

   First determine whether the question maps to one known, discriminating unit
   on each path. In that matched case, compare the addressed units rather than
   total artifact sizes, including search, loading, transformation,
   verification, and failure recovery. If either path fans out across units or
   supplies a key the consumer did not know, compare the aggregate paths instead
   of forcing the one-unit grain test.

   - If the documentation does not close the named question and the source must
     still be read for the same answer, mark the documentation **additive** and
     omit it. Reclassify a genuinely separate routing question in its own row.
   - In a matched one-unit comparison, if the source retrieval floor is no
     larger and the prose supplies no separate transformation or reliability
     value, omit the prose copy and read the source live.
   - If the documentation has a lower matched retrieval floor and closes the
     question, continue to the value test.
   - If fan-out, discovery, or synthesis prevents a matched one-unit comparison,
     carry its aggregate path cost into the value test explicitly.
   - If neither path reliably finds the answer, repair naming or routing before
     adding explanatory volume.

7. **Estimate cache value for the actual LLM workload.** Use one comparison
   currency and the same answer and reliability threshold on both paths:

   `cache value = net cost saved per reconstruction × reconstructions avoided − maintenance`

   Count only relevant fresh sessions. Account for durable repository maps,
   prompt caches, long-running sessions, and other reuse that reduces repeated
   reconstruction. Include the cost of detecting and repairing drift in
   maintenance.

   Keep the cache only when the result is credibly positive. If evidence is
   absent or close, prefer live source reading or the smallest routing surface
   that can be tested. Do not infer value from agent statelessness, source size,
   or whole-document compression alone.

8. **Choose the cache's maintenance form.** Use the first applicable branch:

   - If the value is mechanically derivable and comparable, generate it when
     needed or store it in a machine-locatable form that a validator re-derives
     and checks. Never retain a trusted, hand-maintained copy of deterministic
     truth.
   - If the summary requires judgment and passed the value test, name its
     sources and the source-change trigger that sends it to review. Do not claim
     exhaustive coverage unless a check enforces that claim; state its partial
     scope and preserve a fallback search instead.
   - If neither maintenance path is available, omit the cache and read the
     source live.

9. **Test audience specialization separately.** Start with one maintained
   content source for humans and LLMs. Create a separate LLM-specific content
   layer only when its marginal task benefit exceeds the extra maintenance and
   drift surface. Prefer generated consumer-specific views over two authored
   copies of the same claims.

10. **Execute the dispositions in dependency order.** For an existing
    document, first relocate unique content, then add generation, checks, review
    triggers, and retrieval routes, and only then remove duplicated or
    uneconomic units. Follow the repository's retirement and redirect rules for
    any file that becomes empty.

## Verify

- Every unit has exactly one disposition and an authoritative source or unique
  destination.
- No unique content was removed before its destination was verified.
- Every retained unit answers a named consumer question and has a retrieval
  path that fires during that task.
- Exact catalogs and completeness claims are generated, checked, or explicitly
  partial with a fallback search.
- Recoverable prose kept for convenience passed both the selective-reading test
  and the cache-value test.
- No separate LLM copy exists only because LLM sessions are stateless.

---

Relevant notes:

- [For its load-bearing part, documentation generates the system rather than describing it](../../notes/documentation-generates-the-system-rather-than-describing-it.md) — rests-on: supplies the claim-level recovery test and the distinction between recoverable cache and unique content
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) — rests-on: supplies the matched one-unit retrieval-floor comparison and its fan-out boundary in step 6
- [Opposed recompute factors do not decide documentation segmentation](../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) — rests-on: supplies the cache-value and audience-specialization tests
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: supplies the deterministic cache maintenance rule
