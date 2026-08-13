from app.database import Database


def seed_skills(db):
    skills = [
        {"id": "S001", "name": "Python", "category": "Programming"},
        {"id": "S002", "name": "SQL", "category": "Database"},
        {"id": "S003", "name": "Java", "category": "Programming"},
        {"id": "S004", "name": "Machine Learning", "category": "AI"},
        {"id": "S005", "name": "Deep Learning", "category": "AI"},
        {"id": "S006", "name": "Data Analysis", "category": "Data"},
        {"id": "S007", "name": "Power BI", "category": "Visualization"},
        {"id": "S008", "name": "Tableau", "category": "Visualization"},
        {"id": "S009", "name": "PySpark", "category": "Data Engineering"},
        {"id": "S010", "name": "AWS", "category": "Cloud"},
        {"id": "S011", "name": "Docker", "category": "DevOps"},
        {"id": "S012", "name": "Git", "category": "Tools"},
        {"id": "S013", "name": "HTML", "category": "Web Development"},
        {"id": "S014", "name": "CSS", "category": "Web Development"},
        {"id": "S015", "name": "JavaScript", "category": "Web Development"},
    ]

    query = """
    UNWIND $skills AS skill
    MERGE (s:Skill {id: skill.id})
    SET s.name = skill.name,
        s.category = skill.category
    """

    db.execute_query(query, {"skills": skills})

    print(f"Created/updated {len(skills)} skills.")


def seed_companies(db):
    companies = [
        {
            "id": "CO001",
            "name": "TechNova",
            "industry": "Information Technology",
            "location": "Hyderabad",
        },
        {
            "id": "CO002",
            "name": "DataSphere",
            "industry": "Data Analytics",
            "location": "Bengaluru",
        },
        {
            "id": "CO003",
            "name": "CloudWorks",
            "industry": "Cloud Computing",
            "location": "Hyderabad",
        },
        {
            "id": "CO004",
            "name": "InnovateLabs",
            "industry": "Software",
            "location": "Bengaluru",
        },
        {
            "id": "CO005",
            "name": "AI Solutions",
            "industry": "Artificial Intelligence",
            "location": "Pune",
        },
    ]

    query = """
    UNWIND $companies AS company
    MERGE (c:Company {id: company.id})
    SET c.name = company.name,
        c.industry = company.industry,
        c.location = company.location
    """

    db.execute_query(query, {"companies": companies})

    print(f"Created/updated {len(companies)} companies.")
def seed_candidates(db):
    candidates = [
        {
            "id": "C001",
            "name": "Shajith",
            "education": "B.Tech Computer Science",
            "experience_years": 0,
            "location": "Bhimavaram",
        },
        {
            "id": "C002",
            "name": "Mohith",
            "education": "B.Tech Information Technology",
            "experience_years": 1,
            "location": "Bengaluru",
        },
        {
            "id": "C003",
            "name": "Arjun",
            "education": "B.Tech Computer Science",
            "experience_years": 0,
            "location": "Hyderabad",
        },
        {
            "id": "C004",
            "name": "Sneha",
            "education": "B.Tech Data Science",
            "experience_years": 1,
            "location": "Pune",
        },
        {
            "id": "C005",
            "name": "vamsi",
            "education": "B.Tech Computer Science",
            "experience_years": 2,
            "location": "Bengaluru",
        },
        {
            "id": "C006",
            "name": "Manasa",
            "education": "B.Tech Artificial Intelligence",
            "experience_years": 0,
            "location": "Hyderabad",
        },
        {
            "id": "C007",
            "name": "Kiran",
            "education": "B.Tech Information Technology",
            "experience_years": 1,
            "location": "Chennai",
        },
        {
            "id": "C008",
            "name": "Subhash",
            "education": "B.Tech Computer Science",
            "experience_years": 0,
            "location": "Pune",
        },
        {
            "id": "C009",
            "name": "Aditya",
            "education": "B.Tech Data Science",
            "experience_years": 2,
            "location": "Bengaluru",
        },
        {
            "id": "C010",
            "name": "Nisha",
            "education": "B.Tech Computer Science",
            "experience_years": 1,
            "location": "Hyderabad",
        },
    ]

    query = """
    UNWIND $candidates AS candidate

    MERGE (c:Candidate {id: candidate.id})

    SET c.name = candidate.name,
        c.education = candidate.education,
        c.experience_years = candidate.experience_years,
        c.location = candidate.location
    """

    db.execute_query(query, {"candidates": candidates})

    print(f"Created/updated {len(candidates)} candidates.")
