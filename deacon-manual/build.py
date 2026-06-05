#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the complete three-Part Deacon Manual -> PDF."""
import os, sys
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from front_matter import COVER, NOTICE, ABOUT
from day_to_day import (OFFICES, DEFMANUAL, ATTITUDE, HISTORY, QUAL, REWARDS,
                      MISSION, USHERS, MINISTER, ARENA)
from procedures import COMMUNION, FUNERAL, COUNSEL
from verbatim import (PLACING, COD_SUPP, CHURCHORDER63, RESPONS,
                      GUIDELINES, SERVICECHK, PHXORDER, LEXICON, REFERENCES)
from positions import positions_extras, service_flow_table
from reference import role_cards, index_section, training_checklist

CSS = (ROOT / "assets" / "book.css").read_text(encoding="utf-8")

# Part Three opener — the seven-offices teaching, in the church's own words.
# (Verbatim as given, normalizing only three transcription typos: its / Treasurer / altars.)
SEVEN_OFFICES_OPENER = '''
<section id="s-sevenoffices">
  <div class="eyebrow">Part Three &#183; Church Order</div>
  <h1 class="section-title">On the Order of the Church</h1>
  <div class="title-rule"></div>
  <div class="callout wine"><div class="clabel">The Seven Offices</div>
  <p>For an established Church to be perfectly in order, it must have its Seven Major Offices (or main
  offices): the Office of the Pastor, the Associate Pastor, the Trustees (&#8220;Confiables&#8221;), the
  Deacons, the Treasurer, the Sunday School Superintendent, and the Music Program. Every office has its
  own specific work to do. Essentially, each and every one of us has a job to do; and the first thing we
  must do is to undo the altars of ignorance.</p></div>
  <p class="note-inline">The offices described on the pages that follow are these seven. Each is given so
  that the body may be supported and kept in order &#8212; not as ground for conflict or position.</p>
</section>'''

def part_divider(num, title, desc):
    return f'''
<div class="partdiv"><div class="frame"></div>
  <div class="pd-inner">
    <div class="pd-kicker">Phoenix Tabernacle Deacon Manual</div>
    <div class="pd-num">Part {num}</div>
    <h1>{title}</h1>
    <div class="pd-rule"></div>
    <div class="pd-desc">{desc}</div>
  </div></div>'''

# ---- Table of contents (three parts) ----------------------------------------
TOC_PARTS = [
    ("Part One &#183; Day to Day", [
        ("Definition of a Manual","s-defmanual",0),
        ("Attitude","s-attitude",0),
        ("The History of the Deacon","s-history",0),
        ("Qualifications for Deacons","s-qual",0),
        ("The Deacon&#8217;s Mission Statement","s-mission",0),
        ("The Deacon&#8217;s Training Checklist","s-training",0),
        ("The Man in the Arena","s-arena",0),
        ("Communion Procedures","s-communion",0),
        ("Funeral Procedures","s-funeral",0),
        ("Counseling Code of Conduct","s-counsel",0),
    ]),
    ("Part Two &#183; The Message Foundation", [
        ("Ushers &amp; Deacons","s-ushers",0),
        ("What Is a Minister?","s-minister",0),
        ("The Rewards of Faithful Service","s-rewards",0),
        ("Placing of Deacons","s-placing",0),
        ("Responsibilities of a Deacon","s-respons",0),
        ("Church Order &#8212; 1963-1226","s-co63",0),
    ]),
    ("Part Three &#183; Church Order", [
        ("On the Order of the Church","s-sevenoffices",0),
        ("Operations of Church Offices","s-offices",0),
        ("Church Order &#8212; COD Supplement","s-codsupp",0),
        ("Role Quick Reference","s-rolecards",0),
        ("Guidelines for Deacon Department Positions","s-positions",0),
        ("Service Program Procedural Checklist","s-servchk",0),
        ("Phoenix Tabernacle Church Order","s-phxorder",0),
        ("Lexicon Definitions","s-lexicon",0),
        ("References &amp; Additional Readings","s-references",0),
        ("Index","s-index",0),
    ]),
]

def toc():
    out = ['<div class="toc"><h1>Contents</h1><div class="trule"></div><ul>']
    for pname, entries in TOC_PARTS:
        out.append(f'<li class="part">{pname}</li>')
        for title, anchor, sub in entries:
            cls = "entry sub" if sub else "entry"
            out.append(f'<li class="{cls}"><a href="#{anchor}"><span class="t">{title}</span>'
                       f'<span class="leaders"></span></a></li>')
    out.append('</ul></div>')
    return "\n".join(out)

# ---- assemble ----------------------------------------------------------------
from front_matter import EPIGRAPH
front = COVER + NOTICE + ABOUT + EPIGRAPH + toc()

part1 = part_divider("One", "Day to Day",
    "The deacon&#8217;s calling, qualifications, and the service procedures used week to week "
    "&#8212; communion, funerals, and counseling.") + '<div class="pp1">' + \
    DEFMANUAL + ATTITUDE + HISTORY + QUAL + MISSION + training_checklist() + ARENA + COMMUNION + FUNERAL + COUNSEL + '</div>'

part2 = part_divider("Two", "The Message Foundation",
    "References &amp; why &#8212; the verbatim teaching of Bro.&nbsp;William&nbsp;Branham that "
    "establishes the order of the church and the calling of the deacon.") + '<div class="pp2">' + \
    USHERS + MINISTER + REWARDS + PLACING() + RESPONS() + CHURCHORDER63() + '</div>'

part3 = part_divider("Three", "Church Order",
    "The seven offices, the COD supplement, the position guidelines, and the order of "
    "Phoenix Tabernacle.") + '<div class="pp3">' + \
    SEVEN_OFFICES_OPENER + OFFICES + COD_SUPP() + role_cards() + GUIDELINES() + positions_extras() + \
    SERVICECHK() + service_flow_table() + PHXORDER() + LEXICON() + REFERENCES() + index_section() + '</div>'

html_doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Phoenix Tabernacle Deacon Manual</title>
<style>{CSS}</style></head><body>
{front}
{part1}
{part2}
{part3}
</body></html>'''

OUTDIR = ROOT / "output"
OUTDIR.mkdir(exist_ok=True)
with open(OUTDIR / "manual.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

OUT = str(OUTDIR / "Phoenix_Tabernacle_Deacon_Manual.pdf")
HTML(string=html_doc, base_url=str(ROOT)).write_pdf(OUT)
print("WROTE", OUT, os.path.getsize(OUT), "bytes")
