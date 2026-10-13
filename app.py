import streamlit as st
from pathlib import Path
import base64

from profile_selection_page import profile_selection
from HOME_PAGE.home_page import home_page

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

    profile_selection()