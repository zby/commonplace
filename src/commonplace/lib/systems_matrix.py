"""Parse agent-memory-system reviews into comparison-matrix rows.

Pure parsing logic for the systems matrix (``kb/agent-memory-systems/systems.csv``).
Text-in, row-out, so it is unit-testable; the CLI runner
(``scripts/build_systems_matrix.py``) owns file discovery, the identity join, and
CSV writing. Stdlib only (ADR-008 — the package carries no runtime deps).

The matrix is **faithful**: multi-valued axes are one-hot indicator columns
(``1`` present / ``0`` assessed-absent / ``''`` not assessed or assessed-unknown),
authored as a set of backticked tokens after a lead label, e.g.::

    **Read-back signal:** `coarse` `identifier` `inferred / embedding` — …

Values come only from authored lead tokens, never guessed; an applicable axis
with no lead token is left blank and flagged, which makes the flag list the
precise retrofit worklist. A lead line containing only ``not-determinable`` is
treated as assessed-unknown: it leaves the axis blank without flagging. See
kb/agent-memory-systems/types/agent-memory-system-review.md for the authoring
contract.
"""
from __future__ import annotations

import re
from pathlib import Path

NOT_DETERMINABLE = "not-determinable"
# Assessed-absent sentinel: the reviewer looked and found none of the axis values
# apply. Distinct from `not-determinable` (assessed-unknown -> blank) and from an
# omitted line (retrofit gap -> flag). `none` records an explicit 0 across the
# whole axis, so "verified no curation" stays distinct from "not assessed".
NONE_TOKEN = "none"

# --- single-valued lead tokens (one column, one backticked value) -------------
SINGLE_VOCAB = {
    "storage_substrate": ("Storage substrate",
        {"files", "repo", "sqlite", "rdbms", "vector", "graph", "kv",
         "in-memory", "prompt-registry", "model-weights", "service-object"}),
    "read_back_direction": ("Read-back", {"pull", "push", "both"}),
}

# --- one-hot axes: column -> the controlled backticked token it fires on -------
# Applicability decides whether a missing token is flagged (worklist) or simply
# left blank (axis does not apply to this system).
FORM = {"form_prose": "prose", "form_symbolic": "symbolic", "form_parametric": "parametric"}

ONEHOT_AXES = {
    "Lineage": {
        "lin_authored": "authored", "lin_imported": "imported",
        "lin_trace_extracted": "trace-extracted"},
    "Behavioral authority": {
        "auth_knowledge": "knowledge", "auth_instruction": "instruction",
        "auth_enforcement": "enforcement", "auth_routing": "routing",
        "auth_validation": "validation", "auth_ranking": "ranking",
        "auth_learning": "learning"},
    # write side: agency is universal; curation operations gate on automatic agency.
    # Keep "Write agency" before "Curation operations" so wa_automatic is parsed
    # before the curation-ops applicability check reads it.
    "Write agency": {"wa_manual": "manual", "wa_automatic": "automatic"},
    "Curation operations": {
        "op_consolidate": "consolidate", "op_dedup": "dedup",
        "op_evolve": "evolve", "op_synthesize": "synthesize",
        "op_invalidate": "invalidate", "op_decay": "decay",
        "op_promote": "promote"},
    "Read-back signal": {
        "sig_coarse": "coarse", "sig_identifier": "identifier",
        "sig_inferred_lexical": "inferred / lexical",
        "sig_inferred_embedding": "inferred / embedding",
        "sig_inferred_judgment": "inferred / judgment"},
    "Trace source": {
        "ts_session_logs": "session-logs", "ts_tool_traces": "tool-traces",
        "ts_event_streams": "event-streams", "ts_trajectories": "trajectories"},
    "Learning scope": {
        "ls_per_task": "per-task", "ls_per_project": "per-project",
        "ls_cross_task": "cross-task"},
    "Learning timing": {
        "lt_online": "online", "lt_offline": "offline", "lt_staged": "staged"},
    "Distilled form": {
        "df_prose": "prose", "df_symbolic": "symbolic", "df_parametric": "parametric"},
}

