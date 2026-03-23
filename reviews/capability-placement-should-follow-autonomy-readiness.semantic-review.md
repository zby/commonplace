=== SEMANTIC REVIEW: capability-placement-should-follow-autonomy-readiness.md ===

Claims identified: 8

1. "Capability placement is a separate decision from AGENTS.md control-plane design." (opening paragraph)
2. "The organizing variable is autonomy readiness: how safely and reliably the agent can execute a capability without human steering." (opening paragraph)
3. Three-tier decision rule: Ready -> skills; Reusable but not autonomous-ready -> instructions; Exploratory or unstable -> methodology/operations notes (Decision rule section)
4. "AGENTS.md should not carry capability inventories." (Consequence section)
5. "If a capability is autonomy-ready, the agent runtime exposes it through skills." (Consequence section)
6. "AGENTS.md may still contain minimal routing pointers...when omission would create high-cost failure" (Consequence section)
7. Four-step migration path: capture in notes -> distill into instructions -> promote to skill -> remove pointers (Migration path section)
8. "This sequence prevents premature automation while avoiding AGENTS.md bloat." (closing line)

WARN:
- [Completeness] The three-tier decision rule uses "autonomy readiness" as its single organizing variable, but the linked parent note (agents-md-should-be-organized-as-a-control-plane.md) uses a two-variable model: loading frequency x failure cost. A capability could be autonomy-ready yet have low loading frequency (rarely needed), or not autonomy-ready yet have high failure cost (dangerous if the agent improvises instead of following a procedure). The note does not address how autonomy readiness interacts with these two variables. Boundary case: a capability that is safe for autonomous execution but only used once a quarter -- the decision rule says "promote to skill," but the control-plane note's logic says "occasional -> operations catalogue." The two frameworks give conflicting placement advice for this case.

- [Completeness] The decision rule's middle tier ("Reusable but not autonomous-ready -> keep as instruction") conflates two different reasons a capability might not be autonomous-ready: (a) the procedure itself is unstable or still being refined, and (b) the procedure is stable but requires human judgment at decision points. These have different implications -- (a) should mature toward autonomy, (b) may permanently require human steering. The note treats autonomy readiness as a temporary property on a migration path, but some capabilities may be structurally non-autonomous. Boundary case: a "delete and restructure a note cluster" operation that is well-understood but always requires human taste -- the migration path implies it should eventually become a skill, but it may never be safe to automate.

- [Grounding / Scope mismatch] The note claims "Capability placement is a separate decision from AGENTS.md control-plane design," but the parent note (agents-md-should-be-organized-as-a-control-plane.md) already includes capability inventories in its exclusion rules (line 93: "capability inventories (injected or non-injected)") and discusses lifecycle guidance (section "Lifecycle of guidance," lines 98-108) that covers the same progression this note formalizes. The parent note treats capability placement as a consequence of the control-plane model, not a separate decision. This note reframes it as independent, but the linked source treats it as derived. The relationship annotation says "isolates the separate decision rule," but the source material suggests the rule was already embedded, not separate.

INFO:
- [Completeness] The three tiers map to three artifact locations (skills, kb/instructions/, notes), but the note does not address capabilities that span tiers. Boundary case: a capability like "/connect" where some sub-operations are autonomous-ready (scan descriptions, check links) while others require human judgment (deciding whether a connection is substantive). The decision rule assumes capabilities are atomic units placed in one tier, but real capabilities may have mixed autonomy profiles.

- [Grounding / Vocabulary] The note uses "autonomy readiness" as if it were a single assessable property, but neither the note nor any linked source defines how to assess it. The instructions-are-skills-without-automatic-routing note describes the skill/instruction boundary as "a judgment call about whether the procedure is common enough to warrant automatic routing" (line 46) -- framing the distinction as about frequency of use, not autonomy readiness. The skills-derive-from-methodology-through-distillation note frames the progression as about distillation quality, not safety/reliability. The note's organizing variable does not appear in any of its sources -- it is the note's own coinage, which is legitimate, but readers may assume the linked notes share this framing when they do not.

- [Internal consistency] The migration path (step 3: "Promote to skill only after repeated successful autonomous execution") implies empirical testing as the gate for promotion. But the decision rule uses the static label "Ready for autonomous use" without specifying how readiness is assessed. The migration path implicitly defines readiness as track-record-based; the decision rule leaves it undefined. These are compatible but the gap means the decision rule alone is not actionable -- you need the migration path to know what "ready" means.

- [Grounding / Domain] The maintenance-operations-catalogue note describes a four-step distillation pipeline (capture -> re-run -> mark ready -> distill to instructions) that partially overlaps with but is not identical to this note's four-step migration path. The maintenance note's pipeline terminates at instructions; this note's migration path continues to skills and pointer removal. The two sequences are compatible but the note does not acknowledge that its migration path extends rather than replaces the catalogue's pipeline, which could cause confusion about which sequence governs.

PASS:
- [Internal consistency] The consequence for AGENTS.md ("should not carry capability inventories") is consistent with the parent note's exclusion rules, which list "capability inventories (injected or non-injected)" as content that should stay out of AGENTS.md. The notes agree on the conclusion even if they frame the reasoning differently.

- [Grounding] The link to instructions-are-skills-without-automatic-routing is accurately described as "defines the intermediate form between notes and skills." That note does define instructions as the form between methodology notes and skills, with the distinction being routing/discoverability rather than content quality. The attribution holds.

- [Grounding] The link to skills-derive-from-methodology-through-distillation is accurately described as "theoretical basis for promotion from reasoning artifacts to execution artifacts." That note does provide the theoretical framework for why methodology becomes skills through distillation, and this note's migration path is consistent with that framework.

- [Internal consistency] The note's three sections (decision rule, consequence, migration path) are mutually consistent. The decision rule establishes tiers, the consequence section derives AGENTS.md implications from those tiers, and the migration path describes movement between tiers. No pairwise contradictions found.

Overall: 3 warnings, 4 info
===
