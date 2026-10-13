import streamlit as st

from HOME_PAGE.components.cards import project_card
from HOME_PAGE.data.portfolio_repository import get_projects


def projects_section():

    projects  = get_projects()


    cards_html = ""

    for project in projects:

        cards_html += project_card(
            number=project["number"],
            name=project["name"],
            description=project["description"],
            technologies=project["technologies"]
        )


    st.html(f"""
    <style>

    .projects-section {{
        padding: 20px 6% 50px 6%;
    }}


    .projects-title {{
        font-size: 28px;
        font-weight: 700;

        color: white;

        margin-bottom: 22px;
    }}


    .projects-row {{
        display: flex;

        gap: 22px;

        overflow-x: auto;

        padding: 10px 5px 25px 5px;

        scrollbar-width: thin;
    }}


    .project-card {{
        min-width: 330px;

        height: 210px;

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

        position: relative;

        overflow: hidden;

        flex-shrink: 0;

        transition:
            transform 0.3s ease,
            border 0.3s ease;
    }}


    .project-card:hover {{
        transform: scale(1.04);

        border: 1px solid rgba(255,255,255,0.3);
    }}


    .project-number {{
        font-size: 14px;

        color: #888888;

        margin-bottom: 10px;
    }}


    .project-name {{
        font-size: 24px;

        font-weight: 700;

        color: white;

        margin-bottom: 12px;
    }}


    .project-description {{
        font-size: 14px;

        line-height: 1.5;

        color: #bdbdbd;

        max-width: 280px;
    }}


    .project-tech {{
        position: absolute;

        bottom: 20px;

        left: 25px;

        color: #999999;

        font-size: 12px;
    }}

    </style>


    <div class="projects-section">

        <div class="projects-title">
            Featured Projects
        </div>

        <div class="projects-row">

            {cards_html}

        </div>

    </div>
    """)