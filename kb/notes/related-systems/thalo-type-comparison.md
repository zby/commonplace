---
description: Reference for borrowing recurring note shapes from Thalo — their entity types (opinion, reference, lore, journal, synthesis) map onto our types with concrete gaps still open (supersedes links, source status tracking)
type: note
traits: [has-comparison]
status: current
areas: [related-systems, claw-design]
---

# Thalo entity types compared to claw document types

Both systems define types with structural expectations. Thalo commits to types upfront via a grammar; we [discover ours through practice](../document-types-should-be-verifiable.md). This comparison is a reference for borrowing — when we encounter a recurring note shape, we can check whether Thalo already has a useful structure for it.

## Type system mechanisms

| Dimension | Thalo | Claw |
|-----------|-------|------|
| Type declaration | `define-entity` in grammar | `type:` in YAML frontmatter |
| Sections | Required/optional per entity, grammar-enforced | Implied by templates, not validated |
| Metadata fields | Typed (`string`, `link`, `datetime`, unions), grammar-checked | Convention-based (`description`, `areas`, `status`) |
| Status tracking | Per-field (`status?: "unread" \| "read" \| "processed"`) | Orthogonal axis (`seedling`, `current`, `speculative`, `outdated`) |
| Traits | Not separated — baked into entity definitions | Independent checkable properties (`has-comparison`, `has-external-sources`, `has-implementation`) |
| Evolution | `alter-entity` directive | Edit templates, update conventions |

## Thalo's entity types mapped to ours

### opinion → structured-claim

Thalo's `opinion` has:
- `confidence`: `"high" | "medium" | "low"` (required)
- `supersedes?`: link to previous stance
- `related?`: link[]
- Sections: **Claim** (required), **Reasoning** (required), **Caveats** (optional)

