import streamlit as st
import html
from pathlib import Path

from .skill_icons import skill_icon_url, skill_icon_needs_invert


def skill_card(skill):
    """One tile of the skills grid. Styling lives in skills_section.py."""
    name = str(skill or "")
    safe_name = html.escape(name)
    icon_url = skill_icon_url(name)

    if icon_url:
        invert = " skill-icon-invert" if skill_icon_needs_invert(name) else ""
        icon_html = (
            f'<img class="skill-icon{invert}" src="{icon_url}" alt="" '
            'width="44" height="44" loading="lazy" decoding="async">'
        )
    else:
        letter = html.escape(name.strip()[:1].upper() or "?")
        icon_html = f'<div class="skill-mono">{letter}</div>'

    return f"""
    <div class="skill-tile">
        {icon_html}
        <div class="skill-name">{safe_name}</div>
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
    description,
    is_open=False,
):
    """One timeline entry. Collapsed it shows duration + company; clicking
    it slides open the role and description. Styling lives in
    experiance_section.py."""
    safe_company = html.escape(company or "")
    safe_role = html.escape(role or "")
    safe_duration = html.escape(duration or "")

    # A multi-line description in the admin panel renders as bullet points.
    lines = [
        html.escape(line.strip())
        for line in (description or "").splitlines()
        if line.strip()
    ]

    if len(lines) > 1:
        points = "".join(f"<li>{line}</li>" for line in lines)
        description_html = f'<ul class="exp-desc">{points}</ul>'
    else:
        text = lines[0] if lines else ""
        description_html = f'<p class="exp-desc">{text}</p>'

    open_attr = " open" if is_open else ""

    return f"""
    <details class="exp-item" name="experience"{open_attr}>

        <summary class="exp-head">
            <span class="exp-dot"></span>
            <span class="exp-when">{safe_duration}</span>
            <span class="exp-company">{safe_company}</span>
            <span class="exp-chevron"></span>
        </summary>

        <div class="exp-body">
            <div class="exp-role">{safe_role}</div>
            {description_html}
        </div>

    </details>
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
