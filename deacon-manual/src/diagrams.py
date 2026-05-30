# -*- coding: utf-8 -*-
"""All inline SVG diagrams used in the manual, kept together in one place.

PARKING_SVG and SANCTUARY_SVG appear in the Funeral Procedures section
(see procedures.py). POSITIONS_MAP_SVG is the Deacon Department Positions
floor map in Part Three (see positions.py). Each is a self-contained <svg>
element; book.css sets `figure svg { width: 100% }` so they scale to the page.
"""

PARKING_SVG = '''
<svg viewBox="0 0 760 600" xmlns="http://www.w3.org/2000/svg">
<defs>
      <marker id="pk" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.4" markerHeight="6.4" orient="auto-start-reverse">
        <path d="M2 1L8 5L2 9" fill="none" stroke="#0f6e56" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></marker>
      <marker id="pkx" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.6" markerHeight="6.6" orient="auto-start-reverse">
        <path d="M2 1L8 5L2 9" fill="none" stroke="#3b6d11" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></marker>
    </defs>
<rect x="110" y="44" width="580" height="360" rx="10" fill="none" stroke="#b4b2a9" stroke-width="1.2" stroke-dasharray="5 5"/>
<rect x="110" y="44" width="38" height="360" fill="#f4fbf8"/>
<rect x="148" y="318" width="536" height="48" fill="#f4fbf8"/>
<rect x="156" y="54" width="202" height="96" rx="8" fill="#f1efe8" stroke="#888780" stroke-width="1.1"/>
<text x="257.0" y="102.0" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="14" font-weight="600" fill="#444441">Church</text>
<rect x="156" y="158" width="202" height="36" rx="6" fill="#e1f5ee" stroke="#0f6e56" stroke-width="1"/><line x1="196.4" y1="158" x2="196.4" y2="194" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="236.8" y1="158" x2="236.8" y2="194" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="277.2" y1="158" x2="277.2" y2="194" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="317.6" y1="158" x2="317.6" y2="194" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="348" y1="176.0" x2="146" y2="176.0" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/><circle cx="180" cy="176.0" r="12" fill="#0f6e56" stroke="#fff" stroke-width="1.5"/><text x="180" y="176.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="13" font-weight="700" fill="#fff">1</text>
<rect x="156" y="204" width="202" height="36" rx="6" fill="#e1f5ee" stroke="#0f6e56" stroke-width="1"/><line x1="196.4" y1="204" x2="196.4" y2="240" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="236.8" y1="204" x2="236.8" y2="240" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="277.2" y1="204" x2="277.2" y2="240" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="317.6" y1="204" x2="317.6" y2="240" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="348" y1="222.0" x2="146" y2="222.0" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/><circle cx="180" cy="222.0" r="12" fill="#0f6e56" stroke="#fff" stroke-width="1.5"/><text x="180" y="222.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="13" font-weight="700" fill="#fff">3</text>
<rect x="156" y="250" width="202" height="50" rx="6" fill="#e1f5ee" stroke="#0f6e56" stroke-width="1"/><line x1="189.7" y1="250" x2="189.7" y2="300" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="223.3" y1="250" x2="223.3" y2="300" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="257.0" y1="250" x2="257.0" y2="300" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="290.7" y1="250" x2="290.7" y2="300" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="324.3" y1="250" x2="324.3" y2="300" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="348" y1="275.0" x2="146" y2="275.0" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/><circle cx="180" cy="275.0" r="12" fill="#0f6e56" stroke="#fff" stroke-width="1.5"/><text x="180" y="275.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="13" font-weight="700" fill="#fff">4</text>
<rect x="376" y="54" width="78" height="96" rx="6" fill="#e1f5ee" stroke="#0f6e56" stroke-width="1"/><line x1="376" y1="73.2" x2="454" y2="73.2" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="376" y1="92.4" x2="454" y2="92.4" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="376" y1="111.6" x2="454" y2="111.6" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="376" y1="130.8" x2="454" y2="130.8" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="415.0" y1="154" x2="415.0" y2="326" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/><circle cx="415.0" cy="72" r="12" fill="#0f6e56" stroke="#fff" stroke-width="1.5"/><text x="415.0" y="72.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="13" font-weight="700" fill="#fff">2</text>
<rect x="470" y="54" width="78" height="150" rx="6" fill="#e1f5ee" stroke="#0f6e56" stroke-width="1"/><line x1="470" y1="72.8" x2="548" y2="72.8" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="470" y1="91.5" x2="548" y2="91.5" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="470" y1="110.2" x2="548" y2="110.2" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="470" y1="129.0" x2="548" y2="129.0" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="470" y1="147.8" x2="548" y2="147.8" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="470" y1="166.5" x2="548" y2="166.5" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="470" y1="185.2" x2="548" y2="185.2" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="509.0" y1="208" x2="509.0" y2="326" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/><circle cx="509.0" cy="72" r="12" fill="#0f6e56" stroke="#fff" stroke-width="1.5"/><text x="509.0" y="72.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="13" font-weight="700" fill="#fff">5</text>
<rect x="562" y="54" width="116" height="150" rx="6" fill="#e1f5ee" stroke="#0f6e56" stroke-width="1"/>
<line x1="591.0" y1="98" x2="591.0" y2="326" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/>
<line x1="620.0" y1="98" x2="620.0" y2="326" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/>
<line x1="649.0" y1="98" x2="649.0" y2="326" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/>
<circle cx="584" cy="72" r="12" fill="#0f6e56" stroke="#fff" stroke-width="1.5"/><text x="584" y="72.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="13" font-weight="700" fill="#fff">6</text>
<text x="628.0" y="74" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9.5" font-weight="600" fill="#0f5040">South-end</text>
<text x="628.0" y="87" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9.5" font-weight="600" fill="#0f5040">Parking Lot</text>
<line x1="670" y1="342.0" x2="152" y2="342.0" stroke="#0f6e56" stroke-width="1.8" marker-end="url(#pk)"/>
<rect x="98" y="321.0" width="52" height="42" rx="6" fill="#eaf3de" stroke="#3b6d11" stroke-width="1.2"/>
<text x="125.0" y="339.0" text-anchor="middle" font-family="Poppins,sans-serif" font-size="10.5" font-weight="700" fill="#27500a">EXIT</text>
<text x="125.0" y="353.0" text-anchor="middle" font-family="Poppins,sans-serif" font-size="7.5" fill="#27500a">Baseline Rd</text>
<line x1="106" y1="342.0" x2="76" y2="342.0" stroke="#3b6d11" stroke-width="2" marker-end="url(#pkx)"/>
<rect x="110" y="446" width="490" height="102" rx="10" fill="#e1f5ee" stroke="#0f6e56" stroke-width="1"/>
<line x1="168.6" y1="458" x2="168.6" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="215.2" y1="458" x2="215.2" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="261.8" y1="458" x2="261.8" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="308.4" y1="458" x2="308.4" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="355.0" y1="458" x2="355.0" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="401.6" y1="458" x2="401.6" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="448.2" y1="458" x2="448.2" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="494.8" y1="458" x2="494.8" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/><line x1="541.4" y1="458" x2="541.4" y2="536" stroke="#0f6e56" stroke-width=".7" stroke-opacity=".55"/>
<circle cx="144" cy="497.0" r="12" fill="#0f6e56" stroke="#fff" stroke-width="1.5"/><text x="144" y="497.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="13" font-weight="700" fill="#fff">7</text>
<text x="365.0" y="497.0" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="13" font-weight="600" fill="#0f5040">West-side Parking Lot</text>
<line x1="470" y1="444" x2="470" y2="368" stroke="#0f6e56" stroke-width="1.8" marker-end="url(#pk)"/>
<circle cx="120" cy="570" r="10" fill="#0f6e56"/><text x="120" y="570" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="11" font-weight="700" fill="#fff">#</text>
<text x="138" y="574" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">Number = order of dismissal (1 first &#8230; 7 last).</text>
<line x1="360" y1="570" x2="388" y2="570" stroke="#0f6e56" stroke-width="1.7" marker-end="url(#pk)"/>
<text x="396" y="574" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">Drive-lane flow. Cars park nose-out (back-in) for a quick exit.</text>
</svg>'''

