import streamlit as st

from HOME_PAGE.components.cards import education_card
from HOME_PAGE.data.portfolio_repository import get_education


def education_section():

    education = get_education()


    cards_html = ""

    for item in education:

        cards_html += education_card(
            institute=item["institute"],
            degree=item["degree"],
            duration=item["duration"],
            details=item["details"]
        )


    st.html(f"""
    <style>

    .education-section {{
        padding: 20px 6% 60px 6%;
    }}


    .education-title {{
        font-size: 28px;
        font-weight: 700;
        color: white;
        margin-bottom: 25px;
    }}


    .education-row {{
        display: flex;
        gap: 22px;
        overflow-x: auto;
        padding: 10px 5px 25px 5px;
    }}


    .education-card {{
        width: 100%;

        padding: 30px;

        box-sizing: border-box;

        border-radius: 10px;

        background:
            linear-gradient(
                135deg,
                #25252b,
                #151519
            );

        border: 1px solid rgba(255,255,255,0.08);

        transition:
            transform 0.3s ease,
            border 0.3s ease;
    }}


    .education-card:hover {{
        transform: translateY(-4px);

        border: 1px solid rgba(255,255,255,0.3);
    }}


    .education-institute {{
        font-size: 24px;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }}


    .education-degree {{
        font-size: 17px;
        color: #e50914;
        margin-bottom: 8px;
    }}


    .education-duration {{
        font-size: 14px;
        color: #888888;
        margin-bottom: 15px;
    }}


    .education-details {{
        font-size: 15px;
        color: #bdbdbd;
        line-height: 1.6;
    }}

    </style>


    <div class="education-section">

        <div class="education-title">
            Education
        </div>

        <div class="education-row">

            {cards_html}

        </div>

    </div>
    """)