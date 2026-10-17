import base64
from pathlib import Path

import streamlit as st

from theme import top_right_button

PROFILE_IMAGE = Path(__file__).resolve().parent / "assets" / "kartik photo 1.jpeg"

PROFILE_NAME = "Kartik"
PROFILE_ROLE = "Software developer"


@st.cache_data(show_spinner=False)
def _profile_image_base64() -> str | None:
    """Read the profile photo once and keep it cached between reruns."""
    try:
        return base64.b64encode(PROFILE_IMAGE.read_bytes()).decode("ascii")
    except OSError:
        return None


# The card geometry (--pc-card, --pc-name-h) is shared by the visual card and
# the invisible button placed on top of it, so the two always line up.
# Plain string (not an f-string) so the CSS braces stay readable;
# __PHOTO__ is swapped in below.
PROFILE_CSS = """
<style>
:root {
    --pc-card: clamp(150px, 20vw, 230px);
    --pc-name-h: 84px;
}

/* ---------- stage ---------- */

.pc-stage {
    position: fixed;
    inset: 0;
    z-index: 2;
    overflow: hidden;
    pointer-events: none;
}

.pc-vignette {
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse at 50% 46%, rgba(70, 12, 18, 0.5) 0%, transparent 52%),
        radial-gradient(ellipse at center, transparent 38%, rgba(0, 0, 0, 0.8) 100%);
}

.pc-beam {
    position: absolute;
    inset: 0;
    background: radial-gradient(
        ellipse 42% 70% at 50% 0%,
        rgba(255, 255, 255, 0.11),
        transparent 72%
    );
    animation: pc-breathe 7s ease-in-out infinite alternate;
}

.pc-grain {
    position: absolute;
    inset: 0;
    opacity: 0.07;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

/* letterbox bars: open like a curtain on load, then rest as a thin frame */

.pc-bar {
    position: absolute;
    left: 0;
    right: 0;
    height: 6vh;
    background: #000;
    animation: pc-bars 1.3s var(--ease) backwards;
}

.pc-bar-top { top: 0; }
.pc-bar-bottom { bottom: 0; }

/* ---------- title ---------- */

.pc-title {
    position: absolute;
    left: 0;
    right: 0;
    top: max(9vh, calc(50% - (var(--pc-card) + var(--pc-name-h)) / 2 - clamp(64px, 11vh, 110px)));
    margin: 0;
    text-align: center;
    font-family: var(--font-display);
    font-size: clamp(38px, 7vw, 76px);
    font-weight: 800;
    line-height: 1;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text);
    animation: pc-title 1.2s var(--ease) 0.7s backwards;
}

/* ---------- profile card ---------- */

.pc-card {
    position: absolute;
    left: 50%;
    top: 50%;
    width: var(--pc-card);
    height: calc(var(--pc-card) + var(--pc-name-h));
    transform: translate(-50%, -50%);
}

.pc-inner {
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.4s var(--ease);
    animation: pc-rise 1.1s var(--ease) 1.25s backwards;
}

.pc-frame {
    width: var(--pc-card);
    height: var(--pc-card);
    border-radius: 8px;
    overflow: hidden;
    background: linear-gradient(135deg, #333333, #18181c);
    box-shadow: 0 0 0 3px transparent, 0 18px 50px rgba(0, 0, 0, 0.6);
    transition: box-shadow 0.4s var(--ease);
}

.pc-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 20%;
    display: block;
    transition: transform 0.6s var(--ease);
}

.pc-initial {
    width: 100%;
    height: 100%;
    display: grid;
    place-items: center;
    font-family: var(--font-display);
    font-size: calc(var(--pc-card) * 0.5);
    font-weight: 800;
    color: #d8d8d8;
}

.pc-name {
    margin-top: 16px;
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 700;
    letter-spacing: 0.05em;
    color: #b8b8b8;
    transition: color 0.3s ease;
}

.pc-role {
    margin-top: 2px;
    font-size: 14px;
    color: var(--text-mute);
    transition: color 0.3s ease;
}

/* ---------- hover / keyboard focus (the invisible button is on top) ---------- */

body:has(.st-key-enter_card:hover) .pc-inner,
body:has(.st-key-enter_card button:focus-visible) .pc-inner {
    transform: translateY(-6px) scale(1.04);
}

body:has(.st-key-enter_card:hover) .pc-frame,
body:has(.st-key-enter_card button:focus-visible) .pc-frame {
    box-shadow: 0 0 0 3px #ffffff, 0 0 80px var(--accent-glow), 0 18px 50px rgba(0, 0, 0, 0.6);
}

body:has(.st-key-enter_card:hover) .pc-img,
body:has(.st-key-enter_card button:focus-visible) .pc-img {
    transform: scale(1.06);
}

body:has(.st-key-enter_card:hover) .pc-name,
body:has(.st-key-enter_card button:focus-visible) .pc-name,
body:has(.st-key-enter_card:hover) .pc-role,
body:has(.st-key-enter_card button:focus-visible) .pc-role {
    color: #ffffff;
}

body:has(.st-key-enter_card:active) .pc-inner {
    transform: scale(0.98);
}

/* ---------- the real Streamlit button, invisible, covering the card ---------- */

.st-key-enter_card {
    position: fixed;
    top: 50%;
    left: 50%;
    width: var(--pc-card);
    height: calc(var(--pc-card) + var(--pc-name-h));
    transform: translate(-50%, -50%);
    z-index: 5;
    gap: 0;
}

.st-key-enter_card [data-testid="stElementContainer"],
.st-key-enter_card [data-testid="stButton"],
.st-key-enter_card button {
    width: 100%;
    height: 100%;
}

.st-key-enter_card button {
    opacity: 0;
    padding: 0;
    cursor: pointer;
}

/* ---------- motion ---------- */

@keyframes pc-bars {
    from { height: 50.5vh; }
}

@keyframes pc-title {
    from { opacity: 0; letter-spacing: 0.5em; filter: blur(10px); }
}

@keyframes pc-rise {
    from { opacity: 0; transform: translateY(46px) scale(0.94); filter: blur(10px); }
}

@keyframes pc-breathe {
    from { opacity: 0.55; }
    to { opacity: 1; }
}
</style>
"""

