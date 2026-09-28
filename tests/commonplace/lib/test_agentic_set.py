from pathlib import Path

from commonplace.lib import agentic_set
from commonplace.lib.note_parser import parse_document


def test_identity_errors_are_reported_per_member() -> None:
    def document(name: str, values: str) -> agentic_set.SetDocument:
        content = f"---\n{values}\n---\n# {name}\n".encode()
        parsed, error = parse_document(content.decode())
        assert error is None and parsed is not None
        return agentic_set.SetDocument(name, Path(name), content, parsed)

    member_set = agentic_set.MemberSet(
        artifact=None,
        overview=document("overview.md", "run-id: R\nreviewed-boundary: B"),
        members={
            "runtime.md": document("runtime.md", "run-id: R\nreviewed-boundary: other"),
            "memory.md": document("memory.md", "run-id: R\nreviewed-boundary: B\nsource-identity: s"),
            "epistemic.md": document("epistemic.md", "run-id: other\nreviewed-boundary: B"),
        },
    )

    assert agentic_set.set_identity_errors(member_set) == [
        "runtime.md: reviewed-boundary does not match the overview",
        "epistemic.md: run-id does not match the overview",
    ]
