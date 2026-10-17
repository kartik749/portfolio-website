
import base64
import html
import mimetypes
from pathlib import Path

import streamlit as st

from HOME_PAGE.data.portfolio_repository import get_projects


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Supported image formats
ALLOWED_IMAGE_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
}


def resolve_project_image(image_path):
    """
    Resolve a relative image path safely.
    Return the image path only if it exists inside the project directory.
    """
    if not image_path:
        return None

    try:
        relative_path = Path(str(image_path))

        # Only allow relative paths
        if relative_path.is_absolute():
            return None

        project_root = PROJECT_ROOT.resolve()
        image_file = (project_root / relative_path).resolve()

        # Prevent directory traversal outside the project
        if not image_file.is_relative_to(project_root):
            return None

        # Only allow supported image formats
        if image_file.suffix.lower() not in ALLOWED_IMAGE_TYPES:
            return None

        if image_file.is_file():
            return image_file

    except (OSError, ValueError, TypeError):
        return None

    return None


def create_project_card(project):
    """
    Build one project card, including its optional thumbnail.
    """
    number = html.escape(str(project.get("number") or ""))
    name = html.escape(str(project.get("name") or "Untitled Project"))
    description = html.escape(
        str(project.get("description") or "No description available.")
    )
    technologies = html.escape(
        str(project.get("technologies") or "")
    )

    image_html = ""
    image_file = resolve_project_image(project.get("image_path"))

    if image_file:
        mime_type = ALLOWED_IMAGE_TYPES.get(image_file.suffix.lower())

        try:
            image_bytes = image_file.read_bytes()
            encoded_image = base64.b64encode(image_bytes).decode("ascii")

            image_html = f"""
                <img
                    class="project-image"
                    src="data:{mime_type};base64,{encoded_image}"
                    alt="{name}"
                    loading="lazy"
                />
            """
        except OSError:
            image_html = ""

    return f"""
        <div class="project-card">
            {image_html}

            <div class="project-content">
                <div class="project-number">
                    PROJECT {number}
                </div>

                <div class="project-name">
                    {name}
                </div>

                <div class="project-description">
                    {description}
                </div>

                <div class="project-tech">
                    {technologies}
                </div>
            </div>
        </div>
    """


def projects_section():
    """
    Display projects retrieved from PostgreSQL.
    """
    try:
        projects = get_projects()
    except Exception:
        st.error("Unable to load projects. Please try again later.")
        return

    if not projects:
        st.info("No projects available yet.")
        return

    cards_html = "".join(
        create_project_card(project)
        for project in projects
    )

    st.html(f"""
        <style>
        .projects-section {{
            padding: 20px 6% 30px;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }}

        .projects-title {{
            font-size: 28px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 22px;
        }}

        .projects-row {{
            display: flex;
            align-items: stretch;
            gap: 22px;
            overflow-x: auto;
            padding: 10px 5px 25px;
            scrollbar-width: thin;
            scrollbar-color: #555555 #17171b;
        }}

        .project-card {{
            display: flex;
            flex-direction: column;
            min-width: 330px;
            width: 330px;
            height: 370px;
            box-sizing: border-box;
            border-radius: 12px;
            background: linear-gradient(135deg, #25252b, #151519);
            border: 1px solid rgba(255, 255, 255, 0.08);
            overflow: hidden;
            flex-shrink: 0;
            transition:
                transform 0.3s ease,
                border-color 0.3s ease,
                box-shadow 0.3s ease;
        }}

        .project-card:hover {{
            transform: translateY(-5px);
            border-color: rgba(229, 9, 20, 0.6);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
        }}

        .project-image {{
            width: 100%;
            height: 175px;
            min-height: 175px;
            object-fit: cover;
            display: block;
            background: #202027;
        }}

        .project-content {{
            padding: 16px;
            overflow-y: auto;
            flex: 1;
        }}

        .project-number {{
            font-size: 12px;
            font-weight: 600;
            color: var(--accent, #e50914);
            margin-bottom: 6px;
            letter-spacing: 1px;
        }}

        .project-name {{
            font-size: 20px;
            font-weight: 700;
            line-height: 1.35;
            color: #ffffff;
            margin-bottom: 8px;
            overflow-wrap: anywhere;
        }}

        .project-description {{
            font-size: 13px;
            line-height: 1.6;
            color: #bdbdbd;
            overflow-wrap: anywhere;
        }}

        .project-tech {{
            color: #999999;
            font-size: 12px;
            line-height: 1.5;
            margin-top: 10px;
            overflow-wrap: anywhere;
        }}

        .projects-row::-webkit-scrollbar {{
            height: 7px;
        }}

        .projects-row::-webkit-scrollbar-track {{
            background: #17171b;
            border-radius: 10px;
        }}

        .projects-row::-webkit-scrollbar-thumb {{
            background: #555555;
            border-radius: 10px;
        }}

        @media (max-width: 600px) {{
            .projects-section {{
                padding: 16px 4% 24px;
            }}

            .projects-title {{
                font-size: 24px;
            }}

            .project-card {{
                min-width: 285px;
                width: 285px;
            }}
        }}
        </style>

        <div class="projects-section">
            <div class="projects-title">Featured Projects</div>

            <div class="projects-row">
                {cards_html}
            </div>
        </div>
    """)
