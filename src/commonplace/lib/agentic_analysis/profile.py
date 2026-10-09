"""The profile's declared check: a new-engine profile is a version-2 memory comparison.

Content, identity, correction answers and carried limits are the standard
handlers' and the type's; semantic support is the verifier's judgment.
"""

from __future__ import annotations

from commonplace.artifactrun.checks import Candidate


def comparison_version(check: Candidate) -> list[str]:
    """Refuse a profile whose memory comparison is not version 2."""
    if not check.fields:
        return []
    comparison = check.fields.get("memory-comparison")
    if not isinstance(comparison, dict) or type(comparison.get("version")) is not int or comparison["version"] != 2:
        return ["[invocation] new workflow profiles require memory-comparison version: 2"]
    return []
