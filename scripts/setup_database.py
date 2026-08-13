from app.database import Database


def setup_database():
    db = Database()

    constraints = [
        """
        CREATE CONSTRAINT candidate_id_unique IF NOT EXISTS
        FOR (c:Candidate)
        REQUIRE c.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT skill_id_unique IF NOT EXISTS
        FOR (s:Skill)
        REQUIRE s.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT job_id_unique IF NOT EXISTS
        FOR (j:Job)
        REQUIRE j.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT company_id_unique IF NOT EXISTS
        FOR (c:Company)
        REQUIRE c.id IS UNIQUE
        """,

        """
        CREATE CONSTRAINT project_id_unique IF NOT EXISTS
        FOR (p:Project)
        REQUIRE p.id IS UNIQUE
        """
    ]

    try:
        db.verify_connection()
        print("Connected to CognoDB.")

        for constraint in constraints:
            db.execute_query(constraint)

        print("All database constraints created successfully.")

    except Exception as e:
        print("Database setup failed:")
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    setup_database()