SANCTUARY_SVG = '''
<svg viewBox="0 0 760 470" xmlns="http://www.w3.org/2000/svg">
<defs>
      <marker id="sar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.6" markerHeight="6.6" orient="auto-start-reverse">
        <path d="M2 1L8 5L2 9" fill="none" stroke="#6e2a2a" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></marker>
    </defs>
<rect x="70" y="40" width="562" height="370" rx="10" fill="none" stroke="#b4b2a9" stroke-width="1.2"/>
<rect x="330" y="98" width="42" height="262" fill="#faf7f0"/>
<text x="351.0" y="229.0" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" fill="#6e2a2a" transform="rotate(-90 351.0 229.0)">Middle aisle &#8212; guarded, no dismissal</text>
<rect x="130" y="140" width="192" height="220" rx="6" fill="#f1efe8" stroke="#d3d1c7"/><rect x="139" y="147.0" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="139" y="183.7" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="139" y="220.3" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="139" y="257.0" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="139" y="293.7" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="139" y="330.3" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/>
<rect x="380" y="140" width="192" height="220" rx="6" fill="#f1efe8" stroke="#d3d1c7"/><rect x="389" y="147.0" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="389" y="183.7" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="389" y="220.3" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="389" y="257.0" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="389" y="293.7" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/><rect x="389" y="330.3" width="174" height="20.5" rx="3" fill="#ffffff" fill-opacity=".5" stroke="#cbc4b6" stroke-width=".6"/>
<rect x="136" y="316" width="180" height="38" rx="5" fill="#eaf2ee" fill-opacity=".96" stroke="#0f6e56" stroke-width="1" stroke-dasharray="3.5 3"/>
<text x="226.0" y="331" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" font-weight="600" fill="#0f5040">North-side seating addition</text>
<text x="226.0" y="344" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" fill="#0f5040">(cry room)</text>
<rect x="70" y="40" width="562" height="58" rx="10" fill="#f7f1e5" stroke="#d8cdba"/>
<text x="351.0" y="62" text-anchor="middle" font-family="Poppins,sans-serif" font-size="11" font-weight="600" letter-spacing="1" fill="#6e2a2a">FRONT &#183; PLATFORM &#183; ALTAR &#183; EAST</text>
<rect x="307.0" y="78" width="88" height="22" rx="3" fill="#f1e8d6" stroke="#9a7b3f" stroke-width="1.1"/>
<text x="351.0" y="89.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#6e2a2a">Casket</text>
<line x1="604.0" y1="352" x2="604.0" y2="118" stroke="#6e2a2a" stroke-width="1.9" marker-end="url(#sar)"/>
<line x1="596.0" y1="116" x2="403.0" y2="116" stroke="#6e2a2a" stroke-width="1.9" marker-end="url(#sar)"/>
<line x1="299.0" y1="116" x2="106.0" y2="116" stroke="#6e2a2a" stroke-width="1.9" marker-end="url(#sar)"/>
<rect x="63" y="318" width="14" height="36" rx="3" fill="#eaf3de" stroke="#3b6d11" stroke-width="1.2"/>
<path d="M98.0 118 L98.0 336 L61 336" fill="none" stroke="#6e2a2a" stroke-width="1.9" marker-end="url(#sar)"/>
<text x="48" y="336" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8.5" font-weight="600" letter-spacing=".1em" fill="#3b6d11" transform="rotate(-90 48 336)">NORTH DOOR</text>
<circle cx="604.0" cy="334" r="10.5" fill="#6e2a2a" stroke="#fff" stroke-width="1.5"/><text x="604.0" y="334.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="10.5" font-weight="700" fill="#fff">1</text>
<circle cx="351.0" cy="116" r="10.5" fill="#6e2a2a" stroke="#fff" stroke-width="1.5"/><text x="351.0" y="116.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="10.5" font-weight="700" fill="#fff">2</text>
<circle cx="98.0" cy="140" r="10.5" fill="#6e2a2a" stroke="#fff" stroke-width="1.5"/><text x="98.0" y="140.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="10.5" font-weight="700" fill="#fff">3</text>
<circle cx="84" cy="336" r="10.5" fill="#6e2a2a" stroke="#fff" stroke-width="1.5"/><text x="84" y="336.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="10.5" font-weight="700" fill="#fff">4</text>
<rect x="70" y="364" width="562" height="46" rx="10" fill="#f7f1e5" stroke="#d8cdba"/>
<rect x="70" y="364" width="562" height="12" fill="#f7f1e5"/>
<text x="351.0" y="388.0" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="10" font-weight="600" letter-spacing=".04em" fill="#9a7b3f">VESTIBULE / BACK &#8212; dismiss from here first &#183; WEST</text>
<text x="56" y="250.0" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" letter-spacing=".15em" fill="#8a7f6c" transform="rotate(-90 56 250.0)">NORTH SIDE</text>
<text x="646" y="250.0" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" letter-spacing=".15em" fill="#8a7f6c" transform="rotate(90 646 250.0)">SOUTH SIDE</text>
<text x="70" y="436" font-family="Poppins,sans-serif" font-size="8.6" fill="#4a4234"><tspan font-weight="700" fill="#6e2a2a">Order of dismissal:</tspan> (1) up the south aisle &#183; (2) across the front past the casket &#183; (3) down the north aisle &#183; (4) out the north side door.</text>
<text x="70" y="452" font-family="Poppins,sans-serif" font-size="8.6" fill="#4a4234">Released from the back first; the middle aisle stays guarded (no dismissal).</text>
</svg>'''

