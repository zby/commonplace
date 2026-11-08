"""Inventory GitHub repositories from saved gist comment API pages (no network).

Usage: python3 scripts/triage_gist_repositories.py CAPTURE_DIR --output FILE
Checks contiguous pages and terminal Link headers; hashes exact response bytes.
Coverage is filename-only screening, not verification of an accepted analysis.
Does not launch workers, read analysis reports, or execute linked content.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path

URL = re.compile(r"https?://github\.com/([\w.-]+)/([\w.-]+)", re.IGNORECASE)
RESERVED = {
    "features",
    "topics",
    "collections",
    "marketplace",
    "settings",
    "orgs",
    "users",
    "login",
    "sponsors",
    "notifications",
    "user-attachments",
}


def repositories(text):
    result = {}
    for owner, repo in URL.findall(text):
        repo = repo.rstrip(".")
        repo = repo.removesuffix(".git")
        if owner.lower() not in RESERVED and repo:
            key = f"{owner}/{repo}".lower()
            result[key] = f"https://github.com/{owner}/{repo}"
    return result


def capture_gist_id(comment):
    return comment["url"].split("/gists/", 1)[1].split("/", 1)[0]


def inventory(capture, root, cutoff):
    pages = sorted(capture.glob("page-*.json"))
    if not pages:
        raise ValueError("No page-NN.json files")
    records, seen, manifest, rows = [], set(), [], {}
    for number, path in enumerate(pages, 1):
        if path.stem != f"page-{number:02d}":
            raise ValueError("Noncontiguous page sequence")
        raw = path.read_bytes()
        comments = json.loads(raw)
        headers_path = path.with_suffix(".headers")
        headers = headers_path.read_text()
        if not isinstance(comments, list) or not re.search(r"HTTP/\S+ 200", headers):
            raise ValueError(f"Not a successful API page: {path}")
        has_next = 'rel="next"' in headers
        if has_next != (number < len(pages)):
            raise ValueError(f"Missing next page or pages beyond terminal Link: {path}")
        manifest.append(
            {
                "page": number,
                "comments": len(comments),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "headers_sha256": hashlib.sha256(headers_path.read_bytes()).hexdigest(),
                "response_date": next(
                    (
                        line[5:].strip()
                        for line in headers.splitlines()
                        if line.lower().startswith("date:")
                    ),
                    None,
                ),
            }
        )
        for c in comments:
            if c["id"] in seen:
                raise ValueError(f"Duplicate comment across pages: {c['id']}")
            seen.add(c["id"])
            records.append(c)
            origin = (
                "new"
                if c["created_at"] > cutoff
                else "updated"
                if c["updated_at"] > cutoff
                else "earlier"
            )
            for key, url in repositories(c.get("body") or "").items():
                row = rows.setdefault(
                    key,
                    {
                        "key": key,
                        "url": url,
                        "comments": [],
                        "coverage_paths": [],
                        "old_triage": [],
                        "unresolved_elsewhere": False,
                    },
                )
                row["comments"].append(
                    {
                        "id": c["id"],
                        "url": f"https://gist.github.com/karpathy/{capture_gist_id(c)}?permalink_comment_id={c['id']}#gistcomment-{c['id']}",
                        "created_at": c["created_at"],
                        "updated_at": c["updated_at"],
                        "origin": origin,
                    }
                )
    for relative in [
        "kb/agentic-system-analyses/retained",
        "kb/agentic-systems/reviews",
    ]:
        directory = root / relative
        if directory.exists():
            for path in directory.iterdir():
                slug = path.stem.lower() if path.is_file() else path.name.lower()
                for key, row in rows.items():
                    owner, repo = key.split("/")
                    if slug in {owner + "--" + repo, repo}:
                        row["coverage_paths"].append(str(path.relative_to(root)))
    old_files = list(
        (root / "kb/work").glob("karpathy-gist-agent-memory-review-candidates*.md")
    )
    for path in old_files:
        for key in repositories(path.read_text()):
            if key in rows:
                rows[key]["old_triage"].append(str(path.relative_to(root)))
    holds = repositories(
        (root / "kb/work/agentic-system-completion/targets.md").read_text()
    )
    for key, row in rows.items():
        row["unresolved_elsewhere"] = key in holds
    return {
        "cutoff": cutoff,
        "capture": str(capture),
        "pagination_complete": True,
        "limits": "Non-atomic mutable API capture; edited/deleted comments and bare non-GitHub URLs require separate inspection. Filename matches are coverage leads only; unqualified names can collide.",
        "pages": manifest,
        "comment_count": len(records),
        "new_comments": sum(c["created_at"] > cutoff for c in records),
        "updated_earlier_comments": sum(
            c["created_at"] <= cutoff < c["updated_at"] for c in records
        ),
        "repositories": sorted(rows.values(), key=lambda row: row["key"]),
    }


def dispatch(result, selection, capture, root):
    """Join human selection with public metadata; fail closed on duplicate coverage."""
    rows = {row["key"]: row for row in result["repositories"]}
    selected, seen = [], set()
    for item in selection:
        row = rows[item["key"]]
        stem = item["key"].replace("/", "--")
        meta_path = capture / "repos" / f"{stem}.json"
        readme_path = capture / "repos" / f"{stem}.README.md"
        meta = json.loads(meta_path.read_bytes())
        canonical = meta["full_name"].lower()
        if canonical in seen:
            raise ValueError(f"Duplicate canonical repository: {canonical}")
        seen.add(canonical)
        owner, repo = canonical.split("/")
        matches = list(row["coverage_paths"])
        for relative in [
            "kb/agentic-system-analyses/retained",
            "kb/agentic-systems/reviews",
        ]:
            for name in [owner + "--" + repo, repo]:
                for suffix in ["", ".md"]:
                    path = root / relative / (name + suffix)
                    if path.exists():
                        matches.append(str(path.relative_to(root)))
        holds = repositories(
            (root / "kb/work/agentic-system-completion/targets.md").read_text()
        )
        if matches or row["unresolved_elsewhere"] or canonical in holds:
            raise ValueError(
                f"Selected repository has coverage/ownership lead: {canonical}"
            )
        if (
            meta.get("private")
            or meta.get("disabled")
            or meta.get("archived")
            or not meta.get("size")
        ):
            raise ValueError(
                f"Selected repository is not an active public source: {canonical}"
            )
        readme = readme_path.read_bytes()
        if len(readme) < 200:
            raise ValueError(f"Missing substantive README: {canonical}")
        selected.append(
            {
                **item,
                "url": meta["html_url"],
                "canonical_key": canonical,
                "preparation_label": re.sub(r"[^a-z0-9-]", "-", owner + "-" + repo),
                "default_branch_observed": meta["default_branch"],
                "comments": row["comments"],
                "coverage_paths": [],
                "source_revision": None,
                "worker_profile": "pi-sol",
                "metadata_sha256": hashlib.sha256(meta_path.read_bytes()).hexdigest(),
                "readme_sha256": hashlib.sha256(readme).hexdigest(),
            }
        )
    return selected


def render(result, selected, directory):
    """Render reviewable discovery state and source-only worker inputs."""
    directory.mkdir(parents=True, exist_ok=True)
    urls = [item["url"] for item in selected]
    (directory / "dispatch-urls.txt").write_text("\n".join(urls) + "\n")
    lines = [
        "# Dispatch-ready repository queue",
        "",
        f"Capture: `{result['capture']}`. These are analysis candidates, not verified system findings.",
        "All selected sources returned public repository metadata and a substantive README.",
        "No matching current publication/review filename or completion-workshop ownership was found;",
        "this is identity screening, not proof against every possible alias or external run.",
        "",
        "Use `dispatch-urls.txt` or `dispatch.json` for source inputs. The order is a suggested",
        "first wave (up to 10) followed by a wider queue, not authorization to launch every target.",
        "Do not send selection reasons, inspection questions, old triage or this file to fresh analysts.",
        "Give each worker only its repository URL and the instruction to execute the current",
        "`analyse-agentic-system` skill with default profile `pi-sol`, in its own prepared worktree.",
        "No revision is requested: acquisition freezes the default-branch tip at run time.",
        "This screening did not clone repositories, execute target code or freeze a source commit.",
        "",
        "| # | Canonical source | Selection rationale (a lead) | First inspection question | Gist evidence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for n, item in enumerate(selected, 1):
        comments = ", ".join(f"[{c['id']}]({c['url']})" for c in item["comments"][:3])
        lines.append(
            f"| {n} | {item['url']} | {item['reason']} | {item['question']} | {comments} |"
        )
    lines += ["", "## Source identity notes", ""]
    for item in selected:
        if item["key"] != item["canonical_key"]:
            lines.append(f"- `{item['key']}` redirects to `{item['canonical_key']}`.")
    lines += [
        "",
        "Recheck active writer/run ownership and the committed analysis method before dispatch.",
        "Consult the workshop framing for cross-target scope notes and preparation gates.",
        "",
    ]
    (directory / "dispatch.md").write_text("\n".join(lines))
    chosen = {item["key"]: item for item in selected}
    counts = {}
    lines = [
        "# Repository candidate dispositions",
        "",
        "Generated from the captured thread and filename-based coverage screening.",
        "Every extracted identity has a provisional disposition. Deferred means not selected",
        "for this bounded batch, not a finding that the system is unworthy or unavailable.",
        "Reopen deferred rows when the selected batch is exhausted or a specific mechanism gap needs them.",
        "Sample URLs and support links can remain among deferred rows; extraction is not semantic admission.",
        "",
        "| Repository | Origin | Disposition | Evidence / next decision |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["repositories"]:
        origin = ", ".join(sorted({c["origin"] for c in row["comments"]}))
        if row["key"] in chosen:
            state, why = "recommended", chosen[row["key"]]["reason"]
        elif row["unresolved_elsewhere"]:
            state, why = (
                "owned elsewhere",
                "Completion workshop decision required; do not relaunch.",
            )
        elif row["coverage_paths"]:
            state, why = (
                "coverage lead",
                "; ".join(row["coverage_paths"]) + "; no duplicate run selected.",
            )
        else:
            state, why = (
                "deferred",
                "Outside this bounded selection; source/relevance not fully checked.",
            )
        counts[state] = counts.get(state, 0) + 1
        comment = row["comments"][0]
        lines.append(
            f"| [{row['key']}]({row['url']}) | {origin} | {state} | {why} [comment {comment['id']}]({comment['url']}) |"
        )
    lines[2:2] = [
        "Counts: "
        + ", ".join(f"{key}: {value}" for key, value in sorted(counts.items()))
        + ".",
        "",
    ]
    (directory / "candidates.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capture", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--cutoff", default="2026-06-18T13:26:05Z")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--selection", type=Path, help="Human-authored key/reason/question JSON list"
    )
    parser.add_argument(
        "--dispatch-output",
        type=Path,
        help="Optional selected-source JSON; requires --selection",
    )
    parser.add_argument(
        "--render-dir",
        type=Path,
        help="Render dispatch URLs, queue and dispositions; requires selection",
    )
    args = parser.parse_args()
    if args.render_dir and not args.selection:
        parser.error("--render-dir requires --selection")
    if bool(args.selection) != bool(args.dispatch_output):
        parser.error("--selection and --dispatch-output must be supplied together")
    result = inventory(args.capture, args.root, args.cutoff)
    selected = (
        dispatch(
            result, json.loads(args.selection.read_text()), args.capture, args.root
        )
        if args.selection
        else None
    )
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    if selected is not None:
        args.dispatch_output.write_text(json.dumps(selected, indent=2) + "\n")
        if args.render_dir:
            render(result, selected, args.render_dir)
    print(
        json.dumps(
            {k: v for k, v in result.items() if k not in {"repositories", "pages"}},
            indent=2,
        )
    )
    print(f"repositories: {len(result['repositories'])}")


if __name__ == "__main__":
    main()
