import streamlit as st

from queries import (
    get_candidate_skills,
    find_matching_jobs,
    get_missing_skills,
    get_company_jobs,
    get_related_skills,
    get_multi_hop_connections,
)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="SkillGraph",
    page_icon="🔗",
    layout="wide",
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🔗 SkillGraph")
st.subheader("Graph-Based Skill and Job Recommendation System")

st.write(
    "Explore candidate skills, matching jobs, missing skills, "
    "companies, related skills, and graph connections using CognoDB."
)

st.divider()


# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------

st.sidebar.title("SkillGraph")

page = st.sidebar.radio(
    "Choose a feature",
    [
        "Candidate Dashboard",
        "Job Matching",
        "Missing Skills",
        "Company Jobs",
        "Related Skills",
        "Graph Connections",
    ],
)


# --------------------------------------------------
# Candidate Data
# --------------------------------------------------

candidates = {
    "Shajith": "C001",
    "Mohith": "C002",
    "Arjun": "C003",
    "Sneha": "C004",
    "Vamsi": "C005",
    "Manasa": "C006",
    "Kiran": "C007",
    "Subhash": "C008",
    "Aditya": "C009",
    "Nisha": "C010",
}


# --------------------------------------------------
# Company Data
# --------------------------------------------------

companies = {
    "TechNova": "CO001",
    "DataSphere": "CO002",
    "CloudWorks": "CO003",
    "CodeCraft": "CO004",
    "AI Labs": "CO005",
}


# --------------------------------------------------
# Helper Function
# --------------------------------------------------

def display_error(error):
    st.error(f"Something went wrong: {error}")


# ==================================================
# PAGE 1 — CANDIDATE DASHBOARD
# ==================================================

