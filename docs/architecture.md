# 🏗️ SkillGraph — Architecture

## Architecture Overview

SkillGraph follows a simple layered architecture.

```text
┌──────────────────────┐
│   Streamlit UI       │
│   User Interface     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Python Application │
│   Query Logic        │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Neo4j Python Driver  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│      CognoDB         │
│   Graph Database     │
└──────────────────────┘
```

## Components

### Streamlit
Provides the interactive web interface.

### Python
Handles application logic and executes database queries.

### Neo4j Python Driver
Provides connectivity between Python and CognoDB.

### CognoDB
Stores the graph data and relationships.

### Cypher
Used to query and traverse the graph.

## Data Flow

```text
User Action
    ↓
Streamlit
    ↓
Python Query Function
    ↓
Neo4j Driver
    ↓
CognoDB
    ↓
Cypher Query
    ↓
Result
    ↓
Streamlit Display
```

## Configuration

Database credentials are stored securely using environment variables.

```text
.env
  ↓
Python Configuration
  ↓
Database Connection
```

For deployment, the same values are stored using **Streamlit Secrets**.