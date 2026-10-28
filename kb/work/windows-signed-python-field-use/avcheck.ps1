param(
    [Parameter(Mandatory=$true)][datetime]$RunStart,
    [string]$NamePattern = 'commonplace|python|\\uv'
)
# Antivirus observation for one window (windows-install round 2 method).
# ASCII only: Windows PowerShell 5.1 reads BOM-less files as ANSI.
# Code Integrity 3033 events from other drivers (e.g. McAfee) flood the log;
# NamePattern selects the ones that concern the install.
$ci = @(Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-CodeIntegrity/Operational'; Id=3033,3077; StartTime=$RunStart} -ErrorAction SilentlyContinue)
$ciNamed = @($ci | Where-Object { $_.Message -match $NamePattern })
$def = @(Get-MpThreatDetection -ErrorAction SilentlyContinue | Where-Object { $_.InitialDetectionTime -ge $RunStart })
$defEv = @(Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Defender/Operational'; Id=1116,1117,1121,1122; StartTime=$RunStart} -ErrorAction SilentlyContinue)
$av = 'C:\ProgramData\Avast Software\Avast'
$chestCount = 'n/a'
$sbNew = @()
if (Test-Path "$av\chest\index.xml") {
    [xml]$chest = Get-Content "$av\chest\index.xml" -Raw
    $chestCount = $chest.DocumentElement.ChildNodes.Count
}
if (Test-Path "$av\log\autosandbox.log") {
    $cur = $null
    foreach ($line in Get-Content "$av\log\autosandbox.log") {
        if ($line -match '^(\d\d\.\d\d\.\d{4} \d\d:\d\d:\d\d)\s+Autosandbox candidate: (.*)$') {
            $t = [datetime]::ParseExact($matches[1], 'dd.MM.yyyy HH:mm:ss', $null)
            $cur = if ($t -ge $RunStart) { "$($matches[1]) $($matches[2])" } else { $null }
        } elseif ($cur -and $line -match 'Result: (.*)$') { $sbNew += "$cur => $($matches[1])"; $cur = $null }
    }
}
"AV[$($RunStart.ToString('yyyy-MM-dd HH:mm'))..$((Get-Date).ToString('yyyy-MM-dd HH:mm'))]: CI any=$($ci.Count) named=$($ciNamed.Count); Defender det=$($def.Count) ev=$($defEv.Count); Avast chest=$chestCount sandbox-new=$($sbNew.Count)"
$ciNamed | ForEach-Object { $first = $_.Message.Split([char]10)[0]; "  CI $($_.Id) $($_.TimeCreated.ToString('yyyy-MM-dd HH:mm:ss')): $($first.Substring(0,[Math]::Min(240,$first.Length)))" }
$sbNew | ForEach-Object { "  SB $_" }
