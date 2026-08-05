# 📄 Task API – PostgreSQL with Docker & PDF Report Generation

## 📌 Description

This project is a **FastAPI CRUD Task API** that uses **PostgreSQL** as the database. PostgreSQL runs inside **Docker**, and the application connects to it using environment variables.

The project also includes **PDF report generation** using **ReportLab**. Reports are generated **as background tasks** and saved in the `reports/` folder.

---

# 🚀 Features

- ✅ Create tasks
- ✅ Read all tasks
- ✅ Read a task by ID
- ✅ Update tasks
- ✅ Delete tasks
- ✅ PostgreSQL database
- ✅ Docker support
- ✅ PDF report generation
- ✅ Background report generation using FastAPI `BackgroundTasks`

---

# 🛠 Technologies Used

- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- psycopg
- ReportLab
- python-dotenv

---

# 📦 Setup

## 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd flyRank-assignment-2
```

## 2️⃣ Create the Environment File

Create a `.env` file using `.env.example`.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/tasks
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=tasks
```

## 3️⃣ Start PostgreSQL

```bash
docker compose up
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 5️⃣ Run the FastAPI Application

```bash
uvicorn main:app --reload
```

## 6️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📚 API Endpoints

## 📝 Tasks

| Method | Endpoint |
|--------|----------|
| GET | `/tasks` |
| GET | `/tasks/{task_id}` |
| POST | `/tasks` |
| PUT | `/tasks/{task_id}` |
| DELETE | `/tasks/{task_id}` |

---

## ❤️ Health Check

| Method | Endpoint |
|--------|----------|
| GET | `/health` |

---

## 📄 Reports

| Method | Endpoint |
|--------|----------|
| POST | `/reports` |

This endpoint generates a **PDF report** in the **background** and saves it inside the `reports/` folder.

---

# 📄 PDF Report Generation

Each generated report includes:

- Report title
- Generation date & time
- All tasks stored in PostgreSQL
- Task status (Done / Pending)

Generated reports are saved inside:

```text
reports/
```

Example:

```text
reports/report_20260805_230231.pdf
```

---

# 💾 Data Persistence

Data persistence was verified by:

1. Creating tasks through the API.
2. Restarting the PostgreSQL Docker container.
3. Running `GET /tasks`.
4. Confirming that all previously created tasks were still available.

---

# 📁 Project Structure

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
├── .env
├── .env.example
├── README.md
└── requirements.txt
```

---

# ▶️ How to Generate a Report

1. Start PostgreSQL:

```bash
docker compose up
```

2. Run the FastAPI server:

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

5. A PDF report will be generated automatically in the `reports/` folder.

---

# 👩‍💻 Author

**Minahil Saghir**

---
**FlyRank Backend Assignment**