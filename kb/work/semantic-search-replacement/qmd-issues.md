# qmd issues observed

A catalogue of the concrete problems we hit with qmd in Commonplace. Grouped by root cause rather than chronology. Supports the replacement evaluation in `README.md`.

## 1. Sandbox incompatibility

qmd's writable state is scattered across the home directory and the global npm prefix. Agent sandboxes (Codex `workspace-write`) allow writes inside the repo, not under those paths.

- **SQLite sidecar writes fail.** The sandbox could read `~/.cache/qmd/index.sqlite` but could not write WAL / journal / lock sidecar files next to it. Surface error: `SqliteError: unable to open database file — SQLITE_CANTOPEN`. The `qmd-repo-local-setup` workshop moved the SQLite file into `.qmd/` in the repo, which fixes this slice.
- **Hardcoded model cache.** `qmd embed` and `qmd query` require the local embedder, whose model cache path is baked in at `~/.cache/qmd/models`. There is no knob to redirect it per project.
- **node-llama-cpp localBuilds.** The embedder's native build tries to create CUDA / local-build lock directories under the installed qmd npm package (`.../node_modules/node-llama-cpp/llama/localBuilds`). In sandboxes that path is read-only; qmd then falls back to CPU or hangs during rerank.
- **GPU visibility.** qmd expects a visible device. `workspace-write` sandboxes hide GPU device nodes even when CUDA is installed on the host. Fallback behavior is unreliable.

The `.codex/config.toml` in this repo documents the consequence: two extra writable-root entries per machine (`~/.cache/qmd` and the absolute npm-global localBuilds path) just to make qmd quiet.

## 2. MCP daemon introduced as a workaround, with its own bugs

Because the shell qmd path hits the sandbox problems above, we adopted qmd's HTTP MCP daemon (run outside the sandbox, reached by Codex over localhost). That moved the problem rather than fixed it.

- **Issue #343: MCP does not serve `--index <name>` reliably.** The HTTP daemon effectively serves the default `index` database, so the project-specific index has to be mirrored into `~/.config/qmd/index.yml` and `~/.cache/qmd/index.sqlite` before every start. INSTALL.md §5 documents the mirroring dance with `.bak` backups.
- **Single initialized MCP transport per process.** One Codex session can initialize the daemon; a second parallel session may fail during initialize with "Server already initialized" / "error decoding response body". Parallel Codex sessions need separate qmd MCP processes on separate ports. This was the last straw.
- **Index-name gymnastics.** `COMMONPLACE_QMD_INDEX` env var, `--index <name>` flag, default `index` DB, and the mirrored copy all have to agree. Easy to desync.

## 3. Monolithic architecture — embedder coupled to storage

qmd ships its own local embedder (`node-llama-cpp` + gguf models) tightly bound to its storage/search layer. This is the root cause of everything above:

- Can't swap to a CPU-only model. The build chain assumes native compilation.
- Can't swap to an API-backed embedder (OpenAI, Voyage, Cohere, Gemini). No plugin seam exists.
- Can't prepare embeddings offline on a GPU host and ship just the vectors to sandboxed agents.

A tool that separated "turn text into a vector" from "store and search vectors" would not force any of these choices.

## 4. State fragmentation

Before the `qmd-repo-local-setup` workshop, one project's qmd state spanned four locations under two owners:

| Kind | Location | Owner |
|---|---|---|
| Collection config | `~/.config/qmd/<index>.yml` | user |
| SQLite index | `~/.cache/qmd/<index>.sqlite` | user |
| Model cache | `~/.cache/qmd/models/` | user |
| Native localBuilds / locks | `<npm-global>/.../node-llama-cpp/llama/localBuilds/` | root or nvm |

`qmd-repo-local-setup` moved the first two into `config/qmd/` and `.qmd/` in the repo. The other two cannot be moved with current qmd.

## 5. Operational overhead

Small, individually forgivable — together they add up:

- **Two-step refresh.** `qmd update` rescans files but does not regenerate embeddings; you also need `qmd embed`. Skipping embed leaves new docs unqueryable without a clear error.
- **Writer serialization.** Concurrent writers corrupt the SQLite DB; we added `flock "$INDEX_PATH.lock"` to every `update`/`embed` invocation in AGENTS.md.
- **Collection-config install step.** Until the installer is updated, every new project still manually copies `qmd-collections.yml` to `~/.config/qmd/$COMMONPLACE_QMD_INDEX.yml`.
- **Stale asset comments.** The shipped `src/commonplace/assets/qmd-collections.yml` still documents the pre-workshop copy step; the shipped `.envrc.template` still exports `COMMONPLACE_QMD_INDEX`. Every install creates drift.

## Role in context

Taken individually, each issue has a workaround. Taken together, they require:

- two writable-root holes in `.codex/config.toml` per machine,
- an MCP daemon process to bypass the GPU/sandbox problem,
- a mirroring workaround to bypass issue #343,
- one MCP process per parallel Codex session to bypass the single-client bug,
- a repo-local config move that still cannot run `qmd embed` in-sandbox,
- `flock`-protected two-step refresh,
- and an installer update that has not yet happened.

All of this is in service of an optional recall booster in one skill (`cp-skill-connect`). qmd is not load-bearing; the primary discovery path (index scan + `rg`) works without it. The cost / benefit has flipped.