PROFILE_HTML = """
<div class="pc-stage">
    <div class="pc-vignette"></div>
    <div class="pc-beam"></div>
    <div class="pc-grain"></div>

    <div class="pc-title" role="heading" aria-level="1">Who's here?</div>

    <div class="pc-card">
        <div class="pc-inner">
            <div class="pc-frame">__PHOTO__</div>
            <div class="pc-name">__NAME__</div>
            <div class="pc-role">__ROLE__</div>
        </div>
    </div>

    <div class="pc-bar pc-bar-top"></div>
    <div class="pc-bar pc-bar-bottom"></div>
</div>
"""


def profile_selection():
    """Cinematic 'Who's here?' screen. Clicking the card enters the site."""
    image_base64 = _profile_image_base64()

    if image_base64:
        photo_html = (
            f'<img class="pc-img" alt="{PROFILE_NAME}" '
            f'src="data:image/jpeg;base64,{image_base64}">'
        )
    else:
        photo_html = f'<div class="pc-initial">{PROFILE_NAME[0]}</div>'

    page_html = (
        PROFILE_HTML
        .replace("__PHOTO__", photo_html)
        .replace("__NAME__", PROFILE_NAME)
        .replace("__ROLE__", PROFILE_ROLE)
    )

    st.html(PROFILE_CSS + page_html)

    # Admin entry: top-right corner, replaces the old sidebar button.
    top_right_button("Admin", "admin", key="open_admin")

    # The whole card is the click target: a real, keyboard-focusable button
    # stretched over the card and made invisible by the CSS above.
    with st.container(key="enter_card"):
        if st.button("Enter portfolio", key="enter_portfolio"):
            st.session_state.view = "home"
            st.rerun()

    if image_base64 is None:
        # A toast stays visible above the full-screen stage; a warning would not.
        st.toast(
            "Profile image not found. "
            "Place 'kartik photo 1.jpeg' inside the assets folder."
        )
