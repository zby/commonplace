# Batch 22 execution-route design review

**Recommend a two-phase, harness-native handoff route, not a new analysis launcher.**
Keep the existing checker read-only. Prepare release records and bounded
per-target coordinator instructions; execute them only after separate authority.
The native CLI already supplies worktree preparation, immutable run allocation,
acquisition and analysis scheduling. It does not supply batch admission,
source selection or an assistant-delegation backend.

This is an advisory review of [batch 22](./batch-22.md) and its
[manifest](./batch-22.json), not authorization to prepare a worktree, install,
acquire, open or advance a run, launch workers, reset, judge, publish or integrate.
Only this review file is owned by this reviewer. Production code, tests and
future execution artifacts remain with their assigned owners. No target sources,
old retained analyses, instantiated worker prompts or logs were inspected.

## Route choice

Prefer parent-authored handoff records consumed through the exposed analytical
harness tool. These are workshop records, not a new native manifest format or
scheduler. Give each fresh coordinator the ordinary canonical skill, its exact
source commission, method revision, new destination and runtime constraints.
Do not give analysts the batch manifest, predecessor metadata, old findings or
audit corrections. Driver-created analytical handoffs remain unchanged.

An **operator-run** shell launcher analogous to [batch 20](./bash-20.sh) is a
possible outer entry point only if separately chosen and authorized by the
operator. It must not become this assistant's substitute for analytical
harness delegation. In particular, do not invoke `pi` through Bash to evade an
unavailable exposed subagent tool. The skill's `prepare -- <command>` option
supports an operator-started fresh harness, but then the preparing session stops;
it is not the same-session continuation route. Do not mix the two routes.

Batch 20 is a useful guard example, not a script to copy wholesale. Its local
historical clone setup contradicts this batch's fresh remote policy. Its
skip-and-continue behavior is weaker than batch 22's stop requirement. Its
process exit files are not analysis verdicts or proof that workers stopped.

## Release before any execution

1. Finish the profile validator/test alignment and required verification in the
   parent's scope. Commit the coherent method before selecting it. The review
   does not establish that this gate has passed. Do not freeze the contract-only
   checkpoint or patch any old prepared method.
2. Select one full committed method revision for the release. Require committed
   code, method/type/plan/profile files, lockfile, build metadata and startup
   instructions. Prefer a clean origin at release; native preparation permits
   unrelated dirty origin files by default, but excludes them. Explicit
   `--require-clean-origin` is supported if this stricter release policy is used.
3. Validate the **entire committed inherited retained corpus**, not just thirteen
   target names. Reuse `current_analyses` and normal validation semantics at the
   selected revision. Require working/index code and corpus to match that
   revision, with no untracked canonical additions; a two-tree diff alone does
   not catch staged/unstaged changes that cancel. Keep the parent-held complete
   byte maps, root-file maps and release bindings. Recheck around admission.
4. Enumerate normalized exact source identities and native publication names.
   Refuse an existing canonical source or another source owning a destination;
   return for a decision rather than silently replacing or marking complete.
   Recheck selected identities after the three selection cases resolve. Native
   opening permits a same-source incumbent replacement; that is not this batch's
   fresh-lineage admission policy. Owner-qualified GitHub names are native;
   custom publication names are not.
5. Establish exclusive ownership of each **new** worktree, sibling preparation
   record, coordinator transcript, result/exit record and eventual publication.
   Require absence including dangling symlinks, canonical non-redirected paths,
   pairwise disjointness and disjointness from every preserved predecessor.
   Recheck the external mount, actual parent permissions and capacity. Existence
   checks are not writer locks: use one admitted writer and exclusive output
   creation, not check-then-truncating redirection. Never reuse a partial output.

The existing [checker](./bash-22.sh) checks preparation bindings and preservation;
it does not prove source suitability, full native corpus validity, writer
idleness or execution authority. Keep it that way. Method selection and changed
binding reconciliation belong in a separate release record, not a mechanical
rewrite of historical evidence to make checks pass.