if page == "Candidate Dashboard":

    st.header("👤 Candidate Dashboard")

    candidate_name = st.selectbox(
        "Select Candidate",
        list(candidates.keys()),
    )

    candidate_id = candidates[candidate_name]

    st.divider()

    # ----------------------------------------------
    # Candidate Skills
    # ----------------------------------------------

    st.subheader("🛠️ Candidate Skills")

    try:

        skills = get_candidate_skills(candidate_id)

        if skills:

            skill_columns = st.columns(4)

            for index, row in enumerate(skills):

                with skill_columns[index % 4]:

                    st.info(
                        f"**{row['skill']}**\n\n"
                        f"{row['category']}"
                    )

        else:

            st.warning("No skills found for this candidate.")

    except Exception as error:

        display_error(error)

    st.divider()

    # ----------------------------------------------
    # Recommended Jobs
    # ----------------------------------------------

    st.subheader("💼 Recommended Jobs")

    try:

        jobs = find_matching_jobs(candidate_id)

        if jobs:

            for job in jobs[:5]:

                percentage = job["match_percentage"]

                st.write(
                    f"### {job['job']}"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write(
                        f"📍 **Location:** {job['location']}"
                    )

                with col2:
                    st.write(
                        f"🎯 **Match:** {percentage:.2f}%"
                    )

                with col3:
                    st.write(
                        f"🧩 **Skills:** "
                        f"{job['matched_skills']}/"
                        f"{job['total_required']}"
                    )

                st.progress(
                    min(int(percentage), 100)
                )

                st.divider()

        else:

            st.warning("No matching jobs found.")

    except Exception as error:

        display_error(error)


# ==================================================
# PAGE 2 — JOB MATCHING
# ==================================================

elif page == "Job Matching":

    st.header("💼 Job Matching")

    candidate_name = st.selectbox(
        "Select Candidate",
        list(candidates.keys()),
    )

    candidate_id = candidates[candidate_name]

    st.write(
        f"Showing jobs matching the skills of **{candidate_name}**."
    )

    try:

        jobs = find_matching_jobs(candidate_id)

        if jobs:

            for job in jobs:

                percentage = job["match_percentage"]

                with st.container():

                    st.subheader(job["job"])

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.write(
                            f"📍 {job['location']}"
                        )

                    with col2:
                        st.write(
                            f"🎯 {percentage:.2f}%"
                        )

                    with col3:
                        st.write(
                            f"Matched: "
                            f"{job['matched_skills']}"
                        )

                    with col4:
                        st.write(
                            f"Required: "
                            f"{job['total_required']}"
                        )

                    st.progress(
                        min(int(percentage), 100)
                    )

                    st.divider()

        else:

            st.warning("No jobs found.")

    except Exception as error:

        display_error(error)


# ==================================================
# PAGE 3 — MISSING SKILLS
# ==================================================

elif page == "Missing Skills":

    st.header("📚 Missing Skills Analysis")

    candidate_name = st.selectbox(
        "Select Candidate",
        list(candidates.keys()),
    )

    candidate_id = candidates[candidate_name]

    try:

        jobs = find_matching_jobs(candidate_id)

        if not jobs:

            st.warning("No jobs available.")

        else:

            job_options = {
                job["job"]: job["job_id"]
                for job in jobs
            }

            selected_job = st.selectbox(
                "Select Job",
                list(job_options.keys()),
            )

            job_id = job_options[selected_job]

            st.divider()

            st.subheader(
                f"Skills missing for {selected_job}"
            )

            missing = get_missing_skills(
                candidate_id,
                job_id,
            )

            if missing:

                for skill in missing:

                    st.warning(
                        f"❌ **{skill['missing_skill']}**  \n"
                        f"Category: {skill['category']}"
                    )

            else:

                st.success(
                    "🎉 The candidate has all required skills "
                    "for this job!"
                )

    except Exception as error:

        display_error(error)


# ==================================================
# PAGE 4 — COMPANY JOBS
# ==================================================

elif page == "Company Jobs":

    st.header("🏢 Company Jobs")

    company_name = st.selectbox(
        "Select Company",
        list(companies.keys()),
    )

    company_id = companies[company_name]

    try:

        jobs = get_company_jobs(company_id)

        st.subheader(
            f"Jobs offered by {company_name}"
        )

        if jobs:

            for job in jobs:

                with st.container():

                    st.subheader(job["job"])

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write(
                            f"📍 {job['location']}"
                        )

                    with col2:
                        st.write(
                            f"🎓 {job['experience_level']}"
                        )

                    with col3:
                        st.write(
                            f"🆔 {job['job_id']}"
                        )

                    st.divider()

        else:

            st.warning(
                "No jobs found for this company."
            )

    except Exception as error:

        display_error(error)


# ==================================================
# PAGE 5 — RELATED SKILLS
# ==================================================

elif page == "Related Skills":

    st.header("🔗 Related Skills")

    skill_options = {
        "Python": "S001",
        "SQL": "S002",
        "Java": "S003",
        "Machine Learning": "S004",
        "Deep Learning": "S005",
        "Data Analysis": "S006",
        "Power BI": "S007",
        "Tableau": "S008",
        "PySpark": "S009",
        "AWS": "S010",
        "Docker": "S011",
        "Git": "S012",
        "HTML": "S013",
        "CSS": "S014",
        "JavaScript": "S015",
    }

    skill_name = st.selectbox(
        "Select Skill",
        list(skill_options.keys()),
    )

    skill_id = skill_options[skill_name]

    try:

        related = get_related_skills(skill_id)

        st.subheader(
            f"Skills related to {skill_name}"
        )

        if related:

            for row in related:

                st.info(
                    f"**{row['related_skill']}**  \n"
                    f"Category: {row['category']}"
                )

        else:

            st.info(
                "No related skills found."
            )

    except Exception as error:

        display_error(error)


# ==================================================
# PAGE 6 — GRAPH CONNECTIONS
# ==================================================

elif page == "Graph Connections":

    st.header("🕸️ Graph Connections")

    candidate_name = st.selectbox(
        "Select Candidate",
        list(candidates.keys()),
    )

    candidate_id = candidates[candidate_name]

    try:

        connections = get_multi_hop_connections(
            candidate_id
        )

        st.write(
            f"Showing connections for "
            f"**{candidate_name}**"
        )

        if connections:

            st.dataframe(
                connections,
                use_container_width=True,
            )

            st.divider()

            st.subheader(
                "Graph Traversal"
            )

            st.code(
                """
Candidate
    ↓
HAS_SKILL
    ↓
Skill
    ↑
REQUIRES
    │
   Job
    ↓
OFFERED_BY
    ↓
Company
                """,
                language="text",
            )

        else:

            st.warning(
                "No graph connections found."
            )

    except Exception as error:

        display_error(error)


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.sidebar.divider()

st.sidebar.caption(
    "SkillGraph | Python + Streamlit + Neo4j + CognoDB + Cypher"
)