Our equivalent: [`structured-claim`](../claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) with Evidence/Reasoning/Caveats sections. This was adopted after the original comparison flagged the gap — three independent threads (Thalo's opinion entity, claim titles, the affordance table) converged on the same Toulmin-derived shape. The `confidence` field and `supersedes` link remain interesting features we haven't adopted — confidence as metadata would let us query for low-confidence claims that need evidence, and `supersedes` explicitly tracks opinion evolution.

**Already borrowed:** Claim / Reasoning / Caveats sections — now the `structured-claim` base type. **Still borrowable:** `supersedes` link for tracking when one note replaces another. `confidence` field.

### reference → source-review (partial overlap)

Thalo's `reference` has:
- `url?`, `file?`, `ref-type` (`"article" | "video" | "tweet" | "paper" | "book"`)
- `author?`, `published?`, `status?` (`"unread" | "read" | "processed"`)
- Sections: **Summary**, **Key Takeaways**, **Related** (all optional)

Our `source-review` template (in `project_claw/sources/`) covers the "processed" case — it has Summary, Key Claims, Relevance to Project. But we don't have Thalo's `status` tracking for unprocessed references. Our `/ingest` skill handles the pipeline but doesn't track reading status as metadata.

**Borrowable structure:** The `status: unread | read | processed` field for source tracking. Their lighter structure (optional Summary + Key Takeaways) works for quick captures where a full source-review is overkill.

### lore → note (general)

Thalo's `lore` has:
- `type`: `"fact" | "insight"` (required)
- `subject`: `string | link` (required)
- `date?`: date-range
- Sections: **Description** (required)

This maps loosely to our general `note` type. The `fact | insight` distinction is interesting — facts are verifiable, insights are learned wisdom. We don't distinguish these; both are just notes. The `subject` field (linking lore to an entity) is similar to our `areas` but more granular.

**Borrowable structure:** The fact/insight distinction might map to our type system — `structured-claim` already marks developed insights; a trait or type for verifiable statements could mark facts.

### journal → text (rough equivalent)

Thalo's `journal` has:
- `subject`, `type` (idea, reflection, experience, doubt, question), `mood?`, `context?`
- Sections: **Entry** (required)

Our `text` type (no frontmatter) is the capture equivalent but completely unstructured. We don't have journal-style entries. The `type` field (idea, reflection, doubt, question) is a richer classification of captured thoughts than we use.

**Borrowable structure:** Not directly applicable — our agent-learnings serve a similar purpose but aren't personal reflections.

### synthesis → no equivalent

Thalo's `synthesis` is a saved query + prompt pair for repeatable synthesis operations. We have no equivalent. See the [main Thalo note](./thalo.md) for analysis — powerful map-reduce pattern but we lack the use case.

### me → no equivalent

Self-reference entity. Not applicable to our project-focused KB.

## What this comparison reveals

1. **Structured argument sections converged.** Thalo's opinion entity (Claim/Reasoning/Caveats) flagged a gap we've since filled with the [`structured-claim` type](../claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md). The convergence — both systems arriving at Toulmin-derived sections independently — validates the choice. Our `structured-claim` adds an `## Evidence` section that Thalo's opinion lacks, separating checkable facts from reasoning.

2. **We're missing status tracking for sources.** Their `unread | read | processed` pipeline status is useful. Our `/ingest` pipeline does this operationally but doesn't persist the status as queryable metadata.

3. **Our trait system has no equivalent in Thalo.** They bake everything into entity definitions. Our traits (independently checkable properties orthogonal to type) are more flexible — a `structured-claim` can carry `traits: [has-comparison, has-external-sources]`. This is an advantage, not a gap.

4. **Our status axis is richer.** Their status is per-entity-type (`unread/read/processed` for references only). Our status (`seedling/current/speculative/outdated`) applies universally and tracks commitment, not processing stage. These are complementary — we could have both.

5. **Supersedes links are valuable.** Explicitly tracking when one note replaces another is better than our current approach of marking notes `outdated` without linking to the replacement.

## Validation rules compared

Thalo has 32 deterministic validation rules. Our `/validate` skill has 14 checks mixing deterministic and LLM-judged. Here's what maps where.

### Rules we already cover

| Thalo rule | Our equivalent | Implementation |
|-----------|---------------|----------------|
| missing-required-field | Description exists | LLM (skill) |
| invalid-field-type (enums) | Type/traits/status valid | LLM (skill) |
| unresolved-link | Link health | LLM (skill) |
| missing-required-section | Type-specific structure | LLM (skill) |
| duplicate-metadata-key | Frontmatter valid | LLM (skill) |
| empty-required-value | Description exists (non-empty) | LLM (skill) |

### Rules we could adopt

- **Unknown field warning** — flag frontmatter fields not in our known set (`description`, `type`, `traits`, `areas`, `status`, `last-checked`). Catches typos like `descrption:`. Deterministic, cheap.
- **Unknown section warning** — flag unexpected H2 headings per type. Only useful once we define expected sections per type.
- **Empty section warning** — heading with no content beneath it. Catches incomplete notes. Deterministic.

### Rules that don't apply

Schema evolution rules (alter-entity, define ordering), type expression matching, timestamp ordering, synthesis rules — all specific to their grammar/format, not transferable.

### Checks we have that they don't

- **Description quality** — semantic discrimination check (LLM-judged)
- **Composability** — title works as inline prose (LLM-judged)
- **Areas-Topics consistency** — frontmatter/footer sync
- **Orphan detection** — notes with no inbound links (batch)
- **Accumulation signals** — seedling count, text file count (batch INFO)

### The architectural insight

Every one of Thalo's rules is **deterministic** — a script checks them without LLM involvement. All of our checks run through an LLM (the `/validate` skill uses Sonnet), including the deterministic ones like enum validation and link resolution.

This is the [crystallisation trajectory](../agentic-systems-learn-through-three-distinct-mechanisms.md) applied to validation itself: our deterministic checks (frontmatter valid, enum values, link health, areas-topics sync) could move to a Python script that runs in milliseconds — potentially as a pre-commit hook. The LLM-judged checks (description quality, composability, title-as-prose) stay at skill level because their [oracle strength](../oracle-strength-spectrum.md) is too low for deterministic verification.

The split would be:

| Check | Oracle strength | Belongs in |
|-------|----------------|-----------|
| Frontmatter valid | Hard | Script |
| Description exists + non-empty | Hard | Script |
| Type/traits/status enum | Hard | Script |
| Link targets resolve | Hard | Script |
| Areas-Topics sync | Hard | Script (already have `sync_topic_links.py`) |
| Unknown frontmatter fields | Hard | Script |
| Required sections per type | Hard | Script |
| Description quality | Soft | Skill |
| Composability / title-as-prose | Soft | Skill |
| Orphan detection | Hard | Script (batch) |

This would make `/validate` cheaper (skip deterministic checks already passed by the script) and enable a fast feedback loop via hook or CI.

## When to revisit this comparison

When we encounter:
- Need to track source processing status as queryable metadata
- Notes that supersede other notes (need explicit replacement links)
- Decision to split validation into script (deterministic) + skill (judgment) — see [deterministic-validation-should-be-a-script](../deterministic-validation-should-be-a-script.md)
- Any other recurring note shape — check here first whether Thalo has a useful structure for it

---

Relevant Notes:
- [document-classification](../document-classification.md) — our type system being compared
- [document-types-should-be-verifiable](../document-types-should-be-verifiable.md) — the design principle both systems share
- [claim-notes-should-use-toulmin-derived-sections](../claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — resolves the gap this comparison originally flagged: `structured-claim` with Evidence/Reasoning/Caveats sections
- [stabilisation-is-learning](../agentic-systems-learn-through-three-distinct-mechanisms.md) — the validation split (script vs skill) is crystallisation applied to the validation process itself
- [oracle-strength-spectrum](../oracle-strength-spectrum.md) — determines which checks can be deterministic (hard oracle) vs must stay LLM-judged (soft oracle)
- [quality-signals-for-kb-evaluation](../quality-signals-for-kb-evaluation.md) — the broader quality framework these validation rules feed into
- [thalo](./thalo.md) — the main system review note
- [Toulmin argument](../../sources/purdue-owl-toulmin-argument.md) — grounds: Toulmin's formal argumentation model provides the canonical decomposition (claim/grounds/warrant/qualifier/rebuttal/backing) that Thalo's opinion entity approximates with Claim/Reasoning/Caveats sections

Topics:
- [claw-design](../claw-design.md)
- [related-systems](./related-systems-index.md)
