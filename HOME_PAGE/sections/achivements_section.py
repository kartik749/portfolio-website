
import streamlit as st

from HOME_PAGE.components.cards import achievement_card
from HOME_PAGE.data.portfolio_repository import get_achivements


def achievements_section():

    achievements = get_achivements()

    cards_html = ""

    for item in achievements:
        cards_html += achievement_card(
            category=item["category"],
            title=item["title"],
            description=item["description"]
        )

    st.html(f"""
    <style>
    .achievements-section {{
        padding: 20px 6% 50px;
    }}

    .achievements-title {{
        font-size: 28px;
        font-weight: 700;
        color: white;
        margin-bottom: 25px;
    }}

    .achievements-row {{
        display: flex;
        gap: 22px;
        overflow-x: auto;
        padding: 10px 5px 25px;
    }}

    .achievement-card {{
        flex: 0 0 330px;
        min-height: 170px;
        padding: 25px;
        box-sizing: border-box;
        border-radius: 10px;
        background: linear-gradient(135deg, #25252b, #151519);
        border: 1px solid rgba(255,255,255,0.08);
        transition: transform 0.3s ease, border 0.3s ease;
    }}

    .achievement-card:hover {{
        transform: scale(1.04);
        border-color: rgba(255,255,255,0.3);
    }}

    .achievement-label {{
        font-size: 13px;
        color: #e50914;
        margin-bottom: 10px;
    }}

    .achievement-title {{
        font-size: 21px;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
    }}

    .achievement-description {{
        font-size: 14px;
        line-height: 1.5;
        color: #bdbdbd;
    }}
    </style>

    <div class="achievements-section">
        <div class="achievements-title">Highlights</div>
        <div class="achievements-row">
            {cards_html}
        </div>
    </div>
    """)
