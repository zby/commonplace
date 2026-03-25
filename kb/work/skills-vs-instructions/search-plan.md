# Verification Plan: Skills vs Instructions

The file format is irrelevant — you can freely convert between the two. The only question is the loading mechanism: what does the skill pathway do that the instruction pathway doesn't, and does it matter?

## Phase 1: Establish ground truth (local)

### 1.1 What does the Skill tool do?
- Observe: when a skill is invoked, what actually happens? Is it `Read(file)` + "follow this", or does it inject variables, set up state, modify conversation mode?
- **Key question**: Is there runtime behavior that `Read(instruction_file)` doesn't get?

### 1.2 Is `Skill("X")` different from `Read("path/to/X.md")`?
- When the agent follows a CLAUDE.md routing rule ("when doing X, read Y.md"), it calls `Read`. Compare the result to what happens when the Skill tool fires.
- **Key question**: Same content loaded — does the loading pathway change agent behavior?

### 1.3 Do the two discovery surfaces differ?
- Skills appear in system-reminder messages as a list with descriptions and trigger conditions.
- Instructions appear in CLAUDE.md routing table entries with conditions and paths.
- Both are always-loaded. Both carry name + description + condition.
- **Key question**: Does one surface produce more reliable activation than the other, or are they equivalent?

### 1.4 Token cost
- Measure a skill description line vs a routing table entry. Both are ~1-2 lines.
- Check for hidden costs: Skill tool schema tokens, descriptions repeated in multiple places.
- **Key question**: Any real cost difference, or roughly equivalent as expected?

## Phase 2: Platform documentation (web searches)

### 2.1 Claude Code skills — official guidance
- **Query**: `"claude code" skills ".claude/skills" documentation guide`
- **Query**: `site:docs.anthropic.com claude code skills`
- **Verify**: Does Anthropic document any mechanical difference beyond discovery? Any guidance on when to use skills vs CLAUDE.md instructions?

### 2.2 The Skill tool internals
- **Query**: `"claude code" "Skill tool" invocation what it does`
- **Query**: `"claude code" skill invoke vs read instruction`
- **Verify**: Is there documented behavior of the Skill tool beyond loading file content?

### 2.3 Codex equivalent
- **Query**: `codex AGENTS.md skills agents documentation`
- **Verify**: Does Codex make the same distinction? Different loading mechanism?

## Phase 3: Practitioner evidence (web searches)

### 3.1 Skills vs instructions in practice
- **Query**: `"claude code" skill vs CLAUDE.md instruction when to use`
- **Query**: `"CLAUDE.md" routing instructions best practice 2025 2026`
- **Verify**: Do practitioners report any behavioral difference (reliability, compliance) between the two pathways?

### 3.2 Activation reliability
- **Query**: `"claude code" skill "not triggered" OR "doesn't activate" OR "doesn't invoke"`
- **Query**: `"CLAUDE.md" routing rule "agent ignores" OR "agent doesn't follow"`
- **Verify**: Is one activation mechanism more reliable than the other in practice?

### 3.3 Cross-platform
- **Query**: `cursor custom command vs rules file instruction routing`
- **Query**: `agent system prompt instruction vs invokable skill comparison`
- **Verify**: Does the same loading-mechanism distinction appear across platforms? What do other platforms reveal?

## Phase 4: Synthesis

Write `findings.md`:

1. List every verified mechanical difference in the loading mechanism
2. For each difference, evaluate whether it matters (does it change discoverability, composability, or trustworthiness of the procedure?)
3. Assess whether the current KB claim ("instructions are skills without automatic routing") holds
4. Answer the workshop question: when should you create a skill, and when is a CLAUDE.md routing entry enough?
