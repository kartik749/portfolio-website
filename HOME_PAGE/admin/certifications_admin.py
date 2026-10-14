
import streamlit as st
from sqlalchemy import text

def certifications_admin():
    # Protect this page
    if not st.session_state.get("admin_authenticated", False):
        st.error("Please log in as admin to access this page.")
        return

    st.title("Manage Certifications")
    st.caption("Add, edit, or delete certifications in your portfolio.")

    conn = st.connection("neon", type="sql")

    def get_certifications():
        with conn.session as session:
            result = session.execute(
                text("""
                    SELECT id, provider, name, sort_order
                    FROM certifications
                    ORDER BY sort_order, id
                """)
            )
            return [dict(row) for row in result.mappings().all()]

    certifications = get_certifications()

    # Add certification
    with st.expander("➕ Add Certification", expanded=False):
        with st.form("add_certification_form"):
            provider = st.text_input(
                "Provider / Organization",
                placeholder="e.g., IBM SkillsBuild"
            )
            name = st.text_input(
                "Certification Name",
                placeholder="e.g., AI Strategy & Business Intelligence"
            )
            sort_order = st.number_input(
                "Display Order",
                min_value=1,
                value=len(certifications) + 1,
                step=1
            )

            submitted = st.form_submit_button(
                "Add Certification",
                type="primary"
            )

            if submitted:
                if not provider.strip() or not name.strip():
                    st.error("Please fill in both fields.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    INSERT INTO certifications
                                    (provider, name, sort_order)
                                    VALUES (:provider, :name, :sort_order)
                                """),
                                {
                                    "provider": provider.strip(),
                                    "name": name.strip(),
                                    "sort_order": sort_order
                                }
                            )
                            session.commit()

                        st.success("Certification added successfully.")
                        st.rerun()

                    except Exception:
                        st.error(
                            "Could not add certification. Please check "
                            "your database connection and try again."
                        )

    st.divider()

    # Edit or delete certification
    st.subheader("Existing Certifications")

    certifications = get_certifications()

    if not certifications:
        st.info("No certifications found. Add one above.")
        return

    st.dataframe(
        certifications,
        use_container_width=True,
        hide_index=True
    )

    certification_options = {
        f'{item["name"]} — {item["provider"]} (ID: {item["id"]})':
            item["id"]
        for item in certifications
    }

    selected_label = st.selectbox(
        "Select a certification to manage",
        options=list(certification_options.keys())
    )

    selected_id = certification_options[selected_label]
    selected = next(
        item for item in certifications
        if item["id"] == selected_id
    )

    action = st.radio(
        "Action",
        ["Edit", "Delete"],
        horizontal=True,
        key="certification_action"
    )

    if action == "Edit":
        with st.form("edit_certification_form"):
            updated_provider = st.text_input(
                "Provider / Organization",
                value=selected["provider"]
            )
            updated_name = st.text_input(
                "Certification Name",
                value=selected["name"]
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
                if not updated_provider.strip() or not updated_name.strip():
                    st.error("Both fields are required.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    UPDATE certifications
                                    SET provider = :provider,
                                        name = :name,
                                        sort_order = :sort_order
                                    WHERE id = :id
                                """),
                                {
                                    "provider": updated_provider.strip(),
                                    "name": updated_name.strip(),
                                    "sort_order": updated_order,
                                    "id": selected_id
                                }
                            )
                            session.commit()

                        st.success("Certification updated successfully.")
                        st.rerun()

                    except Exception:
                        st.error("Could not update certification.")

    else:
        st.warning(
            f'You are about to delete "{selected["name"]}".'
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this certification.",
            key="confirm_delete_certification"
        )

        if st.button(
            "Delete Certification",
            type="primary",
            disabled=not confirm
        ):
            try:
                with conn.session as session:
                    session.execute(
                        text("""
                            DELETE FROM certifications
                            WHERE id = :id
                        """),
                        {"id": selected_id}
                    )
                    session.commit()

                st.success("Certification deleted successfully.")
                st.rerun()

            except Exception:
                st.error("Could not delete certification.")
