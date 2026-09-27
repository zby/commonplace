# Context-engineering additions, first chunk

## Scope and decision

On 2026-09-27 the operator requested a larger chunk. This pass reads the first
twenty open context-engineering suggestions in stable queue order. All twenty
qualify under the existing head. Three companion suggestions also qualify:
failure-modes and curation on the retrieval-miss note, and document-system on
the seven-documentation-cases evidence note.

The boundaries matter. Prompt assembly qualifies where the note develops the
supplied roles, checklists, and probes; activation alone is not sufficient.
Information value qualifies through its concrete retention and loading rule
for a bounded reader. The legal-drafting comparison qualifies through its
worked prompt-design and task-targeted compression applications. No head is
broadened to accept these cases.

This is a metadata placement decision, not a new truth or grounding assessment.
Note bodies, inclusion rules, original reviewer words, and frozen baselines
are unchanged. Two curated links keep failure-modes and curation complete.

## Accepted entries

| Entry | Note | Reason |
| --- | --- | --- |
| ADD-013 | [A retrieval miss is a local reflective-path failure](../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) | Accept context-engineering, failure-modes, and curation: the note traces how discovery and mandatory loading deliver a self-representation, how a retrieval miss leaves it inert, and how unenforced index completeness suppresses the search needed to recover missing members. |
| ADD-016 | [Access burden and transformation burden are distinct query dimensions](../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) | Accept context-engineering: the note separates finding required inputs from transforming them, then develops a repeated acquire/transform/check route that exposes only the inputs and unresolved judgment needed for each bounded semantic call. |
| ADD-021 | [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) | Accept context-engineering: retrieval and activation are developed as the memory subsystem problem of getting stored knowledge into the right bounded call; the runtime decomposition assigns that work to the context engine. |
| ADD-033 | [AGENTS.md should be organized as a control plane](../../notes/agents-md-should-be-organized-as-a-control-plane.md) | Accept context-engineering: loading frequency and omission cost govern what stays always loaded, what routes to task-specific material, and what should be externally triggered, with token pressure and attention dilution as distinct costs. |
| ADD-034 | [Agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) | Accept context-engineering: follow/skip decisions allocate a bounded reading budget; pointer cues must reduce uncertainty enough to justify their context cost before the target is loaded. |
| ADD-059 | [Conversation vs prompt refinement in agent-to-agent coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) | Accept context-engineering: conversational continuation, prompt refinement, and shared-prefix forking are compared by what intermediate work and misleading history cross the next call boundary. |
| ADD-061 | [Decomposition heuristics for bounded-context scheduling](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) | Accept context-engineering: the scheduling heuristics decide what each call receives, which intermediates stay outside it, when items must be co-loaded, and which information compression must preserve. |
| ADD-069 | [Elicitation requires maintained question-generation systems](../../notes/elicitation-requires-maintained-question-generation-systems.md) | Accept context-engineering: the note assembles review calls from perspective assignments, explicit domain checklists, and targeted probes, then maintains those inputs as failure families change. The fit is to constructing and refreshing the supplied context, not a claim that all parametric knowledge activation is retrieval. |
| ADD-076 | [Seven documentation cases left routing and synthesis](../../notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md) | Accept document-system and context-engineering: the casebook tests which documentation units remain worth retaining and routes exact questions to live source while preserving unknown-name discovery maps and cross-component synthesis. |
| ADD-082 | [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../../notes/feasibility-is-the-heaviest-forks-net-load.md) | Accept context-engineering: feasibility depends on the largest residual context load after work is moved to siblings or a parent; the note separates token volume, processing complexity, and interference. |
| ADD-086 | [Flat memory predicts specific cross-contamination failures that are empirically testable](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) | Accept context-engineering: search pollution, scattered operational knowledge, and trapped session insights are analyzed through whether useful material reaches later sessions and which retained spaces make it findable. |
| ADD-088 | [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) | Accept context-engineering: precomputed results replace discovery, source loading, and derivation inside a later call; the note specifies token, interference, validity-window, and prompt-assembly tradeoffs. |
| ADD-098 | [Information value is observer-relative](../../notes/information-value-is-observer-relative.md) | Accept context-engineering: the KB application chooses retained content by what the intended bounded reader cannot reliably supply, and develops descriptions, claim titles, and short notes as ways to select and load useful content. |
| ADD-099 | [Instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) | Accept context-engineering: the note directly allocates universal rules, skill descriptions, skill bodies, and task documents across always-loaded and on-demand context. |
| ADD-100 | [KB goals in always-loaded context guide inclusion decisions](../../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) | Accept context-engineering: the dedicated placement argument puts frequently used inclusion criteria in always-loaded context, comparing their availability with the retrieval hop and search pollution of alternative arrangements. |
| ADD-102 | [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) | Accept context-engineering: the note distinguishes storage-to-context delivery from context-to-action uptake, specifies routing and loading remedies, and explains why adding context can also dilute relevant cues. |
| ADD-105 | [Legal drafting solves the same problem as context engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) | Accept context-engineering: the worked transfer to prompt and knowledge-system design includes term definitions, instruction precedence and routing, reusable prompt components, and task-targeted compression under page and attention limits. The placement rests on these applications, not the title alone. |
| ADD-106 | [Link-following and search impose different metadata requirements](../../notes/link-following-and-search-impose-different-metadata-requirements.md) | Accept context-engineering: link-following, search, index entries, and skill descriptions provide different cues for deciding which artifact to load next, requiring different routing metadata. |
| ADD-109 | [Links encode conditional possibilities, not obligations](../../notes/links-encode-conditional-possibilities-not-obligations.md) | Accept context-engineering: inline-versus-link decisions depend on the reader state, what is already loaded, and which unmet need justifies bringing another artifact into context. |
| ADD-111 | [LLM contexts interpret instructions and content through the same token medium](../../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) | Accept context-engineering: the shared instruction/content medium creates scope contamination and authority confusion during context assembly, and routing is needed to identify which prose should change behavior. |

