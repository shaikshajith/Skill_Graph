# 🗄️ SkillGraph — Database Design

## Database

SkillGraph uses **CognoDB** as its cloud-based graph database.

The database represents entities as **nodes** and connections as **relationships**.

## Nodes

The main nodes are:

```text
👤 Candidate
🛠️ Skill
💼 Job
🏢 Company
```

## Relationships

```text
(Candidate)-[:HAS_SKILL]->(Skill)

(Job)-[:REQUIRES]->(Skill)

(Job)-[:OFFERED_BY]->(Company)

(Skill)-[:RELATED_TO]->(Skill)
```

## Graph Model

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

## Purpose of Relationships

| Relationship | Purpose |
|---|---|
| `HAS_SKILL` | Connects candidates with their skills |
| `REQUIRES` | Connects jobs with required skills |
| `OFFERED_BY` | Connects jobs with companies |
| `RELATED_TO` | Connects related skills |

## Example

```text
Candidate: Shajith

Skills:
Python
SQL
Machine Learning
Data Analysis
```

These relationships can then be used to find suitable jobs and identify skill gaps.