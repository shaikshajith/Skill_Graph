from app.database import Database


def seed_candidate_skills(db):
    relationships = [
        ("C001", "S001"),  # Rahul - Python
        ("C001", "S002"),  # Rahul - SQL
        ("C001", "S004"),  # Rahul - Machine Learning
        ("C001", "S006"),  # Rahul - Data Analysis

        ("C002", "S001"),  # Priya - Python
        ("C002", "S002"),  # Priya - SQL
        ("C002", "S007"),  # Priya - Power BI
        ("C002", "S012"),  # Priya - Git

        ("C003", "S003"),  # Arjun - Java
        ("C003", "S002"),  # Arjun - SQL
        ("C003", "S012"),  # Arjun - Git

        ("C004", "S001"),  # Sneha - Python
        ("C004", "S004"),  # Sneha - Machine Learning
        ("C004", "S006"),  # Sneha - Data Analysis
        ("C004", "S008"),  # Sneha - Tableau

        ("C005", "S001"),  # Vikram - Python
        ("C005", "S009"),  # Vikram - PySpark
        ("C005", "S010"),  # Vikram - AWS
        ("C005", "S012"),  # Vikram - Git

        ("C006", "S001"),  # Anjali - Python
        ("C006", "S004"),  # Anjali - Machine Learning
        ("C006", "S005"),  # Anjali - Deep Learning
        ("C006", "S015"),  # Anjali - JavaScript

        ("C007", "S003"),  # Kiran - Java
        ("C007", "S002"),  # Kiran - SQL
        ("C007", "S011"),  # Kiran - Docker
        ("C007", "S012"),  # Kiran - Git

        ("C008", "S013"),  # Meera - HTML
        ("C008", "S014"),  # Meera - CSS
        ("C008", "S015"),  # Meera - JavaScript
        ("C008", "S012"),  # Meera - Git

        ("C009", "S001"),  # Aditya - Python
        ("C009", "S004"),  # Aditya - Machine Learning
        ("C009", "S009"),  # Aditya - PySpark
        ("C009", "S010"),  # Aditya - AWS

        ("C010", "S001"),  # Nisha - Python
        ("C010", "S002"),  # Nisha - SQL
        ("C010", "S006"),  # Nisha - Data Analysis
        ("C010", "S007"),  # Nisha - Power BI
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (c:Candidate {id: rel[0]})
    MATCH (s:Skill {id: rel[1]})

    MERGE (c)-[:HAS_SKILL]->(s)
    """

    db.execute_query(query, {"relationships": relationships})

    print(
        f"Created/updated {len(relationships)} "
        "Candidate → Skill relationships."
    )
def seed_candidate_projects(db):
    relationships = [
        ("C001", "P001"),  # Rahul - Resume Parser
        ("C002", "P004"),  # Priya - Data Analytics Dashboard
        ("C003", "P008"),  # Arjun - E-Commerce Website
        ("C004", "P002"),  # Sneha - Sales Prediction
        ("C005", "P007"),  # Vikram - ETL Data Pipeline
        ("C006", "P003"),  # Anjali - Image Recognition
        ("C007", "P009"),  # Kiran - Chatbot
        ("C008", "P008"),  # Meera - E-Commerce Website
        ("C009", "P006"),  # Aditya - Customer Churn Prediction
        ("C010", "P004"),  # Nisha - Data Analytics Dashboard
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (c:Candidate {id: rel[0]})
    MATCH (p:Project {id: rel[1]})

    MERGE (c)-[:HAS_PROJECT]->(p)
    """

    db.execute_query(query, {"relationships": relationships})

    print(
        f"Created/updated {len(relationships)} "
        "Candidate → Project relationships."
    )
def seed_candidate_projects(db):
    relationships = [
        ("C001", "P001"),  # Rahul - Resume Parser
        ("C002", "P004"),  # Priya - Data Analytics Dashboard
        ("C003", "P008"),  # Arjun - E-Commerce Website
        ("C004", "P002"),  # Sneha - Sales Prediction
        ("C005", "P007"),  # Vikram - ETL Data Pipeline
        ("C006", "P003"),  # Anjali - Image Recognition
        ("C007", "P009"),  # Kiran - Chatbot
        ("C008", "P008"),  # Meera - E-Commerce Website
        ("C009", "P006"),  # Aditya - Customer Churn Prediction
        ("C010", "P004"),  # Nisha - Data Analytics Dashboard
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (c:Candidate {id: rel[0]})
    MATCH (p:Project {id: rel[1]})

    MERGE (c)-[:HAS_PROJECT]->(p)
    """

    db.execute_query(query, {"relationships": relationships})

    print(
        f"Created/updated {len(relationships)} "
        "Candidate → Project relationships."
    )
def seed_project_skills(db):
    relationships = [
        # Resume Parser
        ("P001", "S001"),
        ("P001", "S002"),

        # Sales Prediction
        ("P002", "S001"),
        ("P002", "S004"),
        ("P002", "S006"),

        # Image Recognition
        ("P003", "S001"),
        ("P003", "S005"),

        # Data Analytics Dashboard
        ("P004", "S002"),
        ("P004", "S006"),
        ("P004", "S007"),

        # Food Donation Platform
        ("P005", "S013"),
        ("P005", "S014"),
        ("P005", "S015"),

        # Customer Churn Prediction
        ("P006", "S001"),
        ("P006", "S004"),
        ("P006", "S002"),

        # ETL Data Pipeline
        ("P007", "S002"),
        ("P007", "S009"),
        ("P007", "S010"),

        # E-Commerce Website
        ("P008", "S013"),
        ("P008", "S014"),
        ("P008", "S015"),

        # Chatbot
        ("P009", "S001"),
        ("P009", "S003"),

        # Cloud Deployment
        ("P010", "S010"),
        ("P010", "S011"),
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (p:Project {id: rel[0]})
    MATCH (s:Skill {id: rel[1]})

    MERGE (p)-[:USES_SKILL]->(s)
    """

    db.execute_query(query, {"relationships": relationships})

    print(
        f"Created/updated {len(relationships)} "
        "Project → Skill relationships."
    )
def seed_job_skills(db):
    relationships = [
        # Data Analyst
        ("J001", "S001"),
        ("J001", "S002"),
        ("J001", "S007"),

        # Machine Learning Engineer
        ("J002", "S001"),
        ("J002", "S004"),
        ("J002", "S005"),

        # Python Developer
        ("J003", "S001"),
        ("J003", "S012"),

        # Data Engineer
        ("J004", "S002"),
        ("J004", "S009"),
        ("J004", "S010"),

        # Backend Developer
        ("J005", "S003"),
        ("J005", "S002"),
        ("J005", "S012"),

        # Frontend Developer
        ("J006", "S013"),
        ("J006", "S014"),
        ("J006", "S015"),

        # AI Engineer
        ("J007", "S001"),
        ("J007", "S004"),
        ("J007", "S005"),

        # Cloud Engineer
        ("J008", "S010"),
        ("J008", "S011"),
        ("J008", "S012"),

        # Software Engineer
        ("J009", "S003"),
        ("J009", "S012"),

        # Business Analyst
        ("J010", "S002"),
        ("J010", "S006"),
        ("J010", "S007"),

        # Junior Data Scientist
        ("J011", "S001"),
        ("J011", "S004"),
        ("J011", "S006"),

        # DevOps Engineer
        ("J012", "S010"),
        ("J012", "S011"),
        ("J012", "S012"),

        # Web Developer
        ("J013", "S013"),
        ("J013", "S014"),
        ("J013", "S015"),

        # BI Developer
        ("J014", "S002"),
        ("J014", "S007"),
        ("J014", "S008"),

        # AI/ML Developer
        ("J015", "S001"),
        ("J015", "S004"),
        ("J015", "S005"),
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (j:Job {id: rel[0]})
    MATCH (s:Skill {id: rel[1]})

    MERGE (j)-[:REQUIRES]->(s)
    """

    db.execute_query(query, {"relationships": relationships})

    print(
        f"Created/updated {len(relationships)} "
        "Job → Skill relationships."
    )
def seed_job_companies(db):
    relationships = [
        ("J001", "CO001"),
        ("J002", "CO005"),
        ("J003", "CO001"),
        ("J004", "CO002"),
        ("J005", "CO004"),
        ("J006", "CO001"),
        ("J007", "CO005"),
        ("J008", "CO003"),
        ("J009", "CO004"),
        ("J010", "CO002"),
        ("J011", "CO005"),
        ("J012", "CO003"),
        ("J013", "CO004"),
        ("J014", "CO002"),
        ("J015", "CO005"),
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (j:Job {id: rel[0]})
    MATCH (c:Company {id: rel[1]})

    MERGE (j)-[:OFFERED_BY]->(c)
    """

    db.execute_query(query, {"relationships": relationships})

    print(
        f"Created/updated {len(relationships)} "
        "Job → Company relationships."
    )
def seed_related_skills(db):
    relationships = [
        ("S001", "S004"),  # Python → Machine Learning
        ("S004", "S005"),  # Machine Learning → Deep Learning
        ("S001", "S006"),  # Python → Data Analysis
        ("S002", "S006"),  # SQL → Data Analysis
        ("S006", "S007"),  # Data Analysis → Power BI
        ("S006", "S008"),  # Data Analysis → Tableau
        ("S009", "S010"),  # PySpark → AWS
        ("S010", "S011"),  # AWS → Docker
        ("S013", "S014"),  # HTML → CSS
        ("S014", "S015"),  # CSS → JavaScript
        ("S003", "S012"),  # Java → Git
        ("S001", "S012"),  # Python → Git
    ]

    query = """
    UNWIND $relationships AS rel

    MATCH (s1:Skill {id: rel[0]})
    MATCH (s2:Skill {id: rel[1]})

    MERGE (s1)-[:RELATED_TO]->(s2)
    """

    db.execute_query(query, {"relationships": relationships})

    print(
        f"Created/updated {len(relationships)} "
        "Skill → Skill relationships."
    )
def main():
    db = Database()

    try:
        db.verify_connection()
        print("Connected to CognoDB.")

        seed_candidate_skills(db)
        seed_candidate_projects(db)
        seed_project_skills(db)
        seed_job_skills(db)
        seed_job_companies(db)
        seed_related_skills(db)

        print("All graph relationships created successfully.")

    except Exception as e:
        print("Relationship seeding failed:")
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()