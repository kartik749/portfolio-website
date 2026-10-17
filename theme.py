"""Shared design tokens and one-time global CSS.

Every section reads its colours, fonts and easing from the CSS variables
below, so changing the look of the whole site means editing this file only.
Call inject_global_css() once, from app.py.
"""

import streamlit as st

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Instrument+Sans:wght@400;500;600;700&display=swap');

:root {
    --bg: #0b0b0f;
    --bg-raised: #17171b;
    --surface: #1e1e24;
    --line: rgba(255, 255, 255, 0.09);
    --line-strong: rgba(255, 255, 255, 0.28);

    --text: #ffffff;
    --text-dim: #c5c5c5;
    --text-mute: #8a8a92;

    --accent: #e50914;
    --accent-soft: rgba(229, 9, 20, 0.18);
    --accent-glow: rgba(229, 9, 20, 0.45);

    --font-display: 'Big Shoulders Display', 'Arial Narrow', Arial, sans-serif;
    --font-body: 'Instrument Sans', 'Segoe UI', Arial, sans-serif;

    --ease: cubic-bezier(0.2, 0.8, 0.2, 1);

    /* lets <details> panels animate to their natural height */
    interpolate-size: allow-keywords;
}

/* ---------- page background ---------- */

[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at center, #1a1a22 0%, var(--bg) 65%);
}

.stApp {
    font-family: var(--font-body);
}

.block-container {
    padding-top: 0rem;
}

/* ---------- no sidebar, no Streamlit toolbar ---------- */
/* The toolbar (Deploy / menu) sits where the Admin button lives. */

[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapseButton"],
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    display: none !important;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* ---------- top-right corner button (Admin / Back) ---------- */

.st-key-admin_btn {
    position: fixed;
    top: 14px;
    right: 20px;
    z-index: 1000001;
    width: auto !important;
}

.st-key-admin_btn button {
    min-height: 0;
    padding: 6px 18px;
    border-radius: 999px;
    border: 1px solid var(--line-strong);
    background: rgba(20, 20, 24, 0.55);
    backdrop-filter: blur(10px);
    color: var(--text-dim);
    font-family: var(--font-body);
    font-weight: 500;
    transition: color 0.2s ease, border-color 0.2s ease, background 0.2s ease;
}

.st-key-admin_btn button:hover {
    color: var(--text);
    border-color: var(--accent);
    background: rgba(229, 9, 20, 0.16);
}

/* ---------- accessibility ---------- */

a:focus-visible,
button:focus-visible,
summary:focus-visible {
    outline: 2px solid #ffffff;
    outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
</style>
"""


def inject_global_css() -> None:
    """Inject the shared stylesheet. Call once per run, before any view."""
    st.html(GLOBAL_CSS)


def top_right_button(label: str, target_view: str, key: str) -> None:
    """Render the pill button fixed to the top-right corner.

    Clicking it switches st.session_state.view to `target_view`.
    """
    with st.container(key="admin_btn"):
        if st.button(label, key=key):
            st.session_state.view = target_view
            st.rerun()
