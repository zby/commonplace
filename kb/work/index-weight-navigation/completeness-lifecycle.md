# The completeness-mark lifecycle: what each consumer actually needs
Design deliberation for the `complete` mark on `tag-readme` artifacts. The question: a complete tag-README inevitably grows into the weight gate and must drop the mark — splitting cannot rescue completeness without doing something illogical to the parent tag. So what is the mark actually _for_, what does each consumer lose when it drops, and what should the exit discipline be?
## The mechanism and its inherent dynamic
A `tag-readme` with `complete: true` makes two enforced promises: every note carrying the tag is linked (membership check, same query as the rg recipe), and the file sits under the weight gates (type contract: small).

This creates a **write-side obligation**: writing a new note with tag T fails validation until the writer adds an entry to T's README. That coupling is the engine of the whole lifecycle:

1. Each new tagged note adds ~150–300 B (link + context phrase).
  
2. The README crosses the soft gate (~8 KB, ≈25–30 entries): warning — plan the exit.
  
3. It approaches the hard gate (~16 KB, ≈55–60 entries): the mark **must** drop.
  

The drop is not a failure to be engineered away; growth makes it inevitable for any successful tag. The design question is making the drop _cheap_, not preventing it.
## The safety property everything else hangs on
**The mark is an accelerator, never a load-bearing wall.** No consumer's correctness may depend on the mark being present — the scoped `rg` query is always available and always truthful, so enumeration completeness is recoverable at the cost of one tool call regardless of any README's state. The mark only saves work and adds trust.

