import streamlit as st

def resume_section():

    st.html("""
    <style>

    .resume-section {
        padding: 30px 6% 60px 6%;

        text-align: center;
    }

    .resume-title {
        font-size: 28px;
        font-weight: 700;

        color: white;

        margin-bottom: 12px;
    }

    .resume-description {
        font-size: 15px;

        color: #a8a8a8;

        margin-bottom: 25px;
    }

    .resume-box {
        max-width: 700px;

        margin: auto;

        padding: 35px;

        border-radius: 12px;

        background:
            linear-gradient(
                135deg,
                #25252b,
                #151519
            );

        border: 1px solid rgba(255,255,255,0.08);
    }

    .resume-text {
        font-size: 17px;

        color: #dddddd;

        margin-bottom: 20px;
    }

    </style>


    <div class="resume-section">

        <div class="resume-title">
            Resume
        </div>

        <div class="resume-description">
            Interested in working together?
            Take a look at my resume.
        </div>

        <div class="resume-box">

            <div class="resume-text">
                View my experience, projects,
                technical skills and education.
            </div>

        </div>

    </div>
    """)