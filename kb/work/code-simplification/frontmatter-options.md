# Frontmatter Options

## Decision to make

What should Commonplace use as its canonical **markdown frontmatter** implementation now that the package can declare prerequisites?

## Status update

Part of the earlier dependency question is already resolved:

- `PyYAML` is now a base runtime dependency
- authored type definitions already use JSON Schema in YAML syntax
- the remaining question is only about markdown note frontmatter, not type-definition parsing in general

## Option A: Keep the current strict local parser

Use [`src/commonplace/lib/frontmatter.py`](../../../src/commonplace/lib/frontmatter.py) everywhere and extend it only as needed.

### Advantages

- zero new runtime dependencies
- the accepted syntax stays narrow and explicit
- parser behavior is fully under repo control

### Costs

- we own every edge case
- commands that need richer YAML forms either keep bespoke logic or force more work into the local parser
- the parser contract can drift from what users expect when they hear "YAML frontmatter"

### Best case

The KB's frontmatter contract is intentionally narrow, and the main problem is only inconsistent usage across commands.

## Option B: Keep the strict contract, but use a third-party parser underneath

Expose one `commonplace.lib.frontmatter` API, but implement parsing with a dependency such as `pyyaml` or a dedicated frontmatter library while still rejecting unsupported shapes at the Commonplace layer.

### Advantages

- removes low-level parsing code while preserving the KB's narrower contract
- commands still consume one local API
- easier to grow support for a few more YAML forms without building them by hand

### Costs

- dependency plus wrapper complexity
- some code remains because Commonplace-specific validation still exists above the parser

### Best case

We want to keep strong control over the accepted schema, but no longer want to maintain delimiter and scalar parsing ourselves.

## Option C: Replace the strict contract with standard YAML frontmatter

Use a YAML/frontmatter library directly and allow the broader syntax it supports.

### Advantages

- maximum code deletion
- least surprising to users who expect normal YAML frontmatter
- likely fixes `sync_topic_links.py` style divergences immediately

### Costs

- the KB loses a deliberately constrained file contract
- validator logic may need stronger normalization because more YAML shapes become valid
- broader syntax may make files less uniform and harder for agents to produce consistently

### Best case

The benefits of standard tooling and less bespoke code outweigh the value of the current narrow grammar.

## Current lean

Short-term, Option A looks like the right default.

Reason:

- the type-system simplification already got most of the value that justified `PyYAML`
- no live workshop, note, or source content currently appears to require richer frontmatter forms
- the biggest remaining simplification wins are dead-code deletion and helper consolidation, not frontmatter syntax expansion

Option B remains the first fallback if a real maintained use case needs broader YAML without giving up the narrower KB contract.

## Questions to answer before deciding

- Does a third-party parser actually reduce net code once Commonplace-specific validation is included?
- Which currently valid files rely on YAML forms the local parser rejects?
- If broader YAML becomes necessary, should Commonplace preserve the current narrow contract at the wrapper layer or switch fully to standard YAML frontmatter?
