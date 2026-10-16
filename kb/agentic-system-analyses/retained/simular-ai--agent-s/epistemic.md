---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Agent S epistemic routes: desktop evidence, experience admission, coding reports and offline comparative judgment."
run-id: AAS-2026-10-16-agent-s-db6fee212353-01
reviewed-boundary: "15776a8dc659658b1963816ea006f7af1978e595"
---

# Agent S epistemic report

## Source-and-claim boundary

This asks which routes turn observations or retained experience into content fit for reliance, and what checks actually license. Scope and exclusions are **see [boundary](boundary.md#boundary-and-evidence)**; sources and evidence layers are **see [Source register](boundary.md#source-register)**. SRC-1 supplies implementation, doctrine/design and reported operation, not observed runs or causal experiments. The report distinguishes installed S3, historical experience paths and offline selection. A route existing in one does not establish its presence in the others.

The consequential claims are [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification), [EPI-CLM-knowledge-bank](#epi-clm-knowledge-bank), [EPI-CLM-fact-accuracy](#epi-clm-fact-accuracy) and [EPI-CLM-bbon-performance](#epi-clm-bbon-performance). None establishes a system-wide knowledge-production guarantee.

| Entry point or operation | Source path in SRC-1 | Coverage and supporting records |
|---|---|---|
| Installed command dispatch and terminal handling | `setup.py`; `gui_agents/s3/cli_app.py` | Direct source reads; see [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop). Both failure and completion enter the completion-dialog branch. |
| Advertised actions and formatting | `gui_agents/s3/memory/procedural_memory.py`; `gui_agents/s3/utils/formatters.py`; `gui_agents/s3/utils/common_utils.py` | Direct reads of introspection, formatters, parsing and eval; see [RT-RTE-action-check](runtime.md#rt-rte-action-check). Advertised methods are not a capability restriction. No separate hook registry is established by these paths. |
| Worker reflection and text-buffer writes/read-back | `gui_agents/s3/agents/worker.py`; `gui_agents/s3/agents/grounding.py` | Direct reads; [EPI-RTE-trajectory-reflection](#epi-rte-trajectory-reflection), [EPI-RTE-notes-buffer](#epi-rte-notes-buffer). The buffer is materially distinct from persistent historical JSON. |
| Grounding, OCR cleanup and text-span selection | `gui_agents/s3/agents/grounding.py` | Direct reads of coordinate generation and OCR/text alignment; [EPI-RTE-text-grounding](#epi-rte-text-grounding). Other GUI methods enumerated by search; their application-specific effects are not individually audited. |
| Coding feedback, summary and downstream verification | `gui_agents/s3/agents/code_agent.py`; `gui_agents/s3/agents/worker.py` | Summary construction directly read; controller loop supplied by [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation); [EPI-OBJ-code-summary](#epi-obj-code-summary). |
| S1/S2 hierarchy, experience and bootstrap | `gui_agents/s1/core/AgentS.py`; `gui_agents/s2/agents/agent_s.py`; `gui_agents/utils.py` | S2 updater directly read; S1 updater and historical exposed methods searched. Remaining retrieval/caller chain is supplied by [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience) and [RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap). S1 platform-specific observation transformations and S2/S2.5 grounding internals are not independently assessed here; no exhaustive historical epistemic negative follows. |
| S2.5 alternate worker and provider/model state | `gui_agents/s2_5/agents/agent_s.py`; `gui_agents/s3/core/engine.py` | Supplied runtime findings, not independent full reads; see [RT-CMP-lmm-agent](runtime.md#rt-cmp-lmm-agent), [RT-CMP-grounding-model](runtime.md#rt-cmp-grounding-model), [RT-CMP-embedding-engine](runtime.md#rt-cmp-embedding-engine). |
| OSWorld execution/evaluation and OpenClaw bridge | `osworld_setup/s3/lib_run_single.py`; `integrations/openclaw/agent_s_wrapper.py` | Supplied [RT-RTE-osworld-driver](runtime.md#rt-rte-osworld-driver) and [RT-RTE-openclaw-bridge](runtime.md#rt-rte-openclaw-bridge). No direct reassessment of external evaluator semantics. |
| Caption generation, cleanup, selection and later scoring | `gui_agents/s3/bbon/behavior_narrator.py`; `gui_agents/s3/bbon/comparative_judge.py`; `osworld_setup/s3/bbon/generate_facts.py`; `osworld_setup/s3/bbon/utils.py`; `osworld_setup/s3/bbon/run_judge.py` | Narrator/judge and save/load portions directly read; other caller/scoring findings supplied by [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection). |
| Public benefit claim | `README.md` | Direct read; [EPI-CLM-bbon-performance](#epi-clm-bbon-performance). Hosted Sai claims remain outside functional scope. |

Missing execution traces prevent identifying actual generated propositions, compliance, accepted comparison instances and later effects. Missing release bundles prevent assessing initial knowledge truth and lineage. Missing external evaluator definitions prevent determining precisely what benchmark success certifies. Missing provider internals/weights prevent assessing parametric knowledge, internal checking or training. Missing controlled comparisons prevent component-level or transfer attribution. Available but uninspected historical transformations are a coverage limit, not an access gap or evidence of absence. These limits allow route-specific conclusions, not a system-complete negative.

## Epistemic-object inventory

Properties owned by declarations are **see** the cited record. Candidate contents below identify the assessed truth domain rather than assert that a particular output occurred.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory) | Primarily instructions, not truth claims | see record | see record | Policy compliance is not established. |
| [EPI-OBJ-screen-evidence](#epi-obj-screen-evidence) | Screen state, displayed text and target locations | see record | SRC-1: `gui_agents/s3/agents/grounding.py` | Displayed text need not be true of the world. |
| [EPI-OBJ-ocr-table](#epi-obj-ocr-table) | Recognized words and bounding boxes | see record | SRC-1: `gui_agents/s3/agents/grounding.py` | Cleanup can delete numerical content; OCR accuracy unknown. |
| [EPI-OBJ-trajectory-reflection](#epi-obj-trajectory-reflection) | Progress, loops, completion and failure explanations | see record | SRC-1: `gui_agents/s3/agents/worker.py` | Candidate assessments, not verified outcomes. |
| [EPI-OBJ-notes](#epi-obj-notes) | Arbitrary model-supplied notes; truth-aptness depends on instance | see record | SRC-1: `gui_agents/s3/agents/grounding.py` | No supplied instance; not determinable for individual notes. |
| [EPI-OBJ-code-summary](#epi-obj-code-summary) | What code attempted and what resulted | see record | SRC-1: `gui_agents/s3/agents/code_agent.py` | Summarizer does not receive controller outputs directly. |
| [EPI-OBJ-experience-summary](#epi-obj-experience-summary) | Task/subtask observations and procedural advice | see record | SRC-1: `gui_agents/s2/agents/agent_s.py` | No captured generated entry or downloaded bundle. |
| [EPI-OBJ-fact-caption](#epi-obj-fact-caption) | Screenshot differences or the agent's terminal indication | see record | SRC-1: `gui_agents/s3/bbon/behavior_narrator.py` | A fact label supplies no truth certification. |
| [EPI-OBJ-judge-choice](#epi-obj-judge-choice) | Which supplied rollout better meets a request | see record | SRC-1: `gui_agents/s3/bbon/comparative_judge.py` | Index is symbolic; its task-fit interpretation is model judgment. |

## Authority-route ledger

Each row isolates a consequential function. Repeated route citations identify the same implementation container, not additional declarations. `see` delegates generic route identity, timing and mechanics to that record; the epistemic assessments remain local. All architectural statuses below describe implementation, not observed operation. No row asserts an observed accepted ampliative claim.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop) | content transformation | implemented | [EPI-OBJ-screen-evidence](#epi-obj-screen-evidence) | truth-apt transformation: acquisition/import | Desktop display enters model context | Screenshot producer; display domain, source warrant unknown | see route | Possible visible-state evidence | Input supply, not endorsement | Supports interpretation of rendered state, not application/backend truth | Provides basis for next action | see route | see route | none | none | No captured observation or calibrated accuracy. |
| [EPI-RTE-text-grounding](#epi-rte-text-grounding) | content transformation | implemented | [EPI-OBJ-ocr-table](#epi-obj-ocr-table) | truth-apt transformation: indeterminate | Image/OCR words become cleaned table | OCR plus regex; lexical screen domain | see route | Recognized text may be altered or omitted | Input to text-span model | Unknown OCR warrant; cleaning degrades numerical fidelity | Alters target evidence | see route | see route | none | none | Neither semantic preservation nor entailment established for general inputs. |
| [EPI-RTE-text-grounding](#epi-rte-text-grounding) | operational admission/selection/consumption | implemented | [EPI-OBJ-ocr-table](#epi-obj-ocr-table) | no content change | Phrase maps to word ID and geometry | Text-span model, then digit extraction/indexing | see route | Word coordinates or indexing error; default ID zero if no digits | Permissive target selection | No independent license that chosen word matches phrase | Supplies highlight endpoint | see route | see route | none | none | Geometry calculation does not validate semantic alignment. |
| [EPI-RTE-trajectory-reflection](#epi-rte-trajectory-reflection) | check/evidence production | implemented | [EPI-OBJ-trajectory-reflection](#epi-obj-trajectory-reflection) | truth-apt transformation: indeterminate | Task progress, repeated failure or completion | Reflector model, task and visible trajectory | see route | Continue/change-course/completion assessment | Advisory | Candidate judgment of visible task progress | Can influence next worker action | see route | see route | none | none | Could reshape evidence or add conjecture; actual output needed to distinguish. |
| [EPI-RTE-trajectory-reflection](#epi-rte-trajectory-reflection) | operational admission/selection/consumption | implemented | [EPI-OBJ-trajectory-reflection](#epi-obj-trajectory-reflection) | no content change | Reflection enters generator message | Nonempty result condition; worker interprets | see route | Reflection delivered | Advisory, not veto | Delivery licenses no additional factual reliance | Worker may revise or continue | see route | see route | none | none | No independent acceptance check or observed changed behavior. |
| [RT-RTE-action-check](runtime.md#rt-rte-action-check) | check/evidence production | implemented | [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory) | no content change | Action response format and trial evaluability | Regex and live eval; response strings/Python execution | see route | Formatting feedback or trial value | Feedback retries; effects may already occur | Only regex/evaluation result, not action safety or task correctness | Reproposal can occur; effects are not rolled back | see route | see route | none | none | Trial success is not a pure proof. |
| [RT-RTE-action-check](runtime.md#rt-rte-action-check) | disposition/acceptance | implemented | [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory) | no content change | Action returned after retry loop | Empty feedback or exhausted attempts | see route | Last response proceeds to conversion | Best-effort admission, not fail-closed | No epistemic acceptance of screenshot analysis or success claim | Can permit action despite format failure | see route | see route | none | none | Domain is executable proposal admission only. |
| [EPI-RTE-notes-buffer](#epi-rte-notes-buffer) | retention | implemented | [EPI-OBJ-notes](#epi-obj-notes) | no content change | Supplied strings appended | Model proposes; list extension admits without truth test | see route | In-memory notes | Automatic retention | No factual acceptance criterion | Later worker can use text | see route | see route | [EPI-CLM-knowledge-bank](#epi-clm-knowledge-bank) | Task-local bank, not durable knowledge certification | No independent endorsement, expiry or content revision in this method. |
| [EPI-RTE-notes-buffer](#epi-rte-notes-buffer) | operational admission/selection/consumption | implemented | [EPI-OBJ-notes](#epi-obj-notes) | truth-apt transformation: non-ampliative reshaping | Notes joined into message text | Deterministic join; worker interprets result | see route | Current Text Buffer rendered | Advisory context supply | Formatting does not increase warrant | Notes may guide copying/actions | see route | see route | [EPI-CLM-knowledge-bank](#epi-clm-knowledge-bank) | none | Delimiters do not preserve individual-string boundaries unambiguously. |
| [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation) | check/evidence production | implemented | [EPI-OBJ-code-summary](#epi-obj-code-summary) | truth-apt transformation: acquisition/import | Controller status/stdout/stderr enters coding context | Controller reports process execution; source warrant unknown | see route | Execution feedback for coding continuation | Feedback to model | Exit status supports process-level judgment, not task success | Further scripts may be revised/executed | see route | see route | [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification) | none | External controller semantics and actual results unavailable. |
| [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation) | content transformation | implemented | [EPI-OBJ-code-summary](#epi-obj-code-summary) | truth-apt transformation: indeterminate | Action/thought history becomes result summary | Fresh model; summary guidance requests factual results | see route | Summary or failure string | Advisory report | No checked derivation of execution outcomes | Next worker gets report/action history | see [RT-BAP-code-return](runtime.md#rt-bap-code-return) | SRC-1: `gui_agents/s3/agents/code_agent.py` | [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification) | Outcome evidence omitted at summary boundary | Actual outputs needed to classify reshaping versus conjecture. |
| [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop) | disposition/acceptance | implemented | [EPI-OBJ-screen-evidence](#epi-obj-screen-evidence) | no content change | Final task-completion indication | Model belief; sentinel handling in CLI | see route | DONE or FAIL stops loop | Enforcing termination | No implemented postcondition licensing complete task correctness | Stops acting; both branches display completion | see route | SRC-1: `gui_agents/s3/cli_app.py` | [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification) | Required verification is policy, not gate | GUI evidence could support a model judgment; no actual decision supplied. |
| [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience) | content transformation | implemented | [EPI-OBJ-experience-summary](#epi-obj-experience-summary) | truth-apt transformation: indeterminate | Trajectory becomes reusable summary | Summary model and guidance | see route | Narrative/episodic text | Candidate production | Not established as faithful compression or warranted generalization | Supplies later retained guidance | see route | see route | none | none | No instance supports entailment or non-entailment classification. |
| [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience) | retention | implemented | [EPI-OBJ-experience-summary](#epi-obj-experience-summary) | no content change | Candidate enters JSON under new key | Key-existence rule; not factual evaluation | see route | New value stored or old value reused | Enforcing append/reuse rule | Retention is not evidence-consuming acceptance | Makes future retrieval possible | see route | see route | none | none | No content-specific withdrawal or repair demonstrated by updater. |
| [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience) | operational admission/selection/consumption | implemented | [EPI-OBJ-experience-summary](#epi-obj-experience-summary) | no content change | Retrieved guidance enters planning/worker context | Similarity selection, then model interpretation | see route | Prompt guidance delivered | Ranking then advisory | Similarity licenses relevance ranking, not truth | May alter planning/action proposals | see route | see route | none | none | Delivery is not activated use or demonstrated learning. |
| [RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap) | operational admission/selection/consumption | implemented | [EPI-OBJ-experience-summary](#epi-obj-experience-summary) | truth-apt transformation: acquisition/import | Release asset admitted to historical loaders | HTTP/ZIP success; transport/format domain | see route | Extracted initial stores | Permissive content admission | Imported content; source warrant unknown | Available to historical retrieval | see route | see route | none | none | Bundle contents and authorship lineage not frozen. |
| [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection) | content transformation | implemented | [EPI-OBJ-fact-caption](#epi-obj-fact-caption) | truth-apt transformation: indeterminate | Before/action/after become description | Narrator model; visible change domain | see route | Fact-caption text | Candidate production | Interpretation, not certified facts or causal attribution | Later judge receives answer portion | see route | see route | [EPI-CLM-fact-accuracy](#epi-clm-fact-accuracy) | Fact status exceeds demonstrated validation | Fixed terminal descriptions are narrower signal reports, not success assertions. |
| [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection) | retention | implemented | [EPI-OBJ-fact-caption](#epi-obj-fact-caption) | no content change | Narrator result saved | Nonexception result; tag formatter is only structural best effort | see route | JSONL contains successful return values | Automatic persistence | No semantic acceptance | Captions become later judge evidence | see route | see route | [EPI-CLM-fact-accuracy](#epi-clm-fact-accuracy) | none | Exception omission is not correction of false captions. |
| [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection) | check/evidence production | implemented | [EPI-OBJ-judge-choice](#epi-obj-judge-choice) | truth-apt transformation: indeterminate | Relative task satisfaction of supplied rollouts | Model compares task, captions, available endpoint images | see route | Choice plus rationale | Comparative recommendation | Evidence-consuming comparative evaluation for selecting a rollout, not proof of task success | Produces candidate selection | see route | see route | [EPI-CLM-bbon-performance](#epi-clm-bbon-performance) | none | No expected-answer oracle inside judge messages; incomplete views limit assessment. |
| [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection) | disposition/acceptance | implemented | [EPI-OBJ-judge-choice](#epi-obj-judge-choice) | no content change | Model comparison converted to selected directory | Integer parsing and range; finite supplied candidates | see route | Directory or None | Enforcing selection rule | Bounds chosen index, not correctness of its rationale | Records selection for scoring/reporting | see route | see route | [EPI-CLM-bbon-performance](#epi-clm-bbon-performance) | none | Implemented task-fit acceptance path, no observed accepted claim instance. |
| [RT-RTE-osworld-driver](runtime.md#rt-rte-osworld-driver) | check/evidence production | implemented | [EPI-OBJ-screen-evidence](#epi-obj-screen-evidence) | truth-apt transformation: acquisition/import | External task evaluator result | env.evaluate; evaluator target/criteria uninspected beyond task score | see route | Score in result.txt | Reporting; later variance filtering/scoring | Only external score under unknown criteria | Changes offline task subset and comparison statistics | see [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection) | see route | [EPI-CLM-bbon-performance](#epi-clm-bbon-performance) | none | No visible correctness/transfer license from a score alone. |
| [RT-RTE-openclaw-bridge](runtime.md#rt-rte-openclaw-bridge) | disposition/acceptance | implemented | [EPI-OBJ-screen-evidence](#epi-obj-screen-evidence) | no content change | Child process status | Return-code check; process completion domain | see route | Wrapper success/error status | Status reporting to caller | Success means exit zero, not task satisfaction | Host may consume status; host behavior excluded | see route | see route | none | none | Broader success interpretation would exceed evaluator domain. |

No lifecycle-integration row is asserted: the inspected JSON and caption writes demonstrate retention/use, not integration after a demonstrated accepted knowledge claim. This is bounded to the traced stores and consumers, not a negative about all historical or opaque routes. Coordinate rescaling is deterministic arithmetic conditional on its inputs; it cannot warrant that those inputs identify the intended element. No route here establishes entailed world knowledge from warranted premises.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification) | see record | see record | see [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory) | [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation), [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop) | Unavailable | No supplied test of compliance or effect | GUI verification is requested; terminal method does not enforce it | Cannot promote instruction to guarantee. |
| [EPI-CLM-knowledge-bank](#epi-clm-knowledge-bank) | see record | see record | see record | [EPI-RTE-notes-buffer](#epi-rte-notes-buffer) | Unavailable | No observed reuse benefit | Strings can be retained and delivered within ACI lifetime | “Long-term” does not establish disk persistence or epistemic acceptance. |
| [EPI-CLM-fact-accuracy](#epi-clm-fact-accuracy) | see record | see record | see record | [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection) | Unavailable | No independent caption validation; before/after contrast alone does not identify action causality | Evidence-conditioned caption generation and downstream reliance are wired | Accurate-facts premise is stronger than implemented checks. |
| [EPI-CLM-bbon-performance](#epi-clm-bbon-performance) | see record | see record | see record | [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection), [RT-RTE-osworld-driver](runtime.md#rt-rte-osworld-driver) | Reported figures only, not inspected runs | No frozen trial allocation, evaluator definitions or independent component intervention | Implemented offline comparison is consistent with the reported method | Magnitude, human comparison, transfer and component benefit remain unverified. |

## Bounded conclusion

Agent S has several consequential epistemic routes, not one common oracle. Desktop observations and controller feedback supply evidence for model decisions. Their scope differs: rendered state and process results do not independently certify application truth or task completion. OCR is an especially concrete lineage limit: its cleanup can remove a purely numerical token before the text-span model sees the table, as [EPI-RTE-text-grounding](#epi-rte-text-grounding) establishes. Geometric derivation remains conditional on unvalidated recognition and selection.

Reflection is a model-mediated feedback channel about the system's own trajectory, with a wired return to action choice, **see [EPI-RTE-trajectory-reflection](#epi-rte-trajectory-reflection)**. It supports an architectural self-representation/feedback path; actual accurate criticism, changed reliance and benefit are unobserved. Formatting checks have operative consequences but a narrower domain: they test a string pattern and evaluability, can already cause effects, and do not enforce outcome correctness, **see [RT-RTE-action-check](runtime.md#rt-rte-action-check)**. Reflection and autonomous action choice do not by themselves establish theory building or learning.

Notes and historical summaries obtain later behavioral influence without demonstrated epistemic acceptance. Notes use an in-memory append/render path; historical summaries use persistent key-based admission and retrieval, **see [EPI-RTE-notes-buffer](#epi-rte-notes-buffer)** and **[RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience)**. Imported bundles have unknown content warrant. Summary semantics cannot be classified as entailed or ampliative without actual content and premises. Source wiring establishes retention and potential later reliance, not exercised learning, improved capacity or successful self-improvement. For historical experience, retained instructions can enter behavior-determining organization; the missing subsequent-operation dependence and objective-linked comparisons prevent attributing exercised beneficial self-change.

The coding path consumes execution feedback internally, but its returned summary is generated from selected action/thought history rather than direct controller outcomes, **see [EPI-OBJ-code-summary](#epi-obj-code-summary)**. Subsequent GUI checking could improve warrant; it is requested policy, not a postcondition on termination. Failure markers and wrapper process success must not be recast as verified task completion.

Offline judging is a genuine implemented evidence-consuming comparative procedure with a named intended use and criterion: choose a supplied completed rollout that better satisfies the request and judge guidelines for scoring/reporting, **see [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection)**. The model supplies the substantive evaluation; the integer/range rule permits or rejects the directory selection. Its operational horizon is saved comparison and reporting, not live action replay or policy installation. Caption retention is separate from this selection decision. Passing parsing checks does not accept each caption as true. Actual accepted comparison content, selection accuracy and causal performance improvement remain unobserved. Public benchmark figures are attributed reports, not independently established evidence.

Parametric components remain externally hosted and uninspected; their client fixity limits are **see [RT-CMP-lmm-agent](runtime.md#rt-cmp-lmm-agent)**, **[RT-CMP-grounding-model](runtime.md#rt-cmp-grounding-model)** and **[RT-CMP-embedding-engine](runtime.md#rt-cmp-embedding-engine)**. Lack of visible training calls is not a system-wide no-learning conclusion. No inspected instance establishes a localized explanatory theory with content-directed criticism and retained iterative revision; the existing progress judgments and rankings must not be promoted to those independent conditions. Uninspected historical paths and unavailable model processing also prevent an exhaustive absence verdict.

## Shared records

### Operative objects

#### EPI-OBJ-screen-evidence
Label: Screenshot and grounding evidence

Part of: [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

This object is an evidence-bearing part of the runtime route, not a duplicate of that enclosing route. Source-native identity: observation `screenshot`, passed to worker and `OSWorldACI` grounding contexts. Image bytes reside in process dictionaries/model messages; rendered content is interpreted by models, while returned digit coordinates are symbolic inputs to geometry. Candidate truths concern visible UI state and target location. SRC-1, implementation: `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/grounding.py`.

> self.grounding_model.add_message(
>             text_content=prompt, image_content=obs["screenshot"], put_text_last=True
>         )
> --- `gui_agents/s3/agents/grounding.py`

> numericals = re.findall(r"\d+", response)
>         assert len(numericals) >= 2
>         return [int(numericals[0]), int(numericals[1])]
> --- `gui_agents/s3/agents/grounding.py`

These checks establish parseable digits, not their correspondence to the requested target. Screenshots provide display evidence, not endorsement of every displayed assertion.

#### EPI-OBJ-ocr-table
Label: OCR text table and element geometry

Part of: [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

Distinct material part: `get_ocr_elements` returns natural-language recognized words in a symbolic ID table and a Python element list containing bounding-box fields; both are in process memory. Unlike the screen image, the cleaned table has lost some original lexical information. Evidence and concrete transformation are in [EPI-RTE-text-grounding](#epi-rte-text-grounding), SRC-1 implementation at `gui_agents/s3/agents/grounding.py`. This part belongs to the desktop route, not a second declaration of the full route.

#### EPI-OBJ-trajectory-reflection
Label: Worker trajectory reflection

Part of: [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

Source-native identity: `reflection`, `reflection_thoughts`, and `self.reflections` in Worker. Natural-language assessments reside in process strings/lists and generator messages; reset replaces worker context. Distinct from shipped procedural instructions [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory): these are generated progress assessments. SRC-1 implementation/doctrine at `gui_agents/s3/agents/worker.py`, `gui_agents/s3/memory/procedural_memory.py`; evidence is retained in [EPI-RTE-trajectory-reflection](#epi-rte-trajectory-reflection).

#### EPI-OBJ-notes
Label: ACI notes

Part of: [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

Source-native identity: `OSWorldACI.notes`, written by `save_to_knowledge` and rendered as Current Text Buffer. Python list in ACI memory; strings are interpreted as natural-language content by the worker. Not the static policy or historical JSON store. It can hold quoted text, facts, or instructions; individual truth-aptness is not determinable without entries. SRC-1 implementation: `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/agents/worker.py`; passages in [EPI-RTE-notes-buffer](#epi-rte-notes-buffer).

#### EPI-OBJ-code-summary
Label: Code execution summary

Part of: [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation)

Source-native identity: `_generate_summary` output returned under `summary`. Natural-language string in a result dictionary and next worker message; this is the report part of a larger coding route. Action history and controller feedback are distinct evidence streams. Summary construction selects step number, thoughts and action, not execution result dictionaries. SRC-1 implementation: `gui_agents/s3/agents/code_agent.py`; downstream consumer see [RT-BAP-code-return](runtime.md#rt-bap-code-return).

> for step in execution_history:
>             step_num = step["step"]
>             thoughts = step.get("thoughts", "")
>             action = step.get("action", "")
> --- `gui_agents/s3/agents/code_agent.py`

> if thoughts:
>                 execution_context += f"Thoughts: {thoughts}\n"
>             execution_context += f"Code: {action}\n"
> --- `gui_agents/s3/agents/code_agent.py`

The prompt asks for actual outputs, but this input supplies only narrated thoughts and proposed code. Thoughts may themselves mention prior results; this is not direct receipt or verification of those results. Without generated content, faithful reshaping versus added outcome conjecture is indeterminate. Runtime's omission warning is supported, not superseded.

#### EPI-OBJ-experience-summary
Label: Historical experience summaries

Part of: [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience)

The content-bearing part of the historical route, not its retrieval mechanism. Source-native S2 identities: narrative and episodic values in `narrative_memory.json` and `episodic_memory.json`. Natural-language task/subtask summaries and guidance, held in filesystem JSON and later model prompts. Grouped here only under the shared new-key admission rule; narrative and episodic consumers remain separate in the enclosing record. No actual value is frozen. The default bundles in [RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap) are another possible provenance, not proof that any particular generated entry came from a bundle. SRC-1 implementation: `gui_agents/s2/agents/agent_s.py`.

> if subtask_key not in kb.keys():
>                     subtask_summarization = self.planner.summarize_episode(
>                         subtask_trajectory
>                     )
>                     kb[subtask_key] = subtask_summarization
>                 else:
>                     subtask_summarization = kb[subtask_key]
> --- `gui_agents/s2/agents/agent_s.py`

> with open(subtask_path, "w") as fout:
>                     json.dump(kb, fout, indent=2)
> --- `gui_agents/s2/agents/agent_s.py`

Narrative evidence and later-use passage are see [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience). Admission does not test the factual summary or establish whether procedural advice is warranted beyond its originating task.

#### EPI-OBJ-fact-caption
Label: Fact captions

Part of: [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection)

Distinct content part of the offline route: `fact_answer` and `fact_thoughts`, natural-language descriptions stored in filesystem JSONL with screenshot metadata. The later judge receives answer strings only; rationale retention does not establish rationale consumption. SRC-1 implementation: `gui_agents/s3/bbon/behavior_narrator.py`, `osworld_setup/s3/bbon/generate_facts.py`, `osworld_setup/s3/bbon/utils.py`.

> if "fact_answer" in data:
>                     fact_captions.append(data["fact_answer"])
> --- `osworld_setup/s3/bbon/utils.py`

> if isinstance(result, Exception):
>             print(f"Error generating fact caption for step {i+1}: {result}")
>             continue
>         successful_results.append(result)
> --- `osworld_setup/s3/bbon/generate_facts.py`

> if successful_results:
>         with open(fact_captions_file, "w") as f:
>             for result in successful_results:
>                 f.write(json.dumps(result) + "\n")
> --- `osworld_setup/s3/bbon/generate_facts.py`

The prose output is evidence-conditioned but not semantically checked by these write branches. There is a material countercase to treating all captions as outcome conjectures: exact `DONE` returns a fixed report of the agent's indication, not of actual completion.

> if pyautogui_action == "DONE":
>             return {
>                 "fact_thoughts": "The agent has indicated that it is done with the task.",
>                 "fact_answer": "The agent has indicated that it is done with the task.",
>             }
> --- `gui_agents/s3/bbon/behavior_narrator.py`

For concrete input `pyautogui_action="DONE"`, the inspected branch returns those literal fields without image interpretation. This is a deterministic report about an input signal, not evidence that the task succeeded. For ordinary actions, captions might preserve visible facts or add interpretations; the unseen output prevents deciding the relation.

#### EPI-OBJ-judge-choice
Label: Comparative answer and selected trajectory

Part of: [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection)

Source-native identities: comparative `answer`, `thoughts`, `selected_trajectory`. Natural-language rationale and model answer become a symbolic integer/directory selection, retained by the caller in JSON for scoring. Unlike captions, the object assesses relative task fit under explicit guidelines. SRC-1 implementation: `gui_agents/s3/bbon/comparative_judge.py`; criterion doctrine at `gui_agents/s3/memory/procedural_memory.py`.

> The agent is always expected to complete the task; key constraints take precedence over these guidelines which act as tie breakers.
> --- `gui_agents/s3/memory/procedural_memory.py`

The judgment receives the task, answer captions and available initial/final screenshot pairs, not every raw observation, controller result or external expected answer. The enclosing record retains the integer/range passage. The criterion gives a bounded implemented evaluation/selection route; it does not establish actual correct acceptance or acceptance of each constituent factual premise.

### Routes

#### EPI-RTE-trajectory-reflection
Label: Trajectory reflection feedback

Part of: [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

Material feedback subroute, not a replacement of the desktop loop. Worker owns invocation and delivery; reflector proposes assessment; worker model decides subsequent action without a reflector veto. Open-request task mode; no expected-answer oracle. Enabled reflection seeds task/initial screenshot on turn zero and thereafter sends the previous worker response plus current screenshot to the reflector. Text history can remain when old images are removed; context policy see the parent. SRC-1 implementation: `gui_agents/s3/agents/worker.py`; doctrine/design: `gui_agents/s3/memory/procedural_memory.py`.

- Immediate return: Reflection text and thoughts, or None before a reflection call/when disabled.
- Later read-back: inapplicable — ordinary current-run feedback; no durable reflection store in this subroute.
- Delegated visibility: Reflector sees task, previous plan/action response and screenshots in its retained context, not independent task-success evidence or complete coding results.
- Selection predicate: Reflection enabled and turn count above zero; nonempty reflection added to generator message.
- Invalidation or expiry: Worker reset discards reflection state; image/turn flushing constrains visible history.
- Activation or effect: Advisory assessment can influence generator choice; delivered text is not observed compliance.
- Evidence limits: No reflection instance, actual failure diagnosis, changed behavior or benefit supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Case 3. You believe the current task has been completed. In this case, tell the agent that the task has been successfully completed.
> --- `gui_agents/s3/memory/procedural_memory.py`

> reflection, reflection_thoughts = split_thinking_response(
>                     full_reflection
>                 )
>                 self.reflections.append(reflection)
> --- `gui_agents/s3/agents/worker.py`

> if reflection:
>             generator_message += f"REFLECTION: You may use this reflection on the previous action and overall trajectory:\n{reflection}\n"
> --- `gui_agents/s3/agents/worker.py`

The check target is task progress within visible trajectory, not truth of a general explanatory theory. The prompt permits causal-sounding failure explanations, but a generated criticism and its blame/revision chain are not supplied. Thus theory-builder conditions 1–4 are independently unestablished for explanatory theories here, not inferred absent from model opacity. Task reflection has a wired self-representation and return path; exercised learning and improved capacity remain uninspected.

#### EPI-RTE-notes-buffer
Label: Knowledge buffer append and delivery

Part of: [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

A material retention/delivery subroute: model-generated `save_to_knowledge(text)` appends strings to ACI notes, then later worker invocation renders them. Model proposes content, list extension admits; no per-note human approval or truth veto. Open task execution, no oracle. This is distinct from the parent's ordinary message history and from historical filesystem experience. SRC-1 implementation: `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/agents/worker.py`.

- Immediate return: WAIT sentinel after notes are extended.
- Later read-back: Next worker invocation joins all current notes into Current Text Buffer in the user message.
- Delegated visibility: Generator receives joined text; original screenshot/source links are not structurally required for each note.
- Selection predicate: Model invokes exposed method; renderer supplies all notes without relevance ranking.
- Invalidation or expiry: ACI lifetime bounds the list; the method contains no content expiry, revision or withdrawal. Worker reset alone does not establish ACI clearing; see parent.
- Activation or effect: Advisory text may affect later copying/action selection; append can occur during formatter evaluation and again on worker evaluation.
- Evidence limits: No actual entries, fidelity, successful reuse or cross-session persistence supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.notes.extend(text)
>         return """WAIT"""
> --- `gui_agents/s3/agents/grounding.py`

> generator_message += (
>             f"\nCurrent Text Buffer = [{','.join(self.grounding_agent.notes)}]\n"
>         )
> --- `gui_agents/s3/agents/worker.py`

A concrete deterministic render: notes `["a,b", "c"]` and `["a", "b,c"]` both produce the same inner text `a,b,c`. The join reshapes strings without semantic validation and loses unambiguous item boundaries. The inspected implementation, not target execution, supports this deduction. No factual acceptance, rollback or source-provenance requirement is implemented by this method; arbitrary Python outside it remains outside this narrow negative.

#### EPI-RTE-text-grounding
Label: OCR cleanup and phrase grounding

Part of: [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

The text-target subroute, distinct from direct visual referring-expression grounding. `get_ocr_elements` calls OCR, cleans tokens and constructs word IDs/geometry; `generate_text_coords` gives phrase/table/screenshot to a separate model, extracts an ID and computes edge/center coordinates. Software owns cleanup and geometry; model proposes word identity; indexing supplies no semantic veto. Open-request phrase alignment, no expected-answer oracle. SRC-1 implementation: `gui_agents/s3/agents/grounding.py`.

- Immediate return: Table and OCR elements internally, then phrase-aligned coordinates or error.
- Later read-back: inapplicable — table and coordinates are current-action state, not retained content for another invocation.
- Delegated visibility: Text-span model receives phrase, cleaned table, alignment instruction and screenshot; not raw OCR output before cleanup.
- Selection predicate: Last digit sequence from model response selects element; no digits defaults to zero. Start/end alignment selects corresponding bounding-box edge.
- Invalidation or expiry: Text-span model resets on each request; observation refresh replaces current screen evidence.
- Activation or effect: Returned coordinates determine text highlighting endpoints; errors propagate toward action conversion fallback.
- Evidence limits: OCR/provider accuracy, actual phrase choices and resulting GUI effects unobserved; no entailment of correct alignment from index parsing.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> image_data["text"][i] = re.sub(
>                 r"^[^a-zA-Z\s.,!?;:\-\+]+|[^a-zA-Z\s.,!?;:\-\+]+$", "", word
>             )
> --- `gui_agents/s3/agents/grounding.py`

> if image_data["text"][i]:
>                 grouping_map[block_num].append(image_data["text"][i])
> --- `gui_agents/s3/agents/grounding.py`

For concrete OCR token `2026`, the leading disallowed-character run consumes all four digits, leaving an empty string; the conditional omits it from the table/elements. Token `123abc456` becomes `abc`. These are implementation-layer deductions through the inspected regex and branch, not executed observations. Hence cleanup is not universally meaning-preserving, even if OCR itself were perfect; the remaining screenshot input is a countervailing source of evidence, not a restoration of omitted table text.

> if len(numericals) > 0:
>             text_id = int(numericals[-1])
>         else:
>             text_id = 0
>         elem = ocr_elements[text_id]
> --- `gui_agents/s3/agents/grounding.py`

A missing numeral therefore need not reject selection; it can pick the first element. A well-formed numeral can still select the wrong phrase. Geometric arithmetic licenses only coordinates relative to the selected box. Runtime's broader grounding account remains valid; these are added epistemic subroutes, not a supersession.

### Claims

#### EPI-CLM-knowledge-bank
Label: Task knowledge bank

Source-native claimed role: `save_to_knowledge` describes a long-term bank for task reuse. This is a claim about the notes subroute, not a duplicate of [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory). SRC-1 doctrine/design: `gui_agents/s3/agents/grounding.py`.

> Save facts, elements, texts, etc. to a long-term knowledge bank for reuse during this task. Can be used for copy-pasting text, saving elements, etc.
> --- `gui_agents/s3/agents/grounding.py`

The task-reuse clause bounds the claim; it should not be read as cross-session durability. Implementation and authority see [EPI-RTE-notes-buffer](#epi-rte-notes-buffer).

#### EPI-CLM-fact-accuracy
Label: Accurate fact captions

Source-native claimed warrant: comparative prompt treats captioned facts as accurate and directs reliance on them. Unlike [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification), this is an offline judge premise, not GUI-worker verification policy. SRC-1 doctrine/design: `gui_agents/s3/memory/procedural_memory.py`.

> - You **must** refer to final_screenshot to understand what has changed from initial_screenshot to final_screenshot. These facts are accurate; **Do not assume what has changed or likely changed.**
>     - You can cite facts during reasoning, e.g., Fact 2, Facts 1-2, but **must** refer to fact captions for accurate changes.
> --- `gui_agents/s3/memory/procedural_memory.py`

There is genuine contrary evidence to a simple “unchecked text only” characterization: narrator guidance requests before/after evidence and warns against assuming action success.

> - Note that even if the action is expected to cause a change, it may have not. Never assume that the action was successful without clear evidence in the screenshots.
> --- `gui_agents/s3/memory/procedural_memory.py`

That request and the judge's endpoint images supply evidence-conditioned criticism opportunities. They do not guarantee caption fidelity, identify action causality, or implement per-caption acceptance. Saving and later loading are see [EPI-OBJ-fact-caption](#epi-obj-fact-caption); comparative model selection is see [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection).

#### EPI-CLM-bbon-performance
Label: Behavior Best-of-N benchmark gain

Claimed operation/result: adding Behavior Best-of-N raises reported OSWorld performance and exceeds a reported human baseline. No supplied runtime claim has this referent; [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection) is its closest mechanism, not a duplicate claim. SRC-1 reported operation: `README.md`.

> On OSWorld, Agent S3 alone reaches 66% in the 100-step setting, already exceeding the previous state of the art of 63.4% (GTA1 w/ GPT-5). With the addition of Behavior Best-of-N, performance climbs even higher to 72.6%, *surpassing* human-level performance on OSWorld (~72%)!
> --- `README.md`

This is attributed evidence, not a frozen causal experiment. The claim concerns task outcomes and selection, not production of accepted explanatory knowledge. No independent variation or raw trials establish that captioning, judgment or another component caused the reported difference.
