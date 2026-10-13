
import streamlit as st

from HOME_PAGE.components.cards import coding_profile_card
from HOME_PAGE.data.portfolio_repository import get_coding_profiles


def coding_profiles_section():

    profiles = get_coding_profiles()

    cards_html = ""

    for profile in profiles:
        cards_html += coding_profile_card(
            platform=profile["platform"],
            description=profile["description"],
            url=profile["url"]
        )

    st.html(f"""
    <style>
    .coding-section {{
        padding: 20px 6% 60px;
    }}

    .coding-title {{
        font-size: 28px;
        font-weight: 700;
        color: white;
        margin-bottom: 25px;
    }}

    .coding-row {{
        display: flex;
        gap: 22px;
        overflow-x: auto;
        padding: 10px 5px 25px;
    }}

    .coding-card {{
        flex: 0 0 220px;
        min-height: 140px;
        padding: 25px;
        box-sizing: border-box;
        border-radius: 10px;
        background: linear-gradient(135deg, #25252b, #151519);
        border: 1px solid rgba(255,255,255,0.08);
        text-decoration: none;
        transition: transform 0.3s ease, border 0.3s ease;
    }}

    .coding-card:hover {{
        transform: scale(1.05);
        border-color: rgba(255,255,255,0.3);
    }}

    .coding-platform {{
        font-size: 20px;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
    }}

    .coding-description {{
        font-size: 13px;
        color: #999999;
    }}

    .coding-open {{
        font-size: 12px;
        color: #e50914;
        margin-top: 15px;
    }}
    </style>

    <div class="coding-section">
        <div class="coding-title">Coding Profiles</div>
        <div class="coding-row">
            {cards_html}
        </div>
    </div>
    """)