The asymmetry matters in one direction only: an _unmarked but actually complete_ README is harmless (the reader runs an rg it didn't need); a _marked but incomplete_ README is the disaster — it tells exhaustive consumers to stop looking while members are missing. This is the [stale-indexes problem](../../notes/stale-indexes-are-worse-than-no-indexes.md) in its sharpest form, and it is why the mark must be machine-enforced or not exist.
## Consumers, one by one
**cp-skill-connect (exhaustive prospector).** Needs _full membership_ of destination tags to guarantee candidate coverage. With the mark: one README read delivers membership plus editorial signal, and the by-tag rg call is skipped. Without: the rg recipe delivers membership as path + description. Coverage is guaranteed either way; what differs is one tool call and the triage signal (curated context phrases vs frontmatter descriptions — descriptions are written as retrieval filters, so the difference is modest). **Verdict: the mark is a minor optimization for connect; its loss costs almost nothing.**

**Targeted lookup ("find the note about X in T").** Needs routing, not enumeration. A selective README with good groupings often routes _better_ than a complete flat listing — orientation beats coverage here, and `rg` by keyword bypasses the README entirely. The strongest routing form is **typed children**: a README that says "there are three kinds of notes under this tag" and links the three child tag-READMEs. But that claim is structural — "the children cover T" — and without a check it decays silently as notes accumulate outside every child; this is the same marked-but-stale failure as a false `complete`, only at the routing level. The enforceable version is the `covered_by` mark analyzed in exit (c) below. **Verdict: indifferent to the** `complete` **mark itself; the consumer that benefits from an enforced _coverage_ mark.**{>>If there are sub-tags - this can be very effective - the readme could say - for example something like this: "there are three types of notes with this tag" - and then list the child tags. But then we would not have any enforcement.<<}{id="c1" by="user" at="2026-06-10T06:26:18.590Z"}{>>Agreed — and this overturned my exit-(c) verdict: the coverage claim IS enforceable with the same query machinery (membership(T) ⊆ union of child memberships), so I promoted it to a designed second mark, `covered`, with adoption deferred to the first real case. Rewrote this paragraph, exit (c), the lifecycle diagram, and discipline point 5.<<}{id="c2" by="AI" at="2026-06-10T06:29:11.000Z" re="c1"}

**Summarizer / surveyor ("what do we know about T?").** Needs representative coverage plus structure, and crucially a _truthful partial signal_: it must know whether the curated picks are everything or a selection. The mark provides that signal positively; its absence says "run the rg to find the residual." Either way the surveyor can be correct — the danger is only the false positive, covered by enforcement. The curated groupings (which survive the drop) matter more to the summary's quality than enumeration does. **Verdict: needs the mark to be _honest_, not to be _present_.**

**Human on the published site.** Gets the build-time generated tail appended to every tag-README regardless — always complete, with sublinear skim/search access ([the access-cost split](../../notes/design-for-the-first-time-human-except-on-access-cost.md)). **Verdict: cannot tell whether the mark exists.**

**The writer (cp-skill-write path).** The mark converts fuzzy curation ("should this note be in the index?") into a deterministic, checkable obligation: tag T → entry in T's README, written at the moment the writer has the note's context loaded — the best possible moment to produce a context phrase. When the mark drops, the obligation lifts and curation reverts to periodic maintenance ([maintain-curated-indexes](../../instructions/maintain-curated-indexes.md)), where placement decisions are made cold. **Verdict: the mark's main beneficiary is write-time curation quality; its main cost is the same coupling.**

**The maintainer / auditor.** With the mark: nothing to audit for completeness (validation does it); audit attention goes to phrase quality and groupings. Without: the curated-vs-membership comparison is a manual step in the maintenance instruction. **Verdict: the mark shifts completeness work from periodic audit to write time.**
## What the mark actually buys
Summing the consumers: enforced trust (one read, no follow-up call, for exhaustive readers), guaranteed _editorial_ coverage (a phrase for every member, produced at write time when context is hot), and a deterministic write-side curation trigger. What it does **not** buy: anything irreplaceable — rg backstops enumeration for every consumer.

This is why fighting to preserve completeness through growth is the wrong instinct: the thing being preserved is a convenience, and the structures needed to preserve it cost more than the convenience is worth.
## The exits, analyzed
When a complete README approaches the hard gate:

**(a) Drop to selective — the default.** Remove the mark, trim the entries to the editorial best-of. Exhaustive consumers fall back to rg (one extra call); the groupings and best phrases survive; the write-side obligation lifts. Cheap, honest, no new structure. The trimmed-out phrases are a real but bounded loss — they can seed child READMEs later if substructure emerges.

**(b) Split with overlap — an editorial act, not a completeness rescue.** When the README's own groupings reveal genuine substructure, mint child tags. Child-tagged notes **keep the parent tag** (tags overlap per ADR 004) — removing it would be illogical, since the notes still are about T. The parent README goes selective and links the child READMEs with context phrases; small children may take their own complete marks. Note what this does _not_ do: it does not restore the parent's completeness. The parent's full membership is still rg-only.

**(c) The** `covered_by` **mark — designed, adoption deferred to the first real case.** _(Revised after review comment c1: an earlier draft dismissed this; the routing framing changes the verdict.)_ A grown tag can make a different enforceable claim than `complete`: not "every member is linked here" but "every member carries at least one of these child tags" — checked as membership(T) ⊆ ∪ membership(child_i), the same query machinery as the membership check.

**The mechanism needs a symbol the system doesn't have yet.** Nothing currently connects tags to each other — tags are flat strings, and child relationships exist only as free-form prose inside README bodies, which validation cannot consume. The check needs a machine-readable children list, so the mark _is_ the list: `covered_by: [child-a, child-b]` in the parent README's frontmatter. One field carries both the claim and its parameters, so they cannot drift apart (the ADR 024 move: the contract lives on the artifact that makes it). The body's routing narrative ("there are three kinds of notes here…") stays free-form prose linking the child READMEs with context phrases — frontmatter holds the operative part, prose holds the orientation. The alternative — child-side `parents:` pointers with the parent deriving its children by query — was considered and rejected: the coverage claim is the _parent's_ contract, a child can legitimately serve several parents, and a parent whose claim depends on a derived set can change meaning without being edited. This stays the only symbolic tag-to-tag relation; "Related Tags" prose remains editorial, and no general tag ontology is introduced (mint the symbol only where a checked claim consumes it).

Its properties differ from `complete` in exactly the ways growth punishes:

- **Weight-immune.** The README links a handful of children, not every member, so it stays far under the gates no matter how large T grows. `covered` is the mark that _survives_ growth; `complete` is the one that can't.
  
- **The write obligation transfers instead of lifting.** A new T note must take at least one child tag — taxonomy pressure, the arscontexta cost, but now _explicit and enforced_ rather than a silently decaying prose claim ("there are three kinds of notes here") that nobody checks. The smell to watch: a catch-all child (`T-misc`) makes coverage trivially satisfiable while destroying its routing value.
  
- **Who gains:** targeted lookup gets trustworthy typed routing ("which kind of T is this?"); exhaustive consumers get a recursion guarantee (union the children, each of which is itself `complete`, `covered`, or rg-backed). Who doesn't: connect can still just rg the parent — for flat enumeration the mark adds nothing over the query.
  

**Verdict: keep it designed but unadopted until a real tag exercises it — the natural first candidate is** `learning-theory` **(55 notes, visible clusters) when its README migrates.** The _unenforced_ version — prose claiming the children cover the tag — should never be written; that is the routing-level stale-index failure.

**(d) Retire the parent tag.** Only when the concept itself has dissolved into its children — not as a size remedy. While notes are still legitimately about T, removing T from them to shrink a listing is the tail wagging the dog.

The forbidden state is unchanged: partial migration, where some child-tagged notes keep the parent tag and some don't — the parent's membership becomes neither complete nor honestly selective, and the structure goes invisible (the arscontexta failure).
## The lifecycle, stated
```
(no README)                tag accumulates ~5+ notes, curation worth it
    │ create selective
    ▼
SELECTIVE ──────────────── author curates all members, fits gates
    │ add complete: true       (validation confirms membership)
    ▼
COMPLETE ────────────────── each new tagged note must add an entry
    │ soft warn (~8 KB): plan the exit
    │ hard gate (~16 KB) approaching:
    ▼
exit (a) drop to selective            [default]
exit (b) split with overlap           [only if substructure is editorially real;
    │                                  parent → selective, children may go complete]
    │ exit (c) covered_by: [children] [designed, unadopted: enumerated children
    ▼                                  enforced to cover T; weight-immune]
SELECTIVE (default end state for large tags; rg is the membership surface)
  or COVERED (if/when exit (c) is first exercised)
```

A large tag's default end state is _selective head + rg membership + build-time tail_ — the same surface set as a tag that never declared complete. The `complete` mark is a small-tag affordance that degrades gracefully, not a status to defend; `covered_by` is the designed (unadopted) growth-proof alternative for tags with real substructure.
## Refined discipline (supersedes the coarser bullet in the workshop README)
1. The mark may be declared only while full membership fits under the gates; validation enforces both directions (membership and weight).
  
2. No consumer behavior may _require_ the mark; consumers treat it as a skip-one-call optimization (connect records in its trace which tags it skipped the rg for).
  
3. The default exit is drop-to-selective. Splitting is justified by visible substructure only, never by the desire to stay complete.
  
4. Splits overlap: children add tags, the parent tag stays on every note. Parent README links children. Retiring the parent tag is a separate, rare decision about the concept, not about size.
  
5. The `covered_by` mark (c) is designed but not adopted: never write the unenforced prose version of the claim ("the children cover this tag"); adopt the enforced mark the first time a real tag needs typed routing at scale, with `learning-theory` as the natural candidate. The frontmatter list is the only symbolic tag-to-tag relation; watch for the catch-all-child smell.
  
## Open questions
- Should the hard-gate failure message _instruct_ the drop (and should dropping be manual-only)? Leaning manual: the trim that accompanies it is editorial work, and an auto-drop would silently degrade the write-side obligation.
  
- Should the soft warn on a complete README carry a distinct message ("plan the completeness exit") vs the generic weight warning?
  
- Does the hub (`tags-README.md`, complete over the set of tag-READMEs) follow the same lifecycle? Its membership grows much more slowly; it plausibly stays complete indefinitely, which is fine — the lifecycle just never fires.
  
- Should each tag listed in `covered_by` be required to have its own tag-README (the routing link target), or is a bare child tag with rg-only membership acceptable?
- When entries are trimmed at exit (a), is there value in parking the dropped phrases somewhere (the build tail shows description, not the lost phrase)? Current lean: no — phrases are cheap to rewrite when a child README wants them, and parking creates a stale-phrase store.
  

* * *

Relevant notes:

- [stale indexes are worse than no indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: the marked-but-incomplete README is the catastrophic state; enforcement is the defense
  
- [design for the first-time human, except on access cost](../../notes/design-for-the-first-time-human-except-on-access-cost.md) — grounds: the build-time tail keeps human readers complete regardless of the mark
  
- [index curation adds orientation that generation cannot produce](../../notes/index-curation-adds-orientation-that-generation-cannot-produce.md) — rationale: the groupings and phrases are the durable value; they survive the mark's drop
  
- [frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — mechanism: the write-side obligation lands the phrase-writing at the moment the note's context is already loaded
  
- [feasibility is the heaviest fork's net load](../../notes/feasibility-is-the-heaviest-forks-net-load.md) — grounds: connect is the exhaustive consumer whose per-destination cost this design bounds
