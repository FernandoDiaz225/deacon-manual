# -*- coding: utf-8 -*-
"""Render-layer enrichment for the Placing of Deacons transcript.
No words are changed -- only emphasis (bold/underline), styled annotation
blocks, an inline gloss, and an indented Scripture reading are added. Each
anchor must match the rendered transcript exactly once or the build raises,
so the source text and this layer can never drift apart silently."""


def _enrich_placing(html):
    BYLAW = ('<p class="tpara"><span class="pmark">353-3</span>And ever so often, '
             'according to the bylaws of the church, every year, the</p>\n'
             '<p class="tpara">BY-LAW a law or ordinance dealing with matters of local '
             'or internal regulation, made by a local authority, or by a corporation.</p>\n'
             '<p class="tpara">deacons or trustees automatically fill their time.')
    BYLAW_NEW = ('<p class="tpara"><span class="pmark">353-3</span>And ever so often, '
                 'according to the bylaws of the church, every year, the '
                 '<span class="inline-gloss"><span class="gw">By-law</span> a law or ordinance '
                 'dealing with matters of local or internal regulation, made by a local authority, '
                 'or by a corporation.</span> deacons or trustees automatically fill their time.')

    HONJUST = ('<p class="tpara">HONORABLE Worthy of being honored; entitled to respect, reverence.</p>\n'
               '<p class="tpara">JUST Upright, and impartial in one\u2019s dealings; appropriate, '
               'suitable, suitable, complete in amount or character. Exactly, precisely, in replies '
               'etc. in accordance with reason, truth or facts, rights true, correct, exact, accurate, '
               'exact as opposed to approximate.</p>')
    HONJUST_NEW = ('<div class="annot"><div class="annot-row"><span class="aw">Honorable</span>'
                   '<span class="ad">Worthy of being honored; entitled to respect, reverence.</span></div>'
                   '<div class="annot-row"><span class="aw">Just</span>'
                   '<span class="ad">Upright, and impartial in one\u2019s dealings; appropriate, suitable, '
                   'suitable, complete in amount or character. Exactly, precisely, in replies etc. in '
                   'accordance with reason, truth or facts, rights true, correct, exact, accurate, exact '
                   'as opposed to approximate.</span></div></div>')

    SCRIP = ('<p class="tpara">requirements of the deacon. Brother Neville, if you\'ll read it from '
             'the Word of God. [Brother Neville reads I Timothy 3:8-13--Ed.]: Likewise must the deacons '
             'be grave, not double-tongued, not given to much wine and greedy of filthy lucre; Holding '
             'the mystery of the faith in a pure conscience. And let these also first be proved; then '
             'let them use the office of a deacon, being found blameless. Even so must their wives be '
             'grave, not slanderers, sober, faithful in all things. Let the deacons be the husbands of '
             'one wife, ruling their children and their own houses well. For they that have used the '
             'office of a deacon well purchase to themselves a good degree, and great boldness in the '
             'faith which is in Christ Jesus.</p>')
    SCRIP_NEW = ('<p class="tpara"><strong>requirements of the deacon.</strong> Brother Neville, if '
                 'you\'ll read it from the Word of God. [Brother Neville reads I Timothy 3:8-13--Ed.]:</p>\n'
                 '<div class="scripture-indent">Likewise must the deacons be grave, not double-tongued, '
                 'not given to much wine and greedy of filthy lucre; Holding the mystery of the faith in '
                 'a pure conscience. And let these also first be proved; then let them use the office of '
                 'a deacon, being found blameless. Even so must their wives be grave, not slanderers, '
                 'sober, faithful in all things. Let the deacons be the husbands of one wife, ruling their '
                 'children and their own houses well. For they that have used the office of a deacon well '
                 'purchase to themselves a good degree, and great boldness in the faith which is in '
                 'Christ Jesus.</div>')

    RULEREG = ('<p class="tpara">RULE the code of discipline or body of regulation observed by a '
               'religious order; or congregation. A principle regulating practice or procedure.</p>\n'
               '<p class="tpara">REGULATION A rule prescribed for the management of some matter, or '
               'regulating of conduct.</p>')
    RULEREG_NEW = ('<div class="annot"><div class="annot-row"><span class="aw">Rule</span>'
                   '<span class="ad">The code of discipline or body of regulation observed by a religious '
                   'order; or congregation. A principle regulating practice or procedure.</span></div>'
                   '<div class="annot-row"><span class="aw">Regulation</span>'
                   '<span class="ad">A rule prescribed for the management of some matter, or regulating '
                   'of conduct.</span></div></div>')

    EDITS = [
        ("bylaw-gloss", BYLAW, BYLAW_NEW),
        ("honjust-annot", HONJUST, HONJUST_NEW),
        ("scripture-indent", SCRIP, SCRIP_NEW),
        ("rulereg-annot", RULEREG, RULEREG_NEW),
        ("bold-sovereign",
         "And our little church here is sovereign. It doesn't have any denomination or anything to send its deacons; it elects its own deacons. It elects its pastor; it elects its trustees; it elects everything that comes in and out of the church. No one person has the say-so over anything; it's the church. And the church are those who come and support the church with their presence, with their tithe and offerings, are always the ones that has legal say-so in the placing of such.",
         None),
        ("bold-theway-a",
         "The way this is done is the board can appoint deacons, men that they have</p>",
         '<strong>The way this is done is the board can appoint deacons, men that they have</strong></p>'),
        ("bold-theway-b",
         '<p class="tpara">associated with and found to be honorable and just men. The office of a deacon is a very great office, and a great honor to the Lord to be a deacon in the church.',
         '<p class="tpara"><strong>associated with and found to be honorable and just men. The office of a deacon is a very great office, and a great honor to the Lord to be a deacon in the church.</strong>'),
        ("underline-honjust",
         "that these were honorable and just men.",
         "that these were <u>honorable</u> and <u>just</u> men."),
        ("bold-sotherefore",
         "And so therefore, then it has been found favorable with the board and the pastor, and the overseer, to select in this group of people here some men who we think to be honorable and just men. We can only bring them. And it's then they are appointed by the church, by their own vote. And then these man shall serve, if they feel that they will accept this office. Then they will come for a short time to see if they feel that maybe that God has called them. And if later, if they feel that they are disqualified, then they have a right in the next few weeks to resign the office, that someone else could be appointed in their place.",
         None),
        ("bold-wewill",
         "then I--then I'll... We will</p>",
         "then I--then I'll... <strong>We will</strong></p>"),
        ("bold-ordain",
         '<p class="tpara">ordain these deacons by laying on hands, deacons and treasurer in this church. But first they must be appointed and--and see how they like it and how the congregation likes it. Then if it\'s--then if it\'s all right on both sides, then we make these men ordained deacons, just like trustees are elected the same way.',
         '<p class="tpara"><strong>ordain these deacons by laying on hands, deacons and treasurer in this church. But first they must be appointed and--and see how they like it and how the congregation likes it. Then if it\'s--then if it\'s all right on both sides, then we make these men ordained deacons, just like trustees are elected the same way.</strong>'),
        ("bold-bythechurch",
         "it has to be by the church. No one does anything within himself here. It's the vote of the church.",
         None),
        ("bold-lordjesus",
         "Lord Jesus, it is with sober, godly thinking that we come to Thee now.",
         None),
        ("bold-asitissaid",
         'As it is once said concerning the deacon board, "Go, look out yourself among you, men of good reports and with the Holy Spirit, that they might serve in this manner to take care of the widows and orphans, to distribute the money, and to care for the welfare of the church." Later years we have just read the writing of that great, inspired, sainted Paul, who sets forth the declaration of the Scriptures of the requirements of such position.',
         None),
        ("bold-nowyouhave",
         'Now, you have said, "Let these first be tried, and see if they desire this office." Within a few weeks, God willing, I will return back to lay hands upon this group of men to make them the official trust--or the deacons of this church, and treasurer.',
         None),
        ("bold-mayserve-a",
         "And may they serve this office with all their hearts, knowing that it is purchasing to them a great degree in</p>",
         '<strong>And may they serve this office with all their hearts, knowing that it is purchasing to them a great degree in</strong></p>'),
        ("bold-mayserve-b",
         '<p class="tpara">heaven. Someday when the books of heaven shall be closed, may the Book of the celestial beings and the great Book of heaven be opened, may their names be one hundred percent before God and the Saviour and all the heavenly hosts to be the same in His Kingdom.',
         '<p class="tpara"><strong>heaven. Someday when the books of heaven shall be closed, may the Book of the celestial beings and the great Book of heaven be opened, may their names be one hundred percent before God and the Saviour and all the heavenly hosts to be the same in His Kingdom.</strong>'),
    ]

    for label, old, new in EDITS:
        if new is None:
            new = '<strong>' + old + '</strong>'
        c = html.count(old)
        assert c == 1, f"_enrich_placing: [{label}] expected 1 match, got {c}"
        html = html.replace(old, new, 1)
    return html
