#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Front matter: cover, copyright notice, and about pages."""
import datetime

# ---------------------------------------------------------------- cover --------
COVER = '''
<div class="cover">
  <div class="frame"></div>
  <div class="inner">
    <div class="kicker">Phoenix Tabernacle, Inc.</div>
    <h1>Deacon<br>Manual</h1>
    <div class="sub">Principles of Deaconship</div>
    <div class="crule"></div>
    <div class="epi">&#8220;Most men will proclaim every one his own goodness: but a faithful
      man who can find? The just man walketh in his integrity: his children are blessed after him.&#8221;
      <span class="ref">Proverbs 20:6&#8211;7 &#183; KJV</span></div>
  </div>
  <div class="foot">
    <div class="pastor">Pastor: &lt;Pastor&gt;</div>
    <div class="org">1241 East Baseline &#183; Phoenix, AZ 85040 &#183; Office 602-276-6069</div>
    <div class="ed">Third Edition &#183; August 2027</div>
  </div>
</div>'''

NOTICE = '''
<div class="frontpage">
  <div style="margin-top:26pt">
    <div class="eyebrow">Phoenix Tabernacle Deacon Manual</div>
    <h1 class="section-title" style="font-size:19pt">Principles of Deaconship</h1>
    <div class="title-rule"></div>
    <p class="muted">Pastor: &lt;Pastor&gt; &#183; Phoenix Tabernacle, Inc.<br>
       1241 East Baseline, Phoenix, AZ 85040-8005<br>
       Office: 602-276-6069 &#183; 602-276-0081 &#183; Fax: 602-304-1621<br>
       Third Edition &#8212; August 2027<br>
       Twentieth-anniversary edition &#8212; twenty years after the Second Edition of August 2007</p>
  </div>
  <div class="notice">
    <div class="nh">For Internal Use Only</div>
    <p style="margin:0">Property of Phoenix Tabernacle, Inc. Reproduction of this manual in part or
    in its entirety is strictly prohibited without written consent from Phoenix Tabernacle, Inc.</p>
  </div>
</div>'''

ABOUT = '''
<div class="frontpage">
  <div class="eyebrow">About this edition</div>
  <h1 class="section-title" style="font-size:20pt">How to Use This Manual</h1>
  <div class="title-rule"></div>
  <p class="lead">This edition keeps every word of the manual&#8217;s teaching and instruction intact.
  The work here is presentation only: clearer typography, redrawn diagrams, and procedures laid out
  so a deacon can find and follow them quickly &#8212; especially in the moments that matter most.</p>
  <p>To respect the source, the editorial approach is twofold. Scripture, dictionary definitions,
  and the words of <strong>Bro.&nbsp;William&nbsp;Branham</strong>, Pastor Garcia, and other quoted
  voices are reproduced <em>verbatim</em> and set apart in quotation panels. The church&#8217;s own
  administrative and procedural writing has been copy-edited for grammar and clarity only &#8212; no
  instruction, name, place, or requirement has been changed.</p>

  <div class="callout"><div class="clabel">Visual conventions used throughout</div>
  <div class="legend-grid">
    <div class="legend-item"><div class="lh">Numbered steps</div><div class="ld">An ordered procedure to follow in sequence.</div></div>
    <div class="legend-item"><div class="lh">&#9744;&nbsp;&nbsp;Checklist</div><div class="ld">Items to verify and tick off before a service.</div></div>
    <div class="legend-item"><div class="lh">Callout panel</div><div class="ld">An important note, caution, or tip set off from the text.</div></div>
    <div class="legend-item"><div class="lh">Quotation panel</div><div class="ld">Words reproduced verbatim, with the source named.</div></div>
    <div class="legend-item"><div class="lh">Scripture</div><div class="ld">A Bible passage, with its reference.</div></div>
    <div class="legend-item"><div class="lh">Diagram</div><div class="ld">A redrawn plan &#8212; parking, sanctuary, and seating flow.</div></div>
  </div></div>
  <p class="small muted">This book is organized in three parts. <strong>Part One &#8212; Day to
  Day</strong> is the working manual: the deacon&#8217;s calling and qualifications and the full service
  procedures (communion, funerals, counseling). <strong>Part Two &#8212; The Message Foundation</strong>
  gathers the verbatim teaching of Bro.&nbsp;William&nbsp;Branham that grounds the order of the church.
  <strong>Part Three &#8212; Church Order</strong> sets out the seven offices, the COD supplement, the
  position guidelines, and the church&#8217;s order. Parts Two and Three reproduce sermon and reference
  text verbatim; the procedures in Part One have been copy-edited for clarity.</p>
</div>'''

