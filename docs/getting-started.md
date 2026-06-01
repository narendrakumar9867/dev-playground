# Getting Started

## Prerequisites
- Python 3.9 or higher
- pip

## How to run any example

Each folder is independent. Go into the folder, install its dependencies, and run.

```bash
# Example — backend folder
cd backend
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

## Folder overview

| Folder | What's inside |
|---|---|
| `ai/` | LLM, RAG, and agent experiments |
| `backend/` | FastAPI, REST patterns, service design |
| `databases/` | MongoDB, PostgreSQL, Redis examples |
| `realtime-systems/` | WebSockets, event-driven systems |
| `system-design/` | Architecture notes and design practice |
| `testing/` | pytest, unit and integration test examples |
| `authentication-security/` | Auth flows, JWT, security patterns |
| `devops-cloud/` | Docker, Kubernetes, deployment configs |

## Running tests

From the root folder:

```bash
pip install -r requirements.txt
pytest -v
```

## Linting

```bash
flake8 . --exclude=venv,.venv,__pycache__
```

## Adding a new example

1. Create a subfolder inside the relevant topic folder
2. Add your code files
3. Add a `requirements.txt` if new packages are needed
4. Add a `README.md` explaining what the example does and how to run it