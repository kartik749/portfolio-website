
import streamlit as st
from sqlalchemy import text


conn = st.connection("neon", type="sql")


def _get_rows(query: str) -> list[dict]:
    """Fetch rows from PostgreSQL as dictionaries."""
    with conn.session as session:
        result = session.execute(text(query))
        return [dict(row) for row in result.mappings().all()]


def get_skills() -> list[str]:
    rows = _get_rows(
        "SELECT name FROM skills ORDER BY sort_order, id"
    )
    return [row["name"] for row in rows]


def get_projects():
    return _get_rows("""
        SELECT id, sort_order, number, name,
               description, technologies, image_path
        FROM projects
        ORDER BY sort_order, id
    """)


def get_experiences() -> list[dict]:
    return _get_rows(
        "SELECT company, role, duration, description "
        "FROM experiences ORDER BY sort_order, id"
    )


def get_education() -> list[dict]:
    return _get_rows(
        "SELECT institute, degree, duration, details "
        "FROM education ORDER BY sort_order, id"
    )


def get_achievements() -> list[dict]:
    return _get_rows(
        "SELECT category, title, description "
        "FROM achievements ORDER BY sort_order, id"
    )


def get_certifications() -> list[dict]:
    return _get_rows(
        "SELECT provider, name "
        "FROM certifications ORDER BY sort_order, id"
    )


def get_coding_profiles() -> list[dict]:
    return _get_rows(
        "SELECT platform, description, url "
        "FROM coding_profiles ORDER BY sort_order, id"
    )
