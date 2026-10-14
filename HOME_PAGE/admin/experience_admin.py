
import streamlit as st
from sqlalchemy import text


def experience_admin():
    if not st.session_state.get("admin_authenticated", False):
        st.error("Please log in to manage experience.")
        return

    conn = st.connection("neon", type="sql")

    st.subheader("Manage Experience")
    st.caption("Manage internships, jobs, and other professional experience.")

    # Fetch experience records.
    try:
        with conn.session as session:
            experiences = [
                dict(row)
                for row in session.execute(
                    text("""
                        SELECT id, sort_order, company, role,
                               duration, description
                        FROM experiences
                        ORDER BY sort_order, id
                    """)
                ).mappings().all()
            ]
    except Exception:
        st.error("Could not load experience records from PostgreSQL.")
        return

    # Display existing records.
    st.markdown("### Existing Experience")

    if experiences:
        st.dataframe(
            [
                {
                    "ID": item["id"],
                    "Company": item["company"],
                    "Role": item["role"],
                    "Duration": item["duration"],
                }
                for item in experiences
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No experience records found. Add one below.")

    add_tab, edit_tab, delete_tab = st.tabs(
        ["Add Experience", "Edit Experience", "Delete Experience"]
    )

    # ---------------- ADD ----------------
    with add_tab:
        st.markdown("### Add Experience")

        with st.form("add_experience_form", clear_on_submit=True):
            company = st.text_input("Company / Organization")
            role = st.text_input("Job Title / Role")
            duration = st.text_input(
                "Duration",
                placeholder="June 2026 – September 2026",
            )
            description = st.text_area("Responsibilities and achievements")

            submitted = st.form_submit_button(
                "Add Experience",
                use_container_width=True,
            )

        if submitted:
            if not company.strip():
                st.error("Company / organization is required.")
            elif not role.strip():
                st.error("Job title / role is required.")
            else:
                try:
                    with conn.session as session:
                        next_order = session.execute(
                            text("""
                                SELECT COALESCE(MAX(sort_order), 0) + 1
                                FROM experiences
                            """)
                        ).scalar_one()

                        session.execute(
                            text("""
                                INSERT INTO experiences
                                    (sort_order, company, role,
                                     duration, description)
                                VALUES
                                    (:sort_order, :company, :role,
                                     :duration, :description)
                            """),
                            {
                                "sort_order": next_order,
                                "company": company.strip(),
                                "role": role.strip(),
                                "duration": duration.strip(),
                                "description": description.strip(),
                            },
                        )
                        session.commit()

                    st.success("Experience added successfully.")
                    st.rerun()

                except Exception:
                    st.error("Could not add the experience record.")

    # ---------------- EDIT ----------------
    with edit_tab:
        st.markdown("### Edit Experience")

        if not experiences:
            st.info("Add an experience record before editing.")
        else:
            selected_id = st.selectbox(
                "Choose an experience record",
                [item["id"] for item in experiences],
                format_func=lambda item_id: next(
                    f"{item['company']} — {item['role']}"
                    for item in experiences
                    if item["id"] == item_id
                ),
                key="edit_experience_id",
            )

            selected = next(
                item for item in experiences
                if item["id"] == selected_id
            )

            with st.form("edit_experience_form"):
                edit_company = st.text_input(
                    "Company / Organization",
                    value=selected["company"] or "",
                )
                edit_role = st.text_input(
                    "Job Title / Role",
                    value=selected["role"] or "",
                )
                edit_duration = st.text_input(
                    "Duration",
                    value=selected["duration"] or "",
                )
                edit_description = st.text_area(
                    "Responsibilities and achievements",
                    value=selected["description"] or "",
                )
                edit_submitted = st.form_submit_button(
                    "Save Changes",
                    use_container_width=True,
                )

            if edit_submitted:
                if not edit_company.strip():
                    st.error("Company / organization is required.")
                elif not edit_role.strip():
                    st.error("Job title / role is required.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    UPDATE experiences
                                    SET company = :company,
                                        role = :role,
                                        duration = :duration,
                                        description = :description
                                    WHERE id = :id
                                """),
                                {
                                    "id": selected_id,
                                    "company": edit_company.strip(),
                                    "role": edit_role.strip(),
                                    "duration": edit_duration.strip(),
                                    "description": edit_description.strip(),
                                },
                            )
                            session.commit()

                        st.success("Experience updated successfully.")
                        st.rerun()

                    except Exception:
                        st.error("Could not update the experience record.")

    # ---------------- DELETE ----------------
    with delete_tab:
        st.markdown("### Delete Experience")

        if not experiences:
            st.info("There are no experience records to delete.")
        else:
            delete_id = st.selectbox(
                "Choose a record to delete",
                [item["id"] for item in experiences],
                format_func=lambda item_id: next(
                    f"{item['company']} — {item['role']}"
                    for item in experiences
                    if item["id"] == item_id
                ),
                key="delete_experience_id",
            )

            delete_selected = next(
                item for item in experiences
                if item["id"] == delete_id
            )

            st.warning(
                f"You are about to delete "
                f"{delete_selected['role']} at "
                f"{delete_selected['company']}."
            )

            confirmed = st.checkbox(
                "I confirm that I want to permanently delete this record.",
                key="confirm_delete_experience",
            )

            if st.button(
                "Delete Experience",
                type="primary",
                disabled=not confirmed,
                use_container_width=True,
            ):
                try:
                    with conn.session as session:
                        session.execute(
                            text("""
                                DELETE FROM experiences
                                WHERE id = :id
                            """),
                            {"id": delete_id},
                        )
                        session.commit()

                    st.success("Experience deleted successfully.")
                    st.rerun()

                except Exception:
                    st.error("Could not delete the experience record.")
