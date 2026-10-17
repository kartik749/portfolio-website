
import html

import streamlit as st


def contact_section():
    # Contact details
    email = "kartiksangwan7511@gmail.com"

    # Replace these placeholders with your actual profile URLs.
    linkedin_url = "https://www.linkedin.com/in/kartik-sangwan"
    github_url = "https://github.com/kartik749"

    safe_email = html.escape(email, quote=True)
    safe_linkedin_url = html.escape(linkedin_url, quote=True)
    safe_github_url = html.escape(github_url, quote=True)

    st.html(f"""
    <style>
    .contact-section {{
        padding: 30px 6% 60px;
        text-align: center;
        color: #ffffff;
    }}

    .contact-title {{
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 12px;
    }}

    .contact-description {{
        max-width: 650px;
        margin: 0 auto 30px;
        font-size: 15px;
        line-height: 1.6;
        color: #a8a8a8;
    }}

    .contact-info {{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 15px;
    }}

    .contact-item {{
        display: inline-block;
        padding: 12px 20px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #dddddd;
        font-size: 14px;
        text-decoration: none;
        transition:
            border-color 0.25s ease,
            background 0.25s ease,
            transform 0.25s ease;
    }}

    .contact-item:hover {{
        border-color: var(--accent, #e50914);
        background: rgba(229, 9, 20, 0.10);
        transform: translateY(-3px);
        color: #ffffff;
    }}

    @media (max-width: 600px) {{
        .contact-section {{
            padding: 25px 4% 40px;
        }}

        .contact-title {{
            font-size: 24px;
        }}

        .contact-info {{
            gap: 10px;
        }}
    }}
    </style>

    <div class="contact-section">
        <div class="contact-title">Let's Connect</div>

        <div class="contact-description">
            I'm always open to discussing software development
            opportunities, interesting projects and new ideas.
            Feel free to reach out!
        </div>

        <div class="contact-info">
            <a class="contact-item"
               href="mailto:{safe_email}">
                ✉ Email Me
            </a>

            <a class="contact-item"
               href="{safe_linkedin_url}"
               target="_blank"
               rel="noopener noreferrer">
                LinkedIn ↗
            </a>

            <a class="contact-item"
               href="{safe_github_url}"
               target="_blank"
               rel="noopener noreferrer">
                GitHub ↗
            </a>
        </div>
    </div>
    """)

