# Development Playground

This repository is my personal development playground for learning, practice, and small project experiments across backend, frontend, databases, AI, DevOps, and system design.

The idea is simple: keep related topics in separate folders and let each folder grow into its own runnable example or notes collection.

## Repository Layout

- [ai](ai/) - AI, LLM, RAG, and agent experiments
- [authentication-security](authentication-security/) - auth and security patterns
- [backend](backend/) - backend practice and service design
- [databases](databases/) - database-specific examples and configs
- [devops-cloud](devops-cloud/) - Docker, cloud, and deployment notes
- [frontend](frontend/) - frontend experiments and UI work
- [realtime-systems](realtime-systems/) - realtime and event-driven systems
- [system-design](system-design/) - architecture notes and design practice
- [testing](testing/) - testing strategies and examples

### How to run a separate folder

Each topic folder is independent. To run one folder, go into that folder, install only its local dependencies, and start the entry file from there.

Example for the MongoDB folder on Windows:

```powershell
cd databases\mongodb
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## How To Use The Repo

Each folder can be treated independently.

- Keep code and notes for one topic inside the matching folder.
- Add a local `requirements.txt` when a folder contains a Python app.
- Prefer folder-level setup so each example stays easy to run and understand.


## What This Repo Is For

- practicing real-world project structure
- learning by building small focused examples
- collecting reusable patterns for backend, database, and cloud work
- keeping experiments organized instead of mixing everything together

## Contributing

If you want to add something new, read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## Notes

- Some folders are still empty and will grow over time.
- The repo is intentionally organized by topic so each area can remain focused.

## Thank you !!