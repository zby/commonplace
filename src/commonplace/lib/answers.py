"""Answers (`types/answers.md`): the operator's decision on each item of one question file.

A question is a file whose items the operator decides. There are two kinds:

- an edit result (`types/edit-result.md`) with outcome `proposed`: its items
  are its proposals, numbered from 1;
- any other file, a text to approve: its one item, `text`, names the file's
  path and hash.

An answers file names its question by path and SHA-256 and copies each item's
`proposal` unaltered. `pending()` renders the pending file for a question,
with the items the operator already decided for an earlier text carried over.
`problems()` is the part of the acceptance that compares the answers with
their question: the hash and every item present once and unaltered. The
schema checks the rest: the states, a reason on `rejected` and `deferred`, a
revisit condition on `deferred`, and `decided-by: operator` with
`decided-at` on every decided item. The deterministic validator runs both
(`validation.validate_answers`).
"""

from __future__ import annotations

import hashlib

import yaml

from commonplace.lib import frontmatter

TYPE = "types/answers.md"
EDIT_RESULT = "types/edit-result.md"
TEXT_ITEM = "text"
"""The id of the one item of a text to approve."""


def sha(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def question_items(path: str, content: bytes) -> list[dict]:
    """The items of the question file at the repository path `path`; ValueError when it asks nothing."""
    parsed = frontmatter.parse(content.decode("utf-8"))
    data = parsed.data if parsed.ok else {}
    if data.get("type") != EDIT_RESULT:
        return [{"id": TEXT_ITEM, "proposal": {"text": path, "text-sha256": sha(content)}}]
    proposals = data.get("proposals")
    if data.get("outcome") != "proposed" or not isinstance(proposals, list) or not proposals:
        raise ValueError(f"{path}: an edit result is a question only with outcome `proposed`")
    return [{"id": str(index), "proposal": proposal} for index, proposal in enumerate(proposals, 1)]


CARRIED = ("state", "reason", "revisit", "decided-by", "decided-at")
"""The fields a carried-over item copies from the earlier decision."""


def _carried(item: dict, earlier: dict[tuple[str, str], dict]) -> dict:
    """The item `pending`, or decided as before when an earlier decision has the same quote and change."""
    proposal = item["proposal"]
    found = (earlier.get((proposal.get("quote"), proposal.get("change")))
             if isinstance(proposal, dict) and "quote" in proposal and "change" in proposal else None)
    if found is None:
        return {**item, "state": "pending"}
    return {**item, **{field: found[field] for field in CARRIED if found.get(field) is not None},
            "carried-from": found["answers-file"]}


def pending(path: str, content: bytes, earlier: list[dict] = ()) -> str:
    """The answers file for the question at `path`, every item `pending` unless it is carried over.

    `earlier` holds the operator's earlier decisions (`review_workflows.decisions.earlier()`).
    An item whose proposal has the same `quote` and `change` as one of them
    starts decided as before, with `carried-from` naming the earlier answers
    file. The proposal's `reason` is not compared.
    """
    known = {(decision["proposal"]["quote"], decision["proposal"]["change"]): decision for decision in earlier}
    items = [_carried(item, known) for item in question_items(path, content)]
    data = {"type": TYPE, "description": f"The operator's answers to {path}", "question": path,
            "question-sha256": sha(content), "items": items}
    head = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=10**6)
    carried = ("\nItems with `carried-from` hold the operator's decision on the same proposal in the earlier "
               "answers file it names. Change one only on the operator's word, and then remove its "
               "`carried-from`.\n" if any("carried-from" in item for item in items) else "")
    return (f"---\n{head}---\n\n# Answers\n\n"
            "Set each item's `state` on the operator's word: `approved`, `rejected` with a `reason`, or "
            "`deferred` with a `reason` and a `revisit` condition. A decided item also carries "
            "`decided-by: operator` and `decided-at`. Change no `id` or `proposal`.\n" + carried)


def problems(data: dict, content: bytes) -> list[str]:
    """What breaks the answers `data` against the question file's `content`; empty when they match."""
    found = []
    if data.get("question-sha256") != sha(content):
        found.append("question-sha256: the question file has changed since these answers were created; "
                     "create them again from the current question")
    try:
        expected = question_items(str(data.get("question")), content)
    except ValueError as error:
        return found + [str(error)]
    given = [item for item in data.get("items") or [] if isinstance(item, dict)]
    ids = [item.get("id") for item in given]
    found += [f"item {item_id}: appears {ids.count(item_id)} times; each item appears once"
              for item_id in dict.fromkeys(ids) if ids.count(item_id) > 1]
    proposals = {item.get("id"): item.get("proposal") for item in given}
    for item in expected:
        if item["id"] not in proposals:
            found.append(f"item {item['id']}: missing; every item of the question needs an answer")
        elif proposals[item["id"]] != item["proposal"]:
            found.append(f"item {item['id']}: its proposal differs from the question's; change no proposal")
    known = {item["id"] for item in expected}
    found += [f"item {item_id}: not in the question" for item_id in dict.fromkeys(ids) if item_id not in known]
    return found
