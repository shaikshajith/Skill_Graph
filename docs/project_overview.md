# 📌 SkillGraph — Project Overview

## Overview

**SkillGraph** is a graph-based application that connects candidates, skills, jobs, and companies using **CognoDB**.

The application provides an interactive **Streamlit** interface for exploring graph relationships and performing skill-based job analysis.

## Objectives

- 👤 Explore candidate skills
- 💼 Find suitable jobs
- 📚 Identify missing skills
- 🏢 Explore company jobs
- 🔗 Discover related skills
- 🕸️ Perform multi-hop graph queries

## Key Features

| Feature | Description |
|---|---|
| Candidate Skills | Displays skills associated with a candidate |
| Job Matching | Finds jobs related to candidate skills |
| Missing Skills | Identifies required skills not possessed by a candidate |
| Company Jobs | Displays jobs offered by companies |
| Related Skills | Finds connected skills |
| Multi-Hop Queries | Traverses multiple graph relationships |

## Technology Stack

```text
Python
   +
Streamlit
   +
Neo4j Python Driver
   +
CognoDB
   +
Cypher
```

## Project Workflow

```text
User
 ↓
Streamlit
 ↓
Python
 ↓
Neo4j Python Driver
 ↓
CognoDB
 ↓
Cypher
 ↓
Graph Results
 ↓
Streamlit
```

## Outcome

SkillGraph demonstrates how graph databases can be used to model connected information and perform relationship-based queries for skill and job analysis.