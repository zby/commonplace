param(
    [Parameter(Mandatory=$true)][string]$PythonPath,
    [Parameter(Mandatory=$true)][string]$BinDirectory
)

$ErrorActionPreference = 'Stop'
$python = (Resolve-Path -LiteralPath $PythonPath).Path
$bin = [IO.Path]::GetFullPath($BinDirectory)
New-Item -ItemType Directory -Force -Path $bin | Out-Null
$dispatcher = Join-Path $bin 'commonplace-test-dispatch.py'
@'
import os
import sys

from commonplace.cli.init_project import main as init_main
from commonplace.cli.validate_notes import main as validate_main

command = os.path.basename(sys.argv[0]).lower()
if command.startswith("commonplace-init"):
    target = init_main
elif command.startswith("commonplace-validate"):
    target = validate_main
else:
    raise SystemExit(f"unsupported test shim: {command}")

sys.argv = [command, *sys.argv[1:]]
raise SystemExit(target())
'@ | Set-Content -LiteralPath $dispatcher -Encoding UTF8

foreach ($name in @('commonplace-init','commonplace-validate')) {
    $cmd = Join-Path $bin ($name + '.cmd')
    $body = "@echo off`r`n`"$python`" `"$dispatcher`" %*`r`n"
    Set-Content -LiteralPath $cmd -Value $body -Encoding ASCII
}

[pscustomobject]@{
    Python = $python
    BinDirectory = $bin
    Shims = @('commonplace-init.cmd','commonplace-validate.cmd')
}
