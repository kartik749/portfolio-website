import streamlit as st


def skill_card(skill):

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
        {skill}
    </div>
    """

def project_card(
    number,
    name,
    description,
    technologies
):

    return f"""
    <div class="project-card">

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
    """

def experience_card(
    company,
    role,
    duration,
    description
):

    return f"""
    <div class="experience-card">

        <div class="experience-company">
            {company}
        </div>

        <div class="experience-role">
            {role}
        </div>

        <div class="experience-duration">
            {duration}
        </div>

        <div class="experience-description">
            {description}
        </div>

    </div>
    """


def education_card(
    institute,
    degree,
    duration,
    details
):

    return f"""
    <div class="education-card">

        <div class="education-institute">
            {institute}
        </div>

        <div class="education-degree">
            {degree}
        </div>

        <div class="education-duration">
            {duration}
        </div>

        <div class="education-details">
            {details}
        </div>

    </div>
    """


def achievement_card(category, title, description):

    return f"""
    <div class="achievement-card">

        <div class="achievement-label">
            {category}
        </div>

        <div class="achievement-title">
            {title}
        </div>

        <div class="achievement-description">
            {description}
        </div>

    </div>
    """


def certification_card(provider, name):

    return f"""
    <div class="certificate-card">

        <div class="certificate-provider">
            {provider}
        </div>

        <div class="certificate-name">
            {name}
        </div>

    </div>
    """


def coding_profile_card(platform, description, url):

    return f"""
    <a class="coding-card"
       href="{url}"
       target="_blank"
       rel="noopener noreferrer">

        <div class="coding-platform">
            {platform}
        </div>

        <div class="coding-description">
            {description}
        </div>

        <div class="coding-open">
            Visit profile ↗
        </div>

    </a>
    """
