from pathlib import Path

import commonplace
from commonplace.cli.source import main


def test_main_prints_executing_package_path(capsys) -> None:
    exit_code = main([])
    output = capsys.readouterr().out.strip()

    assert (exit_code, output) == (
        0,
        str(Path(commonplace.__file__).resolve().parent),
    )
