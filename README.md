# FlyRank Assignment 2 – Task API

## Project Description

This project is a simple CRUD (Create, Read, Update, Delete) API built using FastAPI. The API manages a to-do list using in-memory storage.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Git
- GitHub

## Installation

Install the required packages:

```bash
pip install fastapi uvicorn
```

## Run the Project

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API information |
| GET | /health | Health check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{task_id} | Get a task by ID |
| POST | /tasks | Create a new task |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## Example curl Command

```bash
curl -i http://127.0.0.1:8000/tasks
```

## Swagger UI

Open:

```
http://127.0.0.1:8000/docs
```

A screenshot of the Swagger UI is included in this repository.