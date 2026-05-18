# BotaniNavBack

Backend scaffold for a BotaniNav service.

## Project status

This repository currently contains the initial project structure, dependency list, and local service definitions (PostgreSQL/PostGIS and Redis).

## Repository structure

- `app/` – application package scaffold (routers, models, schemas, services)
- `tests/` – test package scaffold
- `docker-compose.yml` – local PostgreSQL/PostGIS and Redis services
- `requirements.txt` – pinned Python dependencies

## Prerequisites

- Python 3.11+ (recommended)
- Docker + Docker Compose (for local DB/Redis)

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start local services:
   ```bash
   docker compose up -d
   ```

## Running tests

```bash
pytest -q
```

## Notes

- `requirements.txt` is encoded as UTF-16 LE in the current repository state.
