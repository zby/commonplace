# Marketplace setup for plugin distribution

## Testing (now)

```bash
claude --plugin-dir .
```

No marketplace needed. Skills load directly from the repo's `skills/` directory.

For Codex, the supported local install flow is repo-local marketplace registration plus interactive install in `/plugins`. This repo now ships `.agents/plugins/marketplace.json` for dogfooding; it points `source.path` to `./` because the repo root is the plugin directory.

```json
{
  "name": "local-commonplace",
  "interface": {
    "displayName": "Local Commonplace Plugins"
  },
  "plugins": [
    {
      "name": "commonplace",
      "source": {
        "source": "local",
        "path": "./"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

After changing `.codex-plugin/plugin.json`, `skills/`, or `.agents/plugins/marketplace.json`, restart Codex, run `/plugins`, open `Local Commonplace Plugins`, and install `commonplace`.

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

### Codex consuming-project setup

For a project that vendors this repo as `./commonplace`, the host repo needs its own `.agents/plugins/marketplace.json` entry pointing to `./commonplace`:

```json
{
  "name": "local-commonplace",
  "interface": {
    "displayName": "Local Commonplace Plugins"
  },
  "plugins": [
    {
      "name": "commonplace",
      "source": {
        "source": "local",
        "path": "./commonplace"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

The plugin payload itself still lives in `commonplace/.codex-plugin/plugin.json` plus `commonplace/skills/`. The marketplace file belongs to the host repo, not inside the vendored copy.