**ACE and Agent Skills are independent new commissions.** Do not require old
open-attempt closure, reservation release, reset or old-owner reconciliation as
admission conditions. Keep their old workspaces untouched even if still active;
only exclusive, disjoint new writes must be established. This exception does not
clear old incidents or authorize any old-session termination.

## Ten known-source admissions

Nine Git cases are AI-Context-OS, LLM-Wiki-v3, llmwiki-marimo, Siftly, sift-kg,
Fragility Grid, ACE, Agent Skills for Context Engineering and Secure LLM Wiki.
NAMS is the tenth, explicitly a document source. Start serial target admission;
internal rounds follow the native driver. After later execution authority, each
coordinator uses this supported sequence (notation only; not executed here):

```text
From the originating checkout:
commonplace-analysis prepare --name <key> --worktree <new-absolute-path> --revision <method-commit>

From the returned worktree, using its returned path-prefix:
<prefix>/commonplace-analysis start --system <source-native-name> --source-identity <identity> --source <input> --harness pi --worker-profile pi-sol
<prefix>/commonplace-run advance <returned-run>
```

Retain the ready preparation JSON and the exact allocated run path; never
construct a run ID from the proposed path. All later commands use that worktree
and prefix. Native preparation creates a new token and `start` allocates an
unused numbered run directory. The ordinary first advance executes opening and
acquisition before producing the boundary handoff; it is not a read-only probe.

For the nine Git sources use their exact manifest URLs, omit
`--source-revision`, and require the new source destination absent. Native
acquisition clones the remote default tip and freezes its full commit under
`related-systems/<owner>--<repo>`. Do not seed from an old checkout, use local
clones, alternates or shared object stores, or pass the predecessor pin. A
current-tip result is not a controlled same-pin repair experiment. Use the
fresh source-native target for Fragility Grid, not predecessor subsystem
findings as corrective instructions.

For NAMS pass the supplied Neo4j blog URL as an explicitly declared document
input and stable identity; omit `--source-revision`. Native `acquire` returns
JSON `null` for this non-Git identity: it does **not** download or validate the
page. The native boundary worker must create an immutable capture/bundle in its
handout's capture directory, record exact URL, bytes/hash, capture time and
coverage limits, and establish the source register. Later jobs read it read-only.
Do not guess a Git repository or use a previous capture. Additional evidence
must be established explicitly under the boundary rules, not silently substituted.

At every model round, the coordinator uses only the printed prompt paths,
launches fresh workers without parent conversation, and waits for all workers
before reporting exact attempt IDs through `--completed`/`--failed`. Select or
verify the profile model and effort as the driver requires. `pi-sol` is
`gpt-6.1-sol`, medium; the batch's fully qualified coordinator model string is
not itself proof of worker inheritance. If the exposed harness cannot provide
the profile or fresh isolation, stop before starting the run. No Bash agent CLI
fallback, analyst self-delegation or coordinator-authored analytical replacement.

## Three source-selection admissions

Awesome Agent Memory, Letta and Operational Ontology Framework are **not**
launch-ready repository rows. Conduct a separately authorized, bounded
source-selection phase in each target's own new workspace before allocating
its operational analysis. Do not run the full analysis merely to discover
whether an implementation exists. There is no native `select-source` command or
pause-after-selection option; a small parent-held selection record is enough.
No new selection engine or skill enhancement is needed.

The selection handoff may inspect freshly acquired candidate evidence for the
named target. Its deliverable is the concrete source proposal: named system and
normalized identity; implemented boundary and shipped entry points sufficient
to justify suitability; exact repository URL/full commit or capture URL/hash;
fresh acquisition provenance, immutable local path and capture time where
applicable; coverage limits; and proceed/stop/operator-choice disposition.
Keep candidate evidence and failed acquisition records in the new authorized
workspace. Do not open an operational run until these fields are concrete.

- **Awesome Agent Memory:** the catalog's URL identifies the requested target,
  not permission to choose any project it lists. Establish a suitable named
  implementation or retain a selection stop.
