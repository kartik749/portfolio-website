
import streamlit as st
from sqlalchemy import text


def achievements_admin():
    if not st.session_state.get("admin_authenticated", False):
        st.error("Please log in to manage achievements.")
        return

    conn = st.connection("neon", type="sql")

    st.subheader("Manage Achievements")
    st.caption("Manage your leadership, accomplishments, and milestones.")

    try:
        with conn.session as session:
            records = [
                dict(row)
                for row in session.execute(
                    text("""
                        SELECT id, sort_order, category, title, description
                        FROM achievements
                        ORDER BY sort_order, id
                    """)
                ).mappings().all()
            ]
    except Exception:
        st.error("Could not load achievements from PostgreSQL.")
        return

    st.markdown("### Existing Achievements")

    if records:
        st.dataframe(
            [
                {
                    "ID": r["id"],
                    "Category": r["category"],
                    "Title": r["title"],
                }
                for r in records
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No achievements found. Add your first achievement below.")

    add_tab, edit_tab, delete_tab = st.tabs(
        ["Add Achievement", "Edit Achievement", "Delete Achievement"]
    )

    # ADD
    with add_tab:
        with st.form("add_achievement_form", clear_on_submit=True):
            category = st.text_input(
                "Category",
                placeholder="e.g. Leadership",
            )
            title = st.text_input("Achievement Title")
            description = st.text_area("Description")

            submitted = st.form_submit_button(
                "Add Achievement",
                use_container_width=True,
            )

        if submitted:
            if not title.strip():
                st.error("Achievement title is required.")
            else:
                try:
                    with conn.session as session:
                        next_order = session.execute(
                            text("""
                                SELECT COALESCE(MAX(sort_order), 0) + 1
                                FROM achievements
                            """)
                        ).scalar_one()

                        session.execute(
                            text("""
                                INSERT INTO achievements
                                    (sort_order, category, title, description)
                                VALUES
                                    (:sort_order, :category, :title, :description)
                            """),
                            {
                                "sort_order": next_order,
                                "category": category.strip(),
                                "title": title.strip(),
                                "description": description.strip(),
                            },
                        )
                        session.commit()

                    st.success("Achievement added successfully.")
                    st.rerun()
                except Exception:
                    st.error("Could not add the achievement.")

    # EDIT
    with edit_tab:
        if not records:
            st.info("Add an achievement before editing.")
        else:
            selected_id = st.selectbox(
                "Choose an achievement",
                [r["id"] for r in records],
                format_func=lambda record_id: next(
                    r["title"] for r in records if r["id"] == record_id
                ),
                key="edit_achievement_id",
            )
            selected = next(
                r for r in records if r["id"] == selected_id
            )

            with st.form("edit_achievement_form"):
                edit_category = st.text_input(
                    "Category", value=selected["category"] or ""
                )
                edit_title = st.text_input(
                    "Achievement Title", value=selected["title"] or ""
                )
                edit_description = st.text_area(
                    "Description", value=selected["description"] or ""
                )

                edit_submitted = st.form_submit_button(
                    "Save Changes",
                    use_container_width=True,
                )

            if edit_submitted:
                if not edit_title.strip():
                    st.error("Achievement title is required.")
                else:
                    try:
                        with conn.session as session:
                            session.execute(
                                text("""
                                    UPDATE achievements
                                    SET category = :category,
                                        title = :title,
                                        description = :description
                                    WHERE id = :id
                                """),
                                {
                                    "id": selected_id,
                                    "category": edit_category.strip(),
                                    "title": edit_title.strip(),
                                    "description": edit_description.strip(),
                                },
                            )
                            session.commit()

                        st.success("Achievement updated successfully.")
                        st.rerun()
                    except Exception:
                        st.error("Could not update the achievement.")

    # DELETE
    with delete_tab:
        if not records:
            st.info("There are no achievements to delete.")
        else:
            delete_id = st.selectbox(
                "Choose an achievement to delete",
                [r["id"] for r in records],
                format_func=lambda record_id: next(
                    r["title"] for r in records if r["id"] == record_id
                ),
                key="delete_achievement_id",
            )

            selected_delete = next(
                r for r in records if r["id"] == delete_id
            )
            st.warning(
                f"You are about to delete: {selected_delete['title']}"
            )

            confirmed = st.checkbox(
                "I confirm that I want to permanently delete this achievement.",
                key="confirm_delete_achievement",
            )

            if st.button(
                "Delete Achievement",
                type="primary",
                disabled=not confirmed,
                use_container_width=True,
            ):
                try:
                    with conn.session as session:
                        session.execute(
                            text("""
                                DELETE FROM achievements WHERE id = :id
                            """),
                            {"id": delete_id},
                        )
                        session.commit()

                    st.success("Achievement deleted successfully.")
                    st.rerun()
                except Exception:
                    st.error("Could not delete the achievement.")
