---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OrangePro runtime baseline: local evidence-to-test orchestration, proof admission, durable jobs and platform adapters at the frozen revision."
run-id: AAS-2026-11-08-orangepro-mcp-4e3d3a22c7c8-01
reviewed-boundary: "039cd936e38eb7d52d0e03ded3b3168373d55d77"
---

# OrangePro runtime report

## Runtime account

OrangePro supplies tools to a coding agent, but also ships its own bounded orchestration. Its ordinary local `start` invocation builds evidence, optionally proposes and applies AI associations, attempts proof with existing or generated tests, fills draft slots and emits reports. The coding host owns the surrounding conversation and authorization; OrangePro code owns these internal next steps. This distinction matters: the host-driven write/run workflow is not the only executor. See [RT-RTE-start-run](#rt-rte-start-run), [RT-RTE-test-generation](#rt-rte-test-generation) and [RT-RTE-targeted-proof](#rt-rte-targeted-proof). SRC-1: `src/local/operations.ts`, `src/local/mcp.ts`, `src/local/autoProve.ts`.

### Entry paths and ordinary progression

The package's `opro` and `orangepro-local` binaries resolve to `dist/local/cli.js`; CLI `mcp` starts the local stdio MCP server. CLI commands and local MCP callbacks share `op*` operations. A distinct source entry, `src/index.ts`, starts platform stdio tools, and the Cloudflare worker serves platform tools over stateless `/mcp` HTTP. Neither platform adapter supplies the enclosing hosted agents' implementation. SRC-1: `package.json`, `src/local/cli.ts`, `src/local/mcp.ts`, `src/index.ts`, `src/server.ts`, `packages/mcp-remote/src/index.ts`; [RT-RTE-platform-call](#rt-rte-platform-call).

For an ordinary `opro start <checkout>`, the principal is the invoking CLI user or tool caller. Workspace location and graph IDs identify the corpus; symbol IDs identify credited targets; model names identify configured services, not immutable weights. `opStart` first checks a saved run key. A successful reuse returns prior results with refreshed reports rather than running analysis again. Otherwise `opAnalyze` scans source/docs, builds a deterministic graph, preserves eligible generated artifacts and candidate flows, and saves graph state. Optional coverage generation precedes analysis. With provider configuration, start stages and applies weak links and candidate flows. It then computes changed scope, invokes automatic proof, drafts priority gaps, saves diagnostics, writes coverage views and RTM, and returns summaries and agent next actions. It does not run an unbounded conversational agent loop. SRC-1: `src/local/operations.ts`; [RT-RTE-start-run](#rt-rte-start-run), [RT-RTE-candidate-admission](#rt-rte-candidate-admission).

The proof pass first tries existing associated tests without requiring a model key. Its generation lane requires either configured model service access or an opted-in offline deterministic stand-in; credentials are not required for that stand-in. Generated proof tests can be written to `orangepro_generated/` and executed through `opProveLoop`; a separate draft-filling phase persists proposed tests in the graph without necessarily running them. Default prompt strategy therefore depends on the consumer: direct generation defaults to v2, while start's gap-drafting phase selects v5 for real models unless overridden. Terminal output includes honest blockers, non-runnable drafts and shortfalls, not only successful tests. SRC-1: `src/local/autoProve.ts`, `src/local/operations.ts`, `src/local/generate/generator.ts`.

### Selected forcing routes and guarantees

Four forcing comparisons establish the limits of the ordinary account:

1. **Credentials / no AI / no auto.** Missing credentials do not exclude generation: a configured local model service or the opted-in deterministic stand-in can supply it. Without a resolved model provider or deterministic opt-in, automatic proof still tries existing tests but skips its generation lane. `no_ai` disables start's AI links, flows and separate gap-draft filling; for automatic proof it sets `existingOnly` only when a non-deterministic generation provider resolves. CLI accepts `--no-ai --provider deterministic`, so automatic proof can still generate offline tests subject to static-only, budgets and eligible targets. This is supported-input reachability, not an observed run or evidence of useful tests. `noAuto` disables automatic proof (including its offline generation) and gap drafting, not the earlier AI association passes. These controls are stage-specific, not global read-only authorization. SRC-1: `src/local/operations.ts`, `src/local/autoProve.ts`; [RT-RTE-start-run](#rt-rte-start-run).
2. **Single generation versus comparison and background execution.** Single generation carries static-only into the generator. Comparison constructs a narrower shared options object and does not forward static-only; the Go compile helper consumes only the explicit boolean. Both comparison arms can therefore reach the Go package test-program check despite the process's static-only environment. CLI default comparison, local MCP `compare=true` and detached comparison all reach this same consumer. This is a source-traced reachable path conditional on a selected Go target, executable generated body, installed Go and a module; no run demonstrated it. It prevents a whole-product static-only guarantee. SRC-1: `src/local/operations.ts`, `src/local/generate/generator.ts`, `src/local/cli.ts`, `src/local/mcp.ts`, `src/local/jobs/runner.ts`; [RT-RTE-generation-compare](#rt-rte-generation-compare).
3. **Caller-reported pass versus minted proof.** `record_run` remains static diagnostics even when it finds a hard association or receives `agent_pass`. Dynamic proof requires a green baseline and assertion-failing non-timeout mutant. RTM independently requires a closed dynamic certificate with a current target fingerprint. This is a code protocol for the inspected writers and consumer, not tamper-proof attestation of a writable local ledger. SRC-1: `src/local/operations.ts`, `src/local/rtm.ts`; [RT-RTE-targeted-proof](#rt-rte-targeted-proof).
4. **Trusted local execution versus container verification and delivery.** Local proof setup executes commands in the source checkout. The fault/candidate workflow instead uses copied trees and a Docker contract, repeated original/fault tests, text controls and restoration. Actions replay does not call the drafting model: it uses a configured candidate or returns a brief. Publishing is a separate confirmed GitHub path that opens a draft PR, not a merge. SRC-1: `src/local/operations.ts`, `src/local/candidateTest.ts`, `src/local/boundary.ts`, `src/local/actionsRun.ts`, `src/local/publishTests.ts`; [RT-RTE-draft-verification](#rt-rte-draft-verification), [RT-RTE-actions-delivery](#rt-rte-actions-delivery).

**Guarantee ownership and strength.** The local operation code owns static-only checks at start, automatic proof, default proof runner and setup boundaries; strength is **policy**, with implementation conclusion status: wired and operation conclusion status: uninspected for those checks. The comparison omission above limits coverage. The proof writer and RTM own the certificate protocol; strength is **protocol**, implementation conclusion status: wired, operation conclusion status: uninspected. Docker argument construction owns the requested isolation envelope; strength is **deployment guarantee**, implementation conclusion status: wired, operation conclusion status: uninspected. It requires Docker, OS isolation and successful boundary checks; it does not cover ordinary local setup, Go compile checks or the model HTTP client. Provider text, host shell actions and remote backend behavior do not pass through a single global OrangePro approval gate. These conclusions concern source wiring, not successful activation or benefit.

The capability surface includes reading caller-chosen workspaces, persisting graph/reports, model HTTP requests, subprocess execution, optional setup commands, copied-tree/container tests, workflow installation and confirmed GitHub delivery. The current grant set is the actual host filesystem/environment, configured keys, caller arguments and OS credentials; this analysis has no supplied deployment grants. A copied directory is not a hostile-code sandbox. The container lane requests a stronger, distinct envelope. Model providers return text rather than exercising provider-native function tools in the inspected adapters. External coding agents may act on that text with their own tools; their permissions and context isolation are outside the target. SRC-1: `src/local/generate/providers.ts`, `src/local/operations.ts`, `src/local/boundary.ts`, `src/local/mcp.ts`.

### Evidence and coverage limits

All findings below use SRC-1 implementation text, with explicit doctrine attribution for comments/prompts. Added inspection beyond the boundary's initial coverage includes `src/local/autoProve.ts` (gates, existing-test lane, generated-file write/proof), `src/local/generate/generator.ts` (context, pinning, raw/v5 paths, Go check), `src/local/generate/prompt.ts`, `src/local/generate/compareScore.ts`, `src/local/staticOnly.ts`, `src/local/rtm.ts` (certificate consumer), `src/local/jobs/runner.ts`, `src/local/boundary.ts` (Docker arguments), `src/local/candidateTest.ts` (stage sequence/classifier), `src/local/aiGraph/links.ts` and `src/local/flows/llmFlowDiscovery.ts` (apply), `src/local/actionsInstall.ts` (admission), `src/apiClient.ts` and `src/orangeproTools.ts`. These are source anchors at the frozen commit, not new sources.

No target execution, tests, provider request, Docker run or GitHub request was performed. The runner/mutator internals in `scripts/spikes/` were searched for relevant routing but not audited end to end; the mint protocol cannot establish their full mutation correctness. Parser coverage, all report renderers, source-redaction completeness, export receipt replay internals and infrastructure telemetry are not exhaustively inspected here. No universal non-exfiltration, isolation, mutation-soundness, backend idempotency, latency, quality or benefit conclusion follows. In particular, source excerpts enter generation prompts, so “local” storage and metadata exports do not imply that BYOK generation sends no source text. SRC-1: `src/local/generate/generator.ts`, `src/local/generate/providers.ts`. Model internals, host operation and live backend state remain outside the supplied evidence, as [boundary](boundary.md#boundary-and-evidence) specifies.

## Shared records

### Components

#### RT-CMP-openai
Label: OpenAI-compatible model endpoint

The OpenAI-compatible adapter supplies distributed-parametric inference through configured HTTP `baseUrl` and `model`; parameters reside in the external service, not in the local graph. `gpt-5.3-codex` names select the Responses API; other names use chat completions. Parameters are not updated by inspected OrangePro calls. Exact weights/version are unpinned; a mutable endpoint/name can resolve to another model. Provider training, caching and retention are uninspected. The adapter supplies system/user text, token controls, timeouts and bounded compatibility/truncation retries, not tool execution permissions. SRC-1: `src/local/generate/providers.ts`.

> instructions: req.system,
> input: req.user,
> max_output_tokens: maxTokens,
> store: false
> --- `src/local/generate/providers.ts`

#### RT-CMP-anthropic
Label: Anthropic model endpoint

Distributed-parametric model, external service substrate; `AnthropicProvider` posts system text and user messages with a configured model name. No parameter update is sent in inspected operation. Exact weights are unpinned; endpoint/model selection is mutable. Service internals remain uninspected. Adaptive-model handling raises budgets and retries once on max-token termination; reliable instruction compliance is not established. SRC-1: `src/local/generate/providers.ts`.

> if (data.stop_reason === "max_tokens") {
>   throw new Error("Model output was truncated at the token limit after one retry; no generated code was accepted.");
> }
> --- `src/local/generate/providers.ts`

#### RT-CMP-ollama
Label: Ollama model endpoint

Distributed-parametric inference accessed by `OllamaProvider`; weights reside behind the configured Ollama HTTP service, possibly local. No parameter updates are requested. Model name and endpoint are configurable rather than exact-weight pinned, and may resolve to changed weights. Provider internals remain uninspected. Unlike the inspected OpenAI/Anthropic branches, this adapter returns message content without their explicit truncation retry/rejection logic. The deterministic stand-in is symbolic rendering, not a fourth distributed-parametric component. SRC-1: `src/local/generate/providers.ts`.

> return data.message?.content ?? "";
> --- `src/local/generate/providers.ts`

### Operative objects

#### RT-OBJ-graph
Label: LocalGraph workspace graph

Source-native `LocalGraph`, stored as `.orangepro/graph.json` on the caller's filesystem. IDs, typed edges, fingerprints and status flags are symbolic inputs to fixed consumers; descriptions and acceptance text supply natural-language input to generation. Generated executable bodies are a separate operative part, [RT-OBJ-generated-tests](#rt-obj-generated-tests). This record identifies the graph container and runtime selectors, not a full memory revision assessment. SRC-1: `src/local/workspace.ts`, `src/local/operations.ts`, `src/local/generate/generator.ts`.

> export const WORKSPACE_DIR = ".orangepro";
> export const GRAPH_FILE = "graph.json";
> --- `src/local/workspace.ts`

#### RT-OBJ-generated-tests
Label: Generated test bodies and draft metadata

Part of: [RT-OBJ-graph](#rt-obj-graph)

`generated_tests` holds code bodies, target identity, grounding references, runnable/stale flags and provenance. Executable test bodies are symbolic code for runners; titles and guidance are natural-language input for agents/models. Storage is graph JSON, with separate runnable-file copies in the automatic proof lane and result artifacts in background jobs. A retained draft is not a proven test. SRC-1: `src/local/operations.ts`, `src/local/generate/generator.ts`, `src/local/autoProve.ts`, `src/local/jobs/runner.ts`.

> const freshTests = result.generated_tests.filter((t) => !t.pinned);
> --- `src/local/operations.ts`

#### RT-OBJ-dynamic-proof
Label: Dynamic targeted certificate

`DynamicProofCertificate` is a symbolic JSON ledger payload recording baseline/mutant conditions, runner, target/test identity and fingerprints. Its consumer is RTM's fixed predicate, not model judgment. It is local mutable filesystem evidence, not a signature or an independently authenticated run. SRC-1: `src/local/operations.ts`, `src/local/rtm.ts`.

> proof_kind: "dynamic_targeted",
> baseline_green: baselineGreen,
> mutant_failed_assertion: mutantFailedAssertion,
> --- `src/local/operations.ts`

### Routes

#### RT-RTE-start-run
Label: Start orchestration and automatic proof

CLI/MCP caller → `opStart` → reuse or analysis → AI passes → changed-scope automatic proof → draft fill → reports/return. Code owns sequencing and risk/worklist selection; models propose links, flows and test text, not the next arbitrary shell step. The mode is open repository requests with bounded per-stage budgets, not an autonomous curriculum. Invocation is not per-test human approval. Caller controls include no-AI, no-auto, proof/draft budgets, static-only and fresh recomputation; not every interface exposes every option. SRC-1: `src/local/cli.ts`, `src/local/mcp.ts`, `src/local/operations.ts`, `src/local/autoProve.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reports, changed/gap summaries, AI/proof/generation outcomes and agent guidance; reuse may return earlier results.
- Later read-back: Saved graph, generated drafts, ledger and saved start result feed subsequent runs and reports.
- Delegated visibility: Provider calls receive selected prompts; automatic test subprocesses receive code/setup environments, not the host conversation.
- Selection predicate: Saved run-key eligibility first; otherwise changed scope and deterministic ranking; current proven targets skipped; existing associated tests tried before model-provider or offline deterministic generation; `no_ai` suppresses the non-deterministic automatic generation lane when a non-deterministic provider resolves, but does not suppress explicit deterministic mode.
- Invalidation or expiry: Changed run-key inputs force recomputation; current target fingerprints govern proof/draft reuse; `fresh` overrides start reuse.
- Activation or effect: Writes analysis and reports, may create test files and run proof; source wiring establishes capacity, not exercised activation.
- Evidence limits: No supplied execution or benefit evidence; ranking and all reuse-key internals are not audited exhaustively.

Admission: configured models or the offline deterministic stand-in propose new tests; automatic path containment and no-overwrite checks decide file admission, and the proof oracle separately decides credit. Caller can disable automatic proof with `noAuto` or its proof budget; `no_ai` alone is not an offline-generation veto. No interactive per-content approval appears at the generated-file write. Generated files remain named in results, including unsuccessful proof attempts; rollback is not an automatic deletion guarantee. Baseline failures and project-wide setup blockers are classified; advisory render failures do not invalidate a minted certificate. The reference outcome for credit is the dynamic baseline/mutant protocol, not a known correct test supplied by a human.

The provider distinction follows executable branches rather than start's older “no key ⇒ no files, no proof” comment or its broad no-AI progress message. CLI forwards both the no-AI flag and provider selection. Explicit deterministic resolution does not consult credentials; automatic proof uses a symbolic offline provider and can call generation for remaining eligible gaps. The separate later gap-filling phase still requires `opts.ai !== false`. SRC-1: `src/local/cli.ts`, `src/local/operations.ts`, `src/local/autoProve.ts`.

> if (opts.provider === "deterministic") return new DeterministicProvider();
> --- `src/local/operations.ts`

> existingOnly: opts.ai === false && generationProviderConfigured && !deterministicGeneration
> --- `src/local/operations.ts`

> const provider = deterministic ? new DeterministicProvider() : buildProvider(providerConfig!);
> const generate = deps.generate ?? generateTests;
> const reader = fileReaderFor(sourceRoot);
> --- `src/local/autoProve.ts`

> } else if (!opts.noAuto && generationProviderConfigured && opts.ai !== false && generationLimit > 0) {
> --- `src/local/operations.ts`

> // ── Lane 1: existing associated tests — NO key required, runs FIRST (PR 1.5). ──
> --- `src/local/autoProve.ts`

> if (existsSync(abs)) {
>   // Guardrail: never overwrite an existing file.
>   skipped.push({ target_symbol, title: test.title, reason: `Existing file ${writeRel} not overwritten.` });
>   continue;
> }
> --- `src/local/autoProve.ts`

> writeFileSync(abs, `${GENERATED_HEADER}\n${body}${body.endsWith("\n") ? "" : "\n"}`, "utf8");
> --- `src/local/autoProve.ts`

#### RT-RTE-test-generation
Label: Grounded test generation

CLI single/MCP → `opGenerate` → graph load/provider resolution → target/framework/context selection → v2 completion or v5 plan/parse/repair/batch → body checks → fresh draft persistence → runnable run hints. Code selects evidence and accepts/rejects draft structure; the model proposes scenarios and tests. Prompt rules request criterion-linked assertions and low-confidence treatment of weak context. No independent expected-answer oracle establishes semantic correctness. Mode: open drafting with bounded calls; failure/missing evidence yields guidance or explicitly non-runnable manual fallback. SRC-1: `src/local/operations.ts`, `src/local/generate/generator.ts`, `src/local/generate/prompt.ts`, `src/local/mcp.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Test bodies, validated graph citation summaries, warnings, missing evidence and runnable-only run hints; no provider returns setup guidance.
- Later read-back: Fresh tests and generation runs are appended to graph; unchanged eligible runnable drafts may be returned verbatim on later calls.
- Delegated visibility: Provider gets selected acceptance/workflow, related metadata, redacted source excerpts and weak context; v5 repair sees malformed plan, not a whole host session.
- Selection predicate: Explicit targets or ranked gaps, framework compatibility and capped slots; v5 limits accepted scenarios, filters duplicates and validates repair ties to original text.
- Invalidation or expiry: Pinning requires unchanged target fingerprint; later analysis preserves only eligible artifacts; unresolved bodies remain distinguishable from runnable drafts.
- Activation or effect: Persists proposed executable artifacts and supplies host write/run guidance; Go generation can temporarily write and execute a package compile check outside static-only.
- Evidence limits: Grounding verifies references, not assertions' truth or actual execution; not every language/body validation branch was inspected.

The host may reject or edit a returned test before writing it. Local graph admission is software-controlled, not dependent on this later human/host choice. Direct generation's `wrote_repo_files: false` is not a general non-execution guarantee: Go's check writes a temporary test and invokes `go test -run ^$ .`, then removes it. The source comment correctly recognizes that this starts `init`/`TestMain`. SRC-1: `src/local/generate/generator.ts`.

> // In-process, redacted source excerpts — used for the prompt only, never stored.
> const excerpts = buildSourceExcerpts(graph, behavior, relatedFiles, testFiles, fileReader);
> --- `src/local/generate/generator.ts`

> "- Include at least one assertion tied to a stated acceptance criterion or expected behavior.",
> --- `src/local/generate/prompt.ts`

> static_only: opts.static_only ?? isStaticOnly(providerEnv)
> --- `src/local/operations.ts`

#### RT-RTE-generation-compare
Label: Comparison and detached generation

CLI default generation or MCP compare → `opCompare` → raw and grounded `generateTests` → model judge or lexical heuristic → comparison output/report. Background CLI re-execs a detached child with inherited environment; the job runner uses the same compare/single operations and writes status/result files. This is durable process coordination, not an isolated model agent with its own planning authority. Code owns job state transitions and polling artifacts; a child gets arguments/environment and reloads graph. SRC-1: `src/local/cli.ts`, `src/local/jobs/runner.ts`, `src/local/operations.ts`, `src/local/generate/compareScore.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Foreground comparison suites/scores or background job ID, log and status paths.
- Later read-back: Job status/results and comparison reports can be polled/read after the launcher returns; compare does not append generation runs to graph.
- Delegated visibility: Child inherits process environment and resolved flags, not a transcript; model calls use raw or grounded prompts and judge context.
- Selection predicate: Same selected target/framework/limit options passed to each arm; judge used for real provider with tests, otherwise graph-derived heuristic.
- Invalidation or expiry: Fresh comparison report replaces the previous view; job completion/failure is recorded; automatic restart after interruption is uninspected.
- Activation or effect: Produces comparative artifacts; can reach Go compile execution because the shared compare options omit static-only.
- Evidence limits: Scores are not observed test correctness or a causal experiment; static-only omission is statically reachable, not experimentally exercised.

Mode is a bounded A/B generation view, not improvement of the deployed model or prompt. The heuristic's source-native “oracle” consists of graph tokens/file stems; model judgment is not an independent answer oracle. No selected winner is automatically installed as a new prompt or provider policy. Source comparison comments saying only KG injection differs are qualified: opt-in v5 affects the grounded path, and raw generation has a separate branch. SRC-1: `src/local/operations.ts`, `src/local/generate/generator.ts`.

The static-only exclusion is specifically traced through supported callers: CLI sets the environment before dispatch; CLI default and MCP compare call `opCompare`; background compare also calls it. The shared object below lacks `static_only`, and all three inspected Go generation call sites pass `opts.static_only === true` to the helper. The helper does not itself read the environment. Thus inheritance of the variable in the detached child does not repair this path. SRC-1: `src/local/cli.ts`, `src/local/mcp.ts`, `src/local/jobs/runner.ts`, `src/local/operations.ts`, `src/local/generate/generator.ts`.

> const shared = { target_ids: opts.target_ids, framework: opts.framework, limit: opts.limit };
> const baseline = await generateTests(graph, { ...shared, input_mode: "raw_prompt" }, provider, reader, deps.clock);
> const grounded = await generateTests(graph, { ...shared, input_mode: "graph_grounded", prompt_version: opts.prompt_version }, provider, reader, deps.clock);
> --- `src/local/operations.ts`

> function goCompile(body: string, workspaceRoot: string, relatedFiles: string[], staticOnly = false): GoCompileResult {
>   // `go test -run ^$ .` builds and starts the package's test program (init, TestMain): repository code.
>   if (staticOnly) return { body, issue: NOT_COMPILE_CHECKED };
> --- `src/local/generate/generator.ts`

> execFileSync("go", ["test", "-run", "^$", "."], { cwd: packageDir, stdio: "pipe", timeout: GO_COMPILE_CHECK_TIMEOUT_MS });
> --- `src/local/generate/generator.ts:1668-1668`

#### RT-RTE-targeted-proof
Label: Dynamic proof mint and RTM consumption
Caller or auto-prove → optional `opProveLoop` setup → `opDynamicProof` target resolution/preflight → language-specific runner → common oracle gate → certificate/ledger → RTM current-fingerprint selection. Symbol resolution and target-record preflight constrain what is credited. Go requires anchored test name; Java requires class/method; Python and TS/JS carry explicit test and runner inputs. TS/JS supports a bound preview branch that returns a diff without ledger admission. Code, not caller `agent_pass`, owns credit. SRC-1: `src/local/operations.ts`, `src/local/rtm.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Proof result, diagnostic baseline/mutant summary and ledger status; bound preview returns only proposed mutation/digests.
- Later read-back: Ledger certificate is read by RTM, reports and automatic skip logic.
- Delegated visibility: Default Node child runs language-specific spike; setup runs in the source checkout with inherited process environment; copies/runners are not a universal permission boundary.
- Selection predicate: Resolved credited symbol and supported language; green non-timeout baseline plus assertion-failing non-timeout mutant; RTM requires dynamic certificate and current target fingerprint.
- Invalidation or expiry: RTM selects the newest valid matching proof if any, otherwise latest record as unproven; changing target fingerprint prevents old proof credit.
- Activation or effect: Runs repository tests and appends proof records; proof eligibility changes report tier and future automatic selection.
- Evidence limits: Protocol wiring only; runner soundness, actual mutation kills and hostile ledger tampering are not established.

Admission trigger is an explicit proof request or automatic selected target. Software can reject target shape/staleness, setup or oracle outcome. Setup failure returns unrunnable and appends nothing; proof failure records unproven. Best-ever matching proof selection means a later unproven attempt does not necessarily erase an older current proof. There is no general transactional rollback of arbitrary setup commands. Mode is a bounded mutation test, with a computational reference outcome (baseline green, mutant assertion failure), not a complete specification oracle.

> oracle.status === "proven" &&
> oracle.proven === true &&
> oracle.baseline?.exitCode === 0 &&
> oracle.baseline?.timedOut !== true &&
> oracle.mutant?.exitCode !== 0 &&
> oracle.mutant?.assertionFailure === true &&
> oracle.mutant?.timedOut !== true
> --- `src/local/operations.ts`

> assertMayRunRepositoryCode("a dynamic proof run");
> --- `src/local/operations.ts`

> if (commands.length > 0 && isStaticOnly()) return { ok: false, reason: STATIC_ONLY_REFUSAL };
> --- `src/local/operations.ts`

> entries.filter((e) => isDynamicProofRecord(e.record) && e.record.target_fingerprint === currentFingerprint)
> --- `src/local/rtm.ts`

> reason = "Target already had a static hard edge before this run; record_run is static diagnostics only and public Proven requires orangepro_prove.";
> --- `src/local/operations.ts`

#### RT-RTE-candidate-admission
Label: AI link and flow admission

Caller generate/apply or start → selected graph context → model proposals → staged file → software revalidation → candidate lane in graph. Explicit apply calls need not make a provider call. `opStart` calls both generation and apply, contrary to an older `opAiFlows` comment saying it never auto-runs. The executable start driver determines this finding. Models propose; code validates and admits; manual standalone apply permits caller withholding, but start does not wait for per-proposal human approval. Mode is open bounded candidate discovery. No independent expected-answer oracle validates relevance; allowed identities and structural checks are not semantic proof. SRC-1: `src/local/operations.ts`, `src/local/aiGraph/links.ts`, `src/local/flows/llmFlowDiscovery.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Staging/application counts, rejected proposals and warnings.
- Later read-back: `.orangepro/ai/links.json`, `.orangepro/flows.json` and applied graph lanes feed later apply/report/context consumers.
- Delegated visibility: Model sees shortlisted graph anchors; apply rechecks current graph rather than trusting labels in the staged file.
- Selection predicate: Links are validated against graph; flows require workspace hash match and intersection of shown/current entries and symbols.
- Invalidation or expiry: Flow revalidation drops stale anchors during apply/reanalysis; link admission deduplicates against existing candidates.
- Activation or effect: Adds candidate associations/worklists; candidate links enter weak generation context, but cannot alone satisfy RTM dynamic-certificate credit.
- Evidence limits: Identity/structure validation is not demonstrated relevance; full candidate generation and ranking algorithms are not audited here.

Admission retains symbolic link/flow IDs and natural-language proposal metadata. Software rejection and reanalysis provide recovery from invalid/stale proposals; no dedicated undo transaction is established. Flow metadata is stored separately from deterministic flows; v5 `flowChainFor` selects `analysis.flows`, not `analysis.candidate_flows`. That scoped separation does not imply all AI-derived content is excluded from prompts: weak candidate edges are included by `gatherContext`. SRC-1: `src/local/generate/generator.ts`.

> const merged = dedupeCandidateEdges([...graph.candidate_edges, ...applied]);
> const after = merged.length;
> const next: LocalGraph = { ...graph, candidate_edges: merged };
> --- `src/local/aiGraph/links.ts`

> const validHopIds = new Set(artifact.shown_symbol_ids.filter((id) => anchors.anchorIds.has(id)));
> --- `src/local/flows/llmFlowDiscovery.ts`

#### RT-RTE-draft-verification
Label: Fault brief to verified candidate test

Fault/brief input → `opDraftTest` → provider test JSON → code-built additive patch/assertion record → `opVerifyTest` → bounded repair or terminal verdict. This is a separate mechanism from generic graph draft generation. Code loads and checks a fault run and brief before calling the model, then constrains file/describe/test shape and repairs. The provider proposes code; verifier predicates decide acceptance and can reject it. Human input supplies the task's expected-behavior oracle through the approved brief; this report does not establish its factual correctness or approval history. Mode is a bounded per-fault experiment, not open-ended autonomous improvement. SRC-1: `src/local/draftTest.ts`, `src/local/candidateTest.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Attempt paths and verified/not-verified/inconclusive result with reason and verified run, if any.
- Later read-back: Attempt folders retain prompts/replies/patches/manifests; earlier attempts enforce per-fault budget; successful verify run feeds export/delivery.
- Delegated visibility: First provider call receives fixed header plus generation-request bytes; repair receives prior test and verdict. Docker tests receive copied source/test material, not the provider key by intention of the drafting path.
- Selection predicate: Checked fault/brief, listed neighbour file, unique assertion line and constrained repair; verifier requires original/fault repeats, declared-line failure, restoration, text controls and full-suite conditions.
- Invalidation or expiry: At most three counted candidates per fault plus command deadline; not-caught or blocked verdict stops; provider error is not counted as a written draft and stops this invocation.
- Activation or effect: Writes candidate artifacts and executes verification; verified_gap is a controlled classification, not an observed result in this analysis.
- Evidence limits: Oracle truth, exhaustive AST anti-cheating constraints and live container isolation are not established; no execution supplied.

Recovery keeps attempts and reports why no candidate verified. The first actually verified candidate supplies the baseline for later repair restrictions; repairs may change setup, not assertion/condition/test identity. The classifier returns inconclusive for mismatched copies, unstable tests, text-aware behavior or incomplete full-suite checks. The original checkout remains outside the patched copies and is checked for unchanged state. Docker contract is separate from ordinary local proof: requested no network, dropped capabilities, read-only root and explicit mounts depend on the Docker/OS contract. SRC-1: `src/local/candidateTest.ts`, `src/local/boundary.ts`.

> const SYSTEM = "You write one repository-native Mocha test from OrangePro's brief. You reply with one JSON object and nothing else.";
> --- `src/local/draftTest.ts`

> if (v && (v.result === "blocked" || v.result === "not_caught")) stop = v.result;
> --- `src/local/draftTest.ts`

> if (!input.checkoutUnchanged) return out("blocked", "checkout_modified");
> --- `src/local/candidateTest.ts`

> if (!cleanFile(ot!)) return out("inconclusive", "mutation_aware");
> --- `src/local/candidateTest.ts`

> "--network",
> request.network ?? "none",
> --- `src/local/boundary.ts`

#### RT-RTE-actions-delivery
Label: Actions replay, installation and draft PR delivery

Installer → configured workflow/profile → Actions event → changed targets/fault probe/brief → configured candidate replay → verify/export → separate publisher. This route changes production machinery (workflow files) and customer tests, not OrangePro weights. `opActionsRun` has no generation call in its replay chain; missing candidate returns needs_test. `opPublishTests` checks an export receipt/patch, then requires confirmation and a GitHub token before delivery. SRC-1: `src/local/actionsInstall.ts`, `src/local/actionsRun.ts`, `src/local/publishTests.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Installer preview/conflict/install result; Actions classification/artifact paths; publisher dry-run/delivery/blocker record and PR URL when available.
- Later read-back: Installed workflow/profile drives later events; run folders and receipt drive delivery; GitHub branch/PR are read back for reuse and verification.
- Delegated visibility: Actions test stages use containers; dependency installation uses network-enabled writable checkout mount; publishing uses token-bearing API requests outside that test boundary.
- Selection predicate: Profile/event eligibility, survived fault, verified candidate and fresh export; publisher checks proven commit against base, managed branch ownership and one-file draft PR read-back.
- Invalidation or expiry: Moved base refuses delivery; diverged branch refuses overwrite; closed PR is not reopened; installer refuses conflicting edited managed files.
- Activation or effect: Confirmed install writes workflow machinery; confirmed delivery creates/updates a non-force branch and draft PR, not an automatic merge.
- Evidence limits: Receipt validation/replay internals not audited completely; GitHub operation and OS container enforcement are unobserved; author of configured candidate may be human or computation.

Admission roles: installer code proposes fixed machinery and caller `apply` admits it; code can veto conflicts. Replayed candidate authorship precedes the Actions run; classifier/export predicates admit the test artifact, and a separate `yes` admits publication. The workflow can contain that confirmation automatically, so it is not evidence of a new human approving each test. Expected behavior derives from configured oracle/fixture, with repeated executions used as checks rather than a model correctness judgment. Modes are configured post-merge replay and explicit delivery. Recovery preserves artifacts; a base race may leave the newly created branch without a PR, so delivery is not globally atomic. Merging or reverting the PR belongs to GitHub users/policies, outside this implementation.

> if (!loaded.candidate) {
>   end("needs_test", "no_candidate", `${fault.classification.statement} The profile names no test to replay; the brief is in the artifacts, for one to be written.`);
>   return;
> }
> --- `src/local/actionsRun.ts`

> network: kind === "install" ? "bridge" : "none"
> --- `src/local/actionsRun.ts`

> if (!opts.yes) {
>   return finish("dry_run", null, `Would open a draft PR on ${opts.repo} from ${branch} into ${opts.base}, changing ${run.patch.file} only. Nothing was written (add --yes).`);
> }
> --- `src/local/publishTests.ts`

#### RT-RTE-platform-call
Label: Hosted platform adapter invocation

MCP host → platform stdio or remote worker → authenticated REST call → tool text response. Platform tools can trigger an agent run and request grounding/QA operations, but the backend owns scheduling, model calls and persisted knowledge. No local evidence graph is implicitly shared with it. Source-native agent IDs/tenant IDs are REST parameters, not spawned local agents. SRC-1: `src/index.ts`, `src/server.ts`, `src/orangeproTools.ts`, `src/apiClient.ts`, `packages/mcp-remote/src/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Backend data or MCP error; triggering an agent returns backend run summary rather than locally awaiting its entire work.
- Later read-back: Runs/logs/health tools request backend state; backend persistence and its later consumers are uninspected.
- Delegated visibility: Selected REST arguments and configured credentials cross network; no host transcript supplied by these inspected handlers.
- Selection predicate: Tool/schema and caller agent/tenant IDs; remote request headers may override base URL/key/tenant.
- Invalidation or expiry: Stdio client has configured request timeout; remote worker constructs a stateless server per /mcp request; backend run expiration is uninspected.
- Activation or effect: Adapter can request backend work; actual execution and idempotent retry behavior remain backend contracts.
- Evidence limits: No backend implementation or execution evidence; neither backend isolation nor model authority can be inferred from MCP annotations.

Admission and operating mode: open host tool requests, with caller selecting remote action and backend deciding execution. Starting a run is not per-content approval. No expected-answer oracle, rollback or internal improvement trigger is visible at the adapter boundary. The remote source comment advertises Bearer/X-Api-Key authentication, but its inspected client consumes `x-orangepro-api-key` or worker environment; deployed authentication outside this file is uninspected. A configured environment key is not evidence that incoming requests are independently authenticated.

> const run = await client.post<AgentRunSummary>(agentPlatformPath(tenantId, `/agents/${encodeURIComponent(input.agent_id)}/run`));
> --- `src/orangeproTools.ts`

> const apiKey =
>   requestHeaders.get("x-orangepro-api-key") ||
>   env.ORANGEPRO_API_KEY ||
>   "";
> --- `packages/mcp-remote/src/index.ts`

### Claims

#### RT-CLM-local-generation
Label: Local generation ownership claim

The MCP generation contract describes a host-owned write/run workflow. This is declared interface guidance, not a whole-system invariant. Generic generation's Go package check and start's automatic write/prove lane qualify it. SRC-1: `src/local/mcp.ts`, `src/local/generate/generator.ts`, `src/local/autoProve.ts`; [RT-RTE-test-generation](#rt-rte-test-generation), [RT-RTE-start-run](#rt-rte-start-run).

> // The agent is the test runner: return each RUNNABLE test's suggested write
> // path + run command plus the write -> run -> report workflow. Non-runnable
> // grounded drafts (runnable === false) are excluded from run_hints so the
> // agent never runs a draft with a fabricated/missing import; they remain in
> // `generated_tests` with their `unresolved_reason`. OrangePro never writes
> // to or runs anything in the repo.
> --- `src/local/mcp.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-generation-prompt
Label: Test-generation instruction authority

Consumer: configured model through provider `complete`. Channel: system instructions plus selected evidence in user text. Force: requested test design and output format, mediated by model interpretation; code parsing/body checks constrain what is admitted but do not prove compliance. Horizon: current model request and retained test artifact; later executable authority requires host or automatic write/run. SRC-1: `src/local/generate/prompt.ts`, `src/local/generate/generator.ts`, `src/local/generate/providers.ts`; [RT-RTE-test-generation](#rt-rte-test-generation). Prompt strings are natural-language procedural guidance in shipped TypeScript storage; this record does not assert a formulated theory or a theory-builder route.

> "- Treat WEAK CONTEXT as low-confidence hints, not facts.",
> "- Output ONLY the test code — no Markdown code fences, no prose, no explanation."
> --- `src/local/generate/prompt.ts`

#### RT-BAP-proof-credit
Label: Certificate authority over public tier

Consumer: RTM `isDynamicProofRecord` and current-fingerprint selector. Channel: symbolic ledger fields. Force: fixed predicate grants public Proven tier and skip eligibility; horizon: later reports/start runs while the target fingerprint matches. This consumer checks data values rather than authenticating process origin. SRC-1: `src/local/rtm.ts`, `src/local/autoProve.ts`; [RT-RTE-targeted-proof](#rt-rte-targeted-proof).

> record?.status === "reproven" &&
> record.closed === true &&
> proof?.proof_kind === "dynamic_targeted" &&
> proof.baseline_green === true &&
> proof.mutant_failed_assertion === true &&
> proof.target_not_mocked === true
> --- `src/local/rtm.ts`

## Annotations

none
