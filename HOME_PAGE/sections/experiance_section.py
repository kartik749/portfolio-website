import streamlit as st

from HOME_PAGE.components.cards import experience_card
from HOME_PAGE.data.portfolio_repository import get_experiences

# Vertical timeline. Each entry is a native <details> element, so opening and
# closing works with mouse, touch and keyboard and needs no JavaScript.
EXPERIENCE_CSS = """
<style>
.experience-section {
    padding: 20px 6% 50px 6%;
}

.experience-title {
    font-size: 28px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 26px;
}

/* the rail */

.exp-timeline {
    position: relative;
    max-width: 860px;
    padding-left: 36px;
}

.exp-timeline::before {
    content: "";
    position: absolute;
    left: 6px;
    top: 10px;
    bottom: 10px;
    width: 2px;
    background: linear-gradient(var(--accent), rgba(255, 255, 255, 0.12));
}

/* one entry */

.exp-item {
    position: relative;
    margin-bottom: 14px;
    border-radius: 10px;
    border: 1px solid var(--line);
    background: linear-gradient(135deg, #25252b, #151519);
    interpolate-size: allow-keywords;
    transition: border-color 0.3s ease;
}

.exp-item:hover,
.exp-item[open] {
    border-color: var(--line-strong);
}

.exp-dot {
    position: absolute;
    left: -36px;
    top: 26px;
    width: 14px;
    height: 14px;
    box-sizing: border-box;
    border-radius: 50%;
    background: var(--bg);
    border: 2px solid #5a5a62;
    transition: background 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}

.exp-item[open] .exp-dot {
    background: var(--accent);
    border-color: var(--accent);
    box-shadow: 0 0 0 5px var(--accent-soft);
}

/* the always-visible header: duration on top, company below */

.exp-head {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    column-gap: 16px;
    align-items: center;
    padding: 16px 20px;
    cursor: pointer;
    list-style: none;
}

.exp-head::-webkit-details-marker {
    display: none;
}

.exp-when {
    grid-column: 1;
    font-size: 13px;
    color: var(--text-mute);
}

.exp-company {
    grid-column: 1;
    margin-top: 2px;
    font-size: 22px;
    font-weight: 700;
    color: var(--text);
    overflow-wrap: anywhere;
}

.exp-chevron {
    grid-column: 2;
    grid-row: 1 / span 2;
    width: 9px;
    height: 9px;
    border-right: 2px solid #9a9aa2;
    border-bottom: 2px solid #9a9aa2;
    transform: rotate(45deg) translate(-2px, -2px);
    transition: transform 0.35s var(--ease), border-color 0.2s ease;
}

.exp-head:hover .exp-chevron {
    border-color: var(--text);
}

.exp-item[open] .exp-chevron {
    transform: rotate(-135deg) translate(-2px, -2px);
}

/* the panel that slides down */

.exp-body {
    padding: 0 20px 20px 20px;
}

.exp-role {
    margin-bottom: 10px;
    font-size: 15px;
    font-weight: 600;
    color: var(--accent);
}

.exp-desc {
    margin: 0;
    max-width: 68ch;
    font-size: 14.5px;
    line-height: 1.7;
    color: var(--text-dim);
}

ul.exp-desc {
    padding-left: 18px;
}

ul.exp-desc li + li {
    margin-top: 6px;
}

/* Browsers that support ::details-content animate both opening and closing. */
.exp-item::details-content {
    block-size: 0;
    overflow: hidden;
    transition:
        block-size 0.38s var(--ease),
        content-visibility 0.38s allow-discrete;
}

.exp-item[open]::details-content {
    block-size: auto;
}

/* Everywhere else the text still eases in when opened. */
.exp-item[open] .exp-body {
    animation: exp-reveal 0.42s var(--ease) backwards;
}

@keyframes exp-reveal {
    from { opacity: 0; transform: translateY(-8px); }
}

@media (max-width: 600px) {
    .experience-section {
        padding: 16px 4% 36px 4%;
    }

    .experience-title {
        font-size: 24px;
    }

    .exp-company {
        font-size: 19px;
    }

    .exp-head {
        padding: 14px 16px;
    }

    .exp-body {
        padding: 0 16px 18px 16px;
    }
}
</style>
"""


def experience_section():
    experiences = get_experiences()

    if not experiences:
        return

    # The first (latest) entry starts open; the rest are collapsed.
    items_html = "".join(
        experience_card(
            company=experience["company"],
            role=experience["role"],
            duration=experience["duration"],
            description=experience["description"],
            is_open=(index == 0),
        )
        for index, experience in enumerate(experiences)
    )

    st.html(
        EXPERIENCE_CSS
        + f"""
    <div class="experience-section">
        <div class="experience-title">Experience</div>
        <div class="exp-timeline">
            {items_html}
        </div>
    </div>
    """
    )
