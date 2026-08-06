# 📄 Task API – PostgreSQL with Docker & PDF Report Generation

## 📌 Description

This project is a **FastAPI CRUD Task API** that uses **PostgreSQL** as its database. PostgreSQL runs inside **Docker**, and the application connects using environment variables.

The project also includes **PDF report generation** using **ReportLab**. Reports are generated **in the background** using FastAPI's `BackgroundTasks` and saved in the `reports/` folder.

---

## 🚀 Features

- ✅ Create tasks
- ✅ Read all tasks
- ✅ Read a task by ID
- ✅ Update tasks
- ✅ Delete tasks
- ✅ PostgreSQL database integration
- ✅ Docker & Docker Compose support
- ✅ PDF report generation
- ✅ Background task processing

---

## 🛠 Technologies Used

- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- psycopg
- ReportLab
- python-dotenv

---

## 📁 Project Structure

```text
flyRank-assignment-2/
│
├── reports/
│   └── report_YYYYMMDD_HHMMSS.pdf
│
├── main.py
├── pdf_generator.py
├── repository.py
├── docker-compose.yml
├── .env.example
├── README.md
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd flyRank-assignment-2
```

### 2. Create a `.env` file

Copy `.env.example` and update the values.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/tasks
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=tasks
```

### 3. Start PostgreSQL

```bash
docker compose up
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

### 6. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📚 API Endpoints

### Tasks

| Method | Endpoint |
|--------|----------|
| GET | `/tasks` |
| GET | `/tasks/{task_id}` |
| POST | `/tasks` |
| PUT | `/tasks/{task_id}` |
| DELETE | `/tasks/{task_id}` |

### Health Check

| Method | Endpoint |
|--------|----------|
| GET | `/health` |

### Reports

| Method | Endpoint |
|--------|----------|
| POST | `/reports` |

The `/reports` endpoint starts a **background task** that generates a PDF report and saves it in the `reports/` folder.

---

## 📄 PDF Report Generation

Each generated PDF report contains:

- Report title
- Date and time of generation
- Task information
- Task status (Done / Pending)

Generated reports are stored in:

```text
reports/
```

Example:

```text
reports/report_20260805_231537.pdf
```

---

## 💾 Data Persistence

Data persistence was verified by:

1. Creating tasks through the API.
2. Restarting the PostgreSQL Docker container.
3. Calling `GET /tasks`.
4. Confirming that previously created tasks remained available.

---

## ▶️ How to Generate a Report

1. Start PostgreSQL:

```bash
docker compose up
```

2. Run the FastAPI application:

```bash
uvicorn main:app --reload
```

3. Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

4. Execute:

```
POST /reports
```

5. The PDF report will be generated in the `reports/` folder.

---

## 👩‍💻 Author

**Minahil Saghir**

---

**FlyRank Backend Assignment**