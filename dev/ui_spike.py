"""30-second browser check for the features the redesign relies on.

Run from the project root:   streamlit run dev/ui_spike.py
Each line should look the way its description says. If one doesn't,
tell me which one and I'll switch that part to a fallback.
"""

import streamlit as st

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Instrument+Sans:wght@400;600&display=swap');
.t { font: 16px 'Instrument Sans', sans-serif; color: #ddd; margin: 22px 0 6px; }
.big { font: 800 44px 'Big Shoulders Display', Impact, sans-serif; color: #fff; letter-spacing: .1em; }
.box { padding: 12px 16px; border: 1px solid #555; border-radius: 8px; color: #fff; }
body:has(.hov:hover) .target { background: #e50914; }
details.d { border: 1px solid #555; border-radius: 8px; color: #fff; interpolate-size: allow-keywords; }
details.d summary { padding: 12px 16px; cursor: pointer; }
details.d::details-content { block-size: 0; overflow: hidden; transition: block-size .38s ease, content-visibility .38s allow-discrete; }
details.d[open]::details-content { block-size: auto; }
details.d .in { padding: 0 16px 16px; }
</style>

<div class="t">1. Fonts: this should be a tall, condensed poster-style face (not Arial).</div>
<div class="big">WHO'S HERE?</div>

<div class="t">2. :has() hover: hover the left box, the right box should turn red.</div>
<div style="display:flex; gap:12px">
  <div class="box hov">hover me</div><div class="box target">I turn red</div>
</div>

<div class="t">3. Click-to-slide: click the bar. The text should glide open and glide shut (instant = still works, just not animated).</div>
<details class="d" name="spike"><summary>Travlmate.ai · click me</summary><div class="in">This text slides down.</div></details>
<br>
<details class="d" name="spike"><summary>Second entry (opening this closes the first)</summary><div class="in">Only one is open at a time.</div></details>

<div class="t">4. Icons from the CDN: you should see the Python and Flutter logos.</div>
<img width="44" height="44" alt="" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/python/python-original.svg">
<img width="44" height="44" alt="" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/flutter/flutter-original.svg">
""")
