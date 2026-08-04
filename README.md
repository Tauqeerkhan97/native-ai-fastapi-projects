# Native AI FastAPI Projects 

Two production-style FastAPI backends built to practice real-world backend architecture: an agentic task management system and an internal documentation API — both with authentication, database integration, service-layer design, and automated tests.

## Projects in this repo

### 1. Agentic System (Enhanced)
A task-assignment backend for AI agents. Agents can be created, tasks defined, and tasks assigned to agents programmatically.

- **Agents & Tasks** — core entities with priority and type fields
- **Service layer** — `AgentService`, `TaskService` separate business logic from routes
- **Task assignment workflow** — assign any task to any agent via the service layer

### 2. Internal Documentation API (`doc-api`)
A backend for managing internal documents with user accounts.

- **User accounts** — with secure password hashing via `AuthService`
- **Documents** — create, own, and slug-based document management
- **Service layer** — `UserService`, `DocumentService`, `AuthService`

## Tech stack

- **FastAPI** — both APIs, with auto-generated interactive docs at `/docs`
- **SQLAlchemy-style ORM** — database models and sessions (`get_db()`)
- **Pydantic schemas** — request/response validation (`TaskCreate`, `DocumentCreate`, etc.)
- **Docker Compose** — run both services together
- **Python test scripts** — `run_tests.py`, `test_both_apps.py` verify imports, database operations, and core workflows for both apps

## Project structure

```
native-ai-fastapi-projects/
├── agentic-system-enhanced/
│   └── src/
│       ├── models.py
│       ├── database.py
│       ├── schemas.py
│       └── services/
│           ├── agent_service.py
│           └── task_service.py
├── doc-api/
│   └── src/
│       ├── models.py
│       ├── database.py
│       ├── schemas.py
│       └── services/
│           ├── auth_service.py
│           ├── user_service.py
│           └── document_service.py
├── docker-compose.yml
├── run_tests.py
├── test_both_apps.py
└── Exercise_1.2_Team_Architecture_Workshop.md
```

## Running locally

Clone the repo and set up each app independently, or use Docker Compose to run both together.

### With Docker (recommended)
```bash
docker-compose up --build
```

### Manually (per app)
```bash
cd agentic-system-enhanced
pip install -r requirements.txt
uvicorn src.main:app --reload
```
Visit `http://localhost:8000/docs` for the interactive API documentation.

Repeat the same steps inside `doc-api/` on a different port to run it alongside.

## Running tests

```bash
python test_both_apps.py
```
This verifies that both apps import correctly, connect to their databases, and complete a basic create-and-assign workflow end to end.

## What this project demonstrates

- Structuring a FastAPI backend with a proper **service layer** instead of putting logic directly in route handlers
- **Authentication fundamentals** — password hashing, user management
- Running **multiple independent services** from one repository with Docker Compose
- Writing **integration-style tests** that exercise real database operations, not just route responses


This project was built as part of a backend architecture exercise (see `Exercise_1.2_Team_Architecture_Workshop.md`) focused on designing scalable, team-friendly FastAPI systems.

This project is on journey
