# PDFs Index and Download Instructions

This repository organizes downloadable primary-source PDFs per scientist/folder. Each pdfs/ directory includes:
- `sources.txt`: curated URLs (or local references) to PDFs
- `download.ps1`: PowerShell script to fetch PDFs on Windows (non-interactive)

## Maxwell
- Color theory: `scientists/maxwell/color/pdfs/`
- Original works: `scientists/maxwell/original_works/pdfs/`

## Tesla
- Original works: `scientists/tesla/original_works/pdfs/`

## How to download (Windows PowerShell)
```powershell
# Maxwell color
cd "scientists/maxwell/color/pdfs"
./download.ps1

# Maxwell original works
cd "../../original_works/pdfs"
./download.ps1

# Tesla original works
cd "../../../tesla/original_works/pdfs"
./download.ps1
```

Notes:
- Some sources are Archive.org or Royal Society; URLs may redirect. Scripts attempt simple downloads.
- If a site requires manual access, download via browser and place the PDF in the same folder.