def seed_projects(db):
    projects = [
        {
            "id": "P001",
            "name": "Resume Parser",
            "description": "A system that extracts information and skills from resumes.",
        },
        {
            "id": "P002",
            "name": "Sales Prediction",
            "description": "A machine learning project for predicting future sales.",
        },
        {
            "id": "P003",
            "name": "Image Recognition",
            "description": "An image recognition application using deep learning.",
        },
        {
            "id": "P004",
            "name": "Data Analytics Dashboard",
            "description": "An interactive dashboard for analyzing business data.",
        },
        {
            "id": "P005",
            "name": "Food Donation Platform",
            "description": "A web application connecting food donors with organizations.",
        },
        {
            "id": "P006",
            "name": "Customer Churn Prediction",
            "description": "A machine learning model for predicting customer churn.",
        },
        {
            "id": "P007",
            "name": "ETL Data Pipeline",
            "description": "A data engineering project for processing and transforming data.",
        },
        {
            "id": "P008",
            "name": "E-Commerce Website",
            "description": "A web application for managing online products and orders.",
        },
        {
            "id": "P009",
            "name": "Chatbot",
            "description": "A chatbot application for answering user questions.",
        },
        {
            "id": "P010",
            "name": "Cloud Deployment Project",
            "description": "A project demonstrating application deployment using cloud services.",
        },
    ]

    query = """
    UNWIND $projects AS project

    MERGE (p:Project {id: project.id})

    SET p.name = project.name,
        p.description = project.description
    """

    db.execute_query(query, {"projects": projects})

    print(f"Created/updated {len(projects)} projects.")
def seed_jobs(db):
    jobs = [
        {
            "id": "J001",
            "title": "Data Analyst",
            "experience_level": "Entry Level",
            "location": "Hyderabad",
        },
        {
            "id": "J002",
            "title": "Machine Learning Engineer",
            "experience_level": "Entry Level",
            "location": "Bengaluru",
        },
        {
            "id": "J003",
            "title": "Python Developer",
            "experience_level": "Entry Level",
            "location": "Hyderabad",
        },
        {
            "id": "J004",
            "title": "Data Engineer",
            "experience_level": "Entry Level",
            "location": "Bengaluru",
        },
        {
            "id": "J005",
            "title": "Backend Developer",
            "experience_level": "Entry Level",
            "location": "Pune",
        },
        {
            "id": "J006",
            "title": "Frontend Developer",
            "experience_level": "Entry Level",
            "location": "Hyderabad",
        },
        {
            "id": "J007",
            "title": "AI Engineer",
            "experience_level": "Entry Level",
            "location": "Pune",
        },
        {
            "id": "J008",
            "title": "Cloud Engineer",
            "experience_level": "Entry Level",
            "location": "Hyderabad",
        },
        {
            "id": "J009",
            "title": "Software Engineer",
            "experience_level": "Entry Level",
            "location": "Bengaluru",
        },
        {
            "id": "J010",
            "title": "Business Analyst",
            "experience_level": "Entry Level",
            "location": "Pune",
        },
        {
            "id": "J011",
            "title": "Junior Data Scientist",
            "experience_level": "Entry Level",
            "location": "Bengaluru",
        },
        {
            "id": "J012",
            "title": "DevOps Engineer",
            "experience_level": "Entry Level",
            "location": "Hyderabad",
        },
        {
            "id": "J013",
            "title": "Web Developer",
            "experience_level": "Entry Level",
            "location": "Pune",
        },
        {
            "id": "J014",
            "title": "BI Developer",
            "experience_level": "Entry Level",
            "location": "Bengaluru",
        },
        {
            "id": "J015",
            "title": "AI/ML Developer",
            "experience_level": "Entry Level",
            "location": "Hyderabad",
        },
    ]

    query = """
    UNWIND $jobs AS job

    MERGE (j:Job {id: job.id})

    SET j.title = job.title,
        j.experience_level = job.experience_level,
        j.location = job.location
    """

    db.execute_query(query, {"jobs": jobs})

    print(f"Created/updated {len(jobs)} jobs.")


def main():
    db = Database()

    try:
        db.verify_connection()
        print("Connected to CognoDB.")

        seed_skills(db)
        seed_companies(db)
        seed_candidates(db)
        seed_projects(db)
        seed_jobs(db)

        print("Initial seed data inserted successfully.")

    except Exception as e:
        print("Seed operation failed:")
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    main()