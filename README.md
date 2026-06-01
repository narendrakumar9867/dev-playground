# Development Playground

This repository is my personal development playground for learning, practice, and small project experiments across backend, databases, AI, DevOps, and system design.

The idea is simple: keep related topics in separate folders and let each folder grow into its own runnable example or notes collection.

## Repository Layout

- [ai](ai/) - AI, LLM, RAG, and agent experiments
- [authentication-security](authentication-security/) - auth and security patterns
- [backend](backend/) - backend practice and service design
- [databases](databases/) - database-specific examples and configs
- [devops-cloud](devops-cloud/) - Docker, cloud, and deployment notes
- [realtime-systems](realtime-systems/) - realtime and event-driven systems
- [system-design](system-design/) - architecture notes and design practice
- [testing](testing/) - testing strategies and examples

## How to Run a Folder

Each folder is independent. Go into the specific example folder, create a virtual environment, install its dependencies, and run.

Example for the MongoDB folder on Windows:

```powershell
cd databases\mongodb
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Example on Mac/Linux:

```bash
cd databases/mongodb
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## How This Repo Is Organized

- Each topic has its own top-level folder.
- Each example inside a topic has its own subfolder with its own `requirements.txt` and `README.md`.
- No shared root dependencies — every example is self-contained.

## What This Repo Is For

- practicing real-world project structure
- learning by building small focused examples
- collecting reusable patterns for backend, database, and cloud work
- keeping experiments organized instead of mixing everything together

## Contributing

If you want to add something, read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## Notes

- Some folders are still empty and will grow over time.
- The repo is intentionally organized by topic so each area can remain focused.

## Thank you !!