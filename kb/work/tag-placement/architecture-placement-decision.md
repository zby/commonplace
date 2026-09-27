# Architecture and Commonplace architecture

## Operator decision

On 2026-09-26 the operator requested a separate commonplace-architecture tag
and favored qualified names for narrower subjects in the shared tag namespace.
The general [architecture head](../../tags/architecture-README.md) now covers
how responsibilities, state, authority, and interfaces are arranged in
agent-operated KBs and agent runtimes, and the consequences of those choices.
The new [commonplace-architecture head](../../tags/commonplace-architecture-README.md)
covers substantive arrangements, worked cases, and design proposals specific
to Commonplace.

This is a split with overlap: every child member keeps architecture. A
Commonplace-specific example can qualify as a secondary contribution, but a
general design claim does not gain the child merely because Commonplace uses
it or a footer links to its implementation. Reference documentation and ADRs
remain untagged; the child head links them for navigation. Proposals can carry
the tag without implying adoption.

The tags collection contract now advises scope qualifiers where an unqualified
name would overstate the subject. It does not require mechanically expanding
all existing names. The architecture landing distinguishes the general area
and the Commonplace-specific child.

## Reassessment of the three findings

The preceding pass interpreted architecture under its old Commonplace-only
opening. It retained the always-loaded survey for its developed installation
example and removed the tag from runtime diagnosis and skill discovery. The
operator's split supersedes those two removals. All three original assignments
are now retained under the general opening:

| Finding | General architecture fit | Commonplace child? |
| --- | --- | --- |
| TP-008 — runtime diagnosis | Separates scheduling, context assembly, and external services by responsibility and explains how the distinctions locate failures. | No: practitioner mappings describe generic runtimes, not Commonplace's arrangement. |
| TP-010 — always-loaded context | Compares prompt files, capabilities, memory, and configuration as distinct context surfaces. | Yes: the configuration section develops Commonplace's installation-time path resolution as a worked example. |
| TP-054 — skill discovery | Explains how harness-owned discovery crosses a worker context boundary and limits the parent's scoping control. | No: the historical Commonplace skill is the observed case, but its instructions do not establish a separate Commonplace layout or subsystem argument. |

This is a placement judgment, not verification of every platform claim,
historical template spelling, or incident inference in the notes.

## Membership review

All ten live members left after the preceding pass and the two restored
members were read against the two heads. Six receive the child; six retain
only the general tag. Every resulting member meets the general scope.

| Artifact | Result | Inclusion basis |
| --- | --- | --- |
| Canonical files and database authority | Both tags | General authority and substrate distinction, with Commonplace's review subsystem as a scoped authority-transfer witness. |
| Edge ownership and storage choice | Both tags | General edge-key and workload comparison, with a developed account of the Commonplace freshness store and its authority decision. |
| Runtime structure and governance | Both tags | General structural affordances, plus a Commonplace matrix and explicit boundary with the harness-owned scheduler. |
| Always-loaded context mechanisms | Both tags | General context surfaces, plus the installation example described above. |
| Checked inline blocks proposal | Both tags | Proposes authoritative shared instruction blocks and consumer copies for Commonplace's writer workflows. |
| Channel-compiled instructions proposal | Both tags | Proposes changes to Commonplace's instruction compilation and installation boundaries. |
| KB goals in always-loaded context | Architecture | Explains where installation-specific domain goals sit relative to framework defaults; the specific implementation is routed to a separate reference artifact. |
| Generate KB skills at build time | Architecture | Assigns known configuration binding to setup rather than model execution; the Commonplace implementation is a separate linked artifact. |
| AGENTS.md as a control plane | Architecture | Develops general invariant, routing, escalation, and nested-scope placement rules. |
| Instruction specificity and loading frequency | Architecture | Develops the general always-loaded/on-demand hierarchy. |
| Runtime diagnosis | Architecture | Separates runtime responsibilities; restored under the broader scope. |
| Skill discovery | Architecture | Analyzes a context boundary crossed by harness discovery; restored under the broader scope. |

The child head retains the current-state routes previously held by the general
head. The general head keeps general design entries and routes to the child.
Existing architecture URLs remain valid. Archived proposal tags and workshop
fixtures are outside live membership and remain unchanged. This check did not
expand into a missing-tag audit of the rest of the KB.

## Related additions and hierarchy

The preceding pass's additions remain accepted:

