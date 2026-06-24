param(
    [ValidateSet("default", "docs", "hwpx-policy", "normalizer", "renderer", "security", "review")]
    [string]$TaskType = "default"
)

$ErrorActionPreference = "Stop"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$ConfigPath = Join-Path $Root "context_guard.json"

if (-not (Test-Path -LiteralPath $ConfigPath)) {
    Write-Error "Missing context_guard.json at $ConfigPath"
    exit 2
}

$Config = Get-Content -Raw -Encoding utf8 -LiteralPath $ConfigPath | ConvertFrom-Json
$Profiles = $Config.task_profiles
$ProfileNames = @($Profiles.PSObject.Properties.Name)

if ($ProfileNames -notcontains $TaskType) {
    Write-Error "Unknown task type '$TaskType'. Available: $($ProfileNames -join ', ')"
    exit 2
}

$Profile = $Profiles.$TaskType
$EntryFiles = @()
$EntryFiles += @($Config.default_entry_files)
$EntryFiles += @($Profile.entry_files)
$EntryFiles = $EntryFiles | Where-Object { $_ } | Select-Object -Unique

function Test-ContextPath {
    param([string]$RelativePath)

    if ($RelativePath.Contains("*")) {
        return "GLOB"
    }

    $FullPath = Join-Path $Root $RelativePath
    if (Test-Path -LiteralPath $FullPath) {
        return "OK"
    }

    return "MISSING"
}

Write-Host "Project: $($Config.project)"
Write-Host "Task type: $TaskType"
Write-Host "Last reviewed: $($Config.last_reviewed)"
Write-Host ""

Write-Host "Recommended entry files:"
foreach ($Entry in $EntryFiles) {
    $Status = Test-ContextPath -RelativePath $Entry
    Write-Host "[$Status] $Entry"
}

Write-Host ""
Write-Host "Inspect commands:"
foreach ($Command in @($Profile.inspect_commands)) {
    Write-Host "- $Command"
}

Write-Host ""
Write-Host "Default excludes:"
foreach ($Exclude in @($Config.default_exclude_globs)) {
    Write-Host "- $Exclude"
}

Write-Host ""
Write-Host "Stop and ask the user before:"
foreach ($StopRule in @($Config.always_confirm_before)) {
    Write-Host "- $StopRule"
}

Write-Host ""
Write-Host "Always expand when:"
foreach ($Rule in @($Config.expand_when_global)) {
    Write-Host "- $Rule"
}
foreach ($Rule in @($Profile.expand_when)) {
    Write-Host "- $Rule"
}
