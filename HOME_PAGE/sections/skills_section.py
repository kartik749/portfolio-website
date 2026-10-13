import streamlit as st

from HOME_PAGE.components.cards import skill_card
from HOME_PAGE.data.portfolio_repository import get_skills


def skills_section():

    skills = get_skills()
    cards_html = ""

    for skill in skills:
        cards_html += skill_card(skill)

    st.html(f"""
    <style>

    .content-section {{
        padding: 20px 6% 40px 6%;
    }}

    .content-title {{
        font-size: 28px;
        font-weight: 700;
        color: white;
        margin-bottom: 22px;
    }}

    .skills-row {{
        display: flex;
        gap: 18px;
        overflow-x: auto;
        padding: 10px 5px 20px 5px;
    }}

    .skill-card {{
        min-width: 160px;
        height: 90px;

        border-radius: 8px;

        background:
            linear-gradient(
                135deg,
                #24242a,
                #151519
            );

        border: 1px solid rgba(255,255,255,0.08);

        display: flex;
        align-items: center;
        justify-content: center;

        color: #eeeeee;

        font-size: 17px;
        font-weight: 600;

        transition:
            transform 0.25s ease,
            border 0.25s ease,
            background 0.25s ease;
    }}

    .skill-card:hover {{
        transform: scale(1.08);

        border: 1px solid rgba(255,255,255,0.35);

        background: #2d2d34;
    }}

    </style>

    <div class="content-section">

        <div class="content-title">
            Featured Skills
        </div>

        <div class="skills-row">

            {cards_html}

        </div>

    </div>
    """)