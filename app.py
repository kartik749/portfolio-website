import streamlit as st

from theme import inject_global_css, top_right_button
from profile_selection_page import profile_selection
from HOME_PAGE.home_page import home_page
from admin_login_page import admin_login_page
from admin_dashboard import admin_dashboard

# connecting postgres
conn = st.connection("neon", type="sql")


# Page Configuration
st.set_page_config(
    page_title="Kartik | Portfolio",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# SESSION STATE
# One value decides which screen is shown: "profile", "home" or "admin".
st.session_state.setdefault("view", "profile")

# GLOBAL CSS (design tokens, hidden sidebar, top-right button)
inject_global_css()


def admin_view():
    """Admin login, then the dashboard once signed in."""
    # Leave room for the fixed top-right button.
    st.html("<style>.block-container { padding-top: 4.5rem; }</style>")
    top_right_button("← Back to portfolio", "profile", key="admin_back")

    if admin_login_page():
        admin_dashboard()


# MAIN APPLICATION
view = st.session_state.view

if view == "home":
    home_page()
elif view == "admin":
    admin_view()
else:
    profile_selection()
