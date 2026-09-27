# Context and document additions, second larger chunk

## Scope and decision

On 2026-09-27 the operator requested an even larger chunk. This pass reads
thirty entries: all sixteen remaining context-engineering suggestions in stable
queue order, then the first fourteen other open document-system additions.
The duplicate removal suggestion ADD-039 is outside this additions batch.
All proposed assignments in the thirty selected entries meet their live heads.

This completes the context-engineering suggestions in the retained queue,
not an exhaustive missing-tag audit. No inclusion rule changes. The
context-scarcity thought experiment qualifies through its analysis of what
must be precomputed rather than reconstructed in a bounded call. The risk
triad qualifies through its developed recurring-loading-cost analysis. The
first-principles note qualifies for document-system through its explicit
quality checks for written KB notes, not merely because it states theory.

The document cases concern structure, checking, authoring conventions, and
what content to retain. None needs a revised architecture/document-system
boundary. Placement does not certify the notes' claims or reopen grounding.
Note bodies, tag heads, original reviewer wording, and frozen baselines remain
unchanged.

## Accepted entries

| Entry | Note | Reason |
| --- | --- | --- |
| ADD-112 | [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) | Accept context-engineering: the note analyzes flat context composition, contamination, name capture, and the fresh call boundaries that isolate inputs. |
| ADD-115 | [LLM-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) | Accept context-engineering: compaction and externalization are compared as ways to reduce accumulated conversational load and selectively recover transition-relevant state. |
| ADD-117 | [Local materialization should outperform distant natural-language declarations](../../notes/local-materialization-should-outperform-distant-declarations.md) | Accept context-engineering: local rendering of a canonical fact is a prompt-assembly intervention, tested against distance, competing content, and the cost of added tokens. |
| ADD-125 | [Minimum viable vocabulary is the naming set that most reduces extraction cost for a bounded observer](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) | Accept context-engineering: the note selects a vocabulary for a particular bounded observer and context budget, and explicitly distinguishes loading vocabulary into agent sessions from human learning across sessions. |
| ADD-127 | [Model-resolved indirection adds interpretation work to LLM execution](../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) | Accept context-engineering and constraining: the note compares full delivered prompt forms, model-side binding work, and token costs, then explains when upstream resolution narrows valid interpretations. |
| ADD-141 | [Periodic KB hygiene should be externally triggered, not embedded in routing](../../notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) | Accept context-engineering: always-loaded routing and occasional hygiene procedures have different triggers and loading frequencies, so the note argues for loading the latter only when invoked. |
| ADD-158 | [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) | Accept context-engineering: retaining execution history is separated from selecting and assembling the next call context, including goal-specific compression and failure handoffs. |
| ADD-159 | [Short composable notes maximize combinatorial discovery](../../notes/short-composable-notes-maximize-combinatorial-discovery.md) | Accept context-engineering and document-system: co-loading capacity motivates a one-claim writing rule and selective resolution, with explicit limits from argument coherence. |
| ADD-163 | [Specification-level separation recovers scoping before it recovers error correction](../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md) | Accept context-engineering: external state protocols and explicit frame boundaries recover some scoping before scheduling becomes symbolic; the note distinguishes that context benefit from error correction. |
| ADD-169 | [System-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) | Accept context-engineering: the thought experiment tests which heuristic guidance exists to avoid read-time reconstruction under scarce context, distinguishing that role from commitments and independent benefits of symbolic execution. |
| ADD-176 | [The chat-history model trades context efficiency for implementation simplicity](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) | Accept context-engineering: chronological transcript inheritance is compared with selective loading, scoped calls, and task-shaped handoff artifacts under bounded context. |
| ADD-177 | [The four-field record exposes an efficiency, security, and sovereignty risk triad](../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) | Accept context-engineering: the efficiency analysis connects repeated loading of natural-language guidance to token and context costs and asks when a cheaper operational form removes that burden. |
| ADD-186 | [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) | Accept context-engineering: the proposed dependency chain develops fresh scoped calls, shared-context contamination, and the distinct risks of private conversational state and shared mutable state. |
| ADD-191 | [Types give agents structural hints before opening documents](../../notes/types-give-agents-structural-hints-before-opening-documents.md) | Accept context-engineering: type and description metadata let agents select relevant artifacts before loading full documents. |
| ADD-200 | [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) | Accept context-engineering and document-system: cross-note co-loading creates vocabulary collisions, and write-time naming, visible scope, and checking conventions are proposed to keep documents composable. |
| ADD-206 | [Writing styles are strategies for managing underspecification](../../notes/writing-styles-are-strategies-for-managing-underspecification.md) | Accept context-engineering and constraining: five writing styles are analyzed as different restrictions on interpretation, and style choice is tied to the token cost of always-loaded versus on-demand guidance. |
| ADD-009 | [A note is an atomic step relative to the check that reads it](../../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) | Accept document-system: the note distinguishes reader co-loading size from checker-relative inference size and explains how splitting or retained quotations make a document checkable. |
| ADD-049 | [Claim notes should use Toulmin-derived sections for structured argument](../../notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md) | Accept document-system: required Evidence, Reasoning, and Caveats sections turn argument structure into a document contract, with separate structural and semantic checks and an explicit readability cost. |
| ADD-064 | [Directory-scoped types are cheaper than global types](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) | Accept document-system: the note compares global and collection-local document contracts by authoring eligibility, portability, discovery, and validation. |
| ADD-066 | [Document types should be verifiable](../../notes/document-types-should-be-verifiable.md) | Accept document-system: the note specifies which structural promises document types and traits should make, how they are checked, and how semantic misclassification differs from structural failure. |
| ADD-067 | [Attempted recovery identifies informational gaps, not provenance or authority](../../notes/documentation-generates-the-system-rather-than-describing-it.md) | Accept document-system: recovery assays identify which units of documentation can be reconstructed and which rationale or choices need retention, while separating those judgments from provenance and authority. |
| ADD-085 | [First-principles reasoning selects for explanatory-reach over adaptive fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) | Accept document-system: the KB application gives explicit tests for the quality of written theoretical notes beyond structural validity, including premise variation, transfer boundaries, criticism, and observed fit. |
| ADD-108 | [A linked note's durable payload is what its consumption path cannot reliably supply](../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) | Accept document-system: the note gives an explicit segmentation and retention rule for shared framework exposition, local recognition cues, unrecoverable reasons, and inline versus linked content. |
| ADD-131 | [Naur's compiler case tests one historically bounded documentation-and-consumption system](../../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md) | Accept document-system: the note compares ordinary documentation with structured rationale and raw records, and asks which retained content and consumption process can support later program modification. |
| ADD-152 | [Reverse compression is when LLM output expands without adding information](../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) | Accept document-system: the note diagnoses verbose KB writing that adds no reader-accessible structure and proposes a semantic check over the body and its load-bearing links. |
| ADD-157 | [Semantic review catches content errors that structural validation cannot](../../notes/semantic-review-catches-content-errors-that-structural-validation.md) | Accept document-system: structural validation and semantic review are compared as complementary ways to check KB documents, including enumerations, grounding, boundary cases, and internal consistency. |
| ADD-166 | [Structured output is easier for humans to review](../../notes/structured-output-is-easier-for-humans-to-review.md) | Accept document-system: separating Evidence and Reasoning is developed as a document-structure choice that supports independent checks by human readers. |
| ADD-184 | [Title as claim exposes commitments, enabling Popperian maintenance](../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) | Accept document-system: the claim-title writing convention makes a document commitment visible in an index and changes which notes a maintainer must open. |
| ADD-185 | [Title as claim makes overlap between notes visible](../../notes/title-as-claim-makes-overlap-between-notes-visible.md) | Accept document-system: the note explains how claim-title wording exposes overlap between documents before their bodies are read. |
| ADD-190 | [Type system enforces metadata that navigation depends on](../../notes/type-system-enforces-metadata-that-navigation-depends-on.md) | Accept document-system: document types create enforceable metadata obligations that make descriptions available for navigation. |

## Parent checks and accounting

Four original learning-theory gaps close after checking the supporting tags:

- PG-057 / ADD-067: recovering content, establishing production lineage, and
  identifying live authority are explicitly distinguished, with consequences
  for maintenance and disposal. This fits artifact-analysis.
- PG-089 / ADD-131: the compiler-transfer case concerns preserving and
  activating knowledge for coherent modification under later demands,
  fitting deploy-time-learning's inclusion of maintenance responses and their
  limits. The tag does not assert that this transfer succeeded.
- PG-109 / ADD-163: the note distinguishes scoping benefits from hard error
  correction and explains residual unreliable bookkeeping, fitting
  llm-reliability.
- PG-117 / ADD-186: contamination, correlated checks, and independent
  verification are developed as mechanisms affecting agent output errors,
  fitting llm-reliability.

The new constraining assignments on ADD-127 and ADD-206 each require a
learning-theory parent. ADD-191 gains document-system after checking its
existing type-system assignment: it substantively analyzes the structural
promises and document operations used in pre-read routing.

Five accepted document-system suggestions are also required parents of
existing type-system assignments: ADD-049, ADD-064, ADD-066, ADD-166, and
ADD-190. Each directly develops document structure, type scope, reviewability,
or metadata enforcement. Those five are already counted in the suggested
assignments; they are not additional queue entries or PG closures.

This pass adds forty-one assignments across thirty notes: sixteen
context-engineering, seventeen document-system, two constraining, and six
learning-theory. Thirty-four implement suggestions; seven other assignments
supply required parents. No assignments are removed. All eight head inputs
are unchanged: the added subject heads are selective, and learning-theory's
complete head routes through the supported children.

The workshop now records 135 accepted addition entries, three duplicate
removal closures, and 68 open additions. All 68 original placement findings
remain resolved. PC-07 has 43 resolved and 86 open parent-gap entries.

## Verification

`commonplace-validate` passed on thirty-five of the thirty-six changed files
and the tags collection. The remaining note has one pre-existing failure:

- `validation.base.filename-slug`: the Naur compiler-case note's existing
  filename is 87 characters, exceeding the 70-character limit. This batch
  changed its tags only. A separate pure relocation and backlink update is
  needed to repair the filename; it is not a tag-placement disagreement.

There were no other failures and no warnings. Separate checks confirmed
forty-one added assignments, no removals, thirty unchanged note bodies, eight
unchanged heads, preserved reviewer suggestions and evidence links, queue
counts, and all thirty-eight recorded final hashes. No context-engineering
suggestion remains open in the retained queue. `git diff --check` passed.
These are direct semantic judgments, not new independent assays. Changes
remain uncommitted.

## Checked versions

SHA-256 hashes identify the thirty note inputs and eight unchanged heads used.

| Artifact | Before | After |
| --- | --- | --- |
| `kb/notes/llm-context-is-composed-without-scoping.md` | `ccca53c20d93ce86b08bb9ba8770bb9b825cee7d8dae1836e166200c18dbef12` | `1b576c7acb0babe7e76a090f5f95438b410dba31845bea0a8b2d3b050c37328c` |
| `kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` | `f9cc111e7a590c4be7ddb565dffa68e62abecfe967afd482fbacda8a5074bd93` | `31517afc291b721fab9deac04c5387852b8b9006f6e6993534b322dd9e6ea456` |
| `kb/notes/local-materialization-should-outperform-distant-declarations.md` | `3ea7ac326d8de43adeb1a987a888631a3b34823c705c4274fe1dc1fed481a989` | `4687f7c0e5a4523cb856dc2cc99a40e86b6192720e822c2b2953e57c7f1f2845` |
| `kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md` | `7604f60682cd7c4b0a057798c372e5763c6f725d80d4956377081e1e8e8f76af` | `15aefc3f949dcd19b2158b2b4307c257617678cf24addf0751c56ec7cb62e2f2` |
| `kb/notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md` | `cd367ca01913b79e17a64a2587b18fc3a0462b4f992e14d3369dd211923764ed` | `71380049c82112cdb7ddd82dbc8bb3dcb378a4ee2501aff435a1a09995b83b67` |
| `kb/notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md` | `ad403e36e7a0b1ce1b390565b24fbbeaf27b196855ffdd21589f1fee44cd33b8` | `63e87e7927e5f4f8c93cad9e187b3a5023c3490a97452192aef696a241ac7ca1` |
| `kb/notes/session-history-should-not-be-the-default-next-context.md` | `46a7fd191c09d442cc2dc8cb20fce421698623bbadd8b08cd325f80849318e6e` | `8b6d7e6e765907807d81b60d87278f19fde92f10d29defd2d8a927ac326dbd48` |
| `kb/notes/short-composable-notes-maximize-combinatorial-discovery.md` | `7feda13e0b797e328b9a24cc56c4f5c3a9dc2b165e21599ded4ea5327bda2e71` | `1d65b6c73138fe8f48aa1bb98e6df9d0903884c610fa9b53badc29fc7af7b593` |
| `kb/notes/specification-level-separation-recovers-scoping-before-it-recovers.md` | `0681de3805d43066c621236991e2e6ad7a5e09d3f3d149e4a3fc887f6252ade2` | `4c2b03a7c806d12b5d73f74b8f925652d7a04a2311329e387393d6671b54ea21` |
| `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md` | `6a3e8b70612763ec291bd89ed99b93c7f661c335d7147b25b6a4a157fdad787e` | `185e00ffa9057a6f779157ce04b378314dd293d1bde016f4d6958dc94a5854ad` |
| `kb/notes/the-chat-history-model-trades-context-efficiency-for-implementation.md` | `cf85b6b6c90353e3ce0e30f945cd3d58265f38f740beaff4365cc88896ccc868` | `f13e1e080bd2111af969bb9f827d214a7350762750a3e128110454e2cdf6b9dc` |
| `kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md` | `2465221f15d7b8567f502b9397045bb8df74ee06a27e04d5c134064cd60ffd18` | `0b0781f0330fbbbb9eb113a7a08e4b70cb4dcfd28c88ebd72f341dd726dfe0d5` |
| `kb/notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md` | `177c9a921841e9c614629fe325a3ea4bda6eff3b8ef1c19ccba5480584753258` | `883906305f679b155273e62d1cf11cbc4e7de883c04eca63a8d9f203686ab857` |
| `kb/notes/types-give-agents-structural-hints-before-opening-documents.md` | `9d45975f698886dcfced817e6f061a16a9aa3d3ee152bddaa258bfb029ddeea4` | `15ac23b7168d63496468b0541942bf1eab3be56ab8c4196811310dbc7020d666` |
| `kb/notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md` | `20a90c4fb266a4be9d7c1c55f8291e4974197fe6b1b8fa03eb0934d67c8cc693` | `11b22697d264ab60346610498a825839fc98803abc28f14b7ba1a57ee8449164` |
| `kb/notes/writing-styles-are-strategies-for-managing-underspecification.md` | `87d8134fe16e5bf7b7fb5feaa4d7091c45cdf888df18c62506d601da025331b4` | `c4f0cb11d183f87640e1f7378fab9bcdb3bf90e5b6f69ba89ca0218fb8cd4040` |
| `kb/notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md` | `41fc9ddfb0611015a450ff417bab70c5c54244717a123628be60cafb21013a2e` | `569848c8521178b367aa01f75d1879ac65b6153d320680736d4614544934dc07` |
| `kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md` | `212ee23b7cde4f038f1563b8c01c55facab8bf9f6cd5aef158dced252148b075` | `6d2ca8165977e71324282631eea4a8551a97d69e541e1b667a652209dc22ec26` |
| `kb/notes/directory-scoped-types-are-cheaper-than-global-types.md` | `0678fe8880840dc59ea8718e2bdce69beab50997facad4d539b88db45ce4ea8c` | `24227cb6a2f56747259aedef90c275395ddd9b9121e8910f9a17848261517216` |
| `kb/notes/document-types-should-be-verifiable.md` | `fc8f6a499d18501818bbc8ff718540c6a0db6ca4b4e52a4f5f3b78c9144174bb` | `2d62847d3d4a458a7dc98cf8c10cc06eb3dc141338307b08fef246a26acb3494` |
| `kb/notes/documentation-generates-the-system-rather-than-describing-it.md` | `55193fb68fb1678cf6c3d35096680305faba440bce634d2fd0610705066c5cef` | `a7167a6567ba5f4ecbd3011e000510444080a3377513251672327f39b5bd342b` |
| `kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md` | `7b31e476dd1ce1ba4a1b210cfdb81576c7d56de44453f9b268c756368597155d` | `0c5bfd407938e299c6bdcf8708d28f7663b99b9b27f5ffa3740093da00cefedb` |
| `kb/notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md` | `b4d3a8101ac76c7392f62bbc53616b38427741476b5cc6a0e9230bdeff8c64d1` | `6558d74e2bd264d08d1e6b59dc2d0e60554e03c18e63b00b6af62445035af04e` |
| `kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md` | `88398cbb94c93b192ec514db9d02030441af9669d48dd02e0c539d1c6c817174` | `b7e87e9145fcb24f404fd69042820fffc1a34f41c8518c4cf85c22e5e6bf7373` |
| `kb/notes/reverse-compression-is-when-llm-output-expands-without-adding.md` | `91863484c33235ec11790f764709dd212f8dad9d0c692947d67b7170b0a5474b` | `3fb89cea6e5c13976dbe1b379113f67facd45b3280ba1b5ce3d7ee13a00ae4d3` |
| `kb/notes/semantic-review-catches-content-errors-that-structural-validation.md` | `4e313a3293f06bb5d4250fca971459b3c72db6bb77d4c9dce89c19de5828a4b0` | `c317f849525d159cb1734bc6dcce84a9dc439866838955f0ab3162bd45af7fee` |
| `kb/notes/structured-output-is-easier-for-humans-to-review.md` | `21ee0a773c3a7ddf1380aabc8aad7a148ab3651be22ee3b888f942ab6c022a37` | `8cf44b8a1a81d0a6a92b43aa167a5fda85afa34424e70581cc93e439d1b4c292` |
| `kb/notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md` | `9a0370fb695749836f2434f07a86cfc51d48b809401683fddf09871fb509a23a` | `852b9453ba39b1bf3e0498456b53c070ab207cfbd98a3a358f447cd4285f1c3e` |
| `kb/notes/title-as-claim-makes-overlap-between-notes-visible.md` | `fbdedbb4248fe14e0307fab6fc7243199bfc83c7878e0cda79c54d54d17be7b9` | `ec8775f47b7e1dfaa67f6e5f7dc8796d0df275830360443e5f673ef82e9fb9a0` |
| `kb/notes/type-system-enforces-metadata-that-navigation-depends-on.md` | `e724cd20459f22e5bc49f8f0917ce30c2d3ad958205435760a3fb9f8aa64b1d6` | `c30c7e798c94bc15902aa9a6e539be0e6f7bbba9363138fae94e6bb4e14a4fac` |
| `kb/tags/context-engineering-README.md` | `93b4389c239ba680c7d1fbe134715b41e635e1ca81836613c89e4b5f08052b14` | `93b4389c239ba680c7d1fbe134715b41e635e1ca81836613c89e4b5f08052b14` |
| `kb/tags/document-system-README.md` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` |
| `kb/tags/constraining-README.md` | `70c60b9b0b6607144d278ef47998a8fded1381089a4e7e95b04014d1583a232e` | `70c60b9b0b6607144d278ef47998a8fded1381089a4e7e95b04014d1583a232e` |
| `kb/tags/type-system-README.md` | `684298973c1787bb2740278e2cf7b1cfd33cf6ac264cb20b76e7e562c97beb03` | `684298973c1787bb2740278e2cf7b1cfd33cf6ac264cb20b76e7e562c97beb03` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/llm-reliability-README.md` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` |
| `kb/tags/artifact-analysis-README.md` | `5eb82390efee93f6f45387cb9583c267b3e0a76dd9d31205ca78967d65d44f9e` | `5eb82390efee93f6f45387cb9583c267b3e0a76dd9d31205ca78967d65d44f9e` |
| `kb/tags/deploy-time-learning-README.md` | `aaf1c80d74ce43c34c389773e8d6f362460d7e4939f102839bf4399d53437ee1` | `aaf1c80d74ce43c34c389773e8d6f362460d7e4939f102839bf4399d53437ee1` |