- **Letta:** establish an inspectable server implementation and exact revision.
  A landing page or Letta Code is not a substitute. An expressly historical
  server/archive proposal returns to the operator for mapping before analysis;
  do not guess an archive pin.
- **Operational Ontology Framework:** establish the implementation and declared
  boundary; a linked kit is a candidate, not an approved replacement identity.

Any different project identity requires an operator mapping decision before
analysis. No suitable implementation means a retained source-selection stop,
not automatic exclusion, invented source or forced operational review.

After acceptance, pass the concrete identity/source to a fresh operational
coordinator without the predecessor context. For an approved GitHub source,
`start --source-revision <full-40-hex>` binds the selected commit. Acquisition
can verify a clean, matching remote-acquired checkout already in the new
workspace, or acquire that exact commit remotely; do not fetch a new tip after
selection. Native GitHub identity determines the acquisition path. For a
selected document/bundle, supply its concrete immutable source input and require
the native boundary to establish/verify that same pin. There is no CLI document
hash flag; a handoff alone is not an engine-accepted frozen source. If the
ordinary source route cannot preserve the selected evidence unchanged, stop
for an explicit supported route rather than mutating run parameters.

## Failure evidence and unsupported shortcuts

Preserve complete command stdout, stderr, exit status, returned preparation/run
records, engine attempts and acquisition journals. Preparation can install
packages. Installation failure retains its worktree and sibling failure record;
earlier setup failures may occur before such a record exists, so retain the
outer transcript too. Existing paths, preparation/acquisition failure, uncertain
effects or unexpected external writes stop admission; no automatic retry,
cleanup, next-target continuation or old-run recovery. Native Git clone staging
is internally removed on failure; do not promise retention of every transient
clone byte or add a separate wrapper cleanup. Preserve all evidence the native
operation does retain and disclose this limit.

Native interfaces inspected:

- `commonplace-analysis`: `prepare`, `start`, `inspect`, `integrate` only.
  Preparation supports `--name`, `--revision`, `--worktree`,
  `--require-clean-origin` and optional command after `--`.
- `start` supports system, source identity/input, optional source revision,
  worker profile and harness. No run-ID, publication-path, document-hash,
  selection-record, no-install, dry-run or manifest-consumption flag is exposed.
- `commonplace-run advance` submits attempt results and schedules jobs;
  `status` reports state. Neither launches model workers. There is no native
  batch launch or source-selection stage. Generic `start --param` is not a
  reason to bypass the analysis-specific preparation and allocation checks.
- Although generic advance parses model/effort options, this analysis driver
  explicitly forbids them for result submission: the fixed worker profile is
  provenance. `judge` and `reset` exist but are not routine progression or
  fresh-lineage admission tools. `integrate` needs separate authority.

No transient-worker retry authority is assumed. Follow the driver's stop/report
rules unless the later caller explicitly grants its bounded route. Coordinator
failure is outside that route. A zero process exit, `publishable`, completed
local out-of-scope/blocked result or later content pass does not establish
published completion, operational safety or incident clearance. Preserve the
last advance output and final unchanged inspection JSON. New publications need
a new fixed intake, independent exact-byte and operational audit, and separate
integration authorization.

## Evidence boundary

This review read the complete batch-22 plan/manifest, workshop collection and
framing, root delegation rules, canonical analysis skill and driver, worker
profiles, native boundary rules, bash-20/bash-22, CLI declarations and relevant
preparation/start/opening/acquisition/corpus/namespace guards. Supporting code is
`src/commonplace/cli/analysis.py`, `src/commonplace/cli/run.py`,
`src/commonplace/artifactrun/worktree.py`,
`src/commonplace/artifactrun/sources.py`, and
`src/commonplace/lib/agentic_analysis/{worktree,opening,guards,analyses}.py`.
The review does not certify release verification, runtime tool availability,
current source suitability, ownership or destination readiness. No native
operation or execution fixture was run.
