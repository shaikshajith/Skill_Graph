# 🔍 SkillGraph — Cypher Queries

SkillGraph uses **Cypher** to query and traverse the graph stored in CognoDB.

## Query Files

```text
cypher/
├── 01_candidate_skills.cypher
├── 02_job_matching.cypher
├── 03_missing_skills.cypher
├── 04_company_jobs.cypher
├── 05_related_skills.cypher
└── 06_multi_hop.cypher
```

## 1. Candidate Skills

Retrieves skills associated with a candidate.

```cypher
MATCH (c:Candidate)-[:HAS_SKILL]->(s:Skill)
WHERE c.id = $candidate_id
RETURN c.name, s.name, s.category
```

## 2. Job Matching

Finds jobs whose required skills match the candidate's skills.

```text
Candidate
 ↓
HAS_SKILL
 ↓
Skill
 ↑
REQUIRES
 ↑
Job
```

## 3. Missing Skills

Compares candidate skills with job requirements to identify missing skills.

```text
Job Requirements
       ↓
Compare
       ↓
Candidate Skills
       ↓
Missing Skills
```

## 4. Company Jobs

Retrieves jobs associated with a company.

```text
Company
   ▲
   │ OFFERED_BY
   │
  Job
```

## 5. Related Skills

Finds skills connected using the `RELATED_TO` relationship.

```text
Python
  │
  ▼
Machine Learning
```

## 6. Multi-Hop Query

Traverses multiple relationships:

```text
Candidate
    ↓
  Skill
    ↓
   Job
    ↓
 Company
```

## Main Cypher Operations

```text
MATCH       → Find graph patterns
WHERE       → Filter results
RETURN      → Return data
COUNT       → Count results
ORDER BY    → Sort results
Parameters  → Pass dynamic values
```

These queries provide the core graph functionality used by the SkillGraph application.