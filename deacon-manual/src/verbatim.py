# -*- coding: utf-8 -*-
"""Import verbatim / large sections from the source extraction.
Cleaning is mechanical only (strips scan headers, footers, page numbers, and
rejoins wrapped lines). No words are changed -- these sections are preserved
as printed in the 2007 edition."""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "data" / "deacon_en.txt"
_LINES = open(SRC, encoding="utf-8", errors="replace").read().split("\n")

def _raw(a, b):
    return _LINES[a-1:b]  # 1-indexed inclusive

def _is_chrome(s):
    t = s.strip()
    if not t:
        return False
    if t.startswith("Phoenix Tabernacle Deacon Manual"):
        return True
    if t == "2007":
        return True
    if t.startswith("Property of Phoenix Tabernacle, Inc."):
        return True
    if t.startswith("strictly prohibited without written consent"):
        return True
    if re.fullmatch(r"Page\s*\d+", t):
        return True
    return False

def _sanitize(s):
    # U+F020 is a symbol-font space; other PUA glyphs are extraction garbage.
    s = s.replace("\uf020", " ")
    s = re.sub(r"[\ue000-\uf8ff]", "", s)
    return s

def _clean_lines(a, b):
    out = []
    for ln in _raw(a, b):
        ln = _sanitize(ln.replace("\f", ""))
        if _is_chrome(ln):
            continue
        out.append(ln)
    return out

def _blocks(a, b):
    """Group cleaned lines into paragraph blocks split on blank lines."""
    lines = _clean_lines(a, b)
    blocks, cur = [], []
    for ln in lines:
        if ln.strip() == "":
            if cur:
                blocks.append(cur); cur = []
        else:
            cur.append(ln.rstrip())
    if cur:
        blocks.append(cur)
    return blocks

def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

_PMARK = re.compile(r"^\s*(\d+(?:-\d+)?)\s+(.*)$")          # 353-1 / 1191-5 / 1
_HEAD = re.compile(r"^[A-Z0-9][A-Z0-9 ,’'&/\-\.\?\(\)]{2,55}$")
_POS  = re.compile(r"^Position[s]?\s*#?\s*\d+", re.I)

def transcript(a, b, title, attrib, anchor, eyebrow, first=False):
    """Render a verbatim sermon transcript."""
    parts = [f'<section id="{anchor}"{"" if first else ""}>',
             f'<div class="eyebrow">{eyebrow}</div>',
             f'<h1 class="section-title">{title}</h1>',
             '<div class="title-rule"></div>',
             f'<p class="attrline">{attrib}</p>',
             '<div class="transcript">']
    def _norm(s):
        return re.sub(r"[^a-z0-9]", "", s.lower())
    title_key = _norm(re.sub(r"&#?\w+;", "", title))
    for i, blk in enumerate(_blocks(a, b)):
        joined = " ".join(x.strip() for x in blk).strip()
        joined = re.sub(r"\s+", " ", joined)
        if not joined:
            continue
        nj = _norm(joined)
        if i < 2 and (nj.startswith(title_key) or "williammarrionbranham" in nj[:80]):
            continue  # drop repeated heading / attribution line
        m = _PMARK.match(joined)
        if m and len(m.group(1)) <= 7:
            mark, rest = m.group(1), m.group(2)
            parts.append(f'<p class="tpara"><span class="pmark">{mark}</span>{_esc(rest)}</p>')
        else:
            parts.append(f'<p class="tpara">{_esc(joined)}</p>')
    parts.append('</div></section>')
    return "\n".join(parts)

def teaching(a, b, title, anchor, eyebrow, intro=None, note=None):
    """Render church-authored teaching / guidelines faithfully (headings detected)."""
    parts = [f'<section id="{anchor}">',
             f'<div class="eyebrow">{eyebrow}</div>',
             f'<h1 class="section-title">{title}</h1>',
             '<div class="title-rule"></div>']
    if intro:
        parts.append(f'<p class="lead">{intro}</p>')
    if note:
        parts.append(f'<p class="note-inline">{note}</p>')
    for blk in _blocks(a, b):
        # skip a block that merely repeats the section title
        first_line = blk[0].strip()
        joined = " ".join(x.strip() for x in blk).strip()
        joined = re.sub(r"\s+", " ", joined)
        if not joined:
            continue
        if joined.upper() == title.upper():
            continue
        # heading?
        if len(blk) == 1 and (_POS.match(first_line) or
                              (_HEAD.match(first_line) and first_line == first_line.upper()
                               and len(first_line) < 56)):
            parts.append(f'<h3 class="import-h">{_esc(first_line.title() if first_line.isupper() else first_line)}</h3>')
            continue
        if _POS.match(first_line):
            parts.append(f'<h3 class="import-h">{_esc(first_line)}</h3>')
            rest = " ".join(x.strip() for x in blk[1:]).strip()
            if rest:
                parts.append(f'<p>{_esc(rest)}</p>')
            continue
        parts.append(f'<p>{_esc(joined)}</p>')
    parts.append('</section>')
    return "\n".join(parts)

# --------- imported section instances (line ranges from layout extraction) -----
PLACING      = lambda: transcript(701, 1016, "The Placing Of Deacons",
                    "58-0720E &#183; Rev. William Marrion Branham &#183; Jeff. IN",
                    "s-placing", "Part Two &#183; The Message Foundation")
COD_SUPP     = lambda: transcript(1017, 1427, "Church Order &#8212; COD Supplement",
                    "58-1007 &#183; Rev. William Marrion Branham",
                    "s-codsupp", "Part Three &#183; Church Order")
CHURCHORDER63= lambda: transcript(3653, 5346, "Church Order &#8212; 1963-1226",
                    "63-1226 &#183; Rev. William Marrion Branham &#183; Jeff. IN",
                    "s-co63", "Part Two &#183; The Message Foundation")
RESPONS =      lambda: transcript(1442, 3135, "Responsibilities of a Deacon",
                    "A topical compilation from the messages of Rev. William Marrion Branham",
                    "s-respons", "Part Two &#183; The Message Foundation")
GUIDELINES   = lambda: teaching(5347, 6153, "Guidelines for Deacon Department Positions",
                    "s-positions", "Part Three &#183; Church Order",
                    note="Reproduced from the 2007 edition; a detailed grammar pass on this section is still pending.")
SERVICECHK   = lambda: teaching(6252, 6425, "Service Program Procedural Checklist",
                    "s-servchk", "Part Three &#183; Church Order")
PHXORDER     = lambda: teaching(3136, 3455, "Phoenix Tabernacle Church Order",
                    "s-phxorder", "Part Three &#183; Church Order")
LEXICON      = lambda: teaching(3456, 3621, "Lexicon Definitions",
                    "s-lexicon", "Part Three &#183; Church Order",
                    note="Definitions reproduced from their sources.")
REFERENCES   = lambda: teaching(8305, len(_LINES), "References &amp; Additional Readings",
                    "s-references", "Part Three &#183; Church Order")

if __name__ == "__main__":
    html = PLACING()
    print(html[:1500])
    print("...\n[blocks in Placing:]", len(_blocks(701,1016)))
