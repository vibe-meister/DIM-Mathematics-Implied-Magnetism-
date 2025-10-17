param(
    [string]$OutDir = "$(Split-Path -Parent $MyInvocation.MyCommand.Path)"
)

$src = Join-Path $OutDir 'sources.txt'
if (-not (Test-Path $src)) { Write-Error "sources.txt not found"; exit 1 }

$urls = Get-Content $src | Where-Object { $_ -and ($_ -notmatch '^#') }

$wc = New-Object System.Net.WebClient
$wc.Headers.Add('User-Agent','Mozilla/5.0')

foreach ($u in $urls) {
  try {
    $name = ($u -replace '.*/','')
    if (-not $name.ToLower().EndsWith('.pdf')) { $name = ($name -replace '[^a-zA-Z0-9_.-]','_') + '.pdf' }
    $dest = Join-Path $OutDir $name
    Write-Host "Downloading $u -> $dest"
    $wc.DownloadFile($u, $dest)
  } catch {
    Write-Warning "Failed: $u ($_ )"
  }
}
