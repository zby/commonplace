# Marketplace setup for plugin distribution

## Testing (now)

```bash
claude --plugin-dir .
```

No marketplace needed. Skills load directly from the repo's `skills/` directory.

## Distribution (later)

### Option A: Self-hosted marketplace (simplest)

Add `.claude-plugin/marketplace.json` alongside the existing `plugin.json`:

```json
{
  "name": "commonplace-marketplace",
  "owner": { "name": "Zbigniew Lukasiak" },
  "plugins": [
    {
      "name": "commonplace",
      "source": ".",
      "description": "Skills and templates for agent-operated knowledge bases.",
      "version": "0.1.0"
    }
  ]
}
```

After pushing to GitHub, practitioners install with:

```bash
claude plugin marketplace add zby/commonplace
claude plugin install commonplace@commonplace-marketplace
```

### Option B: Separate marketplace repo

Create a separate repo (e.g., `zby/commonplace-marketplace`) with `.claude-plugin/marketplace.json`:

```json
{
  "name": "commonplace-marketplace",
  "owner": { "name": "Zbigniew Lukasiak" },
  "plugins": [
    {
      "name": "commonplace",
      "source": {
        "source": "github",
        "repo": "zby/commonplace",
        "ref": "main"
      },
      "description": "Skills and templates for agent-operated knowledge bases.",
      "version": "0.1.0"
    }
  ]
}
```

Practitioners install with:

```bash
claude plugin marketplace add zby/commonplace-marketplace
claude plugin install commonplace@commonplace-marketplace
```

**Advantage:** can add more plugins later, version marketplace independently.

### Versioning

Use `ref` in the source to point to tags for stable releases:

```json
{
  "source": {
    "source": "github",
    "repo": "zby/commonplace",
    "ref": "v0.1.0"
  }
}
```

### Codex

Codex uses `.codex-plugin/plugin.json` (already created). Codex marketplace setup may differ — check Codex plugin docs when ready.
