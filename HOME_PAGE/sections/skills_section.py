import streamlit as st

from HOME_PAGE.components.cards import skill_card
from HOME_PAGE.data.portfolio_repository import get_skills

# Fixed number of columns per screen size:
#   desktop 4  ·  tablet (<= 1024px) 3  ·  mobile (<= 600px) 2
SKILLS_CSS = """
<style>
.skills-section {
    padding: 20px 6% 40px 6%;
}

.skills-title {
    font-size: 28px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 22px;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 16px;
}

.skill-tile {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 12px;
    min-height: 124px;
    padding: 18px 12px;
    box-sizing: border-box;
    border-radius: 10px;
    background: linear-gradient(135deg, #25252b, #151519);
    border: 1px solid var(--line);
    transition:
        transform 0.25s var(--ease),
        border-color 0.25s ease,
        box-shadow 0.25s ease;
}

.skill-tile:hover {
    transform: translateY(-3px);
    border-color: rgba(229, 9, 20, 0.55);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
}

.skill-icon {
    width: 44px;
    height: 44px;
    object-fit: contain;
}

.skill-icon-invert {
    filter: invert(1);
}

.skill-mono {
    width: 44px;
    height: 44px;
    display: grid;
    place-items: center;
    border-radius: 50%;
    background: var(--accent-soft);
    color: var(--text);
    font-family: var(--font-display);
    font-size: 26px;
    font-weight: 700;
}

.skill-name {
    font-size: 15px;
    font-weight: 600;
    color: #eeeeee;
    text-align: center;
    overflow-wrap: anywhere;
}

@media (max-width: 1024px) {
    .skills-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }
}

@media (max-width: 600px) {
    .skills-section {
        padding: 16px 4% 28px 4%;
    }

    .skills-title {
        font-size: 24px;
    }

    .skills-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 12px;
    }

    .skill-tile {
        min-height: 108px;
    }
}
</style>
"""


def skills_section():
    skills = get_skills()

    if not skills:
        return

    tiles_html = "".join(skill_card(skill) for skill in skills)

    st.html(
        SKILLS_CSS
        + f"""
    <div class="skills-section">
        <div class="skills-title">Featured Skills</div>
        <div class="skills-grid">
            {tiles_html}
        </div>
    </div>
    """
    )
