# 👤 SkillGraph — User Guide

## Accessing the Application

Open the deployed Streamlit application in a web browser.

## Main Features

### 👤 Candidate Skills

Select a candidate to view their associated skills.

```text
Candidate
   ↓
Skills
   ↓
Skill Categories
```

### 💼 Job Matching

Use the job matching feature to find jobs related to the candidate's skills.

```text
Candidate Skills
       ↓
Job Requirements
       ↓
Matching Jobs
```

### 📚 Missing Skills

Identifies skills required by a job that the selected candidate does not have.

```text
Required Skills
       ↓
Compare
       ↓
Missing Skills
```

### 🏢 Company Jobs

Explore jobs associated with a selected company.

```text
Company
   ↓
Available Jobs
```

### 🔗 Related Skills

Explore skills connected through the `RELATED_TO` relationship.

```text
Skill
 ↓
Related Skills
```

### 🕸️ Multi-Hop

Explore relationships across multiple graph entities.

```text
Candidate
    ↓
  Skill
    ↓
   Job
    ↓
 Company
```

## Expected Result

The application displays graph-based results through the Streamlit interface without requiring users to directly write Cypher queries.

## Troubleshooting

If the application does not load:

```text
1. Check Streamlit Cloud status
2. Check application logs
3. Verify CognoDB credentials
4. Verify Streamlit Secrets
5. Check database availability
```

## Application Flow

```text
Open Application
       ↓
Select Feature
       ↓
Provide Selection/Input
       ↓
Execute Graph Query
       ↓
View Results
```