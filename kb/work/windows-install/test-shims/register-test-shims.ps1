param(
    [Parameter(Mandatory=$true)][string]$PythonPath,
    [Parameter(Mandatory=$true)][string]$BinDirectory,
    [string]$SitePackages
)

# Registers one test shim per commonplace-* console entry point that the
# given interpreter can see. Each shim starts that interpreter on the
# dispatcher, which resolves the entry point by name and calls it. No
# uv-generated launcher executable is written to or run from $BinDirectory.
#
# Variant S (signed python.org interpreter, package installed with
# `uv pip install --target <folder>`): pass -SitePackages <folder>; the
# dispatcher adds it with site.addsitedir before importing anything.
# Variant U (uv-managed interpreter of a venv or tool environment that has
# the package installed): omit -SitePackages.

$ErrorActionPreference = 'Stop'
$python = (Resolve-Path -LiteralPath $PythonPath).Path
$bin = [IO.Path]::GetFullPath($BinDirectory)
$site = ''
if ($SitePackages) { $site = (Resolve-Path -LiteralPath $SitePackages).Path }
New-Item -ItemType Directory -Force -Path $bin | Out-Null

$dispatcher = Join-Path $bin 'commonplace-test-dispatch.py'
@'
import os
import site
import sys
from importlib.metadata import entry_points

extra = os.environ.get("COMMONPLACE_TEST_SITE")
if extra:
    site.addsitedir(extra)

command = os.environ.get("COMMONPLACE_TEST_SHIM", "")
matches = [ep for ep in entry_points(group="console_scripts") if ep.name == command]
if not matches:
    raise SystemExit(f"unsupported test shim: {command!r}")

sys.argv = [command, *sys.argv[1:]]
raise SystemExit(matches[0].load()())
'@ | Set-Content -LiteralPath $dispatcher -Encoding UTF8

# The first llm-commonplace distribution on sys.path wins, so an interpreter
# that carries its own copy of the package shadows -SitePackages. The
# registrar reports which distribution the shims will reach.
$query = "import os, site; e = os.environ.get('COMMONPLACE_TEST_SITE'); e and site.addsitedir(e); from importlib.metadata import distribution, entry_points; d = distribution('llm-commonplace'); print('DIST ' + d.version + ' ' + str(d.locate_file(''))); print('\n'.join(sorted(ep.name for ep in entry_points(group='console_scripts') if ep.name.startswith('commonplace-'))))"
$env:COMMONPLACE_TEST_SITE = $site
$lines = @(& $python -c $query | Where-Object { $_ })
Remove-Item Env:COMMONPLACE_TEST_SITE -ErrorAction SilentlyContinue
$dist = ($lines | Where-Object { $_ -like 'DIST *' } | Select-Object -First 1) -replace '^DIST ', ''
$names = @($lines | Where-Object { $_ -notlike 'DIST *' })
if ($LASTEXITCODE -ne 0 -or $names.Count -eq 0) {
    throw "No commonplace-* entry points visible to $python (site-packages: '$site')."
}
if ($site -and $dist -and -not $dist.StartsWith($site, [StringComparison]::OrdinalIgnoreCase)) {
    Write-Warning "The shims will reach llm-commonplace $dist, not the copy under $site. Remove the package from the interpreter's own site-packages or use a clean interpreter."
}

$pyPosix = '/' + $python.Substring(0,1).ToLower() + $python.Substring(2).Replace('\','/')
$dispatcherPosix = '/' + $dispatcher.Substring(0,1).ToLower() + $dispatcher.Substring(2).Replace('\','/')
foreach ($name in $names) {
    $cmdLines = @('@echo off', "set `"COMMONPLACE_TEST_SHIM=$name`"")
    $shLines = @('#!/bin/sh', "export COMMONPLACE_TEST_SHIM='$name'")
    if ($site) {
        $cmdLines += "set `"COMMONPLACE_TEST_SITE=$site`""
        $shLines += "export COMMONPLACE_TEST_SITE='$site'"
    }
    $cmdLines += "`"$python`" `"$dispatcher`" %*"
    $shLines += "exec `"$pyPosix`" `"$dispatcherPosix`" `"`$@`""
    [IO.File]::WriteAllText((Join-Path $bin ($name + '.cmd')), (($cmdLines -join "`r`n") + "`r`n"))
    [IO.File]::WriteAllText((Join-Path $bin $name), (($shLines -join "`n") + "`n"))
}

[pscustomobject]@{
    Python = $python
    SitePackages = $(if ($site) { $site } else { '(interpreter default)' })
    Distribution = $dist
    BinDirectory = $bin
    Count = $names.Count
    Shims = $names
}
