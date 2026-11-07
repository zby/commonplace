"""Shared trace-scan result contract; parsing stays with each harness.

The scanners are a provisional implementation pending evaluation of existing
solutions. Keep this boundary small so a replacement can preserve evidence.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

SCHEMA_VERSION = 2
CHECKS = ("tool_failures", "provider_errors", "interruptions", "compactions",
          "permission_denials", "recovery", "output_quality")
OBSERVATIONS = {"provider_errors": "provider_error", "interruptions": "interruption",
                "compactions": "compaction", "permission_denials": "permission_denial"}
LOCATOR_FIELDS = ("line", "entry_id", "block_index", "timestamp")
FINDING_FIELDS = (*LOCATOR_FIELDS, "tool_call_id", "tool_name", "call_line", "arguments", "command")


def trace_result(parsed: dict[str, Any], *, harness: str, checks: tuple[str, ...],
                 branch_scope: str) -> dict[str, Any]:
    """Construct v2 from a parser's private accumulation state, not a v1 reader."""
    issues = list(parsed["input_issues"])

    def text_fields(source: dict, keys: tuple[str, ...], details: dict) -> dict:
        fields = {}
        for key in keys:
            value = source.get(key)
            if value is not None and not isinstance(value, str):
                issues.append({"line": source.get("line"), "message": f"{key} is not a string; retained in details"})
                details.setdefault("invalid_fields", {})[key] = value
                value = None
            fields[key] = value
        return fields

    findings = []
    for failure in parsed["findings"]:
        evidence = []
        for item in failure["evidence"]:
            native = item["signals"]
            signals = list(dict.fromkeys("tool_error" if s in {"isError", "is_error"} else s for s in native))
            details = {"native_signals": native}
            code = item.get("exit_code")
            if code is not None and type(code) is not int:
                issues.append({"line": failure.get("line"), "message": "exit_code is not an integer; retained in details"})
                details["native_exit_code"] = code
                code = None
            evidence.append({
                "signals": signals, "exit_code": code,
                "diagnostic_excerpt": item["diagnostic_excerpt"],
                "diagnostic_truncated": item["diagnostic_truncated"],
                "details": details,
            })
        details = {}
        fields = {key: failure.get(key) for key in FINDING_FIELDS}
        fields.update(text_fields(failure, ("entry_id", "timestamp", "tool_call_id", "tool_name", "command"), details))
        findings.append({"kind": "tool_failure", **fields, "evidence": evidence,
                         "recovery": "not_assessed", "details": details})
    observations = []
    for field, kind in OBSERVATIONS.items():
        for item in parsed.get(field, []):
            details = {k: v for k, v in item.items() if k not in LOCATOR_FIELDS}
            fields = {key: item.get(key) for key in LOCATOR_FIELDS}
            fields.update(text_fields(item, ("entry_id", "timestamp"), details))
            observations.append({"kind": kind, **fields, "details": details})
    details = {key: parsed[key] for key in ("worker_ids", "result") if key in parsed}
    identity = text_fields(parsed, ("session_id", "agent_id", "cwd"), details)
    return {
        "trace": parsed["trace"], "harness": harness, "format": parsed["format"],
        **identity, "tool_results_seen": parsed["tool_results_seen"],
        "coverage": {
            "checks": {key: "supported" if key in checks else "unsupported" for key in CHECKS},
            "input_status": "partial" if issues else "read",
            "branch_scope": branch_scope,
            "last_line": parsed.get("last_line"),
            "first_timestamp": parsed.get("first_timestamp"),
            "last_timestamp": parsed.get("last_timestamp"),
            "cutoff_utc": parsed.get("cutoff_utc") or datetime.now(UTC).isoformat(),
        },
        "findings": findings, "observations": observations, "input_issues": issues, "details": details,
    }


def scan_report(traces: list[dict[str, Any]], *, scope: str,
                input_issues: list[dict[str, Any]] | None = None,
                details: dict[str, Any] | None = None) -> dict[str, Any]:
    """Aggregate observed candidates; no inference about unscanned inputs."""
    return {"schema_version": SCHEMA_VERSION, "scope": scope,
            "finding_count": sum(len(t["findings"]) for t in traces),
            "traces": traces, "input_issues": input_issues or [], "details": details or {}}