# ---------------------------------------------------------------- TOC ----------
def toc():
    parts = [
        ("The Office &amp; the Calling", [
            ("Operations of Church Offices","s-offices",0),
            ("Definition of a Manual","s-defmanual",0),
            ("Attitude","s-attitude",0),
            ("The History of the Deacon","s-history",0),
            ("Qualifications for Deacons","s-qual",0),
            ("The Rewards of Faithful Service","s-rewards",0),
            ("The Deacon&#8217;s Mission Statement","s-mission",0),
            ("Ushers &amp; Deacons","s-ushers",0),
            ("What Is a Minister?","s-minister",0),
            ("The Man in the Arena","s-arena",0),
        ]),
        ("Service Procedures", [
            ("Communion Procedures","s-communion",0),
            ("Communion Service Checklist","s-commserv",1),
            ("Communion Sign-Up Sheet","s-commsign",1),
            ("Funeral Procedures","s-funeral",0),
            ("Sanctuary","s-sanctuary",1),
            ("Parking Lot","s-parking",1),
            ("Gravesite","s-gravesite",1),
            ("Funeral Checklist","s-funcheck",1),
            ("Planning a Funeral","s-funplan",1),
            ("Service Sign-Up Sheets","s-funsign",1),
            ("Counseling Code of Conduct","s-counsel",0),
            ("Counseling Report","s-counselrep",1),
        ]),
    ]
    out = ['<div class="toc"><h1>Contents</h1><div class="trule"></div><ul>']
    for pname, entries in parts:
        out.append(f'<li class="part">{pname}</li>')
        for title, anchor, sub in entries:
            cls = "entry sub" if sub else "entry"
            out.append(f'<li class="{cls}"><a href="#{anchor}"><span class="t">{title}</span>'
                       f'<span class="leaders"></span></a></li>')
    out.append('</ul></div>')
    return "\n".join(out)

print("part1 module loaded")

EPIGRAPH = '''
<section id="s-epigraph" class="epigraph-page">
  <div class="epi-kicker">El Mundo Es Mi P&#250;lpito &#183; The World Is My Pulpit</div>

  <div class="epi-block">
    <p class="epi-quote">&#8220;And I, thirty-one years I&#8217;ve stood behind the desk here, and
    around the world, as I have claimed the world to be my pulpit. Then, I have tried to give people
    this Word of Eternal Life. And it&#8217;s the only thing that can help when you come to the end of
    the road. So why would we trust in anything else?&#8221;</p>
    <p class="epi-src">61-1001E &#183; The Comforter &#183; Rev. William Marrion Branham &#183; para. 12</p>
  </div>

  <div class="epi-div"><span></span><span class="d"></span><span></span></div>

  <div class="epi-block">
    <p class="epi-quote es">&#8220;Pero el profeta le est&#225; hablando a toda la Simiente predestinada
    a la cual Dios lo envi&#243; a &#233;l porque &#233;l dijo: &#8216;El mundo es mi p&#250;lpito&#8217;.
    Am&#233;n. El profeta dijo as&#237;, de modo que si nosotros estamos traduciendo lo que &#233;l dijo
    y repitiendo lo que &#233;l dijo al castellano, no es nuestro p&#250;lpito aqu&#237; en Phoenix; el
    mundo entero que entiende el castellano es nuestro p&#250;lpito y para ellos tambi&#233;n es la
    ense&#241;anza.&#8221;</p>
    <p class="epi-src">Ap&#243;stol Bernab&#233; Gonz&#225;lez Garc&#237;a &#183; pastor fundador &#183;
    El Orden B&#237;blico de la Iglesia, 1973</p>
  </div>
</section>'''
