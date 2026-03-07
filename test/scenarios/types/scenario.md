---
description: ""
type: scenario
frequency: common | occasional | rare
---

# {Scenario name}

{One paragraph: what the user wants, what the agent must do.}

## Steps

### 1. {Step name}
- **Context needed:** {what the agent needs to know}
- **Source:** {file path or "always loaded" or "variable"}
- **Hops:** {0 = already loaded, 1 = one read, N = multiple reads}
- **Fixed/Variable:** fixed | variable
- **Notes:** {why this many hops, what could change}

### 2. {Step name}
...

## Escalation path (installed projects only)

{Steps that only apply when the agent hits a case distilled skills don't cover.
Each step follows the same format. These steps are weighted lower in the calculation
because they're conditional.}

## Variants

{Notes on how this scenario differs between commonplace repo and installed projects,
if the step table above doesn't capture it.}
