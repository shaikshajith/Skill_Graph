from app.database import Database


def get_candidate_skills(candidate_id):
    db = Database()

    try:
        query = """
        MATCH (c:Candidate {id: $candidate_id})
              -[:HAS_SKILL]->
              (s:Skill)
        RETURN
            c.name AS candidate,
            s.id AS skill_id,
            s.name AS skill,
            s.category AS category
        ORDER BY s.name
        """

        return db.execute_query(
            query,
            {"candidate_id": candidate_id}
        )

    finally:
        db.close()

def find_matching_jobs(candidate_id):
    db = Database()

    try:
        query = """
        MATCH (c:Candidate {id: $candidate_id})-[:HAS_SKILL]->(s:Skill)
        MATCH (j:Job)-[:REQUIRES]->(s)

        WITH c, j, COUNT(DISTINCT s) AS matched_skills

        MATCH (j)-[:REQUIRES]->(required:Skill)

        WITH
            c,
            j,
            matched_skills,
            COUNT(DISTINCT required) AS total_required

        RETURN
            c.name AS candidate,
            j.id AS job_id,
            j.title AS job,
            j.location AS location,
            matched_skills,
            total_required,
            100.0 * matched_skills / total_required AS match_percentage

        ORDER BY match_percentage DESC
        """

        return db.execute_query(
            query,
            {"candidate_id": candidate_id}
        )


    finally:
        db.close()
def get_missing_skills(candidate_id, job_id):
    db = Database()

    try:
        query = """
        MATCH (c:Candidate {id: $candidate_id})
              -[:HAS_SKILL]->
              (owned:Skill)

        WITH c, COLLECT(owned.id) AS owned_skills

        MATCH (j:Job {id: $job_id})
              -[:REQUIRES]->
              (required:Skill)

        WHERE NOT required.id IN owned_skills

        RETURN
            c.name AS candidate,
            j.id AS job_id,
            j.title AS job,
            required.id AS skill_id,
            required.name AS missing_skill,
            required.category AS category

        ORDER BY required.name
        """

        return db.execute_query(
            query,
            {
                "candidate_id": candidate_id,
                "job_id": job_id
            }
        )

    finally:
        db.close()
def get_company_jobs(company_id):
    db = Database()

    try:
        query = """
        MATCH (c:Company {id: $company_id})
              <-[:OFFERED_BY]-
              (j:Job)

        RETURN
            c.name AS company,
            j.id AS job_id,
            j.title AS job,
            j.location AS location,
            j.experience_level AS experience_level

        ORDER BY j.title
        """

        return db.execute_query(
            query,
            {"company_id": company_id}
        )

    finally:
        db.close()
def get_related_skills(skill_id):
    db = Database()

    try:
        query = """
        MATCH (s:Skill {id: $skill_id})
              -[:RELATED_TO]->
              (related:Skill)

        RETURN
            s.id AS skill_id,
            s.name AS skill,
            related.id AS related_skill_id,
            related.name AS related_skill,
            related.category AS category

        ORDER BY related.name
        """

        return db.execute_query(
            query,
            {"skill_id": skill_id}
        )

    finally:
        db.close()
def get_multi_hop_connections(candidate_id):
    db = Database()

    try:
        query = """
        MATCH (c:Candidate {id: $candidate_id})
              -[:HAS_SKILL]->
              (s:Skill)
              <-[:REQUIRES]-
              (j:Job)
              -[:OFFERED_BY]->
              (company:Company)

        RETURN DISTINCT
            c.name AS candidate,
            s.name AS skill,
            j.id AS job_id,
            j.title AS job,
            company.id AS company_id,
            company.name AS company

        ORDER BY job, company, skill
        """

        return db.execute_query(
            query,
            {"candidate_id": candidate_id}
        )

    finally:
        db.close()
def get_all_candidates():
    db = Database()

    try:
        query = """
        MATCH (c:Candidate)
        RETURN
            c.id AS candidate_id,
            c.name AS candidate
        ORDER BY c.name
        """

        return db.execute_query(query)

    finally:
        db.close()