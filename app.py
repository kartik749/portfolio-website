import streamlit as st
from pathlib import Path
import base64

from profile_selection_page import profile_selection
from HOME_PAGE.home_page import home_page
from admin_login_page import admin_login_page

# connecting postgres
conn = st.connection("neon", type="sql")


# Page Configuration
st.set_page_config(
    page_title="Kartik | Portfolio",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# SESSION STATE

if "entered" not in st.session_state:
    st.session_state.entered = False

# GLOBAL CSS

st.html("""
<style>

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(
            circle at center,
            #1a1a22 0%,
            #0b0b0f 65%
        );
}

.block-container {
    padding-top: 0rem;
}

</style>
""")
# MAIN APPLICATION

if st.session_state.entered:

    home_page()

else:
    if "show_admin_login" not in st.session_state:
        st.session_state["show_admin_login"] = False

    with st.sidebar:
        if st.button("Admin Login"):
            st.session_state["show_admin_login"] = True
            st.rerun()

        if st.session_state.get("show_admin_login", False):
            if st.button("Back to Portfolio"):
                st.session_state["show_admin_login"] = False
                st.rerun()

    if st.session_state["show_admin_login"]:
        if admin_login_page():
            st.info("Authentication successful. Admin dashboard is our next step.")
    else:
        profile_selection()
        pass