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
    if not st.session_state.get("admin_authenticated",False):
        st.warning("Please Login to access the admin dashboard.")
        return 
    st.write("")
    st.write("")
    st.title("Portfolio Admin Dashboard")
    st.caption("Manage the content displayed on your public Portfolio.")

    # Side Bar Navigation
    with st.sidebar:
        st.divider()
        st.subheader("Admin Panel")

        section = st.radio(
            "Manage Section",
            [
                "Overview",
                "Skills",
                "Projects",
                "Experiences",
                "Education",
                "Achievements",
                "Certifications",
                "Coding_Profiles"
            ],
            key="admin_navigation"
        )
    if st.button("Logout", use_container_width=True):
        st.session_state['admin_authenticated'] = False
        st.session_state['show_admin_login'] = False
        st.session_state.pop("admin_navigation",None)
        st.rerun()
    if section == "Overview":
        show_overview()
    if section == 'Skills':
        skills_admin()
    if section == 'Projects':
        projects_admin()
    if section == "Experiences":
        experience_admin()
    if section == 'Education':
        education_admin()
    if section == 'Achievements':
        achievements_admin()
    if section == 'Certifications':
        certifications_admin()
    if section == 'Coding_Profiles':
        coding_profiles_admin()
    
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
  