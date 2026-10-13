
import streamlit as st
from sqlalchemy import text

from HOME_PAGE.data.portfolio_data import (
    SKILLS,
    PROJECTS,
    EXPERIENCES,
    EDUCATION,
    ACHIEVEMENTS,
    CERTIFICATIONS,
    CODING_PROFILES,
)

conn = st.connection("neon", type="sql")

# Each table stores one type of portfolio content.
CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS skills (
        id SERIAL PRIMARY KEY,
        sort_order INTEGER NOT NULL,
        name TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS projects (
        id SERIAL PRIMARY KEY,
        sort_order INTEGER NOT NULL,
        number TEXT,
        name TEXT NOT NULL,
        description TEXT,
        technologies TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS experiences (
        id SERIAL PRIMARY KEY,
        sort_order INTEGER NOT NULL,
        company TEXT NOT NULL,
        role TEXT,
        duration TEXT,
        description TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS education (
        id SERIAL PRIMARY KEY,
        sort_order INTEGER NOT NULL,
        institute TEXT NOT NULL,
        degree TEXT,
        duration TEXT,
        details TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS achievements (
        id SERIAL PRIMARY KEY,
        sort_order INTEGER NOT NULL,
        category TEXT,
        title TEXT NOT NULL,
        description TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS certifications (
        id SERIAL PRIMARY KEY,
        sort_order INTEGER NOT NULL,
        provider TEXT,
        name TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS coding_profiles (
        id SERIAL PRIMARY KEY,
        sort_order INTEGER NOT NULL,
        platform TEXT NOT NULL,
        description TEXT,
        url TEXT
    )
    """,
]


# Seed data only when each table is empty.
# Running this script again will not duplicate existing rows.
SEED_DATA = {
    "skills": (
        SKILLS,
        """
        INSERT INTO skills (sort_order, name)
        VALUES (:sort_order, :name)
        """,
        lambda item, i: {
            "sort_order": i,
            "name": item,
        },
    ),
    "projects": (
        PROJECTS,
        """
        INSERT INTO projects
            (sort_order, number, name, description, technologies)
        VALUES
            (:sort_order, :number, :name, :description, :technologies)
        """,
        lambda item, i: {
            "sort_order": i,
            "number": item.get("number"),
            "name": item["name"],
            "description": item.get("description"),
            "technologies": item.get("technologies"),
        },
    ),
    "experiences": (
        EXPERIENCES,
        """
        INSERT INTO experiences
            (sort_order, company, role, duration, description)
        VALUES
            (:sort_order, :company, :role, :duration, :description)
        """,
        lambda item, i: {
            "sort_order": i,
            "company": item["company"],
            "role": item.get("role"),
            "duration": item.get("duration"),
            "description": item.get("description"),
        },
    ),
    "education": (
        EDUCATION,
        """
        INSERT INTO education
            (sort_order, institute, degree, duration, details)
        VALUES
            (:sort_order, :institute, :degree, :duration, :details)
        """,
        lambda item, i: {
            "sort_order": i,
            "institute": item["institute"],
            "degree": item.get("degree"),
            "duration": item.get("duration"),
            "details": item.get("details"),
        },
    ),
    "achievements": (
        ACHIEVEMENTS,
        """
        INSERT INTO achievements
            (sort_order, category, title, description)
        VALUES
            (:sort_order, :category, :title, :description)
        """,
        lambda item, i: {
            "sort_order": i,
            "category": item.get("category"),
            "title": item["title"],
            "description": item.get("description"),
        },
    ),
    "certifications": (
        CERTIFICATIONS,
        """
        INSERT INTO certifications
            (sort_order, provider, name)
        VALUES
            (:sort_order, :provider, :name)
        """,
        lambda item, i: {
            "sort_order": i,
            "provider": item.get("provider"),
            "name": item["name"],
        },
    ),
    "coding_profiles": (
        CODING_PROFILES,
        """
        INSERT INTO coding_profiles
            (sort_order, platform, description, url)
        VALUES
            (:sort_order, :platform, :description, :url)
        """,
        lambda item, i: {
            "sort_order": i,
            "platform": item["platform"],
            "description": item.get("description"),
            "url": item.get("url"),
        },
    ),
}


try:
    with conn.session as session:
        # Create the tables first.
        for statement in CREATE_TABLES:
            session.execute(text(statement))

        # Populate empty tables with the initial portfolio data.
        for table, (items, insert_sql, make_params) in SEED_DATA.items():
            count = session.execute(
                text(f"SELECT COUNT(*) FROM {table}")
            ).scalar_one()

            if count == 0 and items:
                for i, item in enumerate(items, start=1):
                    session.execute(
                        text(insert_sql),
                        make_params(item, i),
                    )

        session.commit()

        # Verify the final row counts.
        counts = {}
        for table in SEED_DATA:
            counts[table] = session.execute(
                text(f"SELECT COUNT(*) FROM {table}")
            ).scalar_one()

    st.success("Portfolio database initialized successfully!")

    st.write("Rows stored in each table:")
    st.table(
        [
            {"Table": table, "Rows": count}
            for table, count in counts.items()
        ]
    )

except Exception as error:
    st.error("Database initialization failed.")
    st.exception(error)
