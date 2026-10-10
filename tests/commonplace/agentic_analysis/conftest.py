"""Register only the immutable baseline; execution fixtures stay explicit."""

from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - fixture registration
)
