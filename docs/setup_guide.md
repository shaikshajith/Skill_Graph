# 🚀 SkillGraph — Setup Guide

## Requirements

- Python 3.x
- CognoDB Cloud C0 instance
- Git
- Streamlit

## 1. Clone Repository

```bash
git clone https://github.com/shaikshajith/Skill_Graph.git
cd Skill_Graph
```

## 2. Create Virtual Environment

```powershell
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

## 4. Configure Environment

Create `.env` in the project root:

```env
COGNODB_URI=your_uri
COGNODB_USERNAME=your_username
COGNODB_PASSWORD=your_password
```

Do not commit `.env` to GitHub.

## 5. Setup Database

```powershell
python -m scripts.setup_database
```

## 6. Insert Seed Data

```powershell
python -m scripts.seed_database
```

## 7. Create Relationships

```powershell
python -m scripts.seed_relationships
```

## 8. Test Queries

```powershell
python -m scripts.test_queries
```

## 9. Run Application

```powershell
python -m streamlit run app/main.py
```

The application will be available through the Streamlit local URL.

## 🌐 Deployment

The application is deployed using **Streamlit Cloud**.

For deployment, database credentials are configured through **Streamlit Secrets** instead of `.env`.

```toml
COGNODB_URI = "your_uri"
COGNODB_USERNAME = "your_username"
COGNODB_PASSWORD = "your_password"
```

## Security

`.gitignore` should include:

```gitignore
.env
venv/
.venv/
__pycache__/
*.pyc
```