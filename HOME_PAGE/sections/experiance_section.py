import streamlit as st

from HOME_PAGE.components.cards import experience_card
from HOME_PAGE.data.portfolio_repository import get_experiances


def experience_section():
    experiences = get_experiances()

    cards_html = ""

    for experience in experiences:

        cards_html += experience_card(
            company=experience["company"],
            role=experience["role"],
            duration=experience["duration"],
            description=experience["description"]
        )


    st.html(f"""
    <style>

    .experience-section {{
        padding: 20px 6% 50px 6%;
    }}


    .experience-title {{
        font-size: 28px;
        font-weight: 700;
        color: white;
        margin-bottom: 25px;
    }}


    .experience-row {{
        display: flex;
        gap: 22px;
        overflow-x: auto;
        padding: 10px 5px 25px 5px;
    }}


    .experience-card {{
        min-width: 390px;
        min-height: 230px;

        padding: 25px;

        box-sizing: border-box;

        border-radius: 10px;

        background:
            linear-gradient(
                135deg,
                #25252b,
                #151519
            );

        border: 1px solid rgba(255,255,255,0.08);

        flex-shrink: 0;

        transition:
            transform 0.3s ease,
            border 0.3s ease;
    }}


    .experience-card:hover {{
        transform: scale(1.03);

        border: 1px solid rgba(255,255,255,0.3);
    }}


    .experience-company {{
        font-size: 22px;
        font-weight: 700;
        color: white;
    }}


    .experience-role {{
        font-size: 15px;
        color: #e50914;

        margin-top: 6px;
        margin-bottom: 5px;
    }}


    .experience-duration {{
        font-size: 13px;
        color: #888888;

        margin-bottom: 18px;
    }}


    .experience-description {{
        font-size: 14px;
        line-height: 1.6;
        color: #bdbdbd;
    }}

    </style>


    <div class="experience-section">

        <div class="experience-title">
            Experience
        </div>

        <div class="experience-row">

            {cards_html}

        </div>

    </div>
    """)