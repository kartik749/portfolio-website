
import streamlit as st
from sqlalchemy import text


def education_admin():
    if not st.session_state.get("admin_authenticated", False):
        st.error("Please log in to manage education.")
        return

    conn = st.connection("neon", type="sql")

    st.subheader("Manage Education")
    st.caption("Manage your degrees and academic qualifications.")

    try:
        with conn.session as session:
            records = [
                dict(row)
                for row in session.execute(
                    text("""
                        SELECT id, sort_order, institute, degree,
                               duration, details
                        FROM education
                        ORDER BY sort_order, id
                    """)
                ).mappings().all()
            ]
    except Exception:
        st.error("Could not load education records.")
        return

    st.markdown("### Existing Education")

    if records:
        st.dataframe(
            [
                {
                    "ID": r["id"],
                    "Institution": r["institute"],
                    "Degree": r["degree"],
                    "Duration": r["duration"],
                }
                for r in records
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No education records found.")

    add_tab, edit_tab, delete_tab = st.tabs(
        ["Add Education", "Edit Education", "Delete Education"]
    )

    # ADD
    with add_tab:
        with st.form("add_education_form", clear_on_submit=True):
            institute = st.text_input("Institution")
            degree = st.text_input("Degree / Qualification")
            duration = st.text_input(
                "Duration",
                placeholder="August 2023 – May 2027",
            )
            details = st.text_area(
                "Details",
                placeholder="CGPA, specialization, or other details",
            )
            submitted = st.form_submit_button(
                "Add Education",
                use_container_width=True,
            )

        if submitted:
            if not institute.strip() or not degree.strip():
                st.error("Institution and degree are required.")
            else:
                try:
                    with conn.session as session:
                        next_order = session.execute(
                            text("""
                                SELECT COALESCE(MAX(sort_order), 0) + 1
                                FROM education
                            """)
                        ).scalar_one()

                        session.execute(
                            text("""
                                INSERT INTO education
                                    (sort_order, institute, degree,
                                     duration, details)
                                VALUES
                                    (:sort_order, :institute, :degree,
                                     :duration, :details)
                            """),
                            {
                                "sort_order": next_order,
                                "institute": institute.strip(),
                                "degree": degree.strip(),
                                "duration": duration.strip(),
                                "details": details.strip(),
                            },
                        )
                        session.commit()

                    st.success("Education added successfully.")
                    st.rerun()
                except Exception:
                    st.error("Could not add education.")

    # EDIT
    with edit_tab:
        if not records:
            st.info("Add an education record before editing.")
        else:
            selected_id = st.selectbox(
                "Choose a record to edit",
                [r["id"] for r in records],
                format_func=lambda record_id: next(
                    r["institute"] for r in records
                    if r["id"] == record_id
                ),
                key="edit_education_id",
            )
            selected = next(
                r for r in records if r["id"] == selected_id
            )

            with st.form("edit_education_form"):
                edit_institute = st.text_input(
                    "Institution", value=selected["institute"] or ""
                )
                edit_degree = st.text_input(
                    "Degree / Qualification",
                    value=selected["degree"] or "",
                )
                edit_duration = st.text_input(
                    "Duration", value=selected["duration"] or ""
                )
                edit_details = st.text_area(
                    "Details", value=selected["details"] or ""
                )
                edit_submitted = st.form_submit_button(
                    "Save Changes",
                    use_container_width=True,
                )

            if edit_submitted:
                if not edit_institute.strip() or not edit_degree.strip():
                    st.error("Institution and degree are required.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    UPDATE education
                                    SET institute = :institute,
                                        degree = :degree,
                                        duration = :duration,
                                        details = :details
                                    WHERE id = :id
                                """),
                                {
                                    "id": selected_id,
                                    "institute": edit_institute.strip(),
                                    "degree": edit_degree.strip(),
                                    "duration": edit_duration.strip(),
                                    "details": edit_details.strip(),
                                },
                            )
                            session.commit()

                        st.success("Education updated successfully.")
                        st.rerun()
                    except Exception:
                        st.error("Could not update education.")

    # DELETE
    with delete_tab:
        if not records:
            st.info("There are no education records to delete.")
        else:
            delete_id = st.selectbox(
                "Choose a record to delete",
                [r["id"] for r in records],
                format_func=lambda record_id: next(
                    r["institute"] for r in records
                    if r["id"] == record_id
                ),
                key="delete_education_id",
            )

            selected_delete = next(
                r for r in records if r["id"] == delete_id
            )
            st.warning(
                f"You are about to delete: "
                f"{selected_delete['institute']}"
            )

            confirmed = st.checkbox(
                "I confirm that I want to permanently delete this record.",
                key="confirm_delete_education",
            )

            if st.button(
                "Delete Education",
                type="primary",
                disabled=not confirmed,
                use_container_width=True,
            ):
                try:
                    with conn.session as session:
                        session.execute(
                            text("DELETE FROM education WHERE id = :id"),
                            {"id": delete_id},
                        )
                        session.commit()

                    st.success("Education deleted successfully.")
                    st.rerun()
                except Exception:
                    st.error("Could not delete education.")
