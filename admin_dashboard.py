import streamlit as st
from sqlalchemy import text
from HOME_PAGE.admin.projects_admin import projects_admin
from HOME_PAGE.admin.skills_admin import skills_admin
from HOME_PAGE.admin.experience_admin import experience_admin
from HOME_PAGE.admin.education_admin import education_admin
from HOME_PAGE.admin.achievements_admin import achievements_admin
from HOME_PAGE.admin.certifications_admin import certifications_admin
from HOME_PAGE.admin.coding_profiles_admin import coding_profiles_admin

def admin_dashboard():
    # Protect the dashboard from unauthenticated access
    if not st.session_state.get("admin_authenticated", False):
        st.warning("Please Login to access the admin dashboard.")
        return

    sections = {
        "Overview": show_overview,
        "Skills": skills_admin,
        "Projects": projects_admin,
        "Experiences": experience_admin,
        "Education": education_admin,
        "Achievements": achievements_admin,
        "Certifications": certifications_admin,
        "Coding Profiles": coding_profiles_admin,
    }

    # Header: title on the left, Logout on the right
    title_col, logout_col = st.columns([6, 1], vertical_alignment="center")

    with title_col:
        st.title("Portfolio Admin Dashboard")
        st.caption("Manage the content displayed on your public Portfolio.")

    with logout_col:
        if st.button("Logout", width="stretch"):
            st.session_state["admin_authenticated"] = False
            st.session_state["view"] = "profile"
            st.session_state.pop("admin_navigation", None)
            st.rerun()

    # Section navigation: a horizontal bar instead of the old sidebar
    selected = st.pills(
        "Manage section",
        list(sections),
        default="Overview",
        key="admin_navigation",
        label_visibility="collapsed",
    )

    # Clicking the active pill again deselects it; fall back to Overview.
    sections[selected or "Overview"]()

    
def show_overview():
    st.subheader("Portfolio Overview")

    tables = {
        "Projects": "projects",
        "Skills": "skills",
        "Experience": "experiences",
        "Education": "education",
        "Achievements": "achievements",
        "Certifications": "certifications",
        "Coding Profiles": "coding_profiles",
    }

    try:
        conn = st.connection("neon", type="sql")
        counts = {}

        with conn.session as session:
            for label, table in tables.items():
                counts[label] = session.execute(
                    text(f"SELECT COUNT(*) FROM {table}")
                ).scalar_one()

        columns = st.columns(4)

        for index, (label, count) in enumerate(counts.items()):
            with columns[index % 4]:
                st.metric(label, count)

    except Exception:
        st.error("Could not load the portfolio statistics.")
        st.caption(
            "Check the Neon connection and database tables."
        )
  