## Parent checks and accounting

Four original learning-theory gaps close after checking their supporting tags:

- PG-018 / ADD-013: the note explains a failure in causal connection through
  self-representation, directly fitting reflection and its existing
  self-improving-systems parent.
- PG-058 / ADD-069: the elicitation workflow targets missed concerns and
  knowledge the model can supply when probed, fitting llm-reliability's
  detection and correction of output deviations.
- PG-064 / ADD-076: source ownership and retained form change the maintenance
  decision. Exact derived descriptions yield to live implementation; checked
  routing copies and cross-component synthesis retain distinct roles. This
  applies lineage and authority distinctions with retention consequences,
  meeting artifact-analysis's single-field application rule.
- PG-078 / ADD-102: the distinction between exposure and behavioral uptake
  explains why visible knowledge fails to guide output, with explicit
  interventions to detect and correct that failure, fitting llm-reliability.

The retrieval-miss note also gains kb-maintenance as the required parent of
its new curation assignment. That parent addition is outside PC-07's frozen
learning-theory inventory. Context-engineering itself does not require a
learning-theory parent. The document-system addition concerns what document
content to retain and how readers find it, so it does not depend on settling
the broader architecture boundary.

This pass adds twenty-eight assignments across twenty notes: twenty
context-engineering, one failure-modes, one curation, one document-system,
four learning-theory, and one kb-maintenance. No assignments are removed.
The failure-modes and curation heads each gain the retrieval-miss note as a
curated entry. Parent completeness continues to route through supported
children; the other eight head inputs are unchanged.

The workshop now records 105 accepted addition entries, three duplicate
removal closures, and 98 open additions. All 68 original placement findings
remain resolved. PC-07 has 39 resolved and 90 open parent-gap entries.

## Verification