# Axes applicable only to push/both read-back, to trace-derived systems, and to
# systems with automatic write agency, respectively.
PUSH_AXES = {"Read-back signal"}
TRACE_AXES = {"Trace source", "Learning scope", "Learning timing", "Distilled form"}
AUTOMATIC_AXES = {"Curation operations"}

COLUMNS = [
    # identity / meta
    "system_name", "review_file", "public_repo", "clone_path",
    "one_line", "source_tier",
    # artifact analysis
    "storage_substrate",
    "representational_form", *FORM,
    *ONEHOT_AXES["Lineage"],
    *ONEHOT_AXES["Behavioral authority"],
    # write side
    *ONEHOT_AXES["Write agency"],
    *ONEHOT_AXES["Curation operations"],
    # trace-derived learning
    "trace_derived",
    *ONEHOT_AXES["Trace source"],
    *ONEHOT_AXES["Distilled form"],
    *ONEHOT_AXES["Learning scope"],
    *ONEHOT_AXES["Learning timing"],
    # read-back
    "read_back_direction", "rb_pull", "rb_push",
    *ONEHOT_AXES["Read-back signal"],
    "rb_faithfulness_tested",
    "read_back_notes",
]

# Columns the parser owns (recomputed every run). Everything else is
# hand-classified and preserved across runs by the CLI.
_PARSED_ONEHOT = [c for cols in ONEHOT_AXES.values() for c in cols] + list(FORM)
PARSED = {
    "system_name", "review_file", "source_tier", "one_line",
    "storage_substrate", "representational_form",
    "read_back_direction", "read_back_notes", "rb_pull", "rb_push",
    "rb_faithfulness_tested",
    "trace_derived",
    *_PARSED_ONEHOT,
}
JOINED = {"public_repo", "clone_path"}

VOCAB = {k: v for k, (_, v) in SINGLE_VOCAB.items()}

_H1 = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
_TAGS = re.compile(r"^tags:\s*\[([^\]]*)\]", re.MULTILINE)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _btok(value: str) -> str:
    """Regex matching a backticked controlled token, tolerant of internal spacing."""
    return "`" + re.escape(value).replace(r"\ ", r"\s*") + "`"


def _tokens(line: str) -> list[str]:
    return [t.strip() for t in re.findall(r"`([^`]+)`", line)]


def _is_assessed_unknown(label: str, line: str, flags: list[str]) -> bool:
    tokens = _tokens(line)
    if NOT_DETERMINABLE not in tokens:
        return False
    if tokens == [NOT_DETERMINABLE]:
        return True
    flags.append(f"{label}: `{NOT_DETERMINABLE}` cannot be mixed with controlled values")
    return False


def _is_assessed_none(label: str, line: str, flags: list[str]) -> bool:
    tokens = _tokens(line)
    if NONE_TOKEN not in tokens:
        return False
    if tokens == [NONE_TOKEN]:
        return True
    flags.append(f"{label}: `{NONE_TOKEN}` cannot be mixed with controlled values")
    return False


