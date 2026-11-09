---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OrangePro workflow: start-driven evidence analysis, bounded test generation, targeted proof, failure handling and report delivery."
run-id: AAS-2026-11-08-orangepro-mcp-4e3d3a22c7c8-01
reviewed-boundary: "039cd936e38eb7d52d0e03ded3b3168373d55d77"
---

# OrangePro workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a local `opro start` request against a checkout, following its automatic proof lane through report delivery. It was selected because one shipped driver connects graph construction, model proposals, executable tests, proof admission and a returned result. It is not a workflow reconstructed by joining independent tools. The CLI user or MCP caller initiates the request; OrangePro code owns internal stage progression. The surrounding coding agent owns any subsequent conversational planning, authorization and manual repair. This is bounded tool orchestration, not delegation to autonomous planning agents. See [RT-RTE-start-run](runtime.md#rt-rte-start-run), SRC-1: `src/local/operations.ts`, `src/local/autoProve.ts`.

All conclusions concern implementation at the frozen revision, with prompt/interface guidance distinguished from execution. No supplied trace establishes a successful run, model compliance, mutation soundness or improved tests. The account ends at local report/result delivery; a GitHub PR is a separate optional route, not a necessary final step of start. See [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery) and [boundary](boundary.md#boundary-and-evidence).

### Request, graph and model handoffs

1. **Resolve reuse before doing work.** `opStart` derives a run-key input and may return a saved result after refreshing reports. Otherwise it analyzes the checkout and persists a graph. The graph contains symbolic identities and relationships plus natural-language evidence; executable generated bodies remain distinguishable from proof certificates. Reuse therefore does not establish new generation or execution. See [RT-RTE-start-run](runtime.md#rt-rte-start-run), [RT-OBJ-graph](runtime.md#rt-obj-graph), [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests), SRC-1: `src/local/operations.ts`.
2. **Propose and admit associations.** When enabled and configured, start invokes AI link and flow generation, then invokes their apply operations itself. The model receives selected graph context and proposes associations; software revalidates staged results against allowed/current anchors. Start does not wait for a human to approve each association. These are candidate relationships, not dynamic proof. A model error becomes a warning and does not by itself stop deterministic reporting. See [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) and the start annotation below, SRC-1: `src/local/operations.ts`, `src/local/aiGraph/links.ts`, `src/local/flows/llmFlowDiscovery.ts`.
3. **Try existing tests first.** Changed scope and ranked eligible targets constrain automatic proof. Current-fingerprint Proven targets are excluded, and existing associated tests are attempted before provider-gated generation. A missing model API key alone does not prevent drafting: a configured Ollama endpoint can supply model generation without a key, and explicitly selected or opted-in deterministic mode supplies offline symbolic generation. Only when neither a usable provider configuration nor deterministic opt-in resolves does the provider gate skip automatic drafting; existing-test proof can still proceed. `noAuto`, static-only and zero proof limit can disable proof attempts. `no_ai` suppresses automatic model generation when a non-deterministic provider resolves, but does not veto explicit deterministic generation; the separate later gap-drafting phase still requires AI to be enabled. These are stage-specific controls, not evidence of a global filesystem or execution sandbox. See [RT-RTE-start-run](runtime.md#rt-rte-start-run), [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof), SRC-1: `src/local/autoProve.ts`.
4. **Generate only for remaining eligible gaps.** Code supplies selected target IDs, a bounded limit, source reader and provider to generation. For a model provider, the model proposes code from selected evidence, not the host conversation. Provider parameters and exact weights are external/unpinned; the delegated task is text generation, not arbitrary shell control. In deterministic mode a symbolic offline renderer supplies the proposed test instead; this is not a model delegation. Generic generation can return unresolved drafts rather than executable tests. See [RT-RTE-test-generation](runtime.md#rt-rte-test-generation), [RT-CMP-openai](runtime.md#rt-cmp-openai), [RT-CMP-anthropic](runtime.md#rt-cmp-anthropic), [RT-CMP-ollama](runtime.md#rt-cmp-ollama), SRC-1: `src/local/generate/generator.ts`, `src/local/generate/providers.ts`.

The selected automatic branch has an important transformation between draft and execution: it derives run hints, checks for a proof handoff, relocates relative imports, validates unresolved imports at the actual destination, rejects escaping/existing paths, and writes admitted code under `orangepro_generated/`. A draft's original `runnable === false` flag is not an unconditional veto in this branch if relocation resolves its imports. Generated Go/Java tests without this handoff are skipped here because their proof runners require tests in their own package/module; their existing-test lane remains distinct. These workflow-specific qualifications are on [RT-RTE-start-run](runtime.md#rt-rte-start-run) below. SRC-1: `src/local/autoProve.ts`.

### Verification, rejection and recovery

The automatic caller passes target symbol, source root, written test path, replacement and runner into `proveLoop`. This handoff supplies executable artifacts and bounded proof arguments, not a fresh agent with a transcript. The common dynamic gate requires a green non-timeout baseline and an assertion-failing non-timeout mutant. A caller's reported pass or static hard association cannot substitute for it. The certificate is appended to a local ledger; later RTM credit also requires the current target fingerprint. This is a software admission protocol over writable local evidence, not cryptographic attestation or a complete correctness oracle. See [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof), [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof), [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit), SRC-1: `src/local/operations.ts`, `src/local/rtm.ts`.

A concrete rejection path is an unavailable runner or red baseline. The classifier distinguishes setup/environment failures from a non-killing test; it does not mint proof. A classified project-wide blocker can suppress sibling attempts within this run. A surviving mutant remains non-killing and does not acquire that broad quarantine effect. Code owns continuation to lower-ranked candidates and return of diagnostics; fixing dependencies or authoring a stronger test is not automatically delegated to another model in this branch. The detailed route is [WF-RTE-proof-recovery](#wf-rte-proof-recovery), SRC-1: `src/local/autoProve.ts`.

An exception from automatic proof is caught by start, which records a failed-proof reason and proceeds toward deterministic artifacts. This is partial-result recovery, not transaction rollback. In particular, the generated-file write precedes the proof call, and the caught proof exception does not delete that file. See [WF-RTE-proof-recovery](#wf-rte-proof-recovery) and the start annotation, SRC-1: `src/local/autoProve.ts`, `src/local/operations.ts`.

### Delivery and remaining host work

After proof, start separately fills report-visible draft slots, writes diagnostic/report artifacts and builds RTM from the final graph and ledger. It returns a `StartResult` with proof and generation outcomes, artifact paths, gaps, changed scope, warnings and next actions. Local delivery means this return plus the artifacts that actually wrote; it does not mean every target is Proven, every draft ran, every renderer succeeded or a PR merged. Advisory write failures can be surfaced as warnings. Saving the start result for reuse is conditional on the final behavior report having been written. See [RT-RTE-start-run](runtime.md#rt-rte-start-run) annotation below, SRC-1: `src/local/operations.ts`.

The return can ask the coding agent to generate for the changed scope/top gap, write runnable tests and call the provided proof arguments. That is a continuation instruction, not evidence the host executed it. Generic host-driven generation retains the write/run/report handoff described in [RT-CLM-local-generation](runtime.md#rt-clm-local-generation); it must not erase the automatic branch's shipped writing and execution. A host may edit or reject a draft; only the proof protocol controls public Proven in the inspected credit path. No downstream host context policy or authorization guarantee follows. SRC-1: `src/local/operations.ts`, `src/local/mcp.ts`.

### Added source coverage

Beyond the supplied baseline, this member inspected SRC-1 implementation in `src/local/autoProve.ts`: `classifyProof`, the automatic driver, generated-file transformation, proof call and result aggregation; and `src/local/operations.ts`: start preflight/AI/proof exception handling, generation-provider resolution and final diagnostics/report/result construction. Correction inspection also covers SRC-1 `src/local/localConfig.ts`: provider resolution, including keyless Ollama; and `src/local/autoProve.ts`: the existing-tests-first order and subsequent provider/deterministic generation gate. These passages are implementation evidence only. Other languages' complete runners, all run-key dependencies and downstream host execution remain outside this member's inspection; no additional source or observed run is introduced.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-proof-recovery
Label: Automatic proof failure classification and continuation

Part of: [RT-RTE-start-run](runtime.md#rt-rte-start-run)

This route is the run-local failure/continuation branch within start's automatic proof pass, not another declaration of the complete start orchestration or the certificate-minting route [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof). Endpoints: returned proof outcome or caught proof exception → automatic classifier/scheduler → sibling selection or aggregate return. Code owns classification and vetoes; no human or model chooses whether a setup failure counts as proof. SRC-1: `src/local/autoProve.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Attempt classifications, setup needs, skipped reasons, generated filenames and aggregate proof counters return to start.
- Later read-back: The quarantine map is run-local; start can persist distilled attempt diagnostics for later doctor/report consumers, not for proof admission.
- Delegated visibility: The classifier sees proof record/oracle summaries and target/project context; a later skipped sibling receives a derived blocker diagnostic rather than a new model conversation.
- Selection predicate: Closed record yields proven; structured refusal/setup categories yield needs_setup; baseline failure is classified; remaining non-closed outcomes yield non_killing. Only classified project-wide blocker categories populate sibling quarantine.
- Invalidation or expiry: The shared project-block map lasts this autoProve invocation; budgets and candidate-pool exhaustion terminate continuation. Current certificate validity is separately owned by RTM.
- Activation or effect: Can suppress further runner attempts, continue lower-ranked candidates and preserve honest non-proof diagnostics. Generated files written before a failed proof call are not removed by its catch branch.
- Evidence limits: No actual failure/recovery execution is supplied; classifier labels do not establish root-cause accuracy for arbitrary customer failures or successful repair.

Mode: bounded repository proof attempts. Trigger: an automatic proof outcome or exception. Proposed change: continuation/skipping decisions, not model/prompt revision. Software can reject credit; no interactive approval occurs here. The proof protocol supplies the computational reference outcome, not a human expected-answer test. Recovery returns diagnostics or proceeds; it does not automatically repair a failing test, dependencies or retained method text.

> if (record.closed) return { classification: "proven" };
> --- `src/local/autoProve.ts`

> if (dyn.oracle.baseline?.timedOut === true) {
>   return { classification: "needs_setup", reason: dyn.oracle.reason ?? "The original code's test ran past its time limit, so nothing was measured.", category: "timeout" };
> }
> --- `src/local/autoProve.ts`

> const blockedKey = projectBlockKeys(language, projectRoot, targetFileRel).find((key) => projectBlocked.has(key));
> const blocked = blockedKey ? projectBlocked.get(blockedKey) : undefined;
> --- `src/local/autoProve.ts`

> } catch (e) {
>   attempted--;
>   skipped.push({ target_symbol, title: test.title, reason: `Proof could not run: ${redactSecrets(errMsg(e))}`, language, project_root: projectRoot });
>   continue;
> }
> --- `src/local/autoProve.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-start-run](runtime.md#rt-rte-start-run)

Workflow-specific provider/control qualification: the automatic existing-test lane precedes generation's provider gate. Credentials are not the gate's sole condition: configured Ollama requires no API key, and opted-in deterministic generation is symbolic rather than a model call. With a resolved non-deterministic provider, start's no-AI flag selects existing-only proof; explicit deterministic mode is not excluded by that flag. SRC-1: `src/local/localConfig.ts`, `src/local/autoProve.ts`, `src/local/operations.ts`. The supplied runtime record retains the deterministic resolver and start control passages.

> const base = env.OLLAMA_BASE_URL;
> if (!base && requested !== "ollama") return null;
> --- `src/local/localConfig.ts`

> const deterministic = opts.provider === "deterministic"
>   || /^(1|true|yes)$/i.test(String(deps.env.ORANGEPRO_ALLOW_DETERMINISTIC ?? ""));
> const providerConfig = deterministic ? null : resolveProviderConfig(deps.env, { provider: opts.provider, model: opts.model });
> if (!providerConfig && !deterministic) {
> --- `src/local/autoProve.ts`

Workflow-specific transformation: generated proof execution consumes relocated code, not necessarily the draft body unchanged. It also requires a proof handoff; the unsupported generated Go/Java case is explicitly skipped in this branch. A non-runnable draft is reconsidered against imports at the actual write destination. SRC-1: `src/local/autoProve.ts`.

> const body = rewriteRelativeImports(test.body, symbolFile(target_symbol), GENERATED_DIR);
> --- `src/local/autoProve.ts`

> if (test.runnable === false && unresolvedLocalImports(body, abs, sourceRoot, declaredDeps).length > 0) {
> --- `src/local/autoProve.ts`

> Go dynamic proof runs the target package's own test; a generated Go test is out of that package — proven via the existing-tests lane instead.
> --- `src/local/autoProve.ts`

Workflow-specific outer recovery: AI-link errors and automatic-proof exceptions can leave deterministic artifacts deliverable, without granting proof. Delivery is a structured return and advisory paths, not an all-or-nothing success assertion. SRC-1: `src/local/operations.ts`.

> warnings.push(`AI candidate links skipped: ${reason}`);
> --- `src/local/operations.ts`

> reason: `auto-prove failed but deterministic artifacts are ready: ${reason}`,
> --- `src/local/operations.ts`

> if (finalReportWritten) saveStartForReuse(root, reuseInput, result, deps);
> return result;
> --- `src/local/operations.ts`

The diagnostic sidecar extends failure visibility beyond this invocation, but its later reader is not the credit oracle. SRC-1: `src/local/operations.ts`.

> // G1: persist the distilled, already-redacted attempt classifications so
> // `opro doctor --proof` and standalone report regens can explain blockers
> // after this process exits. Sidecar only — never read by the oracle, RTM,
> // or ledger paths; a write failure must never fail start.
> --- `src/local/operations.ts`
