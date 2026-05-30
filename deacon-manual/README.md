# Phoenix Tabernacle Deacon Manual

A print-ready PDF of the Deacon Manual, generated from Python + HTML/CSS and
rendered with [WeasyPrint](https://weasyprint.org/). The content lives in small
Python modules that each return HTML strings; `build.py` stitches them together
and paints the result to a PDF. The three diagrams (floor map, funeral
sanctuary flow, parking-lot order) are hand-written inline SVG.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate   # optional but recommended
pip install -r requirements.txt
python build.py
```

The PDF is written to `output/Phoenix_Tabernacle_Deacon_Manual.pdf`
(along with `output/manual.html`, the intermediate WeasyPrint renders from).

WeasyPrint needs a few native libraries (Pango/Cairo). If `pip install` alone
isn't enough on your machine:

- **macOS:** `brew install pango`
- **Debian/Ubuntu:** `sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf-2.0-0 libffi-dev`
- **Windows:** see the WeasyPrint install docs (GTK runtime).

Fonts are bundled in `assets/fonts/` and wired up via `@font-face` in
`assets/book.css`, so **no system font installation is required** — the build
is self-contained and reproducible.

## Layout

```
deacon-manual/
├── build.py              # entry point: assembles HTML, renders the PDF
├── requirements.txt
├── assets/
│   ├── book.css          # all styling + @font-face rules
│   └── fonts/            # Poppins, EB Garamond, Cinzel (bundled)
├── data/
│   ├── deacon_en.txt     # verbatim source text (read by src/verbatim.py)
│   └── Deacon_Manual_2007_Final-English.pdf   # original 2007 source
├── output/               # generated PDF + manual.html (gitignored)
└── src/
    ├── diagrams.py       # the 3 inline-SVG diagrams (edit drawings here)
    ├── front_matter.py   # cover, copyright notice, about
    ├── day_to_day.py     # Part One teaching sections
    ├── procedures.py     # communion, funeral, counseling (uses 2 diagrams)
    ├── verbatim.py       # imported sermon/reference sections (reads data/)
    ├── positions.py      # position schedule + tables (uses the floor map)
    └── reference.py      # role cards, index, training checklist
```

## Where to edit what

- **A diagram** → `src/diagrams.py`. All three SVGs are there.
- **Wording of a procedure** (communion/funeral/counseling) → `src/procedures.py`.
- **A teaching section** (history, qualifications, mission, etc.) → `src/day_to_day.py`.
- **The position schedule, reserved-seating key, or service-flow table** → `src/positions.py`.
- **Role cards, the index, or the training checklist** → `src/reference.py`.
- **Verbatim sermon / reference text** → these are sliced by line number out of
  `data/deacon_en.txt` in `src/verbatim.py`. The line ranges there assume that
  exact file (a `pdftotext -layout` extraction of the 2007 source). If you
  re-extract the source, regenerate the ranges.
- **Styling, page size, headers/footers, colors, fonts** → `assets/book.css`.
- **Document order, table of contents, part dividers** → `build.py`.

## Previewing while you work

For fast iteration you can open `output/manual.html` directly in a browser
instead of rebuilding the PDF each time. The browser won't paginate exactly
like WeasyPrint (page breaks differ), but it's accurate for content and layout.

## Notes

- `deacon_en.txt` is real input the build depends on — keep it in `data/`, not
  in a temp folder.
- Everything under `output/` is generated; it's safe to delete and is gitignored.
- Tested with WeasyPrint 68.x.
