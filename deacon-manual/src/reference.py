# -*- coding: utf-8 -*-
"""Additive navigation only: role quick-reference cards and a back-matter index.
No teaching text is created or altered. Role cards reuse the verbatim position
labels from positions.USHER_SCHEDULE; the index points to existing section anchors."""
from positions import USHER_SCHEDULE

_LABEL = {num: desc for num, desc in USHER_SCHEDULE}

# Roles grouped by team (position numbers only; labels come from the schedule) ---
_ROLES = [
    ("Platform &amp; Doors", ["1", "1A", "1B"]),
    ("Altar &amp; Sanctuary", ["2", "3", "4", "12", "13"]),
    ("Seating Sections", ["5", "6", "7", "8", "9", "10", "11"]),
    ("Vestibule", ["14", "15", "16", "22"]),
    ("Parking", ["18", "19", "20", "21"]),
    ("Back Office &amp; Program", ["17", "23", "24", "25", "26", "29"]),
]

def role_cards():
    cards = []
    for role, nums in _ROLES:
        items = "".join(
            f'<li><span class="pn">{n}</span>{_LABEL.get(n, "&#8212;")}</li>' for n in nums
        )
        cards.append(
            f'<div class="rolecard"><div class="rh">{role}</div><ul>{items}</ul>'
            f'<p class="rsee">Full duties &#8212; see Guidelines for Deacon Department Positions '
            f'and the Floor Map in this Part.</p></div>'
        )
    grid = "".join(cards)
    return f'''
<section id="s-rolecards">
  <div class="eyebrow">Part Three &#183; Church Order</div>
  <h1 class="section-title">Role Quick Reference</h1>
  <div class="title-rule"></div>
  <p class="lead">The serving positions grouped by team, for fast assignment and training. Each role
  lists its positions; the full description of every position follows in the Position Schedule, the Floor
  Map, and the Guidelines.</p>
  <div class="rolecards">{grid}</div>
  <div class="callout"><div class="clabel">How to use this page</div>
  <p>Hand a trainee the card for their team to learn their posts at a glance, then send them to the
  Guidelines for Deacon Department Positions for the complete duties of each numbered position.</p></div>
</section>'''

# Back-matter index: alphabetical entries -> existing section anchors ----------
_INDEX = [
    ("Altar &amp; sanctuary positions", "s-rolecards"),
    ("Arena, The Man in the", "s-arena"),
    ("Associate pastor, office of", "s-offices"),
    ("Attitude", "s-attitude"),
    ("Back office &amp; program positions", "s-rolecards"),
    ("Church Order (1963-1226)", "s-co63"),
    ("Church Order, Phoenix Tabernacle", "s-phxorder"),
    ("COD Supplement", "s-codsupp"),
    ("Communion procedures", "s-communion"),
    ("Communion service checklist", "s-commserv"),
    ("Communion sign-up sheet", "s-commsign"),
    ("Counseling code of conduct", "s-counsel"),
    ("Counseling report", "s-counselrep"),
    ("Deacon, definition (lexicon)", "s-lexicon"),
    ("Deacon, history of the", "s-history"),
    ("Deacon, qualifications", "s-qual"),
    ("Deacon, responsibilities", "s-respons"),
    ("Deaconess (lexicon)", "s-lexicon"),
    ("Elder (lexicon)", "s-lexicon"),
    ("Floor map", "s-posmap"),
    ("Funeral procedures", "s-funeral"),
    ("Funeral checklist", "s-funcheck"),
    ("Funeral, planning a", "s-funplan"),
    ("Gravesite", "s-gravesite"),
    ("Guidelines for positions", "s-positions"),
    ("Lexicon definitions", "s-lexicon"),
    ("Manual, definition of a", "s-defmanual"),
    ("Minister, what is a", "s-minister"),
    ("Mission statement", "s-mission"),
    ("Music program, office of", "s-offices"),
    ("Offices, operations of church", "s-offices"),
    ("Parking lot procedures", "s-parking"),
    ("Parking positions", "s-rolecards"),
    ("Pastor, office of the", "s-offices"),
    ("Placing of deacons", "s-placing"),
    ("Platform &amp; door positions", "s-rolecards"),
    ("Position schedule", "s-posmap"),
    ("References &amp; readings", "s-references"),
    ("Rewards of faithful service", "s-rewards"),
    ("Role quick reference", "s-rolecards"),
    ("Sanctuary (funeral flow)", "s-sanctuary"),
    ("Seating sections", "s-rolecards"),
    ("Service program checklist", "s-servchk"),
    ("Service program &#8212; position table", "s-serviceflow"),
    ("Seven appointed deacons (lexicon)", "s-lexicon"),
    ("Seven offices, on the", "s-sevenoffices"),
    ("Sign-up sheets, funeral", "s-funsign"),
    ("Sober (lexicon)", "s-lexicon"),
    ("Sunday school superintendent, office of", "s-offices"),
    ("Treasurer, office of the", "s-offices"),
    ("Trustees, office of the", "s-offices"),
    ("Training checklist, deacon", "s-training"),
    ("Ushers &amp; deacons", "s-ushers"),
    ("Vestibule positions", "s-rolecards"),
]

def _sortkey(label):
    import re
    return re.sub(r"&#?\w+;|[^A-Za-z0-9 ]", "", label).strip().lower()

