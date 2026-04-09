# Library Survey

## Conclusion

This survey is now partly historical.

One recommendation already landed:

- `PyYAML` is now a base runtime dependency
- `jsonschema` is also a base runtime dependency
- authored type definitions now use JSON Schema in YAML syntax

That means the main unresolved question is no longer "should we add a YAML library at all?" The unresolved question is "should markdown frontmatter also move to broader YAML, or should the repo keep the current strict parser?"

Current recommendation:

- **Already adopted:** `PyYAML`
- **Reasonable but still secondary:** `python-frontmatter`
- **Possible later, not yet justified:** `markdown-it-py`
- **Not recommended for current needs:** `mistune`, `ruamel.yaml`

## 1. PyYAML

### What it already replaced

- the type-definition parsing path in [`src/commonplace/lib/type_resolver.py`](../../../src/commonplace/lib/type_resolver.py)
- the need for Commonplace to own a custom parser for authored schema files

### What it could still replace

- the custom frontmatter scalar/list parsing in [`src/commonplace/lib/frontmatter.py`](../../../src/commonplace/lib/frontmatter.py)

### Why it is a good fit

- it is current and maintained: PyPI shows version `6.0.3`, released on September 25, 2025
- the official docs explicitly recommend `yaml.safe_load` for untrusted input
- it already paid for itself on the authored-schema side

### Costs

- Commonplace would still need to define which YAML subset it wants to accept for markdown notes
- if the repo keeps its current narrow markdown-frontmatter contract, some validation logic still stays local

### Recommendation

Adopted for schemas already.

Do not treat that as an automatic reason to broaden markdown frontmatter. Only move markdown frontmatter to `PyYAML` if it deletes meaningful code beyond the already-solved schema path.

## 2. python-frontmatter

### What it would replace

- frontmatter delimiter detection and split/load flow in markdown files
- possibly some of the wrapper code around `frontmatter.parse()` / `strip()`

### Why it is attractive

- it is small and purpose-built for Jekyll-style front matter
- it supports loading from files or raw text
- it can handle YAML, JSON, TOML, and other handlers

### Limits

- it does **not** help with authored schema files
- it likely still sits on top of a YAML parser rather than replacing that need
- if Commonplace wants a strict subset, it still needs wrapper validation

### Recommendation

Useful only if the main goal is to stop owning frontmatter delimiter logic.

It is still weaker than just keeping one local wrapper unless delimiter handling becomes the real pain point.

## 3. markdown-it-py

### What it would replace

- regex-based markdown link extraction in [`src/commonplace/cli/promotion_candidates.py`](../../../src/commonplace/cli/promotion_candidates.py)
- regex-based link extraction in [`src/commonplace/review/run_review_bundle.py`](../../../src/commonplace/review/run_review_bundle.py)
- potentially other markdown-structure helpers if Commonplace starts doing richer AST-level work

### Why it is credible

- it is current and maintained: PyPI shows version `4.0.0`, released on August 11, 2025
- official docs expose a token parser API
- the plugin ecosystem includes front matter support through `mdit-py-plugins`

### Why it is not the first dependency to add

- current link extraction needs are still modest
- it would add a full markdown parser to solve a narrower problem than the remaining duplication
- the repo is not yet doing AST-level markdown transformations where this would clearly pay off

### Recommendation

Keep this as a later option if link handling or markdown structure work grows more complex.

Right now it is plausible cleanup, not the highest-value next move.

## 4. mistune

### Why it came up

It is a current Python markdown parser and could also replace regex markdown parsing.

### Why it is weaker here

- the main simplification need is not HTML rendering
- `markdown-it-py` has a clearer token/plugin story for structural markdown parsing
- nothing in the repo currently suggests we need Mistune-specific strengths

### Recommendation

Do not prefer this over `markdown-it-py` for Commonplace.

## 5. ruamel.yaml

### Why it came up

It is a well-known YAML library often used when comment-preserving or round-trip editing matters.

### Why it is overkill here

- Commonplace mostly reads YAML rather than preserving author formatting during writes
- the remaining custom code is about parsing and validation, not round-trip YAML editing
- `PyYAML` is already enough for the current simplification targets

### Recommendation

Do not add this unless Commonplace starts editing YAML files while preserving formatting/comments.

## Practical recommendation

If the goal is to simplify the current code from today's state:

1. Treat the `PyYAML` decision as already made for authored schemas
2. Do not expand markdown frontmatter syntax unless a real maintained command needs it
3. Prefer deletion of obsolete `areas` / `Topics` tooling over adding parser flexibility for historical commands
4. Consolidate remaining note parsing onto `note_parser` and `frontmatter.strip()`
5. Re-evaluate `markdown-it-py` only if link handling grows beyond the current regex-plus-code-strip needs

That path deletes the most real complexity with the smallest conceptual expansion.
