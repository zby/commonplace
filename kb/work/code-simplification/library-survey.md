# Library Survey

## Conclusion

Yes, Commonplace could use external libraries now, and one of them looks clearly justified:

- **Recommended to consider:** `PyYAML`
- **Reasonable but secondary:** `python-frontmatter`
- **Possible later, not yet justified:** `markdown-it-py`
- **Not recommended for current needs:** `mistune`, `ruamel.yaml`

The key test is whether a dependency deletes complexity in more than one place. `PyYAML` passes that test because it can simplify both markdown frontmatter parsing and `types/*.yaml` parsing.

## 1. PyYAML

### What it would replace

- the custom frontmatter scalar/list parsing in [`src/commonplace/lib/frontmatter.py`](../../../src/commonplace/lib/frontmatter.py)
- the custom YAML parsing in [`src/commonplace/lib/type_resolver.py`](../../../src/commonplace/lib/type_resolver.py)
- the special-case block-list handling in [`src/commonplace/cli/sync_topic_links.py`](../../../src/commonplace/cli/sync_topic_links.py)

### Why it is a good fit

- it is current and maintained: PyPI shows version `6.0.3`, released on September 25, 2025
- the official docs explicitly recommend `yaml.safe_load` for untrusted input
- it solves two real parser surfaces in this repo, not just one

### Costs

- Commonplace would need to define which YAML subset it still wants to accept
- if the repo keeps its current narrow frontmatter contract, some validation logic still stays local

### Recommendation

This is the strongest candidate for a new base runtime dependency.

If adopted, Commonplace should still keep a local wrapper module so the KB contract stays under repo control even if parsing moves to `yaml.safe_load`.

## 2. python-frontmatter

### What it would replace

- frontmatter delimiter detection and split/load flow in markdown files
- possibly some of the wrapper code around `frontmatter.parse()` / `strip()`

### Why it is attractive

- it is small and purpose-built for Jekyll-style front matter
- it supports loading from files or raw text
- it can handle YAML, JSON, TOML, and other handlers

### Limits

- it does **not** help with `types/*.yaml`
- it likely still sits on top of a YAML parser rather than replacing that need
- if Commonplace wants a strict subset, it still needs wrapper validation

### Recommendation

Useful only if the main goal is to stop owning frontmatter delimiter logic.

If we add just one dependency, `PyYAML` has broader payoff than `python-frontmatter`.

## 3. markdown-it-py

### What it would replace

- regex-based markdown link extraction in [`src/commonplace/cli/validate_notes.py`](../../../src/commonplace/cli/validate_notes.py) and [`src/commonplace/cli/promotion_candidates.py`](../../../src/commonplace/cli/promotion_candidates.py)
- potentially frontmatter/token parsing for markdown workflows if used with plugins

### Why it is credible

- it is current and maintained: PyPI shows version `4.0.0`, released on August 11, 2025
- official docs expose a token parser API
- the plugin ecosystem includes front matter support through `mdit-py-plugins`

### Why it is not the first dependency to add

- current link extraction needs are modest
- it would add a full markdown parser to solve a narrower problem than the YAML duplication
- the repo is not yet doing AST-level markdown transformations where this would clearly pay off

### Recommendation

Keep this as a later option if link handling or markdown structure work grows more complex.

Right now it is a plausible cleanup tool, not the highest-value one.

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
- the custom code today is about parsing and validation, not round-trip YAML editing
- `PyYAML` is simpler and already enough for the current simplification targets

### Recommendation

Do not add this unless Commonplace starts editing YAML files while preserving formatting/comments.

## Practical recommendation

If the goal is to simplify the current code with minimal dependency creep:

1. Add `PyYAML`
2. Keep `commonplace.lib.frontmatter` as the public wrapper
3. Use `yaml.safe_load` underneath for frontmatter payloads and `types/*.yaml`
4. Refactor `sync_topic_links.py` to stop using bespoke regex YAML parsing
5. Re-evaluate `markdown-it-py` only after the YAML duplication is gone

That path deletes the most bespoke parsing with the smallest conceptual expansion.
