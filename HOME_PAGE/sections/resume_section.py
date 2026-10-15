
from pathlib import Path
import streamlit as st


def resume_section():
    project_root = Path(__file__).resolve().parents[2]
    resume_path = project_root / "assets" / "resume.pdf"

    st.html("""
        <style>
        .resume-eyebrow {
            color: #60a5fa;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .resume-title {
            color: #f8fafc;
            font-size: clamp(30px, 4vw, 42px);
            font-weight: 800;
            margin: 0 0 10px;
        }

        .resume-description {
            color: #aab4c5;
            font-size: 16px;
            line-height: 1.7;
            margin-bottom: 20px;
        }
        </style>

        <div class="resume-eyebrow">My Resume</div>
        <h2 class="resume-title">Download My Resume</h2>
        <p class="resume-description">
            Explore my education, professional experience,
            technical skills, and projects.
        </p>
    """)

    if not resume_path.is_file():
        st.warning("Resume PDF not found in the assets folder.")
        return

    st.download_button(
        label="📄 Download Resume (PDF)",
        data=resume_path.read_bytes(),
        file_name="Kartik_Resume.pdf",
        mime="application/pdf",
        type="primary",
        key="download_resume_pdf",
    )
