---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OrangePro epistemic routes: candidate drafting, mutation evidence, scoped proof credit and verified-patch delivery."
run-id: AAS-2026-11-08-orangepro-mcp-4e3d3a22c7c8-01
reviewed-boundary: "039cd936e38eb7d52d0e03ded3b3168373d55d77"
---

# OrangePro epistemic report

## Source-and-claim boundary

This asks what OrangePro can acquire, generate, check and license for later reliance, particularly what its public Proven tier warrants. The shipped CLI, MCP operations, agent guidance and ancillary adapters remain inside the whole-system artifact boundary. Hosted backend, model internals and enclosing agent remain outside implementation inspection; see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). All source findings below use SRC-1 at the frozen revision. HEAD was checked against that revision. No target code, tests, examples or services were executed.

Direct inspection here adds comparison scoring/judging, RTM selection, fault classification, oracle shape checking, candidate classifier limits and export replay. Supplied runtime findings remain evidence for routes not reread here; they are not represented as independent source inspection. Public warrant claims are [EPI-CLM-proof-scope](#epi-clm-proof-scope) and [EPI-CLM-judge-accuracy](#epi-clm-judge-accuracy); host-owned generation guidance is [RT-CLM-local-generation](runtime.md#rt-clm-local-generation).

| Entry point or operation | SRC-1 path | Coverage and remaining limit |
|---|---|---|
| CLI/MCP dispatch | `src/local/cli.ts`, `src/local/mcp.ts` | Direct dispatch search; CLI roast body read. Confirms extra probe, brief, verify, export-tests, coverage, recipe, agent and delivery surfaces, not just start/generate/prove. |
| Hooks/plugin distribution | `plugins/`, `.agents/`, `.claude-plugin/` | Scoped hook-text search had no matches. Not an exhaustive activation audit; no system-wide absence claim follows. |
| Start/analyze/update, generated drafts and AI links/flows | `src/local/operations.ts`, `src/local/autoProve.ts`, `src/local/generate/generator.ts`, `src/local/aiGraph/links.ts`, `src/local/flows/llmFlowDiscovery.ts` | Supplied [RT-RTE-start-run](runtime.md#rt-rte-start-run), [RT-RTE-test-generation](runtime.md#rt-rte-test-generation), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission); parser/ranker and every report mapping not independently audited. |
| Prove/prove-loop/record/roast/RTM | `src/local/operations.ts`, `src/local/rtm.ts`, `src/local/cli.ts` | Supplied [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof); direct RTM selector and roast source. Language runners/mutators not audited end-to-end: mutation soundness remains bounded. |
| Compare and jobs | `src/local/operations.ts`, `src/local/generate/compareScore.ts`, `src/local/generate/compareJudge.ts` | Direct scoring and return paths; [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare), [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring). No causal prompt-benefit experiment. |
| Probe-fault and oracle | `src/local/faultProbe.ts`, `src/local/contracts/oracle.ts` | Direct preflight/classifier/statement and complete oracle source; [EPI-RTE-fault-probe](#epi-rte-fault-probe). Container/report-signing internals not security-audited. |
| Test-brief/draft-test/verify-test | `src/local/candidateTest.ts`, `src/local/draftTest.ts` | Direct candidate classifier and limitations; supplied [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification). Semantic oracle review not established. |
| Export-tests | `src/local/exportTests.ts` | Direct lineage checks, recomputation, A–H predicates, fresh replay and receipt; [EPI-RTE-export-replay](#epi-rte-export-replay). |
| Actions/install/publish | `src/local/actionsRun.ts`, `src/local/actionsInstall.ts`, `src/local/publishTests.ts` | Supplied [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery); no live GitHub execution or adoption evidence. |
| Coverage, changed-targets, risk score/gaps/status/doctor, recipe, explain/export, agent workflow | `src/local/cli.ts`, `src/local/operations.ts`, `src/local/recipe/dbSqljs.ts`, `src/local/agentWorkflow.ts` | Dispatch identified; narrower algorithms and recipe internals not assessed here. Coverage ingestion and generated numerical claims cannot receive complete correctness assessment; prevents a system-complete negative about other derivation/evaluation routes. |
| Platform stdio/remote and QA/grounding | `src/orangeproTools.ts`, `packages/mcp-remote/src/index.ts` | Supplied [RT-RTE-platform-call](runtime.md#rt-rte-platform-call); backend content and evaluators not determinable from adapter text. |
| Infrastructure/release metadata | `infra/`, `.github/`, `docs/` | Boundary treatment retained. No observed deployment/CI evidence; not additional semantic acceptance evidence. |

Missing provider replies and execution traces prevent claims that any particular generated assertion was conjectured, checked or accepted in operation. Missing customer baseline/mutant observations prevent observed proof and benefit conclusions. Missing backend implementation prevents assessment of hosted QA warrant. Uninspected available helpers are inspection limits, not access gaps. No single system-wide absence of knowledge production, learning, reflection or improvement is inferred.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-graph](runtime.md#rt-obj-graph) | Source/doc assertions, associations and target identities | see [RT-OBJ-graph](runtime.md#rt-obj-graph) | SRC-1 `src/local/workspace.ts` | Container, not uniformly warranted knowledge; imported source warrant unknown. |
| [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests) | Assertion expectations and scenarios; executable structure also has non-propositional operational use | see [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests) | SRC-1 `src/local/generate/generator.ts` | A runnable test is still a candidate. |
| [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof) | Baseline/mutant conditions and credited target | see [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof) | SRC-1 `src/local/operations.ts` | Predicate facts are not authenticated run history. |
| [EPI-OBJ-oracle](#epi-obj-oracle) | Intended observable behavior and expected value | see [EPI-OBJ-oracle](#epi-obj-oracle) | SRC-1 `src/local/contracts/oracle.ts` | Natural language basis and approval assertions remain externally warranted. |
| [EPI-OBJ-fault-evidence](#epi-obj-fault-evidence) | Witness difference, test outcomes and scoped caught/missed classification | see [EPI-OBJ-fault-evidence](#epi-obj-fault-evidence) | SRC-1 `src/local/faultProbe.ts` | Supplied observations absent. |
| [EPI-OBJ-comparison-scores](#epi-obj-comparison-scores) | Quality estimates and exact syntactic counts, separated by evaluator below | see [EPI-OBJ-comparison-scores](#epi-obj-comparison-scores) | SRC-1 `src/local/generate/compareScore.ts` | Scores do not establish test truth. |
| [EPI-OBJ-verification-receipt](#epi-obj-verification-receipt) | Patch lineage and A–H test/fault/revision claims | see [EPI-OBJ-verification-receipt](#epi-obj-verification-receipt) | SRC-1 `src/local/exportTests.ts` | Artifact-only, not deployed/adopted. |
| [RT-CMP-openai](runtime.md#rt-cmp-openai), [RT-CMP-anthropic](runtime.md#rt-cmp-anthropic), [RT-CMP-ollama](runtime.md#rt-cmp-ollama) | Opaque distributed-parametric provider state | see cited components | SRC-1 `src/local/generate/providers.ts` | No exact weight pin or inspected parameter-update route; internal knowledge not individuable. |
| [RT-RTE-platform-call](runtime.md#rt-rte-platform-call) | not determinable: no backend reply instances supplied | see [RT-RTE-platform-call](runtime.md#rt-rte-platform-call) | SRC-1 `src/orangeproTools.ts` | No local graph identity should be inferred for hosted state. |

## Authority-route ledger

Architectural status below concerns source wiring, never observed operation. Each cited record owns its endpoints, timing details, selection, retention and limits; `see` references those fields instead of reproducing them. Separate rows distinguish checking, disposition, retention and consequential use even when one implementation spans them.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | content transformation | implemented | [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests) | truth-apt transformation: indeterminate | Test assertions' expected behavior | Selected graph/source context and model; semantic fidelity not proved | Drafting request | Proposed tests or fallback | Candidate generation only | No semantic correctness license | Draft available for host/automatic use | see [RT-BAP-generation-prompt](runtime.md#rt-bap-generation-prompt) | SRC-1 `src/local/generate/generator.ts` | none | none | Unresolved entailment versus conjecture; provider internals and replies unavailable |
| [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | check/evidence production | implemented | [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests) | no content change | Draft structure, grounding IDs, executability hints | Parser/reference/body checks; Go check is package build/start, not assertion truth | After generation | Runnable/non-runnable and warnings | see [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | References exist; not that assertions are correct | Filters run hints | see [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | SRC-1 `src/local/generate/generator.ts` | none | none | Go compilation is not a test correctness oracle |
| [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | disposition/acceptance | implemented | [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests) | no content change | Draft admission for later writing/running | Software structure checks; host may separately edit/reject | After checks | Retained candidate, not public Proven | see [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | No evidence-consuming acceptance of expected-behavior truth established | Runnable hints and candidate availability | see [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | SRC-1 `src/local/operations.ts` | none | none | Admission is operational, not semantic endorsement |
| [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | retention | implemented | [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests) | no content change | Draft/run metadata | Fresh-test append and fingerprint pin eligibility | Generate and later calls | Saved/reused code | see [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | Verbatim reuse does not add warrant | Avoids regeneration while eligible | see [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) | SRC-1 `src/local/operations.ts` | none | none | Not lifecycle integration of accepted knowledge |
| [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | content transformation | implemented | [RT-OBJ-graph](runtime.md#rt-obj-graph) | truth-apt transformation: indeterminate | Candidate relevance/flow proposals | Model given shortlisted anchors | AI-link/flow generation | Weak candidate associations | see [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | Semantic relevance remains a proposal | Stages suggestions | see [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | SRC-1 `src/local/aiGraph/links.ts` | none | none | Neither entailment nor non-entailment established for arbitrary replies |
| [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | disposition/acceptance | implemented | [RT-OBJ-graph](runtime.md#rt-obj-graph) | no content change | Current identity and structure of proposals | Code revalidation; standalone caller can withhold apply; start applies automatically | Apply or start | Reject or candidate lane | see [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | Identity/structure only, no proof credit | Weak generation context and worklists | see [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | SRC-1 `src/local/flows/llmFlowDiscovery.ts` | none | none | Candidate retention is not acceptance of relevance as true |
| [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) | check/evidence production | implemented | [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof) | truth-apt transformation: acquisition/import | One test's response to one target mutation | Baseline/mutant runner and assertion classifier; supported language route | Explicit/automatic proof | Oracle success/failure/unrunnable | see [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) | Source warrant unknown for unsupplied customer execution; intended narrow test/mutant contrast | Produces evidence for mint gate | see [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) | SRC-1 `src/local/operations.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | Runner correctness not audited; survival may reflect an equivalent mutant |
| [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) | disposition/acceptance | implemented | [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof) | no content change | Public proof eligibility | Green baseline plus non-timeout assertion-failing mutant; target checks | After oracle | Closed dynamic certificate or unproven | see [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) | Protocol acceptance for specified target/test/mutation, not general correctness | Mint ledger credit; record_run cannot substitute | see [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit) | SRC-1 `src/local/operations.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | No run supplied; local ledger writable |
| [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) | retention | implemented | [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof) | no content change | Certificate and attempts | Ledger append | After outcome | Durable diagnostics/certificates | see [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) | Retention itself adds no warrant | Later RTM and auto-prove access | see [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit) | SRC-1 `src/local/operations.ts` | none | none | Failure retention does not necessarily revoke older success |
| [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) | operational admission/selection/consumption | implemented | [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof) | no content change | Current public tier and skip eligibility | RTM valid closed certificate plus current fingerprint, best-ever matching success | Later report/start | Proven tier or fallback | see [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit) | Current target fingerprint, not revalidation of environment/test correctness | Reports and future proof selection | see [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit) | SRC-1 `src/local/rtm.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | Later failed attempt does not demote an older matching proof |
| [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) | check/evidence production | implemented | [EPI-OBJ-comparison-scores](#epi-obj-comparison-scores) | truth-apt transformation: indeterminate | Suite quality, imports and domain fit | Same configured provider as judge; metadata-conditioned quality domain, not test execution | Real-provider comparison after both arms | Four bounded scores and rationale | see [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) | Metadata-conditioned opinion/proxy; no truth oracle | Scores displayed, not installed policy | see [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) | SRC-1 `src/local/generate/compareJudge.ts` | [EPI-CLM-judge-accuracy](#epi-clm-judge-accuracy) | none | Numeric parsing does not establish accuracy; graph-name context incomplete |
| [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) | content transformation | implemented | [EPI-OBJ-comparison-scores](#epi-obj-comparison-scores) | truth-apt transformation: entailed derivation | Syntactic assertion counts, reference counts and deterministic proxy scores | Fixed regex/token matching and formulas; domain is code strings and graph metadata | Deterministic provider or failed judge, with metrics always computed | Exact computed counts and bounded numeric proxies | see [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) | Entailed numerical results given input strings, not correctness/completeness of tested behavior | Returned comparison view only | see [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) | SRC-1 `src/local/generate/compareScore.ts` | [EPI-CLM-judge-accuracy](#epi-clm-judge-accuracy) | none | Concrete deduction below; no semantic truth follows from a regex match |
| [EPI-RTE-fault-probe](#epi-rte-fault-probe) | check/evidence production | implemented | [EPI-OBJ-fault-evidence](#epi-obj-fault-evidence) | truth-apt transformation: acquisition/import | Specified fault changes witness output and is caught/missed by selected tests | Repeated original witness, mutant witness, matched test identities, optional full suite | Probe fault | Stage observations and witness difference | see [EPI-RTE-fault-probe](#epi-rte-fault-probe) | Run observations imported; supplied oracle truth remains unknown | Inputs for classifier/brief | see [EPI-RTE-fault-probe](#epi-rte-fault-probe) | SRC-1 `src/local/faultProbe.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | Difference is not checked against the oracle expected value by this classifier |
| [EPI-RTE-fault-probe](#epi-rte-fault-probe) | disposition/acceptance | implemented | [EPI-OBJ-fault-evidence](#epi-obj-fault-evidence) | truth-apt transformation: entailed derivation | Caught/survived classification and scope | Fixed classifier over recorded stage predicates | After stages | Blocked, inconclusive, invalid_mutation, caught_by_existing, survived_unverified | see [EPI-RTE-fault-probe](#epi-rte-fault-probe) | Conditional classification in the program's domain, not that a production defect exists | Retained classification enables downstream brief route | see [EPI-RTE-fault-probe](#epi-rte-fault-probe) | SRC-1 `src/local/faultProbe.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | Full-suite label requires additional checks; no observed stages supplied |
| [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) | check/evidence production | implemented | [EPI-OBJ-oracle](#epi-obj-oracle) | no content change | Candidate catches fault at declared assertion and survives controls | Repeated originals/faults, full suite, restoration, text controls | Verify-test or draft repair | Candidate outcome | see [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) | Behavioral contrast, not semantic assertion-to-oracle agreement | Supplies repair/stop/export decision | see [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) | SRC-1 `src/local/candidateTest.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | Reporter process and alias/mutation-aware evasion limits explicit |
| [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) | disposition/acceptance | implemented | [EPI-OBJ-oracle](#epi-obj-oracle) | no content change | Candidate for export/repair | Code classifier, not an independent semantic reviewer | After checks | verified_gap or rejection/inconclusive/stop | see [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) | Operational acceptance for narrowly tested fault; expected-value review remains external | Bounded repair or export eligibility | see [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) | SRC-1 `src/local/candidateTest.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | Doctrinal human-approved oracle is not authenticated by shape validation |
| [EPI-RTE-export-replay](#epi-rte-export-replay) | check/evidence production | implemented | [EPI-OBJ-verification-receipt](#epi-obj-verification-receipt) | truth-apt transformation: acquisition/import | Exported patch reproduces verified behavior on fresh copies | Manifest, bytes, git-apply equivalence, recomputation, fresh replay A–H | Export-tests | Evidence rows and replay observations | see [EPI-RTE-export-replay](#epi-rte-export-replay) | Lineage checked and new observations requested; external run warrant unobserved | Eligibility for receipt/publication | see [EPI-RTE-export-replay](#epi-rte-export-replay) | SRC-1 `src/local/exportTests.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | Hash agreement is not source truth or tamper-proof provenance |
| [EPI-RTE-export-replay](#epi-rte-export-replay) | disposition/acceptance | implemented | [EPI-OBJ-verification-receipt](#epi-obj-verification-receipt) | truth-apt transformation: entailed derivation | Receipt classification | No boundary failure and every proof row met | After replay | verified_gap / inconclusive / blocked; not_delivered | see [EPI-RTE-export-replay](#epi-rte-export-replay) | Checked narrow test/fault/revision predicates only | Publication may proceed through separate gate | see [EPI-RTE-export-replay](#epi-rte-export-replay) | SRC-1 `src/local/exportTests.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | No automatic merge or general-correctness acceptance |
| [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery) | lifecycle integration | implemented | [EPI-OBJ-verification-receipt](#epi-obj-verification-receipt) | no content change | Verified patch into delivery workflow | Receipt/base/branch checks and yes confirmation | Publish request after export | Draft PR, not merged test | see [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery) | Scoped artifact acceptance precedes delivery; no new semantic warrant | Confirmed branch/PR creation; adoption external | see [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery) | SRC-1 `src/local/publishTests.ts` | [EPI-CLM-proof-scope](#epi-clm-proof-scope) | none | Only delivery integration is wired; installed knowledge or deployed test benefit not established |
| [RT-RTE-platform-call](runtime.md#rt-rte-platform-call) | content transformation | implemented | not determinable — backend reply | truth-apt transformation: acquisition/import | Backend QA/grounding responses, not local graph content | Hosted API; internals opaque | Host tool request | Backend text/data | see [RT-RTE-platform-call](runtime.md#rt-rte-platform-call) | Source warrant unknown | Returns to host; reliance delegated | see [RT-RTE-platform-call](runtime.md#rt-rte-platform-call) | SRC-1 `src/orangeproTools.ts` | none | none | Platform truth-apt object cannot be individuated without replies |

The platform row names no local graph object: backend truth-apt content and epistemic authority are not determinable without reply instances or backend implementation. No local graph retention is asserted for it.

Deterministic transformation witness: [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) distinguishes exact lexical computation from quality interpretation. With one test whose body is `expect(1).toBe(1)`, no grounding refs, no imports, no graph tokens and no weak-evidence flag, the regex counts one assertion. `scoreArm` gives completeness 33, context awareness 0, accuracy 0 and domain specificity 0; `armMetrics` gives one test, assertion average 1, trace refs 0, weak disclosure 0 and smoke-only 0. These are deductions from inspected implementation, not target execution. The assertion does not test a repository behavior. Thus the count is warranted in its syntactic domain, while a numerical completeness claim about actual behavior remains a proxy. [EPI-OBJ-comparison-scores](#epi-obj-comparison-scores) retains the formula passage.

Countercase to automatic withdrawal: direct RTM selection retains the newest valid proof matching the current fingerprint even if a newer attempt failed. That is selective reliance on historical success, not latest-result acceptance. Countercase to “no checking”: dynamic proof, candidate controls and export replay are substantial code checks; none should be collapsed into model plausibility. Countercase to “a verified assertion expresses the oracle”: candidateTest explicitly reserves semantic agreement for review. See [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof), [EPI-RTE-export-replay](#epi-rte-export-replay) and [EPI-OBJ-oracle](#epi-obj-oracle).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-proof-scope](#epi-clm-proof-scope) | see [EPI-CLM-proof-scope](#epi-clm-proof-scope) | SRC-1 `README.md`, `src/local/exportTests.ts`; doctrine/design | Narrow test/fault/revision wording; source also warns equivalent mutants survive | [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof), [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification), [EPI-RTE-fault-probe](#epi-rte-fault-probe), [EPI-RTE-export-replay](#epi-rte-export-replay) | None supplied | Source protocols, not independently varied empirical intervention; mutation/report validity bounds inference | Implemented scoped test-sensitivity evaluation and public credit | Broad “wasn't protecting” wording exceeds one-mutation contrast; no general correctness license |
| [EPI-CLM-judge-accuracy](#epi-clm-judge-accuracy) | see [EPI-CLM-judge-accuracy](#epi-clm-judge-accuracy) | SRC-1 `src/local/generate/compareScore.ts`; doctrine/design comment | Accuracy described as authoritative judge dimension | [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) | None supplied | Same provider, metadata-conditioned model judgment; fallback lexical heuristics; no execution criterion | Implemented comparative opinion/proxy scores | Not authoritative semantic correctness evidence; no causal KG-benefit attribution |
| [RT-CLM-local-generation](runtime.md#rt-clm-local-generation) | see [RT-CLM-local-generation](runtime.md#rt-clm-local-generation) | SRC-1 `src/local/mcp.ts`; doctrine/design | Host writes/runs returned code | [RT-RTE-test-generation](runtime.md#rt-rte-test-generation), [RT-RTE-start-run](runtime.md#rt-rte-start-run), [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare) | None supplied | Static source reachability, not observed execution | Guidance is path-specific | Automatic write/prove and Go package start qualify universal wording |

## Bounded conclusion

OrangePro distinguishes candidate availability from public proof credit. Graph-grounded drafting imports selected source content with unknown source warrant and asks a model for assertions; reference validation licenses identity, not expected-value truth. Structural admission, storage and fingerprint reuse do not establish acceptance of a produced ampliative claim. Without actual replies or a proof of non-entailment, the content relation of model-produced assertions and relevance proposals remains indeterminate. See [RT-RTE-test-generation](runtime.md#rt-rte-test-generation) and [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission).

The proof route has an explicit criterion, intended use and operational consumer: baseline passes and a specified mutant fails at an assertion without timeout; certificate predicates and current fingerprint license public tier/skip selection. This is acceptance of narrow test sensitivity under the runner contract, not a theory of correctness. A later failed attempt does not necessarily withdraw an earlier current proof. Test/environment drift beyond the checked fingerprint is not thereby resolved. See [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof), [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit) and SRC-1 `src/local/rtm.ts`.

The separate fault lane checks witness difference and scopes missed/caught findings to the selected tests or adequately checked whole suite. Candidate verification adds repeatability, declared assertion position, restored copies and text controls. Export recomputes prior verification, checks byte lineage and replays the patch on fresh copies before constructing its receipt. These are independent evaluators with narrower licenses than “correct test” or “production-safe code.” The oracle's expected value is acquired, not independently established, and semantic assertion agreement remains a review obligation. See [EPI-RTE-fault-probe](#epi-rte-fault-probe), [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) and [EPI-RTE-export-replay](#epi-rte-export-replay).

Verified patches have a delivery path, not demonstrated adoption: separate publication can create a draft PR, while merging belongs outside the target. Generic generated tests have retention and operational use before epistemic acceptance; that is not lifecycle integration of accepted knowledge. Comparison scores change the displayed assessment, not automatically the deployed prompt/provider policy. No observed learning gain follows. Provider parameters are not updated by inspected calls; opaque service processing cannot be used to infer absence or presence of internal reflection. No formulated-theory criticism-and-retention loop or exercised self-improvement is established by these inspected paths, and unassessed included operations prevent a system-wide negative. See [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery), [EPI-RTE-comparison-scoring](#epi-rte-comparison-scoring) and the provider components.

## Shared records

### Operative objects

#### EPI-OBJ-oracle
Label: Oracle expected behavior

Natural-language behavior, expected value, excluded inputs, basis notes and witness input live in symbolic `oracle.json` fields. Approval metadata is symbolic; prose is interpreted by people/models. This differs from [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof): an expected-behavior premise, not a measured baseline/mutant certificate; no supplied object counterpart. SRC-1 `src/local/contracts/oracle.ts`, `src/local/candidateTest.ts`.

The checker accepts proposed or approved status; an approved record must name by/at/where, but those fields do not authenticate a person or validate the basis. Semantic agreement of the candidate assertion remains outside the implemented verification license.

> if (approval.status !== "proposed" && approval.status !== "approved") return fail("approval.status must be proposed or approved.");
> --- `src/local/contracts/oracle.ts`

> "Whether the declared assertion checks the oracle's expected value is not checked by the tool; it rests on review of the test."
> --- `src/local/candidateTest.ts`

#### EPI-OBJ-fault-evidence
Label: Fault stage observations and classification

Symbolic JSON stage records, witness outputs, classification and stage references under `.orangepro/proof-runs/`; generated prose statements present them to readers. Distinct from [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof): fault-probe classification is not the dynamic certificate. [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) consumes this prior fault run but does not declare its object. SRC-1 `src/local/faultProbe.ts`.

> writeFileAtomic(join(runDir, "classification.json"), recordBytes(classification));
> --- `src/local/faultProbe.ts`

> if (same) return result("inconclusive", "no_behavioral_difference", { behavioral_difference: difference });
> --- `src/local/faultProbe.ts`

#### EPI-OBJ-comparison-scores
Label: Comparison dimensions and matrix

Symbolic numeric fields plus optional natural-language rationale in comparison return/report JSON/Markdown. Distinct from [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests): assessments of tests, not code bodies. This is the score-producing part of [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare), not a duplicate route-level finding. SRC-1 `src/local/generate/compareScore.ts`, `src/local/operations.ts`.

Exact syntactic metrics and quality-proxy dimensions have different warrants. The concrete witness in the ledger follows these formulas; normalized graph token matching is not correctness evaluation.

> const assertions = (body.match(CONCRETE_ASSERTION) || []).length;
> --- `src/local/generate/compareScore.ts`

> completeness: pct(0.6 * Math.min(1, assertionsAvg / 3) + 0.4 * Math.min(1, a.n / 3)),
> context_awareness: pct(a.groundedCount / a.n),
> accuracy: pct(Math.max(0, a.realApiCount / a.n - 0.5 * Math.min(1, inventedAvg / 2))),
> domain_specificity: pct(a.domainCount / a.n)
> --- `src/local/generate/compareScore.ts`

#### EPI-OBJ-verification-receipt
Label: Export verification receipt

Symbolic JSON receipt with A–H predicates, stage references, patch hashes and generation/adoption/delivery states, alongside a human-facing HTML summary and additive patch. Filesystem substrate is an export proof-run folder. Distinct from [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof): export receipt for a verified new test patch, not RTM public Proven certificate. It supplies the export material within [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery). SRC-1 `src/local/exportTests.ts`.

> fault: blocked ? "blocked" : firstUnmet ? "inconclusive" : "verified_gap",
> reason: blocked ? (checkoutAfter ? "boundary_or_container" : "checkout_modified") : firstUnmet ? `row_${firstUnmet.row}_not_met` : null,
> generation: "generated",
> adoption: "not_delivered",
> delivery: "artifact_only"
> --- `src/local/exportTests.ts`

### Routes

#### EPI-RTE-comparison-scoring
Label: Comparison quality scoring

Part of: [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare)

The scoring subroute takes the two generated suites and graph-derived context, requests holistic scores from the same configured provider, or uses lexical scoring on null/failure/deterministic provider. Owner is `opCompare`; it returns scores/matrix/rationale to report consumers without installing a prompt winner. This part isolates evaluator scope from the containing generation/job route. SRC-1 `src/local/operations.ts`, `src/local/generate/compareJudge.ts`, `src/local/generate/compareScore.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Both suites, dimensions, matrix and optional rationale, with scoring_method.
- Later read-back: Comparison reports may be read after the call; no automatic learned policy consumer established.
- Delegated visibility: Judge receives behavior/acceptance metadata, grounded references, a capped sample of names and both test bodies.
- Selection predicate: Real provider and any generated tests request judge; null result falls back to heuristic.
- Invalidation or expiry: Fresh comparison overwrites the report, per [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare); no retained winner policy.
- Activation or effect: Displayed assessment only; reliable accuracy or downstream user compliance is unobserved.
- Evidence limits: No independent expected-answer oracle or supplied run; repeated model labels do not prove correctness.

Mode is bounded comparative evaluation. Code selects scoring path, model proposes quality estimates, numeric parser accepts/coerces fields and may fall back. Human comparison is outside this route. It admits no production machinery, knowledge premise or provider change.

> const judged =
>   provider.providerName !== "deterministic" && haveTests
> --- `src/local/operations.ts`

> const raw = await provider.complete({ system: JUDGE_SYSTEM, user, temperature: 0 });
> return parseJudgeResponse(raw);
> --- `src/local/generate/compareJudge.ts`

> if (!o.baseline && !o.grounded) return null;
> --- `src/local/generate/compareJudge.ts`

#### EPI-RTE-fault-probe
Label: Fault observation and scope classification

Caller supplies exact target record, fault, oracle, witness and fixture; `opProbeFault` checks identities, plans the fault, executes selected stages and classifies observations. Code owns preflight and classifier; caller selects the experimental problem, not the outcome. Distinct upstream route absent from the supplied route inventory: [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification) starts from its fault run, while [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) mints a different certificate. No supersession is needed. SRC-1 `src/local/faultProbe.ts`, `src/local/contracts/oracle.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Fault record and scoped classification with caught_by, witness difference and reasons.
- Later read-back: Persisted proof-run classifications, oracle, witness and stage references feed brief/verify/export.
- Delegated visibility: Witness and selected tests execute on prepared copies with fixture/container inputs; no host conversation.
- Selection predicate: Exact supported TS/JS target/fault binding, matching oracle target hash and witness bytes; full-suite widening needs recorded baseline and identity/count checks.
- Invalidation or expiry: Preflight rejects stale/mismatched target/fixture/witness; no general elapsed-time expiry established.
- Activation or effect: Classification is retained for downstream workflow; no observed test sensitivity or benefit supplied.
- Evidence limits: Run/report origin and Docker enforcement not independently established; witness difference is not a check of oracle truth.

Mode is a bounded fault experiment. Caller supplies oracle premises (doctrine expects person-written approval); code checks shape and identity, not the person's authority. Classifier can withhold a finding. Rejected/missing stages produce blocked/inconclusive results; temporary copies are removed in finally, not retained as adopted changes. No live policy update occurs.

> if (sha256Hex(opts.witness_bytes) !== oracle.witness.sha256) throw new ProbeFaultRefusal("witness_mismatch", "the witness script is not the one the oracle names (sha256 differs).");
> --- `src/local/faultProbe.ts`

> if (caught.length > 0) return result("caught_by_existing", null, { scope: "selected", caught_by: caught, behavioral_difference: difference });
> --- `src/local/faultProbe.ts`

> if (!input.full_suite_requested) return survived(null);
> --- `src/local/faultProbe.ts`

> if (ff.failed > 0 || fullFault!.exit_code !== 0 || ff.passed !== input.baseline_passing) return survived("full_suite_inconclusive");
> return result("survived_unverified", null, { scope: "full_suite", behavioral_difference: difference });
> --- `src/local/faultProbe.ts`

#### EPI-RTE-export-replay
Label: Verified patch replay and receipt

Part of: [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery)

Export-tests isolates the receipt-producing stage of the supplied delivery chain: verify/fault/brief runs → manifest and checkout checks → additive patch and git equivalence → recomputed candidate result → fresh replay → A–H receipt → publisher input. It is also callable directly from CLI; containment names the stage referent, not a restriction to Actions. Code owns checks and classification; caller chooses the run, not the verdict. SRC-1 `src/local/exportTests.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Export run directory and receipt, or refusal.
- Later read-back: Receipt/patch/manifests drive separate publisher and reports; adoption is explicitly not_delivered.
- Delegated visibility: Fresh copied trees run fixture Mocha suite through container stage runner; patch bytes enter both copies.
- Selection predicate: Verified gap input, unchanged commit/target/test, allowed additive patch giving verified bytes, matching recomputed verdict, and all A–H predicates for verified receipt.
- Invalidation or expiry: Changed manifests/checkout/patch refuse export; fresh replay can downgrade to inconclusive or blocked.
- Activation or effect: Writes export artifacts and requests replay; does not merge tests or grant general correctness.
- Evidence limits: No replay or publication observed; semantic expected-value review and same-process reporter limits remain.
 
Mode is bounded replay, not new test generation. Prior producer proposes the test; software can veto stale or invalid lineage and withhold verified status. Publication has a separate confirmation and code gate, [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery). Temporary copies are cleaned in finally; selected refusals remove the nascent export run, while terminal receipts retain scoped failures. Rollback of external adoption is outside this route.

> if (recomputed !== verify.verdict.result) refuse("run_invalid", `the verify run's result (${verify.verdict.result}) does not follow from its own stage files (${recomputed}).`);
> --- `src/local/exportTests.ts`

> if (parsed.path !== testPath || !ours.bytes.equals(verifiedTest) || !byGit || !byGit.equals(verifiedTest)) refuse("patch_invalid", "the exported patch does not give the verified bytes, by OrangePro's reading or by git's.");
> --- `src/local/exportTests.ts`

> if (!go("fresh_full_suite_with_patch", "original", fullArgv)) return;
> if (!go("fresh_fault_full_suite_with_patch", "mutant", fullArgv)) return;
> --- `src/local/exportTests.ts`

> } finally {
>   rmSync(tmp, { recursive: true, force: true });
> }
> --- `src/local/exportTests.ts:442-444`

### Claims

#### EPI-CLM-proof-scope
Label: Proof of test protection

README says breaking a target and observing test failure distinguishes protection from mere execution. Its negative implication must be qualified by mutation equivalence and target/input scope. Export limitations explicitly bound proof to one test/fault/revision and distinguish generated, verified and adopted. This is distinct from [RT-CLM-local-generation](runtime.md#rt-clm-local-generation), which concerns executor ownership. SRC-1 `README.md`, `src/local/exportTests.ts`, `src/local/cli.ts`; doctrine/design.

> For a test you care about, it breaks the function in an isolated copy and checks that the test fails.
> --- `README.md`

> If the test still passes, it wasn't protecting that function.
> --- `README.md`

> "Proven means one named test caught one specified fault at its declared assertion on one revision. It is not general correctness or production safety.",
> --- `src/local/exportTests.ts`

> out("Equivalent mutants can also survive, so treat this as a proof-strengthening queue, not automatic blame.");
> --- `src/local/cli.ts`

#### EPI-CLM-judge-accuracy
Label: Authoritative accuracy judgment

The comparison scoring comment assigns authoritative hallucination judgment to Accuracy. That is doctrine, not observed reliable evaluation; inspected judge context, score coercion and lexical fallback support only bounded opinions/proxies. Distinct from [RT-CLM-local-generation](runtime.md#rt-clm-local-generation); nearest route is [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare). SRC-1 `src/local/generate/compareScore.ts`, `src/local/generate/compareJudge.ts`.

> * own imports; sanitization redacts lines) and the Accuracy dimension already judges
> * hallucination authoritatively.
> --- `src/local/generate/compareScore.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