`commonplace-validate` passed on all twenty-eight changed files and the tags
collection: zero failures and zero warnings. Separate checks confirmed
twenty-eight added assignments, no removals, twenty unchanged note bodies,
ten unchanged inclusion rules, queue counts, and all thirty recorded final
hashes. Eight heads are entirely unchanged; the other two gain only curated
entries. `git diff --check` passed.
These are direct semantic judgments, not new independent assays. Changes
remain uncommitted.

## Checked versions

SHA-256 hashes identify the twenty note inputs and ten heads used. Only
failure-modes and curation change, through curated entries.

| Artifact | Before | After |
| --- | --- | --- |
| `kb/notes/a-retrieval-miss-is-a-local-reflective-path-failure.md` | `0a4973cc479ed5b91065f4480a7ffde79f89db8c673abf7387470f119ab63f92` | `904856806e88e20c79c7113885670ee32f35335c500baadc0411aa36597bf0b3` |
| `kb/notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md` | `49c2ceb363d6c476b39311d47d6757828813eb3bcc1602fed005313f7a1bf0a2` | `2889835d491c137d28910796c08c1b2a86da4ffa2ab175bce5a1245b8d888e77` |
| `kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md` | `c52bc781cff5c84a6e596e4e9b285b9c6cdc7c5fa28e1dcb69e670a41a14ae69` | `21cc5afd5a3f59198911bff85c32cc931acbcca7a1ec0e3d14c2b5c2538670b6` |
| `kb/notes/agents-md-should-be-organized-as-a-control-plane.md` | `ab569658aef9a3a4a246b19d28118046da4ba5c20cf905a92ebc2a9f532f5184` | `6da65d3124017087871ee367aa00d4308a503d84a46c11676cb9bc5a2327ed1a` |
| `kb/notes/agents-navigate-by-deciding-what-to-read-next.md` | `11fc9f5e48a1ca3e71ba1325a08479e2827b6a342789d9edbd524a250704b6b8` | `e451be3720df254f86e6d02dfa77a8f48046d7123a2662fa2a8024f88e39301d` |
| `kb/notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md` | `34769e24064ec77a39b1d526c17e47bf4fe253d3d960df595e1bd6a13f4833d8` | `66e7e1d7382626ae5fa2128a55b61b127fb8ef57f09f06b4bd416afa5da9ee3b` |
| `kb/notes/decomposition-heuristics-for-bounded-context-scheduling.md` | `6fc2e8629573eab8ea82f2d4d1893eef60979a90b88c74a782dc750d10aae577` | `4a055e5c41977b355a9cd89a34be2ebf0d9b495785b788fd63457b5e38ff7004` |
| `kb/notes/elicitation-requires-maintained-question-generation-systems.md` | `335496cc5167d70138f3043165323e14de88cb0aa281ffeb0bbe88305a89cce3` | `c87390762a1cf96e8ec9286b061ad1a9f38dd1b7f217860c365c1642d647dd10` |
| `kb/notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md` | `08fa186d122d2af7b01040ce09b5264ba47111b2e476f22cc4f862e9bfb23c07` | `c31be2da82cfbebb05583c79345bc8297bc4fe70b4640f6e86de6df8a64bd389` |
| `kb/notes/feasibility-is-the-heaviest-forks-net-load.md` | `239b3d7f6e8f90ee07027b40e5c9d6124f89fc9979166d4649a498bd69215b25` | `2f14356c5e6fb17a8345a2a66b7c50482295876a1550411aeb9086c90bc48c54` |
| `kb/notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md` | `4ceb67c49f2aec43240753024597675f4a1a1dabfa1786901c9e441c2b5bf5a5` | `601db465009347f71f873a4ae85f669f498033d9b7cb3ca9401842d382ffb4c2` |
| `kb/notes/frontloading-spares-execution-context.md` | `8e16a655692b0c8e1752372d0da25fe9dde031a9e7d7216671bc02acc5328777` | `4356a9b75bc80446228abbedff3d4a27a9e4f615bd83e186cea7ebf39062952a` |
| `kb/notes/information-value-is-observer-relative.md` | `43c0c77654f88a143ffb82627ef09abdef34bd2ebf7eb1e68e85c59a17f1455f` | `77a0864fb10949581ce710869744b320f610d3b04b21f0ec77d69199499001a8` |
| `kb/notes/instruction-specificity-should-match-loading-frequency.md` | `394ff2c3f619b34c933f16b7162a7d6910bf1b44eb24094ec84c85d05ded6195` | `c07f688cebd12531242e40ffb8081e0c9e3f398a4bd099f752c974a21239da3c` |
| `kb/notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md` | `ca272742a78a66b3b8a423409772785953904557558102f114acf5689d5d1c36` | `14e34d6a58997ef2e7ce148b757f5c9194d29517dc7bfb7219faa9792d4f46a7` |
| `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md` | `119c246ef57a3bdf112a472c7c932a282c83f93ae78a4a21f39f91cb48e62398` | `10f25c574545b6badf747c1242746b9d067f57dd336a2c4b9acde0b56dc94342` |
| `kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md` | `4137aa364b12552d8fd13e45a55e82523cbd145eafc14dc5c94ccd5426497ac3` | `d1004d9af87a9844c997827197316db8614c0b38bb9afb34e4110a3317db3f01` |
| `kb/notes/link-following-and-search-impose-different-metadata-requirements.md` | `892e71f69658e027c9f99bf9000753e90979a97fff4170046199068e80e34ab7` | `b1c3a8665568d68ad7c007c4c7f2433de75e8742a1257de06bb95e7674cb14fb` |
| `kb/notes/links-encode-conditional-possibilities-not-obligations.md` | `1ae06564c3e6abd3a1da46714606d828c934e2419a8d5e37f6928fe58f516df1` | `f5c7e41c2621e16b1a8fbf38733d5bc7b8da9407f63a46693d75bdbd4534790c` |
| `kb/notes/llm-context-interprets-instructions-and-content-through-one-medium.md` | `e346561ba654f829eda4fd56aebbafaf8c8167cfe99e6260d61e5f9c10bdfb4b` | `9ad995851d740e4a87bc62f118523b78dd01d83feeb9e9b5002163fb03e97110` |
| `kb/tags/context-engineering-README.md` | `93b4389c239ba680c7d1fbe134715b41e635e1ca81836613c89e4b5f08052b14` | `93b4389c239ba680c7d1fbe134715b41e635e1ca81836613c89e4b5f08052b14` |
| `kb/tags/reflection-README.md` | `03069f68fe3c0324959e9193e99d32cbd88872bd212486368f798f47a83a4996` | `03069f68fe3c0324959e9193e99d32cbd88872bd212486368f798f47a83a4996` |
| `kb/tags/artifact-analysis-README.md` | `5eb82390efee93f6f45387cb9583c267b3e0a76dd9d31205ca78967d65d44f9e` | `5eb82390efee93f6f45387cb9583c267b3e0a76dd9d31205ca78967d65d44f9e` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/self-improving-systems-README.md` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` |
| `kb/tags/llm-reliability-README.md` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` |
| `kb/tags/document-system-README.md` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` |
| `kb/tags/kb-maintenance-README.md` | `01a93c13dded3a6e13f65199ea21cc8062d18fe091cee0c9471b8903368c9157` | `01a93c13dded3a6e13f65199ea21cc8062d18fe091cee0c9471b8903368c9157` |
| `kb/tags/failure-modes-README.md` | `4fe230c7ba5abf0fa4355dec85ef3d35d8e92ba63be320b18922937dc505c85f` | `b5505ed4356c530e91f0fed5aec5151879472bbe8c5986255fe5d2635eaa687c` |
| `kb/tags/curation-README.md` | `4f2b7b108fdd7e846809eaf6fd2bbc1f886ae1a053869f4e7fc5eeb003507951` | `9edf98764c198ac8ded0a38782fa44b34f05c28552337d13d9c8ada710c40699` |
