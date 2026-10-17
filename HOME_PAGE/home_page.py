import streamlit as st
from .sections.skills_section import skills_section
from .sections.projects import projects_section
from .sections.experiance_section import experience_section
from .sections.education_section import education_section
from .sections.achivements_section import achievements_section
from .sections.certifications import certifications_section
from .sections.coding_profiles import coding_profiles_section
from .sections.resume_section import resume_section
from .sections.contact_section import contact_section
from .sections.footer_section import footer_section

def home_page():

    # NAVBAR + HERO CSS

    st.html("""
    <style>

    /* GLOBAL HOME PAGE */

    /* fades in after the profile card is clicked */
    .block-container {
        animation: home-enter 0.9s var(--ease, ease) backwards;
    }

    @keyframes home-enter {
        from { opacity: 0; filter: blur(8px); }
    }

    .home-container {
        width: 100%;
        margin: 0;
        padding: 0;
    }


    /* NAVBAR */

    .navbar {
        width: 100%;

        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 20px 45px;

        box-sizing: border-box;

        position: relative;
        z-index: 10;
    }


    .logo {
        font-size: 28px;

        font-weight: 800;

        letter-spacing: 1px;

        color: white;
    }


    .nav-links {
        display: flex;

        gap: 30px;

        align-items: center;
    }


    .nav-link {
        color: #b8b8b8;

        font-size: 15px;

        font-weight: 500;

        cursor: pointer;

        transition: color 0.2s ease;
    }


    .nav-link:hover {
        color: white;
    }


    .nav-profile {
        width: 38px;
        height: 38px;

        border-radius: 6px;

        background:
            linear-gradient(
                135deg,
                #333333,
                #18181c
            );

        display: flex;

        align-items: center;
        justify-content: center;

        font-size: 20px;

        border: 1px solid #444;
    }


    /* HERO SECTION */

    .hero {
        min-height: 70vh;

        display: flex;

        align-items: center;

        padding: 60px 8% 100px 8%;

        box-sizing: border-box;

        position: relative;

        overflow: hidden;
    }


    .hero-content {
        max-width: 750px;

        z-index: 2;
    }


    .hero-small-title {
        font-size: 18px;

        color: #b8b8b8;

        font-weight: 500;

        margin-bottom: 12px;
    }


    .hero-title {
        font-size: 68px;

        line-height: 1.05;

        font-weight: 800;

        color: white;

        margin: 0 0 20px 0;
    }


    .hero-title span {
        color: #e50914;
    }


    .hero-description {
        font-size: 18px;

        line-height: 1.7;

        color: #c5c5c5;

        max-width: 650px;

        margin-bottom: 30px;
    }


    .hero-tags {
        display: flex;

        flex-wrap: wrap;

        gap: 10px;

        margin-bottom: 35px;
    }


    .hero-tag {
        padding: 7px 14px;

        border-radius: 20px;

        background: rgba(255,255,255,0.08);

        border: 1px solid rgba(255,255,255,0.12);

        color: #d5d5d5;

        font-size: 13px;
    }


    /* HERO BACKGROUND */

    .hero::after {
        content: "";

        position: absolute;

        right: -150px;
        top: 50px;

        width: 650px;
        height: 650px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(229,9,20,0.15) 0%,
                rgba(229,9,20,0.05) 40%,
                transparent 70%
            );

        pointer-events: none;
    }


    /* SECTION TITLE */

    .section-title {
        font-size: 28px;

        font-weight: 700;

        color: white;

        margin-bottom: 25px;
    }

    </style>
    """)

    # NAVBAR

    st.html("""
    <div class="navbar">

        <div class="logo">
            KARTIK
        </div>


        <div class="nav-links">

            <div class="nav-link">
                Home
            </div>

            <div class="nav-link">
                About
            </div>

            <div class="nav-link">
                Experience
            </div>

            <div class="nav-link">
                Projects
            </div>

            <div class="nav-link">
                Skills
            </div>

            <div class="nav-profile">
                👤
            </div>

        </div>

    </div>
    """)

    # HERO

    st.html("""
    <div class="hero">

        <div class="hero-content">

            <div class="hero-small-title">
                COMPUTER SCIENCE UNDERGRADUATE
            </div>


            <h1 class="hero-title">
                Hi, I'm <span>Kartik</span>.
            </h1>


            <div class="hero-description">

                Software Developer focused on building
                scalable backend systems, REST APIs,
                cross-platform applications, and
                AI-powered solutions.

            </div>


            <div class="hero-tags">

                <div class="hero-tag">
                    FastAPI
                </div>

                <div class="hero-tag">
                    Flutter
                </div>

                <div class="hero-tag">
                    PostgreSQL
                </div>

                <div class="hero-tag">
                    React
                </div>

                <div class="hero-tag">
                    AI / ML
                </div>

            </div>

        </div>

    </div>
    """)
    skills_section()
    projects_section()
    experience_section()
    education_section()
    achievements_section()
    certifications_section()
    coding_profiles_section()
    resume_section()
    contact_section()
    footer_section()

    # TEMPORARY BACK BUTTON

    st.write("")

    if st.button("← Back to Profile"):

        st.session_state.view = "profile"

        st.rerun()