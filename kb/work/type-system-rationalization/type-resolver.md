# Type resolver

Given a file and its frontmatter, return the structural profile the validator should apply.

## Lookup algorithm

1. **Determine type name** from frontmatter:
   - No frontmatter → `text`
   - Frontmatter without `type:` → `note`
   - Frontmatter with `type: X` → `X`

2. **Determine scopes** from the file's path (three fixed levels, no directory walking):
   - If file is in `kb/work/{workshop}/**` → workshop scope is `kb/work/{workshop}/`
   - If file is in `kb/{collection}/**` → collection scope is `kb/{collection}/`
   - Root scope is always `./` (repo root)

3. **Look up definition** with scoped fallback:
   - If workshop scope exists: check `{workshop}/types/{type}.yaml`
   - If collection scope exists: check `{collection}/types/{type}.yaml`
   - Check `types/{type}.yaml` (repo root)
   - If not found at any level: return base `note` profile (graceful degradation)

Workshop-local types let a workshop define specialized artifact kinds without polluting the collection or global vocabulary. The types disappear when the workshop is archived.

A workshop that develops its own types is a proto-collection. If it stabilizes, the upgrade path is: move `types/` to the new collection, move artifacts. Type names stay the same — the resolver finds them at a different scope level. No frontmatter changes needed.

## YAML schema

```yaml
# required
base: note                    # parent type — inherit its checks

# optional — each adds checks on top of base
required_headings:
  - "## Context"
  - "## Decision"
  - "## Consequences"

required_fields:              # frontmatter fields beyond base
  - last-checked

allowed_status:               # overrides base status vocabulary
  - proposed
  - accepted
  - superseded
  - deprecated
```

Fields not specified are inherited from the base type. `text` has no base and no requirements.

## Base type definitions

`types/text.yaml`:
```yaml
# no requirements — always valid
```

`types/note.yaml`:
```yaml
required_fields:
  - description
allowed_status:
  - seedling
  - current
  - speculative
  - outdated
```

## Collection type definitions

`kb/notes/types/structured-claim.yaml`:
```yaml
base: note
required_headings:
  - "## Evidence"
  - "## Reasoning"
```

`kb/notes/types/adr.yaml`:
```yaml
base: note
required_headings:
  - "## Context"
  - "## Decision"
  - "## Consequences"
allowed_status:
  - proposed
  - accepted
  - superseded
  - deprecated
```

`kb/notes/types/index.yaml`:
```yaml
base: note
```

`kb/notes/types/related-system.yaml`:
```yaml
base: note
required_headings:
  - "## Core Ideas"
  - "## Comparison with Our System"
  - "## Borrowable Ideas"
  - "## Curiosity Pass"
  - "## What to Watch"
required_fields:
  - last-checked
```

`kb/sources/types/source-review.yaml`:
```yaml
base: note
```

## Inheritance

The resolver merges profiles up the base chain:

1. Load the type's YAML
2. Load its `base` type's YAML
3. Merge: child's `required_headings` and `required_fields` add to parent's; child's `allowed_status` replaces parent's (if specified)

With current types this is always one level deep (`X` → `note`). Deeper chains work the same way if needed.

## Integration with validator

The validator replaces its hard-coded `TYPE_HEADINGS` map with a call to the resolver:

```python
profile = resolve_type(file_path, frontmatter)
# profile.required_headings, profile.required_fields, profile.allowed_status
```

The resolver is a pure function: path + frontmatter in, structural profile out. No side effects, no state.

---

Workshop context:

- [design.md](./design.md) — types are structural, definitions are two files (.md + .yaml)
- [resolution-algorithm.md](./resolution-algorithm.md) — overall resolution steps including traits
- [review-integration.md](./review-integration.md) — traits route review gates (separate from this resolver)
