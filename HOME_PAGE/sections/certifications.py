
import streamlit as st

from HOME_PAGE.components.cards import certification_card
from HOME_PAGE.data.portfolio_repository import get_certifications


def certifications_section():

    certifications = get_certifications()

    cards_html = ""

    for item in certifications:
        cards_html += certification_card(
            provider=item["provider"],
            name=item["name"]
        )

    st.html(f"""
    <style>
    .certifications-section {{
        padding: 20px 6% 50px;
    }}

    .certifications-title {{
        font-size: 28px;
        font-weight: 700;
        color: white;
        margin-bottom: 25px;
    }}

    .certifications-row {{
        display: flex;
        gap: 22px;
        overflow-x: auto;
        padding: 10px 5px 25px;
    }}

    .certificate-card {{
        flex: 0 0 330px;
        min-height: 180px;
        padding: 25px;
        box-sizing: border-box;
        border-radius: 10px;
        background: linear-gradient(135deg, #25252b, #151519);
        border: 1px solid rgba(255,255,255,0.08);
        transition: transform 0.3s ease, border 0.3s ease;
    }}

    .certificate-card:hover {{
        transform: scale(1.04);
        border-color: rgba(255,255,255,0.3);
    }}

    .certificate-provider {{
        font-size: 13px;
        color: #e50914;
        margin-bottom: 12px;
    }}

    .certificate-name {{
        font-size: 19px;
        font-weight: 700;
        color: white;
        line-height: 1.4;
    }}
    </style>

    <div class="certifications-section">
        <div class="certifications-title">Certifications</div>
        <div class="certifications-row">
            {cards_html}
        </div>
    </div>
    """)
