import streamlit as st

def contact_section():

    st.html("""
    <style>

    .contact-section {
        padding: 30px 6% 60px 6%;

        text-align: center;
    }

    .contact-title {
        font-size: 28px;

        font-weight: 700;

        color: white;

        margin-bottom: 12px;
    }

    .contact-description {
        max-width: 650px;

        margin: 0 auto 30px auto;

        font-size: 15px;

        line-height: 1.6;

        color: #a8a8a8;
    }

    .contact-info {
        display: flex;

        justify-content: center;

        flex-wrap: wrap;

        gap: 15px;
    }

    .contact-item {
        padding: 12px 20px;

        border-radius: 8px;

        background: rgba(255,255,255,0.06);

        border: 1px solid rgba(255,255,255,0.08);

        color: #dddddd;

        font-size: 14px;
    }

    .contact-item:hover {
        border: 1px solid rgba(255,255,255,0.25);
    }

    </style>


    <div class="contact-section">

        <div class="contact-title">
            Let's Connect
        </div>

        <div class="contact-description">

            I'm always open to discussing software
            development opportunities, interesting
            projects and new ideas.

        </div>


        <div class="contact-info">

            <div class="contact-item">
                Email
            </div>

            <div class="contact-item">
                LinkedIn
            </div>

            <div class="contact-item">
                GitHub
            </div>

        </div>

    </div>
    """)