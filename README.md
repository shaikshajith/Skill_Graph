# 🔗 SkillGraph

> A graph-based skill and job matching application built with **Python, Streamlit, CognoDB, Neo4j Python Driver, and Cypher**.

---
## 🌐 Live Demo

🚀 **Try SkillGraph Live:** [Open SkillGraph Application](https://skillgraph-bnipddc5fwfkfuzd6zwevw.streamlit.app)

The application is deployed using **Streamlit Cloud** and connected to **CognoDB Cloud** for real-time graph-based skill and job analysis.

## 📌 Overview

**SkillGraph** is a graph-based application that connects **candidates, skills, jobs, and companies** using a graph database.

The application allows users to explore candidate skills, find suitable jobs, identify missing skills, discover company jobs, and explore related skills through graph relationships.

---

## 🎯 Objectives

The main objectives of SkillGraph are to:

- 👤 Manage and explore candidate skills
- 💼 Find jobs based on candidate skills
- 📚 Identify missing skills for a job
- 🏢 Explore jobs offered by companies
- 🔗 Discover related skills
- 🕸️ Perform multi-hop graph traversal
- 🔍 Demonstrate practical Cypher graph queries

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 👤 Candidate Skills | View skills associated with a candidate |
| 💼 Job Matching | Find jobs matching candidate skills |
| 📚 Missing Skills | Identify skills required but not available |
| 🏢 Company Jobs | View jobs offered by a company |
| 🔗 Related Skills | Find skills connected to another skill |
| 🕸️ Multi-Hop | Explore Candidate → Skill → Job → Company |

---

## 🧠 How It Works

SkillGraph represents the data as connected graph entities:

```text
        👤 Candidate
             │
         HAS_SKILL
             │
             ▼
          🛠️ Skill
             ▲
             │
          REQUIRES
             │
             │
          💼 Job
             │
         OFFERED_BY
             │
             ▼
         🏢 Company
```

Skills can also be connected to other skills:

```text
🛠️ Skill ── RELATED_TO ──> 🛠️ Skill
```

---

## 🔄 Application Workflow

```text
👤 User
   │
   ▼
🎨 Streamlit Interface
   │
   ▼
🐍 Python Query Layer
   │
   ▼
🔌 Neo4j Python Driver
   │
   ▼
☁️ CognoDB
   │
   ▼
🔍 Cypher Query
   │
   ▼
📊 Graph Results
   │
   ▼
🎨 Streamlit Display
```

---

## 💡 Example

A candidate may have:

```text
Python
SQL
Machine Learning
Data Analysis
```

The application can use these skills to find suitable jobs:

```text
Candidate
    ↓
Candidate Skills
    ↓
Compare with Job Requirements
    ↓
Matching Jobs
    ↓
Missing Skills
```

For example:

```text
Job: Data Analyst

Required:
✓ Python
✓ SQL
✗ Power BI

Candidate:
✓ Python
✓ SQL

Missing Skill:
→ Power BI
```

---

## 🚀 Main Capabilities

```text
👤 Candidate Analysis
        +
💼 Job Matching
        +
📚 Skill Gap Analysis
        +
🏢 Company Exploration
        +
🔗 Related Skills
        +
🕸️ Multi-Hop Graph Queries
        =
       🔗 SkillGraph
```

---
# 🛠️ Tech Stack

SkillGraph is built using the following technologies:

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Application logic and database interaction |
| 🎨 **Streamlit** | Web interface |
| 🔌 **Neo4j Python Driver** | Connects Python with CognoDB |
| ☁️ **CognoDB** | Cloud graph database |
| 🔍 **Cypher** | Query and traverse graph data |
| 🔐 **python-dotenv** | Loads database credentials from `.env` |
| 🐙 **Git & GitHub** | Version control and project hosting |

---

## 🧩 Architecture

```text
                    👤 USER
                      │
                      ▼
              🎨 STREAMLIT UI
                      │
                      ▼
                🐍 PYTHON
                      │
              ┌───────┴───────┐
              │               │
              ▼               ▼
        Query Layer      Configuration
              │               │
              └───────┬───────┘
                      │
                      ▼
            🔌 NEO4J PYTHON DRIVER
                      │
                      ▼
                 ☁️ COGNODB
                      │
                      ▼
                 🔍 CYPHER
                      │
                      ▼
              🕸️ GRAPH RESULTS
                      │
                      ▼
              🎨 STREAMLIT UI
```

---

## 🔄 Data Flow

The application follows this flow:

```text
User Action
     ↓
Streamlit
     ↓
Python Query Function
     ↓
Neo4j Python Driver
     ↓
CognoDB
     ↓
Cypher Query
     ↓
Graph Result
     ↓
Streamlit Display
```

---

## 🎨 Streamlit

Streamlit is used to build the web interface.

It provides the user with options to:

- Select candidates
- View candidate skills
- Find matching jobs
- Identify missing skills
- Explore companies
- Find related skills
- Perform multi-hop queries

---

## 🐍 Python

Python acts as the main application layer.

It handles:

```text
Streamlit UI
     ↓
Query Functions
     ↓
Database Connection
     ↓
CognoDB
```

The code is separated into different modules to keep the application organized.

---

## 🔌 Neo4j Python Driver

The Neo4j Python Driver is used to connect the Python application to CognoDB.

```text
Python
   │
   ▼
Neo4j Python Driver
   │
   ▼
CognoDB
```

It allows Python to execute Cypher queries and retrieve graph results.

---

## ☁️ CognoDB

CognoDB is used as the cloud-based graph database.

It stores:

```text
👤 Candidates
🛠️ Skills
💼 Jobs
🏢 Companies
```

along with their relationships.

---

## 🔍 Cypher

Cypher is used to query the graph database.

Example graph query:

```cypher
MATCH (c:Candidate)-[:HAS_SKILL]->(s:Skill)
WHERE c.id = $candidate_id
RETURN c.name, s.name
```

Cypher allows SkillGraph to perform relationship-based queries efficiently.

---

## 🔐 Environment Configuration

Database credentials are stored in `.env` instead of being written directly in the source code.

```text
.env
 │
 ▼
Environment Variables
 │
 ▼
Python Configuration
 │
 ▼
Database Connection
```

The `.env` file is excluded from GitHub using `.gitignore`.

---

## 🧱 Architecture Summary

```text
┌─────────────────────────────┐
│       🎨 Streamlit          │
│        Web Interface        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│        🐍 Python            │
│   Query & Application Logic │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   🔌 Neo4j Python Driver    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│        ☁️ CognoDB           │
│       Graph Database        │
└─────────────────────────────┘
```

---
# 🕸️ Database & Graph Model

SkillGraph uses **CognoDB** as its cloud graph database. The application stores candidates, skills, jobs, and companies as graph nodes and connects them using relationships.

---

## 🗄️ Graph Data Model

### Nodes

The main nodes used in the application are:

```text
👤 Candidate
🛠️ Skill
💼 Job
🏢 Company
```

### Relationships

```text
(Candidate)-[:HAS_SKILL]->(Skill)

(Job)-[:REQUIRES]->(Skill)

(Job)-[:OFFERED_BY]->(Company)

(Skill)-[:RELATED_TO]->(Skill)
```

---

## 🔗 Graph Structure

```text
                    🏢 Company
                         ▲
                         │
                     OFFERED_BY
                         │
                         │
                    💼 Job
                         │
                      REQUIRES
                         │
                         ▼
                    🛠️ Skill
                         ▲
                         │
                      HAS_SKILL
                         │
                         ▼
                    👤 Candidate

              🛠️ Skill
                  │
              RELATED_TO
                  ▼
              🛠️ Skill
```

This structure allows the application to navigate between related entities instead of treating them as separate records.

---

# 🔍 Cypher Queries

Cypher is used to interact with the graph database.

The project contains six main query files:

```text
cypher/
│
├── 01_candidate_skills.cypher
├── 02_job_matching.cypher
├── 03_missing_skills.cypher
├── 04_company_jobs.cypher
├── 05_related_skills.cypher
└── 06_multi_hop.cypher
```

---

## 1️⃣ Candidate Skills

**File:** `01_candidate_skills.cypher`

Retrieves the skills associated with a candidate.

```cypher
MATCH (c:Candidate)-[:HAS_SKILL]->(s:Skill)
WHERE c.id = $candidate_id
RETURN c.name AS candidate,
       s.name AS skill,
       s.category AS category
```

### Flow

```text
Candidate
    ↓
HAS_SKILL
    ↓
Skill
```

---

## 2️⃣ Job Matching

**File:** `02_job_matching.cypher`

Finds jobs that share skills with a candidate.

```text
Candidate
    ↓
Candidate Skills
    ↓
Compare with Job Requirements
    ↓
Matching Jobs
```

The matching process uses:

```text
Candidate ──HAS_SKILL──> Skill
                            ▲
                            │
                         REQUIRES
                            │
                           Job
```

---

## 3️⃣ Missing Skills

**File:** `03_missing_skills.cypher`

Identifies skills required by a job that are not present in the candidate's skill set.

```text
Job Requirements
       ↓
Candidate Skills
       ↓
Compare
       ↓
Missing Skills
```

Example:

```text
Required Skills
────────────────
Python
SQL
Power BI
Excel

Candidate Skills
────────────────
Python
SQL

Missing Skills
────────────────
Power BI
Excel
```

---

## 4️⃣ Company Jobs

**File:** `04_company_jobs.cypher`

Retrieves jobs offered by a company.

```text
Company
   ▲
   │ OFFERED_BY
   │
  Job
```

This allows users to explore the jobs associated with a selected company.

---

## 5️⃣ Related Skills

**File:** `05_related_skills.cypher`

Finds skills connected through the `RELATED_TO` relationship.

```text
Python
  │
  │ RELATED_TO
  ▼
Machine Learning
```

This can be used to explore the skill graph and discover related technical skills.

---

## 6️⃣ Multi-Hop Query

**File:** `06_multi_hop.cypher`

Demonstrates traversal across multiple nodes and relationships.

```text
Candidate
    ↓
  Skill
    ↓
   Job
    ↓
 Company
```

Example:

```text
Shajith
   ↓
Python
   ↓
Data Analyst
   ↓
Company
```

This demonstrates one of the main advantages of using a graph database: navigating connected information through multiple relationships.

---

# 🧠 Main Cypher Concepts

SkillGraph uses common Cypher operations such as:

### MATCH

Find graph patterns:

```cypher
MATCH (c:Candidate)-[:HAS_SKILL]->(s:Skill)
```

### WHERE

Filter results:

```cypher
WHERE c.id = $candidate_id
```

### RETURN

Return selected data:

```cypher
RETURN c.name, s.name
```

### COUNT

Count matching skills:

```cypher
COUNT(DISTINCT s)
```

### ORDER BY

Sort results:

```cypher
ORDER BY matched_skills DESC
```

### Parameters

Queries use parameters such as:

```cypher
$candidate_id
$job_id
$company_id
$skill_name
```

instead of directly inserting values into the query.

---

# 📊 Query-to-Feature Mapping

| Query File | Feature | Relationship / Operation |
|---|---|---|
| `01_candidate_skills.cypher` | Candidate Skills | `HAS_SKILL` |
| `02_job_matching.cypher` | Job Matching | `HAS_SKILL` + `REQUIRES` |
| `03_missing_skills.cypher` | Missing Skills | Skill comparison |
| `04_company_jobs.cypher` | Company Jobs | `OFFERED_BY` |
| `05_related_skills.cypher` | Related Skills | `RELATED_TO` |
| `06_multi_hop.cypher` | Multi-Hop | Multiple relationships |

---

## 🎯 Graph Query Summary

```text
👤 Candidate
     │
     │ HAS_SKILL
     ▼
🛠️ Skill
     │
     │ REQUIRES
     ▼
💼 Job
     │
     │ OFFERED_BY
     ▼
🏢 Company

🛠️ Skill
     │
     │ RELATED_TO
     ▼
🛠️ Skill
```

These graph relationships power the main features of SkillGraph, including **job matching, skill-gap analysis, company exploration, related-skill discovery, and multi-hop traversal**.
# 🚀 Installation & Setup

Follow the steps below to set up and run SkillGraph locally.

---

## 📋 Prerequisites

Make sure the following are installed:

- 🐍 Python 3.x
- ☁️ CognoDB Cloud C0 instance
- 🐙 Git
- 💻 VS Code or any preferred IDE

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/shaikshajith/Skill_Graph.git
cd Skill_Graph
```

---

## 2️⃣ Create Virtual Environment

```powershell
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

Install the required Python packages:

```powershell
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the **root project folder**:

```text
Skill_Graph/
│
├── app/
├── scripts/
├── cypher/
├── docs/
├── venv/
│
├── .env          ← here
├── .gitignore
├── requirements.txt
└── README.md
```

Add your CognoDB connection details:

```env
NEO4J_URI=your_cognodb_uri
NEO4J_USERNAME=your_username
NEO4J_PASSWORD=your_password
```

> ⚠️ Do not upload the `.env` file to GitHub.

---

## 5️⃣ Configure Git Ignore

The `.gitignore` file should contain:

```gitignore
.env
venv/
.venv/
__pycache__/
*.pyc
```

This prevents sensitive credentials and local Python files from being committed.

---

# 🗄️ Database Setup

After configuring the database connection, initialize the graph database.

---

## 6️⃣ Create Database Constraints

Run:

```powershell
python -m scripts.setup_database
```

Expected result:

```text
Connected to CognoDB.
All database constraints created successfully.
```

---

## 7️⃣ Insert Initial Data

Run:

```powershell
python -m scripts.seed_database
```

This creates the initial candidates, skills, companies, and other required data.

Example output:

```text
Connected to CognoDB.
Created/updated 15 skills.
Created/updated 5 companies.
Initial seed data inserted successfully.
```

---

## 8️⃣ Create Graph Relationships

Run:

```powershell
python -m scripts.seed_relationships
```

This creates relationships such as:

```text
Candidate ──HAS_SKILL──> Skill

Job ──REQUIRES──> Skill

Job ──OFFERED_BY──> Company

Skill ──RELATED_TO──> Skill
```

---

# 🧪 Test the Database

Before starting the web application, verify the main queries:

```powershell
python -m scripts.test_queries
```

This confirms that Python can successfully communicate with CognoDB and execute the required Cypher queries.

---

# ▶️ Run the Streamlit Application

Once the database and queries are working, start the application:

```powershell
python -m streamlit run app/main.py
```

Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🔄 Complete Setup Flow

For a fresh setup, run the following commands in order:

```powershell
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m scripts.setup_database

python -m scripts.seed_database

python -m scripts.seed_relationships

python -m scripts.test_queries

python -m streamlit run app/main.py
```

---

# ✅ Setup Checklist

```text
☐ Python installed
☐ Repository cloned
☐ Virtual environment created
☐ Dependencies installed
☐ CognoDB C0 configured
☐ .env configured
☐ Database connection tested
☐ Constraints created
☐ Seed data inserted
☐ Relationships created
☐ Queries tested
☐ Streamlit application running
```

---

# 🛠️ Troubleshooting

### `ModuleNotFoundError: No module named 'app'`

Run the application from the **project root**:

```powershell
python -m streamlit run app/main.py
```

Do not run `main.py` directly from inside the `app` folder.

---

### Database Connection Error

Check that:

```text
✓ CognoDB instance is running
✓ NEO4J_URI is correct
✓ Username is correct
✓ Password is correct
✓ .env is in the project root
```

---

### Streamlit Not Found

Activate the virtual environment first:

```powershell
venv\Scripts\activate
```

Then install Streamlit:

```powershell
pip install streamlit
```

---

# 🎯 Final Application Flow

```text
Install
   ↓
Configure .env
   ↓
Setup CognoDB
   ↓
Seed Database
   ↓
Create Relationships
   ↓
Test Queries
   ↓
Run Streamlit
   ↓
🎉 SkillGraph Ready
```
# 📁 Project Structure

```text
Skill_Graph/
│
├── app/
│   ├── config.py
│   ├── database.py
│   ├── queries.py
│   └── main.py
│
├── scripts/
│   ├── setup_database.py
│   ├── seed_database.py
│   ├── seed_relationships.py
│   └── test_queries.py
│
├── cypher/
│   ├── 01_candidate_skills.cypher
│   ├── 02_job_matching.cypher
│   ├── 03_missing_skills.cypher
│   ├── 04_company_jobs.cypher
│   ├── 05_related_skills.cypher
│   └── 06_multi_hop.cypher
│
├── docs/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧩 Folder Responsibilities

| Folder / File | Purpose |
|---|---|
| `app/` | Main Streamlit application and database logic |
| `scripts/` | Database setup, seeding, relationships, and testing |
| `cypher/` | Cypher queries used by the project |
| `docs/` | Project documentation |
| `.env` | Local database credentials |
| `.gitignore` | Files excluded from Git |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

# 🔐 Security

Sensitive database credentials are stored in `.env` and are not committed to GitHub.

```text
.env
NEO4J_URI=...
NEO4J_USERNAME=...
NEO4J_PASSWORD=...
```

The `.gitignore` includes:

```gitignore
.env
venv/
.venv/
__pycache__/
*.pyc
```

> ⚠️ Never expose your actual CognoDB password or connection credentials publicly.

---

# 🚀 Future Enhancements

The current application implements the core assignment requirements. Possible future improvements include:

### 👤 Candidate Profiles

Allow users to create and update their own candidate profiles and skills.

### 💼 Advanced Job Matching

Improve matching using additional factors such as:

```text
Skill Match
Experience
Location
Job Requirements
```

### 📚 Skill Recommendations

Recommend skills based on the candidate's target job and missing skills.

```text
Candidate Skills
       ↓
Target Job
       ↓
Missing Skills
       ↓
Recommended Skills
```

### 📊 Analytics Dashboard

Add statistics such as:

```text
Total Candidates
Total Skills
Total Jobs
Total Companies
Most Required Skills
Average Match Percentage
```

### 🕸️ Graph Visualization

Add an interactive visualization of:

```text
Candidate → Skill → Job → Company
```

to make graph relationships easier to explore.

---

# 🏆 Project Highlights

```text
✅ Streamlit Web Application
✅ Python Backend
✅ CognoDB Cloud Integration
✅ Neo4j Python Driver
✅ Cypher Graph Queries
✅ Candidate Skill Analysis
✅ Job Matching
✅ Missing Skill Detection
✅ Company Job Exploration
✅ Related Skill Discovery
✅ Multi-Hop Graph Traversal
```

---

# 🎯 Conclusion

**SkillGraph** demonstrates how graph databases can be used to model and explore connected information between candidates, skills, jobs, and companies.

The project combines:

```text
🐍 Python
      +
🎨 Streamlit
      +
🔌 Neo4j Python Driver
      +
☁️ CognoDB
      +
🔍 Cypher
```

to provide an interactive platform for:

```text
👤 Candidate Analysis
        ↓
🛠️ Skill Exploration
        ↓
💼 Job Matching
        ↓
📚 Skill Gap Analysis
        ↓
🏢 Company Exploration
```

The project provides a practical implementation of graph-based data modeling, Cypher querying, cloud database connectivity, and interactive web development.

---

# 👨‍💻 Author

**Shaik Shajith**

🎓 Computer Science and Engineering

🔗 GitHub: [shaikshajith](https://github.com/shaikshajith)

---

## ⭐ SkillGraph

```text
        👤 Candidates
              │
              ▼
          🛠️ Skills
              │
              ▼
           💼 Jobs
              │
              ▼
         🏢 Companies

       Powered by Graphs 🕸️
```

---