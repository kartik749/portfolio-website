
import streamlit as st
from sqlalchemy import text


def skills_admin():
    # Protect all skill-management operations.
    if not st.session_state.get("admin_authenticated", False):
        st.error("Please log in to manage skills.")
        return

    conn = st.connection("neon", type="sql")

    st.subheader("Manage Skills")
    st.caption("Add, edit, reorder, or delete your portfolio skills.")

    # Read the current skills from PostgreSQL.
    try:
        with conn.session as session:
            skills = [
                dict(row)
                for row in session.execute(
                    text("""
                        SELECT id, sort_order, name
                        FROM skills
                        ORDER BY sort_order, id
                    """)
                ).mappings().all()
            ]
    except Exception:
        st.error("Could not load skills from the database.")
        return

    # Display current skills.
    st.markdown("### Existing Skills")

    if skills:
        st.dataframe(
            [
                {
                    "ID": skill["id"],
                    "Display Order": skill["sort_order"],
                    "Skill": skill["name"],
                }
                for skill in skills
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No skills found. Add your first skill below.")

    add_tab, edit_tab, delete_tab = st.tabs(
        ["Add Skill", "Edit Skill", "Delete Skill"]
    )

    # ---------------- ADD SKILL ----------------
    with add_tab:
        st.markdown("### Add a Skill")

        with st.form("add_skill_form", clear_on_submit=True):
            name = st.text_input(
                "Skill Name",
                placeholder="e.g. Python",
            )

            submitted = st.form_submit_button(
                "Add Skill",
                use_container_width=True,
            )

        if submitted:
            if not name.strip():
                st.error("Skill name is required.")
            elif any(
                skill["name"].strip().casefold() == name.strip().casefold()
                for skill in skills
            ):
                st.error("This skill already exists.")
            else:
                try:
                    with conn.session as session:
                        next_order = session.execute(
                            text("""
                                SELECT COALESCE(MAX(sort_order), 0) + 1
                                FROM skills
                            """)
                        ).scalar_one()

                        session.execute(
                            text("""
                                INSERT INTO skills (sort_order, name)
                                VALUES (:sort_order, :name)
                            """),
                            {
                                "sort_order": next_order,
                                "name": name.strip(),
                            },
                        )
                        session.commit()

                    st.success("Skill added successfully.")
                    st.rerun()

                except Exception:
                    st.error("Could not add the skill.")

    # ---------------- EDIT SKILL ----------------
    with edit_tab:
        st.markdown("### Edit a Skill")

        if not skills:
            st.info("Add a skill before editing.")
        else:
            selected_id = st.selectbox(
                "Choose a skill",
                [skill["id"] for skill in skills],
                format_func=lambda skill_id: next(
                    skill["name"]
                    for skill in skills
                    if skill["id"] == skill_id
                ),
                key="edit_skill_id",
            )

            selected = next(
                skill for skill in skills
                if skill["id"] == selected_id
            )

            with st.form("edit_skill_form"):
                edited_name = st.text_input(
                    "Skill Name",
                    value=selected["name"],
                )

                edited_order = st.number_input(
                    "Display Order",
                    min_value=1,
                    step=1,
                    value=max(1, selected["sort_order"]),
                )

                edit_submitted = st.form_submit_button(
                    "Save Changes",
                    use_container_width=True,
                )

            if edit_submitted:
                new_name = edited_name.strip()

                if not new_name:
                    st.error("Skill name is required.")
                elif any(
                    skill["id"] != selected_id
                    and skill["name"].strip().casefold()
                    == new_name.casefold()
                    for skill in skills
                ):
                    st.error("Another skill already has this name.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    UPDATE skills
                                    SET name = :name,
                                        sort_order = :sort_order
                                    WHERE id = :id
                                """),
                                {
                                    "id": selected_id,
                                    "name": new_name,
                                    "sort_order": int(edited_order),
                                },
                            )
                            session.commit()

                        st.success("Skill updated successfully.")
                        st.rerun()

                    except Exception:
                        st.error("Could not update the skill.")

    # ---------------- DELETE SKILL ----------------
    with delete_tab:
        st.markdown("### Delete a Skill")

        if not skills:
            st.info("There are no skills to delete.")
        else:
            delete_id = st.selectbox(
                "Choose a skill to delete",
                [skill["id"] for skill in skills],
                format_func=lambda skill_id: next(
                    skill["name"]
                    for skill in skills
                    if skill["id"] == skill_id
                ),
                key="delete_skill_id",
            )

            selected_for_delete = next(
                skill for skill in skills
                if skill["id"] == delete_id
            )

            st.warning(
                f"You are about to delete: "
                f"{selected_for_delete['name']}"
            )

            confirmed = st.checkbox(
                "I confirm that I want to permanently delete this skill.",
                key="confirm_delete_skill",
            )

            if st.button(
                "Delete Skill",
                type="primary",
                disabled=not confirmed,
                use_container_width=True,
            ):
                try:
                    with conn.session as session:
                        session.execute(
                            text("DELETE FROM skills WHERE id = :id"),
                            {"id": delete_id},
                        )
                        session.commit()

                    st.success("Skill deleted successfully.")
                    st.rerun()

                except Exception:
                    st.error("Could not delete the skill.")
