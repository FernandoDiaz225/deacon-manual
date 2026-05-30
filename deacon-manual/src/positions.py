# -*- coding: utf-8 -*-
"""Reconstructed structured content for two sections the flat import mangled:
the Deacon Department Positions floor map, the Usher Position Schedule table,
and the back-office Service Program -> Position table. Data is reproduced exactly
from the 2007 source (pp.144, 150); only the *presentation* is rebuilt."""

from diagrams import POSITIONS_MAP_SVG

# ---- Usher Position Schedule (source p.144, reproduced verbatim) -------------
USHER_SCHEDULE = [
    ("1","Backdoor"),("1A","Platform South Side"),("1B","Platform North Side"),
    ("2","Altar area &#8212; lead position"),("3","Altar area &#8212; assistant"),
    ("4","Middle aisle"),("5","South-side section"),("6","North-side section"),
    ("7","Mid section &#8212; north side"),("8","Mid section &#8212; south side"),
    ("9","North side exit"),("10","South side exit"),("11","Additional seating section"),
    ("12","Team Leader for Sanctuary"),("13","Gatekeeper to Sanctuary"),
    ("14","Vestibule"),("15","Vestibule"),("16","Vestibule"),("17","Team Leader for Program"),
    ("18","Team Leader for Parking Area"),("19","Parking area"),("20","Parking area"),
    ("21","Parking area"),("22","Team Leader for Vestibule"),
    ("23","Program Coordinator &#8212; Back Office"),("24","Liaison &#8212; Back Office"),
    ("25","Back Office"),("26","Back Office"),("27","&lt;Pastor&gt; (reserved seating)"),
    ("29","Video Assistant"),("30+","Substitute"),
]
RESERVED = [
    ("&lt;Pastor&gt;","Pastor &#8212; seat vacant"),
    ("&lt;Associate Pastor&gt;","Associate Pastor &#8212; seat vacant"),
    ("&lt;Deacon&#8217;s Director&gt;","Deacon&#8217;s Director &#8212; seat vacant"),
    ("&lt;Secretary&gt;","Secretary"),
]

def usher_schedule_table():
    rows = "".join(f'<tr><td style="text-align:center;font-family:Poppins,sans-serif;'
                   f'font-weight:600;color:#6e2a2a">{n}</td><td>{d}</td></tr>'
                   for n, d in USHER_SCHEDULE)
    legend = "".join(f'<tr><td style="text-align:center;font-family:Poppins,sans-serif;'
                     f'font-weight:600;color:#9a7b3f">{a}</td><td>{full}</td></tr>'
                     for a, full in RESERVED)
    return f'''
  <h2 class="sub">Usher Position Schedule</h2>
  <table class="tbl"><thead><tr><th style="width:64pt;text-align:center">Position #</th>
  <th>Position Description</th></tr></thead><tbody>{rows}</tbody></table>
  <h3 class="import-h">Reserved Seating &#8212; Key</h3>
  <table class="tbl"><thead><tr><th style="width:90pt;text-align:center">Reserved seat</th><th>Office</th>
  </tr></thead><tbody>{legend}</tbody></table>'''

def positions_extras():
    return f'''
<section id="s-posmap" class="cont">
  {usher_schedule_table()}
  <h2 class="sub">Deacon Department Positions &#8212; Floor Map</h2>
  <figure><div class="figframe">{POSITIONS_MAP_SVG}</div>
  <figcaption>Standing-position zones in the sanctuary (North = left, South = right; front/altar at top).
  Numbers are the positions in the schedule above; gold boxes are reserved seating. A zone guide &#8212;
  see the Position Schedule for each role&#8217;s exact description.</figcaption></figure>
</section>'''

# ---- Service Program -> responsible Position (source p.150) -----------------
SERVICE_FLOW = [
    ("Prelude &amp; Opening", [
        ("Sound System Prelude", "25 / 23"),
        ("Live Prelude", "25 / 23"),
        ("Opening Prayer", "25"),
        ("Interpreter", "26"),
    ]),
    ("Worship", [
        ("Worship Director and Songs", "24"),
    ]),
    ("Testimonies", [
        ("Testimonies (C/O Bro. ___) &#8212; 1. Sister, 2. Brother, 3. Sister", "26"),
        ("Interpreter", "26"),
    ]),
    ("Special Songs", [
        ("Special Songs (guitars, soundtrack, piano, choir, poems, out-of-town guests)", "26 &amp; 23"),
    ]),
    ("Welcome, Petitions &amp; Offering", [
        ("Welcome, Thanksgivings, Petitions, Announcements, Sheet", "25 / 26"),
        ("Song Director and Songs", "24"),
        ("Interpreters (this section)", "26"),
        ("Prayer for Petitions &amp; Offering", "25"),
        ("Child or Family Presentations", "25"),
        ("Baptisms", "25 / 23"),
    ]),
    ("Minister &amp; Altar", [
        ("Minister (mic and special needs)", "23"),
        ("Recording of Interpretation", "23"),
        ("Interpreters (this section)", "26"),
        ("Altar Call / Special Prayers", "25"),
    ]),
    ("Worship, Offerings &amp; Presentations", [
        ("Worship Director and Songs", "24"),
        ("Elder&#8217;s Attendance Sheet", "23"),
        ("Elder&#8217;s Prayer", "25"),
        ("Missionary, Special, Love &#8212; all offerings picked up in a service", "24"),
        ("Special Presentations (engagements, ordinations, Pastor, etc.)", "25"),
        ("Interpreter (this section)", "26"),
    ]),
    ("Sunday School &amp; Dismissal", [
        ("Sunday School Report", "26"),
        ("Interpreter", "26"),
        ("Announcements &amp; Dismiss", "25 / 26"),
        ("Interpreter", "26"),
        ("Prayer for Dismissal", "25"),
        ("Director and Song to Dismiss", "24"),
    ]),
]

def service_flow_table():
    body = ""
    for section, items in SERVICE_FLOW:
        body += (f'<tr><td colspan="2" style="background:#f1e8d6;font-family:Poppins,sans-serif;'
                 f'font-weight:600;font-size:8pt;letter-spacing:.08em;text-transform:uppercase;'
                 f'color:#6e2a2a">{section}</td></tr>')
        for seg, pos in items:
            body += (f'<tr><td>{seg}</td><td style="text-align:center;width:84pt;'
                     f'font-family:Poppins,sans-serif;font-weight:600;color:#6e2a2a">{pos}</td></tr>')
    return f'''
<section id="s-serviceflow" class="cont">
  <h2 class="sub">Service Program &#8212; Back-Office Position Responsibilities</h2>
  <p class="small muted">Each segment of the service and the back-office position(s) responsible for it.</p>
  <table class="tbl"><thead><tr><th>Service Segment</th>
  <th style="text-align:center;width:84pt">Position</th></tr></thead><tbody>{body}</tbody></table>
  <div class="callout wine"><div class="clabel">Confirmation</div>
  <p>Everything should be confirmed by Position&nbsp;23 (Program Coordinator &#8212; Back Office).</p></div>
</section>'''

print("part5 module loaded")