| Entry | Accepted tags | Basis |
| --- | --- | --- |
| ADD-032 | context-engineering | Context assembly, retrieval, and framing are an explicit responsibility in the runtime diagnosis. |
| ADD-036 | context-engineering, agent-memory | The survey compares ambient and on-demand loading under one budget, and separately compares three cross-session memory write policies. |
| ADD-160 | context-engineering | Per-worker discovery changes call-visible instructions; the mitigations change the worker brief. |

The survey retains learning-theory as agent-memory's parent. All six
commonplace-architecture members already carry architecture. PC-08 records
that relation as resolved. No new parent gap is introduced, and the 128 open
entries in PC-07's original inventory are unchanged.

## Verification

The tag collection and every edited artifact except the collection contract
passed `commonplace-validate` with zero failures and zero warnings. Direct
validation of `kb/tags/COLLECTION.md` reports one failure: `frontmatter.type is
required for files with frontmatter`. Its existing `participating` metadata is
unchanged; collection contracts are excluded from the normal artifact scan.
This records the direct-file validation limitation rather than adding an
artifact type to the contract. `commonplace-validate tags` passed.

Membership checks confirm twelve parent members and six child members, with
no missing architecture parent. Status checks confirm 38 findings resolved
(35 retained, three corrected), 30 open, eleven addition entries accepted,
and 195 open. The existing 128 parent gaps are unchanged.
`git diff --check` passed. This pass changes Markdown only.

Stored placement reviews and the frozen baseline retain
the original scope and wording; this disposition is not a fresh independent
assay. Member arguments remain unchanged: edits to those artifacts are only
in tag metadata.

## Input versions

SHA-256 of all twelve resulting parent members, both architecture heads, the
other heads used for accepted additions, and the updated tag naming contract.

| Input | SHA-256 |
| --- | --- |
| `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md` | `af27c3ca68deceb00f08b6ab609599abdd392d33d2c20b5389c208c25eb3d5b1` |
| `kb/notes/agents-md-should-be-organized-as-a-control-plane.md` | `ab569658aef9a3a4a246b19d28118046da4ba5c20cf905a92ebc2a9f532f5184` |
| `kb/notes/always-loaded-context-mechanisms-in-agent-harnesses.md` | `50071eb85ecdcbada9039c3c7624fcf102ae670374d9f8abc9e744aa94e8fb67` |
| `kb/notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md` | `c604fc15965ac1053acc8c08d924f0bfee6b4cdc8d124096147a83b8db94d85a` |
| `kb/notes/generate-instructions-at-build-time.md` | `86440946e30aade14ea3839222c6532b0bb8f5388cc7464459743e777c61912c` |
| `kb/notes/instruction-specificity-should-match-loading-frequency.md` | `394ff2c3f619b34c933f16b7162a7d6910bf1b44eb24094ec84c85d05ded6195` |
| `kb/notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md` | `ca272742a78a66b3b8a423409772785953904557558102f114acf5689d5d1c36` |
| `kb/notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md` | `56f1b9c75b4ba191c22a0ae7f334bbe79a45bfd5db2aaf319c5c4e17499a9b9c` |
| `kb/notes/runtime-structure-determines-governance-control-surfaces.md` | `624bd82b4979511c1df10422d612964ca0588dad98fed4dfd776d9404a8bb99c` |
| `kb/notes/skill-discovery-re-fires-in-every-sub-agent-context.md` | `4ddd30690542ed1ce091ac52156266b3204630bf46a00eab30a42dc3c4db812f` |
| `kb/reference/proposals/channel-compiled-instruction-artifacts.md` | `18264da3e3cffa4a6691cd59bece36a56f364ad3c9ac7595ac29cc3566841984` |
| `kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md` | `4cb400c4aed8b0345e069e3051fe8ea8eb197a8ff352c7e9495b4452ea960c5e` |
| `kb/tags/architecture-README.md` | `bec434d109605ed794509aaa9e07286cb9f51265844501cb0560e3eb54024561` |
| `kb/tags/commonplace-architecture-README.md` | `029b09d0fd56a4cec147e2557c9aadfb2a2bfe73c39a3f394fe465f252dc85f2` |
| `kb/tags/context-engineering-README.md` | `fa3e8c4eedfc0e222b21c5137986a296815ed881012447e8a2132460cc2d9955` |
| `kb/tags/computational-model-README.md` | `482d1626ac250dae25eb0247e4136d3ab9bbb06bcd9220d1ea68ff0a08d33bf8` |
| `kb/tags/agent-memory-README.md` | `d5d29a14971f9ef2cf4e623a1a5ac96b357061522d45990841018c1c557677e2` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/COLLECTION.md` | `d0710c6bcfab839d6c2465cdd4d8c86471391b34c6d122931b27e161cce8f7cb` |
