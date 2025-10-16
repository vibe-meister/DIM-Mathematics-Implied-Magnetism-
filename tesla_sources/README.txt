Tesla Sources — Directory Structure

./tesla_sources/
  /primary_pdfs/            # Archived PDFs (Colorado Springs Notes, Patents, Lectures)
  /images_figures/          # Extracted figures/schematics with captions and page refs
  /manifests/               # Acquisition manifests (URL, date, checksum, notes)
  /extractions/             # Structured extractions (JSON, CSV) of dimensions/parameters
  /notes/                   # Exhaustive reading notes with citations
  /links/                   # Plaintext link lists to source locations

Intake checklist (each document)
- Save PDF to primary_pdfs/ with canonical name
- Record manifest: URL, access date, SHA256, title, source
- Create extraction stub: parameters to collect (N, R, r, wire, coupling, tuning)
- Snapshot key figures into images_figures/ with page numbers
- Write notes with section/page citations to notes/
