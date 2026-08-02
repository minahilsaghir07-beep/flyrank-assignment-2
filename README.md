# Task API – PostgreSQL with Docker

## Description
This project is a FastAPI CRUD Task API using PostgreSQL as the database. PostgreSQL runs inside Docker, and the application connects to it using environment variables.

## Features
- Create tasks
- Read all tasks
- Read a task by ID
- Update tasks
- Delete tasks

## Technologies
- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- psycopg

## Setup

1. Clone the repository.
2. Create a `.env` file using `.env.example`.
3. Run:

```bash
docker compose up
```

4. Open:

```
http://127.0.0.1:8000/docs
```

## Environment Variables

Example (`.env.example`):

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/tasks
```

## Persistence

Data persistence was verified by:
1. Creating tasks through the API.
2. Restarting the Docker container.
3. Running `GET /tasks` and confirming the tasks were still present.

## API Endpoints

- GET `/tasks`
- GET `/tasks/{task_id}`
- POST `/tasks`
- PUT `/tasks/{task_id}`
- DELETE `/tasks/{task_id}`
- GET `/health`