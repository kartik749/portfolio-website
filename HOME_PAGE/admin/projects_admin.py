
import streamlit as st
from sqlalchemy import text


def projects_admin():
    # Protect the page before displaying or modifying data.
    if not st.session_state.get("admin_authenticated", False):
        st.error("Please log in to manage projects.")
        return

    conn = st.connection("neon", type="sql")

    st.subheader("Manage Projects")
    st.caption("Add, edit, view, or delete your portfolio projects.")

    # Fetch projects directly from PostgreSQL.
    try:
        with conn.session as session:
            projects = [
                dict(row)
                for row in session.execute(
                    text("""
                        SELECT id, sort_order, number, name,
                               description, technologies
                        FROM projects
                        ORDER BY sort_order, id
                    """)
                ).mappings().all()
            ]
    except Exception:
        st.error("Could not load projects from the database.")
        st.exception(Exception("Check your database connection and table."))
        return

    if projects:
        st.markdown("### Existing Projects")
        st.dataframe(
            [
                {
                    "ID": p["id"],
                    "Number": p["number"],
                    "Project": p["name"],
                    "Technologies": p["technologies"],
                }
                for p in projects
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No projects found. Add your first project below.")

    add_tab, edit_tab, delete_tab = st.tabs(
        ["Add Project", "Edit Project", "Delete Project"]
    )

    # ---------------- ADD PROJECT ----------------
    with add_tab:
        st.markdown("### Add a New Project")

        with st.form("add_project_form", clear_on_submit=True):
            number = st.text_input(
                "Display Number",
                placeholder="03",
            )
            name = st.text_input("Project Name")
            description = st.text_area("Description")
            technologies = st.text_input(
                "Technologies",
                placeholder="Python · FastAPI · PostgreSQL",
            )

            add_submitted = st.form_submit_button(
                "Add Project",
                use_container_width=True,
            )

        if add_submitted:
            if not name.strip():
                st.error("Project name is required.")
            else:
                try:
                    with conn.session as session:
                        next_order = session.execute(
                            text("""
                                SELECT COALESCE(MAX(sort_order), 0) + 1
                                FROM projects
                            """)
                        ).scalar_one()

                        session.execute(
                            text("""
                                INSERT INTO projects
                                    (sort_order, number, name,
                                     description, technologies)
                                VALUES
                                    (:sort_order, :number, :name,
                                     :description, :technologies)
                            """),
                            {
                                "sort_order": next_order,
                                "number": number.strip() or None,
                                "name": name.strip(),
                                "description": description.strip(),
                                "technologies": technologies.strip(),
                            },
                        )
                        session.commit()

                    st.success("Project added successfully.")
                    st.rerun()

                except Exception:
                    st.error("Could not add the project.")
                    st.exception(
                        Exception("Check the database connection and schema.")
                    )

    # ---------------- EDIT PROJECT ----------------
    with edit_tab:
        st.markdown("### Edit an Existing Project")

        if not projects:
            st.info("Add a project before editing.")
        else:
            project_ids = [p["id"] for p in projects]
            selected_id = st.selectbox(
                "Choose a project",
                project_ids,
                format_func=lambda project_id: next(
                    p["name"] for p in projects
                    if p["id"] == project_id
                ),
                key="edit_project_id",
            )

            selected = next(
                p for p in projects if p["id"] == selected_id
            )

            with st.form("edit_project_form"):
                edit_number = st.text_input(
                    "Display Number",
                    value=selected["number"] or "",
                )
                edit_name = st.text_input(
                    "Project Name",
                    value=selected["name"] or "",
                )
                edit_description = st.text_area(
                    "Description",
                    value=selected["description"] or "",
                )
                edit_technologies = st.text_input(
                    "Technologies",
                    value=selected["technologies"] or "",
                )

                edit_submitted = st.form_submit_button(
                    "Save Changes",
                    use_container_width=True,
                )

            if edit_submitted:
                if not edit_name.strip():
                    st.error("Project name is required.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    UPDATE projects
                                    SET number = :number,
                                        name = :name,
                                        description = :description,
                                        technologies = :technologies
                                    WHERE id = :id
                                """),
                                {
                                    "id": selected_id,
                                    "number": edit_number.strip() or None,
                                    "name": edit_name.strip(),
                                    "description": edit_description.strip(),
                                    "technologies": edit_technologies.strip(),
                                },
                            )
                            session.commit()

                        st.success("Project updated successfully.")
                        st.rerun()

                    except Exception:
                        st.error("Could not update the project.")
                        st.exception(
                            Exception("Check the database connection and schema.")
                        )

    # ---------------- DELETE PROJECT ----------------
    with delete_tab:
        st.markdown("### Delete a Project")

        if not projects:
            st.info("There are no projects to delete.")
        else:
            delete_id = st.selectbox(
                "Choose a project to delete",
                [p["id"] for p in projects],
                format_func=lambda project_id: next(
                    p["name"] for p in projects
                    if p["id"] == project_id
                ),
                key="delete_project_id",
            )

            delete_selected = next(
                p for p in projects if p["id"] == delete_id
            )

            st.warning(
                f"You are about to delete: {delete_selected['name']}"
            )

            confirm_delete = st.checkbox(
                "I confirm that I want to permanently delete this project.",
                key="confirm_delete_project",
            )

            if st.button(
                "Delete Project",
                type="primary",
                disabled=not confirm_delete,
                use_container_width=True,
            ):
                try:
                    with conn.session as session:
                        session.execute(
                            text("DELETE FROM projects WHERE id = :id"),
                            {"id": delete_id},
                        )
                        session.commit()

                    st.success("Project deleted successfully.")
                    st.rerun()

                except Exception:
                    st.error("Could not delete the project.")
                    st.exception(
                        Exception("Check the database connection and schema.")
                    )
