# Internal Consistency

**Note:** `kb/notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md`

## Checks performed

### 1. Open mechanism vs. specific proposal

**Claim A (line 15):** "How the context engine identifies what to inject is an open design question."

**Claim B (lines 32-37):** Proposes a `definition` type as the machine-readable signal for auto-injection.

**Assessment:** These are consistent. The note distinguishes the *need* for injection (the claim) from the *mechanism* (design exploration). Line 15 explicitly says "the claim here is about the need for injection, not the mechanism." The Evidence section explores a concrete mechanism without asserting it's the final answer. No contradiction.

### 2. Current state vs. proposed state

**Claim C (line 11):** "An agent that reads a note linking to codification doesn't know the definition unless it follows the link."

**Claim D (line 57):** "The agent doesn't need to know the definition exists; the injection mechanism ensures it arrives."

**Assessment:** Consistent. C describes the current state (without injection), D describes the proposed state (with injection). The temporal framing is clear — the note argues from a problem (C) to a solution (D).

### 3. Hierarchy extension consistency

**Original hierarchy (line 54):** CLAUDE.md (always) → skill descriptions (always) → skill bodies (on invoke) → task-specific docs (on demand).

**Extended hierarchy (lines 58-63):** Always → On reference → On invoke → On demand.

**Assessment:** Consistent. The extension adds a tier between Always and On invoke without redefining the existing tiers. The mapping is preserved: CLAUDE.md and skill descriptions remain at "Always," skill bodies remain at "On invoke."

### 4. Custom runtime requirement vs. existing-surface references

**Claim E (line 66):** "Requires our own agent runtime... Auto-injection requires an agent runtime with a context engine that parses loaded documents."

**Claim F (line 81, link annotation):** "the two always-loaded surfaces (CLAUDE.md vs skill descriptions) are both candidates for automatic injection."

**Assessment:** The caveat (E) says auto-injection can't happen on Claude Code's runtime because there's no interception point. The link annotation (F) references surfaces that exist on Claude Code's runtime. This creates a mild tension: the note discusses always-loaded surfaces as "candidates for injection" while simultaneously acknowledging the runtime that hosts those surfaces can't support injection.

The resolution is that the note envisions a custom runtime that would reimplement or extend these surfaces. But the annotation doesn't signal this — it reads as if the existing surfaces could participate in injection as-is. **INFO — the link annotation for the always-loaded-context note doesn't acknowledge the runtime caveat, creating a minor tension with the Caveats section.**

### 5. Definition drift check

- **"Context engine"** — used consistently throughout to mean the component that loads documents and manages context.
- **"Auto-injection" / "automatic context injection"** — used interchangeably. No drift.
- **"On reference"** — introduced at line 56, used consistently in the hierarchy.
- **"Referential" vs "argumentative"** — used in two places (lines 25 and 15's surrounding context). Meaning is stable: referential = "as defined in" links; argumentative = links that support or counter claims.

No definition drift detected.

### 6. Summary/body alignment

**Title claim:** "Agent statelessness means the context engine should inject context automatically."

**Body development:** The Evidence section argues definitions are the cleanest case and proposes the `definition` type. The Reasoning section extends the loading hierarchy. The Caveats section identifies prerequisites (custom runtime, context budget).

The title asserts a *should* — a normative claim. The body provides the argument for why (statelessness → can't carry context → engine must provide it). The Caveats section qualifies the *should* with implementation constraints but doesn't undermine it. Aligned.

## Summary

No WARNs. One INFO:

1. **INFO:** The link annotation about always-loaded surfaces being "candidates for automatic injection" doesn't acknowledge the custom-runtime requirement stated in Caveats, creating a minor tension between two parts of the note.
