
import hmac
import streamlit as st


def admin_login_page():
    st.write("")
    st.write("")
    
    st.title("Admin Login")
    st.write("Sign in to manage your Portfolio")

    if st.session_state.get("admin_authenticated", False):
        return True

    with st.form("admin_login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button(
            "Login",
            use_container_width=True,
        )

    if submitted:
        expected_username = st.secrets["admin"]["username"]
        expected_password = st.secrets["admin"]["password"]

        username_valid = hmac.compare_digest(
            username, expected_username
        )
        password_valid = hmac.compare_digest(
            password, expected_password
        )

        if username_valid and password_valid:
            st.session_state["admin_authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid username or password.")

    return st.session_state.get("admin_authenticated", False)
