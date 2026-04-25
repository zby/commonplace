# ARIS Artifact Inventory

## Summary

ARIS can produce artifacts under `kb/work/<somedir>/`, but there are two different cases:

1. **Research Wiki helper only** - already path-configurable. `research_wiki.py` takes an explicit `<wiki_root>`, so it can write directly to `kb/work/<somedir>/research-wiki`.
2. **Full ARIS skills** - mostly project-root-relative. The skills assume paths like `research-wiki/`, `idea-stage/`, `refine-logs/`, `review-stage/`, `paper/`, `figures/`, `MANIFEST.md`, `findings.md`, and `.aris/` relative to the active project root.

So the cleanest full-ARIS experiment is to make a nested ARIS project inside `kb/work/<somedir>/` and run ARIS from that directory. The cleanest incremental experiment is to call path-configurable helpers from the commonplace repo root.

## Verified Research Wiki Helper Artifacts

Initialized with:

```bash
python3 related-systems/wanshuiyin--Auto-claude-code-research-in-sleep/tools/research_wiki.py \
  init kb/work/research-wiki-integration/aris-trial/research-wiki
```

This produced:

```text
kb/work/research-wiki-integration/aris-trial/research-wiki/
  claims/
  experiments/
  gap_map.md
  graph/
    edges.jsonl
  ideas/
  index.md
  log.md
  papers/
  query_pack.md
```

Manual paper ingest produced:

```text
kb/work/research-wiki-integration/aris-trial/research-wiki/papers/vaswani2017_attention_all_you.md
```

The paper page schema is:

- frontmatter: `type`, `node_id`, `title`, `authors`, `year`, `venue`, `external_ids`, `tags`, `added`
- sections: one-line thesis, problem/gap, method, key results, assumptions, limitations/failure modes, reusable ingredients, open questions, claims, connections, relevance

Observed rough edge: the generated `query_pack.md` did not include the manual thesis because the helper looks for `# One-line thesis` while the page renderer writes `## One-line thesis`. If we use the helper directly, this is a small local patch or upstream issue to track.

## Full ARIS Workflow Artifacts

From the ARIS output-versioning protocol and core workflow skills, the main write surfaces are:

```text
CLAUDE.md
findings.md
MANIFEST.md

.aris/
  installed-skills.txt
  meta/events.jsonl
  meta/optimizations.jsonl
  meta/backups/
  traces/<skill>/<date>_run<NN>/

research-wiki/
  index.md
  log.md
  gap_map.md
  query_pack.md
  papers/
  ideas/
  experiments/
  claims/
  graph/edges.jsonl

idea-stage/
  IDEA_REPORT.md
  IDEA_REPORT_<timestamp>.md
  IDEA_CANDIDATES.md
  REF_PAPER_SUMMARY.md
  docs/research_contract.md

refine-logs/
  FINAL_PROPOSAL.md
  EXPERIMENT_PLAN.md
  EXPERIMENT_TRACKER.md
  EXPERIMENT_RESULTS.md
  PIPELINE_SUMMARY.md
  REVIEW_SUMMARY.md
  REFINEMENT_REPORT.md
  REFINE_STATE.json
  round_N_*.md

review-stage/
  AUTO_REVIEW.md
  REVIEW_STATE.json

paper/
  main.tex
  sections/*.tex
  references.bib
  math_commands.tex
  main.pdf
  PAPER_IMPROVEMENT_LOG.md
  PROOF_AUDIT.{md,json}
  PAPER_CLAIM_AUDIT.{md,json}
  CITATION_AUDIT.{md,json}
  .aris/assurance.txt
  .aris/audit-verifier-report.json

figures/
  latex_includes.tex
  specs/*.json
  *.svg
  *.pdf
  *.mmd
  *.png
  ai_generated/*.png
```

Not every run writes every path. The paper artifacts appear only if the paper-writing workflow is used. `.aris/meta` appears if hooks/meta-optimization are enabled. `research-wiki/` appears when initialized.

## Configurability Assessment

| Surface | Redirectable now? | Notes |
|---|---|---|
| `research-wiki/` helper | Yes | All helper subcommands take `wiki_root`. |
| `verify_wiki_coverage.sh` | Yes | Takes `<wiki_root>` and explicit scan paths. |
| `idea-stage/`, `refine-logs/`, `review-stage/` | Indirectly | Skills hardcode these relative paths, but if the ARIS project root is `kb/work/<somedir>/`, they stay contained there. |
| `paper/`, `figures/` | Indirectly | Same: root-relative to the active ARIS project. |
| `MANIFEST.md`, `findings.md`, `CLAUDE.md` | Indirectly | Full ARIS assumes these live at project root. In a nested ARIS project, that means `kb/work/<somedir>/MANIFEST.md`, etc. |
| `.aris/` traces/meta/install manifest | Indirectly | Installer and hooks write under project-root `.aris/`. Keep contained by using a nested project root. |
| `tools/research_wiki.py` calls inside skills | Needs handling | Skills often say `python3 tools/research_wiki.py ...`. The installer symlinks skills, but does not copy `tools/`; a nested project needs either a `tools/` symlink/copy or wrapper instructions using the absolute ARIS repo path. |

## Containment Options

### Option A: Nested ARIS Project

Use `kb/work/<somedir>/` as the ARIS project root:

```text
kb/work/<somedir>/
  CLAUDE.md
  MANIFEST.md
  findings.md
  .aris/
  .claude/skills/
  tools/                  # symlink/copy/wrapper to ARIS tools if needed
  research-wiki/
  idea-stage/
  refine-logs/
  review-stage/
  paper/
  figures/
```

Pros:

- Tests full ARIS with minimal conceptual rewriting.
- Keeps most artifacts contained under `kb/work/<somedir>/`.
- Preserves ARIS names like `query_pack.md`, so the subsystem trial is faithful.

Cons:

- Skill discovery may require launching the agent from the nested directory, depending on the harness.
- ARIS installer is Claude-Code-oriented and writes `.claude/skills`, not commonplace skill metadata.
- `tools/` must be made available inside the nested project or commands adjusted.
- The nested `CLAUDE.md`/`.aris` layer is a project inside a project.

### Option B: Commonplace Wrapper

Keep ARIS installed/available at the repo root, but provide a wrapper instruction:

```text
ARIS_WORKDIR=kb/work/<somedir>
ARIS_WIKI=kb/work/<somedir>/research-wiki
ARIS_TOOLS=related-systems/wanshuiyin--Auto-claude-code-research-in-sleep/tools
```

The wrapper tells agents to call:

```bash
python3 "$ARIS_TOOLS/research_wiki.py" init "$ARIS_WIKI"
python3 "$ARIS_TOOLS/research_wiki.py" ingest_paper "$ARIS_WIKI" ...
```

Pros:

- No nested skill installation required.
- Keeps commonplace in control of paths.
- Good for testing Research Wiki and lifecycle helpers first.

Cons:

- Does not faithfully exercise full ARIS skill behavior.
- Requires adapting hardcoded skill references one by one.
- Less evidence about whether ARIS works as a coherent subsystem.

## Recommendation

Use both paths:

1. For Track A, create a nested ARIS project under `kb/work/<somedir>/` and run full ARIS there. This tests whether ARIS should remain as a subsystem.
2. For Track B, use direct helper calls with explicit paths from the commonplace root. This lets us import individual mechanisms without adopting the whole root-relative workflow.

Do not install ARIS into the commonplace repo root until we decide whether root-level `.aris/`, `.claude/skills`, `MANIFEST.md`, `idea-stage/`, `paper/`, and `figures/` are acceptable. They are probably too noisy for the main repo root.