def index_section():
    entries = sorted(_INDEX, key=lambda e: _sortkey(e[0]))
    out = []
    cur_letter = None
    for label, anchor in entries:
        first = _sortkey(label)[:1].upper()
        if first != cur_letter:
            cur_letter = first
            out.append(f'<div class="idx-letter">{first}</div>')
        out.append(
            f'<div class="idx"><a href="#{anchor}"><span class="it">{label}</span>'
            f'<span class="il"></span></a></div>'
        )
    body = "\n".join(out)
    return f'''
<section id="s-index">
  <div class="eyebrow">Find it fast</div>
  <h1 class="section-title">Index</h1>
  <div class="title-rule"></div>
  <p class="note-inline">Topics, offices, positions, and procedures, with the page where each begins.</p>
  <div class="index-cols">{body}</div>
</section>'''

# Deacon training & formation checklist (a suggested addition, attributed) -----
# Synthesis of HCI principles, Robert Greene's "Laws of Human Nature" and
# "48 Laws of Power", oriented entirely toward the deacon's calling to serve.
# Ordered inside-out: master self -> read people -> serve -> recover -> lead.
_TRAINING_STAGES = [
    ("1 &#183; Master Yourself First",
     "Self-mastery &#8212; the inner foundation (Greene, Law of Human Nature 1; the Attitude of this manual)",
     [
        "I can stay calm and unoffended when I am corrected, criticized, or overlooked &#8212; and still smile and serve.",
        "I have examined my own motives; I serve to honor Christ, not to be seen, thanked, or promoted.",
        "I guard my testimony away from the platform as carefully as on it.",
        "I come prepared and rested, so that pressure never takes charge of me.",
        "I listen first and say less than necessary, and I keep a confidence without fail.",
     ]),
    ("2 &#183; Learn to Read People and the Room",
     "Discernment &#8212; perception before action (Greene, seeing through people&#8217;s masks; HCI, know the one you serve)",
     [
        "I can read a person&#8217;s state from face and posture, not from words alone.",
        "I notice the visitor, the newcomer, and the struggling before they have to ask.",
        "I anticipate what a person will need next, and meet it quietly.",
        "I know every post on the team and exactly who to turn to for what.",
        "I learn each person&#8217;s sensitivities so I can serve them better &#8212; never to use them.",
     ]),
    ("3 &#183; Serve So That It Feels Effortless",
     "Execution &#8212; the best service is unseen (HCI: error prevention, recognition; strategy: make hard things look easy)",
     [
        "I know my post and procedure so well that I act without hesitation.",
        "I prevent problems before they begin &#8212; doors, supplies, seating, sound.",
        "I keep order without ever drawing attention to myself.",
        "I use the checklist every single time, even when I am sure I remember.",
        "I confirm with the responsible position rather than assume (for example, Position&nbsp;23).",
     ]),
    ("4 &#183; Handle Conflict and Recover with Grace",
     "Recovery &#8212; defuse, do not inflame (Greene, on anger and timing; the Counseling code of this manual)",
     [
        "I de-escalate rather than win; when voices rise, mine lowers.",
        "I stand as an intercessor, not a judge, seeking to restore the person.",
        "I sense the right moment to act and the right moment to wait.",
        "I bring matters to the pastor and the order of the church; I do not conference alone or go around it.",
        "When I am wrong, I own it at once, repair it, and do not repeat it.",
     ]),
    ("5 &#183; Lead by Example and Raise Up Others",
     "Maturity &#8212; authority earned by service (Greene, drawing others to follow; &#8220;lead by my example&#8221;)",
     [
        "My steadiness has earned the trust of the people and the confidence of the pastor.",
        "I see the whole service, not only my own post.",
        "I plan all the way to the end of a service before it begins.",
        "I train the next deacon: he shadows me, then does it himself while I watch.",
        "I make the office honorable by the way I carry it.",
     ]),
]

def training_checklist():
    blocks = []
    for title, lineage, items in _TRAINING_STAGES:
        lis = "".join(f'<li>{it}</li>' for it in items)
        blocks.append(
            f'<h2 class="sub">{title}</h2>'
            f'<p class="small muted" style="margin:-4pt 0 7pt">{lineage}</p>'
            f'<ul class="checklist">{lis}</ul>'
        )
    body = "\n".join(blocks)
    return f'''
<section id="s-training">
  <div class="eyebrow">Formation &#183; A Suggested Addition</div>
  <h1 class="section-title">The Deacon&#8217;s Training Checklist</h1>
  <div class="title-rule"></div>
  <p class="attrline">Suggested by Brother Fernando Joel Diaz III</p>
  <p class="lead">A path for forming a deacon who serves well &#8212; not only what to do, but who to
  become. Work through it in order; each stage rests on the one before it.</p>
  <div class="callout"><div class="clabel">Why this order</div>
  <p>The order is deliberate. A deacon cannot read people until he has first mastered himself; he cannot
  serve smoothly until he can read a room; and he cannot lead until he has served. This checklist draws on
  the principles of human nature and strategy in Robert Greene&#8217;s work (<em>The Laws of Human
  Nature</em> and <em>The 48 Laws of Power</em>) and on human-centered (HCI) design &#8212; with every
  principle turned toward the deacon&#8217;s calling to serve, never to dominate.</p></div>
  {body}
  <div class="callout teal"><div class="clabel">The aim</div>
  <p>A deacon who completes this formation has &#8220;used the office of a deacon well&#8221; &#8212;
  gaining the trust of the people, the approval of the pastor, and boldness in the faith. Review it
  periodically; formation is never finished.</p></div>
</section>'''

if __name__ == "__main__":
    print(role_cards()[:300])
    print("...")
    print(index_section()[:300])
