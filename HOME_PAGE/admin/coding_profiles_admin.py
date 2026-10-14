
import streamlit as st
from sqlalchemy import text
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    """Allow only HTTP/HTTPS URLs with a valid hostname."""
    try:
        parsed = urlparse(url.strip())
        return (
            parsed.scheme in ("https", "http")
            and bool(parsed.hostname)
            and not any(char.isspace() for char in url.strip())
        )
    except ValueError:
        return False


def coding_profiles_admin():
    if not st.session_state.get("admin_authenticated", False):
        st.error("Please log in as admin to access this page.")
        return

    st.title("Manage Coding Profiles")
    st.caption("Add, edit, and delete your external profile links.")

    conn = st.connection("neon", type="sql")

    def get_profiles():
        with conn.session as session:
            result = session.execute(
                text("""
                    SELECT id, platform, description, url, sort_order
                    FROM coding_profiles
                    ORDER BY sort_order, id
                """)
            )
            return [dict(row) for row in result.mappings().all()]

    profiles = get_profiles()

    # Add a coding profile
    with st.expander("➕ Add Coding Profile"):
        with st.form("add_coding_profile_form"):
            platform = st.text_input(
                "Platform",
                placeholder="e.g., GitHub or LeetCode"
            )
            description = st.text_input(
                "Description",
                placeholder="e.g., Projects and problem-solving profile"
            )
            url = st.text_input(
                "Profile URL",
                placeholder="https://..."
            )
            sort_order = st.number_input(
                "Display Order",
                min_value=1,
                value=len(profiles) + 1,
                step=1
            )

            submitted = st.form_submit_button(
                "Add Profile",
                type="primary"
            )

            if submitted:
                if not platform.strip() or not description.strip() or not url.strip():
                    st.error("Please complete all fields.")
                elif not is_valid_url(url):
                    st.error("Enter a valid HTTP or HTTPS URL.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    INSERT INTO coding_profiles
                                    (platform, description, url, sort_order)
                                    VALUES
                                    (:platform, :description, :url, :sort_order)
                                """),
                                {
                                    "platform": platform.strip(),
                                    "description": description.strip(),
                                    "url": url.strip(),
                                    "sort_order": sort_order,
                                }
                            )
                            session.commit()

                        st.success("Coding profile added successfully.")
                        st.rerun()

                    except Exception:
                        st.error("Could not add coding profile.")

    st.divider()
    st.subheader("Existing Coding Profiles")

    profiles = get_profiles()

    if not profiles:
        st.info("No coding profiles found. Add one above.")
        return

    st.dataframe(profiles, use_container_width=True, hide_index=True)

    profile_options = {
        f'{item["platform"]} (ID: {item["id"]})': item["id"]
        for item in profiles
    }

    selected_label = st.selectbox(
        "Select a profile to manage",
        options=list(profile_options.keys())
    )

    selected_id = profile_options[selected_label]
    selected = next(
        item for item in profiles if item["id"] == selected_id
    )

    action = st.radio(
        "Action",
        ["Edit", "Delete"],
        horizontal=True,
        key="coding_profile_action"
    )

    if action == "Edit":
        with st.form("edit_coding_profile_form"):
            updated_platform = st.text_input(
                "Platform",
                value=selected["platform"]
            )
            updated_description = st.text_input(
                "Description",
                value=selected["description"]
            )
            updated_url = st.text_input(
                "Profile URL",
                value=selected["url"]
            )
            updated_order = st.number_input(
                "Display Order",
                min_value=1,
                value=int(selected["sort_order"]),
                step=1
            )

            save = st.form_submit_button(
                "Save Changes",
                type="primary"
            )

            if save:
                if (
                    not updated_platform.strip()
                    or not updated_description.strip()
                    or not updated_url.strip()
                ):
                    st.error("Please complete all fields.")
                elif not is_valid_url(updated_url):
                    st.error("Enter a valid HTTP or HTTPS URL.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    UPDATE coding_profiles
                                    SET platform = :platform,
                                        description = :description,
                                        url = :url,
                                        sort_order = :sort_order
                                    WHERE id = :id
                                """),
                                {
                                    "platform": updated_platform.strip(),
                                    "description": updated_description.strip(),
                                    "url": updated_url.strip(),
                                    "sort_order": updated_order,
                                    "id": selected_id,
                                }
                            )
                            session.commit()

                        st.success("Coding profile updated successfully.")
                        st.rerun()

                    except Exception:
                        st.error("Could not update coding profile.")

    else:
        st.warning(
            f'You are about to delete "{selected["platform"]}".'
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this profile.",
            key="confirm_delete_coding_profile"
        )

        if st.button(
            "Delete Profile",
            type="primary",
            disabled=not confirm
        ):
            try:
                with conn.session as session:
                    session.execute(
                        text("""
                            DELETE FROM coding_profiles
                            WHERE id = :id
                        """),
                        {"id": selected_id}
                    )
                    session.commit()

                st.success("Coding profile deleted successfully.")
                st.rerun()

            except Exception:
                st.error("Could not delete coding profile.")
