from pathlib import Path

import commonplace

from commonplace.cli.source import main, source_path


def test_source_path_points_at_executing_package() -> None:
    assert source_path() == Path(commonplace.__file__).resolve().parent


def test_main_prints_source_path(capsys) -> None:
    assert main() == 0
    assert capsys.readouterr().out.strip() == str(source_path())
