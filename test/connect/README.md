# Connect Skill Tests

Integration tests for the `/connect` and `/connect-new` skills. Each test runs a skill on a fixture note and checks the output.

**Workshop: `test/connect/`** — all reports are saved here.

## Fixtures

| File | Description |
|------|-------------|
| `fixtures/frontloading-stripped.md` | Copy of `frontloading-spares-execution-context.md` with all links and Relevant Notes removed |
| `fixtures/constraining-stripped.md` | Copy of `constraining.md` with all links and Relevant Notes removed |
| `fixtures/codification-intact.md` | Copy of `codification.md` with all links preserved |

## How to run

Set the workshop, then invoke the skill on a fixture:

```
Workshop is test/connect/

/connect-new test/connect/fixtures/frontloading-stripped.md
```

## Test cases

### 1. Stripped note — can it recover connections?

**Input:** `fixtures/frontloading-stripped.md` or `fixtures/constraining-stripped.md`
**Skill:** `/connect-new`
**Workshop:** `test/connect/`

**Check:**
- [ ] Report saved to `test/connect/connect-report-<name>.md`
- [ ] Discovery Trace section present (shows methodology was followed)
- [ ] Connections Found section lists connections with relationship types and reasons
- [ ] All link targets in the report point to files that actually exist
- [ ] No files were edited (discovery-only)
- [ ] Core connections recovered (compare against the real note's Relevant Notes)

**Expected core connections for frontloading:**
- `indirection-is-costly-in-llm-instructions.md` — overlaps
- `generate-instructions-at-build-time.md` — overlaps
- `codification.md` — distinguishes
- `agentic-systems-interpret-underspecified-instructions.md` — grounds
- `context-loading-strategy.md` — motivates

**Expected core connections for constraining:**
- `codification.md` — extends
- `distillation.md` — contrasts/complements
- `agentic-systems-interpret-underspecified-instructions.md` — grounds
- `storing-llm-outputs-is-constraining.md` — exemplifies
- `methodology-enforcement-is-constraining.md` — exemplifies
- `deploy-time-learning-the-missing-middle.md` — grounds
- `bitter-lesson-boundary.md` — extends

### 2. Intact note — does it handle existing links?

**Input:** `fixtures/codification-intact.md`
**Skill:** `/connect-new`
**Workshop:** `test/connect/`

**Check:**
- [ ] Report saved to `test/connect/connect-report-<name>.md`
- [ ] Existing connections identified and documented (not duplicated or removed)
- [ ] New connections found beyond existing ones
- [ ] All link targets verified
- [ ] No files were edited

### 3. No workshop set — does it fail?

**Skill:** `/connect-new`
**Workshop:** (not set)

**Check:**
- [ ] Skill stops with a message about no active workshop

## Comparing old vs new

To compare both skills on the same fixture:

```
Workshop is test/connect/

/connect test/connect/fixtures/frontloading-stripped.md
/connect-new test/connect/fixtures/frontloading-stripped.md
```

Then diff the outputs:
- Old connect: check if the fixture file was edited
- New connect: check the saved report
- Compare connection lists for coverage