def extract_token(label: str, text: str) -> str:
    """Value of a ``**Label:** `token``` lead token, or '' if absent."""
    m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*`([^`]+)`", text)
    return m.group(1).strip() if m else ""


def _lead_line(label: str, text: str) -> str | None:
    """The remainder of the line after ``**Label:**``, or None if absent."""
    m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.+)", text)
    return m.group(1) if m else None


def _onehot(label: str, cols: dict[str, str], text: str, applicable: bool,
            row: dict[str, str], flags: list[str]) -> None:
    """Set a one-hot axis from its authored lead-token line.

    applicable=False -> leave blank (axis does not apply). applicable=True with no
    lead token -> blank + flag (retrofit worklist). Present -> 1/0 across the vocab.
    A sole `not-determinable` token means assessed-unknown and leaves the axis blank.
    A sole `none` token means assessed-absent and sets every column to 0.
    """
    if not applicable:
        return
    line = _lead_line(label, text)
    if line is None:
        flags.append(f"{label}: missing lead token")
        return
    if _is_assessed_unknown(label, line, flags):
        return
    if _is_assessed_none(label, line, flags):
        for col in cols:
            row[col] = "0"
        return
    matched = False
    for col, value in cols.items():
        hit = bool(re.search(_btok(value), line))
        row[col] = "1" if hit else "0"
        matched = matched or hit
    if not matched:
        flags.append(f"{label}: lead token has no controlled value")


def empty_row() -> dict[str, str]:
    return {c: "" for c in COLUMNS}


def parse_review_text(text: str, review_file: str, source_tier: str) -> tuple[dict[str, str], list[str]]:
    """Extract the parsed fields from one review's text. Returns (row, flags)."""
    flags: list[str] = []
    row = empty_row()
    row["review_file"] = review_file
    row["source_tier"] = source_tier

    h1 = _H1.search(text)
    row["system_name"] = h1.group(1).strip() if h1 else Path(review_file).stem

    # one-line description from frontmatter, stripped of the "<Name> review:" prefix
    # the reviews conventionally lead with (127/129) so the human table reads cleanly.
    md = re.search(r'^description:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
    one_line = md.group(1).strip() if md else ""
    one_line = re.sub(r"^.{0,40}?\breview:\s*", "", one_line, count=1, flags=re.IGNORECASE)
    row["one_line"] = one_line

    tags = set()
    mt = _TAGS.search(text)
    if mt:
        tags = {t.strip() for t in mt.group(1).split(",") if t.strip()}
    trace_derived = "trace-derived" in tags
    row["trace_derived"] = "yes" if trace_derived else "no"
    # Targeting (coarse vs instance) lives in the Read-back signal one-hots; there is
    # no separate push_engineered flag — an `instance` signal *is* a targeted push.

    # single-valued lead tokens + vocab flagging
    for col, (label, vocab) in SINGLE_VOCAB.items():
        v = extract_token(label, text)
        row[col] = v
        if not v:
            flags.append(f"{col}: missing")
        elif v not in vocab:
            flags.append(f"{col}: off-vocab `{v}`")

    # read-back justification + direction one-hot (kills the `both` bucket)
    mrb = re.search(r"\*\*Read-back:\*\*\s*`[^`]+`\s*[—-]+\s*(.+)", text)
    if mrb:
        row["read_back_notes"] = mrb.group(1).strip()
    direction = row["read_back_direction"]
    is_push = direction in ("push", "both")
    if direction in ("pull", "push", "both"):
        row["rb_pull"] = "1" if direction in ("pull", "both") else "0"
        row["rb_push"] = "1" if direction in ("push", "both") else "0"

    # representational form: one-hot components; derive a compact component list
    line = _lead_line("Representational form", text)
    if line is None:
        flags.append("Representational form: missing lead token")
    elif _is_assessed_unknown("Representational form", line, flags):
        pass
    else:
        present = []
        for col, value in FORM.items():
            hit = bool(re.search(_btok(value), line))
            row[col] = "1" if hit else "0"
            if hit:
                present.append(value)
        if present:
            row["representational_form"] = ";".join(present)
        else:
            flags.append("representational_form: lead token has no controlled value")

    # generic one-hot axes
    for label, cols in ONEHOT_AXES.items():
        applicable = True
        if label in PUSH_AXES:
            applicable = is_push
        elif label in TRACE_AXES:
            applicable = trace_derived
        elif label in AUTOMATIC_AXES:
            applicable = row.get("wa_automatic") == "1"
        _onehot(label, cols, text, applicable, row, flags)

    # faithfulness tested (single yes/no), applicable to push/both
    if is_push:
        ft = extract_token("Faithfulness tested", text)
        if ft in ("yes", "no"):
            row["rb_faithfulness_tested"] = ft
        elif ft == NOT_DETERMINABLE:
            line = _lead_line("Faithfulness tested", text) or ""
            _is_assessed_unknown("Faithfulness tested", line, flags)
        elif ft:
            flags.append(f"rb_faithfulness_tested: off-vocab `{ft}`")
        else:
            flags.append("Faithfulness tested: missing lead token")

    return row, flags
