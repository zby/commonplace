# Four-system baseline: operative oracles and where explanation sits

Working note, 2026-08-19. Opening position for the comparison — the per-system readings produced by running each system through the selection question of [weakly discriminated qualities tend to be underselected](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md): what is the operative oracle, what does it strongly and weakly discriminate, is explanation entered into selection, and does accepted output feed later iterations.

## The spectrum

| System | Strong (operative) oracle | Explanation's position | Feedback of accepted output |
|---|---|---|---|
| ScienceFlow | task-metric evaluator gating Stage acceptance | absent from representation — no claim or hypothesis object in retained state | accepted anchors become workspace, memory, and ESTRA's selection menu |
| Ontology draft | measurement policy over signed attestations | represented (hypothesis statement, Knowledge layer) but unscored; Knowledge marked an optional projection, not a source of truth | claims motivate new objects and procedures by design |
| Eigenius | type checking, certificate validation, optional Lean proof check | warrant formally checked; content truth, encoding fidelity, and explanatory quality weakly discriminated, with mechanized faithfulness grade-capped at Derived | committed sentences become citable Verified witnesses for later reasoning |
| Commonplace | structural validation, verdict-kind gates | declared quality goal with a weak operative oracle — reach critique is report-kind (no acceptance force), the reach audit is a manual recurring task | accepted notes become premises, links, and review baselines |

Four different strong oracles — metric, measurement policy, formal validity, structural validation — and in all four systems explanatory quality sits on the weakly discriminated side. Candidate mechanism for that regularity: hard oracles cluster on form because form is what is codifiable ([the verifiability gradient](../../notes/verifiability-gradient.md), [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md)); explanation resists codification, so a research system's accepted population enriches for form-fit unless a composite reach oracle is deliberately assembled.

## Per-system readings

**ScienceFlow** is the purest instance of the conjecture: all three conditions hold by explicit design (Stage candidates vary; the reject-capable Gate and evaluator scores decide acceptance; accepted anchors are the starting state of later iterations). The fixed decomposition puts even oracle improvement outside the loop — the agent cannot modify the evaluator oracles. The selection angle strengthens the lineage-workshop finding "a Stage verdict selects an anchor; it does not certify truth" to: the verdict is also the only selection pressure, so trajectories are predicted to enrich for evaluator fit and drift on everything unrepresented, explanatory content included.

**The ontology draft** designs the asymmetry in before any loop runs: evidence records carry metric, value, and error; well-formed claims are digest-pinned threshold statements; status derives from policy over attestations. Explanation is represented but nothing separates a better explanation from a worse one. This is the designed-in example now in the weakly-discriminated note, and the source of the schema corollary: a first-class slot in the data model, like a prominent name in the rubric, exerts no selection pressure by itself.

**Eigenius** is the contrast case because its strong oracle is formal validity rather than empirical measurement, yet the weak side is the same trio: content truth (outputs stamped `epistemic:derived` on successful execution regardless of truth), encoding fidelity ("checker-passing ≠ faithful", with the ~97% judge vs ~66% human agreement figure), and explanatory quality. Its reasoning protocol's epistemic grades are a manually loaded rubric enforced only at named boundaries. Two additions the selection angle surfaces:

1. *Route-level oracle asymmetry.* Persistence does not reveal which checks ran — program outputs skip AutoOnLoad, kernel follow-up layers skip structural validation — so the apparent oracle is stronger than the operative one on several commit routes, and committed sentences feed later reasoning via citation, compounding whatever slips through. This is asymmetry between routes into the accepted population, a variant the weakly-discriminated note does not currently name.
2. *The grade cap as a response type.* Capping mechanized faithfulness at Derived, never auto-Verified, neither strengthens the weak oracle nor ignores it — it refuses to let the weak oracle masquerade as strong.

**Commonplace** declares reach as the quality goal but its operative acceptance is structural validation plus verdict gates; the reach critique carries no acceptance force and the reach audit is manual. The predicted drift has an observed trace: the narrowing episode ([narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md)) documents repair optimizing defensibility toward analytic claims, and its proposed remedy — a warranted-contribution judgment with the same force as the gates — is the "enter explanation into the operative oracle" move stated as system design.

## Response taxonomy (candidate)

Three observed responses to the form-vs-explanation oracle asymmetry:

- **Exile** (ontology draft): keep explanation out of the kernel entirely; the acceptance machinery scores only what it can measure, and the Knowledge layer is explicitly non-authoritative.
- **Grade cap** (Eigenius): admit the weak oracle's output but bound its authority — mechanized faithfulness never reaches the top grade.
- **Declare and audit** (Commonplace): state explanation as the quality goal, review it open-endedly without acceptance force, and audit periodically.

ScienceFlow takes no response — the asymmetry is unmanaged because explanation is unrepresented. Missing from all four: a discriminating composite reach oracle wired into acceptance. Whether these three responses are stable kinds or points on a continuum (authority granted to the weak oracle: none / bounded / advisory) is open; the next system examined should be read against this question.

---

Relevant notes:

- [weakly discriminated qualities tend to be underselected](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) — rests-on: the selection conjecture all four readings apply
- [Eigenius](../../agentic-systems/eigenius.md) — evidenced-by: pinned code-grounded authority for the Eigenius reading
- [ScienceFlow ingest](../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md) — evidenced-by: pinned code-grounded authority for the ScienceFlow reading
- [the verifiability gradient](../../notes/verifiability-gradient.md) — mechanism: why hard oracles cluster on form
- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — mechanism: oracle hardening as codification applied to the objective itself
- [narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — is-evidence-for: Commonplace's observed drift under gate-shaped acceptance
- [lineage-mechanisms](../lineage-mechanisms/README.md) — see-also: the same two code-grounded systems read through the lineage angle