POSITIONS_MAP_SVG = '''
<svg viewBox="0 0 744 712" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="20" width="664" height="540" rx="10" fill="none" stroke="#b4b2a9" stroke-width="1.2"/>
<rect x="50" y="24" width="250" height="42" rx="6" fill="#fff" stroke="#d8cdba"/><text x="175.0" y="40" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" font-weight="600" letter-spacing=".06em" fill="#6e2a2a">BACK OFFICE</text><text x="175.0" y="55" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">23 &#183; 24 &#183; 25 &#183; 26</text>
<rect x="308" y="24" width="150" height="42" rx="6" fill="#fff" stroke="#d8cdba"/><text x="383.0" y="40" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" font-weight="600" letter-spacing=".06em" fill="#6e2a2a">VIDEO</text><text x="383.0" y="55" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">29</text>
<rect x="560" y="24" width="134" height="42" rx="6" fill="#fff" stroke="#d8cdba"/><text x="627.0" y="40" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" font-weight="600" letter-spacing=".06em" fill="#6e2a2a">BACKDOOR</text><text x="627.0" y="55" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">1</text>
<rect x="116" y="72" width="496" height="426" rx="6" fill="#fbfdfc" stroke="#0f6e56" stroke-width="1.4"/>
<rect x="116" y="72" width="496" height="56" rx="6" fill="#f7f1e5" stroke="#d8cdba"/>
<text x="364.0" y="90" text-anchor="middle" font-family="Poppins,sans-serif" font-size="10" font-weight="600" letter-spacing="1" fill="#6e2a2a">FRONT &#183; PLATFORM &#183; ALTAR</text>
<rect x="160" y="138.0" width="170" height="107.1" rx="4" fill="#ece6f6" stroke="#7d6bb0" stroke-width="1.1"/>
<rect x="160" y="245.1" width="170" height="133.8" rx="4" fill="#f7ead7" stroke="#c08a3e" stroke-width="1.1"/>
<rect x="160" y="378.9" width="170" height="107.1" rx="4" fill="#f6e0dc" stroke="#c0584e" stroke-width="1.1"/>
<rect x="398" y="138.0" width="170" height="107.1" rx="4" fill="#dfeaf3" stroke="#4f7fae" stroke-width="1.1"/>
<rect x="398" y="245.1" width="170" height="133.8" rx="4" fill="#f3ecd6" stroke="#9a7b3f" stroke-width="1.1"/>
<rect x="398" y="378.9" width="170" height="107.1" rx="4" fill="#d9efe8" stroke="#0f6e56" stroke-width="1.1"/>
<rect x="168" y="142.3" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="169.1" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="195.8" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="222.6" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="249.4" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="276.1" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="302.9" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="329.7" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="356.4" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="383.2" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="410.0" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="436.7" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="168" y="463.5" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/>
<rect x="406" y="142.3" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="169.1" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="195.8" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="222.6" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="249.4" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="276.1" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="302.9" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="329.7" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="356.4" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="383.2" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="410.0" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="436.7" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/><rect x="406" y="463.5" width="154" height="13.4" rx="3" fill="#ffffff" fill-opacity="0.55" stroke="#c9c2b3" stroke-width=".7"/>
<rect x="624" y="116" width="80" height="370.0" rx="6" fill="#fff" stroke="#d8cdba"/>
<text x="664" y="130" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8.5" font-weight="600" letter-spacing=".1em" fill="#9a7b3f">ROW</text>
<text x="664" y="151.9" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">1</text>
<line x1="612" y1="151.4" x2="624" y2="151.4" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="178.7" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">2</text>
<line x1="612" y1="178.2" x2="624" y2="178.2" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="205.4" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">3</text>
<line x1="612" y1="204.9" x2="624" y2="204.9" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="232.2" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">4</text>
<line x1="612" y1="231.7" x2="624" y2="231.7" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="259.0" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">5</text>
<line x1="612" y1="258.5" x2="624" y2="258.5" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="285.7" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">6</text>
<line x1="612" y1="285.2" x2="624" y2="285.2" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="312.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">7</text>
<line x1="612" y1="312.0" x2="624" y2="312.0" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="339.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">8</text>
<line x1="612" y1="338.8" x2="624" y2="338.8" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="366.0" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">9</text>
<line x1="612" y1="365.5" x2="624" y2="365.5" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="392.8" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">10</text>
<line x1="612" y1="392.3" x2="624" y2="392.3" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="419.6" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">11</text>
<line x1="612" y1="419.1" x2="624" y2="419.1" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="446.3" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">12</text>
<line x1="612" y1="445.8" x2="624" y2="445.8" stroke="#d8cdba" stroke-width=".6"/>
<text x="664" y="473.1" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" fill="#4a4234">13</text>
<line x1="612" y1="472.6" x2="624" y2="472.6" stroke="#d8cdba" stroke-width=".6"/>
<rect x="332" y="134" width="64" height="356.0" fill="#faf7f0"/>
<circle cx="364.0" cy="312.0" r="11" fill="#0f6e56"/><text x="364.0" y="312.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">4</text>
<text x="364.0" y="419.1" text-anchor="middle" font-family="Poppins,sans-serif" font-size="7.5" fill="#8a7f6c" transform="rotate(-90 364.0 419.1)">Middle aisle</text>
<circle cx="139.0" cy="191.53846153846155" r="12" fill="#7d6bb0"/><text x="139.0" y="192.03846153846155" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#ffffff">6</text>
<circle cx="139.0" cy="312.0" r="12" fill="#c08a3e"/><text x="139.0" y="312.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#ffffff">7</text>
<circle cx="139.0" cy="432.46153846153845" r="12" fill="#c0584e"/><text x="139.0" y="432.96153846153845" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#ffffff">9</text>
<circle cx="589.0" cy="191.53846153846155" r="12" fill="#4f7fae"/><text x="589.0" y="192.03846153846155" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#ffffff">5</text>
<circle cx="589.0" cy="312.0" r="12" fill="#9a7b3f"/><text x="589.0" y="312.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#ffffff">8</text>
<circle cx="589.0" cy="432.46153846153845" r="12" fill="#0f6e56"/><text x="589.0" y="432.96153846153845" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#ffffff">10</text>
<circle cx="306" cy="106" r="11" fill="#0f6e56"/><text x="306" y="106.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">1B</text>
<circle cx="422" cy="106" r="11" fill="#0f6e56"/><text x="422" y="106.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">1A</text>
<circle cx="338.0" cy="116" r="11" fill="#0f6e56"/><text x="338.0" y="116.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">2</text>
<circle cx="390.0" cy="116" r="11" fill="#0f6e56"/><text x="390.0" y="116.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">3</text>
<rect x="259.0" y="142.3846153846154" width="58" height="18" rx="4" fill="#f1e8d6" stroke="#9a7b3f"/><text x="288" y="151.8846153846154" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="8.5" fill="#6e2a2a">BGG &#183; 27</text>
<rect x="408.0" y="142.3846153846154" width="64" height="18" rx="4" fill="#f1e8d6" stroke="#9a7b3f"/><text x="440" y="151.8846153846154" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="8.5" fill="#6e2a2a">28 &#183; PGG Jr</text>
<rect x="175.0" y="169.15384615384616" width="42" height="18" rx="4" fill="#f1e8d6" stroke="#9a7b3f"/><text x="196" y="178.65384615384616" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="8.5" fill="#6e2a2a">JO</text>
<rect x="175.0" y="195.9230769230769" width="42" height="18" rx="4" fill="#f1e8d6" stroke="#9a7b3f"/><text x="196" y="205.4230769230769" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="8.5" fill="#6e2a2a">EGB</text>
<rect x="179.0" y="383.3076923076923" width="46" height="18" rx="4" fill="#f1e8d6" stroke="#9a7b3f"/><text x="202" y="392.8076923076923" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="8.5" fill="#6e2a2a">AGBJr</text>
<rect x="175.0" y="436.84615384615387" width="42" height="18" rx="4" fill="#f1e8d6" stroke="#9a7b3f"/><text x="196" y="446.34615384615387" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="8.5" fill="#6e2a2a">ER</text>
<rect x="511.0" y="222.69230769230768" width="42" height="18" rx="4" fill="#f1e8d6" stroke="#9a7b3f"/><text x="532" y="232.19230769230768" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="8.5" fill="#6e2a2a">JGA</text>
<circle cx="245.0" cy="474.61538461538464" r="11" fill="#0f6e56"/><text x="245.0" y="475.11538461538464" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">12</text>
<circle cx="483.0" cy="474.61538461538464" r="11" fill="#0f6e56"/><text x="483.0" y="475.11538461538464" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">13</text>
<rect x="46" y="504" width="150" height="52" rx="6" fill="#efdcdc" stroke="#8a3a3a" stroke-width="1.1"/>
<rect x="86" y="510" width="104" height="8" rx="2" fill="#fff" fill-opacity=".6" stroke="#c9c2b3"/>
<rect x="86" y="524" width="104" height="8" rx="2" fill="#fff" fill-opacity=".6" stroke="#c9c2b3"/>
<rect x="86" y="538" width="104" height="8" rx="2" fill="#fff" fill-opacity=".6" stroke="#c9c2b3"/>
<circle cx="64" cy="530" r="12" fill="#8a3a3a"/><text x="64" y="530.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#fff">11</text>
<text x="138" y="551" text-anchor="middle" font-family="Poppins,sans-serif" font-size="7.5" fill="#6e2a2a">Additional seating</text>
<rect x="206" y="504" width="406" height="52" rx="6" fill="#f7f1e5" stroke="#d8cdba"/>
<text x="250" y="518" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" font-weight="600" letter-spacing=".08em" fill="#9a7b3f">VESTIBULE</text>
<circle cx="226" cy="540" r="11" fill="#0f6e56"/><text x="226" y="540.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">14</text>
<circle cx="260" cy="540" r="11" fill="#0f6e56"/><text x="260" y="540.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">15</text>
<circle cx="294" cy="540" r="11" fill="#0f6e56"/><text x="294" y="540.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">16</text>
<circle cx="328" cy="540" r="11" fill="#0f6e56"/><text x="328" y="540.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">22</text>
<circle cx="362" cy="540" r="11" fill="#0f6e56"/><text x="362" y="540.5" text-anchor="middle" dominant-baseline="central" font-family="Poppins,sans-serif" font-size="9" font-weight="600" fill="#e1f5ee">17</text>
<rect x="430" y="510" width="86" height="17" rx="3" fill="#fff" stroke="#b4b2a9"/>
<text x="473" y="519" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" fill="#5f5e5a">Men restroom</text>
<rect x="430" y="531" width="86" height="17" rx="3" fill="#fff" stroke="#b4b2a9"/>
<text x="473" y="540" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" fill="#5f5e5a">Women</text>
<text x="52" y="290" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" letter-spacing=".15em" fill="#8a7f6c" transform="rotate(-90 52 290)">NORTH SIDE</text>
<text x="722" y="300" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" letter-spacing=".15em" fill="#8a7f6c" transform="rotate(90 722 300)">SOUTH SIDE</text>
<text x="40" y="580" font-family="Poppins,sans-serif" font-size="9" font-weight="600" letter-spacing=".08em" fill="#6e2a2a">RESERVED SEATING</text>
<text x="40" y="596" font-family="Poppins,sans-serif" font-size="8.5"><tspan font-weight="600" fill="#9a7b3f">BGG</tspan><tspan fill="#4a4234"> = Bernie G. Garcia</tspan></text>
<text x="250" y="596" font-family="Poppins,sans-serif" font-size="8.5"><tspan font-weight="600" fill="#9a7b3f">PGG Jr</tspan><tspan fill="#4a4234"> = Paul Garcia Jr.</tspan></text>
<text x="470" y="596" font-family="Poppins,sans-serif" font-size="8.5"><tspan font-weight="600" fill="#9a7b3f">EGB</tspan><tspan fill="#4a4234"> = Ernie G. Borunda</tspan></text>
<text x="40" y="612" font-family="Poppins,sans-serif" font-size="8.5"><tspan font-weight="600" fill="#9a7b3f">JGA</tspan><tspan fill="#4a4234"> = John G. Alvarado</tspan></text>
<text x="250" y="612" font-family="Poppins,sans-serif" font-size="8.5"><tspan font-weight="600" fill="#9a7b3f">JO</tspan><tspan fill="#4a4234"> = Joshua O&#8217;Campo Sr.</tspan></text>
<text x="470" y="612" font-family="Poppins,sans-serif" font-size="8.5"><tspan font-weight="600" fill="#9a7b3f">ER</tspan><tspan fill="#4a4234"> = Lalo Ruiz</tspan></text>
<text x="40" y="628" font-family="Poppins,sans-serif" font-size="8.5"><tspan font-weight="600" fill="#9a7b3f">AGBJr</tspan><tspan fill="#4a4234"> = Alex G. Borunda Jr.</tspan></text>
<text x="40" y="644" font-family="Poppins,sans-serif" font-size="8.5" fill="#4a4234"><tspan font-weight="600" fill="#0f6e56">Parking</tspan> 18 &amp; 19&#8211;21<tspan dx="18" font-weight="600" fill="#0f6e56">Substitutes</tspan> 30+</text>
</svg>'''
