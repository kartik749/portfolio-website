import streamlit as st
import html
from pathlib import Path


def skill_card(skill):
    safe_name = html.escape(str(skill or ""))

    return f"""
    <style>

    .skill-card {{
        min-width: 160px;
        height: 90px;

        border-radius: 8px;

        background:
            linear-gradient(
                135deg,
                #24242a,
                #151519
            );

        border: 1px solid rgba(255,255,255,0.08);

        display: flex;
        align-items: center;
        justify-content: center;

        color: #eeeeee;

        font-size: 17px;
        font-weight: 600;

        transition:
            transform 0.25s ease,
            border 0.25s ease,
            background 0.25s ease;
    }}

    .skill-card:hover {{
        transform: scale(1.08);

        border: 1px solid rgba(255,255,255,0.35);

        background: #2d2d34;
    }}

    </style>

    <div class="skill-card">
        {safe_name}
    </div>
    """


def project_card(
    number,
    name,
    description,
    technologies,
    image_path=None
):
    safe_name = html.escape(str(name or ""))
    safe_number = html.escape(str(number or ""))
    safe_description = html.escape(str(description or ""))
    safe_technologies = html.escape(str(technologies or ""))

    # Convert the local image into an embedded image URL.
    image_html = ""

    if image_path:
        try:
            image_file = Path(image_path).resolve()

            # Allow common image formats only.
            mime_types = {
                ".png": "image/png",
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".webp": "image/webp",
            }

            mime_type = mime_types.get(image_file.suffix.lower())

            if mime_type and image_file.is_file():
                image_bytes = image_file.read_bytes()
                encoded_image = base64.b64encode(
                    image_bytes
                ).decode("ascii")

                image_html = f"""
                    <img
                        class="project-image"
                        src="data:{mime_type};base64,{encoded_image}"
                        alt="{safe_name}"
                    />
                """
        except (OSError, ValueError):
            image_html = ""

    return f"""
    <div class="project-card">

        {image_html}

        <div class="project-content">
            <div class="project-number">
                PROJECT {safe_number}
            </div>

            <div class="project-name">
                {safe_name}
            </div>

            <div class="project-description">
                {safe_description}
            </div>

            <div class="project-tech">
                {safe_technologies}
            </div>
        </div>

    </div>
    """

def experience_card(
    company,
    role,
    duration,
    description
):
    safe_company = html.escape(company or "")
    safe_role = html.escape(role or "")
    safe_duration = html.escape(duration or "")
    safe_description = html.escape(description or "")
    return f"""
    <div class="experience-card">

        <div class="experience-company">
            {safe_company}
        </div>

        <div class="experience-role">
            {safe_role}
        </div>

        <div class="experience-duration">
            {safe_duration}
        </div>

        <div class="experience-description">
            {safe_description}
        </div>

    </div>
    """


def education_card(
    institute,
    degree,
    duration,
    details
):
    safe_institute = html.escape(institute or "")
    safe_degree = html.escape(degree or "")
    safe_duration = html.escape(duration or "")
    safe_details = html.escape(details or "")

    return f"""
    <div class="education-card">

        <div class="education-institute">
            {safe_institute}
        </div>

        <div class="education-degree">
            {safe_degree}
        </div>

        <div class="education-duration">
            {safe_duration}
        </div>

        <div class="education-details">
            {safe_details}
        </div>

    </div>
    """


def achievement_card(category, title, description):
    safe_category = html.escape(category or "")
    safe_title = html.escape(title or "")
    safe_description = html.escape(description or "")

    return f"""
    <div class="achievement-card">

        <div class="achievement-label">
            {safe_category}
        </div>

        <div class="achievement-title">
            {safe_title}
        </div>

        <div class="achievement-description">
            {safe_description}
        </div>

    </div>
    """


def certification_card(provider, name):

    safe_provider = html.escape(provider or "")
    safe_name = html.escape(name or "")
    return f"""
    <div class="certificate-card">

        <div class="certificate-provider">
            {safe_provider}
        </div>

        <div class="certificate-name">
            {safe_name}
        </div>

    </div>
    """


def coding_profile_card(platform, description, url):

    safe_platform = html.escape(platform or "")
    safe_description = html.escape(description or "")
    safe_url = html.escape(url or "")
    return f"""
    <a class="coding-card"
       href="{safe_url}"
       target="_blank"
       rel="noopener noreferrer">

        <div class="coding-platform">
            {safe_platform}
        </div>

        <div class="coding-description">
            {safe_description}
        </div>

        <div class="coding-open">
            Visit profile ↗
        </div>

    </a>
    """
