# FlyRank Assignment 3 – Task API with SQLite

## Project Description

This project is a CRUD (Create, Read, Update, Delete) API built using FastAPI and SQLite. Unlike the previous assignment, tasks are stored in a SQLite database, so the data remains available even after restarting the server.

## Technologies Used

- Python
- FastAPI
- SQLite (sqlite3)
- Uvicorn
- Git
- GitHub

## Why SQLite?

SQLite was chosen because it is lightweight, requires no separate server, stores data in a single database file, and is easy to use for small backend applications.

## Database Location

The database file is stored in the project folder as:

```
tasks.db
```

## Installation

Install the required packages:

```bash
pip install fastapi uvicorn
```

## Run the Project

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API information |
| GET | /health | Health check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{task_id} | Get one task |
| POST | /tasks | Create a task |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## Example SQL Query

```sql
SELECT * FROM tasks;
```

## Screenshots

- Swagger UI screenshot
- SQLite database viewer screenshot