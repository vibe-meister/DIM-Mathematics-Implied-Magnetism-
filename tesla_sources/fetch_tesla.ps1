# Requires PowerShell 5+
# Usage: Run from the repository root or from tesla_sources\

param(
  [string]$ManifestsPath = "tesla_sources/manifests",
  [string]$OutputDir = "tesla_sources/primary_pdfs"
)

function Get-Sha256Hex([string]$Path) {
  $hash = Get-FileHash -Algorithm SHA256 -Path $Path
  return $hash.Hash.ToLower()
}

# Ensure output directory exists
$fullOutput = Join-Path -Path (Get-Location) -ChildPath $OutputDir
New-Item -ItemType Directory -Force -Path $fullOutput | Out-Null

# Enumerate manifest JSON files
$fullManifests = Join-Path -Path (Get-Location) -ChildPath $ManifestsPath
$manifestFiles = Get-ChildItem -Path $fullManifests -Filter *.json -File -ErrorAction Stop

foreach ($mf in $manifestFiles) {
  try {
    $jsonText = Get-Content -Raw -Path $mf.FullName
    $manifest = $jsonText | ConvertFrom-Json

    if (-not $manifest.url -or [string]::IsNullOrWhiteSpace($manifest.url)) { continue }
    if (-not $manifest.file -or [string]::IsNullOrWhiteSpace($manifest.file)) { continue }

    $targetPath = Join-Path -Path (Get-Location) -ChildPath $manifest.file
    $targetDir = Split-Path -Path $targetPath -Parent
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

    Write-Host "Downloading: $($manifest.title)" -ForegroundColor Cyan
    Invoke-WebRequest -Uri $manifest.url -OutFile $targetPath -UseBasicParsing -ErrorAction Stop

    $sha = Get-Sha256Hex -Path $targetPath
    $manifest.sha256 = $sha
    $manifest.accessed = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")

    # Save back manifest (pretty JSON)
    $manifest | ConvertTo-Json -Depth 10 | Out-File -FilePath $mf.FullName -Encoding UTF8
    Write-Host "Saved -> $($manifest.file)  SHA256=$sha" -ForegroundColor Green
  }
  catch {
    Write-Warning "Failed: $($mf.Name)  Reason: $($_.Exception.Message)"
  }
}
